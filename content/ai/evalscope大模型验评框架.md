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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCGYY4RI%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033739Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQD8o6pHocTTyHmiwC2%2BIc12Fjp8CPRJsmR3D6qK9H5ikgIgaZe7saM8xSt5%2F%2BcnLmCsNLCwuBbTgmkP69R315Qy6y8q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDGmIOrq2n1bGFmmH6ircA7N5B%2BJm6t4C7fD%2BeOnoDr0sDTl61ewbTTteFp8QoBwJ%2F6XQvoFcnbNpRGNepw2RSjeCv2Io8fgzp2XrTud7zXgA0%2FLLzvw%2Fr6IczvqhaJ0rNXUNPR9O2K1bZuwYoZ4WmGCXA9g7NRyg30bSd0h8AUF5w2h%2FvbnZugFYgFva8EO8tP5hD91dEfCnxKx9gM8qoSieOj0VVkbdgXL0dK2sdyKTsmjrHkKFIXa5BkCJl2gwCqhUGORUNKTXa7rC%2BHplxxBvx8s40KtC%2FCxSQwCSHkTL0V9bpaO2bHf4k97CtcwniFW345HrxKf5VzScqXsRUp0HqS4C%2BMgtU9pI%2Bvd8UGAaYxbk%2B5Vgty89RLJSZGyC9FXN2OZc%2FNjU0hajl5s0WMsPtQHciB%2FXAr%2BaXDQ1pQT3J51CESbtkwZj8civZh43vIxacjacE%2F3ILezZXsHmseIrdn43QMT10xEjyG3lo9Qwe5GZ8cBR90h2QuK%2FkQO3zEUMvfnQvFYgnm5Ipfnl7CZNe89A1AjQEDbtFf5aHhYdtGwKG2SJYVGQQjFaVQYOO5rqwh3PfYysbwnnnH7o82bBCGvRX0iEvUKatmSXBP4chJzS6Zf6pnbbKahvkMBnTPGIOnyJ%2BQ1yzRYTMOK%2Fz8wGOqUB2Jt9tryOZCO56c%2BXOvLPSW0%2Bfcs%2BMzN7xc71PhvBM1pVq6806W77%2BBz7xfZIzP2l2i%2F%2FQlkvwl%2BeM3uWvIw7thTjd2wWLgza%2Fklz683qABgUzAWkQqCSDKjb3NRsRb2mGe8aXBCm3O6In0D5tIqxKDPbhFty8jvP0jzV9EFEgGYd1tWjfmrn2PG64JbPjzcKlDLtSGpHU3h%2BGJESn%2BSSaLnuPvd2&X-Amz-Signature=46b0f3678e9bf2af4ce2aedcc5b7c585c7881fb61ba238e5b03842d3a224b3c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



