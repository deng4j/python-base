# pip install pyzbar
from PIL import Image
from pyzbar import pyzbar


# WiFi二维码查看密码
def scan_qr_code(image_path, threshold=150):
    image = Image.open(image_path)  # 将二进制转为PIL格式图片
    # 将图像转换为灰度图
    gray_image = image.convert('L')
    # 将灰度图转换为二值图
    binary_image1 = gray_image.point(lambda x: 0 if x < threshold else 255, '1')
    binary_image2 = gray_image.point(lambda x: 255 if x < threshold else 0, '1')


    for i in binary_image1, binary_image2:
        barcodes = pyzbar.decode(i)
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")
                return barcode_data
    else:
        return '扫码失败'
print(scan_qr_code('44485f8a0d623fc8ac2dd3178980e08.jpg'))

