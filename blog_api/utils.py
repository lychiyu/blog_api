# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""


class NamedConst:
    choices = tuple()

    @classmethod
    def name_of(cls, v):
        for choice in cls.choices:
            if choice[0] == v:
                return choice[1]
        return "未知"


class States(NamedConst):
    DELETE = 0
    NORMAL = 1

    choices = (
        (NORMAL, '正常'),
        (NORMAL, '删除')
    )
