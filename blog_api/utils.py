# coding: utf-8

"""
 Created by liuying on 2018/8/16.
"""
import qiniu, hashlib, time
from django.conf import settings


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
        (DELETE, '删除')
    )


class QiNiuUtil:

    def __init__(self, key=settings.QINIU_KEY, secret=settings.QINIU_SECRET,
                 bucket=settings.QINIU_BUCKET, prefix_url=settings.QINIU_URL,
                 path=settings.QINIU_PATH):
        self.key = key
        self.secret = secret
        self.bucket = bucket
        self.prefix_url = prefix_url
        self.path = path + '/'
        print(self.key, self.secret)
        self.q = qiniu.Auth(self.key, self.secret)

    def _token(self, key, exp=3600):
        return self.q.upload_token(self.bucket, key, exp)

    def upload(self, data, mime_type='application/octet-stream', key=None):
        key = key if key else '{}{}_{}'.format(self.path, int(time.time()), hashlib.md5(data).hexdigest())
        ret, info = qiniu.put_data(self._token(key), key, data, mime_type=mime_type)
        if not ret:
            return None
        return '{}{}'.format(self.prefix_url, ret['key'])
