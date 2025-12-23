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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCPIBBV6%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIG14k5ofvymiE8A1MY19AP403sBYzgkIia%2BCuNgDqV2wAiAtzzlnBjQeUUwEadKGxvnBEQ0dcxKduLK9PeBiOiJx2Cr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMSnMedYulCsJ2OSkLKtwDb8QrB7fzTaUK94AXdaXEJ21AKjhSwI3Vu7HCk8p2Ek9KbcVNvAGVNf91oyvnRrCgAWWqeKDKfFipyi0TuCueMmgaxCKmZW885ZbDYITP1yNOrDWBHqcrlphnyrMpbvdMNY2e3qsq%2FJodxPELzBY7a1h%2FthHI7J4czLWAaPFwMHLIOxxRbMocke7F%2FRe3Qew%2FsxAtR375miVm2DoZyR75%2BmNrdRaCwqMsFHgeUiRxPQSpRjesb7PD%2BAsEaTBslriR2Rbw%2Byb8DfXRm4b2uvoKBAopgIgOlEkkxsUUFN7RQ82mhMRmTdTTsPnW%2BgSUY%2BOdhBXYdkFSgSU7DzoNzpyynTzbe2JqrgzHPy2Cd45IFM0ngipoplFX9oU8VpE3lEqx2diyT63W1J3Z39hQM5mP1sZF9RxvBnDL7xJ%2F5pL8W3g%2B5dA%2Fus533RArCM62gxQ%2BKKg1ba9bUEIJ0MSvRAsw7Farn24SB78K6k%2BnG5DiZnonGOX4uLHHLurdU5wGGtZNDKR4%2Frpvbi8eKVvfhz4jZR2mBKyF6m1tUSiUhuM8Z8R%2FBXNLPYBzmPQEQJ7SxcVvzBV3gbm1g7IjJQ961Ok1ln9PTL87awyKCUngXuXlu%2FQw1tHjzc6qONhC9bYwsfynygY6pgE4fc%2BTmECTQEoXx5hZnD50GV9oUvfl7Tf8Z4e6U8SF7v7E%2FE423z2pKX7yJu76pouRx6x6l%2FBHQlw0cRu3NMyB%2FWUgQCJjxjMxxxzrK8E4Iy9KfwlcT%2FjI0qYFwmAwZ7UKEfxT9TALpgVCU4JoxXgXuYWpUnXc9icfiPqN0J4qI0W9KOHdVJQfNTX5kdwEauvz6tCRs%2FxWVFp27qGICudwNT%2BbYbZG&X-Amz-Signature=8e24f7d5887eea306131bf33f6baf54011ede5fd9c77d47dc4d5b5ba5f398c60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



