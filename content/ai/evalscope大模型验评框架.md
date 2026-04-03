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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2AEUJKP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIERil8VcTF8KfdxM5BDpNFaGbi%2FI84Cv02NZ1W8rxVMpAiEAjFif%2F2mQKpGFQ0MNYlkS5N8KgJK9hQdRivIEukHFWNIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGnDQslz629apyb5FSrcA6Ubp3FHggV1Usi7g4kF9UAavSMXokQ0ZlLgTlgz%2Btz8bRUjGlhQ2Bz%2FOMD%2BpwxyViM6o2wxmV3mVPPHtYpaza2lNZ%2BO0Y2KqKC0u2zdtLhyaYRboJoYYlpadp9YXtnGO5tr6RSD65gIs7KAcWC%2BgGTnS1WvVshG1vCPLtRe7kH0PmVmvmxCbCgQaSLMKvnRZjWYkKhBw9ntd7GeQGqvn%2FYeh6sGUflvjfJlSj3ljm06pk0PS0KTgzdzkHqTFGXAGa91ww6yeIi8YeN5VrHX4t1G5V2Xjxo7eQf7WaNmk6%2FOGJ6IXPu3UaniQ%2FL65ZQAT5WiwGEy4jCnSdTWm0U7t0wAEL4G9xZYmdzF0bhYHDgQjvCIw1eieJT7dP8TBy3vwBvO8ickVwaiHYC4uLYodwtqOeU9fv%2Fps%2Fg3SQM%2BChf0HSl4jiWDpYxG1U%2BZrs%2Bi3tq8a1JSo17zjTtQC%2BtYjDaiMdi7GKqVHIFNyHKVyjZ12TT%2BX9NyxbyLARi9i1JrTEyiZZ43jBdgJFgf6geT64rB058DDtM9G8YszfnANDt3bSafJ75mC1SqEW1XkwkYAfhSVG1C7Ykbp0dlfM5AD5E3VdUdedWDuIryBTLk0DyxeW9kau4nHA9pYZa%2FMLblvM4GOqUBlhXkCPo1ADU99lZjcnJ6jmn9TOuEzD4RMrtsFYZ86idn6o2qNLpDF5LQUikp2B%2BvvnsxDHE39EZeXMetNts44FzYEnYeOZ8aeGIlcbhY%2FDjg%2FbOmf6u1hsprLRdD1YgQv1kIajA%2BNW0tvHDQOFAt9FnkMNsAxDmPduv0VkqTyocds%2F2r1l7ZhLXesXcIH9gYeEBGYwu%2BYop4lkO9D9qF15x5uPyI&X-Amz-Signature=f38009cb3e7480e752bd39d8bcacdc935d7835dbfbf815078bab83ac6992c873&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



