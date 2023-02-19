import os
import random
# captcha是用于生成验证码图片的库
from captcha.image import ImageCaptcha


def random_captcha_text(num):
    # 验证码列表
    captcha_text = []
    for i in range(10):  # 0-9数字
        captcha_text.append(str(i))
    for i in range(65, 91):  # 对应从“A”到“Z”的ASCII码
        captcha_text.append(chr(i))
    for i in range(97, 123):  # 对应从“a”到“z”的ASCII码
        captcha_text.append(chr(i))

    # 从list中随机获取6个元素，作为一个片断返回
    example = random.sample(captcha_text, num)

    # 将列表里的片段变为字符串并返回
    verification_code = ''.join(example)
    return verification_code


# 生成字符对应的验证码
def generate_captcha_image():
    image = ImageCaptcha()
    # 获得随机生成的验证码
    captcha_text = random_captcha_text(8)
    # 把验证码列表转为字符串
    captcha_text = ''.join(captcha_text)
    # 生成验证码

    path = '/Users/deng4j/Downloads/temp/'
    if not os.path.exists(path):
        print("目录不存在!,已自动创建")
        os.makedirs(path)
    print("生成的验证码的图片为：", captcha_text)
    image.write(captcha_text, path + captcha_text + '.png')


if __name__ == '__main__':
    number = 10
    for i in range(number):
        generate_captcha_image()
