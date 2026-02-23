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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2WY6334%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDi%2Fg5lAXy6x88UCi94KbXLr88Qe0JrOKi4NPKxAtMcCwIgBblAc6FcEDoP0RAfgobbcx2Id6hyWf7XuTrI5EHSDBsqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6vDywIfiODtB3FDircA2dLHh75aIh6zZISLNEgOWzyKIQbHguSW6rP8XO%2Bn1l%2B7oYVUkYqYOsid0augylDeP41V89PUACAz3FpicBXRM69iPrNzXqldROHklGuGdSipCXvl51kX9fUtvwwDA6Ao%2Fmvp7GLsH4YKy83IF5EP5sMc5HhXAn1bkMM0RWrXEk5bkkVcB4fo2jcqBg2np0hM40GVPZw%2BJ9L8NoqmP3RKVkb3T%2Bcr4yjyfbxWV%2F92j1M66P%2BSCIx4ghD2RQc6SoaZ9w8FU34TOem8qnSLGo2GeXp1Ui24Meu50wAL6k7xWyGYENLy7BLZdx8Th7OD1j29KoIgJ1g0RmaUQrgncy2kM0x1roEY4e%2BXXjuG%2FWdRkTA6p05stAteBH%2FB1I%2FVOJ5uJsBPFRuPWRUQI3Q3KRhr1p9is4bWVq9fFybwpzSlepOqD3ljXFv8R%2BGXaJMJXKmuGA3ckJcmc6RzEWv%2FSy3ph4FW2JVm3wfmZ23jkzxMdtGYBN5w25HjgZtT0Grm%2BVo1W8NPHF%2BKWM9FLXwNys%2BLUMD7yye2uVDgjCUJ8jDiKDpjJLTaoz1NSvS3K2UFyXSSTjJfnbu4utBtTIPwkbVjiIuku3bNHS%2FIDa8UDoc2HjuXKQwyTc54ZuNwJZ4MICT78wGOqUBkVsOBPjHtjZqZkjmqq3%2Bi8lmgim4k1FK9tIqPakiSc6tznasEpT1zhv3%2FXHX1zbp4kRFrTE2m4%2BIYw3uLefe5rwApWx2NpXaQlas%2FlzzVNyhS%2BIzZmVCUIpcxJHYLkfJR%2BgZ7veX54HL%2B49lIZq2W3e%2B0sN34955be8xQctV%2BdmM40z9u0SZbbVrOwyTxTAWc8sCgGNaMKl%2FfyK7OqtzVkBF4WuD&X-Amz-Signature=9af9173987fa7d94ee5de31da9290f803597400e9a48024f59d24253a5cca239&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



