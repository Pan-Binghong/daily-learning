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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPN3BOQD%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Bxt8l2BdD26i3xjP1%2BMWgceuCH%2BiR%2FcXj4%2FQSP3acxgIgY4GOxE9Pr8xkqJF4cfirGBW9BDM381pQG4475FQQvUMqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiOom%2BZ2uQl%2FSmE5yrcA9ZnOtU7A9DABPGUzMgI0RiQBHk5zDExgeJ4xPYEZIWqgOqvk6CmcsvoSI5D0gpMUfZWZXDYbV6mluyIhJ5Bu7oRiHlWWcwIKGWrNqTrWxy29wlr19jF6NLDWg3O0E65ZoOkBPEkQKCaoMkAaFs4%2FRekNWXmZRhiyGBoZfTy5Z8O6hZ5fiA6W47PKMNd5gMswoVRer68r0Tt9uqYqEWWOfcfO9EIo7BKXSF%2BOTTc79wFM7itfFhF%2F5WJvIj0WBSl8SIlfFzG7uWcXZdK6C6ge2eIwKLornOwPc3%2FzntDy6qJ48ahChz%2FsNYtNi735lZCmWHjF6pBEi2mBYeNjpGjF2CdRo2QhxCqr7Z%2Fa%2Fse3ep2Jj3b%2BPrKYMHUtyspoZG1Uy%2F%2FrioHhXfkGE00BoNkcMcYY1TqWAtJxVusvXrPhT%2BubwjS3uMzki9OicO0VarlvvpPd%2BOvsiIlCgZ%2FW%2FDtKjf5nfq54X3IimtZRZJWm1v9QyFlMlXds5vd1TUIly8ZSMOvy6D508o7GIwGEGDXcsdf%2B2E96H3OUUM9ibTxmb5czehQOExji0ThkP8jW0QFqQd6Q1zdSE89AuItqDDt8if1OBRutu%2F%2FJ8YomqxvKqvbWqJKP0fHAmY4B2u8MPqcx84GOqUBBVses1I%2FIf1aa%2BIq4NNDEoNWMfYJBVa45dA4yGqz5pHRHKYUaIHUEid6U%2Fdx4AQ8YFpnbux0NeUxQGjUfcajZ0WySxPBYw76reoIv2bdGIhk7NtjE%2FwDBz4LfJlmmSKSY2piJz02lnUwpmlBF%2BbwBMACErVtglm02N%2BRpw9%2F%2FGan2pMgqIwmo4rpJZMFVYBgDo8RwfmeqT%2Fg4XaqHNxIi7N0vG2Z&X-Amz-Signature=6ddc4c7db503c188e0681c67064cf0105a93dcd2a61c15f81bb9c307bf47c432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



