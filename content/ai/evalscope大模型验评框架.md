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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHQQAAJO%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIBeRvkvZtK0emrffzHBTO8S9ftuFODh1I72wXPALh2wLAiEAjrro47rMQMnisJGG4K0Jg8%2F5wRSzBSUA9IpXk7JxRcgqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKxUMqloft7QSK69ESrcAyoOauI0ovvAZkaU2lxuYAJNSkcozrqN0uRLTnbTIFHQts7qLF%2F2pLv0VNzhH51sQX6Y2n2KhmzEasQ%2BwOcaVlldEM%2FQ%2Bz47amL6aAXDSZJXMAoM4Zfshc0jnPUoytzK2BDKT%2F3wkb6xoJqIMHsiNlX9sRIZS5X9%2F9Szfcy4X97pgM2vQsszrDkeZlFvzoPWQmYMuCDBcgbFgm2I86S0wdbUBFy1fjAfx%2FzH%2BOaXDiI1mYnJ%2B1TPl2LH%2BSG7bBfUoXQUHMweBJ8Gye0BYkYMyBaVnnWlLymLqBo644S8hj6StocRTtha58uAq8qy%2B%2FeVapQi3qnLWxR4X2yROul4g2oqg9ptikeDa6Kt8M1mjLsGV8tU1vrK4QRHj8y4jXp8pKcBnwstK%2Bo4Nbx1wx%2F1LI1EpkDik%2Fb6yNvhlb8gKLDiJy%2F9neAfz8SXREZoEhJ9jH4oM7LF3yHGsE8KFZnVP9e2VdLoC20zk2%2FL5fa0W2l5NAS4R2SXhFMbHkQ6HLULUu7sDdTRAerc2WL51iCmICFXLurd3EDFJCJUtB0AMQWKPxznqGhh1gXIk1I8%2FzKRPtP6O27lCSLlmRrxwVm1iatUgPXhGh2i9NB%2B%2BIXXeT%2FAdakEo0H59JUM%2BNKKMPDz0c4GOqUBbRUm69Km5fCq9WYpJwxPhsO2Uf4zZDcz5fyyrKasJnoRACvbB4Fj1ebMkRlQeoCc3wtwep%2ByCDPTPAQdJSeXb3FMC9o7YNAyyIgH7zr0YtZNUXXZvdA7Vh%2FY1vGrtoAe2HiNGuMa%2FYLUxGHYRPrUOjtX9DtaOAzaHW%2BDsqdJHbDIabfiEXxZpq%2FYbnaRwK19mb71YlqS4jrO90pqqxSM0IXrKYQq&X-Amz-Signature=b6bd5a07a397a1cae685af27fa14b18b52e2dc55507ffc47f300dadde569c1be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



