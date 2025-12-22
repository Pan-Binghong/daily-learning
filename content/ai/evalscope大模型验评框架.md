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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF2URKVG%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIAefyYuEi%2Beb1WsDNuh5Yd8oLz35fsKpIxk5g6SGuA3xAiEAkHbm9zeXr%2FnBYvqEUKuzM3j1T5DgOTJRtlSJFLWsErgqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHqv%2Bq%2F%2Fd%2F3G9pq1byrcA8%2FpIXvd1J0%2F9jc5TuLVNCKq%2F2L%2BzLVzUDbjGfFVD61FXXUMqtPhhdNmRq%2BgxS7wITd8ifzRJEACvu9F%2BmbBqrmgxFJmm2sQyJjXpnVaL7NfEKMG5VivN1iPoBzcJ4QoevAXPzO%2FBtjGlpADfsqm7Xn9qekUkydFpgwyp2EjsraPjaDXjBqcvQuCUhwnddKig6reE2QoJUlNiuxIcNFfYZLOEREqEVjzpr%2FPryltltsmHPBtz21zZDkTpNUOiJY6XIIRu8cpz06ucMy0jrFZK5glZuPhmx3gak%2FiSy3iBwQ9DVemsHTrt97FC%2BRomWEimMX%2F%2FS%2BZOW4f0C7FZrFZbptX11X%2FcBywsBcn4forMjhDjkwMQczu6W%2FyapkRbkm54EblHQ3AxMndLASZwaJ7q6Xn2nUlHcEK%2FKvSTVbXD8i2ymKGgRdmLCRcDoPjizul4wGX%2Fhh%2F8Qc%2BsYNWXqYQkJYm3jLz10DV79KVZd81Hr1%2FJ%2FVHDY%2Bl83esFK7gtObByAt%2FgzttCfgCIoNYkjdcL3C3lfriEhHsvT%2F7LnO5BKGVbhDRX6DIPh%2FJdyojmLVA3kTfS1b%2FFA827PSKxIwrvouAE2FvE2gUpGJ5GrfGGsb2TouLiWgARF26r1FvMIXlosoGOqUBzOKT22TfwJPArqcmDmnrz43R5hO3k2Y2aOCnhWe2YlrAMmpg0m3PGoIQA8rIVOpmZ9nNwgeTYkn6OM%2BvSEk5p%2BOUZXVi%2FEP1jZ%2BiG8jKscoPO9J4NzHV9s6XzU%2B%2Bqjm2ZR3ThGXofQ0U%2FI7D%2FL7DtUFfolQM2shcuwe7UtemOGb5wXyoFdKd6ed7P%2F5IXYc1O921Loysli3XsxLJ5OTCl9gSGJVX&X-Amz-Signature=f1c44965911efaa5f3d9c144c3ab223a2c212965446ac2330cf1d7b6fefe468d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



