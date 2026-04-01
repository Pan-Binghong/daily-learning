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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6FG5DEH%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrOBSwCeN6p4ydTXj4%2FSzsYa3LiR6whArMB8lAzPx1DAiA5PloOdbRNeFxe6Y9XNtqBmXO6xCa4HndPRCJK7ORW0Cr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMl4NhCfm1AMaPKSk3KtwDDrdYnHj%2FjkUACs0fflMeW0IqTUSXtfPHcQimBBAHpymkmfBYUHgK%2FzmUPEvupEhZXWfnpUI6LELkPIEvfXFsvoRN5HR0kUVLkmW%2BqbIIbBEQRbl6Hz0DegxfqKCxLpdJj533DdMSErUAyfIZzzq7mMfmlplSt5FnWIOcVNTv2oKGDkeFUkf9Kdv7qJvVdt0tGZM10My44LMj2R2Bwu%2FCl%2BKO3XIMINwCtIH4QIwi2Zuw2FtAkLk27Bk6fVexIXqA2H7oa8zko0huCZJDiyhiV2CcLm3DuldxfaiXAjwnRI3zdUASCojsXNL%2BQpBXq4DlufgwGxqAv29ISVUXyuLMsPT0Sx8%2Ful0Lx3KHL1YAGqgELYhnpT6p6feupRKPmHHEY3Vp406xLW%2FvoF3xtBlMpKpTVvaBmjuzrN48Pmkq5Lc5v59L%2BpiYQRKgbdLGZXEngtoei0%2FxGVfXI5uJe9cn8LUmWSbgxZwwbRz%2BI8Kzf2SgFHzmpq3bF24Ft7dvmKq5IwRLw9iX80nFGwMRVKhUjQaqfYRIf%2B9jKa0c11W5NK%2FUh6ZsQig1juwbMEMuCyaLrGNE788w5k4oxxVVBqNa2APM6enTUoeEcTI5R%2Fi9D5hmr3JzFt0%2FJs9iW0kw4qCyzgY6pgFEbFEh0X4vHfVSsxSZXK5Y09UMr5PfoMA8wicshrf9UWr64bgWDhAYt7xStOcG7jRsCGKYPdtlOCUrFabbdY5gz%2FSfrkEe2pCaR8LSL26jJMu%2BR4RyY2YdzKKLm5MXxjxgEIvG5Idjsx%2BR4VcWMeBzjfG4%2F8pXMjfVF7GPFjiMISC63pMHNJ6Ks9TCcBgLhWyNDGndaLHkLI39toN5b6zpnB1WYWtU&X-Amz-Signature=188b6b608512be8fca86498ee051349ce6daf3f69c91c152a534f1d53a422c3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



