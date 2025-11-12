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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQ52UEV%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIBcV7ucZjCFD606xw1%2FtrMSUHbAU5KKinUeNRiuIRSzQAiEAzVyqEZk%2BUxUW7qD%2BvfziKAfHoAIQnWk5OyUXwexiPmUq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDPiOJa9TKeSS32822SrcA7RBs%2FvYBHtG0mCeUYWXI41BbLIiEsALAW4Blu%2BQneLmbrU9lPogxTK07eDxPYITTT6FeZOIxqAr%2BAz2Rhg8OcSXCscHSMJKPtj9DhFrylhwFVsHEVMtFv4AgakSfq8fB1zQ0lMs5tCOwx3SYuRb4qo69HzW1B%2BrAIVXLlQTMJdImHp7hkDQqNZuYDlYsWTA%2B%2FIaM4%2FtSVUaJWRS55xww9fwKHZv%2B0qZxeyeSvK%2BN6PnOe3MEC%2FOJFP2WQU06lMrdGWyslQjJopNSV9aIsmyG4MFSbg33Uw689L4nI190sRI7EWh65VppOI5ML51ggiresTOPhwpxrUrLclMEyL2eO2zmDM79apIvIJQ%2BY9UhpxsEZhekpRrbywryA%2FROexm9yqOSvejR%2F7ILyTNzWSY5pODknaWpnr8cQKcqrqClm9CtLLFEvHbjRxFRy8OQe8rdagtXPHBDhLT0hgsygQBgYNoxfDEIAQsHc6UIYutsaVOQ58IFz1foopOJ2TnDDg5zdkFt3SMYSC1qGRLwe3GqwRkVuT4Ie91%2BNeNvrvXPla68HjBNIVXoltFiLKonwn%2BWpaEf1IA%2Bl2kiLxSgcp4LOA8OOyoCejOOqsMgIIU5MCwxnsymTOhHvTmEWc2MJrjz8gGOqUBBscShSUg%2BdSmhFW1SgK3wH5bpSaeozATKkmsw61YWy5vQFqaH1gyGH2yPLwsJ1hjKFsmHt1aEWUVuenr8vObQkWxOoZ1iL%2BQHcxr6WbCKsMbywi9vN%2FVUVRKttGDwtlfI%2FIq9EYInHaOUf3x1kzTP3VU5F1W26AMPsjlbU0BITpU%2B99YLiKe9dB4DSFOVU3a7wOjk4xJ6Vxl%2FvEHkruhn0nt0Top&X-Amz-Signature=6cdc790e7dcc1d19d156c035dfd87a94ca91c6109ff4383275034c252efd7e19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



