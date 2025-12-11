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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LBZRKXF%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQC3OqzvF%2B5mkXC1RLcTBuvXYDdaHcFQMU7hzCdzkW1KEwIgL82zRGB6MJcq3B%2FIFkAN5q7uSISUBBe6E8aK%2FGMNPDwqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj%2BeANJ2TbQtzurnCrcA56M2gDWjD1wd2FsaC2ar3dDJgYgmAn9aEWg5XB6XydpYC1PJgirNE2NsP%2Blj3Fnpn3k1Ff21v01u9pHp1uqN5V73cB4mujMUSCUrS8H99UIRgUJJgrKoKbRMZ7zqcrfrQs%2F%2ByY5E789DvEaEUcqQ%2ByHLllfO9aEcgw7OEkr2f53QBdLmNganFM5uww15x%2BivY5fktosGw73SoR9B3d17diZ4TyhBWntJL2ITqLdCvJOJ5sGlE%2BzxRGt1pHm4o55XXgW9NH3v9DQwGdPLoUloxfsd3BlV2qwH%2FsoQzjA4iWrcmmJuHgVr2bVM8XYV2KvKt6tORjSEdc0KD9Ojs%2FPxHcZ%2FFZLzKqsE%2Fl%2BsNjf2K1spBJTNRC2ABCIPF6AwNOZe6jOnAC1eipJlxrUGyNlbYb63lmzKQ4mhpCcNNeOMDZNJNAGH5%2BeKPhVz5z%2FBwFLPSjjzBL14SbKbrgY%2Fw6kdfPIeBpbXxBNWWxVPhsWst548oI7kfmvavN0U2%2FlNmLC7%2BZd8IOIoEe9cmhNcgNi2nCtdXYrb%2B%2F7r%2FOYOikFYqVHduR2k2F3EKt%2FW8aLpDLT55Vlp0PH%2BmeTtWuPSRn4WdN70nzX4E0%2Fmlya5J%2BsXANZSXQ50Ze5%2BDDgU2peMJO16MkGOqUBR7aGpVOHJRbIVaQU8Rh3nKZ%2FqTw2ud7phzAN5OfGBK7znkxPtnA%2FsqTX8rcuyIcbT0MLGxBbMqOdTS7tKlkHdUKoXZXo6a3VeviENb%2BkJUQecr5t%2B1WcGMdlatZ0ahIt%2FmcO4Zuvw8J32wBUq72FUKUdRBhCmSQVdroIg1pgvbdnfHOWbZOQlGA1Mkt7swJBMXpQAobktrQ3N2V1lSBaPrSudrT0&X-Amz-Signature=297a0b2cb89a47c95350203fc4d2195430826f2c57a6b5c451b62b9e86f2c755&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



