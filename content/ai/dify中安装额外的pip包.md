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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCRS2XDI%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEu%2F%2FRFM7RSELHO%2BhQ2usbMD4KHBe%2FZAH779ycm9JbA0AiA%2BpV3e6Fj3Busiv5uHIBs5LN87p%2BfacosMsl7bJcyF5yqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZFsbfKLvxCfrz%2F9RKtwDwx2dan9mZpYLv67zdBTsEvaylMcnyeiecj%2Bf854tRX0mmfNFNSg607bLoGLGo9ol97pOReFciZ%2BKFi2wJ%2BYdsLvrdVefAZsNtZy6osmI95vFfMcxPH23j5VKZIUucMspdmfvmqA2R7rpNIy%2FXoA3fe4o38ukhLYEV9gPli5j6EVePl%2BUUmNqej4znyo5QjKHqLVbiTwoxh9EDuY0kLLp%2Bapi4RF0gJB1yX6PiKs52YNPKmDiUQyKqZtQ9xxX66b3VR1h9zDGB1tF3l%2BQr1U5hehS0VNCkFk5qBCgGckIzK%2Ba1p6rDL%2FV6CIXNAfryj5Waxw%2FEkOTLtmRMOjC8mT6nJkWyzX8SJ52DRQU%2FUIvc0FunWu2KCuRedO%2FGbULl39bJ9hKrsQSfXl%2F8C4hh%2F5Q2lHuflwnYvAgrVxLh4AcwckgE9YMjWeZK4uMVsvavYHoIxqXWR5EgOE4cZ0iQ8nrOQzwpMkzy8NexRTZDo10NEf7EaVeqyrd6AconLeVkAFBrSWPdJnMY%2Bc55Eh8sh5IPnrrqznnzdKWfP82xPMeFHe6nmkNf1hXDkwdrNHdxatMoWuTU0F6b8rJEdB0znoKSxcUgzwuhVxlGjlb9gkfuckkhr63rzE%2F96z1F5YwufOwzwY6pgEwbuif%2FzgUO0m74h4KqH6ty0sIn1S1A1ywMK4CTddYs%2BQRDgwq%2B8cpyBRl%2FKv%2B5vhS4vJdOUYJBW9MT%2FuaW9doZ45jaQTyiAswOkgo4meVFy5Xa4afX22wBHrl5R6oTTlNzTR7VPYYnPXoexPW0eDahN24IXZBKtehAW723YWg%2BGGT87WIdN8l9qL8iahjk%2B4heEyDO2hwY0kBtgHaE0WXVh1jpaBw&X-Amz-Signature=48223251491553651cc76739e1371d9402382f8b5eb956f27effbba895224782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

