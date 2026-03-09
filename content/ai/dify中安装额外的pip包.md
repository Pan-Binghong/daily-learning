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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFQG7MKM%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQClJF61BtaJRxekIARMY%2FctZiJCrSFuCSCG4uh7GRGdvAIgL84DUlGmgH3lDFI0Kr%2Fuf8OYQONA8wCw8lzmAlzk4R8q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJPF%2BtVpAJSnAXkQdCrcAyRG1dWp6uIH%2FB1vwwrSa3HpHPgep4lordtCUpPzuvtnnasB7TL7dmA7QhGHc%2BXTfb4BL0SA0F3aVaoYq4sz4oy8owomAtWYj7Z7CKlGXiF0MaLMgYfr6b32tJQ5p5DWcPweAxQiQ5%2FGU5TWcYqmzs76sfTQE068kLSHBmIlIWBNfah4TWkN46qLzV9G58yf4KLH1uuTELoiajwwT5psBpfo82rXI435gEMLQKCWttsQg3CAN9BbTR2jVBvPZqN0yJmYUiy%2B2mJp3ye%2B%2Fg%2FlcvId2MDT0d%2BYKrxzQKDIozxDbusI5GFcQSjZbS7qAVMdrmJLcc75Sp4YfStCf%2F7Vj3mxJSKWQ3v0GG9UtfHqqwxuK5%2FXjOmsJy00ewiAo2wa%2FIGKtJ2Cia0O2%2Br4lahlHZDDBff4RwP2Uqv9S2wZn3cBN415IfUlzrjAiXXuhO4%2FNDc7vybrZuOajlByOxUep%2Bt9a6oHXu6nuwOW%2BixEG%2FzCEsuHr9D7Xk%2B5%2BDIV7UJGuVZQuRahSEnCyXkPlfpTFXrbQqqFCdCmBzhMkgq9%2FpG1vhDFQSggN7uigZ5zKV5jDMgU7I2BeLoRXKgdp9Dl5cemvE58KcJQ43c7v5exT6ixDQ%2B0Jv3JdNCHvAYdMJ%2F9uM0GOqUBCEOYirwSP0A1C48cXtIHkXLa%2Fvs17K1KtAOy35bCcbNBD32tGEK4Rv3y0lvBvDiNIbl49jI3M0XDcLKQDxucqoANKRA7d%2FF66GDa%2FMi4WjFx3EQ%2F4yfWXfMN9v%2Bxpobl6e1ZBHysEjKrBg4Ay9qmHRoM7mugsVcOaR5uD3CgYGtb%2FbYdtk4TPK49TXJnRfXa5nyeuqSIIRYv5%2FJcobAyeH9EVibm&X-Amz-Signature=eef453e9e8d0382a8ef4855feb84e1ce785406540b60e84fe7cd267fc06a2579&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

