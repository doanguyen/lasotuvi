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
cung = (thapNhiCung[1])


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


def nhapCungChu(draw, tenCungChu, a, b, c, d):
    tenCungChu = unicode(tenCungChu, 'utf-8').upper()
    x = (a[0] + b[0])/2 - fontChinhTinh.getsize(tenCungChu)[0] / 2
    y = a[1] + 5
    draw.text((x, y), tenCungChu, font=fontCungTen, fill=cungTen)
    return draw

nhapCungChu(draw, cung.cungChu, (300, 0), (600, 0), (300, 300), (600, 300))


def anChinhTinh(draw, saoChinhTinh):
    for chinhTinh in saoChinhTinh:
        xViTriChinhTinh = (a[0] + b[0]) / 2
        try:
            yViTriChinhTinh = yViTriChinhTinh + 30
        except:
            yViTriChinhTinh = a[1] + 30


base.save(os.path.join(BASE_DIR, 'imgbackend/test.png'), 'PNG')
print "fine"