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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CWT52U2%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQD%2Fg9M3kh0i8aQyI19JBDA6a4%2BeKxjnDfORT4eXbI1gJgIhAOncKj3de8heFlwN6Ch7eFJw1q0W12wv5YHouVFcO5TjKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzu74XPnMFUEowgthIq3ANyOHK5JK748U2WbBPLcqWG4QHapRhNEnwEJgeQKS586u7We9YniLfB6DwRuoPnJoUCakKJRdbgKMadL%2FlIaLxtzc0AceSw5OBoSuL%2BK80oopCg%2FgZSUG92kYZ%2BlUqf4uBt9accLpgtA%2FA1bw4azVygO3nk6Yl4DliJ0GBDb%2BjgPVN0AFgwbiNu5A4cEqsHMCJ9auV9C1CxBb71hZRA4sCXjphuKbekFKeWYtL%2Fc3VM9m%2BKDoe%2BTnOrGfpNeOyHBG%2FfcFM%2BPcRSltp9ezxi3tvIyZqirmQ%2F4q7%2FCU%2BKOoKWlSAgwE8MVbcU2Cv0foxvKQia1j581y%2Bf9v25lmP4ZXoxKuWly76Uw0yhlUtooiEERPN9QgkZIWkXukCACyhk%2FLa0fPzPbhqEYE34stuHbAPVN46WUiZLaEQeb%2BCgvFDgiAEHTgXu68pmQ8zfxpgHcndrLUq3WX0YOI7IyXQeouAOJDaxKaHs%2F1OSWr7stkPqGV6Eoz0uVwYJSrI9cWV7JVk7qfIKNZ%2FOasRjAL%2B%2FXQ3WtSNhWDdK5npAZfJwBQ1nG%2FlAcHRwdqVkvRj%2F3pzR2fY6cniF81Wdz4Z1TBdD4gzmYGI5foOTfV1lOOhmFCfHNq3SrT3B%2FeOS%2Fn9U7zDIwL%2FMBjqkAUWvq%2F4eKPmJXIPXKNnABAYSPGUm%2FLtn0ee5o6BkQk2CfsUuU08Nl7L9%2FW9p7r%2FBVUvhcMZSkU%2BMfMNpGPjonWovrrF92IL%2BxfQun85z9z35QR07IA9SGJDS8SVDYEKjTXmhqH2fc0x7JttuXgk%2B1nCdcY06xq2c9f5vnipLnecmiGiJsf31XvtDwgIiTX7EvayHwZz2R8cI9AYzmvB020mfFdZA&X-Amz-Signature=95b63046464699ac75e4a34890ef7e0ebbd206681f94a96f4eb645a63ffa755e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



