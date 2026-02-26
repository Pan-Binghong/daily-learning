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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKKPNLEL%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDIGtflVpvwtC0pIO%2FA%2BncoQ2JgACe6J4xX%2FxThtoHISAIgVgsCk%2FkjEGoZS2dWjPQFUtnxCysvkkv7Mn9r0D%2BbO6kq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDBHUDj7RSgPeLriCOSrcAx%2F0US4lUg7jlq4TgdR%2FqCq4Kf1HZHqBAkl4OETRHXV7sks8DgRWWEYCcv3YLICrPngxUWu%2FY3WL%2FlmB8EtQ%2B1T7y0YaK856NCMHE%2BF5Pwqm4k6Us2Eyj%2BtNKrJWJFRx60Va2NcE2u6QpCVnYbF4PknecNjLPfND3v2Cmxi8lb7B5NkuDAiMYKeP8QbQDKxNokT%2Fn%2FsHTn5bNf3jk6wloO5pYbPaaxrI2gtp1jQHXzZqFZLrzRj82VeWSnC8g%2F%2FOQfnPkMf2meJPtPvoSBzrnDoA5Bjh4PEVfQUwedVrjDjdKyCwRKb80cBG4yM7HeIMiAVZZggR7nTMjxnU0CJ9TkqQLcXrnR8ytqdRsSvMgyOj%2FytIlImxvYmdchhHdpQ18FGIM49tutUGgr52SZS4JdLD%2FnG9kM2lc3kxEtPzanzHn3HlIYOBKLQrMue80P%2BBtnHZkaUH2PPBLUL39b4KIiauBYV1mM5fH3yLniYV6Ti9byUBgXOvHm5CGqsU2T07Gc2tz0agIuAlyHzZ2iN4nuE%2BQU9k%2B7YhmzmMlj2ZjS73nBiVXFUME2VukZAOfjhV1ukVOWdRF5VMZmjkfk62L%2FFPBFmEnEWY2nz91%2FRvuYmDGa9yHUGzLSwHg2fJMOX0%2FswGOqUBw41%2Fb7JS3%2B9juf5gHw85%2FmbVniMHY0f1HzKGWBOkcR1khux0kx9%2BXUfW0eTWE8TkySZv24ZGf11xVMn1U2kufC4TfPPcsWLdpA1iUffHWz9fRP637b2yVXZMJCyzxHUbgZrQ9641EZ9ofCBmwQXzDwzc3BVsAlXL5OcSZhcQb1kKFAPJGJQAdobtZ87WqeViu%2B00n%2FhvvdBerDcz4spH6pU32vXq&X-Amz-Signature=c8175a7823e7e8a78290825fcb14217bbb1a761a4433bf25bf840819a3cf1997&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



