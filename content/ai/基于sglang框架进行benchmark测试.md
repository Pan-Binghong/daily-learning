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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674EB3TAT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHzVt6CbAhW0k29JeWtB5%2FLWoXFaZtTAe022jESBSU1DAiBwzOrRiHj0896wJyVICZSzSPYtJDb8w5U6yoalYrLPASqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2zaHfi46fWMdLsCGKtwDvHLeRZd9cZNhbA5IVkJ5kdGZPmluy0v5QU3feaUv0U7KG961z%2BYoXzZf0itnhLjf3GL5bvo4rUHz0Ut2AtOINl2nTazO8Zm%2BpagDC1Xc0DD4t4ekkiFJKRpqObR%2B8drDk4E1OIAo4kj07CciM%2FxhX6vbZhfmMJtPN7rw62n8YmYtaG8Z7YTB2ZkLrsQmhyAAiAT2U8kM85Ti5%2BgoYulHcaQ2PCqG4txThxt%2BNG0%2BCs8qLtPzZvrvfgkwtNTp6JOehIbE6H90UQVYjTb3LMrJqWmKkYMd5M4PRwoSek6483dgxFAC1QpSvJiiiKmCrBWRGsjA8Bib3FrfzvajLki%2B9bFlGL7KJsL1R5x4wPKY8KdyzkY2YDSMx6PevYm67t5JcVTma5%2Fu6jHEd6FMOCY6dKVswNmQURc3hKAoE9kXRm2yEMXPC48VDi%2FZDKv0QrKLKte%2F1L42xrPM8%2FoCwNxKJB0UipZt4hfXWDWX5QhCAORDrWSMvRYIvx4hxyqndjIKHMx55FV0SwP9DAIO4NAFGd2tozMX7j%2ByOjb1ummeHfi7TeriHRX3llInUMfy9F6Ag0bNSmse0xzVPoqVdq7fWEauS8u8FLwi5Go7ZWTb1gHqgn9jvK77fc0F8TMw5JWwyAY6pgGezjOleq7bC%2F2CbTtPYNtmhgAdrSlmYU0X1WtRtt1%2BjxtaNNtKlnMJ6vuyzfwRGe91vSD7isoobYf4vWL%2BFlc6yEaNjDmibd1cJe22YzbQjnGcIlsje4dtU1exZZ%2FXrSovw2UFQMYJ7LY7a2DGJdV5wF6%2Bnwkkxipselt%2FGjeNT1mmEDB1bWaE9k%2FObif5qr12L2htftL8hR7NgXUVrAGr5OIcEiEy&X-Amz-Signature=d81fe46532356aab4205c64f64aad0206d62263bfaa815b2c09b40c26783e16d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674EB3TAT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHzVt6CbAhW0k29JeWtB5%2FLWoXFaZtTAe022jESBSU1DAiBwzOrRiHj0896wJyVICZSzSPYtJDb8w5U6yoalYrLPASqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2zaHfi46fWMdLsCGKtwDvHLeRZd9cZNhbA5IVkJ5kdGZPmluy0v5QU3feaUv0U7KG961z%2BYoXzZf0itnhLjf3GL5bvo4rUHz0Ut2AtOINl2nTazO8Zm%2BpagDC1Xc0DD4t4ekkiFJKRpqObR%2B8drDk4E1OIAo4kj07CciM%2FxhX6vbZhfmMJtPN7rw62n8YmYtaG8Z7YTB2ZkLrsQmhyAAiAT2U8kM85Ti5%2BgoYulHcaQ2PCqG4txThxt%2BNG0%2BCs8qLtPzZvrvfgkwtNTp6JOehIbE6H90UQVYjTb3LMrJqWmKkYMd5M4PRwoSek6483dgxFAC1QpSvJiiiKmCrBWRGsjA8Bib3FrfzvajLki%2B9bFlGL7KJsL1R5x4wPKY8KdyzkY2YDSMx6PevYm67t5JcVTma5%2Fu6jHEd6FMOCY6dKVswNmQURc3hKAoE9kXRm2yEMXPC48VDi%2FZDKv0QrKLKte%2F1L42xrPM8%2FoCwNxKJB0UipZt4hfXWDWX5QhCAORDrWSMvRYIvx4hxyqndjIKHMx55FV0SwP9DAIO4NAFGd2tozMX7j%2ByOjb1ummeHfi7TeriHRX3llInUMfy9F6Ag0bNSmse0xzVPoqVdq7fWEauS8u8FLwi5Go7ZWTb1gHqgn9jvK77fc0F8TMw5JWwyAY6pgGezjOleq7bC%2F2CbTtPYNtmhgAdrSlmYU0X1WtRtt1%2BjxtaNNtKlnMJ6vuyzfwRGe91vSD7isoobYf4vWL%2BFlc6yEaNjDmibd1cJe22YzbQjnGcIlsje4dtU1exZZ%2FXrSovw2UFQMYJ7LY7a2DGJdV5wF6%2Bnwkkxipselt%2FGjeNT1mmEDB1bWaE9k%2FObif5qr12L2htftL8hR7NgXUVrAGr5OIcEiEy&X-Amz-Signature=bedf046cc9f4dec6baf9b9a574026b5c195895e0eae24de356f48a8642169e89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

