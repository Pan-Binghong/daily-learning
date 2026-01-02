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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2TQMKQF%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDt5C4zQlDWWIwLQ%2B9DKyHSBOcSxOC26ATtUfeJfgVgrAIhAIbKMmvz78C4kVlnsieMYbPLBdn2lcMdWxWUe7XEbHY9KogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgylMtK87LGfT%2FEkyXkq3AOE2euypjqMty%2BbHa4%2B4Gikw7zEIcCMaRYWSCXlHwz2%2B7a%2B75iCvfwnKn0ZCGfx6syW%2FhPcu3kNPnSmdNczAmF3gE912cj5qqBF1MwRTv8qDDJxBMKUwtwYcLL7UkBlG6psoh95DAeFbhOTL9OsI%2FJGkdftixoywBwZ8s9EV8hagwjCZnP0JwmkjnEeBMy41SdJUYum1qfREOsJ1rskzstykky5O9nNNN5FDj5zwyyXa3WkZYBSY8fEfS8akbLdUIMYcVgzxlFlJSSGK7uiqMLFvJBiw59Ui1Ac5enn5IpycD7IwzaqD2py0g3mWk%2B%2Bq12Yml6jxFyqxnG1HF6FKJqZgSFk3P6vvxnKQYbuycNHA5ZcLR%2B1Y6MUCw1%2FeS%2BOsR0NUYQwramqXEKuTfg6nSCeGKxzz6mMDA2vIDF4BOl7zpBMuohAu4crhteqdqLMLyO0wgmKaLCLWNbqu2XNn%2BrqCLa6%2FaZV%2F36BxTjpuxlbT5JbcyogyLtxObSr5vlMpZY9Ya1n3Nzqk9CUXBtwbkXOgtPV8eKkKoDTDkTaD0uSuCzIsCeo5b5Xl1Rhxj03wtU8KTy2PqJEp1gGKxCUrugm6DiXJV%2BrIBVxbZ3YCOGiGie4us02Lp0jUEU8ojCyuNzKBjqkAYi9TtM2bJGizMrdHcssFA6vifhc0tfILsa5EtinF9gxjm7DOjOOL%2FhgajwXYDRi8qYKQndvRT3t6gYzXytuC4hIdfSZtBXNF35tICk6xeF83uFI6fhbGBu6FV7ns%2B4bkGy9DChdZF%2B4te7yaCquQmMDTw1H0UD5FIwD2fbaQAcULaoMZD4ujck%2B8%2B%2FtH%2BnUZ7RcIYxtkA7u0KXU3lTUnv5OTSfg&X-Amz-Signature=ecfa00a4c9bb217b6a711092dafaa2b6e534e01617bf204cd79a5c546e4d9bd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



