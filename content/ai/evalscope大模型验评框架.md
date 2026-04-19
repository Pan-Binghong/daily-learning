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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHSML735%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDm%2BnFTJWNq9%2F7bNLPzcZ2tBERT7eL2c7zeYpbFjBfvPQIgZbDkFmNKZSrDKLBqfyt7NTeM6SmioUDBdjwdkMx%2FjNoqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOnthZnBcGPABBcYqSrcA92iC6%2BLxfXEBjvZ9EZA%2FrPF3ICq1VEsKazIqZ6jiV5YWdKTkNlU%2F2CTimpleYZlbjlGdu15QR%2FaV5V5qceQWZ2oQCi3fcbb%2FPfZDZbeRtwmlWdhvUOJ3jzLbyJeJezQ1a4wk4b2Q4F5r1WpNUrAro%2F3nN%2Br7gzzuAuCg7ChMnVdJA5k1pV1h6I1d0yIPCxuHd7t%2BuRtwsXGdwVEneVP%2FF12sulvGjfFkn3d5ks9k2OeQY%2BDNYSeDyt3w%2FmfPfpWrIO6IMkK1Vy1Q%2BejlI%2FxwQJs7UGZfaeHgaEwgyRM1YDqaCKx%2Bx0rmBnL4ZQ3169%2BMTBuj6XLppWQvaLztVRHrJCwiBufG%2FjdIxTvLVxJaA6wSdXvql2eeB%2FJPAtJ60ktLL1sdOE1UlzEJt%2B7FUstwqq44ylS044NMxRAtoEEdNUHeb5IoK91zg5JepeWT256qlsCOU%2FdgHMfdTwY%2BQ%2FY954DKqSH3S3O4QYKwDpEJrJhu63qDrXC46W2ifk8CmWp6n%2BH7zd9VX9a8wicfEHVwslu8DEK%2FVpyg8mbyvfFF%2Bik14UkUtZI3j2QWCT5%2BltjQcQsY%2BMki3545Fw7mTV2b6ge7NUVyjj51Gqca75uY%2F6UMA4rzWMmfwBX%2FkvFMM7ekM8GOqUB9V%2BNLjWt4k5QlidpPW9RlPtuGSQPBYNtI8miM952c8MehGdjB%2FX7kBepT2lik6r4%2FPVDjU1gc7%2FVUSO4m1HiaQQsUgLUg80Nnpd6fYLBeF7tQ27nKN9CAktFP8dw2Bzs6KqbXvVI9UKSUt4yj25xZEn%2F41qhP8dTCd8Sq%2FNa4rhX6ti1zzGeSjgccZzampCkMmCvrDqwkH1obPnnwL0CEuFYWMMC&X-Amz-Signature=6f6b626b84d1c60672d604e503031f65fec1105c5888aeb9a39dd641c0298d26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



