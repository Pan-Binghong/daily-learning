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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OPJDV4Q%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2vL%2BtnBQibAXka24ISYCjdfnKmsa%2Bm56i7u24rLvzOQIgaL8vzwF0EyRI3KuG6Usw%2FNmmF5Wlnu1CZdVtMNl85E8qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJif27pKfGTgJX5iGCrcAx1YlMjhZYgy7ScvVN7HLuYqw2%2BHabsBN3R9Uu8fxJxNGtMggxYTNlHnyxaEusLP8jjMESmGxeNEbG%2FlQccsZYkkqCYrNr4KGSAGDaI9j%2FKij49hmD6V2Ouv99o04meHnosIriS8d7J%2FFaQPRTX0bp4SUNmf51N8d3DLe2EhbCNT0eMwLdTHNB8mDm6jQRYI3zGfPtiDqMF5Qd6RWr0o8m%2BrX4oE7Rg2M6M1x459Nirq4rBu1%2BmDP%2BogTDdbuXZU1nuqQBVvciTzUDvbDFVPFSLq9blj%2BNEG7IFE4NeZLELdD6BBULqavipjeHDjwH3c0jQ%2BhY2GTVveYlSGNMrO28Q0xXdT6K6Lchqrd11c0EvVYRh9K4jt5lAzKcxTaoZCDWT7sefLZqrsiHZATaJYExeyVIxgBnuBFCWO%2BW%2FBp8qcLzs6EH2PrquHIlyJBE5N7aB0igwMOvROoQeIZuzWRaCmT%2B3OYAr1bpQ77nxqS%2FQopyCvxjsQHBRoxLTS5QV6Y7o5O51HDq45ldHyELo%2F574OTyIjLJGze6ZkAnrxMVMt49ibjcvwOTWc9o3HTk%2FrmqE%2FTXP1W9NMNZWWeNjQmEZ9lV09iO8BwrChurdyr0fOWLDEtY3ohDRMihb6MO3L6cwGOqUByh8taFWoabTrAoPwy%2BSaLwBaTNsk6OMAFvL26Yfy6MCYRmv3pV8YYstPy2OFdigPJQ640hrc9NYyNkxUhqWyX%2BDH4SnaydwbVngutjcX1DDC0Dx5Pa0uKk0kjnIU11OD8oqwTXWQoUjH8vhtERbsrqtdXifpxZN33MxFGlS8QBW2QaqdrHoj%2FGvKE35WL%2Br1iEkmq6U3H9SuGZQU%2Fn%2FUDijd47nA&X-Amz-Signature=ebf209c050bba68a0cdb9bb3c1fe8fc64060dd3b8ff4e75f306d880ee77d57e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



