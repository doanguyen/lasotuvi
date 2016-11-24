# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

base = Image.open(os.path.join(BASE_DIR, 'imgbackend', 'background.png'))

# get a font
fontChinhTinh = ImageFont.truetype('imgbackend/noto-serif/NotoSerif-Bold.ttf', 24)
fontPhuTinh = ImageFont.truetype('imgbackend/noto-serif/NotoSerif-Bold.ttf', 20)
fontCungTen = ImageFont.truetype('imgbackend/noto-serif/NotoSerif-Bold.ttf', 20)

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
draw.line([x-width, 0, x-width, y-width], fill=(0, 0, 0, 100), width=width)
draw.line([0, y-width, x-width, y-width], fill=(0, 0, 0, 100), width=width)

draw.line([x/4-width, 0, x/4-width, y-width], fill=(0, 0, 0, 100), width=width)
draw.line([3*x/4-width, 0, 3*x/4-width, y-width], fill=(0, 0, 0, 100), width=width)
draw.line([0, y/4-width, x-width, y/4-width], fill=(0, 0, 0, 100), width=width)
draw.line([0, 3*y/4-width, x-width, 3*y/4-width], fill=(0, 0, 0, 100), width=width)

draw.line([x/2-2, 0, x/2-2, y/4-2], fill=(0, 0, 0, 100), width=width)
draw.line([x/2-2, 3*y/4-2, x/2-2, y-2], fill=(0, 0, 0, 100), width=width)
draw.line([0, y/2-2, x/4-2, y/2-2], fill=(0, 0, 0, 100), width=width)
draw.line([3*x/4-2, y/2-2, x-2, y/2-2], fill=(0, 0, 0, 100), width=width)
# Hoàn thành phần khung

draw.text((5, 5), u"Tý", font=fontPhuTinh, fill=(0, 0, 0))
draw.text((295-fontPhuTinh.getsize(u"35")[0], 5), u"35", font=fontPhuTinh, fill=(0, 0, 0))
msg = u"ĐIỀN TRẠCH"
w, h = fontChinhTinh.getsize(msg)
draw.text((x/8-w/2, 5), msg, font=fontCungTen, fill=cungTen)

# Chính tinh
draw.text((x/8-w/2-20, 30), u"THIÊN CƠ (V)", font=fontChinhTinh, fill=hanhMoc)
draw.text((x/8-w/2, 60), u"TỬ VI (V)", font=fontChinhTinh, fill=hanhTho)

# Phụ Tinh
draw.text((10, 100), u"Ân Quang", font=fontPhuTinh, fill=hanhMoc)
draw.text((10, 125), u"Thiên Đức", font=fontPhuTinh, fill=hanhHoa)
draw.text((10, 150), u"Thiên Y", font=fontPhuTinh, fill=hanhThuy)
draw.text((10, 175), u"Hỏa Tinh (Đ)", font=fontPhuTinh, fill=hanhHoa)
draw.text((10, 200), u"Văn Xương", font=fontPhuTinh, fill=hanhKim)
draw.text((10, 225), u"Bát Tọa", font=fontPhuTinh, fill=hanhMoc)
draw.text((10, 250), u"Lộc Tồn", font=fontPhuTinh, fill=hanhTho)

draw.text((290-fontPhuTinh.getsize(u"Lộc Tồn")[0], 100), u"Lộc Tồn", font=fontPhuTinh, fill=hanhTho)
draw.text((290-fontPhuTinh.getsize(u"Văn Xương (M)")[0], 125), u"Văn Xương (M)", font=fontPhuTinh, fill=hanhKim)

# Truong sinh
draw.text((x/8-fontPhuTinh.getsize(u"Tuyệt")[0]/2, 330), u"Tuyệt", font=fontPhuTinh, fill=hanhKim)

base.save('imgbackend/test.png', 'PNG')
print "fine"


class nhapSao():
    def __init__(self, thienBan, thapNhiCung, imageHandle):
        super(nhapSao, self).__init__()
        self.thienBan = thienBan
        self.thapNhiCung = thapNhiCung
        self.imageHandle = imageHandle

    def nhapCung(Sao, a, b, c, d):
        """
        a. . . . .b
        .         .
        .         .
        .         .
        .         .
        c. . . . .d
        """
        self.anChinhTinh()
        self.anPhuTinh()
        self.anDaiHan()
        self.anTieuHan()
        self.anDiaChiCung()
        self.anNguHanhCung()
        self.anVongTrangSinh()
        return self

    def nhapThienBan(thienBan):
        pass
