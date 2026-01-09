---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O6E6OET%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmnfRNhWeID2RWZabETrpqswUEOLSoAo0kXvHhORQkrwIgGARpq7xmKsj1a0hLAa0eTzp1N%2BkA%2B5WK8175Zn1at5kqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM905mpUCOYKa%2BJszyrcA5cRb2qxzYwwhe5wfk93llSrk7jwHdfasFf%2Bq4%2BxnN%2F9AIV%2F4t4VIjoNGKvCYkQ3JaPMDiUdmSN2QqmhA2HTbSepIO22AQJeof%2BKmwRZQWFJs52Q2lMfV7yeNAZaEc4UZpoEZKE5mVzGkb7L0I3HdLejZ3OzAk99hreOTp56EaHiXZde1bjA8Jeiy0eaeH7K%2B6E%2BVWPokUVXVOH5xMatJ0nkENCnhV2snmy6soLx3LDOFLn4s66N53fwD3nV0p4MdFEbTmMDp6ZPI2m4cEhhppF4fK4LO1BrRS354a%2Bne5Xe0LTEzyIGusvfh1Nqo%2FUjKTf07MaX%2B3k9VQ2YJwAcepsYx2haX2dUjGnL6z5YXfd%2FocbNTGT1zKL9XoFT8b2jrDmAr0I4vysqyM7fLKLuFedDHYhUVvBPWgyVENswJPg7otwJQ%2BcDaEfvfUJvHVi1yjUIDGuV0ptwykM7IJGNp4wkHdGsjeDiUWBmCNXTU6CpYdCZWY7kNqtGGcyU0WU6Y5Zcew1mGoYS5InlluyBwJ%2F5YmMK3ZVMxrUuxoyhW1DlRy9Y8T2ERb7VfJl1O2EA5NFKEG6ZP96FaOTriDuYHsMHBY0nF1cANRy1qOwY7X6AgCSwHPOeAEG3xWvAMOfDgcsGOqUB8DoJ6XHfewbawhtv2QntTfMouzocp%2BHUBHg5vgSPcYinmd%2FPl%2BlBOnwap82YHRd65SZTkI6FLYl9EoO9wzzO6KQRBx%2FAmI%2BsnnugfKrWnbLizq7EkdG0WBVupbugo2M2SvyOrDlhvmR%2Bxxd8q3Vp%2Bt7yqYHDCE493RI930ls9Q6jdn7jqryzxpziN%2FWvBQDhVudDEUPx1QNaov0LawmZEONY8ziG&X-Amz-Signature=052d3a6f23a13973c2b2b1c0523c50dbaf009a3efd344d24675be8e4673c33e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



