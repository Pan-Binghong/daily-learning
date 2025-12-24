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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N6UB6YC%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCrdXa0lF2aQBV8vxaM2qN5dKlVGMulCyb739tS%2FQ1EugIhAPR1LAgzAaXVmxHYC6NnBQDxuJnHah%2FlB33JD0%2Bl4Z9DKv8DCBkQABoMNjM3NDIzMTgzODA1Igyt3APtiYQ1e8LjljYq3AOyUtqiomd1QQuNM57ZkS5X7oly7FzNDRuW1bY52QQcmgNURDcA8hzEjQHK6V996t766aacN5LrwM%2FuQXgBud5zkL69YA6Cgx9GkR%2F21jxB%2FynTsEhxetT1LNP%2BPO21DirPSvtUIQ6qhKiVG%2BBCmt2MoMDDp%2Bm9NG4tbcNWkFYGYOLMOh%2FvJ9wjgarQIFMo0HRhYpvj6ViHmrCrhRz08yu3g3WBQiUSgY%2FjYVxkM8TybVYF3a8X0W1RqP%2B%2FRNKnUQAt0ojwSP2mI7L8r9cmm3TSQb9YT1k6Tb9Z7zNrjRTp6UyctiisNqiq5C4%2BzpgcaZv9wV5%2B3rS9MFs5OPTTlmOW8y81%2Bm7z%2B5mhLYf8EMwERtTyM6xXDkdGhYgZ0rJPi8vtDOkw6dXg%2FV15xCXMZXW1E5zzf7Wo2MAscTQ4mqlbTDF%2FvYJ3WA760nzKuqwz5MTUWIzSLLq0qY6x91JmjgdiXGKzkvIlzy27xFwUXfNr5y0wpadPLfGdPoEmI6MqxjGMskPQ2bwOa94WUfEkM1NiRbELiEXVHooxaxIoauhu8NkDzRTXrrj2GwZoz1ENquo8hNoz1Kbgtr11%2FB5Xtqpp0uqxmhfCzrkMHu7GI4bypE%2Bqw3IGCbDqUneEMzC04azKBjqkAU4R6wMsoLGP6Vy89%2FSw2sWpkKuRNwIrTARKcPE0YT7ro7E4iTPDnVM1E2p6o8clGEZEmkBg%2B9UG89xbYf4xWS7kBfRg1cIXzIK0156rXYHppN62UAzvJrqUGyGEh2HKRq%2BddG7lDzAJmgQyvWCGa78IqWlHUau8mz8ixe7%2BxEi%2FslP2IK61JOpgG8sWhpHJq6DiEyE3VKNiK1GcuWL%2FNLPI5xt5&X-Amz-Signature=7847106dd90bb9ee6d2d90e6bbf701eb5c3dca1a14af706ae63dc524c9846666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



