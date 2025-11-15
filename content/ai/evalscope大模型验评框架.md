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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ICBNOCK%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG9U0D%2B%2B2d62FKNwKN1eQZnBI0Xf0YhgPINR4boXTbtgIhAMQQTnZKA3vRysg5sUVwSB4sg02IrPSzdPOipmcztcdnKv8DCHMQABoMNjM3NDIzMTgzODA1IgzQrKTmU27Kj%2FM6taQq3AMsodE8WsmwrQGqGkTPePlGIskR2G8K1792gaGefUB5cnJ2yAq0%2FNsCU3GhFQRPXjW5T5co%2BWZgWwGapNA3ufDji1kkS3zWNTw5JQoVAuPZsOGlRgAaSLKZCYpmpFfavHkr0ql8edUBmRlZai6aM6%2BtuBGEX0NlEaboB42nNiLQnwQYHXdOAbWaArD1jZrfw4kdFjKHrc5Z7xzUkiP%2F3tJQRD%2FUq5IuU2JV4Bk%2Bow9ZpgpV7FZwHSLI4PRgdh00Rtu5AIQ19vk9o3utKEFgNmyjnpiqt7cag%2BL0Qpf4fFlxnu5Fgep1zyKCuXAr4DMk5kz8tzvHDAIFxHIau4iqW3b8VlRHVpnTZ3AGKlO9yd5fJLKYeVeInJv6Gak0SwCQBZlCeHRCX%2FvkNioTlVaPNarUSaJavQlOPH1a%2FZoS%2FIejdwWeyLCtKTicwpZNplRJcDnRbdALBIc3QYnqkmA7XDejCK4taQ9aYlbGj%2F97c%2BEK72qR15mTaGsaaWYCGeFHf9BiL3Yl0%2FsLXDlb%2BLUd8YmisNYcR3Vd97sTRlS2WqyKE5HqOeS7SRymh01%2FXufRg%2BT7wBlhc1Nrgvra636oDB%2Ft0Mi7SiEHqg7LdrlOon7VQXZ%2FO%2BemNRKURpg3yTCzwN%2FIBjqkAfgQk2se5QfrkVbmLh0XUEHUQEFLLMygokXgpOsw29KBgfbOf%2BwZAOjqjl48%2BOPQ961%2B8byCU72raHFrisHcgzZpNQg5OHzAujkxFex1bw9KjzaMCIFUT5vPFbE407UxTWPQNFWxTubO5OZsalrEinvk9QOsbhEXJsnX5yNqb2FDIp724gTifsC5%2FtR2fjN2ENL8Ta066SakuWaYYsbwef%2FWjVkt&X-Amz-Signature=f0a914ce5b4b6021908cf53332a00e57cdf2608cdff8baa18ca2e4c1142e4155&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



