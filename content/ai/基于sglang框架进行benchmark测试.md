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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XFBOE7Q%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTsLF%2BxdIza6ugYc%2BJLLWOKza3he31OvKdGo7p%2F8clvQIhAKEsRLqZ0p3NOSvDE25Hcat2MohPCinQa%2BHgWLilTifAKv8DCG0QABoMNjM3NDIzMTgzODA1Igxxh8B3HY7CIop8BXAq3AMAlP757yKcjR6dHJg3UZEOOT25HUK1rGhWuIlIN67XvEZxbom93aid9C%2B9Tr6A7sa%2FFTSrkE4vtPnladK0cb6uhJejamxOy7q%2FZFhsfBHzQVbJNKcTnI1%2Bb7t8l9PuCQXLTbUAgzOrZ4Inl7y2gJmkaSi1o8zCdsLo88Joa3v4q%2BLczNYPTMz0gDUTctThXfZm3EWpRdZAaBxIIxkmGE1Hz%2BEyI6xLpr3C57R4xKjv1Aseki20MlSTSC3B0Eofg%2BvJwDXRt42WtVcAtby6CBjnvqIrtJcMadt1p5LYqdUIMFJq1988rF00sMMgvpl%2BmzAqBs%2FfEkZHxb90R4MauofY3C%2By78Qy4bT0Lthog3bqpjJmethe90L59p%2BYYERZN0PFCXLKwBKLAE4POBkvjgrzUUwCCs4Zw%2B8I9B4s9gTCDGcjZ7%2F1glA%2Bdx8GHPNoIAzH4xcsECVJv3H87drQ%2FfJnCfY317GWlB0vFkLME8J80Z4UxMp%2Bs0zqGFTEbfni0Omm2Zf%2FWx9ypQlEpazGkh%2B6k18VQGyORpxi6YRjL8l0mUpbHJM39T%2FM2Vr1PWebUNl5plXCJZ4aay%2F8mqn5ysBSkUZmu9ZlH8ODISYQ%2B69iQ9YuKiJ%2BbMrDr9vb%2BDDSi6DMBjqkAaQI%2BMy5Fi78O0F8C9srFzBkEVlz5phrQZF0J71yqBPog%2F2y2ZZNYWFwf1fQzwxVaABzmrGV1k%2BXJHA2IrDIv5czpSuObgbsy6NdWSf4s52fXF%2BWE7d3zfGgFEBqargI4HwcN%2Fx1AMjuW%2BFV7tLW2ZNSPFVkW3ZjziKynILuiivq8F4YfZPs9dvXqoH6QiGYC3YRgRHO04Of%2Fecb4WVUUocJI1fA&X-Amz-Signature=3142fbbc9afc4c69d41958f34f96f59048401e6236aaa0165f0eb04f8f76044b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XFBOE7Q%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTsLF%2BxdIza6ugYc%2BJLLWOKza3he31OvKdGo7p%2F8clvQIhAKEsRLqZ0p3NOSvDE25Hcat2MohPCinQa%2BHgWLilTifAKv8DCG0QABoMNjM3NDIzMTgzODA1Igxxh8B3HY7CIop8BXAq3AMAlP757yKcjR6dHJg3UZEOOT25HUK1rGhWuIlIN67XvEZxbom93aid9C%2B9Tr6A7sa%2FFTSrkE4vtPnladK0cb6uhJejamxOy7q%2FZFhsfBHzQVbJNKcTnI1%2Bb7t8l9PuCQXLTbUAgzOrZ4Inl7y2gJmkaSi1o8zCdsLo88Joa3v4q%2BLczNYPTMz0gDUTctThXfZm3EWpRdZAaBxIIxkmGE1Hz%2BEyI6xLpr3C57R4xKjv1Aseki20MlSTSC3B0Eofg%2BvJwDXRt42WtVcAtby6CBjnvqIrtJcMadt1p5LYqdUIMFJq1988rF00sMMgvpl%2BmzAqBs%2FfEkZHxb90R4MauofY3C%2By78Qy4bT0Lthog3bqpjJmethe90L59p%2BYYERZN0PFCXLKwBKLAE4POBkvjgrzUUwCCs4Zw%2B8I9B4s9gTCDGcjZ7%2F1glA%2Bdx8GHPNoIAzH4xcsECVJv3H87drQ%2FfJnCfY317GWlB0vFkLME8J80Z4UxMp%2Bs0zqGFTEbfni0Omm2Zf%2FWx9ypQlEpazGkh%2B6k18VQGyORpxi6YRjL8l0mUpbHJM39T%2FM2Vr1PWebUNl5plXCJZ4aay%2F8mqn5ysBSkUZmu9ZlH8ODISYQ%2B69iQ9YuKiJ%2BbMrDr9vb%2BDDSi6DMBjqkAaQI%2BMy5Fi78O0F8C9srFzBkEVlz5phrQZF0J71yqBPog%2F2y2ZZNYWFwf1fQzwxVaABzmrGV1k%2BXJHA2IrDIv5czpSuObgbsy6NdWSf4s52fXF%2BWE7d3zfGgFEBqargI4HwcN%2Fx1AMjuW%2BFV7tLW2ZNSPFVkW3ZjziKynILuiivq8F4YfZPs9dvXqoH6QiGYC3YRgRHO04Of%2Fecb4WVUUocJI1fA&X-Amz-Signature=8b870b4d7ad5af425efdb73b9f28b9a9f02c48740b963965e9615959695549cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

