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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPGCYKJK%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFMklfh0AeA7kwDyh%2BoFuoFElic8bt7ljwRy%2Brycjhl6AiEAsvU2FzVmP2AJfCeRQ1vZaJj6S4lCpvutA9601rFsm1sq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDAOp9YJJ%2FOOGtLuE7SrcA7Xt1WidWmeIxCPwzBOR3QiIXR7k1slGo79CodYriZDmgt6Fue5madxdnWhgM2ycFu5x3OLkcCAcHjT%2F8t71n6RUuxY%2BtRqzPMOEy4FDOHgNtg59msRDV57ZBdNbR81OsXnU0NleaLC%2FAJ7ATWEPQ7ng8I2J1a8Qm1W%2FxzN3vgdGvS9D%2FznLfaNn2%2BjxE5SOOnAlPBzCl3NjERbEWbf3kzzacAbLzxOJYvC%2FBKf69mGaSAG7UWbMXCzO7koqMOu2p55Bn5ouFFEDH0vfEYnNDiMEYMOEzj0203VJA9XiP%2FHmQsDS2CBY9UAQEew5UbdZtfcJHqrigoa0Purj3cQR6reHp92hN%2FWffUktyt2wlyww2dlN4GcF9%2BFYWhIeptU%2F2icTd99pFjZrz%2BnGkmgpTZUvyj80HYx3Ib711ELgxuDVuL%2Byvv4WC3Cz2g60ZrGlmvSX7n5aRZMsQEOj4G28PIEJ5XvN2p%2FiQ3qRxNlzrMI8vjTpbwyRFDRnTSb2U73SqONxHp%2B%2F1dyA8%2F1VuyYY0lyLQYakNum%2B%2B9Bz18fRv6cKlOKN3YzLyFIcaND6ny1cIj45XP%2B5xh%2FCjpkMRmYlU2Lr1fOk3u7HFKDyGOac9bbbuKuWTEefc3E4g%2FP7MK2nzskGOqUBdkeEEN%2B5lY3jwEwjGGf7FqCSyOQb8Y%2FJF1J%2BMi4itXlupXP4EKJYNU%2BayJKFCAC30WvHLdsCQUeEmq%2BfbCqkjMuSvOHmrhjDXMJOkanH4z010Jdv1pXZHmhbP5DVR2uHjZRKaGMvZZ%2B%2BPu9ZTMQWjqcGamwv4HtJFIg743LE4fBSl6AkjNnNn6VaxhBHBu0cGSj0coydPl8uMD7ZYI%2BwD44WI%2FWD&X-Amz-Signature=5621938dfa2f7102358209055c58f13bd1812657df0a8f9cb5eb30e17e52ebed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



