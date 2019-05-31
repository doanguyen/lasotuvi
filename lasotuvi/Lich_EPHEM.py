# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.

Module tính lịch sử dụng thư viện PyEphem  <http://rhodesmill.org/pyephem/>

I. Đổi lịch dương sang âm
1. xác định có phải năm nhuận hay ko? Bằng cách:
    Ví dụ năm cần xác định là 1984,
    tìm Sóc A (ngay trước Đông chí 1983) và Sóc B (ngay trước Đông chí 1984).
    Nếu khoảng cách giữa Sóc A và Sóc B lớn hơn 365 ngày thì năm 1984
    là năm nhuận.
"""
import types
from datetime import date, datetime
from itertools import tee
from math import floor
from typing import Tuple, Optional, Union, List

import ephem

from lasotuvi.ErrorHandling import InputInvalidate



def find_lunar_month_between(previousWinterSolstice, nextWinterSolstice):
    pass


def s2l(solar_datetime: ephem.Date, timezone: Optional[int] = 7,
        location: Optional[ephem.Observer] = None) -> Tuple[ephem.Date, bool]:
    """
    Chuyển đổi từ ngày dương lịch sang âm lịch
    @param solar_datetime: ngày,tháng năm giờ dương lịch
    @param timezone: giá trị của timezone, Việt nam là 7 (optional)
    @param location: địa điểm, bao gồm lon,lat (hiện tại vẫn chưa thực hiện phần này)
    @return List bao gồm ngày tháng năm và có phải tháng nhuận hay không

    Ví dụ:
    hanoi = ephem.Observer()
    hanoi.lon, hanoi.lat = '105.834160', '21.027764'

    ngaysinh = ephem.Date('1984/05/30 16:23:45.12')  # sinh ngày 30 tháng 5 năm 1984, vào 16 giờ 23 phút 45.12 giây

    amlich = s2l(solar_date=ngaysinh, location=hanoi)
    """
    if isinstance(solar_datetime, date) or isinstance(solar_datetime, datetime):
        solar_datetime = ephem.Date(solar_datetime)
    elif isinstance(solar_datetime, ephem.Date) is False:
        raise InputInvalidate("Input is not a ephem.Date instance")

    if location:
        raise NotImplemented

    lunar_hour = solar_datetime.datetime().hour

    lunar_day = find_lunar_day(solar_datetime, timezone, location)

    lunar_month, lunar_leap = find_lunar_month(
        solar_datetime, timezone, location)

    lunar_year = find_lunar_year(solar_datetime, timezone, location)

    lunar_datetime = ephem.Date(
        datetime(lunar_year, lunar_month, lunar_day, lunar_hour))

    return lunar_datetime, lunar_leap


def find_lunar_year(solar_datetime: ephem.Date, timezone: int = None, location: ephem.Observer = None):
    if (solar_datetime - ephem.previous_winter_solstice(solar_datetime) < 4 * 29.5) \
            and solar_datetime.datetime().month >= 11:
        return solar_datetime.datetime().year - 1
    return solar_datetime.datetime().year


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def lunar_month_without_major_term(list_major_terms: List, list_lunar_month_beginning: List) -> Optional[List]:
    month_without_major_term = None
    for early_month, end_of_month in pairwise(list_lunar_month_beginning):
        major_term_inside_lunar_month = False
        for major_term in list_major_terms:
            if (major_term - early_month) * (major_term - end_of_month) < 0:
                # print("Major term %s inside lunar month %s and %s" % (major_term, early_month, end_of_month))
                major_term_inside_lunar_month = True
                break

        if not major_term_inside_lunar_month:
            month_without_major_term = [early_month, end_of_month]
            # print("Month lack major term:", early_month, end_of_month)
            break
    return month_without_major_term


def find_lunar_month(solar_datetime, timzone: int = None, location: ephem.Observer = None) -> Tuple[int, bool]:
    if location:
        raise NotImplemented
    leap_month = False
    previous_winter_solstice = ephem.previous_winter_solstice(solar_datetime)
    lunar_day_diff = (
            solar_datetime - ephem.previous_new_moon(previous_winter_solstice))
    # print("Lunar day diff", lunar_day_diff, "days")
    lunar_month = floor(lunar_day_diff / 29.5) + 11

    if is_leap_year(solar_datetime):
        solar_year_beginning = ephem.Date(
            datetime(solar_datetime.datetime().year, 1, 1, 0, 0))
        lunar_year_beginning = ephem.previous_new_moon(
            ephem.previous_winter_solstice(solar_year_beginning))
        lunar_year_end = ephem.previous_new_moon(
            ephem.next_winter_solstice(solar_year_beginning))
        list_major_terms = find_solar_terms_between(
            lunar_year_beginning, lunar_year_end)
        list_lunar_month_beginning = find_new_moon_between(
            lunar_year_beginning, lunar_year_end)
        month_without_major_term = lunar_month_without_major_term(
            list_major_terms, list_lunar_month_beginning)

        if month_without_major_term:
            early_month, end_of_month = month_without_major_term
            leap_month_diff = (early_month - lunar_year_beginning)
            if leap_month_diff >= 3 * 30:
                leap_month = floor(leap_month_diff / 30) - 1
            if lunar_day_diff > leap_month_diff:
                lunar_month -= 1

    if lunar_month > 12:
        lunar_month -= 12

    return lunar_month, leap_month == lunar_month


def correct_local_time(solar_datetime: ephem.Date, timezone: int = None,
                       location: Optional[ephem.Observer] = None) -> ephem.Date:
    if timezone:
        # so we are working in the correct timezone
        solar_datetime += timezone * ephem.hour
    if location:
        location.date = solar_datetime
        solar_datetime = location.sidereal_time()
    return ephem.Date(solar_datetime)


def find_lunar_day(local_datetime: ephem.Date, timezone: int = None, location: ephem.Observer = None) -> int:
    """
    Tìm ngày âm lịch của ngày dương lịch đã cho.
    :param local_datetime: ephem.Date
    :param timezone: int
    :param location: ephem.Observer
    :return: int
    """
    previous_new_moon = ephem.previous_new_moon(local_datetime)
    if timezone:
        previous_new_moon += (timezone * ephem.hour)
    if location:
        raise NotImplemented
    lunar_day = floor(local_datetime - ephem.Date(previous_new_moon)) + 1
    return lunar_day


def is_leap_year(solar_date: ephem.Date) -> bool:
    """
    :param solar_date: ephem.Date
    :return: is_leap: bool  trả về kết quả dưới dạng boolean xem năm đó có phải là năm nhuận hay không
    """
    return day_in_lunar_year(solar_date) > 365


def day_in_lunar_year(solar_date: ephem.Date) -> Union[float, int]:
    """
    Xác định số ngày trong năm ÂM LỊCH (Năm âm lịch bắt đầu từ thời điểm Sóc của Đông chí trước đó tới Sóc của Đông chí
    kế tiếp
    :param solar_date: ephem.Date
    :return: số ngày int
    """
    if isinstance(solar_date, int):
        raise InputInvalidate(
            "input không được định dạng INT, khi đó ephem sẽ hoạt động không chính xác!"
            " Thử với ephem.Date('2001') == ephem.Date(2001)")
    if isinstance(solar_date, ephem.Date) is False:
        solar_date = ephem.Date(solar_date)

    working_year = str(solar_date.datetime().year)  # Khởi nguồn từ đầu năm

    # xác định ngày đông chí năm trước
    previous_winter_solstice = ephem.previous_winter_solstice(working_year)
    # xác định ngày đông chí năm gần nhất
    next_winter_solstice = ephem.next_winter_solstice(working_year)

    day_in_lunar_year = ephem.previous_new_moon(next_winter_solstice) - ephem.previous_new_moon(
        previous_winter_solstice)
    return day_in_lunar_year


def l2s(amlich: LUNAR_contract, location: ephem.Observer) -> LUNAR_contract:
    return amlich


def find_new_moon_between(start_date: ephem.Date, end_date: ephem.Date) -> list:
    new_moon = []
    while start_date < end_date:
        new_moon_position = ephem.next_new_moon(start_date)
        new_moon.append(new_moon_position)
        start_date += 30
    return new_moon


def find_solar_terms_between(start_date: ephem.Date, end_date: ephem.Date) -> list:
    solar_terms = []
    for degree in range(0, 360, 30):
        term = when_is_sun_at_degrees_longitude(start_date, degree)
        if term < end_date:
            solar_terms.append(term)
    return solar_terms


def when_is_sun_at_degrees_longitude(given_date: date, degrees: int) -> ephem.Date:
    # Thanks to Brandon Rhode @ https://answers.launchpad.net/pyephem/+question/110832
    # Find out the sun's current longitude.

    sun = ephem.Sun(given_date)
    current_longitude = sun.hlong - ephem.pi

    # Find approximately the right time of year.

    target_longitude = degrees * ephem.degree
    difference = (target_longitude - current_longitude) % ephem.twopi
    t0 = given_date + 365.25 * difference / ephem.twopi

    # Zero in on the exact moment.

    def f(t):
        sun.compute(t)
        longitude = sun.hlong - ephem.pi
        return ephem.degrees(target_longitude - longitude).znorm

    return ephem.Date(ephem.newton(f, t0, t0 + ephem.minute))
