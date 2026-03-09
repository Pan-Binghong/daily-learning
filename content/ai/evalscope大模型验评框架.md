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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3PVRRIO%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIHQeRJMBKvCkay0hDQbOwRbXMalkC3CFD%2FH9nusJX%2BWWAiEAk0e5KbTReH532FQZfD2kSPxNaa6CDDhHiGn45OvZlnwq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDCX2vKfEsYfkU0zG1ircA3S0Dk7zHaz%2BUjDPs6yXIb5O9LP9GqBpoB6Jj1we%2BR7ovv7XFeetdjZiiE49foz1S7zHVjGUfeU1sOtC5kmtUOD7OTf%2FWKyt4lMG7V44xJLZj0DC60l1dVUjfI1VVA4MBaCNf4JtpaNcvtVPw6JteEkT4oj91j7ZG4RtK15Ed0m%2Fw%2F3spPm4JBl0ABDAC84w4Onke6GDlmEQdQkNow6XoIsUoZXGbBFwYjEsCgvslkY1HhYvtTlG5uS3s7qzxeTy3%2BRHhcvAGxWmE4r4wtgv8EDmKqLMF0xtL8K3JwGhWOoi2hxRQcL21E%2FFFwN0xghXzu7bnSSyFKzXVSPbY4Ldv%2FbOea%2FF7kB0LgdUPfPO4%2FmTJGioKlTvGMpqo%2ByGX0qCqQg8ZQ8JmiaQbvP0udtE7QwFAg3Cv%2FLVsD%2Fp6pNQp%2BqZ1dyVdQTPzAL%2FLpVb7FQmv13SQuMtMOzGD7kgnP7IsmchubiWsCBPyhg12Ivyxpw6ppZu0fWMaLyer3FSrcqzUC9LO71zkvckmgt3dhW2OB00kqlIqU7DtiQDKhgempSHdJ6mSgkFMN7yXnpgh3v81v5%2FUpeW13z98Tah2%2F24RbCvtid0eSFCvxyx0RWO3%2FRKdX1UOvvn4jMl4BBOMOT9uM0GOqUBOVJ8HEHbgw86TMAVLh6cCMpmyEyZvSF7r%2BKJf80yKqxLmawViD2sWZGD4BVQO%2BksBSkDSHtTvepmzIgD0jD%2B9rMGkmK2xh%2FaiaaecI5g9RBxYCmqHXJZIezc66u%2FcvF0xGD8ymA2H%2FI1W4L%2BVBMqCHeIiU2oFtIwJErFOLXxW6zoDaW79KNlKwAtw2iCcjYCRtGimjqhJX3qLT8QQjWpo9fcbiCE&X-Amz-Signature=7044dccfd9fad36b192e50cf73eefbc5028e4822628efcc04ec8d48f41236376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



