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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TNM2WYZ%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEgnyRDPYg8dohzWvjvIAfQ4cesT0jDK30XB86NbfNUMAiEA%2BFQMmmjEoAxoSV%2BvXwRsbv7y0%2BnFUfW3%2FvFdlYUO%2BXAqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOT%2F5%2BXFmCm6vIb6%2ByrcA8mt6KLnJ3Wp1QETVY60zSniPYZKcAAZ40aZHlK4YZCCNphQJnHLwrQI3I65H2Ic6PNLKkqPT2wVzljZhH4KYlGsTa5fTZ5KbuViKDbRHDpxFWkKUVcmh%2FKKoARBF0vAmGfMMEXmV0s1wMzKWPHdqyvhV4B3aKYxLxARp9CkWwc%2FW2lKgrb%2BIG8S2uxIlKWY1SJfXlGasWmfJG0HIL9HLr3eEIiW55OOUyEs8I6GF3H4qHqIcllUBt19k4wK2Q2NZG4AlZ3%2FhvKgxC389opJFQxzTRkBrnKPIhs88WsSMHN70X0uyVYgSIpXHSy4g8o2Xq%2Bmt%2Fap%2Fb94N%2BmkqT%2FVisER55h1ZuF0fq%2BdVMtP33FyHqwHu3vuk9rWj5F%2F49UXdtrq6%2BVSIuWqW8Boy0if%2B%2FSb6ee7HJdobbgxpO7MmTy0AxpT5xVzyCVfhzp1%2BcM0PKgwd74po5HrtP3qROGKb9xlMJ5k52gBdCcRQthvx27DS844nijnjeSFbQfbIYilJACMOsTcHVmNT7mWrD5qVIlFhynRbpSJGpPsMCmlJJMqyAsvhEVaz40Hel%2F%2BqoYImCdFjc6KblwKwGNxs8UWrPvFp06i9AiDNebGfnESZFvocMEVbFsgIRlCVNn3MLq6hs8GOqUBbdo1umQseYM47OYcYdVKAeRIYosWV%2FjKr23Ayo3G4IuRVG7Q%2FHuCzRI6CBPhORiWyBGaA5PaywCnahVX8VZ%2BEeQZKE3LyyNapegRgOJC44Hlq2uXK4%2Bp31Egv%2F5jtiJ6Ao3%2Fn8p3ixRNWHGcr09qfctN8gkjWo%2Bg6vWizd4sKp%2FhXu5U%2Fe%2FpZ8HPFwpsRA8S%2BQadQ52BEGXLiE8Dt4HDRb%2FCdKXB&X-Amz-Signature=a0ce6edbbd1d1b87f10fec007b2230fd4f888dd18fa0fc6a771396cd08ef711d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



