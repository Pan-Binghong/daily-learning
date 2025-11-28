---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAKEGMOL%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqP4H%2Bf94PEjbsw%2BnuPJQEWPz0yBNZlpPwSVUBUW3kEAiBcimJvQV19m5VeK%2BDtzeRYk%2F%2Bu9%2BDQT4uIlPJ%2B6PNUTCqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvpOQkUXgRhnqOqUOKtwDVWLwlfhCdVYexlrYZCm3wF5wNOxqTv1nnnHha8fh5OCUz06trx7FMX9SZXYmWkK7K%2BprQ%2FYrG%2FsyzzcQ%2F3ZPR7g7YY183suYbAX%2FjOYBohTQ%2FRZV5A6CIKaPYkRHR0u4c9quk06I9Sd5r49MAujIExV5yUTCA3HhMDzy93Qi5SMYyu3R8OStqeBbG0AvGz%2Bw%2FuVB%2FHYoc8mepvfTlyWcmUKpmSR4SfKVWiEgKeXu7b91aOiRP1KhlQNZtwkWJxuUOEVcxzBBTypIjPFTN4CsvIoXgO7wb7pelE3ZLbOeRVl7E9i9Y%2F2%2FDy9rhulZ5RhH4WzCOLardj1RPpRMNInOG5t8aCF3ucipb5EJss5V6hLa5h2AHeIFN7URtAThLXoA%2FNvwXGmkD7H2BotNQWO1hozqM9C%2BhFmj4sR6wBQBEpMhg%2B2bJtRZF3HOiFbzNbUPMd8NHj%2BWBIMIhPoAMSkOjLNfYeLzfaqKrLduP%2BEUKuv%2FHiUT7TGEeoKoXXAr6EtvezeSnb7jWfPVR6idxNW7c9J%2BlZrovy0jQGafVUwsUjFv0Q%2FH3B5xoBHcITGb4ElS%2FL%2BqlJVrnkqzEq9Sft1yuuUubnfg3px6SQMZiKH9fxLTAf7Y%2BR0xVxoyN8UwmIujyQY6pgGiDEmTLUxKzdOeqZkEZ9UVFcAfpZ8MXgPABSAs%2B4yhLHKG9TAqG2reE8WaXiuYpiEVDFRXJOT%2BZ5emhMc1TmxUEeyQPD2b%2FW7j0bfGq%2Bpqiq5sb2tBcj2%2BBtdEJFoMjGOZSVrFybTi497fX%2Ffe2i%2BxWoY8nbQOqzIiCNrCvPE%2BKqxS2sUsMD%2F1erAohaBns%2BmhWfJuURqfgG%2FnJB7wPWRxYqDRFmWm&X-Amz-Signature=2a6695612adf57ed759cdcf2059cc651713b9b09a25eeb054a5a5c8331464373&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAKEGMOL%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqP4H%2Bf94PEjbsw%2BnuPJQEWPz0yBNZlpPwSVUBUW3kEAiBcimJvQV19m5VeK%2BDtzeRYk%2F%2Bu9%2BDQT4uIlPJ%2B6PNUTCqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvpOQkUXgRhnqOqUOKtwDVWLwlfhCdVYexlrYZCm3wF5wNOxqTv1nnnHha8fh5OCUz06trx7FMX9SZXYmWkK7K%2BprQ%2FYrG%2FsyzzcQ%2F3ZPR7g7YY183suYbAX%2FjOYBohTQ%2FRZV5A6CIKaPYkRHR0u4c9quk06I9Sd5r49MAujIExV5yUTCA3HhMDzy93Qi5SMYyu3R8OStqeBbG0AvGz%2Bw%2FuVB%2FHYoc8mepvfTlyWcmUKpmSR4SfKVWiEgKeXu7b91aOiRP1KhlQNZtwkWJxuUOEVcxzBBTypIjPFTN4CsvIoXgO7wb7pelE3ZLbOeRVl7E9i9Y%2F2%2FDy9rhulZ5RhH4WzCOLardj1RPpRMNInOG5t8aCF3ucipb5EJss5V6hLa5h2AHeIFN7URtAThLXoA%2FNvwXGmkD7H2BotNQWO1hozqM9C%2BhFmj4sR6wBQBEpMhg%2B2bJtRZF3HOiFbzNbUPMd8NHj%2BWBIMIhPoAMSkOjLNfYeLzfaqKrLduP%2BEUKuv%2FHiUT7TGEeoKoXXAr6EtvezeSnb7jWfPVR6idxNW7c9J%2BlZrovy0jQGafVUwsUjFv0Q%2FH3B5xoBHcITGb4ElS%2FL%2BqlJVrnkqzEq9Sft1yuuUubnfg3px6SQMZiKH9fxLTAf7Y%2BR0xVxoyN8UwmIujyQY6pgGiDEmTLUxKzdOeqZkEZ9UVFcAfpZ8MXgPABSAs%2B4yhLHKG9TAqG2reE8WaXiuYpiEVDFRXJOT%2BZ5emhMc1TmxUEeyQPD2b%2FW7j0bfGq%2Bpqiq5sb2tBcj2%2BBtdEJFoMjGOZSVrFybTi497fX%2Ffe2i%2BxWoY8nbQOqzIiCNrCvPE%2BKqxS2sUsMD%2F1erAohaBns%2BmhWfJuURqfgG%2FnJB7wPWRxYqDRFmWm&X-Amz-Signature=f6517ba4da32cce311b2d486de8cf7122d1d6a9fe514702ba296d475f3672e10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

