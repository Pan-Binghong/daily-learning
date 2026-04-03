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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RCPM43D%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVL9KjQoTRGdn7%2Bx3Iphr2sOUE%2FVP1ScZ1xj0bUEMArwIhAK7el13ItRXbFnOddPGEynTvNzaPpFMakbmxGCJc%2BPqZKv8DCH8QABoMNjM3NDIzMTgzODA1IgypcnOXmljpfRUAmTMq3AMFBWATMut9U0cwdHci8P0ctkpnBDBqimjnywn8XpBzTTkNrHX7i0mhUrCedRwyAk6R8D8IH9T1bkPiWpz0%2BFo9L2%2FMk%2Bg40gsLCBx1YqO5PxHoVQ4XdY2AWcz%2B%2BPDaqVgs%2FqXKQR2UeEUa%2FMrRRVrrTmlDJFLQSOoRByeimiclBqfkozPKJYU0PVhprAyIAfTJKzkRXC%2FJac4wL7p15%2BC8himLFnaCm%2By0Q6wdA%2Fb2XeXRd58LqF0195idUPnl3uAjJjkRMGaK6afCUL0FHhNl2VHaYje7ijhXK0Yn2sRI7FlkYv3nABzJ3gZH86jYYUqBU7w%2FxGCiMHCnqlEtSYLB%2F298KeW2nLKHIbIpzsf%2BLRL62eTuXWYk3%2Fq2WmrQPCie%2BFkPTN16Qf81b2fsd00OY6ADpIn9TXD9ZNGiXVS42XIzB8diE%2Bwo9K0IJGDLSatf%2Fdxtgr0NPuVfPAcLVuS3V9%2BdqJUpwRWXk0JZB9Q1rV74lebi91KczAeqr%2BABprHIvgADg9ImiztmlGtZOdIKf5CHJHftY8vJE96BrcbaQXrpN2ItfhscOqtwPjSkPU42ekpAR7egHe6ErncRi%2Favczvnvwkpmo6QvY2uEU4iOpOaz044cU0OUeMtXTDgrb3OBjqkASXWknnYzPtBH3Q1rY39uhibIel%2BiB%2BD6lbQqPbPtM3fsJfWkUy6xFJsxnF7ddwLn8Vxozx%2BgSpkGU9YlDbxNMYDitFaaw%2FGqVMa5sk5cjeCYECqHbhDbOwvtmnrEf199PEmrfRTEttpaNryxWRBssziByV6nrDIpFQveuFK%2BE3Hs3PUb17HRXzOk%2Fc1QRMf8zljFNQZg1Z8M22xbX584j4CVbVB&X-Amz-Signature=7bfcb59ddc87f90347b7c51cb17f14d943aabf31e2d01e99e66c3fcf75f8e1d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



