# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from enum import Enum, unique
from typing import Optional

from lasotuvi import AmDuong
from lasotuvi.Hanh import Hanh

int_or_none = Optional[int]
str_or_none = Optional[str]


@unique
class Tinh(Enum):
    """
    1: Chính tinh, 2: Phụ tinh nói chung
    3: Quý tinh, 4: Quyền tinh, 5: Phúc tinh, 6: Văn tinh
    7: Đài các tinh, 8: Đào hoa tinh

    11: Sát tinh, 12: Bại tinh, 13: Ám tinh, 14: Dâm tinh,
    15: Hình tinh, 16: Ác Tinh
    """

    CHINH_TINH = 1
    PHU_TINH = 2
    QUY_TINH = 3
    QUYEN_TINH = 4

    PHUC_TINH = 5
    VAN_TINH = 6
    DAI_CAC_TINH = 7
    DAO_HOA_TINH = 8
    SAT_TINH = 11
    BAI_TINH = 12
    AM_TINH = 13
    DAM_TINH = 14
    HINH_TINH = 15
    AC_TINH = 16


class Sao:
    # Thành phần cơ bản trong tử vi. Tính chất của 1 sao cơ bản bao gồm:
    # id: int
    # ten: str
    # hanh: Hanh
    # loai: Tinh
    # phuong_vi: str
    # am_duong: AmDuong
    # vong_trang_sinh: bool
    pass


class TuVi(Sao):
    id = 1
    ten = "Tử vi"
    hanh = Hanh.THO
    loai = Tinh.CHINH_TINH.value
    phuong_vi = "Đế tinh"
    am_duong = AmDuong.DUONG
    vong_trang_sinh = 0


class LiemTrinh(Sao):
    id = 2
    ten = "Liêm trinh"
    hanh = Hanh.HOA
    loai = Tinh.CHINH_TINH.value
    phuong_vi = "Bắc đẩu tinh"
    am_duong = AmDuong.DUONG
    vong_trang_sinh = 0


class ThienDong(Sao):
    # saoThienDong = Sao(3, "Thiên đồng", "T", 1, "Bắc đẩu tinh", 1, 0)
    id = 3
    ten = "Thiên đồng"
    hanh = Hanh.THUY
    loai = Tinh.CHINH_TINH
    phuong_vi = "Bắc đẩu tinh"
    am_duong = AmDuong.DUONG
    vong_trang_sinh = 0


class VuKhuc(Sao):
    # saoVuKhuc = Sao(4, "Vũ khúc", "K", 1, "Bắc đẩu tinh", -1, 0)
    id = 4
    ten = "Vũ khúc"
    hanh = Hanh.KIM
    loai = Tinh.CHINH_TINH
    phuong_vi = "Bắc đẩu tinh"
    am_duong = AmDuong.AM
    vong_trang_sinh = 0


class ThaiDuong(Sao):
    # saoThaiDuong = Sao(5, "Thái Dương", "H", 1, "Nam đẩu tinh", 1, 0)
    id = 5
    ten = "Thái Dương"
    hanh = Hanh.HOA
    loai = Tinh.CHINH_TINH
    phuong_vi = "Nam đẩu tinh"
    am_duong = AmDuong.DUONG


class ThienCo(Sao):
    # saoThienCo = Sao(6, "Thiên cơ", "M", 1, "Nam đẩu tinh", -1, 0)
    id = 6
    ten = "Thiên Cơ"
    hanh = Hanh.MOC
    loai = Tinh.CHINH_TINH
    phuong_vi = "Nam đẩu tinh"
    am_duong = AmDuong.AM
    vong_trang_sinh = 0


class ThienPhu(Sao):
    id = 7
    ten = "Thiên Phủ"
    hanh = Hanh.O
    loai = Tinh.CHINH_TINH
    phuong_vi = "Nam đẩu tinh"
    am_duong = AmDuong.DUONG
    vong_trang_sinh = 0


class ThaiAm(Sao):
    # saoThaiAm = Sao(8, "Thái âm", "T", 1, "Bắc đẩu tinh", -1, 0)
    id = 8
    ten = "Thái Âm"
    hanh = Hanh.T
    loai = Tinh.CHINH_TINH
    phuong_vi = "Bắc đẩu tinh"
    am_duong = AmDuong.AM
    vong_trang_sinh = 0


class ThamLang(Sao):
    # saoThamLang = Sao(9, "Tham lang", "T", 1, "Bắc đẩu tinh", -1, 0)
    id = 9
    ten = "Tham Lang"
    hanh = Hanh.T
    loai = Tinh.CHINH_TINH
    phuong_vi = "Bắc đẩu tinh"
    am_duong = AmDuong.AM


class CuMon(Sao):
    # saoCuMon = Sao(10, "Cự môn", "T", 1, "Bắc đẩu tinh", -1, 0)
    id = 10
    ten = "Cự Môn"
    hanh = Hanh.T
    loai = Tinh.CHINH_TINH
    phuong_vi = "Bắc đẩu tinh"
    am_duong = AmDuong.AM
    vong_trang_sinh = 0


class ThienTuong(Sao):
    # saoThienTuong = Sao(11, "Thiên tướng", "T", 1, "Nam đẩu tinh", 1, 0)
    id = 11
    ten = "Thiên Tướng"
    hanh = Hanh.T
    loai = Tinh.CHINH_TINH
    phuong_vi = "Nam đấu tinh"
    am_duong = AmDuong.DUONG
    vong_trang_sinh = 0


class ThienLuong(Sao):
    # saoThienLuong = Sao(12, "Thiên lương", "M", 1, "Nam đẩu tinh", -1, 0)
    id = 12
    ten = "Thiên Lương"
    hanh = Hanh.M
    loai = Tinh.CHINH_TINH
    phuong_vi = "Nam đẩu tinh"
    am_duong = AmDuong.AM
    vong_trang_sinh = 0


class ThatSat(Sao):
    # saoThatSat = Sao(13, "Thất sát", "K", 1, "Nam đẩu tinh", 1, 0)
    id = 13
    ten = "Thất Sát"
    hanh = Hanh.K
    loai = Tinh.CHINH_TINH
    phuong_vi = "Nam đẩu tinh"
    am_duong = AmDuong.DUONG
    vong_trang_sinh = 0


class PhaQuan(Sao):
    # saoPhaQuan = Sao(14, "Phá quân", "T", 1, "Bắc đẩu tinh", -1, 0)
    id = 14
    ten = "Phá Quân"
    hanh = Hanh.T
    loai = Tinh.CHINH_TINH
    phuong_vi = "Bắc đẩu tinh"
    am_duong = AmDuong.AM
    vong_trang_sinh = 0


# # Vòng Địa chi - Thái tuế
class ThaiTue(Sao):
    # saoThaiTue = Sao(15, "Thái tuế", "H", 15, "", 0)
    id = 15
    ten = "Thái Tuế"
    hanh = Hanh.H
    loai = Tinh.HINH_TINH
    vong_trang_sinh = 0


class ThieuDuong(Sao):
    # saoThieuDuong = Sao(16, "Thiếu dương", "H", 5)
    id = 16
    ten = "Thiếu Dương"
    hanh = Hanh.H
    loai = Tinh.PHU_TINH


# saoTangMon = Sao(17, "Tang môn", "M", 12)
class TangMon(Sao):
    id = 17
    ten = "Tang Môn"
    hanh = Hanh.M
    loai = Tinh.BAI_TINH


# saoThieuAm = Sao(18, "Thiếu âm", "T", 5)
class ThieuAm(Sao):
    id = 18
    ten = "Thiếu Âm"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH


# saoQuanPhu3 = Sao(19, "Quan phù", "H", 12)
class QuanPhu3(Sao):  # QuanPhu3 để tránh conflict với QuanPhu2
    id = 19
    ten = "Quan Phù"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH


# saoTuPhu = Sao(20, "Tử phù", "K", 12)
class TuPhu(Sao):
    id = 20
    ten = "Tử Phù"
    hanh = Hanh.K
    loai = Tinh.BAI_TINH


# saoTuePha = Sao(21, "Tuế phá", "H", 12)
class TuePha(Sao):
    id = 21
    ten = "Tuế Phá"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH


# saoLongDuc = Sao(22, "Long đức", "T", 5)
class LongDuc(Sao):
    id = 22
    ten = "Long Đức"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH


# saoBachHo = Sao(23, "Bạch hổ", "K", 12)
class BachHo(Sao):
    id = 23
    ten = "Bạch Hổ"
    hanh = Hanh.K
    loai = Tinh.BAI_TINH


# saoPhucDuc = Sao(24, "Phúc đức", "O", 5)
class PhucDuc(Sao):
    id = 24
    ten = "Phúc Đức"
    hanh = Hanh.O
    loai = Tinh.PHUC_TINH


# saoDieuKhach = Sao(25, "Điếu khách", "H", 12)
class DieuKhach(Sao):
    id = 25
    ten = "Điều Khách"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH


# saoTrucPhu = Sao(26, "Trực phù", "K", 16)
class TrucPhu(Sao):
    id = 26
    ten = "Trực Phù"
    hanh = Hanh.K
    loai = Tinh.AC_TINH


# #  Vòng Thiên can - Lộc tồn
# saoLocTon = Sao(27, "Lộc tồn", "O", 3, "Bắc đẩu tinh")
class LocTon(Sao):
    id = 27
    ten = "Lộc Tồn"
    hanh = Hanh.O
    loai = Tinh.QUY_TINH
    phuong_vi = "Bắc Đẩu Tinh"


# saoBacSy = Sao(109, "Bác sỹ", "T", 5, )
class BacSy(Sao):
    id = 109
    ten = "Bác Sỹ"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH


# saoLucSi = Sao(28, "Lực sĩ", "H", 2)
class LucSi(Sao):
    id = 28
    ten = "Lực Sĩ"
    hanh = Hanh.H
    loai = Tinh.PHU_TINH


# saoThanhLong = Sao(29, "Thanh long", "T", 5)
class ThanhLong(Sao):
    id = 29
    ten = "Thanh Long"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH


# saoTieuHao = Sao(30, "Tiểu hao", "H", 12)
class TieuHao(Sao):
    id = 30
    ten = "Tiểu Hao"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH


# saoTuongQuan = Sao(31, "Tướng quân", "M", 4)
class TuongQuan(Sao):
    id = 31
    ten = "Tướng Quân"
    hanh = Hanh.M
    loai = Tinh.QUYEN_TINH


# saoTauThu = Sao(32, "Tấu thư", "K", 3)
class TauThu(Sao):
    id = 32
    ten = "Tấu Thư"
    hanh = Hanh.K
    loai = Tinh.QUY_TINH


# saoPhiLiem = Sao(33, "Phi liêm", "H", 2)
class PhiLiem(Sao):
    id = 33
    ten = "Phi Liêm"
    hanh = Hanh.H
    loai = Tinh.PHU_TINH


# saoHyThan = Sao(34, "Hỷ thần", "H", 5)
class HyThan(Sao):
    id = 34
    ten = "Hỷ Thần"
    hanh = Hanh.H
    loai = Tinh.PHUC_TINH


# saoBenhPhu = Sao(35, "Bệnh phù", "O", 12)
class BenhPhu(Sao):
    id = 35
    ten = "Bệnh Phù"
    hanh = Hanh.O
    loai = Tinh.BAI_TINH


# saoDaiHao = Sao(36, "Đại hao", "H", 12)
class DaiHao(Sao):
    id = 36
    ten = "Đại Hao"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH


# saoPhucBinh = Sao(37, "Phục binh", "H", 13)
class PhucBinh(Sao):
    id = 37
    ten = "Phục Binh"
    hanh = Hanh.H
    loai = Tinh.AM_TINH


# saoQuanPhu2 = Sao(38, "Quan phù", "H", 12)
class QuanPhu2(Sao):
    id = 38
    ten = "Quan Phù"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH


# # Vòng Tràng sinh
# saoTrangSinh = Sao(39, "Tràng sinh", "T", 5, vongTrangSinh=1)
class TrangSinh(Sao):
    id = 39
    ten = "Tràng Sinh"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH
    vong_trang_sinh = 1


# saoMocDuc = Sao(40, "Mộc dục", "T", 14, vongTrangSinh=1)
class MocDuc(Sao):
    id = 40
    ten = "Mộc Dục"
    hanh = Hanh.T
    loai = Tinh.DAM_TINH
    vong_trang_sinh = 1


# saoQuanDoi = Sao(41, "Quan đới", "K", 4, vongTrangSinh=1)
class QuanDoi(Sao):
    id = 41
    ten = "Quan Đới"
    hanh = Hanh.K
    loai = Tinh.QUYEN_TINH
    vong_trang_sinh = 1


# saoLamQuan = Sao(42, "Lâm quan", "K", 7, vongTrangSinh=1)
class LamQuan(Sao):
    id = 42
    ten = "Lâm Quan"
    hanh = Hanh.K
    loai = Tinh.DAI_CAC_TINH
    vong_trang_sinh = 1


# saoDeVuong = Sao(43, "Đế vượng", "K", 5, vongTrangSinh=1)
class DeVuong(Sao):
    id = 43
    ten = "Đế Vượng"
    hanh = Hanh.K
    loai = Tinh.PHUC_TINH
    vong_trang_sinh = 1


# saoSuy = Sao(44, "Suy", "T", 12, vongTrangSinh=1)
class Suy(Sao):
    id = 44
    ten = "Suy"
    hanh = Hanh.T
    loai = Tinh.BAI_TINH
    vong_trang_sinh = 1


# saoBenh = Sao(45, "Bệnh", "H", 12, vongTrangSinh=1)
class Benh(Sao):
    id = 45
    ten = "Bệnh"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH
    vong_trang_sinh = 1


# saoTu = Sao(46, "Tử", "H", 12, vongTrangSinh=1)
class Tu(Sao):
    id = 46
    ten = "Tử"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH
    vong_trang_sinh = 1


# saoMo = Sao(47, "Mộ", "O", vongTrangSinh=1)
class Mo(Sao):
    id = 47
    ten = "Mộ"
    hanh = Hanh.O
    vong_trang_sinh = 1


# saoTuyet = Sao(48, "Tuyệt", "O", 12, vongTrangSinh=1)
class Tuyet(Sao):
    id = 48
    ten = "Tuyệt"
    hanh = Hanh.O
    loai = Tinh.BAI_TINH
    vong_trang_sinh = 1


# saoThai = Sao(49, "Thai", "O", 14, vongTrangSinh=1)
class Thai(Sao):
    id = 49
    ten = "Thai"
    hanh = Hanh.O
    loai = Tinh.DAM_TINH
    vong_trang_sinh = 1


# saoDuong = Sao(50, "Dưỡng", "M", 2, vongTrangSinh=1)
class Duong(Sao):
    id = 50
    ten = "Dưỡng"
    hanh = Hanh.M
    loai = Tinh.PHU_TINH
    vong_trang_sinh = 1


# # Lục sát
# #    Kình dương đà la
# saoDaLa = Sao(51, "Đà la", "K", 11)
class DaLa(Sao):
    id = 51
    ten = "Đà La"
    hanh = Hanh.K
    loai = Tinh.SAT_TINH


# saoKinhDuong = Sao(52, "Kình dương", "K", 11)
class KinhDuong(Sao):
    id = 52
    ten = "Kình Dương"
    hanh = Hanh.K
    loai = Tinh.SAT_TINH


#
# #    Địa không - Địa kiếp
# saoDiaKhong = Sao(53, "Địa không", "H", 11)
class DiaKhong(Sao):
    id = 53
    ten = "Địa Không"
    hanh = Hanh.H
    loai = Tinh.SAT_TINH


# saoDiaKiep = Sao(54, "Địa kiếp", "H", 11)
class DiaKiep(Sao):
    id = 54
    ten = "Địa Kiếp"
    hanh = Hanh.H
    loai = Tinh.SAT_TINH


# #    Hỏa tinh - Linh tinh
# saoLinhTinh = Sao(55, "Linh tinh", "H", 11)
class LinhTinh(Sao):
    id = 55
    ten = "Linh Tinh"
    hanh = Hanh.H
    loai = Tinh.SAT_TINH


# saoHoaTinh = Sao(56, "Hỏa tinh", "H", 11)
class HoaTinh(Sao):
    id = 56
    ten = "Hỏa Tinh"
    hanh = Hanh.H
    loai = Tinh.SAT_TINH


#
# # Sao Âm Dương
# #    Văn xương - Văn khúc
# saoVanXuong = Sao(57, "Văn xương", "K", 6)
class VanXuong(Sao):
    id = 57
    ten = "Văn Xương"
    hanh = Hanh.K
    loai = Tinh.VAN_TINH


# saoVanKhuc = Sao(58, "Văn Khúc", "T", 6)
class VanKhuc(Sao):
    id = 58
    ten = "Văn Khúc"
    hanh = Hanh.T
    loai = Tinh.VAN_TINH


#
# #    Thiên khôi - Thiên Việt
# saoThienKhoi = Sao(59, "Thiên khôi", "H", 6)
class ThienKhoi(Sao):
    id = 59
    ten = "Thiên Khôi"
    hanh = Hanh.H
    loai = Tinh.VAN_TINH


# saoThienViet = Sao(60, "Thiên việt", "H", 6)
class ThienViet(Sao):
    id = 60
    ten = "Thiên Việt"
    hanh = Hanh.H
    loai = Tinh.VAN_TINH


#
# #    Tả phù - Hữu bật
# saoTaPhu = Sao(61, "Tả phù", "O", 2)
class TaPhu(Sao):
    id = 61
    ten = "Tả Phù"
    hanh = Hanh.O
    loai = Tinh.PHU_TINH


# saoHuuBat = Sao(62, "Hữu bật", "O", 2)
class HuuBat(Sao):
    id = 62
    ten = "Hữu Bật"
    hanh = Hanh.O
    loai = Tinh.PHU_TINH


#
# #    Long trì - Phượng các
# saoLongTri = Sao(63, "Long trì", "T", 3)
class LongTri(Sao):
    id = 63
    ten = "Long Trì"
    hanh = Hanh.T
    loai = Tinh.QUY_TINH


# saoPhuongCac = Sao(64, "Phượng các", "O", 3)
class PhuongCat(Sao):
    id = 64
    ten = "Phượng Cát"
    hanh = Hanh.O
    loai = Tinh.QUY_TINH


#
# #    Tam thai - Bát tọa
# saoTamThai = Sao(65, "Tam thai", "M", 7)
class TamThai(Sao):
    id = 65
    ten = "Tam Thai"
    hanh = Hanh.M
    loai = Tinh.DAI_CAC_TINH


# saoBatToa = Sao(66, "Bát tọa", "T", 7)
class BatToa(Sao):
    id = 66
    ten = "Bát Tọa"
    hanh = Hanh.T
    loai = Tinh.DAI_CAC_TINH


#
# #    Ân quang - Thiên quý
# saoAnQuang = Sao(67, "Ân quang", "M", 3)
class AnQuang(Sao):
    id = 67
    ten = "Ân Quang"
    hanh = Hanh.M
    loai = Tinh.QUY_TINH


# saoThienQuy = Sao(68, "Thiên quý", "O", 3)
class ThienQuy(Sao):
    id = 68
    ten = "Thiên Quý"
    hanh = Hanh.O
    loai = Tinh.QUY_TINH


# # Sao đôi khác
# saoThienKhoc = Sao(69, "Thiên khốc", "T", 12)
class ThienKhoc(Sao):
    id = 69
    ten = "Thiên Khốc"
    hanh = Hanh.T
    loai = Tinh.BAI_TINH


# saoThienHu = Sao(70, "Thiên hư", "T", 12)
class ThienHu(Sao):
    id = 70
    ten = "Thiên Hư"
    hanh = Hanh.T
    loai = Tinh.BAI_TINH


# saoThienDuc = Sao(71, "Thiên đức", "H", 5)
class ThienDuc(Sao):
    id = 71
    ten = "Thiên Đức"
    hanh = Hanh.H
    loai = Tinh.PHUC_TINH


# saoNguyetDuc = Sao(72, "Nguyệt đức", "H", 5)
class NguyetDuc(Sao):
    id = 72
    ten = "Nguyệt Đức"
    hanh = Hanh.H
    loai = Tinh.QUYEN_TINH


# saoThienHinh = Sao(73, "Thiên hình", "H", 15)
class ThienHinh(Sao):
    id = 73
    ten = "Thiên Hình"
    hanh = Hanh.H
    loai = Tinh.HINH_TINH


# saoThienRieu = Sao(74, "Thiên riêu", "T", 13)
class ThienRieu(Sao):
    id = 74
    ten = "Thiên Riêu"
    hanh = Hanh.T
    loai = Tinh.AM_TINH


# saoThienY = Sao(75, "Thiên y", "T", 5)
class ThienY(Sao):
    id = 75
    ten = "Thiên Y"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH


# saoQuocAn = Sao(76, "Quốc ấn", "O", 6)
class QuocAn(Sao):
    id = 76
    ten = "Quốc Ấn"
    hanh = Hanh.O
    loai = Tinh.VAN_TINH


# saoDuongPhu = Sao(77, "Đường phù", "M", 4)
class DuongPhu(Sao):
    id = 77
    ten = "Đường Phù"
    hanh = Hanh.M
    loai = Tinh.QUYEN_TINH


# saoDaoHoa = Sao(78, "Đào hoa", "M", 8)
class DaoHoa(Sao):
    id = 78
    ten = "Đào Hoa"
    hanh = Hanh.M
    loai = Tinh.DAO_HOA_TINH


# saoHongLoan = Sao(79, "Hồng loan", "T", 8)
class HongLoan(Sao):
    id = 79
    ten = "Hồng Loan"
    hanh = Hanh.T
    loai = Tinh.DAO_HOA_TINH


# saoThienHy = Sao(80, "Thiên hỷ", "T", 5)
class ThienHy(Sao):
    id = 80
    ten = "Thiên Hỷ"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH


# saoThienGiai = Sao(81, "Thiên giải", "H", 5)
class ThienGiai(Sao):
    id = 81
    ten = "Thiên Giải"
    hanh = Hanh.H
    loai = Tinh.PHUC_TINH


# saoDiaGiai = Sao(82, "Địa giải", "O", 5)
class DiaGiai(Sao):
    id = 82
    ten = "Địa Giải"
    hanh = Hanh.O
    loai = Tinh.PHUC_TINH


# saoGiaiThan = Sao(83, "Giải thần", "M", 5)
class GiaiThan(Sao):
    id = 83
    ten = "Giải Thần"
    hanh = Hanh.M
    loai = Tinh.PHUC_TINH


# saoThaiPhu = Sao(84, "Thai phụ", "K", 6)
class ThaiPhu(Sao):
    id = 84
    ten = "Thai Phụ"
    hanh = Hanh.K
    loai = Tinh.VAN_TINH


# saoPhongCao = Sao(85, "Phong cáo", "O", 4)
class PhongCao(Sao):
    id = 85
    ten = "Phong Cáo"
    hanh = Hanh.O
    loai = Tinh.QUYEN_TINH


# saoThienTai = Sao(86, "Thiên tài", "O", 2)
class ThienTai(Sao):
    id = 86
    ten = "Thiên Tài"
    hanh = Hanh.O
    loai = Tinh.PHU_TINH


# saoThienTho = Sao(87, "Thiên thọ", "O", 5)
class ThienTho(Sao):
    id = 87
    ten = "Thiên Thọ"
    hanh = Hanh.O
    loai = Tinh.PHUC_TINH


# saoThienThuong = Sao(88, "Thiên thương", "O", 12)
class ThienThuong(Sao):
    id = 88
    ten = "Thiên Thương"
    hanh = Hanh.O
    loai = Tinh.BAI_TINH


# saoThienSu = Sao(89, "Thiên sứ", "T", 12)
class ThienSu(Sao):
    id = 89
    ten = "Thiên Sứ"
    hanh = Hanh.T
    loai = Tinh.BAI_TINH


# saoThienLa = Sao(90, "Thiên la", "O", 12)
class ThienLa(Sao):
    id = 90
    ten = "Thiên La"
    hanh = Hanh.O
    loai = Tinh.BAI_TINH


# saoDiaVong = Sao(91, "Địa võng", "O", 12)
class DiaVong(Sao):
    id = 91
    ten = "Địa Võng"
    hanh = Hanh.O
    loai = Tinh.BAI_TINH


# saoHoaKhoa = Sao(92, "Hóa khoa", "T", 5)
class HoaKhoa(Sao):
    id = 92
    ten = "Hóa Khoa"
    hanh = Hanh.T
    loai = Tinh.PHUC_TINH


# saoHoaQuyen = Sao(93, "Hóa quyền", "T", 4)
class HoaQuyen(Sao):
    id = 93
    ten = "Hóa Quyền"
    hanh = Hanh.T
    loai = Tinh.QUYEN_TINH


# saoHoaLoc = Sao(94, "Hóa lộc", "M", 3)
class HoaLoc(Sao):
    id = 94
    ten = "Hóa Lộc"
    hanh = Hanh.M
    loai = Tinh.QUY_TINH


# saoHoaKy = Sao(95, "Hóa kỵ", "T", 13)
class HoaKy(Sao):
    id = 95
    ten = "Hóa Kỵ"
    hanh = Hanh.T
    loai = Tinh.AM_TINH


# saoCoThan = Sao(96, "Cô thần", "O", 13)
class CoThan(Sao):
    id = 96
    ten = "Cô Thần"
    hanh = Hanh.O
    loai = Tinh.AM_TINH


# saoQuaTu = Sao(97, "Quả tú", "O", 13)
class QuaTu(Sao):
    id = 97
    ten = "Quả Tú"
    hanh = Hanh.O
    loai = Tinh.AM_TINH


# saoThienMa = Sao(98, "Thiên mã", "H", 3)
class ThienMa(Sao):
    id = 98
    ten = "Thiên Mã"
    hanh = Hanh.H
    loai = Tinh.QUY_TINH


# saoPhaToai = Sao(99, "Phá toái", "H", 12)
class PhaToai(Sao):
    id = 99
    ten = "Phá Toái"
    hanh = Hanh.H
    loai = Tinh.BAI_TINH


# saoThienQuan = Sao(100, "Thiên quan", "H", 5)
class ThienQuan(Sao):
    id = 100
    ten = "Thiên Quan"
    hanh = Hanh.H
    loai = Tinh.PHUC_TINH


# saoThienPhuc = Sao(101, "Thiên phúc", "H", 5)
class ThienPhuc(Sao):
    id = 101
    ten = "Thiên Phúc"
    hanh = Hanh.H
    loai = Tinh.PHUC_TINH


# saoLuuHa = Sao(102, "Lưu hà", "T", 12)
class LuuHa(Sao):
    id = 102
    ten = "Lưu Hà"
    hanh = Hanh.T
    loai = Tinh.BAI_TINH


# saoThienTru = Sao(103, "Thiên trù", "O", 5)
class ThienTru(Sao):
    id = 103
    ten = "Thiên Trù"
    hanh = Hanh.O
    loai = Tinh.PHUC_TINH


# saoKiepSat = Sao(104, "Kiếp sát", "H", 11)
class KiepSat(Sao):
    id = 104
    ten = "Kiếp Sát"
    hanh = Hanh.H
    loai = Tinh.SAT_TINH


# saoHoaCai = Sao(105, "Hoa cái", "K", 14)
class HoaCai(Sao):
    id = 105
    ten = "Hoa Cái"
    hanh = Hanh.K
    loai = Tinh.DAM_TINH


# saoVanTinh = Sao(106, "Văn tinh", "H", 6)
class VanTinh(Sao):
    id = 106
    ten = "Văn Tinh"
    hanh = Hanh.H
    loai = Tinh.VAN_TINH


# saoDauQuan = Sao(107, "Đẩu quân", "H", 5)
class DauQuan(Sao):
    id = 107
    ten = "Đẩu Quân"
    hanh = Hanh.H
    loai = Tinh.PHUC_TINH


# saoThienKhong = Sao(108, "Thiên không", "T", 11)
class ThienKhong(Sao):
    id = 108
    ten = "Thiên Không"
    hanh = Hanh.T
    loai = Tinh.SAT_TINH
