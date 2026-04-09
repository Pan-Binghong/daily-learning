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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XWJ4USX%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIDoL9QIGuMB2vup5S8qmeCNY7Mk3ytQCnPI4s4q3fEGDAiEA2bX2u4TtX7kl%2FUkrvhnZAyr9u0tesnnVuUO5VvNe9zgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDKe9mcG%2Bukc3dTSZuSrcA%2FnssVL9Zmf0SwWEDSSUaEaFC2rYlx6Hq7PkK7qoUGmJ5ty7%2Bwo35xyb9CXWtWfE10%2FBmAGYOilPve6zLNNV%2F5AEE2nOtgu8RLRzrBLFMMLT7KwWGyW%2BX06x%2BlgtLj1Kxtx3cR5egeziyuy9CoxZYi9kIlxOVubcBuzey%2FAU3j%2FAyGw6CBhHRyNmuzM%2F3uSZavAG4KTGoqU%2F2KIA6xco3aKtsoLheilszcWXCDL8SUjAG43kgTL7DMQhKPyDOLQVN0sFPQg3%2B%2FqcLWeOubiJ1Z4Hak5t%2F5O0%2BtuJbZFq2Bd2fRvNQrZYLjdf1QlOYT1nVu2NJcL7%2BQ9yZh0deCiISKs1SwlOPVd%2FU%2FOdfctgi%2FiOL2183ASEdrrGk6yIum7Flej8oKL7zVMdMh%2B%2FXKVVddEHpiP3SlGfQNDG1Rb95%2BeaKPmOYfb0MyBduPzdRB8amWPUgy2KNj1Um%2F2g7Yod8zrOZ8fSTsajyDbAvG8CKGDLKcytLtgYSQDBAGkNDwU6STlyCHSjB9NnH52flJXsVnAZmDyM00iDbKvbwHugRnv%2BTI0S7p44UAx6fDL3iYPKvz%2FpTBrWQCpMUbEIp2LI7EXno3fQFw574txnwRfudSrjjvN6SdS0fT0E1VkkMJ%2Bz3M4GOqUB4JHZoq8MdjlHE2hKsYUY2lfFNEtHnlK0t4mC4gv4nfC9fQI4kfpg4G1JSSTP8G%2FtVVWSdwqjm8c94ZZUd2leHSz1zpFDDqOmY8qAdWkW1kRzemsBkDSBjPu4FeV4q%2FW2Pik9IiklatDz8ru1oCMMx2quIniD6DzZsbQPVaG1rhth%2BYF8qj%2FrD3L5lJDbBfbcbl0TApA5PAPA1gMs7TPrw79uSTUb&X-Amz-Signature=132ca34eea58935c247dcad95c0c7533488e93e86922bc38b62d0725cbd4f63f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

