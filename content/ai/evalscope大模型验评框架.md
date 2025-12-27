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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S74U5P66%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqC62sNSZlT4WQxe%2FHsRryMeVgaCW%2F%2BUJaCuDEUppnMwIhAMcq312uMo0uV385pbJmI1tc9mksrjfVWAgl6xYT817WKv8DCGIQABoMNjM3NDIzMTgzODA1Igx6kdvLBOJl37v4D9Yq3AOsHEdDZsD%2Frfe8%2FeKMrsSGOQNREhi3QOCZwjzqQ0zGRcih%2BLwOUYeFShf2TXOpYMMk%2Fjd6Phwo1iFBJc16MdG9R81GJYzSjHfunyCCOaynjazJm%2FgVbgccgC8p5TtzLWp4uBysamN8RlWHkvW8%2FlR1AyD9usbcra%2FItv3FJMHFNIqU88pRML%2FyZC1vb7FlR63MsYnt24RqwrS1mT79SMi80ZkTUlvnGemjPulaUq7ufEfOeEFkCdiV%2FrweZ6hw4tjXeDCD%2BIYLf%2FanwhdLu7%2B4fPTtei7gCc2hhroeHMU5IfG7nExS3EouVItyiLvdO7KJupReRhOzrDd1AETdvLXrXq5EM%2BzavBjf%2FhQHBnmx%2F1xKHmctRv9V%2FRHZgjVoJspfd2PpOCTuFTPYYIi7uLMW0ST0ScwWE4hL7krqDevTCMI1WYrPGwyPC9IkWP%2B36j53Eavng9e3JAj0K1yYT73y4iSUXn7%2FRege6YfZSsGKMh6kZLGdGV%2FzXaXZG1l8S3oTuNmuxchmAFLJZIUVhJEgtedoLt4L2fOeTknKq%2FMEvKyLQdYKkiSV0dfYCmAwQ45kuIk4B9vY5twyL1MLlbg8DXjiclKSUQqW7F%2FBTgh871rmOqf%2FtrvV6z5EzTC757zKBjqkAQHuGEe07Lmv3%2BGySTr8dnqFECxQow2O1Rm4nBBQJca%2FkTov5saezaS1DIQxZ0L2xcyMlO%2F8T8%2B1rdp8kL7MZyZVbO6B6XJ1QXZI%2BI7iKmjv8r3%2BrMdxK8gafuF36u06WqZfG4lOF1e8i3gRkxu17Cn558A6EChFZThSJUXBPgh5adfeM1KCf%2BYLhCvOQBAk86Yb%2Ba3Uk2WRLKPfduhi3W5T4sPU&X-Amz-Signature=ddc93359441b3b8dfbae59615c3a1d3cc01bc67a9507428cc6aed99a8ec365f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



