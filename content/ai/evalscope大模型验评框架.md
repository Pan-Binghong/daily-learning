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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SIUP5YQ%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIFOSVMyGbriWH9DkgDUVYdiQKN9milXnLmA5L4vvxKAwAiEA70SKAyFVRAPAvHCuzYfK5VAaPNO4FuFabSBk84VNaF8q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDFk%2BXOjCdnCwtDVe6SrcA2Z24FGtryIN0U%2F8Y7duv08p%2BrhoZv%2B056%2F2gr1VnrFVjIZDuIM7AJoX%2Fy8NdN%2FsUMPlETkQXuczEae4faz8LOlf5HL%2BNMhBeKL1ra9cOQkv0VXHH3LLChTHjCXpecM1bhxy6Ce1cmrRtT%2Bhu75aYGyntbh29xMlTBnGSFZ3bvQJFLTEsElDqlg%2Fab%2B9iAqDUH6N9hR32RkIt3FfC6uhB2oPbxHKRf%2FenXYbDwvLNF40JpA3J2LGMMpZyNlAL%2FCf7FYGAOuDYuuhzTC%2BYwi0SGy67SZ4We1jj9qI%2BJYo%2BMpmG1zLZ1WLjVfs0QAUTvQdT5QlxhHYXCDv4l7Q6%2BTQnrb%2BSkZPPK3ixisAv5T6xbm6HQKMVwej4xP3app%2BGonjF4BsqCrS4jdoZIr6N3sxFVBb6QWaC4ZLMT8G8JQKB9QCXD1ftfD5fQt0NVCeYm7W4YKDUhx9N5I8Oqr9x9rQ4runIa29M3GirUBdOHwQZDnRS6j2onieLjioLWYm1E8OlhQYc9boFgaItIyJqv%2F%2BJHG0MqJuVXM2YaeDDRipnIyOT06uJ5fq3gk5%2BSgmA48uDRrnj4WzfmgwvQHv5LDLSdkn44RRE4T9XXW3%2BmRNwpreAS44wt4VapVsafwXMLW%2Fos4GOqUB2%2FvnvnKRe5jBeC8GADdE7Q2ShPhBsIjhXL2SM50bYYjmgr%2BVw7JvQl6PYLbc2u9vKYyhSl7J8KQVByipR8NuK0LQ20oPdybxbyV%2B1ErWGKHhY7%2F3DrBfgI%2BR%2FRT2Q2HRuIS9JHUpcsG8y5eL88xNgMmyVNcQxtR4Tu6xpcnud7QVDjFekVIGOXPPv1zAtuac3%2BZXnTk6x80WPkVzvljCpZozKiog&X-Amz-Signature=547c037b89071e2b2231875e0713e75b8a90e9193e28a10f940a779ced6362d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



