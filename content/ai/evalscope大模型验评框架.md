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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A7DTPOX%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIG2cSNVy0gdEpNblTkbeBEyXnxB%2BaLbWK9Via%2BYr8DJaAiA2tP%2BcrcX7u7ryoh177H5mBpes8FPmd2NQBn%2FaPJMqfCqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BunsL7J2rWC2AWO%2BKtwDGy8gWL1zMH6RZh8pwNn%2BwGds7HEUDdNQc9e94Mhofr7phIoKHD1whjbC7XAjDiw%2BsciY8UST%2BXLrYHDUtd2GpgOtyhjMc3RJLjTfbk%2BtUgzmI6YRK6ZGhq5Qdw3VBYItXx3%2BgWrUOU5%2FyUlqexEinNLl7rXmruh3NxOkAFkaX9yYM0EZ1R1WWbkSww9JS0KG84kp4pDZiTJpQT55SN%2B9obWY1UsRA%2FX4ZvT8z61t8eKPXmitPLj5RFXKCLuWLaZY5IRo7j6z3np9vrqvpKNhAU3Qh4kFmbGXNvx4LQtTzuMVeFguy6we7vS1lCOv%2FIGnBBO5wH%2FRtiAYjh6vDhHNCy1xpDRmchb2%2FqRanrh5gOH3peBabB11KS4RqDGdcOYULJty%2FGR%2B0Cg%2B9JObu19sqU4i7emGjjPbIA6oOmZVtjW1urZ2IiwDNBPNEMPUj4DBGN0JZvsj9wUXaKn2uComq4UhJ7fmM3E4JlbVkw8I%2B3E86AhQns4l39CRDJG%2BNMBkv8kSQMIuh43NGoZE%2BMU2IIAqRQsY3aRgmNR1G%2Fx7zZm9fvMS0aSW%2BTiLot61MUWze1pn8ADjd36VT5fJTnaS3J5WRdMg%2BYgT0hRXjZqrHN5NPdNKfSz27chT8i4w0dXtyQY6pgE0Y5OF0g3RcyJJ3N5go8tQHa0g95g4yBIKA1ZdTV8StqS6uIB369bNUdejg93daz%2BqcGnCgpaa0w%2FwWnVrsfz%2FxW6p5VWJ3T8meNQO6vDkMV4AoEweAyxvVw%2B62GpTjnY08ZZN1J8xQetZmkx8w6X3l2hWLfHKRCgUxqIBe%2BzZQnWFnu3COICw06IDtM0ySPTxCO9GDsU5%2Fu9P5c2Cu954kl%2Ft84So&X-Amz-Signature=c363d749cdc0e52019b0baba61c80c236fd69735e0363fa1e24a97c56250678c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



