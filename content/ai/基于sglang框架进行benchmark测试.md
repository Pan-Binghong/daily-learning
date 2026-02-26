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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ENYOJSY%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCIix3MPmuI8n%2FIBG6JutKkyrIqYEPXrmdsgkNlI05y9AIhAOr503e9FVIF%2BUZ4Hie18hC0Mmmjk4McXIJjGSD%2F27w7Kv8DCBwQABoMNjM3NDIzMTgzODA1Igy%2Fw%2B%2BPHxRQr7pVssoq3APXZ4dOb9frIyM3DNfE8kP8cUOPdJLX%2FnY3fQVW46yfHw4CZJhn%2FoGBm4%2FA6stLKb4di3K9Nv9Fi1hzWioa3gjO9NU%2FnPeyPWIGj%2BraVQMY5inbAQaN6%2FivwibxJO7bBIdbdsZU3Iw3BoQXGeXuE%2F5vthjDqR8nJP0sFcKCFGtfYTZG8dNRAVxJQbyN%2Fy%2B%2BYbkytR%2Bix%2B%2B8k%2FvnC1P1FEmWlrMdnsrr9GcawWnNvUObhA8hQYILxrN6kNohq1FEzqgM9MxT0CbCRymRPOpjmmXJraPAdr57fPcglKJcf3C8jbmL2ZzQlbtFigI1JuZkPbecLFi17mTqvXPkyKS6KMVkv%2BK2nnVkNQ83BxnvCgzGnAu%2BiL8muO33UmiG01TCVTA4obywtLvKF0VnqydI%2F1EYUUK7TuDBDIXzXPWbzUY1sNQZd6p3r1i4vrKKCSjVwEkKG0OQwuXEKFSEpX9wEF%2F2r%2BNR5tT7UsfaNQlmJDeFqM%2Bt4WOSHpLK%2FflHt57cFkqhv5EcSci7mZJgjUrgUgoj2q82mEY%2F3DymliZOxCLr%2F%2B1k85LwFcGzHDx5U9%2FmE%2BHqKDbAMSQ2B2mrsLH7rLIF2A583WCumFhF4HmgzkqXsMJqEliOBwP2k7RJ3zCW9v7MBjqkAZ%2BLRYHFgB%2B2NxWHOfD0wr3YkRZ%2F3sCNG6lpGITLREF2dAXgEAmkn3b5YfZnSqE%2BYKcW1zV4Sefj09UzSInbjOFYq5I3tAYYFqTvfF33qUkoFu6rbC2GlmB8bhcdcS9z%2FOcevW88SvrvoAEOtP%2F%2FWZ27Eqh5BC73D%2Bi3HELLBcI%2Fqz0f8G079H6ecH3E7eDpIT4ISzllfjpwPJ%2FfdwO2DPFZTTss&X-Amz-Signature=922c221fb000928a82c170f7973029b18860a98394753e245735c575f0677ff1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ENYOJSY%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCIix3MPmuI8n%2FIBG6JutKkyrIqYEPXrmdsgkNlI05y9AIhAOr503e9FVIF%2BUZ4Hie18hC0Mmmjk4McXIJjGSD%2F27w7Kv8DCBwQABoMNjM3NDIzMTgzODA1Igy%2Fw%2B%2BPHxRQr7pVssoq3APXZ4dOb9frIyM3DNfE8kP8cUOPdJLX%2FnY3fQVW46yfHw4CZJhn%2FoGBm4%2FA6stLKb4di3K9Nv9Fi1hzWioa3gjO9NU%2FnPeyPWIGj%2BraVQMY5inbAQaN6%2FivwibxJO7bBIdbdsZU3Iw3BoQXGeXuE%2F5vthjDqR8nJP0sFcKCFGtfYTZG8dNRAVxJQbyN%2Fy%2B%2BYbkytR%2Bix%2B%2B8k%2FvnC1P1FEmWlrMdnsrr9GcawWnNvUObhA8hQYILxrN6kNohq1FEzqgM9MxT0CbCRymRPOpjmmXJraPAdr57fPcglKJcf3C8jbmL2ZzQlbtFigI1JuZkPbecLFi17mTqvXPkyKS6KMVkv%2BK2nnVkNQ83BxnvCgzGnAu%2BiL8muO33UmiG01TCVTA4obywtLvKF0VnqydI%2F1EYUUK7TuDBDIXzXPWbzUY1sNQZd6p3r1i4vrKKCSjVwEkKG0OQwuXEKFSEpX9wEF%2F2r%2BNR5tT7UsfaNQlmJDeFqM%2Bt4WOSHpLK%2FflHt57cFkqhv5EcSci7mZJgjUrgUgoj2q82mEY%2F3DymliZOxCLr%2F%2B1k85LwFcGzHDx5U9%2FmE%2BHqKDbAMSQ2B2mrsLH7rLIF2A583WCumFhF4HmgzkqXsMJqEliOBwP2k7RJ3zCW9v7MBjqkAZ%2BLRYHFgB%2B2NxWHOfD0wr3YkRZ%2F3sCNG6lpGITLREF2dAXgEAmkn3b5YfZnSqE%2BYKcW1zV4Sefj09UzSInbjOFYq5I3tAYYFqTvfF33qUkoFu6rbC2GlmB8bhcdcS9z%2FOcevW88SvrvoAEOtP%2F%2FWZ27Eqh5BC73D%2Bi3HELLBcI%2Fqz0f8G079H6ecH3E7eDpIT4ISzllfjpwPJ%2FfdwO2DPFZTTss&X-Amz-Signature=4fe62f4d644397018a7564c7f4a5461c36d504fa5b6a8f7b7ed555ab3a3b8a9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

