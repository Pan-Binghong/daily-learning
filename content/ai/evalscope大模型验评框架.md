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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGKQMY3I%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5tJOg%2FMJnIYVuCZr3SbiLM%2Bk6shHWAjjkfIdiXa0r7QIgEmAsxP4skFmlaH8TKPi%2F0Fp%2FGrKDQVt33BIBjCc%2F8P4q%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDF4dTOGQCVIS8PfgOSrcA%2Bkbg3ELJxeEvuw9fzE%2FzLLL2hXmmGf24YqBauA4Jb0FibsszRefPGP5LNV3NiVlk0iYxHzwrS%2BnZje%2B1Lq5hBRixb79SK%2BFpTOtxBN6j1jiw1%2F%2Bnr50wxxwXV3%2FZtLk5v%2BKHJZXXyEe81VJV8Z%2FQjX4tkCsgmWOB1TZ511k%2BrDHhZxZtKd21nAojJBwWDBTF03oWWbMlbQWuA0tOLTyeBAThFAIvyFNAaO2YL5XM2EF6%2FHtBoL0lrDo22YyBcIK8HWLvFMo07U9Cgqsd%2Fd0BRCUUaLArklOp5VK8IRVSWaWjEN%2F9XNA%2Fq3sjnAcQgAmZpymnqpqkKYT0nWH3glys9pwe2yUq3LTLTqQFFqNl4RnkqhKKOA53DCiA4ts3UBvWMcWYTtNBqQhhQsdwxlJ66Bk5NVqAjdo1XklRsJsIw7x3nSOCp11dfh5GDhMHBx0y0T3u0P7KvSLtfS%2FSbSuA84FA6KjG1C%2BzjxkkQP%2BRlkaYbHAifxqEII0H4v%2Bj6pJBSISZVozQVnCu8f42NAw4ZEgNFdyIENCNJJNiRhvCd2M3%2FCKWJ4PaELi7RHageDfPMqMONlEzhkrJeC%2Fa50gdDVEKorWSeE3JRqhAqFQk2pxiH5290k8UKSfmZvIMMiW5csGOqUB%2Fzc4xBu4aA%2FFk0YvEqMpPiFPBzDbhGE6O2w%2BPqqB7iiGMi5lhYo4IqzM853RWlwjLBqLkn25R%2FLMMMG5NB981Fa13%2FcjLYyqZ5R0DC3ylp6bASDmVvNtnUWq5LkT%2Bbu74tsik985RxNKYg2eeTv4Is0FtUVlkxC8vERYX2%2F%2BluRe7EhGSvTIze67ICj1BKHrPyvE7dZCjWNUhZwX91WzyEZEtLuG&X-Amz-Signature=0536e284045695ba19d0fbe64cd42119ba10cff9706b1818c268aaa8e809daa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



