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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFHUAGQX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEWhQYW3UP2rLRBoyiJxSAtJ7S8YEvLdGjs4iDAvxw%2B7AiEAyEK5NwkiibFjWwsbC12Kc38YkFdUl%2FLe2PkHXCwI3o4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJfM4XRetexKiOF%2FqircA44aBFXc%2BnMIhVJxgPZ7wvW4H9gBDyfFo4YMR3VKNDkQl%2BsvsxIEd8ajYliu3WrHzilZKPE9IKBataWwPwl5qatdydw6sVyJIk6NY6bnNkaG77%2BKkmYyZextOrOULNfgqg%2FYOECg92h0jFPRY1cGc2MJYTiLVzQc9I%2FUmDajxBuqZMerinTflIcIlSnBu5i4b5ooI4EvqV9CR6PDOTJkgMP1JDRvvJRTbsNO%2BGgw548AoUaC%2FrDGmLysqTB6bOSGOA08U1G3iQp%2FHRAUJIm19ZIgc7NBeIHd0vXola9I0oHrlWGpQpJkIf8X80LaauX%2Fafnumkq9JYJjtQ%2B%2FdmsGJx%2F3SOiioLXxi%2Bl9H77GxR8EwgDxMFDX2gbcS%2B9%2BF2qzB53sBwx2ra%2B8TZfwj%2FTEUTItauVP7Dcd89iq3DWa9MnRyKC0ZXCRpeMn1d%2BL6cLFrqqK5ok4nmKHqOwlslN%2FhX%2BzYnymYxLrB00lt1exPlKRPoDaduMVHJg7Axu8UFQVqqZJ0NM01JV9vAIyfd3T%2B3rnGYNUIAM81nJh1ZN%2BojmLnypuvo2l%2Fd4UfH9jsYc5JR%2BwbZUaDjBBooMOe%2FjSQFWhzJSZse%2Bi%2B0RPjt%2BUbAz%2Bgi7a8EoOUM9rk76AMLbhksoGOqUBsh%2FH2loeuwc6I8xk7BF5b14HMmF0ZDLy7I06U%2FiURQyRftha12Z3TrjuJnHNUG2Y%2F%2FZilrXxG1U5LCy1x7sFAEt0tAjZErFSLVv2YgPhhJ3eLZ7TA2NdQfqEjdEkMgZBy0eq60AZhzVjDCssvT4gMkkzTHiQann8KdmzfQK%2Fszto7IVPLNwpGGWcBaTZlk3WNaRmoewtxG2hyg%2FOkgoHsX3nlDZo&X-Amz-Signature=d1ce86babd8d268df56b148919f964afdac4c9a1ed627ec823150fcb1780bd3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



