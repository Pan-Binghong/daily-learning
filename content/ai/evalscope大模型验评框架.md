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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OZWL2C6%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2Fyikn38Yw%2BO6j6gbMG4U7rZBeoHWpZWQptoRG9jr%2FoAiEAxEhucZBRdM1B6cjgYm9oAl3wo0SfY23fP9FK36i0PHAqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHOtmf5LwCZxTSRCSrcA%2FnxWTWSFOCkp9yRdrnLfMwYgN8fJzGIu7TAMq%2F6JCHaDT7Z0hxOnfWSTFAJgk%2BQPumuEAKaQ%2BW0lsvXywnjAdVDJkgaukspeHcu2fyQr58Ceu8jxYbn7P8HBc51snIFHG8ycU13CrTnmVZMznqVooNu8r9XGJQQd7AJEWuusu3LkMclUUJQAl2OaAZe4rGACI%2BjO4VwB1IyYjytvjh3Gc9L1vSILl2sD2nZKLAndPSGxeRoR3D0kmjJfJ2SLCN1OoFl0jomwiCgevBhQCwcnjxTboZHYrZ94sJf7vKYOohanthColR8DrY9SIEMbJemcocWTKpqd7R5alrwRYAJxy4PYq%2FZNA1zkaGIp5cEYihK4hTy9I1ngll570tOOtspk%2Fwhs5pUj3fEfy6l%2FyrWtsJmnJsZfJ2O4u29M0fHeNXYVVYKo10DM8ICmWZ8VK2m58Qbga6XQrTQ8MvEF2XxsFqre%2FRpG%2FZAHQ7o1WJi%2FfVbBPxWA%2FjGCGpx3Ti%2FDErebi2xF1RlDWPFLVOYk5YeB%2BfXvMQ7ZUdo3Ngj31p5olGx0es3S7mPL%2FmU1v0y%2Fw5z8zZGM8Lkg2yUpQAtDhYd%2BGMeRgLSnJJUX055EDOOW1Oa91Q0vknJ0v12KUT7MNrDqswGOqUB2djUXYqkuRK2CPznaD7m3oszdcHhOvBz805eVxAmmJrGwl%2FCLQjExJ%2F%2BekwTqx714%2Bg3x5HILbhaKgHWpbITbkSmFcalC%2FAcrUII%2B3Rho7XeNfFRQcfym1hHhPeKO0%2FfCBd09FTM7sQzMrRMe4Bq%2Bzbau9czF1WDux5ILcCLUy4ZY7mUeu9wtRhZUTIEFWg7THEkRgcafuV4Bn0AwcK3eMri2F%2FH&X-Amz-Signature=46a857126b9b69edf36cdfa7e9353ab79b07ad23f8ff7e1b4ca1ed1b9eb0ef0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



