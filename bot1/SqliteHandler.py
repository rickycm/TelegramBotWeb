#!/usr/bin/python
# coding:utf-8

# TelegramBotWeb - SqliteHandler.py
# 2018/9/28 11:13
"""    sqlite数据库操作工具类    database: 数据库文件地址 绝对路径"""

__author__ = "WangYuan <owensnow@qq.com>"

import sqlite3


class SqliteHandler:

    _connection = None

    def __init__(self, database):
        # 连接数据库
        self._connection = sqlite3.connect(database, check_same_thread=False)

    def execute(self, sql, args=[], result_dict=True, commit=True)->list:
        if result_dict:
            self._connection.row_factory = self._dict_factory
        else:
            self._connection.row_factory = None
            # 获取游标
        _cursor = self._connection.cursor()
        # 执行SQL获取结果
        _cursor.execute(sql, args)
        if commit:
            self._connection.commit()
        data = _cursor.fetchall()
        _cursor.close()
        return data

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


if __name__ == '__main__':
    db = SqliteHandler('D:\pythonProject\TelegramBotWeb\db.sqlite3')
    #  print(db.execute("select name from sqlite_master where type=?", ['table']))
    #  print(db.execute("pragma table_info([user])"))
    #  print(execute("insert into user(id, name, password) values (?, ?, ?)", [2, "李四", "123456"]))
    #  print(db.execute("select id, name userName, password pwd from user"))
    #  print(db.execute("select * from user", result_dict=False))
    print(db.execute("select * from auth_user"))
