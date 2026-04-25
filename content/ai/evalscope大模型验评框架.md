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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FOQQ5L7%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEbl%2BaH8%2FRZQJpjtBTxLkQjfihpfSyR4uJR%2BvwvdFsNgAiApZH6nQ%2B5lqvuSqw7j4KTvJTAQWFQu9wRuPvJwC1PdISqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuhHMESeGz62WmaBuKtwDuqm30STLU3gDO%2BTQrIbDeCXIs3KGO520G9WkQViwI%2Besau3413XeJBe3Uj%2B9s%2FEsPPa1vj7dnrxPYsEzUWqMBpa1GqsTpObEnLNlyriK6n73lWQ5U5471Kjf5qROoqXpwdz0PhsCMHexFt2%2FnhNBeffjo18Xwy1acaOc%2B2fBqQR87BPR1CfzJpLYDCuETCWpxpKriLN882ep1HGKq86fSCtP4bYRHjEMXLUg0Y3oy7r%2BJDnZnVWILKwSTICeAN7kM1Yw2KB7pEr1Oxli0194Ff%2BDoe%2F2ny5O7Q%2FqTv3ABvByh5q6YggEs4toWPzRnra3REIDWB5Yg4JTaB3iFk4rw1ETPTVAnisu%2BftYtJxbusM8FRiXLksFIyhXYl8gDt1cZECsagslgPZDzz5uccpLX5kQu6xn8asPQxrw5GEN7%2F21xzN6MZJZDZekW8XLdWhy2s9Jg47d1oxsoHS1Fo1BD3B94rCvQBK114n2Rvah3nmJMKPVTQUoKwHN3n44BJ6RNWKOWbyrhNTKHSjlctsBgvxZsU56aLWMpuNIeQNNuI25%2FYW1FPsqKDQBRqp4h00FoGQGhLehQBxxEValYLe%2FfSScVAuH5ONEgBv0bSIKtjFBa3Fv%2FTh0Bsb1ZTcwgPOwzwY6pgGCz1ehhCDlEYo3Yabavb78eJoIMk20CQXa7Lx23ib1%2BucAnQqd%2BRwzp4Y8PcMnpjuk9Zs8jiVUighQUjznbHIjDe%2Bm3oy4H1dM7Xc1A9c4MwDOBdd5mPPjdAisOFk1fVtDAE9iUdvJ8quuRmJefhGYsDornAKnhPbvobVDD64C5vnZo03cKU636tu9VS0ESBoAyRXQivbmBlEzHbkd4yfnzKUIz5aO&X-Amz-Signature=f5d466c136d1a3a0cf5adc667c779e76485731335e1b23a39186883546417a5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



