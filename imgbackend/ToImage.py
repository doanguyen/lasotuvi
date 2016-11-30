# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os
from src.DiaBan import diaBan
from src.ThienBan import lapThienBan
from src import lstv

hoTen = "w"
ngaySinh = 24
thangSinh = 10
namSinh = 1991
gioSinh = 4
gioiTinh = 1
duongLich = True
timeZone = 7

db = lstv.lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh,
                    gioSinh, gioiTinh, duongLich, timeZone)
thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                       gioSinh, gioiTinh, hoTen, db)
thapNhiCung = db.thapNhiCung
cung = (thapNhiCung[2])


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
    'cungTen': "#2196f3"
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

draw.text((5, 5), u"Tý", font=fontPhuTinh, fill=(0, 0, 0))
draw.text((295 - fontPhuTinh.getsize(u"35")
           [0], 5), u"35", font=fontPhuTinh, fill=(0, 0, 0))
msg = u"ĐIỀN TRẠCH"
w, h = fontChinhTinh.getsize(msg)
draw.text((x / 8 - w / 2, 5), msg, font=fontCungTen, fill=cungTen)

# Chính tinh
draw.text((x / 8 - w / 2 - 20, 30), u"THIÊN CƠ (V)",
          font=fontChinhTinh, fill=hanhMoc)
draw.text((x / 8 - w / 2, 60), u"TỬ VI (V)", font=fontChinhTinh, fill=hanhTho)

# Phụ Tinh
draw.text((10, 100), u"Ân Quang", font=fontPhuTinh, fill=hanhMoc)
draw.text((10, 125), u"Thiên Đức", font=fontPhuTinh, fill=hanhHoa)
draw.text((10, 150), u"Thiên Y", font=fontPhuTinh, fill=hanhThuy)
draw.text((10, 175), u"Hỏa Tinh (Đ)", font=fontPhuTinh, fill=hanhHoa)
draw.text((10, 200), u"Văn Xương", font=fontPhuTinh, fill=hanhKim)
draw.text((10, 225), u"Bát Tọa", font=fontPhuTinh, fill=hanhMoc)
draw.text((10, 250), u"Lộc Tồn", font=fontPhuTinh, fill=hanhTho)

draw.text((290 - fontPhuTinh.getsize(u"Lộc Tồn")
           [0], 100), u"Lộc Tồn", font=fontPhuTinh, fill=hanhTho)
draw.text((290 - fontPhuTinh.getsize(u"Văn Xương (M)")
           [0], 125), u"Văn Xương (M)", font=fontPhuTinh, fill=hanhKim)

# Truong sinh
draw.text((x / 8 - fontPhuTinh.getsize(u"Tuyệt")
           [0] / 2, 330), u"Tuyệt", font=fontPhuTinh, fill=hanhKim)
draw.text((10, 330), u"Mão", font=fontPhuTinh, fill=hanhKim)


def nhapCung(Sao, a=(), b=(), c=(), d=()):
    """
    a. . . . .b
    .         .
    .         .
    .         .
    .         .
    c. . . . .d
    """
    self.anCungChu()
    self.anChinhTinh()
    self.anPhuTinh()
    self.anDaiHan()
    self.anTieuHan()
    self.anDiaChiCung()
    self.anNguHanhCung()
    self.anVongTrangSinh()
    return self


def nhapThienBan(self, thienBan):
    pass


def nhapCungChu(draw, cung, a, b, c, d):
    tenCungChu = cung.cungChu
    if (cung.cungThan is True):
        tenCungChu += " ({})".format("Thân")
    tenCungChu = unicode(tenCungChu, 'utf-8').upper()
    x = (a[0] + b[0])/2 - fontCungTen.getsize(tenCungChu)[0] / 2
    y = a[1] + 5
    draw.text((x, y), tenCungChu, font=fontCungTen, fill=cungTen)


def nhapChinhTinh(draw, sao, a, b, c, d):
    for s in sao:
        if s['saoLoai'] == 1:
            if s['saoDacTinh'] is not None:
                s['saoTen'] += "({})".format(s['saoDacTinh'])
            tenSao = unicode(s['saoTen'], 'utf-8').upper()
            xViTriChinhTinh = (a[0] + b[0]) / 2 - fontChinhTinh.getsize(tenSao)[0] / 2
            try:
                yViTriChinhTinh = yViTriChinhTinh + 30
            except:
                yViTriChinhTinh = a[1] + 30
            draw.text((xViTriChinhTinh, yViTriChinhTinh), tenSao, font=fontChinhTinh, fill=mauSac[s['cssSao']])
    return draw


def nhapPhuTinh(draw, sao, a, b, c, d):
    for s in sao:
        if s['saoDacTinh'] is not None:
            s['saoTen'] += "({})".format(s['saoDacTinh'])
        tenSao = unicode(s['saoTen'], 'utf-8')
        if (s['saoLoai'] < 10 and s['vongTrangSinh'] == 0 and s['saoLoai'] != 1):
            xSaoTot = a[0] + 10
            try:
                ySaoTot = ySaoTot + 25
            except:
                ySaoTot = a[1] + 100
            draw.text((xSaoTot, ySaoTot), tenSao, font=fontPhuTinh, fill=mauSac[s['cssSao']])
        if (s['saoLoai'] > 10 and s['vongTrangSinh'] == 0 and s['saoLoai'] != 1):
            xSaoXau = b[0] - 10 - fontPhuTinh.getsize(tenSao)[0]
            try:
                ySaoXau = ySaoXau + 25
            except:
                ySaoXau = a[1] + 100
            draw.text((xSaoXau, ySaoXau), tenSao, font=fontPhuTinh, fill=mauSac[s['cssSao']])


def nhapVongTrangSinh(draw, sao, a, b, c, d):
    for s in sao:
        if s['vongTrangSinh'] == 1:
            tenSao = unicode(s['saoTen'], 'utf-8').upper()
            xViTriVongTrangSinh = (a[0] + b[0]) / 2 - fontPhuTinh.getsize(tenSao)[0] / 2
            yViTriVongTrangSinh = a[1] + 330
            draw.text((xViTriVongTrangSinh, yViTriVongTrangSinh), tenSao, font=fontPhuTinh, fill=mauSac[s['cssSao']])


def nhapDaiHan(draw, cung, a, b, c, d):
    xDaiHan = b[0] - 30
    yDaiHan = a[1] + 5
    draw.text((xDaiHan, yDaiHan), str(cung.cungDaiHan), font=fontCungTen, fill=(0, 0, 0))


def nhapHanhCung(draw, cung, a, b, c, d):
    xHanhCung = a[0] + 5
    yHanhCung = a[1] + 5
    draw.text((xHanhCung, yHanhCung), unicode(cung.hanhCung, 'utf-8'), font=fontCungTen, fill=(0, 0, 0))


def nhapTieuHan(draw, cung, a, b, c, d):
    xTieuHan = a[0] + 5
    yTieuHan = a[1] + 330
    draw.text((xTieuHan, yTieuHan), unicode(cung.cungTieuHan, 'utf-8'), font=fontCungTen, fill=(0, 0, 0))


nhapCungChu(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))
nhapChinhTinh(draw, cung.cungSao, (300, 0), (600, 0), (300, 300), (600, 300))
nhapPhuTinh(draw, cung.cungSao, (300, 0), (600, 0), (300, 300), (600, 300))
nhapVongTrangSinh(draw, cung.cungSao, (300, 0), (600, 0), (300, 300), (600, 300))
nhapDaiHan(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))
nhapHanhCung(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))
nhapTieuHan(draw, cung, (300, 0), (600, 0), (300, 300), (600, 300))

base.save(os.path.join(BASE_DIR, 'imgbackend/test.png'), 'PNG')
print "fine"