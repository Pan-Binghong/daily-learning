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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQSWALZF%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2FfLdx2OtBG7tL3ME6PdlDL7xDh3kHHlhflKoHKu2vlAiEA6i4xd3ibiJQYv2bT%2Blb92vfH1XfOixSXLuO2YutpIXsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDPxF5ct1ww8Gtl9jZCrcAxTCMIrnDLKpSrMtViTzXNEZ121Zv0zNg32SRhXyhMqYLfCYvzRZmjSDE%2FStjOHSsiGcDoItU217bIwfxG%2B34zYJfUxARGClnmpLjL96jdt4MyuyP7EbWHnvE2mOf%2FxiT4lU2rbhjph41zqw%2BW5Tdeb9JgiVZjVgOBTLTL9Vc9tyfJsU%2F%2Fi04f3RHS53tQk%2BKD32xSRzsRGNd74biMfTKMwUxmWBSQu6XBylg9BFS5GmEINfDn8LThqtiewQH29B2oKgh1UPYAMh6BjWft8loNBh7iv92j4%2BgEw9252eyG3hyUpOYWgxcdAcS9hqymadcNhnWX3rau0tDo%2F20wUuB6ypGDBLv%2FBbgR%2FaULTjABWF%2Bh%2FKHnADJZf7waRg7zWfd1511q8nIpUR2hXAPq5DIF%2FbkLOWPmYYoLFn0qZxutU1iiubsM%2F3XjDeOTtiAe8Kvz0PgeWijzgdra6bsZUe34pEPv%2B9pT36%2B0HNylMh%2F0PA6xXgfarqveigILpdS5M%2BV8eIwLX2VRxPJISLtxOQ9HFEj%2FWfYE07%2F1tbBGaGB1VX6%2F4i%2BaB7ZIKBoVfY%2BJiUUk4ATVyq7sePvfN%2FrqOytABPAwmwF6CfxliOJgsuNpfkCBqeS%2B2uJT9XtjlzMKWJ2sgGOqUBdH69AaA8iYiHpRheT%2BWKDlqfXV3JZw0IGz9boV7R6ZLXjxLeZe%2F4TRLGxbA%2F00XVYLVMb46rLG%2FtC04JXcg98hQbRkGyyCdbk5%2BsOJsXU6hMFWlVhtrRtbehuTRl3p%2Be6eRM2%2BzjjYs881rGdCmy7xeFtcBiFJAYbca4%2B80vAvcoDRYIFRtIymZoGbig%2B5%2BdH%2Fh1N5imZmHxbeUT93auu4OLADA3&X-Amz-Signature=8dd54f060383cfde6b64aa25408deb0863c101a41d651dda202c0334fe65e85d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



