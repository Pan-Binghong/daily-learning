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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TISPUIMT%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQCS0Mka8%2FInKbIHX26%2BPrzAkTNxLMiEfzAAA3LHC%2FpE8gIhAP4WfELKKju65OZaKkiALAn76M%2FINjw8ADNB4XEZUniLKv8DCCQQABoMNjM3NDIzMTgzODA1Igx6AvWR2U26Le0CCukq3AORgHGbUBfdgXjPT0v8R33oEU4kv8zdrZJFUuBmX%2BC6vb9zT5X%2BcxDtlK1rZvg4LUdeHeParA8KvO2QukbZeuGOw5WYAzmY4telQSNw2SwlTSCL82LDLQtQRN0L4Uu04QvGivotfp%2BY%2FMK1XR%2Fw4FYtOiG5w%2BY5X%2FalH1Pd5zlVmY6CUVP2kE9AZ6OnkSOAOkIIJP0H9qN5I%2F6Iq62h8wChI8oUQoauLx6SgU6W0e8Gs82Z0W%2FhO9wC1lC3q%2FdpK2px1%2BlL3dyBnfREfySZr3VTUoFeMEjJ3sihHv8HGa7zBWGHlGdArL2o38Oegd%2BE5cchOt1gwuv%2FoRGEVxPU6TxcUG84EKkk8bnJnDJJeCVFHn1k53LlCu4qMbS7VEl1sI68%2FmWle0x6PT3uk%2Fom%2FhO76e0FebuubHIdoTv3dOgnFgdrlQpHHTS7%2BIoXzGWleN7FMs8f%2FeZ%2B3QQFdROSS3gJ06Rnpp4zXjJ2q5JTEfvlbtS3VCRrCwfdNzhIwq%2FiYuFYCNq79h2AClJfS7yDIR8ppwSlGcxkokG5yVCI58zThrRMvh9CJDKIwO5u26NN1Vge4knqb%2FyI%2BxmOyefngjFqtemxhxlSBhcpW2zf5igMHXyopjevUp7pQ0wDXTCTxuHOBjqkAV1VpAJK26ZxlRIvurBkzxrWs4m6JKSMD2%2BnTGu7vOc3Hpe2jf4DzPH84YIO4VQPgSEq0htYXRcJh3PZnyQQcDY4T3UQ8Li3jyTr9pA7Zg4TMyWUgKalK37AHTxkZE4MWJXUFC7ipIpyE1UZvK%2FKrE4Hknt2s5NjsEOHwtWC0gYbodTY4rN31IE2hKhuXVhvpQWrSyLM%2BxKFXL4JTZwsLYE%2Flwx4&X-Amz-Signature=96a7cb33d343c6dcf4f1f4550cd7067fd226d1cec91f5370e89752184bdf387e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



