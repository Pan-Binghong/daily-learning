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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C25JYQN%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIEceecdYUZyQTeGDH%2F%2BKrreSF9jiemj0ggOnLwUCWqW9AiAV4r7czA2HYIWhFaGXY6jjRiRAPCQZz3IaMpUtWVhbbiqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLBGXTZM3zDOK19EsKtwD9jf2zcK%2BW6ROU%2BauWycnaQ8Oep7my0k%2FzOGDvnhnMpMPQJ8FzkoLT9YQcwJzjfDcKox%2B0f0N3SMCngAH5Xge8qJDmQmRKoRga0lCPhWI6pOrxUsm2U6shYLDBO4deeeLu5brxOO1yRDxf4h0PlizF99%2BZKu%2BIcnVrHFkcaW4hBo37FjB1QsXC0qFDj9kWTJ9LPBu3mgrlPHoBIRd580xFnRmrjr5xKszrIjXOomoAPg3Jchh0TkF1TR5QUHspFm8G%2BAAm1%2BlG0qimJB5aV1jM9ORiwySj4m1nZVe%2BVZ1XJm5mQ388ZM8h0%2BDbV8rzlUpCfrzSv0iQ0YT%2B83RqEhtTXx2pQmy2F1eo0zdFAal4%2B498G%2FCW0ozGlwQ9z%2BG74n6REbvCTB2bLuWg7Mhhqk9niVKDs86oBF9qDbAc%2BPaIUJrtsC5pCVxDb93f0A0NS07Vz2oEMaBDNDKzk1BOeQtzNHCTAHyaxtfhjVCPUSndD9vaGQHHcb0WTar34yvpnDJCXyPDtP%2Fw8eZk%2FAjIHsNdm%2FD4CUP%2BM3K9kZzV9kvQInbNo9VdWJRXCpzZaU3j%2FJDXlj0Zx1GobZaHLouYYQyWsURHO1mEqNRNpP2WzYWlMkVuKvy%2FpyMMKLIDxgwnrX0zAY6pgED3LM6XKgUlyZ2rk3wk5Z0j8qDXgoGEHcKHR4cbMBnwbL0kg3kunlR4E9X5b2bP5j84RE6%2BNZ1nkv1NXRyVtSZTK9xZuCVb9Pn84XS9xxXwBQl1skpLeF6PF6uFcMBzwa4VlT%2Bk5AsCCNYkSOiLAh%2Bm8CySpzK4UPWqs9nbbtSrFFBpkNntIn%2FEZmCEP%2FrufE32UzS1dTWHCL5AhTRLMwfYunuZ0iQ&X-Amz-Signature=55243ed1e76f5c71d6430c6c234cfd61666d8d1d23e68e2e940faaefa704bdd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



