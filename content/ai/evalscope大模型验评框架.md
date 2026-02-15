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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T45SCYWS%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIGbKFrGGVT1NcA0VR3LHGgC7AAENww1r77u2M39skOB9AiEAvxGjmNdwNgW%2FdTyY7nAVCfSg%2FeE16AmCJAYB18l2kYIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDE3Ecj6mmW%2BhoBz%2BJCrcA%2F%2BI2JpmuD65LsLOMQHVkFSHTuShOCNx7uCMeWcItwhRTrz2XlVZfFvQXX%2FHniO6YPgJvJlSbGlcxqOmSninZt0C8XGm744fH%2FnVWBjKQUR8CfkudJmhvRcPPJscAEbXV8n0kHL0UJV3mbBKr0QPw9Iu5q%2FHVeAqUezvfFX1s8yhxKAGoNN%2Fv5oE2b5LAfOQ4JwQltWhnJeDgxl76QgCs8Yc7x52CkwOFps4yoEk930PW%2Bo3iU61aKkqjipM9BGTwF9eBirf0FQHpC4S5jokCag40Ef3IdhEfYCdpRC9OujlojJA4kDVMLSGbY5EkuKzolu3NCCkucOLSzgkh%2B2Q%2FmYovUp3bLAVo258%2BLXRQda8ryaMcxusmzz3XtxtSGmn2bn3g%2F%2BR84RYUBhOfyINg0KpQOytl5rN4fcx9xpaxZMK6BfBpQXg%2FkFEfWWPXzjc0exXCsTOrS%2BY%2BJGH10mn44Ewfm13gGeUBVyVB4eNcsd6jDU688PvUSBmlkHak1CjNSelHIjt6MxjLiQg2%2B%2BpcWJ2NiITPsbMxe8ex6w%2F2aGJTgY7zsCsNKfm3roVW5lO%2Br8nTHkCL0eFOSd4Zmi3QtFJE7O0q326RucsYdzN%2F4SwHx6hBb2zeQ4k9HG%2BMMWexMwGOqUB8ngY%2B4JapeCajdINiH8n7NrQIqaLrgzlpsrzsPXC%2F7PzJ76tlY8Omepjt0HZLRvErj%2B%2Bfx6b3wT6rjOidY33N6dQTe4WTNNYnXnFQXCklndH7%2FeWatJ3Z8v5VvvDOvgYNP2T73wpVtZtgoU%2BF9eREvQFrWoQduExixSmsh9JbdRk8ccvhNJl23B5%2FBNeE63rHUH6suVPZoPhwmfFXHaqp61UDWNA&X-Amz-Signature=2c674e49cf78f09d03f78d656f0fbd48496177bd447cef154c0c6cef9fa67a2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



