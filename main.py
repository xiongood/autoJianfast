from lxml import etree
import random
import requests

# 获取第一页 图片地址
srcs = []
#url = r'https://www.yaash.cn/tag/second-dimension/'#分类
#url = r'https://www.yaash.cn/?cat=&s=%E6%B8%85%E7%BA%AF'#关键字搜索
url = r'https://www.yaash.cn/'#主页
response = requests.get(url)
# print(response.status_code)
# 检查请求是否成功
if response.status_code == 200:
    response.encoding = 'GBK'
    content = response.text
    # print(content)
    tree = etree.HTML(content)
    srcs = tree.xpath("//img[contains(@style, 'object-fit: cover;')]/@src")
# for src in srcs:
#     print( src)
src = random.choice(srcs)
# print(src)
# 替换
src = src.replace('@small', '@middle')
#
# 目标URL
url = r"https://www.jianfast.com/home/bg/show?type=update&picurl="+src
print(url)
# 拼装Cookie（字典形式）
headers = {
    "Cookie": "wel_code=1; u=b31de6781203a97eb0b17b388e6d91ab; Hm_lvt_7cfb32da5a4a5240b600dddec4023a51=1752626936,1752627273,1752627864,1752628707; HMACCOUNT=6B860EBD77E2A2E0; PHPSESSID=0cuvgq2qcv7hqomspotb1aefdc; Hm_lpvt_7cfb32da5a4a5240b600dddec4023a51=1752628765",
}

# 发送带有Cookie的GET请求
response = requests.get(url, headers=headers)



