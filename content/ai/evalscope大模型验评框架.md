---
title: EvalScope大模型验评框架
date: '2025-03-28T01:13:00.000Z'
lastmod: '2025-04-21T02:58:00.000Z'
draft: false
标签:
- LLMs
- Eval
categories:
- AI
---

> 💡 之前都是使用vllm或者sglang官方提供的benchmark脚本，现在尝试更换为EvalScope框架。记录使用该框架对速度进行基准测试全流程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQNTFMYE%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEwKFPS%2F8gpaMwzuqyWzb2GQXG%2BjhCD8xPop47buE9OKAiB901nAGJcgcO2e9Ls0e%2FxNxrKr7cgTp0HuoNpm8N2M4SqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtlcjU0P4371RrivaKtwDW2kqL9D5Op8bJcLXGyUkhktT8%2ByeVtYDIhTB2erzO8ZF0DQO4f82W9OqYBZ5N42v6kvHj0YLPTV8j6cd%2F%2F9DQBiNhtChTyQwZ0yx5Mdf1D51%2BPpmno7enRMXcAg4KGWgHL2%2FUVcUXnfX48sL0TMmXsTyQyD1bEoCpRf8aK%2FRK3K0TzLsXVlOdkNYI5VZevtRtwGviL6xQpKwCKO3%2BMkqei5bf9mpVwsJMu3jjnnKRnvrBVCBRhE3CShWfpSPm%2BruSgI0APBy%2FAh%2BJYnAsAwTd8yij006QSb6DCdhWem33Acs6HepDJsSXOMajrRmidVxqBnKln04vxO5P5zA9jTHueezb4tP0%2BWHlpO4%2BrIX9%2BFr2I9xq0atDW5T5S8Im38SrwGepe22P9k7QHyC1kEbsLs%2BMjjxYlpYVHAf9B9RBmQBuJPqRwBYgUdteOFkQpan%2BbwZZLCVlD6oAbmgoJOfjHtHMdARhiRoVz8enStcgMclT5NiEp37M22OqW95lJ4sKTQzmSFAoyjkr6jgCdRx%2B7DKkQudyBQxfujmEqcwUPutzM8knPMXoigbR61KbO0%2B5Sd9wefDbkW0zxTC6cRfmiaiRbHokvqRfTfmmABMLeOC9jSKsQ4cVoK5s6cw%2F6KsyAY6pgG5NIzjoC0uSkOKynhgbXTNwFKCy8FPQ0ek0qZyZ6QPR26OoXXQ24whouax6PCVFfvLeYK1BMxH7YKXu%2B%2FO1KGkdUITFt1J9hVGgp%2Bt4NpRavsJ3ke%2Bni5mS65Y9iHnBjeVB6yndrOK3PC8IMugx7Np2srmGj8ZnouBg6p2AKDok5LJqwM6hGGc8etfVlliKoDS24JWWhGSj2fG7Cg1Z%2BGpb1wQmYl2&X-Amz-Signature=f97a64027d5d523a4779f494b542bafac94fe659c4d8579111f0df0410497770&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



