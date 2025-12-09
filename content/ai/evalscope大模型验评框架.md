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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FG5J3IQ%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMwq1xznrFNWOFu4%2BLmPz6aUxjUx%2FF%2BLt7U8R0w0rYaAIhAIypn7Ll9%2F6pgRpGz6pznbmzycQcVvOupa2rnniW5%2FSCKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igza0fTwtpbkGYI6mD8q3AM%2FMgNyPjfjrU14fVBencpKf%2FMyEQFwgL4qj8dXjn4BoLw6SEUiTwkNcPv0S5lnwtn9vwKhg2LQAa8r%2FlX4bCvCZ9W%2FlJkuufphXi6gFOkdvoPt5aVTH8jMkiDlHk0drXwv8EaM7BoKpwNOa0DYqBfq%2F0um3qIL%2BFXAPREyoz4YeCzjazOW28AAFAskfV5VPlBbnBAzUV9IA6YlCrYcyTIOi8OhM7eysxWSgvNSrR1q0h%2FPfGgxSx0o3sAplNwXug6nHCh3gRrn00U6m%2BHexF29AbIJ%2BN4UXbB%2BAkaD7EAC2zBdam1u2%2FIrSWKC%2B8kklFRkduz9v3YfrpUvYjilBUvu%2FGIlSM%2FzUDTRydSDUz7NvdUnByWRnKNj%2FglAcycPE5MfocfnT5JbnWdFmEm0KRnvAlJ0YPUbulMOce1RiUqyCs4kMqER62%2F6pSc0Ml7khISsLDjzmycvf7xmXYPn6gUKgtY2Q6ddYz70fF4LVlJlC9P09Xwz54iwajFuIA0at%2Fd6m4O8WPLNkDKa6R7r%2FgwmVvbK0U97Cjf%2B8%2F3Asbv3jhAoebG%2Fq%2B%2FQl4k1L%2BtqQMFVSbjGLQ96a13xPkEzYBLEPZoAy%2B2RT1kMaxLs%2BelEuoXjYuuXqa5hxZFSYjDUjt7JBjqkASW%2BKLGMZTn%2FjKrDeB63bSnlTVKp8ufxDUJAqQ%2BSGgEWBGZMy2p9m4MpyeWMYxr6mQTaLeX78zlrfsToRzev%2B0Hl7kOv0TURZyIMfIRjlpMgFDCN5ZW30KburKCv1ek%2BwM78Nf5XnidF8AVDj6sBBSgBDt8Qsuqe%2FovgRkmY18h3dVmmQB3MOjjyVtAxPFavZSuj76PPHkb0ekIAUBys4I4ZSJsZ&X-Amz-Signature=18f1669a6f9816ea94b299904e36f431229648865a0c0f45488f9628a61c7736&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



