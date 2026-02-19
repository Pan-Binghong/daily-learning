---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O4SJ54J%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoQQLWRMcUsi4QMSn98yx%2BH%2FLjMrqHo9vI9dQdhUgxtgIhAJKOwwn5NEpCyhylRe7YDadwki5T1fLQt2y9D38%2FkQn1Kv8DCHQQABoMNjM3NDIzMTgzODA1IgyvXvaOQe1gsaT0NDcq3AMg1zn2vTJKDrhqWdXcKeHknNdq1p%2FXUqAikdI7%2FhUXaTyeVWNcEmD90FVfsK29D15rapwd1JNEJQexDmxh4apUS0GbTwvI%2FlppgbYiqGBcu024OihZeXrgSjR8f%2FvppW7OHssTPEbRFe24hMCQe6rXcgbEOh4xHwvUw7rCGTYreQBDkCf4rHHSoS5VsPmJ8vynMLlOYHrikxIFw%2F7rRJQH2EzF%2FV0Vi%2BlH4QCDg6R6mRNjfxqZjftgXnDJBDFF%2Bt9skERVLiRIUzf0F7UuCJD1APuZi%2BZVa7euMKr8MSIfzf5%2Bv91%2B9HevSgqR80%2FY6BPJuIegOm4lFDtTwY7wMdSXXi0KwA8Rtuw06i4qEJ%2BUr%2BbJ1gEYmzUwWRdfbfyWrbRZCq7e2iYEGJr6KeASHeyUZbHSG8kI7WC7wiG16a4a5vhbgTTB6D1UdiR4gZJpBNnXAjlSkCTHb7VxWBH%2FyrfXfdnP5Db5n3m83vAwyAH7hlmgeXvxXS%2BX%2F0JQDt9RGoVCoQouBgkVEYI43oNV1HLoZM%2FqMiBdfSTLAQiSl%2BkiQNNL5ENsgnvTnol9684LxeVCoWa4fGtDp2%2FUWV%2BkFkFe2kHB4X6llr75awFroSqUGEq87LvFE2DNfUOXZzDp8tnMBjqkAa05VD2j1sKS%2BoERdPV6U1dvDngeqQimZXH7Og7gXrZMABeJzCiKzm%2FNiT1VTLKhZ0KZDhlfVP8cnwZw%2BdoVbaat15Sk29l6AdCkEdTgBDnjlTvCvDoOzApQLgkDJpqwSurClLE7SzckWg5yMCZN3RLrANBD9AgYmh7yADQMSd6EkrUQ0JKQW3rZGzQf8ZmRJuS3r5QPmVgOcFP4SacDRka3%2FlGT&X-Amz-Signature=6e6a02312607eaad04b85a81507d66eec2e78d5f90459d009a1ae77297a0e527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



