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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZZTEYWK%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICnOK1eTx0B1QbZ%2FMr4U9xDChlcHPI%2F3BtnJKSAltUP5AiAZ5X38j3mZYPCLinfek1htBU%2BirMkJTHghPigtIQSJPir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMl03wjIeJp3mspjllKtwDTqhSdrBybxwSARBBs8KT7jd6YCtWElPywIl4xfGxEALZ%2B2Hz6a%2FiPEgB%2FEeusPijKVM8zsYhXG7chTOzqaIjy2%2Bw%2Fcnda3gR03XDGeMyYKcK479xZzM6qtDSsFA6fY%2FTjGNKLdKXq2CVIEKMP47%2FUkogfXU84tjadVGfB6TrkqVPOlMmB8kwx%2BlXAEFX5fZ0h%2Bxyfd15tV0ixOv3tD9AjLuLSrsD%2F5bvh%2F6P8RCL%2B20YqMWvOYFLstml59DprHoyC1KlloBf8ebhPITDksft7BKEFlarKOLOfiyabaAdYPW%2FPMBwt3tfyGwc%2FdNjqR8VPmNFIPPbxo8Yk7aRzyQcKESupaZcg1miAnr2ZFXHv8DAP9ksRVMFxsKGOaHrDWnPQQXuo0y%2B7AXBnIogeuHEWNPo1ZdcFMJSr%2FQ9HQQFw40etTg7Uvu7JZQ2Eu3rTUeXgKrTjDiNlQT8YQkoumXbWs4QAjlqLCtYhovw9i5tDUG1HkDSn8F5paUy6gQ8J7qKz3AvgAXE8LXlAk2JRuGfrxQS175CSBekn3AFfvn1BVxoQsDvZGo1RWHb6KgOqat%2FZrR6NqJJB1J1Ul1jOgf7gGxm9Ym8it%2FzwEhena64QmY4JsarhH8hyrMiPHkws6DUzAY6pgEWJTo6FAsmuiahE0vgprcj1L9qQ7yurVcOkxqN626CUd9w0c1RXwJJp7vKFImUbdd7%2FkXNnLdJMitNDYfoDUldEvj4bc4VXDYev7cCYHBPZXQejj8LbLqD29ngW0aqMG2P42CXNVxi8ktKmnWlWT4TbNccUrlqTyAMVxGcwtatqFAr03vO0ZQbkpHArDCj8tTheFyAjSXPy61iOQQGHhniYiIkq1%2BT&X-Amz-Signature=72376503ef053174ae23d968e7da307215264c57a3ec96741cebbbdc48fad213&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



