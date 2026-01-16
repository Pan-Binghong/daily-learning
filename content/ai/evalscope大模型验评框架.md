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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654WN5Z4Z%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIFeC5tRvJ5mjJ%2B0MWWj6rZpTSPFS%2BycIIZaxSEdPQlkWAiEA7ro0REM7gy2GgM7K1WrEjygaYBngLsIz3mgBsH4PxMgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDCI8K%2B43JQHD1VR7%2BSrcAyrU9c966cToW7xFNzu0j0x492kq%2FXNJQif3Iqxyi%2BaGewUD5vpHi5Okw2lK%2FzT5DQNfsnm6maMV8N2FQBhTZpx2TghyEp9uAoLayv5ze0o9Ss%2Fh6OcOEFe1P3up0JBvIfiIjW2Jw2R%2FH%2BDFuQjuReTcLTrV3yBIQC%2BcP27BeKoDRKbRhDZr0muk8MqM6WkfMdK%2BoiV5mr9dbfRlfVjd9FJ4wyZ%2BF%2F6C%2ByXiA0f2N7T4v9gpvNKNMP1ihOERGkdGoqOSnRpYopqtbYYkeYN38kxplYfhweq4BMbGvw24Tt0UVvZRG%2FMXJ3BnHGgBnzVDsSey1NBJJBgYpa8SxVswxKVNah3Cj7JHqgTIeAA%2Fg4FEHWIYb%2BSzNKU%2FGWSWzDUTaH%2F9ldyh4SG4uWZVYTLHIU%2FyGVpECFqu%2FNGUgOYDzO57S69380xfyBsQx4uarEdamzNT5pVUfp9Jm1wTWGnA5%2F5uIPv%2BHLjNDNXlvwBjIkcQmo95ioDdFeKYHaFLLrmFMCq23lhSZHjahfAk5bMvReZhom3SjOE6e0pk14x8u6eVWGfYSnlydQ700C2gY1Q80ioNGbqn6Guaw2XB2CjUQWEl7Ob1VSD8XK3vgois0WwigAPJddOC4aaVIr9ZMKy%2FpssGOqUBPpuQ5nkVgfBh8O2I5ypTPPSXs6aufkPKeEgP95HqUwr7A2e5A1r92bvQNydaFT0%2BMyFVeaAxTZSujYT1Wt9UiRUFZuBviFgt93nSYKoJJoSTvi3%2BC9DT1o3Zxj2RI0pYhQ4M0k78jvZtgSJEhLL4ND77KCQtQMijoAHwx40hYjp9BsmXQbMeII3KubTfwu%2BvX9flRAnJTI1iml37KoYnp8eQ4dmL&X-Amz-Signature=8f12ec395f9352f7422aae2d5f9a5f4d442fc6ee2b954011aa398c7bae4e966f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



