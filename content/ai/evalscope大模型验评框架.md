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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYMU6VNQ%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDz5JxbFO11ODZWwu0N2fSZ5pEgmoLYFRsEPzKg6tkymQIgOg7qVGhdFn1gORCNp0DBXi%2BSROo%2B9CfAYXrppsvGASYq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDIHCvTMgkH%2B43xNlPCrcA9bohAMyV2HAibcIAXxbdZ%2BiJSv4jQBlgnbiTjIcfHP%2FNspwDUrtzoiQYDcSQTRk6P1Q3rMpRLWWoNvwYhTErPZ0AY4065JC8YBaK5AzgN%2FwbWCe%2BsUXmaT8e%2FP7EccoRZaRivJrixyvGxCdfcQdyR1H5BhwTvqiSl6Xg4eaeWkMGJmwl5EJxOlfJPXdsG8TEkGSrXabY887WAsaicqhydPjsry%2FayFRPepbycDBQ5kCAny7ltKLOqNhyavr39aeuinI9VNLUQKmELfC0kOuqf5%2FdM5uNDRQtHjtYR0Z5taq6dP3sCQSWY3cbId41oHdkVMcgbmpUmRkXB519B0XfmFO6cvI2xDsxpchN0nNtPun%2BADucQIpHjzzkhRFyGpXqT%2FObuyjMbXojiTx3Hi2lYKXuHBkO3HoAAmYA2C4HM08IY4rD%2FkWfHvXGdD%2FVSTZNCebVIZVaUNqw48NIl5V1CyMDcY8LRh%2B6Q8XLOh3KLD2BUW2lkKpRkij0ppovHgHEWFb0wP7LhvQKQwQlXFGa%2FCE8q3eT%2B5P4rHPFbUPTqM55KBI6kSCtgQATQg%2FHQ0Xn0qQ2%2F%2FbKw220NZUFt6fiVuGGr2VBT%2BoMQFTS7NLBeNF4W5G4Hf35zWBRkjgMLOP%2BM0GOqUBdnccZplqp%2BDI5yo1O8nxkgP9GsrEHmXCOP01lCzuJQr43JAGh8bcLQRMPlLGw91a9W9YvHX8ax8NTnBodfS4wl996OR6Nu7ooP9Si6XFY048dU0LWEzAzf0OvaoTgXzb5pVLEdspNI1MGtW%2BkN%2FvNFhkonzIzSsvPfcTvK3TUTKMuHkzUlHXcIeXpw9bo%2FaC8go0DnrXSC4jKffswVCcaAheHLKM&X-Amz-Signature=95e9f38b02514050d54916ac118bb1ceee33b16362fea69a7bc33624f68a9bd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



