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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OYNYSAG%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDY%2BwLmZ44PeCKkJxbCkVNtbk6x%2FT0adJpzYTxPAl98ngIhAKZVf0ACVrHEdlHx%2BGAEB6OHz2dAAD4NavBcu8wFNMikKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgypvREcIyQg4UIhcwAq3APltAE%2F4G4aonYTu1GIygIfsF5miI6TzTIhk1TC6%2Fl96Z64xUo7Anz%2BpBDqbBzMVaaOVpq%2FzIulOLkmIAjOjheh5YzyZCkUHmPYfPUQCQKrDAljv9uVMX87qX8aN5qGetC4vKjFVq4jju14v0w2x%2BnK0a9Oi%2BGMW%2FpEVhkHm%2BaPputfGGnfUfHTxi1pkqjPCERKekp10Ktpk2WOG2hJ4JCa4sZdNrscmrfSy2Mm%2BXqYjfHIYxVEr9Q93Z9MjDCqfC3%2Fi4DVPclgR9KXiF%2FOMk%2B%2BKRw1LcHNMnil8zcwVBBCAPGssBWcuka3%2BC2kvvpPd0acMO%2FJCPm1Nyzy60IJDyeu%2BO5oSKnMM91d65w3IK9An%2ByerCk0Y6GmIVijN%2BI8GI%2BAZskxbty3ZBIWzEyFEw7ycn%2B0tAcZo3Wbt37lYJVa8ufXSyS%2FwTE1phR2Pdv5wDqSnDCDpABihscK70gs%2BmGZdoFEJMntVj2gIzp4Bmv27qIv7NHBnIty%2BNmGa279%2BvKCVnJffzAjfRpHJLqAsWH8dudWaH5dUsMS1Uy7b5HsCgfmmVe2dVRaeZNSIcIhrjYkxs65iTDxTlst6zvuBOaQK1vb2U0upjNRI26Yc2vLfHeAV8Cy%2BbMlmvfkOzCz8q%2FIBjqkAVl0xVT51CI2jQcK4BcPiKsWgrD50q%2FWMgyGRNcBqQdn142q579vFJXLN1C9w9F6KsOKi6zaecsl6Dfkw3S6vh%2F7tZF4F24zp%2BP5Bqtm2oD814xmE%2BqEbUv0ju%2Fkp6oUFwN6LlZai2iHxZnzN%2FpSA3IsCw9cdfGAVMZxIjvc7gRdjfGk7PeA%2BrlWOiZe7mXE2QLAnIxGLMvBT7MtEFLT0sBWlv2T&X-Amz-Signature=79bf35fb74fac42deb902720c0050ffa2a05d0114a8cb5dd8e611c8910b87674&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



