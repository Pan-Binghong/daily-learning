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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653OHQ7C7%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbVlc5OWeD1s2YJsWoJ%2FKLYD1fxeGY3Z9H2qJHoUbAYAIgC2IK%2FZtmpSlRD9EaHNkAjftpE%2FEwXdt5CgUL%2BM2dunsq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDC%2FaFtvmCL%2BknshmoircA2UuwebIH1raZhYIeLB11%2By6kEbK1Ls9mfICmd%2FjCjZQjlYnvNELZTFnFgB%2B%2FaljcJfNfasRNRP5f4klFp4pOEJt1wRPTHjhWU6pSCRkr9rYco745DvxocL8HggGxv86CBFUYQSZGIgzBcpeerYdDqy3BmryrI3Ao%2FCiLqj%2BgSho0sGQ1qJhkcivnBqZjqDkpBf7Q5sp8KzzsI7NWHr8BorM5TB2GU%2Br4V7wsDfjf%2FsCORjUpb%2BWTFpFNHOHSdqWxA4Hz31LolCiTzu4JZ654oOE%2BhWas%2Ft5pnRD9rgcAeZuPLqvkBg%2F1KGik1PO6C%2BhPj6nXk3Pn%2B21TsmI5PoyWD%2F0D5vQLjHcUy6yaZyJhW16QmeZDOk1eKoFaQ%2F7Td4PgK1SLQzkQWJlGJeNKt%2BVjS2GPchw7QnqqrqY1N%2FRmOW96u5FuYJTM%2FXZW9dXETOAAjbhIce%2FaUV%2B6%2B%2FoYvqt1T%2BgWBivOlOcfBY3eed%2FtimUh6p%2BPMkTJix2AKA23juxNfI1Vv84kpzz8GRFb8SSrNXhKzsj8Rq6kkjqSLGRgbkfNnU7k0S7sXFJHjPvNPfLP7tXC6wiNmNqsS54eIYhUcQ4ZOYSF0mUy7okPZ8uf%2B2FIdpio%2FojgGnli%2FbHMN2wmckGOqUBi4h8ec3pyywPjnLOBfg8ouRsjgYdlyEokzSPdUDJrgP1Urh40n7jmDv7%2FW2UYjBdvFGbaTm3lzAewog4djkW0ThbpFhT1aGEyLuGUeqShwwBD4yz%2FOrf3tKkeUUOWVJEB4EHEVVkhHRiXLTND2PLFlOG%2FYMb4Qc%2F4zjQ14PkZvJwl%2FJMe7vB%2FfBYTKQcKyl6HDOm2CRmmOxs8%2B%2BxW8KZwoVikvjU&X-Amz-Signature=7e46c74f32163af84d374c883401c307ba89d7617062609f258c7a121d2ada48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



