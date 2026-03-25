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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WNERD63%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLNm8lYUEfnzsbGw%2F49AEfUSUHz2DeF%2BguTW%2FFOKKv%2FAiAmjxemndYapryuFkEI3tponei5bVZCnCjFn24AjDCDhiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjUzeCaa1RL%2Bv8b%2B0KtwDpMQOD58YlGihjSesMgy1alcA40Js%2B4zeirVm5JO0KvF7psFKQWfllkcq6W5lt9nVFvMupXzQz0F6Xbl8TxvfxV2HqhRfCLVrQhrDOz%2B08OddaSqKwToPWSmzhJuXLrhWwuuplnBRw1nyaNOsVb1u%2BVLtd%2FAfLn8j6ZIvfeHOC%2BLffbXIsj32qTdosB%2F%2FsqXTnE5WBGLiD8705%2Fvw4T3GTSDPKvOE3FjWj%2BFMGR2qHiiKgQu%2BvoH%2B9kSgEshi%2BvgyYqZ07KPg2pPKUgLOKDYTvaA27OVHB3DhL%2FvToXU92QuXhZdJQ8us%2BONDx%2FS8KIuGWGHNZX5YEWFhaGavVvdZ60OqyWKrlF8cyNuewAb4x4d2QiBjNb7t8C7IBxmnbBtaTNvLSnlzmGmdsdbZZZTGN3CGZoh8xqu%2Bl%2BzUy%2BXWBQw4AMy8NyeAgk4tuVwIkLm4VWBdL1a4XKM6B9Nptq%2F%2F13Ly7uX3Nx9SjtkpTR0yp21ZBwm1ga2ZhDTfaxtE0Z0PO65pm2ggJsIRgqqyFpxbdtLd0N09QtOkH8gB05lDm5BLkn4hfBoYGKwLFoVP8mA5hA1IutI2cH6TfhzbcW3MYKssJbahtFP7AeKzREWIcALHqCMrHxhxcelC670wsdaOzgY6pgGJ9Pzpcc8dMZk%2FQTZnRBa1BQwzWJm0ZZDTKNQySuk4d%2BGyUGkhCz%2BVn1bqy8qN9vPWJpKHGdx5Ptjgy7MpBphuogeDlzWmJCeakYOBG5vHSJIFMOWeS5ffwmyIChx%2BwxAmeYHe%2BjQirRkpq5KO6ZdCx0mfhXPLmpuJA6zDQG9Ip7vUNu65YPyf1socVHJ38LdaVGYzxmfteyvuXkc08yDtkMrRQxqk&X-Amz-Signature=100bb328fe26407cdbefeb19bf44eb9d2a7287dc4130c430348ed7ab44d7ee88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



