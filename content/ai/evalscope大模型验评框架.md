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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644W5B4TS%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjtXuZK7wa3RSoYrGI8zz4UzucBJlsd6dwL2yS%2BkAwwQIgQoZS2WQp0FvlyiYQkXO4nwASfFoefMmFxGV7epfjztMq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH7tuCccte5Ol%2BvsUSrcA25qQWT4OdiL8BZoaRy4O3ReiKUJqvXGcU%2F0AHRnCcvFodliqBEwEx9Ys4TlCIyv5nmMu3qOjSc2X%2FsxOhGjDdUv%2FyEfaIxZ%2FeObTUIXK42MCaws7iTsGMQDpuCu8pasnOk33aCw8LP%2F6Vn%2Fm%2F21KA4r6kzzx6pn%2Bs5S8ap6il%2FMgjWt61lswi%2F4Ux6uCMvFtwsBetNdYx%2BUAfefbCC6MuBMedVVvGsDEXI%2B9jElFNO%2BjJWd7ZMDYX6dpBd5JIw6AalQBdpBBjPkVy0bhVScQ0hq67nR6bksuXiGUXFdYq%2BqQI%2FMEOBWd6PvrgE47%2BTLuc%2B7iwAapGqDrME%2FFEyrLClgzUAXehzqUiyDSJwA3geXVhKTI9jR%2FCFm3O5pJ0DzGVUeEIKhwZSZi1JDqBqc2iByHZyyDpYGIN1MFcHd740iHbUcZjqG7vx%2F5RmE%2FZtPP%2BzMai6DOAa9DkPr3BbUJVnogLmry9YWOekAfm1MDL%2Byzx8%2FQ0T5MCRMprKYZKMBYUstDbXyPO%2Bf%2FodeHoLHNoIcaZD9v3o5BpuXZsdqJfjSPXj5ZyotwkwAQ78QU1FA4GqaXBBdgyq1ZVVuLLSoKLvHQ5kI59EuvwETxGEbiWZ%2FUk0hKfqAF7tIghAYMJndjskGOqUBoapf0K1raUe%2FkbNHLdd9J6rt%2F5cjcG6UueT67h1NwvvLzYvLtmJ51%2FN%2FlCfzdbn31Q%2Fuhvumia0rv97lfzqh3s3sIZ91PJO%2BjXwJZjJz6MW9Lii38kWeT8ojJ0kqE5PK6MgClA4WyatSDFMQ6oXSywcB%2B0nE%2Bgf6F3lc6hNogRnzE5nQ1u5Z2n6FJxOLuyAss1rn0xjUHSTnp8wMtSjJa7o%2FMtDi&X-Amz-Signature=7ec30c8954aafcdea9890ecbc1d132d56cf3817320b0c4b63ed1badfaf308a23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



