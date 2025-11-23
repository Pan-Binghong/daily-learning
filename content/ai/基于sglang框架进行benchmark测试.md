---
title: 基于SGLang框架进行Benchmark测试
date: '2025-03-21T00:33:00.000Z'
lastmod: '2025-03-21T02:46:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 SGLang最近更新了，打算重新写一份测试手册。并且优化了一下批量测试脚本。测试对象为DeepSeek-R1-Distill-官方提供的六个版本。

---

# 1. 环境配置

拉取最新版SGLang镜像

```python
docker pull lmsysorg/sglang:latest
```

---

# 2. 启动容器

```python
docker run -dit --gpus all \
	--shm-size 32g \
	-v /home/weights:/data/ \
	--ipc=host \
	--name sglang   lmsysorg/sglang:latest /bin/bash
```

> 💡 -v /home/weights:/data/ 替换为自己模型的路径。

---

# 3. 进入容器

```python
docker exec -it sglang /bin/bash
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSIJFNDA%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCICpP7nR4n8mUCocm3WI198LkbXQrB25FRlYTUi3qAb%2BtAiB3MA6FS%2F%2BukxFz749%2BSFBTU2d%2BG9o7yPqOmvWGF1k2Eir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMTDXzY23Qu2oGxRO6KtwDXOTP2uSf9lbk7MT1K6ughzBnMQVUTE6ycxskYq72juBMSwxpnay%2F0Mf71E7TGC3h1kkHP71WDM2iywII2vCrXBtbNiJ6k4STQ6VSoZTayQ%2ByNM%2F%2FqI7B1MBJCPns8GVK7T6Ots9%2FbdC3DwwwExaV54xc8jrnW1wV1A%2FcByFtQiTKcZhcDqgD5oCBGOXNyD3I2U0Q9XV6TdCkSF1XcFaZivalfMcFM1WPRBedKxAJ%2F4nkU7mxZt6Lkj8KeMYlWL2iGKMDuicXQoYhWBmO5Nqqxh%2F%2BB1QtpHf032Pjd9xjzGhBpPPL%2Fr6amvg6gmJ68asYlCE497OpVwjIwOFYcSazxCUyVWji6X9egDfrP3xK0ZhXyLkt7Q%2FTEAEfw7zeFxY6KiNQqQg7jdh9XfdmBeDKikI96cdusz7%2F85QEdqw7ypaBu152%2Be7SiAFb5AP6nvsCyU1xEOfAn%2FN0Pj17y1CJ6Mak7qBpvRLnlkSEBnG3gsO0h9AD0VgqvpkrfN9CHfhWJUM5f%2BVHAVBR82207NNIYlGwAKlgVsD5UD8WeSOaFhv4AlxZaNtMqAiNyGeTRaAArbx2hT3Mq8t1v316SF%2BHDLdPls9hLtZ%2FCIMgrHspZ0zNSCz6d2QVEregiyEwv7CJyQY6pgGRgI%2F%2Be1dZ9tTCC7EYqkPAAr3yII%2Bs1ErjNxEz77Rd5BYX%2FRaoODXgDkiNnj6tZ0xoauaZepvZUGLipHjja%2F0SWveOj5XvgDoCqlj55D9QjmmQghZnAA0MvzBDu7wbCM5w%2Fp5K9fff5IqFNIOYFkYJ9OPnLDIBqTQbJHPL%2B5P%2FXymaJl6CNTJ41wHX6pl1XbX9S2e%2BEI9lyBq0P81JxXB0j99ByvUk&X-Amz-Signature=74cc56f079e071a660fcbb6ee3db7865cf9cfbc7c5e78f6d2e328a967299021f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSIJFNDA%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCICpP7nR4n8mUCocm3WI198LkbXQrB25FRlYTUi3qAb%2BtAiB3MA6FS%2F%2BukxFz749%2BSFBTU2d%2BG9o7yPqOmvWGF1k2Eir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMTDXzY23Qu2oGxRO6KtwDXOTP2uSf9lbk7MT1K6ughzBnMQVUTE6ycxskYq72juBMSwxpnay%2F0Mf71E7TGC3h1kkHP71WDM2iywII2vCrXBtbNiJ6k4STQ6VSoZTayQ%2ByNM%2F%2FqI7B1MBJCPns8GVK7T6Ots9%2FbdC3DwwwExaV54xc8jrnW1wV1A%2FcByFtQiTKcZhcDqgD5oCBGOXNyD3I2U0Q9XV6TdCkSF1XcFaZivalfMcFM1WPRBedKxAJ%2F4nkU7mxZt6Lkj8KeMYlWL2iGKMDuicXQoYhWBmO5Nqqxh%2F%2BB1QtpHf032Pjd9xjzGhBpPPL%2Fr6amvg6gmJ68asYlCE497OpVwjIwOFYcSazxCUyVWji6X9egDfrP3xK0ZhXyLkt7Q%2FTEAEfw7zeFxY6KiNQqQg7jdh9XfdmBeDKikI96cdusz7%2F85QEdqw7ypaBu152%2Be7SiAFb5AP6nvsCyU1xEOfAn%2FN0Pj17y1CJ6Mak7qBpvRLnlkSEBnG3gsO0h9AD0VgqvpkrfN9CHfhWJUM5f%2BVHAVBR82207NNIYlGwAKlgVsD5UD8WeSOaFhv4AlxZaNtMqAiNyGeTRaAArbx2hT3Mq8t1v316SF%2BHDLdPls9hLtZ%2FCIMgrHspZ0zNSCz6d2QVEregiyEwv7CJyQY6pgGRgI%2F%2Be1dZ9tTCC7EYqkPAAr3yII%2Bs1ErjNxEz77Rd5BYX%2FRaoODXgDkiNnj6tZ0xoauaZepvZUGLipHjja%2F0SWveOj5XvgDoCqlj55D9QjmmQghZnAA0MvzBDu7wbCM5w%2Fp5K9fff5IqFNIOYFkYJ9OPnLDIBqTQbJHPL%2B5P%2FXymaJl6CNTJ41wHX6pl1XbX9S2e%2BEI9lyBq0P81JxXB0j99ByvUk&X-Amz-Signature=82c1a0318a8d77378c89f582a85888d5f6db64cf1d389973b254215b78e6237e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 5. 吞吐性能测试

## 标准|官方测试流程

[https://github.com/sgl-project/sglang/blob/main/python/sglang/bench_serving.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/bench_serving.py)

1. 修改bench_serving.py中的代码vim /sglang-workspace/sglang/python/sglang/bench_serving.py,将SHAREGPT_URL的域名替换为hf-mirror.com 。
1. 运行测试脚本
3.Result

---

## 创建解放双手版本

1. 创建shell脚本
1. 运行脚本
---

> References

