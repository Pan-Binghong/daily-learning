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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WQ2TW4E%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA39IoxgXNHNwEbqHmJElqvWTFGgeU42LhA0oXkamB7JAiEAmgHm1OWbjozPaw9UAli25SErcX0OlVmXR8PSvJEJkpAqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBzaalCjOvsFPBebHircA8GS%2BvMTqDs4otvBTckRUNiOI9mO6wG25mgHbGb%2BrPzwXHtIiIP4sX90eNO4Fq6pqvy3pw0%2BYHnQLlbDw971JNWtygrF78%2B535%2Blx00grmEmyZUcvAK1UuXfBWTZx3wWqmUizWRNlHPqzFhIVX6dgXYf3DPR22XUoIWdIFQUYeFjiYhZENsTSR%2FbMyjmRkAXQyNO%2F6Var%2FOMlt9x2ahfZ0gpRDcppKrfb580GAYYz26XihQhoFI7O0wbKtce9jOal4FaGq8yRZh6ITbsZZKsDHVCn2WL2dYm%2BYGFf29OPbLvWDBxOruDUybpK%2FUVfCK97jpuR1%2B%2Fgz3wOtQ2xrq8HMnVlF9EeafHO23WZAt5TNHKDUBdp%2FVUfeIuypxbNTV53bDdcFJYziKgAV4HCJEanEiWY%2BWdZJ4sfC33KRTbYRR82d%2FaKffcONdqcvwkIG4HKcclW2VRSsTReimowCrufG4E2IwktEq%2FWXt2rsEl8eQWXySbxF2vip0L02eNu5lbFdcIMG92oMCxf3G%2B9OqyStNacrOxeB1O4Xypkl%2B3LLR5jg24%2Fp0a1QLE4Bs1RGhX%2BG36P0MpjScs5dg%2Fw57%2BiKj4Kc1ivLHffSqKGvnVNlmn0TUlSIeYEBoCuLRKMJXg5MgGOqUBIBOYegOCDka1XylP0d38hjT9JUeZgPuyFjZOrv9GH4K1zAgCzeA%2FplnE6wfoRjWuDSwCclr0ZUsR7tSGCxVfxGcD%2FM2SiEg0WPGm8cZ5803HpBC3bbv0TO1kUP0wuteT%2Frp6q1m%2FYG61HBRFWlEVryf3QP6lJ1XFefvLifGzWZdoXmB061wdQPBm4A9NemDlVCWQ6KNRnXBLJ8tvqFSWyTr%2FARHN&X-Amz-Signature=9a0a1296d031611ed198e3b7e5f8a628fa1c6f79e7b068346c5e68455f017996&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



