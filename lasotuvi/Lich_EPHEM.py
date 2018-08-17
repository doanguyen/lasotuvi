# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.

Module tính lịch sử dụng thư viện PyEphem  <http://rhodesmill.org/pyephem/>

I. Đổi lịch dương sang âm
1. xác định có phải năm nhuận hay ko? Bằng cách:
    Ví dụ năm cần xác định là 1984, tìm Sóc A (ngay trước Đông chí 1983) và Sóc B (ngay trước Đông chí 1984). Nếu khoảng cách giữa Sóc A và Sóc B lớn hơn 365 ngày thì năm 1984 là năm nhuận.

"""

from datetime import date, datetime
from math import ceil
from typing import Tuple, Optional, Union

import ephem

from lasotuvi.ErrorHandling import InputInvalidate

LUNAR_contract = Tuple[ephem.Date, int]  # [date, thang_nhuan]


def find_lunar_month_between(previousWinterSolstice, nextWinterSolstice):
    pass


def s2l(solar_datetime: ephem.Date, timezone: Optional[int] = 7,
        location: Optional[ephem.Observer] = None) -> LUNAR_contract:
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

    if location:
        raise NotImplemented

    lunar_leap = False

    solar_datetime = correct_local_time(solar_datetime, timezone)

    lunar_day = find_lunar_day(solar_datetime)

    lunar_month = int(ceil((solar_datetime - ephem.previous_winter_solstice(solar_datetime)) / 29.5) - 2)

    # if is_leap_year(solar_date):

    lunar_year = solar_datetime.datetime().year
    print(date(lunar_year, lunar_month, lunar_day))
    return Tuple[ephem.Date(), lunar_leap]


def correct_local_time(solar_datetime: ephem.Date, timezone: Optional[ephem.Observer],
                       location: Optional[ephem.Observer]):
    if timezone is not None:
        solar_datetime += timezone * ephem.hour  # so we are working in the correct timezone
    if location:
        location.date = solar_datetime
        solar_datetime = location.sidereal_time()
    return solar_datetime


def find_lunar_day(local_datetime: ephem.Date, timezone: int = None, location: ephem.Observer = None) -> int:
    previous_new_moon = ephem.previous_new_moon(local_datetime)
    if timezone:
        previous_new_moon += (timezone * ephem.hour)
    if location:
        raise NotImplemented
    lunar_day = local_datetime.datetime().day - new_moon.day + 1
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
    newMoon = []
    while start_date < end_date:
        newMoon.append(ephem.next_new_moon(start_date))
        start_date += 29.5
    return newMoon


def find_solar_terms_between(start_date: ephem.Date, end_date: ephem.Date) -> list:
    solar_terms = []
    for degree in range(0, 330, 30):
        term = when_is_sun_at_degrees_longitude(start_date, degree)
        if term < end_date:
            solar_terms.append(term)
    return solar_terms


def when_is_sun_at_degrees_longitude(date: date, degrees: int) -> ephem.Date:
    # Thanks to Brandon Rhode @ https://answers.launchpad.net/pyephem/+question/110832
    # Find out the sun's current longitude.

    sun = ephem.Sun(date)
    current_longitude = sun.hlong - ephem.pi

    # Find approximately the right time of year.

    target_longitude = degrees * ephem.degree
    difference = (target_longitude - current_longitude) % ephem.twopi
    t0 = date + 365.25 * difference / ephem.twopi

    # Zero in on the exact moment.

    def f(t):
        sun.compute(t)
        longitude = sun.hlong - ephem.pi
        return ephem.degrees(target_longitude - longitude).znorm

    return ephem.Date(ephem.newton(f, t0, t0 + ephem.minute))
