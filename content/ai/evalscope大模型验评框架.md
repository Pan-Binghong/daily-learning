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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP5LU4V6%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKzW%2F6ZPB134v8FgNFSBUMYqzaY3GcEUU3%2FqJVsCYnggIgEIWpNZD0POCUtFotpTqrZ0VhIYS5Md9SuCtLY91s6Wcq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOXCfOm5iDYuHDCZ3yrcA9x84a2oCAkQ2S5ebH%2BnxX709qwlP2tzPifJ0ki02YBHkOr0xgDj%2B6QguqGOczuAabAlIk3XlwA62AboKoFO9%2FfXafMVmPH25UX7lsNslbLhiubP9WDZJixcH7RN0eyfrffpUliz%2BSEGPY%2BYeG1L8x%2FRFkWOxQ%2FvgvR5eUcA8MKYZRNbGJNzPXEd%2BWfwe2H32ks6kD7dGh57KSI47XfKaS9fC%2FW8%2BJ47izFAID0qO9Z%2B1jpDlJLFuNcyT7oi4d9bWbqWi3ItT8nkMONzvY%2BzitlusacvoBbG0JaJvth39EvTSXK3v%2B2TqREDPqOH9d%2Fe29F%2FvuKOFh3bgH1hdiV2%2FuD28nXQjt43zeuMclGnqIEQAuQKdK0nEbaDNndAfXcquObClJgAbcfGgHycrx44q2KK05Gd%2FHvTOPAWMhvhSA1YcIGmlVGsoysx1xmWsAnEWdj05GgplvJiGRzLiRe9gX5q7Tx60A8DMX5NG%2BFO1kUSuVL77W9gc%2BYj36erSY6iSMMxB8fMg8oiBBs9kvAeeuo7%2Fl0SVQo6dvLcHCk%2BbpdQGdqQWdBdzTSWKcnD19NYwTwLAMRO10rQBKcmFvhZBa5J85tdOaqhQe6zEKLgQOTpEHesuZmlomdFovyiMN%2Flpc8GOqUBoOIjqzlvjF%2F0D7jTrTz%2FPhxmRG6KkM1DLZp2CRqDSw6yIGHjvY2T%2Bjwf8trw5os%2BRVOuaPz20GpV1ewkDDfx%2F5z9uUeCrEW7BAWXTKHAinZzJcSb3tWDMw9r3QLl%2Bt%2FsGVN8%2FptNXOxZO6sdnT5vnq%2F99NHU07EAnE1TennAN%2BOxhPi0LJJ5TgJIuT34dvtihbaHjzKGVOEEYc287CKD58CKmRAw&X-Amz-Signature=1a59345360b10cc8de2306938d0e626e350428c40320603d79bfe38c41f32539&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



