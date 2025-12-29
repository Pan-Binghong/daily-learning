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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U27WHDYC%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLEURHNdJ3cFqmlFQtAfO%2BHSuelbFPdnhepgrfkxIp8AiBl%2F0IW33oi7gOnszDlBUSV4XY%2BaHNmdXcb2%2FSESB7aJyqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbNQLXbPUsQa3BOcEKtwDgd1275Ix%2FIY5MSYxII7lGHimwB2OtGuVm0af7u7rvX5d4F96M6y6P1%2BFkXBP9l1Ra%2FaRyX1zZQJ%2BwjHif9wbql7aINWaphBUN1O2mxnIXxzIM%2FnRRRWAiz5LNtncfpBeCpPUPy3MyLpnYw5oH%2BHPFbRIi%2FsJU9X6uueBd0Cfy9nQ4g4GBpnluNSENaxmCXvccQi17b3%2BLcfCYFe9Qj1YnHjtq9ldSfZX1DUtclk%2FUGATdcGmnKtMFbRwI5UVhJc3ry3P8878qKB5Msy4U7TheqbtngWeSuJHmcFgOvJGBmNJZaS0fuzMpDyEomIShu3cP%2BOVGRuAMIyBPMzjp%2FcrybJaZ9snBBBvm8CQr9ZREojxkJ%2BdZ1FBF4QyvBVQKvxQfoUL8LhgN8pHjWsnNtVPDsxRGm19C78EfShAcfGuG%2BBf7AWNw39hvP%2BXtZrzNewgN%2B0yHceAPdDz9GyW%2BlQ3snbZA%2FgFJtv2oQDb9fyTZmcLa1aWlqaWn5ON7PmQXcpTxvBrHSKl2s9dy3PSW2BAh5%2BHrLQpUzngCYrCmURElEgELvvtA5RfiVfUjvMDupTzDiF0zhcb9%2FeB0OUaPk5nvLnlYuePNfpz7SDRgjqcG9RYdjZI%2Fbc4j9eCfPQwmpvHygY6pgHgYHNXcCo3f2A3fVX7uZjpa0rhifdyR8rvb5YzpXVbvryXRwgCwwSW3Sm5Nvbg9ysMHulynbYRKE74k2%2FLw1V4uroK56%2FdnsrUjosCORMU%2F6Owc7t2wnFkHGf9kO%2FUR%2BFPshZxW%2FvGUtm9SJDlYB%2FdRYCUWz62uk6S9K9XSpijW6HL2dFZkONYwHHPARLQjNrDHmO%2B%2FFFAa8rgPIcQ0yGzMfz4fEdf&X-Amz-Signature=cfbc7835784a43b63c57ed5daa50eb87f7d50e7da142ac0aebf8ecf58473e212&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



