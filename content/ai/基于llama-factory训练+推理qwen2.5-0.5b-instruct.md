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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCLHMW4Q%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIECtG2Kkm4l2OTOqQ2pJHc5SHwDbWLHjUWCNhvOZZf83AiBWUV%2Fu0LS2WFxK%2B69JSwFOwP0qOSWa68HuK98eI%2BFE%2BSqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMgP2KO0%2Fgsove7RYKtwDAgBqFr40TjuOaaGbBwakc4p6sQvKLXZY8nzNXOkULwRhTSvWl%2FCHlErlck%2F4JvDJfTp%2FOj8YD62etyQd5jYpFAp2pJSu5hBMsrIwX%2BvguwJ9brnRj%2FQtuHuoA4Bf%2BH4nkvMmTREszHkEkVMJQsypvAPqbkTqJS48OWkog90icrqyD%2Fwsvt5DmDKZz4aqn7f5Dq695oNoMjPYvOHQx4zSa28guNNqHD5F3057bWio%2BOSKL4%2BTuel%2FiCWAvIv9JmsngMPAQqFORXlAbzXKh0tASxScBjROfRp%2FF7cVpazpE%2BX5gA95PogH76KF14QYPH5r4w0v2PbtunkRhSIYZbEZ6p6zuOYs05QMpNZlIrfecNED9lcDIxgLNIKoE2AcRlWW0EBCAEvCCpsnuc1JdttzSoS3AGg%2Foc5K0jCrI%2BKIRkLFWdeSgSVj89cY8OWfTCg%2FtMxcGqbe7PDBYwRuuqOv1SaccZJ2lIXkc42IOE5iWNVkzpdMQ6OrHWbZMGXnxaEEDGUVGSEP%2Bp3Hs75Bk7uSExrO7jXrKbIMWd0z4kJis7%2B%2B%2ByeKB8XUusqDQJ2v9E4pimk8TH9cb7gIpJd77zt3s%2BpQyKj0p4POCxkcM4VFO2YQDe5vA4kINDSrxSow56SNzgY6pgH4zOoVz11jGaUhqwVZAqoe3DKvuFHAR53XkSUuLLgfEpNegjU0vHoPUxGBlfkgeRe6FQKtWJArOcjL1oH6jjMW8dJPgH6yk1AquYYwwXNdteJsDwglrHL3D1%2BCMpr6Z4rEFu8C%2BAEivkpsxcZr9lNUGnBW%2BQ1HGUMLVIdtYssiqik%2BFvfq3dKP0gGUCGffM9%2FNOkQ6snpraUianbp7nrHa%2F2n7LKDJ&X-Amz-Signature=58b3375f74b253679b9c4b393b50b3e438ff0485399431415daa1fd7959d95b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



