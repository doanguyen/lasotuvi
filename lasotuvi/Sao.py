# -*- coding: utf-8 -*-
"""
MIT License
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""

from lasotuvi.AmDuong import nguHanh
from lasotuvi.Hanh import HanhVar, Hanh
from lasotuvi.primitive import AmDuongVar, TinhVar, Tinh


class Sao:
    def __init__(self, id: int, ten: str, hanh: HanhVar, loai: TinhVar, amDuong: AmDuongVar = None,
                 phuongVi: str = None, vongTrangSinh=0):
        """Sao là thành phần cơ bản trong tử vi
            Args:
                id (int): 1, 2, ...
                ten (str): Tử vi, Tham lang,...
                hanh (Hanh): Hanh.H,...
                loai (lasotuvi.primitive.Tinh): Sao tốt < 10, sau xấu > 10
                    1: Chính tinh, 2: Phụ tinh nói chung
                    3: Quý tinh, 4: Quyền tinh, 5: Phúc tinh, 6: Văn tinh
                    7: Đài các tinh, 8: Đào hoa tinh

                    11: Sát tinh, 12: Bại tinh, 13: Ám tinh, 14: Dâm tinh,
                    15: Hình tinh
                phuongVi (str, optional): Bắc Đẩu tinh, Nam Bắc Đẩu tinh
                amDuong (AmDuongVar): Âm Dương của sao
                vongTrangSinh (int, optional): 0/None: Không thuộc vòng Tràng sinh
                                                1: Thuộc vòng Tràng sinh
            """
        self.id = id
        self.ten = ten
        self.nguHanh = hanh
        self.loai = loai
        self.saoPhuongVi = phuongVi
        self.saoAmDuong = amDuong
        self.vongTrangSinh = vongTrangSinh
        self.cssSao = nguHanh(hanh)['css']
        self.saoDacTinh = None

        self.viTriCung = None

    def anDacTinh(self, dacTinh):
        """An Đặc tính cho sao: V, M, Đ, B, H
        Args: saoDacTinh (str): Đặc tính của sao, Vượng (V), Miếu (M),
                                Đắc (Đ), Bình (B), Hãm (H)
        Returns:
            object: self
        """
        self.saoDacTinh = dacTinh

    def anCung(self, viTriCung):
        """Summary

        Returns:
            TYPE: Description
        """
        self.viTriCung = viTriCung


# Tử vi tinh hệ
saoTuVi = Sao(1, "Tử vi", Hanh.O, Tinh.CHINH_TINH, 1, "Đế tinh", 0)
saoLiemTrinh = Sao(2, "Liêm trinh", Hanh.H, Tinh.CHINH_TINH, 1, "Bắc đẩu tinh", 0)
saoThienDong = Sao(3, "Thiên đồng", Hanh.T, Tinh.CHINH_TINH, 1, "Bắc đẩu tinh", 0)
saoVuKhuc = Sao(4, "Vũ khúc", Hanh.K, Tinh.CHINH_TINH, -1, "Bắc đẩu tinh", 0)
saoThaiDuong = Sao(5, "Thái Dương", Hanh.H, Tinh.CHINH_TINH, 1, "Nam đẩu tinh", 0)
saoThienCo = Sao(6, "Thiên cơ", Hanh.M, Tinh.CHINH_TINH, -1, "Nam đẩu tinh", 0)

# Thiên phủ tinh hệ
saoThienPhu = Sao(7, "Thiên phủ", Hanh.O, 1, 1, "Nam đẩu tinh", 0)
saoThaiAm = Sao(8, "Thái âm", Hanh.T, 1, -1, "Bắc đẩu tinh", 0)
saoThamLang = Sao(9, "Tham lang", Hanh.T, 1, -1, "Bắc đẩu tinh", 0)
saoCuMon = Sao(10, "Cự môn", Hanh.T, 1, -1, "Bắc đẩu tinh", 0)
saoThienTuong = Sao(11, "Thiên tướng", Hanh.T, 1, 1, "Nam đẩu tinh", 0)
saoThienLuong = Sao(12, "Thiên lương", Hanh.M, 1, -1, "Nam đẩu tinh", 0)
saoThatSat = Sao(13, "Thất sát", Hanh.K, 1, 1, "Nam đẩu tinh", 0)
saoPhaQuan = Sao(14, "Phá quân", Hanh.T, 1, -1, "Bắc đẩu tinh", 0)

# Vòng Địa chi - Thái tuế
saoThaiTue = Sao(15, "Thái tuế", Hanh.H, 15, 0, "")
saoThieuDuong = Sao(16, "Thiếu dương", Hanh.H, 5)
saoTangMon = Sao(17, "Tang môn", Hanh.M, 12)
saoThieuAm = Sao(18, "Thiếu âm", Hanh.T, 5)
saoQuanPhu3 = Sao(19, "Quan phù", Hanh.H, 12)
saoTuPhu = Sao(20, "Tử phù", Hanh.K, 12)
saoTuePha = Sao(21, "Tuế phá", Hanh.H, 12)
saoLongDuc = Sao(22, "Long đức", Hanh.T, 5)
saoBachHo = Sao(23, "Bạch hổ", Hanh.K, 12)
saoPhucDuc = Sao(24, "Phúc đức", Hanh.O, 5)
saoDieuKhach = Sao(25, "Điếu khách", Hanh.H, 12)
saoTrucPhu = Sao(26, "Trực phù", Hanh.K, 16)

#  Vòng Thiên can - Lộc tồn
saoLocTon = Sao(27, "Lộc tồn", Hanh.O, 3, "Bắc đẩu tinh")
saoBacSy = Sao(109, "Bác sỹ", Hanh.T, 5)
saoLucSi = Sao(28, "Lực sĩ", Hanh.H, 2)
saoThanhLong = Sao(29, "Thanh long", Hanh.T, 5)
saoTieuHao = Sao(30, "Tiểu hao", Hanh.H, 12)
saoTuongQuan = Sao(31, "Tướng quân", Hanh.M, 4)
saoTauThu = Sao(32, "Tấu thư", Hanh.K, 3)
saoPhiLiem = Sao(33, "Phi liêm", Hanh.H, 2)
saoHyThan = Sao(34, "Hỷ thần", Hanh.H, 5)
saoBenhPhu = Sao(35, "Bệnh phù", Hanh.O, 12)
saoDaiHao = Sao(36, "Đại hao", Hanh.H, 12)
saoPhucBinh = Sao(37, "Phục binh", Hanh.H, 13)
saoQuanPhu2 = Sao(38, "Quan phù", Hanh.H, 12)

# Vòng Tràng sinh
saoTrangSinh = Sao(39, "Tràng sinh", Hanh.T, 5, vongTrangSinh=1)
saoMocDuc = Sao(40, "Mộc dục", Hanh.T, 14, vongTrangSinh=1)
saoQuanDoi = Sao(41, "Quan đới", Hanh.K, 4, vongTrangSinh=1)
saoLamQuan = Sao(42, "Lâm quan", Hanh.K, 7, vongTrangSinh=1)
saoDeVuong = Sao(43, "Đế vượng", Hanh.K, 5, vongTrangSinh=1)
saoSuy = Sao(44, "Suy", Hanh.T, 12, vongTrangSinh=1)
saoBenh = Sao(45, "Bệnh", Hanh.H, 12, vongTrangSinh=1)
saoTu = Sao(46, "Tử", Hanh.H, 12, vongTrangSinh=1)
saoMo = Sao(47, "Mộ", Hanh.O, vongTrangSinh=1)
saoTuyet = Sao(48, "Tuyệt", Hanh.O, 12, vongTrangSinh=1)
saoThai = Sao(49, "Thai", Hanh.O, 14, vongTrangSinh=1)
saoDuong = Sao(50, "Dưỡng", Hanh.M, 2, vongTrangSinh=1)

# Lục sát
#    Kình dương đà la
saoDaLa = Sao(51, "Đà la", Hanh.K, 11)
saoKinhDuong = Sao(52, "Kình dương", Hanh.K, 11)

#    Địa không - Địa kiếp
saoDiaKhong = Sao(53, "Địa không", Hanh.H, 11)
saoDiaKiep = Sao(54, "Địa kiếp", Hanh.H, 11)

#    Hỏa tinh - Linh tinh
saoLinhTinh = Sao(55, "Linh tinh", Hanh.H, 11)
saoHoaTinh = Sao(56, "Hỏa tinh", Hanh.H, 11)

# Sao Âm Dương
#    Văn xương - Văn khúc
saoVanXuong = Sao(57, "Văn xương", Hanh.K, 6)
saoVanKhuc = Sao(58, "Văn Khúc", Hanh.T, 6)

#    Thiên khôi - Thiên Việt
saoThienKhoi = Sao(59, "Thiên khôi", Hanh.H, 6)
saoThienViet = Sao(60, "Thiên việt", Hanh.H, 6)

#    Tả phù - Hữu bật
saoTaPhu = Sao(61, "Tả phù", Hanh.O, 2)
saoHuuBat = Sao(62, "Hữu bật", Hanh.O, 2)

#    Long trì - Phượng các
saoLongTri = Sao(63, "Long trì", Hanh.T, 3)
saoPhuongCac = Sao(64, "Phượng các", Hanh.O, 3)

#    Tam thai - Bát tọa
saoTamThai = Sao(65, "Tam thai", Hanh.M, 7)
saoBatToa = Sao(66, "Bát tọa", Hanh.T, 7)

#    Ân quang - Thiên quý
saoAnQuang = Sao(67, "Ân quang", Hanh.M, 3)
saoThienQuy = Sao(68, "Thiên quý", Hanh.O, 3)

# Sao đôi khác
saoThienKhoc = Sao(69, "Thiên khốc", Hanh.T, 12)
saoThienHu = Sao(70, "Thiên hư", Hanh.T, 12)
saoThienDuc = Sao(71, "Thiên đức", Hanh.H, 5)
saoNguyetDuc = Sao(72, "Nguyệt đức", Hanh.H, 5)
saoThienHinh = Sao(73, "Thiên hình", Hanh.H, 15)
saoThienRieu = Sao(74, "Thiên riêu", Hanh.T, 13)
saoThienY = Sao(75, "Thiên y", Hanh.T, 5)
saoQuocAn = Sao(76, "Quốc ấn", Hanh.O, 6)
saoDuongPhu = Sao(77, "Đường phù", Hanh.M, 4)
saoDaoHoa = Sao(78, "Đào hoa", Hanh.M, 8)
saoHongLoan = Sao(79, "Hồng loan", Hanh.T, 8)
saoThienHy = Sao(80, "Thiên hỷ", Hanh.T, 5)
saoThienGiai = Sao(81, "Thiên giải", Hanh.H, 5)
saoDiaGiai = Sao(82, "Địa giải", Hanh.O, 5)
saoGiaiThan = Sao(83, "Giải thần", Hanh.M, 5)
saoThaiPhu = Sao(84, "Thai phụ", Hanh.K, 6)
saoPhongCao = Sao(85, "Phong cáo", Hanh.O, 4)
saoThienTai = Sao(86, "Thiên tài", Hanh.O, 2)
saoThienTho = Sao(87, "Thiên thọ", Hanh.O, 5)
saoThienThuong = Sao(88, "Thiên thương", Hanh.O, 12)
saoThienSu = Sao(89, "Thiên sứ", Hanh.T, 12)
saoThienLa = Sao(90, "Thiên la", Hanh.O, 12)
saoDiaVong = Sao(91, "Địa võng", Hanh.O, 12)
saoHoaKhoa = Sao(92, "Hóa khoa", Hanh.T, 5)
saoHoaQuyen = Sao(93, "Hóa quyền", Hanh.T, 4)
saoHoaLoc = Sao(94, "Hóa lộc", Hanh.M, 3)
saoHoaKy = Sao(95, "Hóa kỵ", Hanh.T, 13)
saoCoThan = Sao(96, "Cô thần", Hanh.O, 13)
saoQuaTu = Sao(97, "Quả tú", Hanh.O, 13)
saoThienMa = Sao(98, "Thiên mã", Hanh.H, 3)
saoPhaToai = Sao(99, "Phá toái", Hanh.H, 12)
saoThienQuan = Sao(100, "Thiên quan", Hanh.H, 5)
saoThienPhuc = Sao(101, "Thiên phúc", Hanh.H, 5)
saoLuuHa = Sao(102, "Lưu hà", Hanh.T, 12)
saoThienTru = Sao(103, "Thiên trù", Hanh.O, 5)
saoKiepSat = Sao(104, "Kiếp sát", Hanh.H, 11)
saoHoaCai = Sao(105, "Hoa cái", Hanh.K, 14)
saoVanTinh = Sao(106, "Văn tinh", Hanh.H, 6)
saoDauQuan = Sao(107, "Đẩu quân", Hanh.H, 5)
saoThienKhong = Sao(108, "Thiên không", Hanh.T, 11)
