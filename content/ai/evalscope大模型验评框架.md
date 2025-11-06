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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT2YBC5I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArWx5af6xyx%2FLZl02FvLZL3GdTNxw6vdlSPQxt0erzcAiA5GWS9escsax4MRa%2BdFOXtvHVm0L%2BD0WWzkpXItua5GCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGTdTnStqFIzXpYUQKtwDUiditi%2FY42jVyyrwhGimG2o%2BhGf691Iemj5ELZ3Uy3%2BXokmfjsFVvv%2BZwcgRFWs7DAqMkzUsgZB7hs%2FaW55w%2FEUu%2F8MqIgtNFTbsEmxv3SHCKOU0uM9TngPK6wxpCwgcyk1kT7TLvmNs46ocRbKP9t2Yny5tQvg0pAeHua4wWaOtKWBejSZxcrkcQOU4J49s61ogYuwZHkwx%2BaTOpUq9VLMqcnNJqVMSSnUmwKA6edfDCV2y4T24RaAjfLMQ3HNcjYT9tdJ%2BOoPyhLA894tJMj56zY%2FFQQcVc%2B8xknpP%2BdO9De1LMcUidgcj%2BevKZGOArjTeTmKL97ZUHl0wfC8%2BcT%2BUqBgKNNeIr5xCvSqePR8iKf5GinHQ5ZA8Rw7sKfrD1lnIJ36M2uspOTSYmf86FUqz2xMbDhZuy0AIlRHgSOLO2Z6BrAw%2Fy0ixEDoiiyV53sSa3cygJULT8DV3RC0M9wk%2B3Id9Mp8kAlqVy5doXFCb8oMMlWJ7eRn7KxjgvuzG%2FWegcMpCE2Ps%2FUSM502%2Bv5btPE9fOrDYXlDA3%2FHr%2FvtRouFKK3DIT%2FOi66ANe2Fsg4PIVYFkTf643FapeiXUKs2mN6nO8k88%2F7kfxulEo9e2lidWD4Bo7aF%2BYakw85SwyAY6pgGdnRzrGl%2F%2BlJkVVM6hjsp7LIGj8s1O9siv3zwWq5MbPKQ%2FsSY1KVQc6q%2BPMIJ6%2FIkSL1STKBoatvIQMzLYwngTj0rowQ%2FaTIDjqlTuYDTymQBqB7OyBd%2B4q44Il4bLp%2FNiHxS6aklBOowsMF5r5tOKH5V3mI5QYAgd0GgAT%2F9y1M6CHumf1Pt47zYgRrKux9fukBeX20EZTPvLZEZ7fsNeIH6x5Slt&X-Amz-Signature=161105c4aab5740d0cef40e1b574d040f18bc1f8ed5b57352fd6b64e96a22ce9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



