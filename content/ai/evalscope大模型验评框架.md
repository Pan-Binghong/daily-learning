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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667J6BIMEL%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSn8HEtm%2B4IbUJafbEPz5OlyvJuBzO5mQACkYKmWL99gIhANgfi5mriP%2FtAiMxKHoHUczO5ZAo6Vj3i5Jf4Jx4j02RKv8DCHwQABoMNjM3NDIzMTgzODA1Igzic9JdKM5LJFGrxRkq3AOHI5O75gphzOArejpoNZS7c9JXQW7NwwUekxcd7EnVLepk%2BkKKN41zJ8yDhiN2r2zCFHJx8g6Xgvcz%2BOSdJt71FKECvp4DCm%2FpaE%2FBTcDxGdPvb2nQWlDmTJ1PPWJGBRdIRcYOmq2YtddTd8PUwd%2BL9aYVU6E9aOMHswnpq1I4Dd4aBtA7GdBq3buOZMAUw6363SZmrmIciKOpuaUMiCNYaKtJYXnUB%2FL1K1Flh7hE0XfYb3Njb4dYTbAII1xsF%2BtD4SFP3EE%2FiQev56MN0310V2ajNLUh4rBfRXwV9%2Ba69t%2Fi6x4k3RMrJxQBwC33FH0GCgr9pW8%2B3SCuZugEzWNBB6yjaBWvYsmQzYVMbiTYt7j7DQUTpv%2FEznRtnvhiXDpHX8fRZLEr07Jazro0WOx09my1%2FQrpILICZ9fDRtIkT3540MAZ%2FpAeKLZj4rMNgK2of9FTO%2BpGN0Il4MFwIk9zHAHrnbWit97FTt52Gh7RaaMPM9Tqw88l0KAQ1eo7zxREWd1v%2BYf9bRlujtmsETl6XiatWLAvB9M1MzCtxXUcHTNRHLoS07qGliHdEm%2FmX5acttFWi2VHlwSlLYa%2FRptau765S%2BXzvgWKO%2BcaQk0MRWUR9%2FtMyEYbxDm2zDDF%2FpPNBjqkAV1hFSnfALiFNAUglalJPORQQUybSg8T%2FupM9HaHREC3lS5qZIreLsaBHFSaCuX2iZsj%2Bjqb04yJADLvTERf7P%2BJkGUH3ADuNv3YEEKaAqptxDLiraI0A1jHYFsilXoxwWhu1W35NNUNQmuBxWRZcjgYVG8Ac4%2BntKp3%2BF%2F%2BnIHlW4JF7jtDWsnnOVP%2FgtmekqtAdDY2qyjsRLIAhsXd9wV8JxhZ&X-Amz-Signature=545c5d3cb3abc516caf724bb44112d48e5ec3fd24cfa4e75d3fd3b9cbe9ac400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



