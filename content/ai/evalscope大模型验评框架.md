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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ4SVDCQ%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICovZ%2BWpzqEEcGb04333LC068CVcBlXStXfd02XBiOmSAiB%2FABEX6KYREEUX5dckYfKChAJrKEgphEKu0biOQxGkCyr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMxosfZjN%2F8LC4gyz%2FKtwDa0eLRAepXrFNVPZKyjWaJMJnQdu9wtDnEKuUlMimNlcCOYri6RLmORrXJVlwSLUysbhD88zL4owkydmAIVZlWQxNZNWdLWHUNk0Ia9XtExoJTSl%2BX7SnLK4KQm0lFuk4TCdNCUGTpqQvfHsuS9DnVaTr8ER1eZKe1kB3T1PZCtQeMh1p2gDWCyk%2B6uBX18%2F0onFzag9SnhMnpQtvc1nsNNr6%2Fct1aTPZquDJZ9lSB%2FhMqijgC7YcPar3IoIJ6lgtUk18p%2FPLkfZTQFRv5ugO7MhB1%2BYP6qI8JaHWA8wLVzGG2vFIX%2BkOyn9C%2B0B53Jyw3xtfyNvPVdqbkwQ6ephPejh4WiLODq7RbbHYsSURaJ5Kz8LlXx%2F6LvzMETdIWX0e9PLRSHTwFKM4IpdCLlYGYJQRWd%2Fhh7WC3S96sblPpVLt8heSKPIWupl6xJZcQ3G3AT%2Bw6Tlev1d69t1J8VTjdQTmA4%2FTg4eBxK4M7wqZiJziExVmPxo7dfkY2HIRcGYBDr2YCtnBXXRajGVW65ALfIzlxWCRvCMQQH6rUOgYxOSwGARUVbrhkiAdpARGFMH9U5gejGVSjcp%2FqH9h8Lg9vwAZY%2B5hZLUAsRMzetafNdMy3NpyX0HBLsZNnmUwg8SazAY6pgEnsbiyeTyPymRbdIv%2FsRc3oFc0wF4auX1PQYZFgvWRKoivaImS0E0OuLDrLt6nU2BmFrNoXHGzzNtdG7W8WfLPRL08uEVTy2upGAfDP0958q2NgpCDjvA6NHagiuioUU4IDpBX8oQ1WD1jSuesV7iB5neTKZ7ssUMmjWilN2fHwrWcxbNIxnzCvdsE3guvjTXtNIYqXdgTCm9c3szGTru3bi%2B835V%2B&X-Amz-Signature=50601b467075b97a58216a94e68ce5f4a3d90c5818ba2fcb4d81fd393bcf663b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



