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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZWUO7P3%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIFSHEz%2FOeTrbj7MxWUcpHGG0ibkwLV5CT0rCignor7GuAiEAjZD3iDUJQjeyICax4PnTVYaQFIxpWlbVJZcrkaPlwWkqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7tGx9cWX6lrPuyLCrcA0MbhCBmrRxr%2FExPHU6TPGIUlz8fAzK2IJm1QaPSiggTsn2eApRFfr4TCJkdLchwb73v0IJ3QBN9V9UHhaq2oql8dPPTK9M3BEbL3flIVqD0kv0jfgbwqlOWs1KC8olWkzeQzsIJsRidYuCEeA5Rey9Y0B0nb%2BBZGkDumOGIyC4FHyDRvQLD6FVPpX%2FshdKkLnTUKpCoeTuZTCq9Hv1eb01VReILmCc2pFSgFbFXYRb4dvAkjk%2F09OcPyO%2BLLLgLmJ78LDZSvCUyuunp%2FKXZH7d2mnw4M57oTYZYKrl%2B4Dl%2BvR1obrBTbIhcnmjc5HyOJRcbEcOeSUprLVB7eAIPBxRvRhL6DNzUPZK%2F%2F4cVBsT99ri5IKMl%2F2Xex2tGr5G%2FVK1NXC1NDaAF%2BeKHiBm9hKnnyvHcyhdazRrewQkw6%2BUAp180vkf6RtKUU8ZAuj181EoWaVRfVq6F4A3MUh8arDT6PkTo96Uswx6urDq1FZ1Q6NgsKOO4OOrufJOstq%2BdHwh9%2BJ7sCUwHqSw3d3tXBjD0IRAIuW5mZiDmOGf3X7OpvEVsLLL9gO22YM09tKdYOEJgoXIxMxdEUBJmCCM%2BeErxl5oZMx3GKpzy2j7otpffWAhEpLT4Yv4olOsnML626MkGOqUB%2FWXsA1RJDWuj7ZWEbAtiflUHWtDH%2BtFuANQrsNqPSZ2sxk4QNJmnAI%2BpjBna%2F2RAyIEecWTFe8dJhRDl1x6h7blaiXIoqvkrfCi8B02dZFKKYpi3wF8uuLDSgc66dKJKfCyhvaTrPrq5K56FPVSxJBRwB%2Fs%2FRZxaaHjV2rjRWnWV%2B0JNHD7L9quXqNWlczjbjWqD53HmsF2LT5SlCO3ehD%2BkoQbE&X-Amz-Signature=504b7ef9126fc8323673a5d6331d85d421acecc7e4246074d1c93fea9198bd2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

