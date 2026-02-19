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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636GYKPKI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnkPuY3yg%2Bu9oiIGCZRTHVZYVHR%2FpXRetTYrOkrRpavAIgJfteSIi%2ByTKBuFbiLwVtkCT1Dq1upULPDGincT9aInsq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDDbTMUWfXfMCxUw4KircA%2BD6Ht5Worv74aRimkGKIKGiMxBOhW8zbuuhr5e%2FPyJ4MiK9Twgb5fZkpVh1DmwYZuHoeDb6E0ODLNp3cQHObZNEouWewyKW6sK%2FNAope79pWYCC2q7jzCXGK%2B4ZVI9lbK5e9x1Vu2Y9LAkLG7D6QcQmRVNoJXSjYevdgqaGBKRXZcS1nWofsnG11PYCdHiDmt0AwqixlZ36eCsWFC9ap%2FYZi8Sac9RuPV4F%2FF9Sz2PHduGo7ybCVGACbz5zHjTRSfacnUnnt2mk%2F3ZFvzzXQHdDGZvnULta44bmgEiA1ttO%2BxOnojQhlrwepvXnxUsTisEeNlpvgfIqNkaUdiT4JOavPgIBrZ6%2FVtDjAqI1J1uZpIAMZP07%2BipDvHp9MbmYrxC4vfp1gcYLm6dR%2BkhPKhjsq14j%2FRgdOPziPDDYHJ8GfI0DeGS7nclIvumR9Dro4CsmP2LJpymQrLBMHKc%2FXFkb9GT2SLAXtUrlaH4%2BoPoDKLQOgH4QvbgOxLj1AuvDNG6r2xVCK6A5Iw7tJoekvTpEYXhBWpNUkHmapvDik5Fddf7zbLGNpp9RKESzvIJHlXwhJ7HK%2F%2FgJHu0zW7ftw2UplStxmUiMizQcU3CD8LGR1tPW0XVWiOwNuTWeMJDy2cwGOqUBPKujR1p1jvWxgxQ73X%2FIWWYAkaWM5hx2eymxM7eeOM80D%2FLCe16GDf89ukDfSoPfYCzOPVD1fwm%2FePabPxaZNt%2BsYDG9xz%2Bni0Yo%2FW6EXJZMWdEz7%2Fp2cTtYCZyHxhRAQewLXDhFSgCRSJPlsABBS5dD0ogZQaMuUSGgEt1j3yRdESCEC9uoh4vW7Z1sM%2F600Z9S3xiIJwsMcP2uTB17cJCOOcmg&X-Amz-Signature=8b6c68aeb3f31ecd27f156c32a74e3e876ddfb66d58580268688c5c5f38af66f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



