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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZDATW5B%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCID23y%2FlulxkOT30M1xluJhaBd0A7b78to5x3AaSveiH2AiEA4KxFthgCQ4xlZVMDVD%2B%2FXR1zR8mjERYKWJUnziNpxB8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDEgm%2FKtX2xJC8tCPeSrcA08Qe7hBYkZrgqlq6mixf3ySuvr97aBvslOcDoFSP%2Bzzl4e0GV4mR6njQ67T5HF7%2BABHcRZtGqlcg4fbP8b3vp0Y%2F6v4EAY26627fdovTbgQko7Vb3l9kf9y9UDvVrFoqmftZfCZ6UMpwPCef1Oz7AQQUAoMlSDbLPK2%2B3n1GyXrii9QKNgIlmD8Yr360SIbhnmRce5aBzzkSYEt9Z9GtH3B3W1CkhqG9cwIVhpgFz8hcG4479g0mYPKgvOx6sQBRxSSDgrPSnm2KZaB%2FUfKplY4WilggrRywMFaK%2FcT94%2BL3wpsaZy3Vg7eVq2csb2WSwAGi35LMkrBRuW3cFQWz%2FqnBeoOl4ajWQRRLsd1GrMMz%2B9bqqaY2ZQgU%2Bjua89OYW6vwgZ%2FzVXeIKPSM06OaK5vmDLdjy3%2FCKhan%2BIHM%2F1vgS%2FVKmx38BExKqNR7EqenKWtLlGOF7u7L%2BROoUcf9%2B7cfF3N%2BbaYyqPohABsd9n6c1w%2FFiPeaOuobAFZLixtcyS46CHNlzcJv9OoGHarh7j9E%2Feez81ntHGBm5WEjKRKVrk8NNkh1DS15OlUgQxopGcxJJ%2FGjec4NdRZ7OsP8VvCQASDn45OukfUAoQIr19Tg3xRiPKE79ycX8zaMNi9ysgGOqUBbFY7qL1iOBIosbggCDfDQfcnocwTra1Q0iEyLvAEDHFW2fWz0gHzs7de9VyPjX7wphLBqA%2BLz0EV0cZWgTve3g93gOd3bHwbAuYQrkysMT4ODdlNwYhbDNL2q8vkynUzGZtn%2BK2vzmGnIC1K2cDp5r0%2FVEekv3TMEihmKVNa1wM7jVPN5I63uu0cepoqGEoTtyq0ZgwKrFcPL5Cy820ROcXAKrN9&X-Amz-Signature=f14ecd510ced1c4f5edb553943aa5a0f979a434ce0e9df93d25013b22003ce6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



