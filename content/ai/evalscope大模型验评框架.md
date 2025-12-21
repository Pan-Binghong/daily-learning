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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVBPSWK2%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIAvTLLtvBS4iY197As0Uz9tsmsn%2Bz3z%2FfX7ZyPPLunQcAiEAzvGQhWqsyBcFi%2FNx80y7SfinispK40qruCw7eHHQInAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDai%2BzBd5apNQqINAyrcA%2BTL8d5KCUj0v8xVqNoUOlzWSHb%2FiRRjzHMj1xSFRFG%2Fy97g46EvioalTzfMT4cB2Pqj3lWRChVCCbVGEuDH4TqqUq9d03yyYo8yzojB5gV1vat8civZFvIMB1SpjObR9gSpD4LBa31oaid9c%2BGKs53Ml6jQql%2FsolW%2BH%2Fzy4rb44YgN8Q7nrmQu7lNbBJ3oCm%2BoucxfURLdhFLzjGtd9sv7sCpDwW9SbCfZp9jjXq5D2rtPIYhmpMOmuvz6s05sFWErnti4A1JjTjg9YyiUC%2BC6IpSvr5q6ZmWbQpmKKZjVAIbVRx8FmnIwcMrHOr4DNKdiMil85Lqso2C3IRhBmTnppFNNHJpq3Qv9n75qIyfCpxwyxPNnhgvnduAw2AQrswXVW%2FhdbX4jgzKb70RZIVAyxRD9JHNcqUjHwuoKWo6kCLSs%2BQx9tDdiLCl4HTb30rHCdTmdiAIXo0L7SriZiRMWQUtBXyIKhMaqDKVNVX6P1l%2Fh9%2FCwIWI4HIIFo7IHyVu77VUzgU5g7n8lduNrL2bIF0bUpqQKtA3tCWkLYQo%2F3rJukVbIu%2Fm%2BJPySG7pnVVlmrF2jtXoJnlANoDrfhyXXcrjQjPG6MeRsOmhSn%2F%2F9H0OI%2BtOS1zB2yje3MOz4nMoGOqUBIaP4M123fucWBPB7fq2Qb9PYDbokaa7%2BkBIwthB39r1RghB646KA59XwScSOeQbX38yT1BubSgjz8NQ8%2BfIZAknQEkSaPNaKTOsOu1dEa3wwDIgczJvHqsifuuZSod5oSdVVcNJdR5j6mu9H8NsJZ36cUiHf%2FmugUUyqamPh71IiHEX14olvUxhnov3dI8sTOI1TW%2Beidrx2i9rhQFeR4dIeUeiv&X-Amz-Signature=c04990cd253e8921946b3828b045c22a54e113e41e40266518da7a9501675ad5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



