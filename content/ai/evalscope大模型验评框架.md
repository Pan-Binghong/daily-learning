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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627K4MSRH%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmR7FTymTV24XNHred%2FJkE1f%2BJKVZTUc2yxXI0qcE6vgIgemtA0Sa6icVq%2Ff%2FUCqPKY8ntlLS3D%2BuZWbE71IHMItEqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLiqPvnMUu2Dq61LBCrcA8Bgopp6aXQGvBfLGdh%2FHpBkoBBVQBdxUD7RoN5p6KkDIPDGI7w3a4eJ57jtcsc%2FDhJ2x%2FBurNv8xhqM5FuqkC0Izr%2FYHOc7TmlmJ012RLUe5O5r4MqJz3%2FlEZ0bUXsD5byeDXNfb9pIdGEirs19aabH3DcmI%2B2QizGOcwEb8tPrRsAo0DYq52W%2FUPnu15A8CY9NCoFy0cDbbBWMnYVymeVwn8imUW7SiaM15%2BPS5Swd8OfjUHO5JRCOi7jnZP6rr7PmlsSltX2josq%2FVkFy6jxk7a0h%2FdStaOui3o1%2FfjP4nnIyCvYyGS3Vu%2F1bI5pqP3xUiWF7Z3Ix7rjxjB8p3vfBK9KQkRy8NvyWLZTfv5FQUa9Tta1A5asAwCYuhDFMA3zASkaNhRlS%2FeQ7m8H79sMlTdmIDC4BepbOyqeAYU04IW0Om71NzMr75rVpnZIlRReWli9832PlM%2BsOC1gttjbk72Mp4gYcUNXe6MWtiyLIfnmoyZ6kDcL6niibii3wyeZ6evBNigPgi1L6QjSVxymUDXoIX92keatz3wt7nf173fSjky%2BNjYutbesvS27upi5PDwdmSaPwW%2Bwo8tiSXZnqQZK%2FyBs441EU4jmhRszVZ1%2B9VNtzlthLETC9MJTe9s4GOqUB%2FO0bAb5iX%2BwZRAVMQpMC8qJZEPS%2FidLLIXgBRFh1YDVwmJ8%2FPDKDuAMqVaEYEc5hC6zKUEDBFBUjCLV1YVwqiHOcuaUIsyWutLKcq5BYr1nLO064CS5Hz9HU0vtWCFZ3HhSTRZZtAY2aYlfD1Q%2BLFIEXyJVn%2Fa14qJeIm2v3TkFJ5oInK67MfcMmwo%2BnsjN7qe5XJT%2FGZq%2FnivdjCY3V%2FNvDncX%2F&X-Amz-Signature=14c19705609c031640eb2ed53c29d157013066353f086c59b73d4fb014fe7d22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



