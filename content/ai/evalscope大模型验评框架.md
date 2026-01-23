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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FEVH2SZ%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDz1a%2BFPE3XrIQFBDzaCnx1sSZGrgq48d%2BPbS6ReRfu7AIhANdYVWIlXXZ7R5kob5i0ngEmdeVZFwvsgQ52aE3feilCKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGMT9yCZevuADK2%2B4q3ANcgccyw4PlNK7FfufKp9MUgKZCMOJXJqnRD%2FMz41TSe628N6qeiqdgowjBWorJezRuXcMZdXPg53cPoZoXBXOu4M6KzSPTasgpSte5VzS5nVjgN8B76PVaTaZOcYoPTuF2RgA3BqCJCX7MeehIRy88LeinpG5sYZaYpIk2%2FWxh1LNFx89q7WiO77RFYIxtOTxP7MTyK67w3F1WDHrpkSesP1OfkT3yxt1vOr6Jjk0DZ5jm9dmwbMQtGRpwODMGmpaoKZORraOyc%2BBqBSYlSdOqmggmM3jiNoPjIKIolO1BhFN9YMz3dLtCcQXFD5rrB9bsiWu9uUxBSybDVg1rchzCsmLeFW7VCqxNPODIDu0TVExxsKDxN1qB3%2FHZeH6mmqSAtJzdlA7GT6E9AiK90tYF9eL%2BhNjVpYzMRSca5mVR%2FjsfLyClFLG0p%2Fpknfr7X6lg6dDIJEZpbFHn2LlLxFI9vcVpXMFzb5EGngHDPlcx4udbeaBGYlY7oAlgVBapp%2BJhW35GrCuJ9zwGIQ64E4rurzxLv1xxgKAFYr7UwYibjjgF9TBv7yV7TKNED4ncdzQO11wtwi5Q0ZOZdp3DqMLRgQfiL9JH99bCh0IClRBacuVAiOc1vE7EgvsFlDDdrsvLBjqkAcujIgrrfX4j289qjAmbPMDLfDZIWl2RjW5WuopDfH7i%2BkHMU3nA9sDdEmHdJleo6DfwChBRfY8l%2ByjEAjPmVry4AvPUTOwFaJqIP9x3ZgcYY2beVdrnMYx69AnizhRd7ffiPSMHhjtbtckRy75OvZliKN0aYpO1ICxywE4nCWuwf%2FTrL95W6ThZmF9bd9L%2Br1qAoI4HbSECaZdmwy656YLfcAdO&X-Amz-Signature=79fb88ee192beb6189e4f26ab555a9d087017f6af0aec16a4bcc6914b39e5842&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



