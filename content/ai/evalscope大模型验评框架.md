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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3XGSZIQ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEALajOdoXpG1L1dJGm5cFnD8QF8t5TXFkIKhtIrTZlAAiBtbgO3jDymp8jT7nbXZt82TjiDMRpuEibJVk1DBHwpfSr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMQky0RmnMXWYiGy47KtwDuNpWT3XiQusTTSL%2BXeF%2FkzMRD7dZFQiwluXQDEu6%2BNt0YKaPylAQJr9mHAzbvtpmFEcMIpgElSrRilY1u1Q1NpDumuANvnt7F0Pjkww02vWwGy%2FocnmUGu8PH0%2Bh%2BlSiTcrSuAFhUOlIwnMBmxzZPz375BepqA7S0lAJJ56NcBg%2BpJzJ8I0MshXUzSJBKsCdZt6y4mCqSrM9%2B7TNKDQElSyNR9ha%2FG6SSzJ%2FGhsk8alZaIRY5Qz1VN%2BDKpX78NXdgMEfxO40GGtt%2BXB7taqLQG2cVv0ijUHptA0nCVYCNwv8la3SSnao3aA8WbAJ8f2VzxO%2FV6wm811ZeZ4HmTyZSn5hDWDTRlRlyVvUqOuVEoYB2ZIgMNNfILFMynC0POPEqjx3tTgGYskPBj2oj6ikqzIff%2F%2BS375FZwF3o4Hgpv%2FK6dfwRiPYJ8oYsWMSEvW1YmWZzDreHVmkUwnsTuSASQLoqB8H94GCKy3fcmtMa5y6Ly8GU6z%2BTFn%2FBHX3t4Lyddc%2BxVrz99hy%2Bdb%2FCNcsyQkEUcRu8iGBWsedZbj9ElqVzoO1pLszzaoDHzm0c4p5W0lq8n8obkm%2FhetWFVL%2FY29LzVklkCyUT5UUg67MBECLsBBx48wwqX%2B%2FthYwpMHDzQY6pgERBlFC91mjMt%2FXS03pwRR1ZilDPds0lMVP9RlTkEhldXxkSaOQCtVzQEIJFtorYbAUJ7bhJfzVD2eOFa0sjfRXOOiMcvoFvr2l%2F5U2U3FcrzC7U088DVwfrJbtMivwdEn3GoewrqEJcernQ15FDE%2F0JHBeiMtTtdPeZsiSHqUAwcjWi0dV8ezNlp38GDDyEPulVXS1NooZZJ2jdYWatGTCy9KNeNXs&X-Amz-Signature=9cd24a69e0d0406fb1361e790a4bdc869bad3d5ecb147872e56bd233388e0078&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



