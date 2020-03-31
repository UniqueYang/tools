#!/usr/bin/env python
# -*- coding=utf-8

# XML Python SDK 的初始化方式
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import uuid

filenames = str(uuid.uuid4())

'''
:secretId
:secretKey
:Region
:Bucket

:Details https://support.typora.io/Upload-Image/#custom
typora image upload setting
python typora_qcloud.py
'''

secret_id = 'xxxxxxxxxxxxxxxxxx'      # 替换为用户的 secretId
secret_key = 'xxxxxxxxxxxxxxxxxxxxx'      # 替换为用户的 secretKey
region = 'ap-guangzhou'      # 替换为用户的 Region
token = None
scheme = 'https'
baseUrl = 'https://xxxxxxxxxxxxx.cos.ap-guangzhou.myqcloud.com/'  # Bucket
config = CosConfig(Region=region, SecretId=secret_id,
                   SecretKey=secret_key, Token=token, Scheme=scheme)

client = CosS3Client(config)

number = len(sys.argv)

while number > 1:
    response = client.upload_file(
        Bucket="xxxxxxxxxxxxxx",
        LocalFilePath=sys.argv[number - 1],
        # 放在img文件夹下
        Key="img/" + filenames
    )

    print(baseUrl + "img/" + filenames)

    number -= 1
