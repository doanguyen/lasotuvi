# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os
from src.DiaBan import diaBan
from src.ThienBan import lapThienBan
from src import lstv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

hoTen = "w"
ngaySinh = 3
thangSinh = 2
namSinh = 1980
gioSinh = 1
gioiTinh = 1
duongLich = True
timeZone = 7

db = lstv.lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh,
                    gioSinh, gioiTinh, duongLich, timeZone)
thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                       gioSinh, gioiTinh, hoTen, db)
thapNhiCung = db.thapNhiCung
cung = (thapNhiCung[12])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

base = Image.open(os.path.join(BASE_DIR, 'imgbackend', 'background.png'))

# get a font
fontChinhTinh = ImageFont.truetype(os.path.join(
    BASE_DIR, 'imgbackend/noto-serif/NotoSerif-Bold.ttf'), 24)
fontPhuTinh = ImageFont.truetype(os.path.join(
    BASE_DIR, 'imgbackend/noto-serif/NotoSerif-Bold.ttf'), 20)
fontCungTen = ImageFont.truetype(os.path.join(
    BASE_DIR, 'imgbackend/noto-serif/NotoSerif-Bold.ttf'), 20)

# màu ngũ hành
mauSac = {
    'hanhKim': "#9E9E9E",
    'hanhThuy': "#000100",
    'hanhMoc': "#4CAF50",
    'hanhHoa': "#a71a14",
    'hanhTho': "#e6bd37",
    'cungTen': "#2196f3",
    'tuanTriet': "#FFFFFF"
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
# print (x, y)
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


def nhapCungChu(draw, cung, a, b, c, d):
    tenCungChu = cung.cungChu
    if (cung.cungThan is True):
        tenCungChu += " ({})".format("Thân")
    tenCungChu = (tenCungChu).decode('utf-8').upper()
    x = (a[0] + b[0]) / 2 - fontCungTen.getsize(tenCungChu)[0] / 2
    y = a[1] + 5
    draw.text((x, y), tenCungChu, font=fontCungTen, fill=cungTen)


def nhapChinhTinh(draw, sao, a, b, c, d):
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
                yViTriChinhTinh = a[1] + 30
            draw.text((xViTriChinhTinh, yViTriChinhTinh), tenSao,
                      font=fontChinhTinh, fill=mauSac[s['cssSao']])


def nhapPhuTinh(draw, sao, a, b, c, d):
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
            draw.text((xSaoXau, ySaoXau), tenSao,
                      font=fontPhuTinh, fill=mauSac[s['cssSao']])


def nhapVongTrangSinh(draw, sao, a, b, c, d):
    for s in sao:
        if s['vongTrangSinh'] == 1:
            tenSao = (s['saoTen']).decode('utf-8').upper()
            xViTriVongTrangSinh = (a[0] + b[0]) / 2 - \
                fontPhuTinh.getsize(tenSao)[0] / 2
            yViTriVongTrangSinh = a[1] + 330
            draw.text((xViTriVongTrangSinh, yViTriVongTrangSinh),
                      tenSao, font=fontPhuTinh, fill=mauSac[s['cssSao']])


def nhapDaiHan(draw, cung, a, b, c, d):
    xDaiHan = b[0] - 30
    yDaiHan = a[1] + 5
    draw.text((xDaiHan, yDaiHan), str(cung.cungDaiHan),
              font=fontCungTen, fill=(0, 0, 0))


def nhapHanhCung(draw, cung, a, b, c, d):
    xHanhCung = a[0] + 5
    yHanhCung = a[1] + 5
    draw.text(
              (xHanhCung, yHanhCung),
              (cung.hanhCung).decode('utf-8'), font=fontCungTen, fill=(0, 0, 0)
             )


def nhapTieuHan(draw, cung, a, b, c, d):
    xTieuHan = a[0] + 5
    yTieuHan = a[1] + 330
    draw.text(
              (xTieuHan, yTieuHan),
              (cung.cungTieuHan).decode('utf-8'),
              font=fontCungTen, fill=(0, 0, 0)
              )


nhapCungChu(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))
nhapChinhTinh(draw, cung.cungSao, (300, 0), (600, 0), (300, 300), (600, 300))
nhapPhuTinh(draw, cung.cungSao, (300, 0), (600, 0), (300, 300), (600, 300))
nhapVongTrangSinh(draw, cung.cungSao, (300, 0),
                  (600, 0), (300, 300), (600, 300))
nhapDaiHan(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))
nhapHanhCung(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))
nhapTieuHan(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))

xyTuanTriet = {
    1: (1082, 600),
    3: (1, 1),
    5: (1, 1),
    7: (1, 1),
    9: (1, 1),
    11: (1010, 1082)
}

# print xyTuanTriet[2]


class taoFileAnh(object):
    def __init__(self, drawContainer, diaBan, thienBan):
        super(taoFileAnh, self).__init__()
        self.draw = drawContainer
        self.diaBan = diaBan
        self.thienBan = thienBan
        self.viTriTriet = []
        self.viTriTuan = []

        self._tuanTriet()

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
        self.xyTuan = xyTuanTriet[min(self.viTriTuan)]
        self.xyTriet = xyTuanTriet[min(self.viTriTriet)]
        self.draw.rectangle((self.xyTuan[0], self.xyTuan[1]-15, self.xyTuan[0]+80, self.xyTuan[1]+15), fill=(0, 0, 0))
        self.draw.text((self.xyTuan[0]+10, self.xyTuan[1]-15),
                       "Tuần".decode("utf-8").upper(), font=fontPhuTinh,
                       fill=mauSac['tuanTriet'])

print fontPhuTinh.getsize("TUẦN")

myc = taoFileAnh(draw, db, thienBan)
base.save(os.path.join(BASE_DIR, 'imgbackend/test.png'), 'PNG')
print("fine")
print myc.__dict__
