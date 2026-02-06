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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PU3JZBJ%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDWPBSXYglZtFCHnJFtQfWBr%2Bidk5NIXT40vlpqyXTYzgIgedAKdXkOPRRgb3CfJzojGk9lJYcYEHSaFErQ7BD5Zo8q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDISmwj7%2BuSrwkIC54yrcAy0fYzlSlxYKyFxopKD3i7M3%2Fv2Qf9vM%2B7LtC6WEAoH8IFl6AK5ROAlLQj%2Bo1CGPLsYWdGWhVLfmBIMrlUxZmIdtlsCz0iPsRBf5zk7LGrtM36rPtiDFBzYt0tXtDg5D7Q4Zd0OfifTGayjXGi9W9S3jSAhDgcX8xVRLwnH1TdvCVzvG3KWgCsjXalbYWpMkDgEE1fKf5ChDFLQhbRF89UhvqOE%2FSQStLpKUwX7ElFbbgnBcIy75eSXhx%2BOB19lKRupOwIfm%2B6xXhPCBZIssjQ00tOa3b0%2FBdotF8mN8OnGpNnOaoKVnfZ5lNv5%2FkPQk0UdL8gJHOwggF3HSwsAjVJ%2FPT%2FwZ8CRLmGJNP9kXBAZJTXvFZxFsN%2BZz1cbR93tFqPBvviK1pK3%2F1UGml3ash88nAJKwmY20el5SNvo43ls8YwiBToa1AkfDl5rsatS7cw9dBFsjGFyUWT4wUDo9%2Bt2uR8tMApFslSVfXGCo50scCS83YUPcPKYz1VG70OyumExMPUu0Wok82FiXhMBw4PvVUA5bAMZkLyf3ROV%2B%2BW%2B0%2Bh0vkSz1Pj9%2FRx%2B1I13q8rzxrrfsYnZ8vTo%2BPWDq%2FmIzOkpOdQrc62K9ntcg2h3UBv868erfsoGx%2BwZVMKe7lcwGOqUBMHWvPuB8xXQxglXAv0Lze75gNa1wFR3vaEvf0ZAwsZojV%2BQVur989EVrnhPQdi6TYfb%2FGixID2vYE7%2Bp9vwUY728iKh7C%2BPgX%2FVWGpO4XEAfgiYVuGKnynYg9ZB18dLS8QTOgaJikUJ9O4GTOvadQkyuFIneMZIUpvl%2FJhG%2FscjbzMwhhN%2F4QC77NRFuZ6A%2BwarDOZ%2BKojlFyzgtuQiiAXCfMBF3&X-Amz-Signature=1e59b9a9fd28e25dab36a56f864eba1fd8fb55aee8967065ada7cafb94d31ebf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



