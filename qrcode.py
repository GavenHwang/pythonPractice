# -*- coding: utf-8 -*-
import qrcode

qr = qrcode.QRCode(
    # 设置Version，范围1~40 即21*21 ~ 177*177
    version=1,
    # 纠错率，有L,M,Q,H四种，分别对应7%，15%，25%，30%，默认为ERROR_CORRECT_M
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # 每个方块的像素个数
    box_size=10,
    # 二维码距图像外围边框的距离，默认为4
    border=4,
)
qr.add_data('https://github.com')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
# 直接显示二维码
print(img.show())

import pyqrcode
# 生成 QRCode
url = pyqrcode.create("hello world!")
# 创建并保存图片，矢量图
# url.svg("./myqr.svg", scale=8) 默认黑白的
url.svg("./myqr.svg", scale=8, background="white", module_color="#7D007D")
# 生成 png 文件之前需先安装pypng
url.png('./code.png', scale=5, module_color="#7D007D", background=[0xff, 0xff, 0xcc])
