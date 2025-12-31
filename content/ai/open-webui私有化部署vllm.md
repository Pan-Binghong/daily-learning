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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ER7DTTQ%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICngh3mH162KZMsCuYkJOq2TVcx5mP2riLBr6k4kH50IAiBfOSzdEQBETSIw3j1%2BondqQZxZoJ6CGUc0Xt6NkadkeCqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMriu2n3UwgujfqTNDKtwDQAtYqYfWFYHEecFyDTSXgL23F7YW%2BwiDuKitCutB68X9aeyCVgYYB6OzpGNCEkt2JkQIMdMqm8ewDZt%2BqBLUo0LashBPw74wLrolJNDjmmJc%2FUaWwr8cGuS2eqy3DVVbfSLc11xxS7e%2BHeJ26CHkDVtYrczTrD0ymSr1pp7xd7R%2FHOb17qRUB4PSavU5AN%2FPtbcX0%2BrYyd6rkkg8T6CrwYySj1pKvpDdr7Zd70vSfboABCczOgCqu2ondMFLX9MaBv7t%2BwROmIqLGAttOBX0uo2hlqfffApvhvLJ%2FTBW0V%2FvSt9o5zcPPt5xsCpBY8K4xaYwBKUnKavOVB8wCpgNGeOe%2FW7ad2dEeLP3LAx9cTTmwgd3hOeI11m%2B61XmResRiwP7RJ65TvTTBeDIGjCpl%2BO3NDi%2F8N6TMcvPaNVVfzT2yNGhkgh%2B1P%2BCyQJxhJEvhuDsgi7Woaud2q%2BsKAuqqyPcZucHmlt8vpdiXwI6bA4MHmj%2FiSEy%2BkORPg%2BjIn7yeN3PcxkIPt1Eh2wBrVz9rRwJZ63O5Hf2UXW3B47zSFWvy4p2bowKj1fMP41yoIQ4IrZLlBhXErHDkD%2FMMrJksH9IcJCSpOaNtodzK8uxlitgYwTHCr6plU7sEiwwlvnRygY6pgHlBnRcuS66L6aXVIt0r4HVlB2IMndt8lglHWPc4yRiqd0KzVYyvcbWsL2Sb1alC8rMfZTQPGvuHfuezmhHrSOYzJdgPXzNFOoUfIPo%2FaN92chkLwmL%2BKejWcbMr3yfIIP4F5VhSbBY693kn02Jb1oODUVGSbH5%2F4awLIGx7QO9xFYDDyLt%2Bfe0pJbbIaW5jUOGLuhKw4Rul2LvBKLW77%2Br0W9bztbh&X-Amz-Signature=796aa383cfc74182172bb583c9fbf137603dbcc053b12837b400b0e90da122cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



