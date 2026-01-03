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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WM6RVG%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQC1FP%2BZl0OGzXsPXDEyQKC6FxcQwTOQ1SyZIGiEQnKe3gIge%2FrCHKyjSJz0NKT5Fy%2F%2BbDNJHkQcYH4DQKw040A%2FVQ0q%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDMfkoSNfDGeo7QEboyrcA0nmhjuR4VMg%2BYuS6PNE9O0oKAQPUadb9JYuwNAmmWIqi4IliYZBwf3O68Gl%2BxmUcxFKbJNL2J7SHXljMFjDVMPU4E8xApFxTMHeE2dBNdgQKHi5gHtA17AXiQ2HoGZ4hpNYu5bVuIDZ1pmNPN8R9VaSE%2Fi%2Bf7aZn0ufA98l%2BzGIdnZeQJ%2B2H%2FyvrVvDioZrmtRNMF9L8QP7ddi5mK1xWYdPLofb11B9HS9fRXdCcU792J3nSLTV8tnvuqgel5o925sPHjmKUbpD2xbdrO5a01hra8sMNJAE8uJXfOvhVlGE9qIbjpdrD56MHWokxdhOy0PALG6XGpLiyDBtd33LlDAcioEYTdxYS5RbmF1tuHAJ4XhNC%2FPGEUDSEqw92C5qhHztpFW5g2zlZGTL0SWJyjaEky9I2udrh3DzJn7uxPRcITKZiKzFMWeZDsl81vZqUSmwf%2BkF76S7YBHvt4oim%2B9orqr5dRE8okOJA%2BaTTWv6FtVMD1jIRHQ36dFmHO6m%2F6K%2FezfrS0s0wRnr9NA2H92StVe6KNQtWBsL10eftWS9%2BxktJWHNeama2SjbaQQOcCbK9aFHBelH6cg0tAGaLolaxAPnsYNM2eqQYMZIj%2FSI851A%2BMERb9aWrtiDMPL34coGOqUBi15ZGse%2F46IxIGPR%2FfmeeYFEzu%2FvbKUPhy8PtaED3IelOc2h%2FpkONzQN6cede%2FyNPNfJ%2FQM8JSAt5O29yg7mmK94QhNNUTEmTKQwT3035wBBttwPlONsRtQ2YJmV74Tszd%2BrNcJXwtkvpSscA1trbtHqNU24FabBZ1TDMy9YKJVdVLxpx1JyQ%2BdGXKUftmHVNCT58w6zJgVS0TFRQN1BrqWWTYff&X-Amz-Signature=40388458fcc6633693d7e335299e4f5b3aea75baef5e4176d8e52eb92f0cf57a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



