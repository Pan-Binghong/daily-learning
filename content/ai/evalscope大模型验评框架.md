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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFXYVKYX%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIAuRTk%2FnOKONVgxTUbKK%2FJqRuxxqpfagpU8BHiNOrhQwAiAK5phsP5UgE2hP%2Fw3sp7IjCJGUMT0S2zXGGLALwZ4czCqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQZ4trKIwc8sujGq8KtwDzb8U7XuLXVTEOOrcFaEFO%2F2zzfI5PYDLoLiRK9SIqCyjrb97Uh0sW2d%2FpaZx44khWTEyBT93Xf9QRDsXIkbUKLZsXPgc5y%2Fe34N%2Fc1Msaqbl4TUXE4ddmyHYlnHOVV0ruqGKGvDWm7yveY5L9hXe2FF9G7V1eff74WWR%2BzvVFBhEeYdxn9bdBF75zXg3DRaiKcvDdCvx7JTeuhtj4TS0Uc99t61HkbluN2SHzp4aeyq6oFV%2BQ2wuNEqpTA7G8BTGsfVnP9yqfYiuDx%2FNVWjZrNIVWTMMSYuwaeI%2BoZhUFlLNQCOki3sp%2BxIRvv7kqkFnjz6k6Zy9hJwurZzE%2FZRkKEXjACkoSftP1ScTUUNUJX0LhHyblnTx0vA4yNwHhgETxPCuE4BP0%2BXmLKgMNWoQTAmduIodVdvP6n1BNkaFBTB2Ag8UcNu7BGrT6FuhSb1fmXAal6AxFNzlqe3HCOHFej%2FM%2B2kIUn%2FYF0v88I2aQFlD%2BJEtdarXDEIyPgMuCZb4PBvYi%2FCsWF6r46jhvGulVPNEXChDr0cSyQ44tVpyD7VmpSoEZMV7sXdJvbYlEOpfFtaXu22JajgdPWo206z%2BKxtC8VSNpVMWC5KYceZNhQNprGyt0%2FR6oz4n9J4wnri%2FyAY6pgG71WizFhNvWURPo7I6ZRcQ43%2FlGd8dlGd%2FynzSf2CNThUT5Ak9dd3oyUCMcQ8IjuGAYJzQ3zrX0rWpI62QD6%2FIrn2ViFXT1RX8OPuyyoZHXKF09crvVaqqgtuJqqmv8ZV75Fhe1xCxpcrPPBQwos6rXPge9JVI%2Fv5LWqOUKtag7fHX9u%2FzljN4wlUgxgM9o1uP4um4%2B6n7ESkpN1ddF0FQPr4sHP%2By&X-Amz-Signature=f27d700078dd6097ffbcc62011a58c9fd67f27896a940593f08af9be33dd794a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



