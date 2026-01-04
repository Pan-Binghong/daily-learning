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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFMLTXCY%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIGH5qTtsaP88HXMe7dhFcOF7Aq%2F9AFbRIqnb7JYJPqwQAiEA2vAwacNCT9mh6Ik788ILzbaSyEOg0Pru3tWAyRBRKNIq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDKkViAQOpLxIDJaltCrcAzjqCj3UTvUg4qUkt4byOrLXWzCosVbaeFmSttmFuZMVfTW2cA%2FBzOrarQXJgJgn1T2GVluwfZP0wkUqtUsqBzd%2BoLD4u5zahJj84moZOj0B18rpfZPQarmg8fEbNTTcI0g7EHf6kXWT0c%2BJ8A0xX0Hya3c%2Ba%2Bq9UuAH9V1OsgwfgUjPlkMIH9qBaSz%2Be9hZA5eHTmNHGzv3FZneEO56fQviM2cv2IcUlUkCqsT9LlWHyUf8Q8veCkzo4ECfCyR30NeVc0fubFHdiajQICQ4dZwAdhSbOv0MA7FfRReLUm85AnjZbvKXOEdTOLmhXMRQZOreusWR3ijAanHao6Q5TI8GwgBOfCverabtcdnwuazzP6pbxOPOn3nLwSnHfegGciVa1u7cmJPxtvk0R9P5rrnXLOPTZQsgP9set2XrGt1xo%2B%2FDlEBAAXx7MIdaJuFGo4AY985OD9pW2XMXkWW6O44fqLrVluZTaUYWNogikP4RRqQLiHBl7zUZcN7sAG8PRqyKmM8AcJQgSJWhIrOhZ1s8UuqHainAAyjLJsnfCtkUFt7MF8hJWW4syvMZn9vrIUZ73lwRQUump2xZ%2B30QEn38OPlp%2Bd4vxLij7PLYegeYm1I%2BfLgLxBRe7AgiMJaj5soGOqUBr0OaimBx849q4phGCClPcDj8P%2BSQK%2Bl02MZrlI8zZ1gfCu0fEMkS2tGfns4sy52TQIhePUNQyOUraA3zD7sb%2B%2BUXfqKabZxXPR9jj3GET2t5%2Bp98MEOfzcKbmuJntmQiJA%2FSMcE09ax1fEbSaL0lZXNVgbhRPLvu6lH7ygawefNYlx5rKpFp77ZU7eur55BLKR2518RZLS6lANf7UTVfSBUrfLc%2B&X-Amz-Signature=b9e6d69fae14e3c5bdaae65df9453194bb09294b87e6b4a401c573424abbbd4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



