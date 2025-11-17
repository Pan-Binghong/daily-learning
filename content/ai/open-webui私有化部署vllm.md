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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRAFQXXV%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBciRhOh3sSvdb0D8CDfmrNaSn%2BEm37yxFhX7TTckgEJAiEA75JA8J8kN1sgVHktxjfH8RrDmGDnqBCJDDfYtHyffQ8qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB48LpprC%2Fc38IlbEyrcA01D2T4i6XtkGmS3WqvMY6H582%2B8Cx9jpN6AYhdCGTImzFy%2BMVxtQ25w%2BqOMT1EhKHMXpzs1bLp8ll1mcVmvBxJjOhdfsFPQ1QgIygYoYzOQtkbxfDnFs9qpI41dIk0kfrySKeNr%2Bt55EiPOd7mbWFy%2BnUeWEWbrZk%2FumltRnu8yX2Nd5qPwz3dO83YD3rwdAHdkUeY9kiNJMywqe7FoFMrwPzJ5wg2UChlr3YxjlaC5zjRm4G8zevIhM2j3ysGvCnoE%2BQAzryRdCcZEqrKtsJBzdY5RKiHqXheGZ04Mgi%2FWfcSL0r1oiZVc7f0MvtYRrN%2B8AVP7vyzDt5ZwhwNohRSDsHI225DV94quTGV2DbzFImxcRwchYKkSpnA6H8QGqrAyW1KxIom8bjrhntG%2BKi1EeqiZh5h1csd1v3BK%2BQwmpPFEfxPJcwFpf3AhvcXL6hQlDTL%2BD3F1mDcbMfEuJBW0qiKhqlJJ1UR1QDJOtO5uYVmbU4tCqRHCe6H7zLhA3kbGF8gpXOsd7d4wFBEh%2FqPBhX9mMdTw%2BFvH0pexih391Y274FbTCX9Aj5XR7Z5bq6ZCiTswXKqo6iMNEaaJnUUZKz2k797la%2FrC7orovGQilCemBwclMImubPS3MJOH6sgGOqUBPNWLgYD%2Bk5JhO751V0F5fd4KMWvBMQd7Fl%2BW54x0Qr7iBRGfOA%2B5YrZKRNCa2SsEGH6xPKKU7wTUh7iJ1H6YoLkKuwHn9pLaOFyQpbHzO9eulnQnDk7kZdLwxV0JqR6Tm%2FivP9%2BOJj84fn5MsZTgrQiQlWJZcNuV5KNgjSwuVmMlJXHCwRDWg3sFbTubmtmK83YE2Ddmbs94haHZFw4i36MzQOmm&X-Amz-Signature=739d0adb0608bdfc810a4653b982f4b52a5ad37d30083405af9cca2b1f4b2582&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



