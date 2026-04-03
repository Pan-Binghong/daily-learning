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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647JYZIXL%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDkrCyAcTS%2FwyHqfCb25KVaJQKqzWNFtutOAlikWqVokgIhAInNmCBXApv3oWS1pbMkytgFv2fVx2RUBvMdjFQbx0dXKv8DCH8QABoMNjM3NDIzMTgzODA1IgxgiR2ZCBHlZPzW9FIq3AMfNLYsnUMEzSn7HBLG52xzvcmUCqIzyobr78%2BOHH0wH2DYPPAUuNv9lBUU%2Bkqam89DvcrIKb7bPQHUz%2BtS%2FIdpEHXaSZJY3NXISLmsb38WBwsqDIbqAjOkEkTUvzHjwNoXSIGfFcmluFRTVwVMr4ck2lA19xsgslrv8VHAdgHlTDUpmyfgFCvgBOK9cFjo%2FLOboyMk5DWusKQjCSxe%2FGqHc3Z07hAiS%2Feh33QvwLgt%2FkV9eJ3xlnqHThkpB%2FJNsXjIRU6J%2F%2BaRSDLttBikcjFKdGyV4EjOGPH0NPLilfQPIyEULf%2BhpXzcETT%2B5tU%2FNgFjVNBS%2BYqk2ykPh4URILO%2FIXZ3NyczoZlQt1Nd8uN3BfKkTWDB6bNBbSxKCgaWCLLmPOtI%2BXFIAfJe%2Fypq2dw2YgccxDIJwxVVbo90VG3vq%2BjLjn1xxp7wTHTLsmhlEfLsMx%2FQA%2FH1AxYtjiFUj%2Fe%2BNgNduRyhM0PZe7QZEM9Hod4fJ%2BJVzJJ17S%2FLtkZs4YnkG432mK8uD0rD7i2bfRyYrURIZfxCTrd1k8CGF1DemNzwDX5EyeiERn9q43MwDi7Xxrv9IqDxm6CW4xPIMezQCzpUZDxtu%2FnQc7JTxceECi8TaivhvfHHTB9ERzCsrL3OBjqkAfofhKhK3q%2BJL2tn5%2FdszLy2QymR31sBVFZAsSZ%2BDL0tAHzjdAY3HU%2FTo7LraAkRxqMkAiu3BTwxguBrV0gv0w%2FVW7S7B2Q7iUzhcBj81%2FFy%2BDPqbS%2FMnY6uhiF7Uodwd4Y6UUxC670SRR6nBk77T7QHfeXXNgRnYEYUFNdfStStC1IsZcM3O%2BFvsL135%2FfrXxFhe2xWkvY2w%2Bclnc2MrS7d6BaR&X-Amz-Signature=773d436be3ccf2c553061fe35b46fb925e00f27940b4c47faff7dbb4860535a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



