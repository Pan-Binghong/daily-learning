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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDP6V5MY%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIBV58EfhEVcKisyNL1z7xC2xupQJsIy5DcFFABHLEsk%2BAiB6IwpnFZDqqpVUwJ3CrhwPSMLfp83m%2BmOm4o7Wcgeo8iqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZhGgXhTSmPtiUvqlKtwDhfsZGqkB2em5g4R36igU69znysr%2FQBBx8E3nbdTvh%2BjRbS2onuksWrthHWkMHw2sNmMwzi%2FcIBloEZskCbTzj1G05KfuuTYp%2FiTYj%2FwdAO%2BQ80h6zPe1rq54lZ23gLL9ZNnbxm4oFIWLHFbP8tCvfeVbxY9zAGnv26qskgj1bDmc5wseSRp3rViaO%2Fahl%2BQrsVmdU35eIRQplto1DE9sEx%2FarYBwRSYY%2FgbVS9UXmkkyGEUlA0mucOYZM7Hw7YJDFBDdkXF4JbUfHpnZAGbQu4bix9crXY7cf1PhxNBz2KuChGMuIJYX8Ur%2FqYVSEgF%2BkNaa0EzizIL8snG1YyxiCniuXNWxKntN9A1vMWcuR3YezdqHYqF0C%2F5SnsdvpCjM%2BxSrXn6QUAJjM1d4jz6BnJPz3%2FCfAXY9%2Ffvw2cPg2lRQJ3aHZk8BO821ttUcEQcX4uJMgq1PtrFlLd%2F6vs0egppST0r4Ieh1P8iksV%2BY%2Bp8RPhsr1s16T48lKUjIMBcaSmu0cQdM6L9PUlZoPwwi3HUa4F0OrFy2wNa19io0jc2xnqGGf2S2CX0Fga3ophkzg9v7SEIg2Kuo8vn0al9UEkBtXsADMYBlSjNxaldVlT52FLKbOPSQgdTCGUcwkqyLzwY6pgG%2BMbs5AhZ3KP4de1kakhHjcZ2LngDayTl9RmTx6hCVBiT0hgARBP4X0NCi77bUzxlgeMymjUxBFov37zWsF3VZDgcFd6andSaIfI2eYhrVgIegAsJgwBtczZo7eEo%2FHtCnjq7mI%2FSD43O32CygjqrIEq6oDTRdpDFKdCwgSLTLKbEVPNIO5AUv503Hp2xtp%2BLl6ZqdYc5AY609BE4ocoRgnnJ0AEz6&X-Amz-Signature=9a62f8c756f86b4170fa47c5d6e3e60b8b99f1e0d66b6151b8a00e8131f7aa65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



