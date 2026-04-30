---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652NANUVD%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIGXdjIjihpVpXfukn%2BN%2Ber4d2%2BHF%2BoBiHmhoEGGvCqI6AiEA9xNHE1m10EFtpZ8w5W7HzJwu%2BImxI%2FOrZ2b0%2BnKQVLkq%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDFfrA2Uqhm%2B4nILbuyrcA3iFoOp7yu3YedSPjLiMzJZ4h9MIj1InVd8Bte9p9s8o1x9igby8NFUertdn3Uozjpkor43XUehpIQpXxLdSK7A7tAn7bZrxmmZDP%2BgDtzDGjiV8J2d3SpaT%2BQfqJ4QNnTEcC3WYlypddC3iQNQnzmkQXx4GnD%2Fe3Ze7zKWvIPiduHEkz1Cwl%2F0St3eqZZ6lsCa%2FenFy8iYwNTS1R4fqMvoKaTcLrPQSYpB6xEt9YKe4YCVKjkmqt6SPXaFo6z%2BJzyHadBulxv1bOKfRhehl64SdTwnoIidghBQ5MH%2BW9MGFxd5vkR80iNTCiBiK16kdIc8dLl3rdwgEsA510pIbrCfzGz1ZZM3mK09hBt2i%2FvNo8qKEmfIEsVvDMq7xrrd0dlQiDoC77Z7evLttdEz1HRoxoEdxl%2BZmdO89Vnk8WoZjLmvS6uv2NuWwlMTMt3LF9Bi2j9UNW5neScZEZ7M3IEXvTHxqDHG5FQqIu%2ByLSIBElfkhGKGytExadXdXUzgTF6dzeULUdW2FiytopXJK6HSG6wgmToGzTVykZfHvp1TzVV3gl9u8ULVh%2B%2Fsk959Dd5TdOJ3eDnhZdn8hgUrLp8KLV6WODDhe0lHaKWjIBgVXKqLr4LmrXRXSsO8jMP6zy88GOqUBTPJkgejc5cF92dBx7LpuSCOhsNQZgJLl59DRxylcho4DSXNw%2BaKigJeIFBwkx62G59JsdiIL4QOAxo9TQt9diBGl1L7Q4P2K2bJuTllgSIbiSpOZxIm2Ls7ZuSfk77aQmUobohBUJBJBmZwXRG%2Fka%2BHFu%2FHo9DSoDAd%2BHn%2BA5nD9bNewSh30WfRV1LTEEVNMvYdBBwlgMX1FW21u27wrtepgj%2B4N&X-Amz-Signature=585936e7a6acead9b906e73ef17cf75d21749cc0ce8d9f1bba2b95b0cf537fde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

