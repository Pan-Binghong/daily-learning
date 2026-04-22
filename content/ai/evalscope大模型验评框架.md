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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRUWUWTU%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIAyMV6wqGjlaz5fvQeZAsS2e2aQjQdY%2Fl2sQHZ0wIxo4AiEAuNf%2BrcxhxEuy8ku2QovB6irA9JHxjmoytn74lMh0x%2FAq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDHVYcLgb8uCOIguVhCrcA93u0h7UzDupWbHWui%2BftATTklhrDyMMp5JYEHCboiEEloWUKefSpJTY6cLnWAluS356DeWr5EoRfsBBH%2F8s1ZMTrQTkaLyCE99S5rT%2BwuqzOQxPXOdlCH%2B26SSUa3wQ5YH0TNTnESHcxEvJEkOqLm2MlozVnSPxsh77t6O8CFOOoC5E2A7zy6h9dcsz%2B%2BmUx815w06tnwFIWos10pegaw%2FsS05FnexsVKV6Rs1OFzSux%2FvgzXiTpAvsx3xnzEq27rsS3HQx3Yp4DdmOjAnI%2BYV1TtaJlZIk8ddVSYXonhmfk0q2i1ZWbLCXYC8dHfR21eb4ByxK4NGlYYE4Jg3O8oPXxT3tbGtH2e%2BFFcEfH0LxpWs6gfJ6w4NfcUfEghU41djC4IKUcPs7hnO0%2FBzuz2SSYX%2FnvcKkLKNjpRvU6vcCM8MzPKcsLBT1g7ftAAoi3SVvjGgxJ%2FEiWiRDjEXIQtkleVm95lQQ0Nu2snz0kSqahxr17IQKXcBcP2QNf9c%2BLqvLr9jK3FkpQVuygguTcUGprW9WEpoy80Z5rq3Cr2bkpzHzEEHmEewkPR6foCCu6L5e%2BzNn1%2F8JwRErgxSjTc57AVY6Ppr1bV0jeCNLADUEmpRJJT7e5yCQM1DwMNr6oM8GOqUBa7VpcO8sg5VuCFMcsibkLTaLJxNXUecl9rpqTALLYhK49zR1ypRTffl7BdemADkcgZ8fQuo7LGlZ3XNxtBhEthlmnBDXQR0OoogYQkXDnTVw40izgOD8cPoS8DGbg24kMzAAK8pgsoLoVkPbhVVJAMgninvr21k3HPqoy3HAPfkq%2Be6mudG9EZ0sIlSe5a%2FibFRKle7j9hn9xY3mdr7xCWVgd7Oo&X-Amz-Signature=0f32ded7c9e9d8b30d1863e35e71ab97e772e753ade582b42579bc8d384fa7a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



