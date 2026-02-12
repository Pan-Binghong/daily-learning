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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3L4HMKX%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIBdeVczrNhz65JCqt4CxGleYQQ77akDdTMmtZW4ubM6%2FAiBSKMAQnRu6xaUdwdaLrTDRBT1hyXegKXuK8mQSxAlaMyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpFgWIO4wNvwcNqqlKtwDoHxzCvIjUJqNaWIG6mEZCZs2%2B1yIxzFZVVefgI4GELgZhR7lEpsxQKIx3pN%2BMhT6pCe09NlZuC1vqLQXwd2vFi1TUaHSMbBd2xswFQjV4B1TJNS2OMXP9BvsHWGoymBOZyx4BSdj1ZnYnDQQ1ISo%2FUMkcYh7T5juD3g2JbPBpC54wBNSoKFm4PYgLcOVw0i9VD89pPABJApiiVRbPDtEyvvvAPRe31hDOeypfiyF6Iffd%2BjDsYVP6IisymY0dNhMQwuAZmIagVx%2F4ZTngdaVlddYW5QdljDiU%2BTFW%2Fx8LA9zVXaEKA9uwOPhd6wu2aQUzwPNjuUiOMJPmSC2F3cwoSsdmkb5kAM3W347d%2B7kTiAFqsn%2FM61NsVzpiyTqK7d5M1NU7DQfTCEXg0hQyZudHsB2sHdQjc924%2BvrL5aFG9xUBYTi5KUC8UB6jZi2xIiR7b4ba7hR5FSZYQeKKoj%2B%2BeZTd5cNeCUmLPMDvEikMjvPvTox24gpUPUbdp7%2FiZxTpKEzLMco9JdUk8Y8GNt4hf8yqnZfT9KMmEZphBLE0TOIJRBi6ixfuKvmzX7m7wlf3u4qTtQGeQ%2BfxDIYrQzi2kc%2BD6cc4H%2Fk%2BInzItbWLO40c3uVkrdrqMObT0Iw5pG1zAY6pgHVWwAp2lX0Ad3FjedgM%2B5fQ2LQXRV8%2B4GjplS4nGuCXAAusNeZiaXBBp4QNjS4q0yCAPNQmijFRtW5nYcuNQXilTx2gNo8yxVuHLa9TIYEsE%2BLzr3XY0DLPS4cncER32m%2F3Cl6TjxB9h4%2Flog6QYd3losm8biairRWsAdfrgIqmLYuFW7SdPMk5dSTgDWyxbSLhUEcC%2FY%2F9INBq%2FKun4t299LR7wui&X-Amz-Signature=f5cce234bf5ef9467c80cc48068c55d0638875495e2ccd43de05e2a3545d6170&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



