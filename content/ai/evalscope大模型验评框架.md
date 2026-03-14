---
title: EvalScope大模型验评框架
date: '2025-03-28T01:13:00.000Z'
lastmod: '2025-04-21T02:58:00.000Z'
draft: false
tags:
- LLMs
- Eval
categories:
- AI
---

> 💡 之前都是使用vllm或者sglang官方提供的benchmark脚本，现在尝试更换为EvalScope框架。记录使用该框架对速度进行基准测试全流程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFCPUDZ%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNFvD6VmKcbtIVoS75gfRTzLZZhG01YCfmGsf2KhvzSAIhAOrChEZaaAioeFKSVLvBrq82xp1XC6oz0ZI5RMH%2FkJa8KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz17hMfqNDLbN9xkekq3AMxKzNWWCGzloy9CT4x7qZWBQujo43djJc6B9Wd%2FvJRO4Eac0oOr%2BQ88j8WedYIwcylSBDIkmQNjbBlaW6tH%2BnG2I8rxjLZBn2yR2lSh7V8SVl5Jtu61TsPheFl1IOYBUzlhom9%2FRLl1qYNzvgaxoiP9vIceWQDzkD8SRbqpjIEFamKoTKGoQ%2FxqxhZYoc7%2Bhn8dkq8pTJ5XLWWGjTKtR9cvzlrP411umyoSoyEE5brGYt7g%2Bx%2BUH2BKVgrg8WtOP%2BoCYo4OU3TQUUWk89jX%2FXOdKA2bCiUGqK3KdbUKFw7wnJ4dE75wcUwoAb8xtrAOIHugQSehspOVs11qHzCDvWHBLfkT9NRceMvyT0eDj9O%2Fk8vGSxY1Vc%2Fp%2FHVg3aJ8K%2BH28RSasWOhjnNwigaj3SQjbl191Z0b99XTORohDELqFP3iS0kMdC1ScCKKvO4fiA%2BKijpClLOTddVDv0dIZFr8xAKWpQkykfyfbZGhFueqUbUzfRxFbsvIL45%2BgkEfMzzNfkYCAzLSR0nPWfIxEeUPKuPKTJB9VffGBKvTnr6KbBNnF1BxV9XWmU8FyY8iPROzwK91ls6ReCDsfByl14YVSbc1iRfxJlXRSP5xFt%2BiAOX%2FKtPUbBRm%2BaYkDCLgtPNBjqkAQiMb8BwTFbKi8yqFMHlfY1m0dIA2xEU8G0K5FGFi%2FuyPs53rQOqF7XTIFciF%2FOEj6nV7nBUuoymqLsl%2F15KgH82PS2v9dQ0DmDzwAoQ3Bfi7NACwVmH54YMaJsFEa7y6M9QyAUtiGv6hDcV1PRYnTlRcZ1e8ujdODXNkH6E%2FjWIP73Yn2UXJedC9rtbfaUrC%2BYeiCrcCbI6P%2BsXbhHDWtJCFMeO&X-Amz-Signature=66d8bbbf7198ff2ca25871540d857057edd3d7b34d59dfbfad2e3569e62272ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 1. 安装

官方提供3种安装方式，1.pip/2.source code/3.docker。

## Pip安装

1. 更新pip
1. pip安装
---

## 源码安装 | 推荐

1. 下载代码
1. 编译
---

## Docker安装

https://modelscope.cn/docs/intro/environment-setup#%E6%9C%80%E6%96%B0%E9%95%9C%E5%83%8F

1. 拉取镜像
1. 创建容器
---

# 2. 运行模型推理性能压测

参数详细说明：https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/parameters.html 

推理性能测试有2种策略，第一种为标准的并发压力测试，第二种为单并发下的速度测试。在该框架下，特别说明了如果需要使用速度测试，则url需要设置为/v1/completions。https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/speed_benchmark.html

## 命令行方式启动

```bash
# eval.sh
CUDA_VISIBLE_DEVICES=0,1,2,3 \
evalscope perf \
--parallel 20 \
--model /data/DeepSeek-R1-Distill-Llama-70B \
--url http://127.0.0.1:8000/v1/chat/completions \
--port 8000 \
--api local_vllm \
--dataset random \
--max-tokens 640 \
--prefix-length 64 \
--min-prompt-length 32 \
--max-prompt-length 64 \
--number 100 \
--tokenizer-path /data/DeepSeek-R1-Distill-Llama-70B \
--stream \

# 为了截图，暂先取消设置该参数
#--debug 
```

<details><summary>测试长截图</summary>

</details>

---

# 3. 可视化

1. 安装wandb依赖包
1. 注册 + 获取密钥
1. 运行命令后追加
1. 结果展示
<details><summary>截图</summary>

</details>

---

# 4. 测评模型能力

1. 首先将模型启动，使用vllm框架进行启动：vllm serve /data/DeepSeek-R1-Distill-Qwen-7B --tensor-parallel-size 2
1. 运行以上命令后，会在当前目录下输出一个output文件夹，其中保存着日志文件。可以将日志路径保存。
1. 终端输入：
1. 访问本地的7860端口：
---

> References



