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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643MXJCVZ%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQC26jaPJGehEohe7uaxBrsWO6pvWAUtpGNgiJ%2BGIbklywIgH8pfZu3eBBE57yPlXQJ19rHmL7Xw6FqsVgBTbNduyAMq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOMpr4Nrn0a6dTYOXSrcA%2B5MQIqEYfRtwZWiVw1LZKAMPbzCv0i%2BxWyZqGI662WP9J8gLJeYPnUjZJdhxizhScGxMhLtXPNMpMZWib%2BErKzh3t%2BhUxAh2Um8TAB67LWAEZgELB17T%2BLD7ZyKLRYcPWAVt5y7fmXC0sIlLrb5HgnjEpASKIe80ZgJq31x4D%2F5%2BnF0NybhtCxKRzzubZE7aZczQDrK8rxc%2Fqvxki7XA60goNIxWgKckkQz6zJA1zykvDkzTZHqiGku9w0BmLiOTmFqPjSYEbo7Pk6qS0aM1rhY%2FRIok8iECWJrz%2FIxbWqXR%2B98zPTrrcpiKnwKQW9BY4GsZu7vLuQaJhKxcCU9S0Ar58W5vgswh4HYbCbzzJ%2F1BBe%2BijTGs159TEan6dEwzySVLQM1KADvsQcglUm4jXrycK2dv7PIRgFwwNl%2BQ20YbQpL1%2Fnd%2FypwRYwgLzmkrchZoWW0%2Bm8SmCWrjwMvK6TSH8%2F74MgoyPDsY8SeNCGjUCJ9eq9W8vc37wtXFB5XDTAcXoK4YpXYr%2BDY97rWFcSy4Ij4WkTAuH4oJSFQrTAder%2FH67CyYrcIZwOtoe2hKSCNwQtgWGWInBMkhORuYJ1lZ8fi%2BHbqA1Vu%2FEgD8YlkHR8MWXRNs5i1%2F2zmMIrop84GOqUBgygTJaTQvNT63rA4sMLB3qBue0SvG119ghXwwGBNOE68T2ulBJjOiVzxGS7XvbKJfp56x9Ba0zmKprLYaIGa6V7GjMKy30tieopfk8s%2FZd1E4UX26aoLM8vWewzeAQFkIHWvsl9rbw3054DWBEws7aAc3SEkU%2FGFfDqSxRLvo6vDIOZxo7krhE84bZt6R36c%2FeeG6IGvNuUjv%2FKEI15EDmYY6FnV&X-Amz-Signature=4211bffb7c743aa9add6cacaf03f6dd508145b7663355d6f31e6e6606f535a18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



