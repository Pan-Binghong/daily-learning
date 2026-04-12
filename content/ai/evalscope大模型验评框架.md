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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675EI36TT%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtCkPuyoULK4IELoNDFooEZga3N23Eq%2B7fcD2H05EyiQIhAPoKm8SycJi48Y5ygHMudqp1C3AJfgpMPcUqfxSzv%2FdFKv8DCFQQABoMNjM3NDIzMTgzODA1IgwlXnh1Qe%2B6fBIZF6gq3ANlOg%2FncRayOuWpiFQH6iWUVtC5DCUBYmjFetIij4IcvOWWBiR5vcdgQbFE4LpQ0fktBM3U05TD61Ovr0ko%2FlPfjzMyQMqn%2BpcFBXYZ4%2Ftv6rnqoR2EYJ5J%2FVCE%2FD4sDiDldyRO3Dxp4Nq1cEONo03bF52jkO%2BwaZA2NPlxBGPc6tqWFtvYVDAKnyAefhCt0%2F%2F8eaBcklnY2S5NXlFZt3znTZdN%2BMxCBzf4kArfQik5120aR%2BeGq3r6J1Q2gT5En%2B5OwctZJ4QKpTFoh4eyG3oM6R7d3smFn2nC5ST9VUZy39rZ2J1VCG4HFTU2Nx6dJRVMWIqY4%2F4CWf%2F8s45%2FJ89Vdacur27hZSVgiVJ5Z8ij2iVDZ7zgpy%2BKociZtlZE8eVaddFQ5wwWqgXAJ9LOQ061uXP1kZ8Sa6xK%2FIMjTnpVVNQhNBqIfg2NmGskZ4XJGEhb9VTJcsjmSXVdDU0M9FBx1K%2BkplKpdLhBlHJ%2F0s2GtSoei3J5ID%2B4TfuUxFuNwXdxVJt32m%2Bx%2FVfV%2BtMeznGe8zRh%2BaZT5bYT7vYAmzNtAPXtiHBsnGxS6uGYI7I%2Fs5qUoKj2gGoyKAV%2BwqJMN%2FpdzkgjJgfRF2B9JasYvB4Rdtozf2qL0M2ONnATxzDNiezOBjqkARC8AA5cgC61N0tksMcpaZmCMuVCVhsJa4BUkacG0inKm36MZrvTgmjXDXoohhcKyT9wAwQLRn4rlyPUSgInFgivwNht3sJHp7pOKBtTv4e%2B5L7IY4TikXpEt6aoMx%2FY9wI2Fv00GjXi%2Fd8NtBmmv3mA77ytcTLsl1asSHkXms%2B0c5ZgRA6OdAdehv2KnanKvMyD8V%2BU706sVTEvUJClcW8WdI6M&X-Amz-Signature=f6f3ab8dca616355af98b6d484c013c97478c3f65dd9aeedfa1f0e533c83b98a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



