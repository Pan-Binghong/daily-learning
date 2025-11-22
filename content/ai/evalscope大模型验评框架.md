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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDLUC47%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIDzPuWrvBMJ7EuuVAEew4xzyvGqfIBoEt%2F8pqM%2BCqRRqAiBObFQMuVDMMJepVt0HvAaIBWoWRgDpreGCvGeoGVI0Hyr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMKve3Ru2hTWdwapftKtwDm4gGxU3BQ1rw65u0n9PAhB2IqRa8x2VzKq0uDjy5WnZECsn6cx6ishiNKotya2txCQHA1gahaWQL9cCXME7j3qqcH5YkoW8B%2BPggKmmVT6tQb31IrK%2BEbUqR5avOR0ParLzcPaUUArtjJttKXBNxD7AwsNmFSW04dlGGkHX5ArpC%2FSsPkvurqEC8IEbKVKvLRY7rqGUJjd4VUNAEGmNl3J34N18DXmpv8yG29jkTpY%2BIJkPrEe15WOAiyrq%2F7%2BJSOsGlEFFAKQviSxgoYyWKlFgW7OgwcyuG98W3kiyK5uF3UuzKLj8E8eQyap91UePMNgL2qtIFNte1%2Fgh7ItcIUq%2B%2BebmTFQdqnuircWwGja7uel6YXivlmONRbxqm7OMAfI4ZC12xVbt7jq3g0%2BU3zOGjdEzRTDfBTuMSCK9aVZujWabaEaga0ag%2FixJLgq73g6E%2BrG6iQmNR78dcKfSIK17N4QDNL3FM0Ovp5OX7yBAfRVwfBU176F4jPplFX6%2BNkCrsyI0mLaK4xcQVNYc%2FHjQCUNxfdZtt3BNiIjt%2BeS2p8D5HrL1%2B0K8MYmzFxAMlA61cXk1UIo9X%2Bmq4GgZss5K0pQXJFhqRbCk8bqU3eUX0ljIxOWH9Qn%2Bck90wsqGEyQY6pgHxeRIUSP7VmFg1z5QCDFh0RbFoftz3I0F9N1jU1dn2IXfJI7HW0iDAebL7X3EsGtQaPw9WewssDDdeFK%2Bmm%2FeNxRbb932Mp7%2B6CDUJUpJmNJqZoEwE6bNu2fAjyjyvvhWpbSk73hF%2BSh%2BZ6eAUNPwO%2F2VlxuK9paWq%2BXqTBgWgmubWLyyACoocRzGerlDNlm%2B2A4GnFSZ1%2BxK3TpTynPQU5HDgvUnP&X-Amz-Signature=23ccb0fd9afa2326e0c7fc58cdaf2ebd8dd64876d3c673c33fa9b6e63cc5d730&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



