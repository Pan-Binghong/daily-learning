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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IHRJ6IQ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz5g0gkmqFwlBLAl0uyyKCBYZ%2BSzV8pq1T6pmXhrjMJgIhAN7MEzarwcwYTfPJeaCn5ee5HVjAWEGqZ3AHU7zUvcLVKv8DCHwQABoMNjM3NDIzMTgzODA1Igz86kNIqzUgK2bxYDEq3AMHlrF9p05bnXrdE79UkRbOYHrWC%2F0uYNVCllOcB3gDUzqmswbqZd%2FM89hQYotoRQCLUopJ%2BootK2gP%2BvYGTxGg1QenNrA8KF1hnfqmcwgnoviQlc5WFzYzJ%2B4sU3Ylv6olq9n7P9rl6i6bGn4fyrLDzzEhmFMNMGRJ2Ad7soHqi%2FTydDuTkefOVdu68E5ZZfr4kXgbbNj%2BPK7Cjg3Wvl1koEexpbjqBZQKF9AnGMlWfigCDeA78ev2KQJOkXnk44MgqUaPdz8rE8SJac%2BamZFXce6Np8Ans1%2BfcASNPWti9uGaBxAWzQD0aNkc2IfOYtCwPxp1uZIBtuZ2JhztRl6J%2FavUovSOcnKTZ24sEeeW8HcxqxO7w7Ao9%2BSrBKoUUUffm1KL8D1YDkvY%2B%2BdQVEXJOwlHfHSA2gFaGvOTGaGLzfqgH1sD06sKkBLvMlfUMqRks4waIDR79KSam1fYa0umrC2pbxN7kXSRilU6sLnLp3cAmKryXcDq3M9IdhnAcO9kPZUXQrYWM6vxd76blfL1Yl2eMj0HN5rbHJVXZWDt8Gj%2FK%2BvdukUpKSQd87%2FRr2nt%2F02Eql%2BUq8AVfcaGgHDVC5Xx5zNztiQi96xcsPbwvyTZTyyV94vyfWIexDDLouvLBjqkAa3D6BktxUc5dliQOQBuU3guaJy9xfvM4Dj6WFc%2BhroIaJMAI%2Fx5yWIPZ0AhEHEIzieV6cMZ8ES0Zw7rBp29LGM9FZRaIrIdplK8CgJ9D4RK7GLSsFhQxup4nYyPMK80bAa%2F9jCeYilsBkyH39M2X1hviPHvAvntHH0DAm1tfnhOQF8kcNdzkNrJwOsJwWPYlJzuW4Thq%2BmUCTOt%2BMF4xE%2BxJPp6&X-Amz-Signature=21900e231bce00fea0653823e03f8ed7c15350c069fda069e609e64038a30d86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



