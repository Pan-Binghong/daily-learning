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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBCPHJNN%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDrmpmjN8xesNdh85MySi1DuoDqWxzvzczgn9pUNnQbywIgSZzDOsLhskaKbCno3oAsQcEB4Owvn313AmcYwbN2Ugoq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDMx2i9%2FlB%2B7KB1SzySrcA2v1iyaYQl3okTKo5fWlxluNX6XuHbIA%2Bb%2FLqVbvOV42pmGbDCv7mJ27hJOazG3c%2FgdvTUrM4ATe6XWY3g4HQVAUkUv5Dj%2FQ9xvLF3l85oW5lQT7zkzMPdvZaOuIIDoazhQHZTBaitWaBCWh3xxbRqi13r3EiCj7wOGb9HNhT351L2x94YPbAxwd6lZ2GoSo8Dnp%2BuNHIZu%2BzzuWsnBttdUUa%2BbchxfVDjyAClDk%2B9LvacIWyaF4ge0qXYMXMwNa97A1GpewUWuVmSc4OzQIkCFDF7gG82Aa%2FXQAmSeQvT31jlBXtKMM2vtQoEvB%2F%2BlUdcw7%2Bu96ARREcxlc4TPZTpVFT1mebyebo4xAHL%2FByB%2F%2FTwzUvXR%2B5RTgWOHnduFy52f5jYI2%2F%2FltpU9WypY72zwV0TTurdplLdoobwvwyvI7FBcfjyIfeUok84A8UCEA%2FAYA9W508D53RdPs7bbnQIL5dqRbp5bhhQcQxRPuJxpB33u92HHfo7KGqyClm81Zpo9HU7LRMN2xg92m3VxASAcSlcElDqNNAGhqx2zsKYokkJ72cv9%2FiFm%2FwIfmErFW6LQouLGQ3sRCwttbuAZMJn3EPqoLjLVU8DF%2BFpIHChP1nf6T5vDky3Vv1BtoMNWF1ssGOqUBvnx5j6n%2BGLJ9y6Lr%2BRsdxrvNjQToxip%2BpB7u5hzZFVHfdJigCllON3Tr%2FajaFEiX9OXhmbi%2BhDnyUO0Hfqh3vJPRdMhGIwX9AwgE3QrjKFzUhcvvuc7g80iytd1z%2BwvC8y0Aqk3Mg%2FgtqgdpJa1jpX3Ijvl88nTTe5xnqkx3H9lziOztNBuk7faWxbVrCcBoIGVeDYFk0pWjbjotRHulzUqj1lG0&X-Amz-Signature=d49f0ea7fcb02bf56277b8012b1d00778261116c1aaad89cefbd6fcab04080d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



