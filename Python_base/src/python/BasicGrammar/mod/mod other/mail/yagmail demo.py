import yagmail

# user@126.com 发件⼈邮箱
# 1234 发件⼈邮箱授权码(授权码，注意不是邮箱密码)
# smtp.126.com ⽹易126邮箱发件服务器 yag = yagmail.SMTP( user="user@126.com"

yag = yagmail.SMTP(user="1353976012@qq.com", password="chgqehbkdkorjfea", host='smtp.qq.com')

# 邮箱正⽂
contents = ['https://www.4399.com/flash/210650.htm',
            '一起来玩造梦无双']

# 发送邮件
# taaa@126.com 收件⼈邮箱
# subject 邮件主题
yag.send('1353976012@qq.com', 'subject', contents)
