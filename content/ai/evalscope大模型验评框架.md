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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VU34IP4V%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIB8KxIlSYnkonNrbLjz5aP2U3uKzbK%2FRzzJ9tzF%2BBM9SAiB0crbU5rDvOx3DVvqF%2F4rV0TUU7C%2FT%2FuO769IPE57TdiqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLXNdvaCe2En2LGZ2KtwDq4iNR936nuThLQcHSW5X10uIbK40CDlZan6OiddXXgBjgxQLY2uFQ42PSMheEqMt2MQrU1I7VjILfHxG%2BY3yai70ahPehSsJGKCIEn9%2Fwkl0WX48QFVilSnTQfjKpCj%2BjEWlLrIQiLrzF5fnxsCRaoRLEa%2BVUxa5NxPisKVW%2BqiiBSz8DL8m04q3xiulh956CP95Vkkx0uh%2B%2FyIVv53ox8VNI3DbXh7jeWPXT%2FrX1zAqgOBzolhP8LlxIwdz1JOBGHYoEePwSIs31ykdExEldHN991uoOxc7FkDetScowUlt%2Fc%2FnvVKNQc0QRy0wonTbiywDuprdbccQGOdOqNbzGSdJiVR5%2BhDNkYjFfe5oq%2BV6Ja0cbvxukHfAS0tuPbsSsOKGVmraFrXJcD%2F6RKMI4zgHQW4yqHGiY5lYThszXhxANAEGE0ZM8dynjWmmfGit6bMBupwURQuRvADIhvV1dJ26X3ahV6PpBOQ2Byu2f78DPiqc1UHpCt%2BaSntZD%2BwDkTKyg6gX8xK6gUzycn2ek9PESZEXrYVIJoEqk1LHFr%2FBxquqJCvpev0BG9zbTyh9186CoFnhhEApmHAESkm6HhZgowwjy%2BdM6FBxGlMPQY4mv0p%2Boy1aTGmnTigwgr7dzQY6pgGX98KOGyW0ctVr9ZK6YJAgm%2FjvsB9avNxC5y5qVzIeDZ2DHXyANaX00d%2F6EU%2BWZIJNaPyvI6U1zod%2BCDn5reLb4AYGTP%2Fm7KfDVjkpjFvYCx%2FITnxmuzUN%2FRI9Ul5bZQR58eTVx3nNHZHzYtAZxECTRWzfdvUuGFR2jD65fxCdNYjDbXTA4%2FHwDt6zsMmgurN4oJuX9CPU82wM8NxaU3MR%2F9u8FJyQ&X-Amz-Signature=fdebc85fc9a4ed7fa949d83626bfdec448320cbb490d10a436016ea93d2f3804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



