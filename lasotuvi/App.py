# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from lasotuvi.AmDuong import (dichCung, ngayThangNam, ngayThangNamCanChi, nguHanh, thienCan,
                              timCoThan, timCuc, timHoaLinh, timLuuTru, timPhaToai, timThienKhoi,
                              timThienMa, timThienQuanThienPhuc, timTrangSinh, timTriet, timTuVi,
                              diaChi)
from lasotuvi.Sao import *


def lapDiaBan(diaBan, nn, tt, nnnn, gioSinh, gioiTinh, duongLich, timeZone):
    if duongLich is True:
        nn, tt, nnnn, thangNhuan = ngayThangNam(nn, tt, nnnn, duongLich, timeZone)
    canThang, canNam, chiNam = ngayThangNamCanChi(nn, tt, nnnn, False, timeZone)

    diaBan = diaBan(tt, gioSinh)

    amDuongNamSinh = thienCan[canNam]["amDuong"]
    amDuongChiNamSinh = diaChi[chiNam]["amDuong"]

    # Bản Mệnh chính là Ngũ hành nạp âm của năm sinh
    # banMenh = nguHanhNapAm(canNam, chiNam)

    hanhCuc = timCuc(diaBan.cungMenh, canNam)
    cuc = nguHanh(hanhCuc)
    cucSo = cuc['cuc']

    # Nhập đại hạn khi đã biết được số cục
    # Theo sách Số tử vi dưới góc nhìn khoa học
    # Dương Nam - Âm Nữ theo chiều thuận
    # Âm Nam - Dương Nữ theo chiều nghịch
    diaBan = diaBan.nhapDaiHan(cucSo, gioiTinh * amDuongChiNamSinh)

    # Nhập tiểu hạn
    khoiHan = dichCung(11, -3 * (chiNam - 1))
    diaBan = diaBan.nhapTieuHan(khoiHan, gioiTinh, chiNam)

    # Bắt đầu an Tử vi tinh hệ
    viTriTuVi = timTuVi(cucSo, nn)
    diaBan.nhapSao(viTriTuVi, TuVi)

    viTriLiemTrinh = dichCung(viTriTuVi, 4)
    diaBan.nhapSao(viTriLiemTrinh, LiemTrinh)

    viTriThienDong = dichCung(viTriTuVi, 7)
    diaBan.nhapSao(viTriThienDong, ThienDong)

    viTriVuKhuc = dichCung(viTriTuVi, 8)
    diaBan.nhapSao(viTriVuKhuc, VuKhuc)

    vitriThaiDuong = dichCung(viTriTuVi, 9)
    diaBan.nhapSao(vitriThaiDuong, ThaiDuong)

    viTriThienCo = dichCung(viTriTuVi, 11)
    diaBan.nhapSao(viTriThienCo, ThienCo)

    # Thiên phủ tinh hệ
    # viTriTuVi = 4
    viTriThienPhu = dichCung(3, 3 - viTriTuVi)
    diaBan.nhapSao(viTriThienPhu, ThienPhu)

    viTriThaiAm = dichCung(viTriThienPhu, 1)
    diaBan.nhapSao(viTriThaiAm, ThaiAm)

    viTriThamLang = dichCung(viTriThienPhu, 2)
    diaBan.nhapSao(viTriThamLang, ThamLang)

    viTriCuMon = dichCung(viTriThienPhu, 3)
    diaBan.nhapSao(viTriCuMon, CuMon)

    viTriThienTuong = dichCung(viTriThienPhu, 4)
    diaBan.nhapSao(viTriThienTuong, ThienTuong)

    viTriThienLuong = dichCung(viTriThienPhu, 5)
    diaBan.nhapSao(viTriThienLuong, ThienLuong)

    viTriThatSat = dichCung(viTriThienPhu, 6)
    diaBan.nhapSao(viTriThatSat, ThatSat)

    viTriPhaQuan = dichCung(viTriThienPhu, 10)
    diaBan.nhapSao(viTriPhaQuan, PhaQuan)

    # Vòng Lộc tồn
    # Vị trí sao Lộc tồn ở Can của năm sinh trên địa bàn
    #  sao Bác sỹ ở cùng cung với Lộc tồn
    viTriLocTon = thienCan[canNam]['vitriDiaBan']
    diaBan.nhapSao(viTriLocTon, LocTon, BacSy)

    amDuongNamNu = gioiTinh * amDuongNamSinh
    viTriLucSi = dichCung(viTriLocTon, 1 * amDuongNamNu)
    diaBan.nhapSao(viTriLucSi, LucSi)

    viTriThanhLong = dichCung(viTriLocTon, 2 * amDuongNamNu)
    diaBan.nhapSao(viTriThanhLong, ThanhLong)

    viTriTieuHao = dichCung(viTriLocTon, 3 * amDuongNamNu)
    diaBan.nhapSao(viTriTieuHao, TieuHao)

    viTriTuongQuan = dichCung(viTriLocTon, 4 * amDuongNamNu)
    diaBan.nhapSao(viTriTuongQuan, TuongQuan)

    viTriTauThu = dichCung(viTriLocTon, 5 * amDuongNamNu)
    diaBan.nhapSao(viTriTauThu, TauThu)

    viTriPhiLiem = dichCung(viTriLocTon, 6 * amDuongNamNu)
    diaBan.nhapSao(viTriPhiLiem, PhiLiem)

    viTriHyThan = dichCung(viTriLocTon, 7 * amDuongNamNu)
    diaBan.nhapSao(viTriHyThan, HyThan)

    viTriBenhPhu = dichCung(viTriLocTon, 8 * amDuongNamNu)
    diaBan.nhapSao(viTriBenhPhu, BenhPhu)

    viTriDaiHao = dichCung(viTriLocTon, 9 * amDuongNamNu)
    diaBan.nhapSao(viTriDaiHao, DaiHao)

    viTriPhucBinh = dichCung(viTriLocTon, 10 * amDuongNamNu)
    diaBan.nhapSao(viTriPhucBinh, PhucBinh)

    viTriQuanPhu2 = dichCung(viTriLocTon, 11 * amDuongNamNu)
    diaBan.nhapSao(viTriQuanPhu2, QuanPhu2)

    # Vòng Địa chi - Thái tuế
    viTriThaiTue = chiNam
    diaBan.nhapSao(viTriThaiTue, ThaiTue)

    viTriThieuDuong = dichCung(viTriThaiTue, 1)
    diaBan.nhapSao(viTriThieuDuong, ThieuDuong, ThienKhong)

    viTriTangMon = dichCung(viTriThaiTue, 2)
    diaBan.nhapSao(viTriTangMon, TangMon)

    viTriThieuAm = dichCung(viTriThaiTue, 3)
    diaBan.nhapSao(viTriThieuAm, ThieuAm)

    viTriQuanPhu3 = dichCung(viTriThaiTue, 4)
    diaBan.nhapSao(viTriQuanPhu3, QuanPhu3)

    viTriTuPhu = dichCung(viTriThaiTue, 5)
    diaBan.nhapSao(viTriTuPhu, TuPhu, NguyetDuc)

    viTriTuePha = dichCung(viTriThaiTue, 6)
    diaBan.nhapSao(viTriTuePha, TuePha)

    viTriLongDuc = dichCung(viTriThaiTue, 7)
    diaBan.nhapSao(viTriLongDuc, LongDuc)

    viTriBachHo = dichCung(viTriThaiTue, 8)
    diaBan.nhapSao(viTriBachHo, BachHo)

    viTriPhucDuc = dichCung(viTriThaiTue, 9)
    diaBan.nhapSao(viTriPhucDuc, PhucDuc, ThienDuc)

    viTriDieuKhach = dichCung(viTriThaiTue, 10)
    diaBan.nhapSao(viTriDieuKhach, DieuKhach)

    viTriTrucPhu = dichCung(viTriThaiTue, 11)
    diaBan.nhapSao(viTriTrucPhu, TrucPhu)

    #  Vòng ngũ hành cục Tràng sinh
    # !!! Đã sửa !!! *LƯU Ý Phần này đã sửa* Theo cụ Thiên Lương: Nam -> Thuận,
    # Nữ -> Nghịch (Không phù hợp)
    # **ISSUE 2**: Dương nam, Âm nữ theo chiều thuận, Âm nam Dương nữ theo
    # chiều nghịch

    viTriTrangSinh = timTrangSinh(cucSo)
    diaBan.nhapSao(viTriTrangSinh, TrangSinh)

    viTriMocDuc = dichCung(viTriTrangSinh, amDuongNamNu * 1)
    diaBan.nhapSao(viTriMocDuc, MocDuc)

    viTriQuanDoi = dichCung(viTriTrangSinh, amDuongNamNu * 2)
    diaBan.nhapSao(viTriQuanDoi, QuanDoi)

    viTriLamQuan = dichCung(viTriTrangSinh, amDuongNamNu * 3)
    diaBan.nhapSao(viTriLamQuan, LamQuan)

    viTriDeVuong = dichCung(viTriTrangSinh, amDuongNamNu * 4)
    diaBan.nhapSao(viTriDeVuong, DeVuong)

    viTriSuy = dichCung(viTriTrangSinh, amDuongNamNu * 5)
    diaBan.nhapSao(viTriSuy, Suy)

    viTriBenh = dichCung(viTriTrangSinh, amDuongNamNu * 6)
    diaBan.nhapSao(viTriBenh, Benh)

    viTriTu = dichCung(viTriTrangSinh, amDuongNamNu * 7)
    diaBan.nhapSao(viTriTu, Tu)

    viTriMo = dichCung(viTriTrangSinh, amDuongNamNu * 8)
    diaBan.nhapSao(viTriMo, Mo)

    viTriTuyet = dichCung(viTriTrangSinh, amDuongNamNu * 9)
    diaBan.nhapSao(viTriTuyet, Tuyet)

    viTriThai = dichCung(viTriTrangSinh, amDuongNamNu * (-1))
    diaBan.nhapSao(viTriThai, Thai)

    viTriDuong = dichCung(viTriTrangSinh, amDuongNamNu * (-2))
    diaBan.nhapSao(viTriDuong, Duong)

    # An sao đôi
    #    Kình dương - Đà la
    viTriDaLa = dichCung(viTriLocTon, -1)
    diaBan.nhapSao(viTriDaLa, DaLa)

    viTriKinhDuong = dichCung(viTriLocTon, 1)
    diaBan.nhapSao(viTriKinhDuong, KinhDuong)

    #  Không - Kiếp
    # Khởi giờ Tý ở cung Hợi, đếm thuận đến giờ sinh được cung Địa kiếp
    viTriDiaKiep = dichCung(11, gioSinh)
    diaBan.nhapSao(viTriDiaKiep, DiaKiep)

    viTriDiaKhong = dichCung(12, 12 - viTriDiaKiep)
    diaBan.nhapSao(viTriDiaKhong, DiaKhong)

    viTriHoaTinh, viTriLinhTinh = timHoaLinh(chiNam, gioSinh, gioiTinh, amDuongNamSinh)
    diaBan.nhapSao(viTriHoaTinh, HoaTinh)
    diaBan.nhapSao(viTriLinhTinh, LinhTinh)

    viTriLongTri = dichCung(5, chiNam - 1)
    diaBan.nhapSao(viTriLongTri, LongTri)

    viTriPhuongCac = dichCung(2, 2 - viTriLongTri)
    diaBan.nhapSao(viTriPhuongCac, PhuongCac, GiaiThan)

    viTriTaPhu = dichCung(5, tt - 1)
    diaBan.nhapSao(viTriTaPhu, TaPhu)

    viTriHuuBat = dichCung(2, 2 - viTriTaPhu)
    diaBan.nhapSao(viTriHuuBat, HuuBat)

    viTriVanKhuc = dichCung(5, gioSinh - 1)
    diaBan.nhapSao(viTriVanKhuc, VanKhuc)

    viTriVanXuong = dichCung(2, 2 - viTriVanKhuc)
    diaBan.nhapSao(viTriVanXuong, VanXuong)

    viTriTamThai = dichCung(5, tt + nn - 2)
    diaBan.nhapSao(viTriTamThai, TamThai)

    viTriBatToa = dichCung(2, 2 - viTriTamThai)
    diaBan.nhapSao(viTriBatToa, BatToa)

    # ! Vị trí sao Ân Quang - Thiên Quý
    # ! Lấy cung thìn làm mồng 1 đếm thuận đến ngày sinh,
    # ! lui lại một cung để lấy đó làm giờ tý đếm thuận đến giờ sinh là
    #  Ân Quang
    # ! Thiên Quý đối với Ân Quang qua trục Sửu Mùi
    # @ viTriAnQuang = dichCung(5, nn + gioSinh - 3)
    # @ viTriThienQuy = dichCung(2, 2 - viTriAnQuang)
    # Phía trên là cách an Quang-Quý theo cụ Vu Thiên
    # Sau khi tìm hiểu thì Quang-Quý sẽ được an theo Xương-Khúc như sau:
    # Ân Quang − Xem Văn Xương ở cung nào, kể cung ấy là mồng một
    # bắt đầu đếm thoe chiều thuận đến ngày sinh, lùi lại một cung,
    # an Ân Quang.
    # Thiên Quý − Xem Văn Khúc ở cung nào, kể cung ấy là mồng một,
    # !!! bắt đầu đếm theo chiều nghịch đến ngày sinh, lùi lại một cung,
    # an Thiên Quý.!!!
    # ??? Thiên Quý ở đối cung của Ân Quang qua trục Sửu Mùi mới chính xác???

    viTriAnQuang = dichCung(viTriVanXuong, nn - 2)
    diaBan.nhapSao(viTriAnQuang, AnQuang)

    viTriThienQuy = dichCung(2, 2 - viTriAnQuang)
    diaBan.nhapSao(viTriThienQuy, ThienQuy)

    viTriThienKhoi = timThienKhoi(canNam)
    diaBan.nhapSao(viTriThienKhoi, ThienKhoi)

    viTriThienViet = dichCung(5, 5 - viTriThienKhoi)
    diaBan.nhapSao(viTriThienViet, ThienViet)

    viTriThienHu = dichCung(7, chiNam - 1)
    diaBan.nhapSao(viTriThienHu, ThienHu)

    viTriThienKhoc = dichCung(7, -chiNam + 1)
    diaBan.nhapSao(viTriThienKhoc, ThienKhoc)

    viTriThienTai = dichCung(diaBan.cungMenh, chiNam - 1)
    diaBan.nhapSao(viTriThienTai, ThienTai)

    viTriThienTho = dichCung(diaBan.cungThan, chiNam - 1)
    diaBan.nhapSao(viTriThienTho, ThienTho)

    viTriHongLoan = dichCung(4, -chiNam + 1)
    diaBan.nhapSao(viTriHongLoan, HongLoan)

    viTriThienHy = dichCung(viTriHongLoan, 6)
    diaBan.nhapSao(viTriThienHy, ThienHy)

    #  Thiên Quan - Thiên Phúc
    viTriThienQuan, viTriThienPhuc = timThienQuanThienPhuc(canNam)
    diaBan.nhapSao(viTriThienQuan, ThienQuan)
    diaBan.nhapSao(viTriThienPhuc, ThienPhuc)

    viTriThienHinh = dichCung(10, tt - 1)
    diaBan.nhapSao(viTriThienHinh, ThienHinh)

    viTriThienRieu = dichCung(viTriThienHinh, 4)
    diaBan.nhapSao(viTriThienRieu, ThienRieu, ThienY)

    viTriCoThan = timCoThan(chiNam)
    diaBan.nhapSao(viTriCoThan, CoThan)

    viTriQuaTu = dichCung(viTriCoThan, -4)
    diaBan.nhapSao(viTriQuaTu, QuaTu)

    viTriVanTinh = dichCung(viTriKinhDuong, 2)
    diaBan.nhapSao(viTriVanTinh, VanTinh)

    viTriDuongPhu = dichCung(viTriVanTinh, 2)
    diaBan.nhapSao(viTriDuongPhu, DuongPhu)

    viTriQuocAn = dichCung(viTriDuongPhu, 3)
    diaBan.nhapSao(viTriQuocAn, QuocAn)

    # Thai phụ - Phong Cáo
    viTriThaiPhu = dichCung(viTriVanKhuc, 2)
    diaBan.nhapSao(viTriThaiPhu, ThaiPhu)

    viTriPhongCao = dichCung(viTriVanKhuc, -2)
    diaBan.nhapSao(viTriPhongCao, PhongCao)

    # Thiên giải - Địa giải
    #    Theo cụ Thiên Lương: Lấy cung Thân làm tháng Giêng, đếm thuận nhưng
    #    nhảy cung là Thiên giải. Một số trang web đếm nhưng không nhảy cung???
    #    Liệu phương cách nào đúng?
    viTriThienGiai = dichCung(9, (2 * tt) - 2)
    diaBan.nhapSao(viTriThienGiai, ThienGiai)

    viTriDiaGiai = dichCung(viTriTaPhu, 3)
    diaBan.nhapSao(viTriDiaGiai, DiaGiai)

    # Thiên la - Địa võng, Thiên thương - Thiên sứ
    viTriThienLa = 5
    diaBan.nhapSao(viTriThienLa, ThienLa)

    viTriDiaVong = 11
    diaBan.nhapSao(viTriDiaVong, DiaVong)

    viTriThienThuong = diaBan.cungNoboc
    diaBan.nhapSao(viTriThienThuong, ThienThuong)

    viTriThienSu = diaBan.cungTatAch
    diaBan.nhapSao(viTriThienSu, ThienSu)

    # Vòng Thiên mã
    viTriThienMa = timThienMa(chiNam)
    diaBan.nhapSao(viTriThienMa, ThienMa)

    viTriHoaCai = dichCung(viTriThienMa, 2)
    diaBan.nhapSao(viTriHoaCai, HoaCai)

    viTriKiepSat = dichCung(viTriThienMa, 3)
    diaBan.nhapSao(viTriKiepSat, KiepSat)

    viTriDaoHoa = dichCung(viTriKiepSat, 4)
    diaBan.nhapSao(viTriDaoHoa, DaoHoa)

    # Phá toái
    viTriPhaToai = timPhaToai(chiNam)
    diaBan.nhapSao(viTriPhaToai, PhaToai)

    # Đẩu quân
    viTriDauQuan = dichCung(chiNam, -tt + gioSinh)
    diaBan.nhapSao(viTriDauQuan, DauQuan)

    #  Tứ Hóa
    # An theo 10 câu của cụ Thiên Lương trong cuốn
    # Số tử vi dưới mắt khoa học

    if canNam == 1:
        viTriHoaLoc = viTriLiemTrinh
        viTriHoaQuyen = viTriPhaQuan
        viTriHoaKhoa = viTriVuKhuc
        viTriHoaKy = vitriThaiDuong
    elif canNam == 2:
        viTriHoaLoc = viTriThienCo
        viTriHoaQuyen = viTriThienLuong
        viTriHoaKhoa = viTriTuVi
        viTriHoaKy = viTriThaiAm
    elif canNam == 3:
        viTriHoaLoc = viTriThienDong
        viTriHoaQuyen = viTriThienCo
        viTriHoaKhoa = viTriVanXuong
        viTriHoaKy = viTriLiemTrinh
    elif canNam == 4:
        viTriHoaLoc = viTriThaiAm
        viTriHoaQuyen = viTriThienDong
        viTriHoaKhoa = viTriThienCo
        viTriHoaKy = viTriCuMon
    elif canNam == 5:
        viTriHoaLoc = viTriThamLang
        viTriHoaQuyen = viTriThaiAm
        viTriHoaKhoa = viTriHuuBat
        viTriHoaKy = viTriThienCo
    elif canNam == 6:
        viTriHoaLoc = viTriVuKhuc
        viTriHoaQuyen = viTriThamLang
        viTriHoaKhoa = viTriThienLuong
        viTriHoaKy = viTriVanKhuc
    elif canNam == 7:
        viTriHoaLoc = vitriThaiDuong
        viTriHoaQuyen = viTriVuKhuc
        viTriHoaKhoa = viTriThienDong
        viTriHoaKy = viTriThaiAm
    elif canNam == 8:
        viTriHoaLoc = viTriCuMon
        viTriHoaQuyen = vitriThaiDuong
        viTriHoaKhoa = viTriVanKhuc
        viTriHoaKy = viTriVanXuong
    elif canNam == 9:
        viTriHoaLoc = viTriThienLuong
        viTriHoaQuyen = viTriTuVi
        viTriHoaKhoa = viTriThienPhu
        viTriHoaKy = viTriVuKhuc
    elif canNam == 10:
        viTriHoaLoc = viTriPhaQuan
        viTriHoaQuyen = viTriCuMon
        viTriHoaKhoa = viTriThaiAm
        viTriHoaKy = viTriThamLang

    diaBan.nhapSao(viTriHoaLoc, HoaLoc)
    diaBan.nhapSao(viTriHoaQuyen, HoaQuyen)
    diaBan.nhapSao(viTriHoaKhoa, HoaKhoa)
    diaBan.nhapSao(viTriHoaKy, HoaKy)

    #  An Lưu Hà - Thiên Trù
    # Sách cụ Thiên Lương không đề cập đến 2 sao này
    # Mong mọi người kiểm chứng
    viTriLuuHa, viTriThienTru = timLuuTru(canNam)
    diaBan.nhapSao(viTriLuuHa, LuuHa)
    diaBan.nhapSao(viTriThienTru, ThienTru)

    # An Tuần, Triệt
    ketThucTuan = dichCung(chiNam, 10 - canNam)
    viTriTuan1 = dichCung(ketThucTuan, 1)
    viTriTuan2 = dichCung(viTriTuan1, 1)
    diaBan.nhapTuan(viTriTuan1, viTriTuan2)

    viTriTriet1, viTriTriet2 = timTriet(canNam)
    diaBan.nhapTriet(viTriTriet1, viTriTriet2)
    return (diaBan)
