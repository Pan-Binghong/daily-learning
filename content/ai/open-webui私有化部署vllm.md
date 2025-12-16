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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS7VZQLS%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUQYJ2tX%2BW1z6Pw52lts9QTsypK%2BOM1Y6PUI8Pk6kZxwIgcbv325r2EkDyNRgYWlvd2RoFWd3M5HBjrGT5hyTiBJ4q%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDG8hNRT26Dn3tVV0circA%2FlP861seNhlJj1Wa1pgWhagWSkBzdzYtKOBfdiqm8%2BW3xm%2BMtnM%2FVrDg2i4yAIy6BTaPbvdZp1vinsD2%2Fq1on8qMsW8go8fe9cGoOWcnTXL%2BiuTrd3yjpS9yzLP2ozkijeXTE3xCG7nLEqBxypM4Ot8h7MKZHf3D6JW7FpyTts8Qzx0uRbv9%2BZcPN6xSLf9d7yDvwsXzErVWWtZ0TNe2uCpU2vtlivY9Rvxjw0OyG5thEK52wtOTfGHTnQXoasl7C0ilZTwXcfPApdSgOIk4GojAz%2B5WL8TuIHmE9krGlJvtGoXjUD83%2F5VVrampTr5kf8VJYI5%2BigGmA%2B8ux6P%2B97c0zprqutkLmqEsIpTQiFBLoPkDdZTwEDo9RWSlV%2FkTVxqw4j4sqvddxNtJlnxWeHDuiinfATEU%2BRL1IdAfbsujtAG0BTT8n1Qo6%2FGjI7TLUa3GTQj15t2hGCXPzVOsdQeh9NTOGPrvr9ZrAiINF9p484jcehFRwXJhZkemVthexO%2BLcvrfaMp%2FD9%2BvXmT0rt3ltAfwLNPgfmXgytAlFq4fBtWZ1PPY54kTlfwS3EVyp0sMfLuVh%2BSLxgCcV%2BTCrMm2PnAcbNVH24J3bAV5MRBVzi%2FHqGpqJVe4oQaMIuMg8oGOqUBy%2B4gjHRPRc20Domt%2FnoB7Gj6xwyvuRIYNSdf0tW8Y9cYTCJyP4u9BNGWxdS6mQWtqTcoVfopsxfBRsYl%2FvyA3l2w1XhxaSGP%2FgeqslMjnyv7H2EPUShiLUZmJ3RFevVeVJlkhtZyBIVpWWkRTIK5fYQNo4sEOqR0vjNvL7FQxdGObhd2qrAQFAc1xYRLzpzxiyuEOwQHJlF9Sj07Sk1WcU%2BiN9t6&X-Amz-Signature=f0ae88d3a870f36905febfdb942d3206479a12773de04e6eb4506f926f15c20e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



