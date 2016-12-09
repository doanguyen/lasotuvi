# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os
from src.DiaBan import diaBan
from src.ThienBan import lapThienBan
from src.AmDuong import nguHanh, nguHanhNapAm
from src import lstv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

hoTen = "x"
ngaySinh = 6
thangSinh = 2
namSinh = 2016
gioSinh = 1
gioiTinh = 1
duongLich = True
timeZone = 7

db = lstv.lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh,
                    gioSinh, gioiTinh, duongLich, timeZone)
thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                       gioSinh, gioiTinh, hoTen, db)
thapNhiCung = db.thapNhiCung
cung = (thapNhiCung[11])


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

base = Image.open(os.path.join(BASE_DIR, 'src', 'background.png'))

# get a font
fontChinhTinh = ImageFont.truetype(os.path.join(
    BASE_DIR, 'fonts/NotoSerif-Bold.ttf'), 24)
fontPhuTinh = ImageFont.truetype(os.path.join(
    BASE_DIR, 'fonts/NotoSerif-Bold.ttf'), 20)
fontBatTu = ImageFont.truetype(os.path.join(
    BASE_DIR, 'fonts/NotoSerif-Bold.ttf'), 18)
fontCungTen = ImageFont.truetype(os.path.join(
    BASE_DIR, 'fonts/NotoSerif-Bold.ttf'), 20)
fontThuPhap = ImageFont.truetype(os.path.join(
    BASE_DIR, 'fonts/thuphap.ttf'), 60)
# màu ngũ hành
mauSac = {
    'hanhKim': "#9E9E9E",
    'hanhThuy': "#000100",
    'hanhMoc': "#1B5E20",
    'hanhHoa': "#F44336",
    'hanhTho': "#EF6C00",
    'cungTen': "#3F51B5",
    'tuanTriet': "#FFFFFF",
    'phuHoa': "#4E342E"
}
hanhKim = "#9E9E9E"
hanhThuy = "#000100"
hanhMoc = "#4CAF50"
hanhHoa = "#a71a14"
hanhTho = "#e6bd37"
cungTen = "#2196f3"

# get a drawing context
draw = ImageDraw.Draw(base)
x, y = base.size
width = 2

# Vẽ khung
draw.line([0, 0, 0, base.height], fill=(0, 0, 0, 100), width=width)
draw.line([0, 0, base.width, 0], fill=(0, 0, 0, 100), width=width)
draw.line([x - width, 0, x - width, y - width],
          fill=(0, 0, 0, 100), width=width)
draw.line([0, y - width, x - width, y - width],
          fill=(0, 0, 0, 100), width=width)

draw.line([x / 4 - width, 0, x / 4 - width, y - width],
          fill=(0, 0, 0, 100), width=width)
draw.line([3 * x / 4 - width, 0, 3 * x / 4 - width, y - width],
          fill=(0, 0, 0, 100), width=width)
draw.line([0, y / 4 - width, x - width, y / 4 - width],
          fill=(0, 0, 0, 100), width=width)
draw.line([0, 3 * y / 4 - width, x - width, 3 * y / 4 - width],
          fill=(0, 0, 0, 100), width=width)

draw.line([x / 2 - 2, 0, x / 2 - 2, y / 4 - 2],
          fill=(0, 0, 0, 100), width=width)
draw.line([x / 2 - 2, 3 * y / 4 - 2, x / 2 - 2, y - 2],
          fill=(0, 0, 0, 100), width=width)
draw.line([0, y / 2 - 2, x / 4 - 2, y / 2 - 2],
          fill=(0, 0, 0, 100), width=width)
draw.line([3 * x / 4 - 2, y / 2 - 2, x - 2, y / 2 - 2],
          fill=(0, 0, 0, 100), width=width)
# Hoàn thành phần khung


xyTuanTriet = {
    1: (600, 1080),
    3: (150, 1080),
    5: (150, 360),
    7: (600, 360),
    9: (1050, 360),
    11: (1050, 1080)
}

# print xyTuanTriet[2]


class taoFileAnh(object):

    def __init__(self, drawContainer, diaBan, thienBan):
        super(taoFileAnh, self).__init__()
        self.width = 1440
        self.length = 1200
        self.padding = 5
        self.draw = drawContainer
        self.diaBan = diaBan
        self.thienBan = thienBan
        self.viTriTriet = []
        self.viTriTuan = []

        self._tuanTriet()
        self._nhapDiaBan()
        self._nhapHeaderThienBan()
        self._nhapThienBan()

    def _nhapDiaBan(self):
        for cung in self.diaBan.thapNhiCung[1:]:
            a, b = self._viTriCung(cung.cungSo)
            self._nhapCungChu(cung, a, b)
            self._nhapChinhTinh(cung.cungSao, a, b)
            self._nhapDaiHan(cung, a, b)
            self._nhapPhuTinh(cung.cungSao, a, b)
            self._nhapVongTrangSinh(cung.cungSao, a, b)

    def _nhapThienBan(self):
        self._nhapTenNguoiLap()
        self._nhapAmDuongThuanLy()
        self._nhapBanMenh()
        self._nhapCuc()
        self._menhThanChu()
        self._sinhKhac()
        self._batTu()

    def _viTriCung(self, cungID):
        viTriCung = {
            1: [(600, 1080), (900, 1080)],
            2: [(300, 1080), (600, 1080)],
            3: [(0, 1080), (300, 1080)],
            4: [(0, 720), (300, 720)],
            5: [(0, 360), (300, 360)],
            6: [(0, 0), (300, 0)],
            7: [(300, 0), (600, 0)],
            8: [(600, 0), (900, 0)],
            9: [(900, 0), (1200, 0)],
            10: [(900, 360), (1200, 360)],
            11: [(900, 720), (1200, 720)],
            12: [(900, 1080), (1200, 1080)]
        }
        return viTriCung[cungID]

    def _tuanTriet(self):
        for cung in self.diaBan.thapNhiCung:
            try:
                if cung.trietLo is True:
                    self.viTriTriet.append(cung.cungSo)
            except:
                pass
            try:
                if cung.tuanTrung is True:
                    self.viTriTuan.append(cung.cungSo)
            except:
                pass
        if (min(self.viTriTuan) == min(self.viTriTriet)):
            text = u"Tuần - Triệt".decode("utf-8").upper()
            l, w = fontPhuTinh.getsize(text)
            xy = xyTuanTriet[min(self.viTriTuan)]
            self.draw.rectangle((xy[0] - l/2 - self.padding, xy[1] - w/2,
                                xy[0] + l/2 + self.padding, xy[1] + w/2),
                                fill=(0, 0, 0))
            self.draw.text((xy[0] - l/2, xy[1] - w/2),
                           text,
                           font=fontPhuTinh, fill=mauSac['tuanTriet'])

        else:
            self.xyTuan = xyTuanTriet[min(self.viTriTuan)]
            self.xyTriet = xyTuanTriet[min(self.viTriTriet)]

            tuan = u"Tuần".decode("utf-8").upper()
            triet = u"Triệt".decode("utf-8").upper()

            ltu, wtu = fontPhuTinh.getsize(tuan)
            ltr, wtr = fontPhuTinh.getsize(triet)

            self.draw.rectangle((self.xyTuan[0] - ltu/2 - self.padding, self.xyTuan[1] - wtu/2,
                                self.xyTuan[0] + ltu/2 + self.padding, self.xyTuan[1] + wtu/2 + self.padding),
                                fill=(0, 0, 0))
            self.draw.text((self.xyTuan[0] - ltu/2, self.xyTuan[1] - wtu/2),
                           tuan, font=fontPhuTinh,
                           fill=mauSac['tuanTriet'])

            self.draw.rectangle((self.xyTriet[0] - ltr/2 - self.padding, self.xyTriet[1] - wtr/2,
                                self.xyTriet[0] + ltr/2 + self.padding, self.xyTriet[1] + wtr/2),
                                fill=(0, 0, 0))
            self.draw.text((self.xyTriet[0] - ltr/2, self.xyTriet[1] - wtr/2),
                           triet, font=fontPhuTinh,
                           fill=mauSac['tuanTriet'])

    def _nhapCungChu(self, cung, a, b):
        tenCungChu = cung.cungChu
        if (cung.cungThan is True):
            tenCungChu += " ({})".format("Thân")
        tenCungChu = (tenCungChu).decode('utf-8').upper()
        x = (a[0] + b[0]) / 2 - fontCungTen.getsize(tenCungChu)[0] / 2
        y = a[1] + 13
        self.draw.text((x, y), tenCungChu, font=fontCungTen, fill=cungTen)

    def _nhapTieuHan(self, cungID):
        pass

    def _nhapChinhTinh(self, sao, a, b):
        for s in sao:
            if s['saoLoai'] == 1:
                if s['saoDacTinh'] is not None:
                    s['saoTen'] += "({})".format(s['saoDacTinh'])
                tenSao = (s['saoTen']).decode('utf-8').upper()
                xViTriChinhTinh = (a[0] + b[0]) / 2 - \
                    fontChinhTinh.getsize(tenSao)[0] / 2
                try:
                    yViTriChinhTinh = yViTriChinhTinh + 30
                except:
                    yViTriChinhTinh = a[1] + 35
                self.draw.text((xViTriChinhTinh, yViTriChinhTinh), tenSao,
                               font=fontChinhTinh, fill=mauSac[s['cssSao']])

    def _nhapPhuTinh(self, sao, a, b):
        for s in sao:
            if s['saoDacTinh'] is not None:
                s['saoTen'] += "({})".format(s['saoDacTinh'])
            tenSao = (s['saoTen']).decode('utf-8')
            if (s['saoLoai'] < 10 and
                    s['vongTrangSinh'] == 0 and s['saoLoai'] != 1):
                xSaoTot = a[0] + 10
                try:
                    ySaoTot = ySaoTot + 25
                except:
                    ySaoTot = a[1] + 100
                draw.text((xSaoTot, ySaoTot), tenSao,
                          font=fontPhuTinh, fill=mauSac[s['cssSao']])
            if (s['saoLoai'] > 10 and
                    s['vongTrangSinh'] == 0 and s['saoLoai'] != 1):
                xSaoXau = b[0] - 10 - fontPhuTinh.getsize(tenSao)[0]
                try:
                    ySaoXau = ySaoXau + 25
                except:
                    ySaoXau = a[1] + 100
                self.draw.text((xSaoXau, ySaoXau), tenSao,
                               font=fontPhuTinh, fill=mauSac[s['cssSao']])

    def _nhapVongTrangSinh(self, sao, a, b):
        for s in sao:
            if s['vongTrangSinh'] == 1:
                tenSao = (s['saoTen']).decode('utf-8').upper()
                xViTriVongTrangSinh = (a[0] + b[0]) / 2 - \
                    fontPhuTinh.getsize(tenSao)[0] / 2
                yViTriVongTrangSinh = a[1] + 320
                self.draw.text((xViTriVongTrangSinh, yViTriVongTrangSinh),
                               tenSao, font=fontPhuTinh,
                               fill=mauSac[s['cssSao']])

    def _nhapDaiHan(self, cung, a, b):
        xDaiHan = b[0] - 35
        yDaiHan = a[1] + 5
        self.draw.text((xDaiHan, yDaiHan), str(cung.cungDaiHan),
                       font=fontCungTen, fill=(0, 0, 0))

    def _nhapHanhCung(self, cung, a, b, c, d):
        xHanhCung = a[0] + 5
        yHanhCung = a[1] + 5
        self.draw.text(
            (xHanhCung, yHanhCung),
            (cung.hanhCung).decode('utf-8'), font=fontCungTen, fill=(0, 0, 0)
        )

    def _nhapTieuHan(self, cung, a, b):
        xTieuHan = a[0] + 5
        yTieuHan = a[1] + 330
        self.draw.text(
            (xTieuHan, yTieuHan),
            (cung.cungTieuHan).decode('utf-8'),
            font=fontCungTen, fill=(0, 0, 0)
        )

    def _nhapHeaderThienBan(self):
        text = u"Lá số tử vi".decode('utf8')
        x, y = fontThuPhap.getsize(text)
        self.draw.text((600-x/2, 400), text, font=fontThuPhap, fill=(0, 0, 0))

    def _nhapTenNguoiLap(self):
        text = self.thienBan.ten.decode('utf8')
        x, y = fontPhuTinh.getsize(text)
        self.draw.text((600-x/2, 480), text, font=fontPhuTinh,
                       fill=mauSac['hanhHoa'])

    def _nhapAmDuongThuanLy(self):
        text = u"{} {}, {}".format(
            self.thienBan.amDuongNamSinh.decode('utf-8'),
            self.thienBan.namNu.decode('utf-8'),
            self.thienBan.amDuongMenh.decode('utf-8')
        )
        x, y = fontPhuTinh.getsize(text)
        self.draw.text((600-x/2, 510), text, font=fontPhuTinh,
                       fill=mauSac['cungTen'])

    def _nhapBanMenh(self):
        menh = self.thienBan.menh
        css = nguHanh(menh)['css']
        text = u"Mệnh {}".format(
            self.thienBan.banMenh.decode('utf-8')
        )
        x, y = fontPhuTinh.getsize(text)
        self.draw.text((600-x/2, 535), text, font=fontPhuTinh,
                       fill=mauSac[css])

    def _nhapCuc(self):
        text = u"Cục: {}".format(
            self.thienBan.tenCuc.decode('utf-8')
        )
        x, y = fontPhuTinh.getsize(text)
        self.draw.text((600-x/2, 560), text, font=fontPhuTinh,
                       fill=mauSac['cungTen'])

    def _menhThanChu(self):
        menhChu = u"Chủ mệnh: {}".format(
            self.thienBan.menhChu.decode('utf8')
        )
        thanChu = u"Chủ thân: {}".format(
            self.thienBan.thanChu.decode('utf8')
        )
        a, b = fontPhuTinh.getsize(menhChu)
        c, d = fontPhuTinh.getsize(thanChu)
        self.draw.text((600-a/2, 585), menhChu, font=fontPhuTinh,
                       fill=mauSac['cungTen'])
        self.draw.text((600-c/2, 610), thanChu, font=fontPhuTinh,
                       fill=mauSac['cungTen'])

    def _sinhKhac(self):
        text = u"{}".format(
            self.thienBan.sinhKhac.decode('utf-8')
        )
        x, y = fontPhuTinh.getsize(text)
        self.draw.text((600-x/2, 635), text, font=fontPhuTinh,
                       fill=mauSac['cungTen'])

    def _batTu(self):
        cssNam, napAmNam = nguHanh(nguHanhNapAm(self.thienBan.chiNam, self.thienBan.canNam))['css'], nguHanhNapAm(self.thienBan.chiNam, self.thienBan.canNam, True)
        cssThang, napAmThang = nguHanh(nguHanhNapAm(self.thienBan.chiThang, self.thienBan.canThang))['css'], nguHanhNapAm(self.thienBan.chiThang, self.thienBan.canThang, True)
        cssNgay, napAmNgay = nguHanh(nguHanhNapAm(self.thienBan.chiNgay, self.thienBan.canNgay))['css'], nguHanhNapAm(self.thienBan.chiNgay, self.thienBan.canNgay, True)
        cssGio, napAmGio = nguHanh(nguHanhNapAm(self.thienBan.chiGioSinh['id'], self.thienBan.canGioSinh))['css'], nguHanhNapAm(self.thienBan.chiGioSinh['id'], self.thienBan.canGioSinh, True)
        x1, x2, x3, x4, x5 = 364, 484, 604, 724, 844
        y1, y2, y3, y4, y5 = 680, 705, 730, 755, 780
        nam = u"Năm"
        thang = u"Tháng"
        ngay = u"Ngày"
        gio = u"Giờ"
        duong = u"Dương lịch"
        am = u"Âm lịch"

        self.draw.text((x2 - fontBatTu.getsize(nam)[0]/2, y1), nam, font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x3 - fontBatTu.getsize(thang)[0]/2, y1), thang, font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x4 - fontBatTu.getsize(ngay)[0]/2, y1), ngay, font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x5 - fontBatTu.getsize(gio)[0]/2, y1), gio, font=fontBatTu, fill=mauSac["cungTen"])

        self.draw.text((x1 - fontBatTu.getsize(duong)[0]/2, y2), duong, font=fontBatTu, fill=mauSac["phuHoa"])
        self.draw.text((x2 - fontBatTu.getsize(str(self.thienBan.namDuong))[0]/2, y2), str(self.thienBan.namDuong), font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x3 - fontBatTu.getsize(str(self.thienBan.thangDuong))[0]/2, y2), str(self.thienBan.thangDuong), font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x4 - fontBatTu.getsize(str(self.thienBan.ngayDuong))[0]/2, y2), str(self.thienBan.ngayDuong), font=fontBatTu, fill=mauSac["cungTen"])

        self.draw.text((x1 - fontBatTu.getsize(am)[0]/2, y3), am, font=fontBatTu, fill=mauSac["phuHoa"])
        # self.draw.text((x2 - fontBatTu.getsize(str(self.thienBan.namAm))[0]/2, y3), str(self.thienBan.namAm), font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x3 - fontBatTu.getsize(str(self.thienBan.thangAm))[0]/2, y3), str(self.thienBan.thangAm), font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x4 - fontBatTu.getsize(str(self.thienBan.ngayAm))[0]/2, y3), str(self.thienBan.ngayAm), font=fontBatTu, fill=mauSac["cungTen"])
        self.draw.text((x5 - fontBatTu.getsize((self.thienBan.chiGioSinh['tenChi']).decode('utf8'))[0]/2, y3), self.thienBan.chiGioSinh['tenChi'].decode('utf8'), font=fontBatTu, fill=mauSac["cungTen"])

        self.draw.text((x1 - fontBatTu.getsize(u"Can Chi")[0]/2, y4), u"Can Chi", font=fontBatTu, fill=mauSac["phuHoa"])
        self.draw.text((x1 - fontBatTu.getsize(u"Nạp âm")[0]/2, y5), u"Nạp  âm", font=fontBatTu, fill=mauSac["phuHoa"])

        namAm = u"{} {}".format(self.thienBan.canNamTen, self.thienBan.chiNamTen)
        self.draw.text((x2 - fontBatTu.getsize(namAm)[0]/2, y4), namAm, font=fontBatTu, fill=mauSac[cssNam])
        yn5 = y5
        for text in napAmNam.split():
            self.draw.text((x2 - fontBatTu.getsize(text.decode('utf8'))[0]/2, yn5), text.decode('utf8'), font=fontBatTu, fill=mauSac[cssNam])
            yn5 += 20

        thangAm = u"{} {}".format(self.thienBan.canThangTen, self.thienBan.chiThangTen)
        self.draw.text((x3 - fontBatTu.getsize(thangAm)[0]/2, y4), thangAm, font=fontBatTu, fill=mauSac[cssThang])
        tn5 = y5
        for text in napAmThang.split():
            self.draw.text((x3 - fontBatTu.getsize(text.decode('utf8'))[0]/2, tn5), text.decode('utf8'), font=fontBatTu, fill=mauSac[cssThang])
            tn5 += 20

        ngayAm = u"{} {}".format(self.thienBan.canNgayTen, self.thienBan.chiNgayTen)
        self.draw.text((x4 - fontBatTu.getsize(ngayAm)[0]/2, y4), ngayAm, font=fontBatTu, fill=mauSac[cssNgay])
        nn5 = y5
        for text in napAmNgay.split():
            self.draw.text((x4 - fontBatTu.getsize(text.decode('utf8'))[0]/2, nn5), text.decode('utf8'), font=fontBatTu, fill=mauSac[cssNgay])
            nn5 += 20

        gioAm = u"{}".format(self.thienBan.gioSinh)
        self.draw.text((x5 - fontBatTu.getsize(gioAm)[0]/2, y4), gioAm, font=fontBatTu, fill=mauSac[cssGio])
        gn5 = y5
        for text in napAmGio.split():
            self.draw.text((x5 - fontBatTu.getsize(text.decode('utf8'))[0]/2, gn5), text.decode('utf8'), font=fontBatTu, fill=mauSac[cssGio])
            gn5 += 20


myc = taoFileAnh(draw, db, thienBan)
base.save(os.path.join(os.path.dirname(BASE_DIR), 'thuvienlaso/test.png'), 'PNG')
print("fine")
