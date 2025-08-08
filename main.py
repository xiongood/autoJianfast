from lxml import etree
import random
import requests
import smtplib
from email.mime.text import MIMEText

# 获取第一页 图片地址
srcs = []

# 在0123中取随机数
index = random.randint(0, 3)
# url = r'https://www.yaash.cn/'#主页
url = r'https://www.bizhihui.com/page/'+str(index)#主页
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    response.encoding = 'UTF-8'
    content = response.text
    # print(content)
    tree = etree.HTML(content)
    srcs = tree.xpath("//img[contains(@width, '450')]/@src")

# print(srcs)
src = random.choice(srcs)

# 替换
# src = src.replace('@small', '@middle')
src = src.replace('-pcthumbs', '')
print(src)

# # 拼装Cookie（字典形式）
headers = {
    "cookie": "wel_code=1; u=b31de6781203a97eb0b17b388e6d91ab; act=1; Hm_lvt_7cfb32da5a4a5240b600dddec4023a51=1754461713,1754461791,1754461911,1754463844; HMACCOUNT=D3BBBE66B6CCC6D8; PHPSESSID=lelo28sn929ul2pnjfhppcth03; loadingbg=https%3A//img.netbian.com/file/2024/0325/234506wB8aC.jpg; Hm_lpvt_7cfb32da5a4a5240b600dddec4023a51=1754464974",
}

data = {
    "bg":src
}
# 发送post请求
response = requests.post(r'https://www.jianfast.com/home/bg/save', data,headers=headers)
print(response.status_code)
if response.status_code == 200:
    print("保存成功")
else:
    print("保存失败")
    # 发送邮件
    """发送纯文字邮件"""
    # 创建邮件内容
    msg = MIMEText('简法壁纸发送失败'+src, 'plain', 'utf-8')
    msg['From'] = 'java0417@163.com'
    msg['To'] = 'xiongood@88.com'
    msg['Subject'] = 'github Actions 通知'

    try:
        # 163邮箱的465端口需要用SMTP_SSL而非starttls
        with smtplib.SMTP_SSL('smtp.163.com', 465) as server:
            # 不需要调用starttls()，SSL连接本身就是加密的
            server.login('java0417@163.com', 'HLYAyKmG4Fg4jskQ')
            server.send_message(msg)
        print("邮件发送成功！")
    except Exception as e:
        print(f"发送失败: {str(e)}")

