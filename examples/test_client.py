# -*- coding: utf-8 -*-

from dbpost.client import Client

#client = Client('l%t-$72o67!hs1-^!1&ayj5uf2b39s57', '127.0.0.1', 35000)
client = Client()

client.post(
    dict(
        uri='mongodb://admin:admin@127.0.0.1/test',
        tb='user_{year}{month}{day}{hour}{minute}{second}',
        m=dict(
            name='dantezhu',
            password='dantezhu',
        )
    )
)

client.post(
    dict(
        uri='mongodb://admin:admin@127.0.0.1/test_{year}',
        tb='user_{hour}',
        m=dict(
            name='dantezhu',
            password='dantezhu',
        )
    )
)

client.post(
    dict(
        uri='mysql://root@127.0.0.1/test',
        tb='user',
        m=dict(
            name='dantezhu',
            password='dantezhu',
        )
    )
)
