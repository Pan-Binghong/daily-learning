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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5P3PWP6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIEhb2ScYn%2BZ4HLAxrt31sImASKmkNhxw%2BzmNJi41xNn8AiEA8KlWnV934V9YsLgRzkJVHNXe456QfmEqR68kQL8mwBAq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDFE%2F4J7upFP2qG5IzSrcA4zBxOXV5Ug4Irg04OXfSeWbQsOMXGARHcQ88g0H2d%2BXEeDA56S1Q3YYxW0t5qbUAZ%2Fslhbm%2BDtNFO8CBXi88XtJBdNVfRn6Zz%2Fx2i9FIzGPtp%2BF8qJ%2Fh6QJHvRt8AUBZonzTnJnW%2Bo4iAyB%2FJodmZtsIV1EDatmpJuJ6%2FqwsVQ1v3BTmgJIoHjW7M%2BJvyeAJJS2KBl5Qe7hEBnsOvr%2BnYefd6%2BqDj6N5k8pG89srxUoMeAkAtxMp545BZ%2FrEvGDQW6DuxqLikd%2B6zmfLyp7Pycnfporj6tlAlqYBhOPR3Y%2BMhqA593pBEAsoaO1F5gt8uUf4FO9OJCJ7nIgGeIJFdMoeHn2vHbMfQTFlovspfmifAzC770Xm7Fee1NQ4sxFErBnls%2B%2Bm5U2mt3L%2FJzN60IwHeqQnbamZvsX%2Fn1D4KiY8Cv%2Beh5KhniWLHK2BY3HRD4Fnz%2Bm6YvvdUh0AlUYmEZ1JxUKjbflFCuw%2BNYi3mveEZSXqVg4z3oeKDhNJ68uf6%2BnmcEzLX8Mfqm0pXDZ4g7jNhZVxQC%2FanB1TFHpbRXHIffeEwJfhbPxqlnSNENs4VxD8LsieLfKqtmanYLWM9VVZkOAWMB4AbTFk44hHa1kHibr97WeTp6vPZ3sMJqN88kGOqUBvem%2BlRNCZ7nwkk%2BRKVvpr3grf8W%2F87riioyC6vrGXFCo68bgbGMrs0Yrtyw0kDYmGXAyCKWbJ7UbPu1QwymLLRS0bdCBGxOj009M8nAZ4yazWAJwGuCtjxu4ppdeAgaFzRSttPxr7Jc1arq3Z4D2A6xsL1I%2FUwvYkoC8ZwNf5YEGtCCddJFaQ2dq2SJemWajxcZ8%2FnvubhQn1%2FHJYaDNrbhvSal1&X-Amz-Signature=05ca329d49fed58d2c7f922d7e3ba6676d23817ad95a3bf78a6c98d99316625b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



