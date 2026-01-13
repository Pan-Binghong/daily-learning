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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYORQ5RG%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIHbKy%2F95HbBGPMC6ttFNCS9hwapfb6m2a2uVDnk%2FWfdwAiEA4SManyp1mvpn%2F1bGDVsQl4Ksgfmk3Qe%2FbAodNtj3p%2FYqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHM%2BVSVpO1A5O7dJCrcA6sBFBb619ingZWl8cbxyiOvDUAPo93qTxaMhWNYOvRPL9%2BcLOb5YOp60rdNzr6bs5NfRv%2BLFu3utTPyEl3c3bVK0rrV3pe3RU3BOcsNp8KK%2BinWlI%2BPLx7orHJsCNQx%2BKxi8oEDWoJuiaTYRGC4KXkUejtvO8LE9%2B4r4sruNF3J%2FpMjdZ39N%2BZZzAmGBQ6Z2Ak90ZXjWFL48gbcvOno%2Bwhvwl4jb1QelgDN0K2yu8%2BbU4doShCDD3PH09YUQJZmsFcC%2BtmdZoUH%2FBsweLdF8FPt16HcRykbsq7AYi27A6Wrgqi4S2HtWlSFZ%2FkjemAfV%2Feq9voDZ%2F10lVbYmiRZt3PdR4AxWmEn1W2f%2BO6TXjtxxQ%2Fl%2FMyit4wFEH%2F7K%2BTQiZMRCAJcxBi%2B3lSKh4heWgC6cPufuqS%2FssM3JNgQCbeu%2BU6vIFCVmCmmZfKBh%2FnLdUgqfF8fwsypY9ST6RqnSp4Kbk5jVTiNC6wshHtCHf6N%2BreS1znZFg4kaxgnJqaDwg7CG1Bb%2BvUUXAU%2FHLXhFUay%2BjTup8P%2F3%2Fr9hReTyY93v4R%2BXTyvfBRDHJCSBRSS5lwqWsZpRX%2BS3eLWbCgAt%2F%2BhhHMsgMpNOTSoNFDz4SptnIKnHggoXbRkya5%2FMJXnlssGOqUB0Qi1vWPug0MmNt%2B7E4ZtN8XoLkdmHEJHQ6FD7pNvueo939V3pNDsqW3%2FcKkBgooMeelBXQobURioRZsbxBosSf2oJwe1jEgd%2FsOjuMXT9ON3HHz53Rqo4nw38pdXpH%2B1I4puBwXqIaykwQ4yBGoMecl99oXfA22ovYT5NnVY0PrS2TmtRLTg9f3g1clMJfMX%2FsThVVPtmxQ56s4pkiJ6Js18Ksbs&X-Amz-Signature=dc76307adfe722db1b9ce0bba7f4a349a92181547bb15b8b5db5bdb9f93a0c6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



