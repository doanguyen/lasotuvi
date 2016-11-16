# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

base = Image.open(os.path.join(BASE_DIR, 'imgbackend', 'background.png'))

# get a font
fontChinhTinh = ImageFont.truetype('imgbackend/noto-serif/NotoSerif-Bold.ttf', 25)
fontPhuTinh = ImageFont.truetype('imgbackend/noto-serif/NotoSerif-Bold.ttf', 25)

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

draw.text((5, (x/40-2)/2), u"Tý", font=fontPhuTinh, fill=(0, 0, 0))
msg = u"ĐIỀN TRẠCH"
w, h = fontChinhTinh.getsize(msg)
draw.point((x/10, (y/40-2)/2), fill=hanhHoa)
draw.multiline_text((x/8-w/2, (y/40-2)/2), msg, font=fontChinhTinh, fill=cungTen, align="center")
draw.multiline_text((x/8-w/2, (y/40-2)/2+h), u"THIÊN CƠ (V)", font=fontChinhTinh, fill=hanhMoc, align="center")
draw.multiline_text((x/8-w/2, y/2), u"QUAN ĐỚI\nVai4", font=fontChinhTinh, fill=hanhTho, align="center")

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
        pass
