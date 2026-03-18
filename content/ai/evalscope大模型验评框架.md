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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WCFH6BP%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJFMEMCH2KwancDvwqVE1QJ7QrdJy4TdhwwpAPkDrWjFG4hHJgCIE5QRmlh9bIrf0644zEIv1GMqwFanlURb7B4nyZLaUj9KogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUk8hD0QcAzTpCjKEq3APcbfGw%2BJrzhKlJQuzxhSg9fReehKqpZ%2BIYyr6YuS7t73rcDJttalG9dXWnBj7HLoahji4bCRjX4pPUyrhLfeaDGOiYQWYwvPrgaedFyT8qLAjPq%2Be5EikkataDkNqsJXjMZj9BYEfrCa40Pt9CUB5QmMtUoxazifJPf71n23%2BkoHU5om28FTrdtHTr4mYCeWoDM8CqYf4X17nFqvPGKI6e3n%2F6%2FV5IVcDF%2Fm1qm%2FfkAaiTc6gRLFP7exBENhocJHhhoQ1ht3Uc70ttgmVNRXizCH%2FoX6r%2B%2BLaQBiiB%2B40X%2BaTllp2PcgXCQ%2FZutZRW%2BDd59WX6A3pjPlwb4w%2B8bZ0aXwHjn%2FnkGx5gaEWqijWMkEKYUyUyiZDU87dz0JOA%2F6uG0hzEqWOusce7u6fkjOa8ZGIX0gt7uTeTYzRq6gwBCohySTYxpeups8c5xzl1RNJ7%2BRYGdXw0Ze4IcyNlG37%2FAKo0xuSAhCFPo1qu%2F6NrSooocRvJI5ntKi2SqrziYmBhnDKCPEtrV38vmhXNTjT6QKIqZxREEoRWt%2Bo6V4nVGhPFym%2Bm0YWmjYd52N%2F%2FWqs1QFpNa%2FiXc9723AjQbm7R5fMD%2FcnG0gLZt5hbuIjrKPhXnk55WhCC%2BUwweDDXpejNBjqnAbRmHTvUqwz0znQqU7e843UCFCZc3zne%2BrU1J4mDHXVVq8JdITmFVUgtnQRnPND0Jx8wMX%2FNSER4PAzoA9lb9aPa1jNCESFjfuIpChMTa%2BQLQFHQGP6Qdvl087jISVUdlHdjS1n92Pyk2QUzD%2Fqt%2Bjw%2FJNwslsxXGRo4COm2Ka5ksfhhqwWhSDYXb80dLYYYZYoQxk97y0s3X5VXhW%2Fx4AsBqZiYw6ib&X-Amz-Signature=892833210d9e883ac8b5cf88e8863a806c175a9d8a2f6e7562874abfe039c955&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



