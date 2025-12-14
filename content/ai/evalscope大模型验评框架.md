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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKSKQQPX%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIA1ahWDdqGTnAEly2M0pt2FIe%2FehYS9V5vnjNfGznvZTAiAfBgpVzpmecE5%2FHgi1jcdVxDBFtVApFJqaSI4%2FFxRcGyr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMlufxqbOBTB2qwdYIKtwDnQ%2FWpEaFMoazxBnHUevfIxcqQRq%2FnaB%2BWTsgBBns9Bl1nphXBp1yHDFEchf86iwYtVA%2Fs5CskN4YGEFSBz%2FzLljPNu3%2B0zEdiyoUAxF7%2BUimbInKdb6asDTwSQll0mq1lGtfviRlb8tJXXhDUC0%2B%2FQICH4oXN%2FWtpnFLrzhHQ1ZHbmWe8WjSYUpenHwr1UlrOcCoZfxF2j6Lhv1SKDGaGMRCoyt1ZT6T6o1S0Aw0G7MccucveqVvlXYYqdUiti%2BtP6VhyXrVFv5A%2FAWUdCJVta3xX4jcvcQsmLX86MhS6d%2FCnD8x9r32LTeLbdXu9mNjujYAjH183es4w7B2fvEQGWPUQn2jongHeUxHFz3NnOmaXXriQE2anOA%2BUltOVfS%2B%2BN6a8b%2BeEHzyx2MLn4lNKHN%2FR7oyMzJF9LfPhyGtRPJ9cKlzNXsDVLzKu1cHXnujBRNct9NmLF0HmHBjd4g7imsHe72kRWUb%2FIb5ex1TF4Vwec%2FF5LEx5sZ8eVBoJx2FoIKZAFl27Ihg5uPKt5ycUOikyX%2BgyaJcZYHlnyivCrXssQMQPovNu%2Fx4Qt4QALq%2BFa%2FANpiMH2K3%2B0TdbnIc5ipwkL8%2FYiELCnN3G1stJr9kIPT1po%2BISTAuq4wwurD4yQY6pgEvGvguKUsY%2FDzhCiyB7CYSMGPCUvTerKqATbSdDRD9pLf%2Fym7subuiwBpyFWO1q7ggfrp1lUFSmiYqTDTajk2oLcr2OXYDFi5CXQ86MIdtCa39subS5W4QP2wavzo%2BxWXwZQt59yu5R8uGQkJZWiUUFSZWrXprD%2FOhnz3YYbgtAd%2Ffwp2RHWsgSxrHl%2BIZjH56VCM7eSIx0MwOJPer%2Bi975QQNHQkS&X-Amz-Signature=b990fe576821fffd10e80222e6bdb110c0ec40d9c75153c189ba39f77a01f5e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



