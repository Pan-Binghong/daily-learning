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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DMIVUF7%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIB9o5Iyhe%2BDolaBfixQJS%2B5wSMWkip87sTRXSGlZyUM3AiEAvYdxt%2FDbmjwdejXO9vIdQH%2B01fWpBd9UkoH%2BrOihzokqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCyeMMKZbFwDFRvW4ircAyhfZnvf6m%2BHPbGpWbFzgA7sh7fZTT83d1wHex2BHjnHaJaqKvJi2t%2BuN%2FJBgUcKd0FF1GYSudw5R1YKwHHZY9UI%2FqGvf%2BxR8%2BXkOMKm7eU3WXPWsirEvOIFRlQJxfVhsc3IeBl7SB6olpxLVpYKk5PI%2FHyejqKLzy3SsXYKgte99HV4ULcZyf3q0Bt8hY8S6fJbZ32fOUGU6ydevRWumP%2BjDbl5qp5daN3hlS7UJy%2BE%2FyJfRDCHBRkk0Z3emFjP8QBtwPLLlURqTR1zGDYt1F6DBXSgdFu5PZSqG7jBO5Zrer4IirhznqaKs0HgzEfK8A1y6yA6%2F2hCYMAcqGW%2B4dDEi%2FgeAR5OQTB3Eljzkn6Mc030H8IAJ7zOsn7KmY5EKC7ca8m2xBO8XF4dNuZn9cvWbH%2FExicg2c2ueoDBBMNt%2F4HYHv1vzjjfMw8qDwLY7fp6%2BLw51okAuo%2FXyKG441Q%2Fg4I3OpK5%2Bc61FlyLbaWJxPCYED0P1Tk7weyhpVht9dRTNimb3yTEuyGZtsgzeBj3CjbBUC%2BafDV%2F7c4rw9EszLjaLQTTnKg9W0dfkgxGFQb0UsBljNB6GGE3NQknebWgPPW27HuN0tkIntpCEE8FgjDwAiVaVYyVGQYoMMiTrs0GOqUBtUUBO6IfaxlTZdczzTPmid3%2F19%2FaDrgak3xZ6YpkPBBd8Gdin9h%2FRTei5OFpREgK5PwtTNLYVkr%2BSFbyQ7Ew%2BLWmZwi0TLCQ2EWYNgEIMGC4ZXpnc9SIvhsdOVadArLmZA27sKqIVGPQrv5ufqOb5l5Hh33nMAsHkmfeFKlWQzEzy1p8QxoRPTtSCgWIgv%2F6dVgTHEpQBs%2F7Fed22ruDM%2FWDPOYu&X-Amz-Signature=d30ec02809175408fcb7326490e6157a36e4dfc3cd31b6abcb135c49bf5a91db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



