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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBI5PFIZ%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025701Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDzz9%2FO5faRzKQ77RUCz%2BE2XpLeemVoYKE3chpST4aK8AIhAP%2BMA5%2F8ar%2FFkNNMlQjMQAtHAdGJL%2FBRhp3Ajl8Sjo83Kv8DCDIQABoMNjM3NDIzMTgzODA1IgwT4CL59xXcN5k6XsIq3ANk5EVpgJ%2BwsLrRf63%2BPOotQi%2BN8oP4XephN7ycC%2B98gDbRFKQqu0%2Fz9gU%2BZ5JTqnAnfE%2BAEIeU43lP9OA5L7%2BIFIUneKWug2VN13EO%2BJuR1FbcVvdN%2FrDL5wwHzFp1AhXhxGYNIeAjRlnMhBdDktulJ80tKn7NCtWI6c%2FfO0086vnoSi32ZStC8rMS0BQUn6zAKKIpNzHdE%2FQy6t6wpVVJ3bXYrchPDyXk3eAGiDNje68oRmF4AwFQzhOorym5xf0TDdiZs5EOS2aZF8xK9skeFmf%2FPBcgkwiO0ikYwp1njY5KnuFs28CLFpeyOWY9qHUTHirhN2baYmk%2Fbw8UhYybe0PgkMyRVgbzyNIGErtOL9pRlZukjEXaNvpLOSkeSGjTmHp2eqFUtimpJvJLOy%2Fdh9Pmdxo5RRLAHnpaImr7ZiqeRiGO0itU1p%2FkI%2FRSWiIyvXPKPe%2Fjk4gM34zXGbrG4qiU%2FdydsQx%2B32gfp68bprp10sCWv%2BsFbf6LyOE1S07vsI%2F0tleoJ6bM9D6UtiMRMcbDasds%2BiLTeGHhPAYOx6Y0qAXjE1DkBgLXlkxitl3HeunX%2B4mx9qkVmcCvBbwElTzK6OfQbh0g3d29u%2BA3Z9zzKfcgWAwUjchrVzCBn7LKBjqkAYVGvwAG8tggvqc5gHS%2BLPKfUOFAKmlrYVwIsRUzdFxg3iNyPoA8h0DzaYJWpTbcZ%2Ft8x9751ZQkfkBnbwL%2BzzBQt5j%2BBDAYi6q2ECt0PImi6soI8t%2BbA3YoQuR8ae97z6MSyXNB8Mw%2BzoBzBy%2BRNE6XZwgkd7Q%2F%2BeVx83dnJ4xXhgnuW%2BVcSnKZxhxm3mkbVN3mVAjBNVcGz%2F86f%2FL0RxNdHIZX&X-Amz-Signature=be03334ffc7a40ba48c51a6ffbb06408ec515a40e64a67a20fdf85bbbd531e12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



