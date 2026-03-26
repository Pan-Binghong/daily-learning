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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXGX54LC%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHNqM5XsT%2BMHKng0C7ukXPmAxhNj4EyGUT%2BRfoVLwl7wIhAMn1uH%2FnQYtXSKOe3JiRqSzzSOY3m5bXP8uf12hQY76%2BKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDQwu58UiGCo4dzuoq3APMDBV0cyGCl2hRLxmCM3848JZTY1pe53aZI041RjW0jhffkWV480rs2VAZWB%2FMoJELsMn7dnKP7vfOxcfbnaFyuwlLCCTVE%2B8QFMDtU86WizhX2rMggtnpMroUH9GFwm5R1H55GJsewmO6SfFqatY92xPb8ly5GH6YnRsOrtTCJ7h3bMp6nJhQRBfWGYtldwewSVtnkasYPtPHidZqLaCOJGki8P3GGyEc5nn8UyS9lKcb7O6cF5Z0HSh0IiJ6T%2Bx9s03fA3KO8%2BQ2yE0uqjx1D6QhXLZSmZ53mv%2BJmEYedrpldM7G8f1Ve0IKq04engRpRLQxA7xgLn6FaX63mcw8r47L3xYV7refN1yybbcwYIjsa3gu0R9X6wUBVzYDHwC9Y9LxqM8euYcuNj49Q0%2FApqFrfPY9Eitxoe9eCDuUgXGTyvbMhp8UzcgMEiXVl1L7CjZ3OXR8Lq2akIRs60oIMPK8C4kcBCt1vhgdeRL%2BYn9JJr0m8YosmBiGDebUaTZYz%2BPfahGMuRk5LGlDdoJrQ76kLDTmbM73Mn%2FbPr63Aqx%2Ft14XOVxHh3yxibpXEyBl%2F%2B9lveDTNsu%2BHHr26EGvzfQTPloNlivuTyFtJwCiO5uu6XcXQHXrwNxG5DC3yZLOBjqkARxOSrZmnoOp28M6uKbpNSqSvJcTfyyoc03F%2FrqYdcL5w2edN4dRXgib33PnKEG%2B23K7v6FjX1fLoEHD3JE0odRMZdlEk6faIi3F%2FtNqYbHlv%2FqhoNEwIZoNMIyODteE99lxgr3cQYMvymah0H0i5JXX7UNINET2USZvO67QUWsHCH%2FjkiDU0d58PBlM%2Fhk9jqZ7KDeCORGFIEOQt7YF9AsNCEpg&X-Amz-Signature=e8e3a8ad5a21517fcf2aa66e99f22115ab84aefaf29eba29154c63eddc0e0172&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



