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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LILHGVD%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKgqAbjT1U%2FCaMhazj4y4VkFS61WjZHyItjTVX36D7YAiEAnmA5SwT5H8LWk899jXBsM6b6eZmFlq1kqN6sjekLtQ8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI25Q34%2BrT2dYt07gSrcA6YtLcFXJVKbfce%2B5txMgNj3CloNkXkOGZfvBAGry6saNMTJQ%2F1LFL2Wtbkn9ZHBNM7zkwA%2BCTxTMRi6Lrkh6HT4nh%2Bo4CoMPTj%2BeT3bO8Gm%2F0pesoGriN%2Ft3g8zv8q3zx5HuLh15fBYFK1xklWzj5nc2k6oruUDobnXPSdqlrhsA6HX9rhuwjd%2BMAStQaKI3nV3u24AtQSDqR5ruAMXVrV0zgYUwdJ6CtHarnKOwtucJ4bbD2XVV5015Mo2TGPz0%2BlJtkijP9Hjg4586N73hQaqLEbmzJAPqFXBjlMfjODbbvykQBQTD%2FxjacqdfgmkJeiRq3x%2F%2FGXYC8b60Jo6kHwVPGllfBMKVA7enBZ%2FKCohFKdwkfP4PpG2Xus9HRJ9hYj2iWJwJGSnyYlbyDEDpV6uwC4NqtUNX5W5o52Zou2RXgW3bN3Dr9%2BMY3M7k3vboNLy2m0WgkEOzsUZbpM3MKx%2BQk0wG8hIYjIFciIwVPDklelr81emvPVJXaP5MYFPK3r9UIvosjcB60dikroml5BIRd1m3s3wDlzs5%2FlyGzmOtpc6IqNVbHkT07gC0vReQ21KORtqF%2FSY5LHFAzuTxnVX7pfobj0qcpT5veD%2BUv4UVedSZ4oFHGJUc5ssMPjJjcoGOqUBN3cd4g%2Fer3S1CK%2FFMyqV715tDPZQBkQFsm8Jg3PNfcIYdTmgBPiTGGkH1w8h9OVUI8kkKugZLFJ9Ux%2B2Pg%2B37fuMZk18vhYM1d%2FkwHGtalmWaavo6NqItKuqzlVOR8RF6bPVY7nZ0RjSwXy3gNkNsOO5lts0C0lJfb5x7ixdFg5%2Bvz8gTKfE%2BKaxa9vx1xdoqNHESlCozVHq1SVS%2FKDM3c8HLu2F&X-Amz-Signature=8c51a26c683cd4ceef9d29cef532d3bcc911228d379a0eff1fffc6422deed491&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

