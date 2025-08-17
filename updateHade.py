import sys
import mysql.connector
from mysql.connector import Error
import requests


src = sys.argv[1]

# 处理参数（这里只是简单展示，你可以根据需要修改）
# print(f"你输入的参数是: {src}")
# print(f"参数长度为: {len(src)}")
# print(f"参数大写形式: {src.upper()}")

try:
    connection = mysql.connector.connect(
        host='mysql2.sqlpub.com',
        database='xiongood',
        user='xiongood',
        password='pdeIwVJvQivhj9Mx',
        port='3307'  # 使用指定的端口号
    )
    if connection.is_connected():
        db_Info = connection.server_info
        print(f"已连接到 MySQL 服务器版本: {db_Info}")
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print(f"当前数据库: {record}")

        update_values = []
        update_query = f"""
                    UPDATE JIANFAST_SRC
                    SET IS_HATE = %s
                    WHERE SRC = %s
                    """
        update_values.append(1)
        update_values.append(src)
        cursor.execute(update_query, tuple(update_values))
        connection.commit()

except Error as e:
    print(f"连接数据库时发生错误: {e}")


url = "https://api.github.com/repos/xiongood/autoJianfast/dispatches"
headers = {
    "Content-Type": "application/json",
    "Authorization": "token xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "Accept": "application/vnd.github.v3+json"
}
data = {
    "event_type": "trigger-workflow"
}

try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f"请求错误: {err}")

