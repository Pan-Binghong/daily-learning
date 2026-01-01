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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDFHOCLR%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIG5wXi7f6kWi32L%2B45TM%2ByuXwgL%2Fj1F0CtU0o9fXyRmcAiAk0WkJpw03n7O%2FVQKo38rh8J4PMu6UZKxkJhP6I8s8wCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqZTTL9O5OWAlDjq3KtwDXve%2FnLIh%2BkqFu9JSXRCGlpl7R4rYHFPjMzsLxoBEeA4aQxqZ2hNr79K4hJ5izFGsQljkLstPoH5PQ%2FBoRmG2yedA4tlEKgQWg44s9nDDQwgpP9Cmn77l4nR731h%2BU7yvgzGtnWNVTwFAEWg6xpP%2F2sP4AGDtiNi9L%2B8%2BqJsVigxrOB5W%2Bvc95WVP3qHgokeCL2MB62Ul07SykcZvq2aiaZoVnVpkBuWYhO49cgmc4Lp2TkIexKzst06zOSDAYzbya7waypRs2QazLaWwaluZCG3Udn%2FBbDXmVQuCaVpPsuhnelS%2B7Y7zTbyuOsKfZQVMA7TUbeS3saCnAHYZ%2BD7JDznq72be24dPIo01chK7W2HiEMYBsUvUXK1WYQ%2BaCnP1e1iohefqTJcje4vWBJCExf%2FVnoWKzdSl%2BfBb%2FvKYCaFJwvzJgAjgnwh6spdBN0Q13tYWHMxHD1MbnCvpUO1yX%2FPuHXu2CzcK3%2Ff9mZEz%2Fy9jr2OKzoFfUlWRzWLKazGqBrMtNV0QcF6QfVQ1UGD7JNNuSKwzKXkEnqIxoLKYZQ8Cxx0lX0EyRiJYpoEbK89tBQanQbNbJz8udSSVRo%2BkpzAZ21L1nKQU5jG7RFRZ9LrCDFUAJIpqUVGstXEw6pzXygY6pgHhxgvf6eCl0rqVxAVi7JDx0CI6F40cfITtsSYWGIUFstYi%2BMgHWXfWl6zPUi1UHUk8izi7YHSXLaubiR9VVHVPFtq4nTh%2FnVSAnElqG44P6GE5bPRf8u0x%2FdNzgZpDaF3oIoi6CkU4zLTrW0w8hH2f%2B61HwbDaYyh%2FWglZq4NbE4aCbRzLtmI5matTjfSBST8ntc1AWVZFByH%2B0PcvpPkYJ33Oeaw7&X-Amz-Signature=1b5d46326a99475020c6b4d92de0a9f95c5386b513f2fe776768950334f0d9f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



