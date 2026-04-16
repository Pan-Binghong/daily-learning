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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMOUXRIS%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFIz5CR0lvxKW6bJfK9qhpxtWnJjpiZI362DO%2B2nnNxNAiA%2FxFeoHNOcFc2N0XhzqQFt036B6Ds875JPMiIw0AwRoCqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FaTtlAKGj65tA0C2KtwDEHbvlN1Hb1wjZ8qi4buMse7%2BY28mLMFp8tUITRJN8SSc83sWVSdVSsuKzucD1As8ykYm%2BhMLR7SChPzSY8Jc1qpkkTIP1PBavJHsNM9BuBu2wzPn4XqKdRTbk6shVofKcjiHOfHj15AUb670VwhhqxKS%2BJdY0kHQMW9BPzXyiXtkpq9txgCupPODdu8BLUO88dnDxyD4xag8RnSa1XLLfIFZTptNwwDQ5tHxJjV7aj%2F99KpaU4%2FgPeM9Gh29iAsdUaV%2BIRm4ylBjNNozQ80aN3awav3D54GdC%2F1rEY%2BVHVYbQ6dTo%2BGfa9Vzig1hJPJPObOKocqlWar3ZPB8cqhjPng6edJuo57OcoxG%2BkgMWjuhK%2Bf75w4x7KcIYB5gXbqZOLFOhOY0ozcmnPqkaMohjKDGjwy7U1WjS00v8YY4ZuDbZ24txHpjZYfxp7WnDFlP8uhW8OFRxtrxF24Mf6tFOP8le2Rv9zhrHecHeaetSwtMq3So9Rp5x29Uh5REVBfabaOAdOAXavNFCTlMj3ZdyTBYasQwSCFRjLn%2BkKEuhp%2B%2F1HApKA2oOVoZAVTnqBcL%2BcJ6cHTCHXU%2Fhu2HVy%2Ftk8cnR1Ys3WIVNbBgd8cTTTmc9VzHmA5MOkJLl1gwsbWBzwY6pgGzm93%2F2ZHh1UgND%2B2bVFDKLNHSU4y64McRMbOafQrwliMJMfM008EpW77XJbB2aIH6SGoS6ob2TbPg8rib%2Fr15ypmQAP3%2Ft0LYF6tm2PatbEGQTSEyExuI%2BUUlNxZkMd6BFwKzUzExuZyVRuDHzQjBQKc6Uqnc5KvnyGOzjZICiCjD5DFMQsBkQpuud7O8ePEmMWP%2FjmAJbr2%2BqtHuW1uipH7K7fQ%2B&X-Amz-Signature=69c06773ce378c2e8359b30c371f32cf00c74e0fb8f169b912c085722fd65509&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



