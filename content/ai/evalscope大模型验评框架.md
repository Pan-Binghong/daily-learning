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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627MMH7B5%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJGMEQCIF%2BYsTuU85om1fhKpBF%2BzsV6UbYl6ub4JG5ZtV0U6Fb5AiBR3kMuJkyvL4mo6Fa8KGqLD5ZUj%2B4OkCxMEkFDwreOjSr%2FAwgCEAAaDDYzNzQyMzE4MzgwNSIMrT7PjNIHipIBjwynKtwDOQY4ElWFXNj1F489DsHawMqmo5a%2B%2FWFk6%2BuapCDRxibEwHgHP5Lf%2Fp%2BW%2Fw44J4U%2BUoH9Ej4Pt4Ir%2FBvVXu8qdaItT3vVuVInZbxehURGXqzUF0vo3DvMwkBcyCOWjS7ux3Am4GbfNphFVKOLjATm8RwnCakyS%2FOLcE7y7YkuxgkWxTHsAMP8aZNzQ0%2F6cyEvPB1VxapmGvf1sqHynVkO4O47OPgKmDHSsbRZFDSSqnf2XhaMOUzIdG%2Bb9VONHzz7NIn8d%2BY8TYJXEVOhRfK58TZWcbbsvevQpmYsNK0EQanCZ4uaFqTO2ZMRRIHcY%2F6%2FzNEoJgWupVOM%2Bb%2Bd9%2B2jkVCFGE0uO6OK5TciNaqimZFThA%2FXztitMSyNd6T6TuW%2FllFWjaDCL4N5Z0aiBD50p3TZ0CHCRBPYhy6NHJbjVv58CFkeMkRdjRndPFHQMUHR%2FUCR1AvhAw5Yoq2xvdMf%2BNf8Hp0eTy6Ab2Hml48UN7xp1GeKXaCaaFCgUvOELv0juCqRX56RrNsy9yH8GAgBIigzOEzjNO9%2FNto8UMGlLgwOhtU5Ekp0pOlwYLFHY9hjorj6wwuatT0tQufxv8dvmoV2qHAFM9kSZ24F7AqRFBwoBjZNkbIL6wQZYnkwx4P5zAY6pgEIeXMqoGydA2U4S8Sin3qrR%2F1lzL0ykajYiA7MNF5zUy6uarmH9i0bqVKMk2jbo3y0hw7hTxB71JtNKiIZOpRZtPXe81Clt4x8mQ1n0qPffzvgl2aglnR031dngZDe3T0v2saYO4cyZUwURHBlfOpACRpxCD0yp8vKp2cqV2DAEXm3sYAwCLChJLiQwJffMX67vdToqWZuiHja1dxuaY5O21jZ3YCc&X-Amz-Signature=3d573663d7cd79d10f46d281085cc3af34f7499d5948f248156c2a01b9aa98a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



