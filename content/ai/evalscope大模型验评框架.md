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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ734SAR%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDdhqGTQctJ%2Fg2WY4YvpzhmSklsInfw%2Fnje3b%2FiZuA0hAiEA5E1yiLTwweHXmGlvW%2ByXEaKdjVhwmjWUefb33dyVME0qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN3rQ7lwjL7a6snZJircAyKKa3otJFOvYhWYt9TxYtldE2COzNIZWvaUJ0zzujq1XnSkSmcJ1e3ic8NR5bVwGNqnfHw3nedxKqY5ZnvFnib%2B7jgtoBHVNGmjgnI5rs8e7UENWHbQP9MSOzD2KvUEB9rT7fhNc5y2lpGQ5GwNw%2B7fxhfp5DFyau1UbF4o0z21a7D2CP%2FB8jvKMBWH09gj6o%2B6ZwvWCglm%2BTgh98AKRy4Y6mih8ZqXtsE621IR335%2F5%2F9sHSg7%2F%2BvJDhTriC7VYrvgJv67zKIASPTbt2Zd6pD%2BOk9%2BLL10e5NV8lYKPrsWJSYcB1%2BHcAfDNaopBbsqBmi1bXZj%2FMLhsN5HMUroULeyW904ANcDdNPMon8pDWufktVqvXSzUxnfLIucr7ADFd1KK0yOfzVxt59TDhbl2nW%2Bqrh4%2BqI3q04v5HioeIb75VaQRQKu42S6AjToe5S6bUcda1ZQg5vU6q9SPI5DIug0PxrJ%2BAn06Vu9%2FjPbW1Q3MumG%2BU5cTFHK5jmuyB5soXqUXS3IH5WehzlD1gQG4Uy2CZOaT7SV27g%2FsgkAWfKrFbMXsMaoWVbfHi65rryWi2v6%2BxQNJkjDTYtMJ7pvRPZYn9muoD%2FNf70i2Pvq4Vp8WlywhtR877WiTjWsMJeY78gGOqUBiF%2Fwf5b2tnuy6%2B9CvjYBjskWrq0Ye0%2B7CU%2B5MtfgvVC6gmkQ2CzNkkDcMNEyFk8i8uS5cVbc2baQ4wwpTnYRYUY5ZIUqCbhb1BKCTajgRGxN6AvnLoORlUrC%2B3XseNdupjf7z1YhSzYCFt48SZxi5fbWVU8d0cD%2Bbo0r8C6oK1wDTRX22KbDaESQ0WCY64c4CL7QQwdhfPWZzrdfBKc2e1c839yt&X-Amz-Signature=30d4ebd90bef93bde68964b43f93eb805f9afe8c5d25daffcfe423aa863a80a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



