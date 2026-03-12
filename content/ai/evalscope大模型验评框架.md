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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTXUZYLW%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwOtOQadxEhvyg7lWyyGEMoB3zIYGsjc84bm%2Fi2OMQbQIgCv1huNz8a3F6ZK2aA1SrKylDGeoHQDt0uxEzPcEGhBUq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDEebwvaHfY66sqX31SrcA0ArzVO8H9xcdRg8qjIP6kHQl8Ms2ANNQ%2F%2BGE3BxPe%2FSJc2a9JEmhTJCAJphvdZdc8%2FTqbGs4Ru9LYb97i4eFFEw4UxfVPS%2BU%2Fv99OWcVPkLuegSEyoQLSYoRoWYhmRB1iDQ3sm%2FS3kDSMnAvm%2F%2B%2BPqcv4OwEv%2Ffp%2FJP6bLf7s9wBTv2n050yI0wnooyk88i4EDeWWdve3XIGWVdhcl7M1kqMxTWUMXMPG3WiEPDNwnSvmSPN8xVsDUXV6BLfUZD2vHR4qwIiVUC4pd4H8pGGXklie1NbIOVeGoFdRX4uw8qN2W50EV7U1abvw2z1h9hjvRZwb2LJHr0ncwAmwB7gvN0D9%2FqmctMi4QRW0jJpaiWFN9l0z2dh8prTsuhhWEn%2FY%2Bo3ZBnbtYY9njk5x61smNrJHPEMOiPlCpuM8JYDbwIcKwownV2QEeBkPK0s83gdMn%2BeD6oRmnLkUEUOD3S8nj2%2FFNk2yIDZYobXEe4cvMAy02PcudlVz7oTHdWkMcdxXBSHXNMORLNVyINo6VtVxvOZqTDGDMyrUn0AqVE%2BzWraTQ2MxdJdZ0lKKp8lOv23n2ZX6hKt2XKSC%2FfF%2BH%2FV6AyTTiVYbybp7d10SN%2B3hhd6YgK51K%2Fg3QyI%2FYUMLGyyM0GOqUBziBfVXneZrdrtu24Ldhj5Fo9LrP%2FircQlhlKM32oMF7ohY885cHYOWzPFt9lyz3v63y7fSkWA%2BBEK%2BXwebEaBZKiSdCO6P6saSONtZr0tDdnEkKneHZOcdwhzHUUc8Ejsx27L85IIIgiF3V8UY71mQMg5HRIcMRwB%2BORkytEPVk1MMMYc23mMmbHmr1761ykboX%2FflLwNeEU2ViviWqkLAtjWBjp&X-Amz-Signature=46c0962158efe87b22de6b63c5b5bfc78f26038f27504586827b4616f4f08f8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



