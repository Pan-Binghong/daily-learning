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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NGKNQIZ%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCRvA3XBnUp%2Fr7f1J4vaOmYgkdFBIvAtqquUMlVWj5M4QIgS6xWr4YYTxMOWUj18OaUfJZZmlc913qyf6hp3V1HC0YqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN52%2FHYHo2mvv98GgSrcAyKKO4i5Y4PnOjCBtTkhYfBqTfRQIJ8RYadZIqZdwxDtBSJCNiI9CS%2Fdw9tO9h7G%2FxbhNVPUBHL2oKAuliSfQZDOLoHfic2mY%2BIFZrl0ROCTYwvfmtolKFqTOR%2Bu%2FhhuXCKlYk%2BO9NhEBJBAC%2B60yLL2y%2BONMIqQWWgDM8PQW%2BhXt0xZWp5cBcAHefT1AiOHd%2FQbEIJeM40Jxd3JggvoXx1SEEp8st3n715EBVlKWbYvA3xW629H1C4JZ9dixR0N7nvoPCKaQuutsUtnaNjfFiwNaipdwRuQvC%2BQtVWohHfiJ82kP6Y37CiPCa8xSj5e%2FpfmtOauWVKskMCKOeVrgQcura54c8%2Fu%2B7VMtzFYpxSFLfgaL9ziPyjbvAyJ2YM75Q%2F4aiCLQvNSEvPXQ1Ddf7%2Fy7JdWNLAALx7XdOMcIz1wdKUCBfog22ikcOzd0HVzEGktGGQmV6f%2B1wWA3%2Be5%2FAznsFENeFbOuvar1WQzaQa6N%2F86psv%2B7PEqsLAjLDhN4EgHEgMAe3XNK88eEqs3lxCn%2BeANy0iWyJ%2BsiEGxxznxj3mTjWL0XRHbInBYPWhdB0OaOj7UVfWGl0AwztTJaNRO5mlnay8HRH%2BtP30Hc1IZR3H5MbM43uDeBiY0MN6HgMwGOqUBRxjW0v5v1jPIEShFI6FTTfQ6hh6gOmlxS9TiNTv1MnARGyIqVLk88%2F%2Footgv7zZwQ2KIONugdP98eTJCstYkp8s3ZChGmHi3lWZs2XGl3Uum90kb43FMXGC20uQa2HGWgTWfkaqu0nqD0t3ds7IXCIJgvVUGBp1%2F7MeK3vUjzZVTROw6IhkZoVaP0pcw76shnbYR59x6RUKe3sa36SpcpqXziOKJ&X-Amz-Signature=e3ec9a61695d53e9386d58f7e3f5d1c25b0a912f2c473d81981f8f2a476bc2e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

