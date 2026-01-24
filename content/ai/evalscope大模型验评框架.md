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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZZLJD5X%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDAmr5m37ZV9RuvGK6%2FwBA%2Fih1bdyK1sNAhU0%2F8aY29VgIhAKN39mp4QUfWhI%2BTUoBy2UdoKbdSysX8ZihiqD4iXhrmKv8DCAMQABoMNjM3NDIzMTgzODA1IgzV9e07gT80JM0m%2Bfgq3AOxUxDsl8lXD2sAFM03wu17tx2xGgsWscYh%2B4gN5S%2BG%2Bp7ekwH8y4VElSzf5w2i74mbDP9qiVHZdW23988dsLv7T1UwAiPknMzeIgiv%2BCe90sYlDkaQWe8N5PnaK1BUPux41rw7uqOUNNr91r%2BZqRgyU%2BIMbj6%2BTpYLVS2j4n3d0amzdUl9cQXq9oljpVhoX2gwlqMpO8VxtCaEzRyAb7pHVXet%2Bz0srdzuTMHDW8CIsLd1y3SKkFbrg28PqXhNVOURSmXJI432P6hlj%2FMGWj6buQizMRMOthJCzoOlBSqH84b6JPJDLmsAFpzMrjxwDqhONLwYM7C%2By8guqfGrWiO1w%2FFOEXJ7ilEAIIkPP%2BDpxTo2wcFrSEIAfWSwskif9lrxbz7J6sbIDeBBCtWrz8akPjg522aV0ilv%2BhVAUJgyWA1t1njc%2Fk2HIthssmtFu8TrC2uwJ2bfDpWbaUZj72tUwbWRMB3x5EaLDO98ClPZRPbVAWgow7sj%2B7uSAvbeNsGLz4Wt4F8jm9EWGJ97NKspMzBgsczbL9hjt8iicLVi6R16Z%2FdtSPmK10cksa4feJlq56uUrKyrjAXOrEbL8AZM3XkDBNgmqRlGgdVT59%2B381mUqW4FHPN2M8TprzCuztDLBjqkAVkFdN%2FHSVJg05d30miwzJRvYqxSOwobCCUs6JFsxzRYUXIDWd6eZzdoDaKsNoFC9qcQy9%2B7Q6WYlieQKzQ%2B%2F7ljUpxp%2BW%2Fdl7pIAjlRFiiK%2FiXPFZU5yb99oSuhBnlIJMHjMhNJj1kmTL%2Bp%2BrzHNGyeaNO33lx%2FKdRI%2Facl3F21hqKqxhjzQUYhHL7h7qsV4m1csQ9bZft21Ajn6uAkwqeFXllS&X-Amz-Signature=4265483549bcf731934816e2a9907007d97168fc70725b4c17f762c2bcaa24c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



