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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWDIV2YM%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDNJTXWP3%2FQzRqcc9VJnpOhnJGcV9W6yk%2FuslqW%2FFotHAiEAsJxhk437gtyd1DuJ9%2Fq2PCWjr6lckb9CtjU63ctqvkQqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMyecDvXnDTErkiP6CrcA8HRJ6obKMDMOACOFXPROUVroWtAbMg2TNZwX5uGFvY3p76%2FIVjcpdLTWxM63l929cyV2eiaMV9%2FivlRXEPawBuo6xZDAISsWfCHY2OcBSyOsLaVCdMFgo%2FuZd3q4gSugPaJ1LEhNY578mbE%2FSuxBTyOJe7qdMiiu1fC1zAxp5owsrA%2F0nP3XgVuQQeeAjsrC2gXLZsqqhuFIuzn4SPQpnxzqWtc0BK%2BMsxwyJnl15jNscXSe6m8nFfnlXGJ5BO5oTwyF%2FgXBUSs8SCNog2aZrDWR6KX6vFCLnU6Qy59Na3U943XrrvjiypfaYvKea%2BoJ5ss4OtYbLxdiDZ3vjtiiqPAJ8SjnTyRH%2BnuflrPbVdnJd3%2FRLkMZr9bucOtt5fp9p%2FcdIE3iYMIBQPMq9I2ySaJrq4o1uGWqPRnVAf9MkDtnPmrkt3W7JZKjMe5xMu8ikryzZsD8NmdKScy%2BYksds0ali5tYcu1APOqrVB2O9i0q15VJ9qM0h%2BHXHYwXv9kjQ3jjbNmSPO3Sw5yujdOAkk7Dz5GI%2FpdXhHCf%2FoxObbppjKu4PzEKNsfyXmcaLKPXB0Ybo1AbY9mH4yJzrGS4XpPlPzjUJ7ECxI7zG4nnrkyegEAzKdU%2BgChyks1MLvJ8MsGOqUBdn7ZHJRf%2BneLkcguxJcKnD5ELIxSY6Up%2FsV52GNHobA5skFrMoFF8Y%2Bc7RBAZU2aPdORu0i3YnbUgzVqJ2lAHKnUTPYkMB7uFlAWufP2lKFXx0kvs09FireG%2FKHJ1XS5QFUIp%2FFqDKHsgihTPWc4M3gZuRrtH1TUP8s6ZeDIiyQLVaKghx6aw1ZH9fXvTmDNHDldNuyPFuhdobK6cMm%2B3o2P648U&X-Amz-Signature=ff30d13586ea504ab3661346e7e7fc8b8d8c95fa9b513ce649a6ca4dd1e4a20c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



