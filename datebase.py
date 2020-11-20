# 函数.py
from mysql.connector import connect


# 游标
def get_connection():
    conn = connect(user='root', password='', database='teamwork')
    cursor = conn.cursor()

    return conn, cursor


# show用户信息
def show_all_users():
    conn, cursor = get_connection()

    sql = 'select `username` from `users`'
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


# 保存添加用户
def save_add(username, student_nums):
    conn, cursor = get_connection()

    sql = 'insert into `users` (`username`, `student_nums`) values (%s, %s)'
    cursor.execute(sql, (username, student_nums))

    conn.commit()
    cursor.close()
    conn.close()
