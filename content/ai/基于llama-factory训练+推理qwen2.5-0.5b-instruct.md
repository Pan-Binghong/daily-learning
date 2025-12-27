---
title: 基于LLaMA Factory训练+推理Qwen2.5-0.5B-Instruct
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- LLamaFactory
categories:
- AI
---

## LLaMA-Factory框架总述

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZA2A26HA%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB65kBbtccKgj%2BLsLIyG7HDk3nOoXjrCVMh5jWRbkFdAIgXzr00nUNnN2hPWa3Sk1In55GhkX6B5Aq9SOzURlAqgYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJ%2BlvcPYdKo3ZL6iEircA1%2FnxA94TutsFPnM4NNcOQUo12HmUNgFhq9%2BF7cH327xEi%2FZPpdxe6VosVc3vTLbNI0TA6FU598ECKS44aA6byikVX3zj%2Bwbt5wZgGcChlds5L4hKym1uAyOKvhDpRNugUx8DP2%2BvKIQS3KsP2Otfx45f6VkcVVjUnSliME5mglrFSRyStmoxEjK2VuHWCvX8INQvZ9%2FPDXzrvHtgzBAnizP4ehYUNQvDTySjBCatKFSpHP8ag9ECUbxZAijyjDH%2FNu3vCX94V4Boc0YbHAYgik9YOKzXw6b5qFvDaIucHNUyh%2BXkKVuHJHI8EV%2BoHdQQxQJPE0oiDF3bYDnihyPIMJMaagGlS9t10bBguD6WXhFZyPr3emnbvW9UxSS5tSefiX0Jt9g6ym7I%2BVoqjOCy4WtOrDHmq9w8C7prjbT957jubMt4mji9uahe%2BLK%2BniQQKC6MG8l%2BU773WLPK%2BdQ5i6wkELZbew3NpYo0KHLzoNcOcIQ%2BGaPUvSy8SGtx6UcahoLjXW2N0wP%2Ffe0NIWLSGr04hOZrnupxYPBgEEcNIpCMUuL8892C2G8Av0ZBIRfxIWA3xS92HyZp22hVZt01RWokHuIEIg8aQ5F2qdTfJWvNWqlzssK854rasqNMKfnvMoGOqUB%2BB7hW4sJaT854c9z03O8sbEaGObYLdkiJOp3JRTDLtEpdfw8blpcyZcDVhH%2FD8mPQKa9mEzxzLN%2Fc59HYJ%2FOu9n0HL9X1HmdJ6emB1v6A2aghkMzpZzOj%2Fswq3vqUVCqoKPeOt%2BCmcYrHbNtxPIYk4VNA1bQFX%2FLrHKgl6zk2B8UOhBH2TO%2B2a%2FRS2yxmxQrfQiOFq35ZKzSWj9AFCRcpxWkasAu&X-Amz-Signature=20b956973f5bf6b580d72e2f8c6536521ce5b10356dd0db64a5e49acad61674f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前置条件: 环境，模型

- 模型路径 : /root/autodl-tmp/xinference/modelscope/hub/qwen/Qwen2___5-0___5B-Instruct
- 微调完成 : /root/saves/Qwen2-0.5B-Chat/lora/train_2024-10-10-19-48-53/checkpoint-62
- 融合完成 : /root/LLaMA-Factory/models/qwen2.5
## 数据

## 训练

## 推理

## Reference

> https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

> https://llamafactory.readthedocs.io/zh-cn/latest/index.html

> https://inference.readthedocs.io/zh-cn/latest/



