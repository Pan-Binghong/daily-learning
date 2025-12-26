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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKLIY6J4%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP44kE%2Bw6jYi9J2OmvMu%2FgbgfOqD83J8k%2Fx3aa72bTXAiBgi%2Fg7PUW99rUUZe1r1AMvzzRFE%2BABy10Eake2Dx4wPSr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMdKPlNtySOBdMNO2FKtwD3WiWxCrjpVbAkzPrIas%2FVuo1tVjVlIgLZaM019CQY%2FgSIF7sUdI97%2BlRKFgc2P%2B635B%2B0Jzcc0bEiaVZDQUaE5OE1qLiWTKqtMYOc%2F4SSqU8LsIovVjNWmC%2FMlqa%2FIM26HnlzpNoQLmixCmzi%2BwVHvPZgdc8mcbitl6nHxfh2kIC7WjO22KSl5hsCo%2BfnV0Ed15uqdZN1of9fzT9N54mM%2Bp6wO4%2FhSn175CPjdmMuRBuDO4TUAFJHBBheg21%2BwGPjsAOPrulOHwka4ogT%2FBnXZFV42q%2B0YlaI6k6M2RV8I7U2fV9DbqYOsCR4UzCmidLQoR2KMp1NGZ%2BpGhwnO%2FQ6Xqy1%2B0HLOl7%2FVXMyt3ro5Omj%2Bh9T39A%2F9rE4S17ZRsR8DgkJ9F%2Fw%2FA3Hv0EH%2BQ2xDf21PspVq%2BpEHfeLvF%2BLSjSyvyJi0Dc0ZH3ZZtAauvTsw6Y4y6yOUfS5MkAs4g3mE6CzK7gO8OdLYq7pjqlIGhWb6Bf07NIpd%2FOLGN4P8KcKtdjlmlb7b%2BuZePujjEuXIzzcpKb3yZYNVuP0ZupyNJA3kGFVCPhoyyMQKF4r17d2Q3EEJOwK8PdnX8dyjq46nCn9IODxyrNQpg14hik7aCiUGLvz3nShDA82yQwytK3ygY6pgFoLcco7I3AvDlJ6n4v%2BCdV7jK9GxmaGIMKhBL9AFY1JNQ1YLfUqLw87HqbSJLcUyMPfCYHteR7JtkKx1Qd4OZZ0625kdODX4HAtCNt4cQ6w%2BZUMu2GBxWI3t65qFUkurdICcRL3JNIWk1TPj%2B8QtEcHYcM7ilaeiaz0CInS3%2Fo4Wtpk1YwzL7UGua%2BHOKIRu%2BRNDgwvTyrQG70LW9NVRmFGsYtEOc7&X-Amz-Signature=84f79b365516edd49f24d59e621145a27d8e142651b6a5e68b773f9eebc083af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



