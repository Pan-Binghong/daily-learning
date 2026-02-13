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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZACAAKCW%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQDJRVEK9Ug1ZjTukzy%2FBlGaqamAbrT9urEKn%2BTCtxvZywIgT81umumSbIOd65Sf8wFEgq%2F0ByJj3RouU6ES%2FcLyt0MqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIop7Tk1xo6jb48oCCrcA9gPLq7NtprgTVvIQ7rXLPxwdT6AaB0rjmnpo%2Feqqis8uc2DBS6i83vahkevnxjAkVstwY%2BEH5NgX4btPUxCYU%2B%2FFE2IHWbNIvKhAtVaUEAv64sHoAkvqj65nli5V8QQxEDAA%2BCg1dYK6J0fU3X9gehkw7Lxt%2BPrbDxStLDYqM9qE6gpx1z%2BWInxZPnRsN1t5brMIUU8fcTYd%2Fk30IZHcbddzByQHxkbVMALYBPsMwyjhsF8sxrZgHYIQFbTla5QSFS3Yw7SkZb9lVwISfacf6xQ%2BB7Ytnx7g04Fy8Z3yBTzOp7a9u4uWxqBv%2FpH55U5X8OLjVJ9xe96SV%2FWAReRwdvKqwxtSQCS6jbl88Ml%2Bq8Gg5I%2BMVnRnx3A%2BsTqy2T4i%2FDfqXE4pkWpM9HCMC2mW050uZkYAinH49m8ESmJdi4XEeWCDBgrLUmQ%2BgDvrg4MB1G1gh2VokfXiFXTvImYc5l%2B8l4VrR4pKTnSTV4s%2FCL28Sip2EQ6hNFwA%2B%2FNLjBRdyi3Cnst4ydP9OwIzNzamYn9afM%2B9MzIYPX2D%2F5Q0C4V1a%2FV5QPs4SbiWSJ3H%2FslUryg2PYGPVnQI59gzJ28r8sMbnqkNCmBQN7fExm0U%2FHVn0bfntDEZWPzAnOcMIOUuswGOqUBuq6rb0PR61Egv0XPmxaFAe%2BSbwkMhKUBVidWdClOhmIF5PT3ujGaPVT7astuMPNYXTsslMvU%2FFQz9nokMlhDEAYKQrC4gizWr296coaZP%2F%2F%2FVojqSLa8Htw6SG0GV23XsRNLaL4Rz2n7po0oKLdTxC8XNh68YbyfyIu%2Frz5zAeKupkyELh6dhAE7PNJbloBiHY5i37owFfHqrU5MmG7zR9YVKkWE&X-Amz-Signature=6ad489f0ec5e23c9f6e856f8824adcd1b3c18c15acd5259f0f6c4ecea85c168f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



