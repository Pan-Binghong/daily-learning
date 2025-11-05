---
title: EvalScope大模型验评框架
date: '2025-03-28T01:13:00.000Z'
lastmod: '2025-04-21T02:58:00.000Z'
draft: false
标签:
- LLMs
- Eval
categories:
- AI
---

> 💡 之前都是使用vllm或者sglang官方提供的benchmark脚本，现在尝试更换为EvalScope框架。记录使用该框架对速度进行基准测试全流程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QL75ZWB%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSr9ib05aJQzJsKhPRY2UZsPPshRL%2FSenukgPzv3wnwAIhANITaqNhC66gXGTDVHOgr6FBa5%2FZa2voei3F4oVpeMwVKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxla8hHqUKGY6f6ccoq3APRN8PmZ2W6HejOLYDGOBiE0mS7bSw9fFqjV4X9TKtABHxpU4L%2B5XSPF7DELeiIVb995rhkcDYfe0%2F0XLZ3QMb8cdIXlkej1OvqqArM8vtho2KT6EAIrzCkwHi1tE0jIAMkHfecX7n%2F7ftVunUAxqo1%2Belarc%2B5TqcF7Vzs9Z%2Bm3oNJfmftD%2F5ncdn6KQHyd47ASyJ%2Fn68Zg1NZUVjuY5S1uzSyxwLVi%2FlR4Bshod0svT9YHtOkjRq6iOsbeKP5oCiNnKLwBfjjRe3rsl1th2ZquMtUyU9oUeTXoLo8MA4Ui02jXSpUKkkxmmSW4RTUuYnURR473Bg%2FPiNMvIQPiGB09tf6V%2FbJ1Dkown1BnPnipmXCDANbsV15gdb9I6WkBBQV9Jpq34NOTSnslKfCWaCsIS5EWM7RVciXQjzmTaGFnLsBo%2FPDJ8bsPlLii%2FlMSm5KWwMd87LC591GjTcjRbSLWyKFN9ng5TWdmsEh96kAHHd9h49LhkfC9aVw7F8TjLTiNbN4UuZWjsbAXIXl4A3pvcRueU4aKNyrfBfletBa4CVst%2FAj%2FbmrV7xZnh%2Bg9DS7846mhCTjXwwTZLufa5gTsHHq%2BcTba1558A4Dlc3aIU%2F09fkhyWlINCGegTDCn6zIBjqkAUvB9iss5QY9kljxT0Y5bB8egs4VfwOobyIedQsdGqY%2FftixkwQMU2ba9huhap88j7j1DzXKXOvw80lg1fQIRY5c15iR%2B7HHWj89n48%2FFDiz0gTrWGd%2FM3Icv1byJo51jDMwJoACSVXCJR0usIx7a6n7HUqsOGh4i3t1VUCr4TcCQM72PtGj1PxfhqbnLXawJZxqANNaGCqMTaEdmqxHFW2qjl4U&X-Amz-Signature=f05ac68f7fd5d7fa54892ba561630660b576a5d4272b5a1645164e84a8e218d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



