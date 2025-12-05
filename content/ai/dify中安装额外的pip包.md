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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIWNH6WK%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzHpMPg8ytRbH3wHsv416EACav2jFNgkSkQq1kF73AMgIgURyPrV7vKTfBUkRj1bLK5yMIAZN%2BpiLiJV5k%2BoP%2BV5Uq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDNrGO4DG3IoQLF8OdSrcAyz%2Fv1gALkoNAMJ%2FPsdRFWaIlZoIj083c5C9SBIvt2SZXV0oSVYulpOH39nUhyk850rm93zj5%2BkTWexM3qqSGfFQ1tc9BaoAhWjXu6zXETdkdBOpWXrFU4X29Fv%2BiX%2FUQzmG3xX6pkc305jbhX6yY%2BvHss0%2BDFiYcmppbgcdI4nKtxSCBZErHWMusXYjn6k18w5H81Hu4crbtWgfhN0thXMRQ8Tue0nBNtl9wvLeFwnfgzIHeg43UBOxs%2BtZaPWzed82wjv%2FuwKZZ2bcJWNXx4ZGPuFYvgOD8aIHDFO%2B%2BDi1uUT3OvSzOzFBGTr2J0sjk%2BIj7yItWbFYaOWiMoZ2IflD2fp58zZ0bAoiB1LVkATkqd%2B3Tsximl6lbV74vG2W0FmCSIc7vMjQrY1BAplupDP%2F6Ta3ilvDe5V5JGz7rVxuURSoNIkC3qGtpbN5RnmExq%2FpmWnL8OO4NHy%2BzFtvmrkY7t2rb6Y1v9UFkS%2BJOiY%2BB37n6Od6Ei1GOxaXNFW9vNB6S2R7W3nLYASUId2mjTzLpisv8VUPWGLwXSktt1SCSScloVOhPA3CuGgVBUzibVSZHU5KqPn2ZDSD9oHMMWcmjroqFykrpjGRtiTaUVfCexu%2FeeE2w4F%2BaycvMIKMyMkGOqUBuPzq%2FeazxjxSvejQKJ6Hnb4YCR1OQF4Yb6M4TDlclFhjTUonQYybW0gEb6F%2BM%2FFweTSoGRRwx2Fx%2BtFDOPxgZVXzbKPMZABVCiEROyHr5l8ivNcsiOLRRGDBpkH0QIKXZeSDQoxBzy%2B%2FkBX31SZAGmKKvKDkIPEJKgT2MB38X7R%2FI%2Bi3TQY9TxQLd7WghnYLr1Wa44BcOixx%2BJtyvxcFn%2FXazdS%2F&X-Amz-Signature=7d2c2d404b5973e34cd9b48499d63d531fddc39ed72d472216d149a6a34d5ee0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

