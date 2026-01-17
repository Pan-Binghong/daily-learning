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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RODFHQXZ%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEbyV4LdfX%2FdNsQcOwX1Ru146H6lSM%2B4FYCtd0q1o%2Ft8AiEA7vsP1jyu%2B4lB5chqdhwAtbihVEqc2speXUm47OWtL9Yq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDL62xl3AP%2F1QZ7GmgCrcA7JqiBAoIWSjQdmlSoOqUv2pTqYA9PueAUJfr%2Btbx0gZvO6tQMJIv06LcykoeMwtDyyjUI05PL345pz%2F8Zdqy2KY6teL%2BJG3oQuVYCvlv4vYmK1iKzA3Fvg5P17C3X7N2wMo2ie9GWMmkZgaxqJ8U4LTuXzC5S%2FD5Dk8KrNPU%2FAZLpqJypzdwjImQ15EtPw0i%2BjyOc%2BFcdYlTmJLMU82SZmA9CZI79ivp8Ng%2Bqf9oZMLePhe5MMFiPaEptj3VZ3jHJpTvO7cWbl9SwiKGGCjdGgh85sYQYwEWdWXsGOkK1eHtxYCa9yyqBj18WUDSsag1V9ny9OoiHDm4zTSqIww95%2FLkEQGhiDYYY6NGtTw3a9bAgUpFPoWbDbt%2F2isUUWn5HkJqJwGadky0v05KMAaXVgHLaAewml0sqWS93D%2FBOaAXwYU5rM%2F9FZtC3Q5ZbdiAiMoOYRH2wL%2F7DrEBoml5yCzkOYD6PquFU9WCR2yL0zjVHe5FExlREi1%2Fj6xnPQ%2F8YOja6Pk0ASVDuS8Or31CrZrZpimTOLD6xy9UV%2BQp3ATqj5vqY9i9V0ocjyDgkZK%2FwnPO6n68TknNgBEcE4RpnntUTLb1QUhV4wP6ieE6b9t2Rr2iNrZKe%2FjgurtMJLSq8sGOqUBg8Z2wJvyfX%2FFC7ojywwo8%2FmmXFimFM9mznK5qEtm0EREe2CtDQxvXvqzJbS9G5BTkCozbiwLnjblFjDHhh5WGrLyVn6DW5ExQ5PaxZGHuvadCEKFcgU232NZHLvGrRD9fRniCygVyAWIzuDUCybWkb9hAwcZ9ddWd64KJeQZaNUFtfzD3yp2o5GYYDFLyT8R1x1Ty0Z20EcXK7dMVR7s47QTRZzm&X-Amz-Signature=67b327a4ee2b680e7ae715e55a3f6a43530b57126da9449f19b3e83d7580823f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



