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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TNHYIFY%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCnB%2BBuqiTCJprb7wWNZ3oQJGc1h8%2FGzcnFn3qiRJssqgIhAL%2BYSeeHDiuE1u491dK1MYf2%2BUcl1xSSrNq1Gjec8vP2KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3S1qUFon8qYL9wyIq3AP%2F%2Fs1n0tMKX4BWqS4Z%2FVgt05sIXnMzzE8hJBZbekmHiuZR%2Ft5N62D9VDvCkzw6Ua2dqSUzAbuJEO91WYXsO5zIJRU64ZdRne9HX5JxpKRzSHLTxdbrEHZv%2F5ZRbClabC1WcJdeodfU4KoohDZ54IMhTZ6BIrW2VgoN%2F6XpU%2BZmWTwxiR36SBR3PhvpxfG19KKvjrGMjyEpixoFEndVMnuyMOMDg3hbgNgKdAcpjvvng3%2BRrI9LTBc%2Fk%2BUrGV36cJ7j0QGrYEsxxe5JH8CL%2F8Igw5Fm4%2FewmA7Peq7taISg%2BbEzJf1XpPz87U1uht2J3lHlK%2FbSkoRQN3JxvxWnoUcH70Ug4i4VpcSzVrf6Hdp2sBCa85Ag8lvbDpcGhQx3m0qKuS1%2BTvMFb4F0cWbK322zW7PWKJYwvD%2FQFltng9FeJPC6Bo%2BV6ZcgbksZcp9yqVxZ5LG4hLBHqYitDc%2BPQdwt0ziDLGPxThVxpqFQfnDIO2M%2B9OBUDVSNVMVqLQkYZe4Ypx8D6KsBDvl84lrz0U7EPuo2Id1546cz50aMyQ7EsGtHybJqOe9Hgcq20zaBRIv6dPjVfe4f3bLgHdbIun0XhDO1DgxAYXrXMRv7jgapMCFUkklWg6T0Mcu%2BqzC4tpjNBjqkAbT7Ip9X3xIKUbLhvgN5r7OOz7rFg2xBTX6eVjTaLy8mMoOCkUUk%2BtkyKNaVB9m8zfGumvoFJf3oP1YTYpnJluKDuSPiMIGkM%2BgToLVJOH%2FdBd5A0bbYhQbDGjC37DXoboEgH2ENwFXO0Q8LiHf4sn8SogQIIrdGKIfLW%2BrCcD3odnf4IaB9Nl0GyOBeLyW5Nw6YLm23rbcETXIDclGSdF5HOcwO&X-Amz-Signature=30d8f76113e02283ab05b4d9806af953fbb3fc5a0d6bb3519a3240a173dcf8f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



