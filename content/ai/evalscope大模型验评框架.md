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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIV77623%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQDt%2FrTyYtRiEYUdP2zFK5fov7EMkvLNUry9qXDAsVv%2FcQIgVDqb4pCsdxlYYA8hrWQ98PjsSEOMYRpB2w%2FE1waZjpAq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDBOcX70psxJN5boT1CrcA0OfBmWm5QDMj7mzLnY%2Bg12h%2FN7lDBPbvVEeQv3k0qfDOS4DD6QP2wLTSHrH2q5VQaO14mRwUCGL3BT2l2tvRLjiMLV4EGE1tz0q1OSHTXHulZJy%2Bna0aMtovU%2BBCtlVO2NX%2BJ3jl3Y1elH00H0uNuLGG7Bpx4KJAM8hkaRZ6V3hlzFBpYJdtpnt8Mnv0lCCfyCZYto5gmMYKiW%2FaIQW%2FPs5JdLM1Z%2ByTsSalPIPF%2FhqSf9O8ELHFCo%2B5dO0wniZFeAl7Yw97TWVAn%2F9lNvf4e4Rc%2FT34ux54wFOWlLohng%2F7ZNgNCYsYbroyA73TLg89uDrfY%2FL8IetGtLUXjXE3kT2Xkt7aO83cuOz0O2YqCbdveYmjW%2FksdIRz1j83Gfi4M1nSu6u%2B33XMeapDGd5go4nle3ItUuMT2EaZ4R2jxI%2B4%2FGOpksWf1BE3qNgj9qJ0Hc5oIgfdFMFaAJKKjQI4%2FPldXjcI0qQBNaWSozF9NRJ7zMA0rVQLtO51z%2FBmyml1lqQC3OzC1D87cBKIxE9MPZWIywg0Wg8%2BsF7KjXTBs8oGSrYnWVVudYzqBnOcSyzQYmPmFHcBdR5NL3gh6vYHsvfh1JU%2BoTm9ORLJUo0drYNL1lOzD93IwzJL0m5MNfduMkGOqUBaoxYMv6E9kjbhPtFgx3yneDyTmOEwM%2FpVFcHeWjpr575L22uggoT%2Fjfhr0bYkb2I8nGgfIm2dpguc0qyIlx%2FLxH51ZqC4Q%2BwmwUqnjIruMpcK7kG0x6LTdqC%2FfRjBVWKc19OzkERO%2FNwqje%2BVYL62jLZR%2BgYPKr805SPnzaAeo7bOvzV%2FZvXAv3fA9gvEbl63RJSiBkM6lvz0InpBylmAbAbDlnT&X-Amz-Signature=846d13f19d9252a0d3bdb8d6b1d6e658f864182437d8d3e811ce7dec35761a8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



