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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VA63ZCN%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQDrWoGLqpq2bI9mgV0V5pzgKiC2U9NGNYMs6AQsB7k6jgIhAJaBX9L%2FynHHpP5YqhtjUotz0FjZ0leZLaTjzR2Dkar5KogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyVp8afB5HBgTEpZWAq3APHGdlIWfOTyuuSf6s0fCcjLQxJdXCZ8LTOfw5kCyFVDnVSQ6v3SS%2FQEpmpdHpsbzD6I30TzetWUgE1wYZPdv%2BgS3TqNhjm76UaZZ6cHfP%2BgJ4AHJwsvRc2SQU506Lyeee3T%2BywdtZim5SJJ6hZaVLtjj8UOvv2ybg1x4v8%2F7413wgxLRZZ0sHfKTiNKfYhIZklircnWWwpiLmRPpm794dmbRD1sCXvH87KtBwoKsQzE8tm6YkdvwehxSW9%2FT5DBYx3JqZ1TkCb4BEYNZidAd3jdnj2Tf4IPreBubcqJhlluQia%2F7MzOf1j5tXQWX4H4UUlAbzCTdCUgW7n7DSJOi8kScrQjX2x23fYXTVVbFu3imRkbr08uQ%2Bum1lkCNQRZHXmGcOMjUw9YntSgdgnLTohvrzidkz9XOzvUjzLlOewVWQ62qCTkL5%2F8wq1j8j%2FztRq7MSQYXEVMdidmCd6RjASZ26WJbK520tEuhRvkWEEiErMpbXcGf6g6JeVj0rueMlxcIF9OhDaN5wVtAhb3RXLbRT%2FCrnULxnIQWHqr88DXSdnwEM%2BhS4TkvGyg4LSS7g2QUy%2BDLlDWtS9E36bg0QDWJi450I1h%2FlBfUAlrWHLRNzO00IGM9U2gVYOwzDW2IXMBjqkAXuIHTycfzufBurAaVdO90VsUWmOo2ZwyfTWuVdSbpPrz7g%2F70WOBVzlBY2v%2FJoniJWd%2FP1iWAz%2BzoyidO%2F50IA2wjkwm0xqdQ%2FUuCkpWg06kK3cfc75GYJyS%2FHtWncuCaMuJcxK2ZmCRnHOgMnPpN9Lou4Qd2KWi0T2vFDp%2FE2YwqotvhxCKH%2BEG8hVEoP8UsBkXcwPC6eXsFw4shVKqoaDHBvO&X-Amz-Signature=4649c432ba0e30c58cc32058bb1a35d516c25b0e40097789f7ed29e7403808ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



