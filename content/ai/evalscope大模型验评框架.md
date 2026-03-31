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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOZ45TR7%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCICZMpxOOStKEik6vTnP3CltTd5kKHu0livKbFAW5Sf2bAiAKnE2csjxlBxOlipep9Nb4nUnfUphld9RY3ZeOxCuMcCr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMuYFQMPa7UptVCS2kKtwD%2FCvWLUEOqbambfMV%2FHh1cBVdHlvm8MyC6%2FWquwEOHqxhK67X7FbqUcljswRkOlGLgBVbXuc3kF4%2FbSEnWSc8XQNgUI5vASkYVQ8sth5hCHvWTJXASnNSitYOND8Mnv8KUnfJmlJZRBBOZTtH3vgxtSY4%2Byu1J1iHdL8IuoEL4DveghA6dPrqJ2%2FqWJq38hzCG0xkabaSfHQ%2BeTSurRLdd4vIQpmE7sURWG5UH3DgzAymoPVoUlQd%2FaIgDCXuAhEO1NN7U6OjkrBdiWtFvgrD73K2K28j0GBMLtchRLpp%2FqUbvHWOO7sKUlZEt%2B0Fu5RCopBfyrc2HKKBDu6L1i5xRZmBXmwFclIdgcaST9n9k63gk%2BW0XT4z8UMqbTs8N4W4t5E9hR%2FWSCcq%2BFla4AYF9Txk%2FmIg3VsJjnX2xJvgeuRL9TPNns0eKGDBhzyCKixPlY04mf1zWi4hunIizd6lIlZfaW1VIDGebLSLObanvAcA4BNFU4y4cCKhpzyji7xx3GOcwn%2FN0ELoCAZz%2BPWbQjRvms5SdlFR%2FHyy%2BGGuKjaDgUEFeQAhVWMGNj9YUmfHrWkiZQLhBycxQLo3wrw0Vnh%2FtAt11TEtXmiue6uDh75ENm4a5xHnxaMCjEQw5e6szgY6pgGgMZIvUz%2F2vGS4OTdQqtLUMIXfBupjOZOxf07LK7tNQup1cV04SBXf0SBgeXJfINOTR%2FMKt888Hb1T5U%2FdiWvNWET92PhDJ%2BwggUb%2F89POcsrVYgZ9UD5wH2I4QdQnT32upqGpSQ%2BCT%2BohqN%2FNaKpUOA%2F%2F2dXAF5L1smpXD5Y%2BIuaQWAg2X927DOJmRBlA9YMILa0AL0NZh9H1ZHJ4CFSLIl8fMZv5&X-Amz-Signature=8245bc4fd2b14c5d452950bd2e864969d2fcb0f2513232e617db801bd8ef69e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



