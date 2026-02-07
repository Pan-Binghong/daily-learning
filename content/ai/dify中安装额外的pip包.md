---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662N7L4AS7%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZX5qJrEKR3WR17R4Xp%2BSAwncB89cNsCb6cJtuvQpvaQIhAJepPyTy5usrs3i588wHxRpZkp94yKm2MqzovsJyzUHIKv8DCFMQABoMNjM3NDIzMTgzODA1IgwYQCRJHCo7QYTW0Hgq3APj%2B5zHHYo5C9%2BsrvOUecUrVyr1MR3Bxg%2BGLfxvUyHOyUOJ9gswClzIHzASAwY24QCqPPdfvSuGqwUCZDWcZYFQ0hirjyHQdb%2BmznLlyVXFv6QLWLqYyi57vzBCO%2FycPLw%2FhBe3qeA6Ct9ylanURMRrRk31frW7rVmSzSUYGhL23PkQyzWEFhjwxHflz7bBQkZ1TgfnroyITOE9%2Bb3mFLVtmAvSXf%2FSQ0wOqw9p8uvZKuONfPXQmlaoBnT7aqIHdqRPhTLOR85tp6eYgmasAkd2wM2sZcs9IlBpUcYAcpMXafzI4M9wOpw0hvuoOmdi4MYHAiAJOhE9%2F%2FqKCvcjm07oiaV41iUvOtH0Ke5KkieiauIQU9WYSOF5rXbRIMuJn4qvKgzB3wyW7SvTOfI%2FecgRGTwV0pNhtAdc4U3JR0Ced%2BNSR98GWOXlwB98QP5v2Oih8jdOPQZUwaqwiDhxysB2sjo8cuiGsFUIIbdS4NDu1kEyN0jDJErGxp%2BqDhG7diR2cO2pT6HeTt3coljbdhaA%2BVyWlem1qVZwFk%2Bd45uqyhWmipq4SGENQ4bDH1T2Riu%2BBOwvodm%2BCFYRtjnGqX6Vg6wSl0HQauqKlFERq80iPWt67Tc47oyM1M7F9jCBxJrMBjqkASnlCp1rvJIBG2bj2lo7RcKOusnQMbPcWr623nR0MoJWxPDKdAwUDNCGLV3R30UpsgOaNI9Xdoh%2FBpA03V1P2dg1B9gcvg9nwUr%2BBneiUgbnlg%2BVsWAV298Yyky0nb8hISc0ARLECvG5qyslCFAq0fhYM9fMjtzSlj5nBbt3zoctmX4R9eELFHpazOS1WY7fVGIX9VMo5N0oXUGriTCnwD%2Bj0HQn&X-Amz-Signature=02d4f5535bd71b1caeae765c9f56d04fef29cce269f3aaeb2d98d3fa6c948fea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

