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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4BDZTEZ%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIHp0qxlM6s7gicCkUvdgxlyUZUlPKVNeOTguWW1UqieJAiEAur0jJgy1l5qiM3LZ%2BTS6aS6Ba9HTQy9AGl0pPv%2BSPlYqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFbnU15EfaRj88dCPCrcA2c3IxVHLQGDmAQdDhkH3w5DFqQtbhNjcaCeNP9xvPaxNaSifIvEqTavC9fXWiWv4roIHzm0jaAb1pPeluCtLSa7p0NTe4B5KS3um4xnVbKiXcB4E%2FWLrH4hof6it5ezmZMmI0CrVQTBUEY4uHhf18VUorL8ekn%2BsJWOgEIV0X6iV6JnyKRUdGcssT9x9isKoO%2BaY%2BXK7hE1A8eijUQuC8awq5e0UfVmCzaez1WOrBJ7zc2szkl5HWhz7wX1B%2FzCwcIJxwa301kcHeK58T1IJn0SbvlCEwdwN3zJ14WyzmG2iFc5G6F61VMcd%2BF1Ye0GlO%2B%2FEa40GWqHDdKv0v75zAmbwCuyt8GLOSfpnmA1m%2FdnNLjBQBMl%2FWzp1kCfcdn56KdAl1%2BHf%2B0g8iOBAb%2FGUwNudeYVgtedY6tCOYWOv6IbIbL5cNNOnHH0ITpfekL6Zx2o579gYw0r20D9WDbWg2ephQ7B2ZwyASHD9G9uTgduJKIczg84tHfQ1p%2BPIotgQy5maLJIH2W3sdH%2BODoYUSXKuE6lJnNEaqmFsmxjnu2HIJm75tMq12vf1qFjS1nIS55kBaKW1z342rgqMIoby338RfARY9kzZrD83jYboJecW4fYjxU%2BiCVAH569MIy19MwGOqUBLIXSNzswzKsvrvOc9pn%2BmFI4d1SN%2B2cD1H4n6KbecVkm9JN5U6TazbI23XYMYkR1XF3wSqyS3dIQXXNEsINyNxdX7V%2BCedDK7JAZ%2Bhud6E3gznoISK7yJeKpePj%2FZJwJ6nlx0OekEU%2B4vHvSq8x6CJGlBAfx3Gx4qZRTwoKiBnYSqZj0uHtcYcQ0JYroOUzyxsM424Ovk1kcK1Yxyb12dG8AvT4G&X-Amz-Signature=0d43185e643ce5a1ca2f4b0d7b8a3426577e12d060fe05a486b457988027756b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



