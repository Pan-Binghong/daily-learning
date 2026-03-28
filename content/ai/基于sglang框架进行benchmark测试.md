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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIWIPKOS%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDAf313%2FS8bFtx81cj7AU%2BpJXrU4Rf%2FMKWojTLwJwuObwIgP2JhbChJ5QHA1PLureJZqAcL4PInSh5aBNm8wsnnAAUqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJTCqUql9nRVgZ2m3SrcAwzYNYGLl%2Fbd0uK8lotN0hbtsjL0sq0rYFl3BW70N%2B6BXBqXtf4gkXO0mqUuEjB9GTgNx4gyiX9yfZy4rFNdBjgzG8M0qxyen8QawL4z8xc0bUe2uNzfPGamurzvikHXMeHDQVKSRy9uODhUzdqxJqwKxOdXnLFu%2FoqLlcx1Q8SXrrmNMXRLHlD4QUKx2bA%2BgCoNenUPnrIkTVh4JY91bnIlYENBMdUDydzW164e8PTL4VldQoCOc6zp6RdzeKE5UoWRHFIayfvTUwcchsUvAzUUvjQlSBfegJCCwhJPxCfrPvrugrGVFwLNUCBbGMQ9cXWHGlVs5bEKyA0ZhxULaiQWaYG7JKny5GUOVA%2Fjn7Fh%2FAN9ylSZfx%2FD0JHzRlyW%2FQbzd9Gq5L3ghnVfIqvJLQQr%2FyZ%2B3ldMRj6ClmFDcyV8FQYxoXv8046E1ZudJsimkX29PENGzUadQgqAklkTOjL%2FcHaL45MnYgFwQ81LunIvNJuPYpt%2Bh4D6AtUqlmvULH%2B0G3O%2Bx%2Bg8LNy72zzEGxOeOZ3rsYq6BlN%2BWbgbRAXK6suzDgPPAsuRR7jTo3zQwX78t1R47ngimeyIlSkwidNYFiinw1rBlDqBTzC8ovNOUr%2FWqiqNOswm6xSuMN3snM4GOqUBUrTs1%2FlXVtgNeK3lzvlbQLuwhZ78MySnYw%2Bm3TRLfanu6qSbSWlfzf9Fp%2BOqsmbl2IsSxqBIMjYUAUntzYRjUhAsxT3ClUcpEAbvQq8lzxPiIAF6rSsMOQZECchsx%2BAZMdFaPFzhQYA96R2iM%2BqV652jP%2BDMTPFnOe8hFNdKzuayv7BDPp0WmF0aMvbEyww%2BeiDUJ1lcGiMJfjliYCrlikkDLKzH&X-Amz-Signature=968ec3d3114bffa940c2fb09d7b375126862741aa5eb898f2d93723488d041aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIWIPKOS%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDAf313%2FS8bFtx81cj7AU%2BpJXrU4Rf%2FMKWojTLwJwuObwIgP2JhbChJ5QHA1PLureJZqAcL4PInSh5aBNm8wsnnAAUqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJTCqUql9nRVgZ2m3SrcAwzYNYGLl%2Fbd0uK8lotN0hbtsjL0sq0rYFl3BW70N%2B6BXBqXtf4gkXO0mqUuEjB9GTgNx4gyiX9yfZy4rFNdBjgzG8M0qxyen8QawL4z8xc0bUe2uNzfPGamurzvikHXMeHDQVKSRy9uODhUzdqxJqwKxOdXnLFu%2FoqLlcx1Q8SXrrmNMXRLHlD4QUKx2bA%2BgCoNenUPnrIkTVh4JY91bnIlYENBMdUDydzW164e8PTL4VldQoCOc6zp6RdzeKE5UoWRHFIayfvTUwcchsUvAzUUvjQlSBfegJCCwhJPxCfrPvrugrGVFwLNUCBbGMQ9cXWHGlVs5bEKyA0ZhxULaiQWaYG7JKny5GUOVA%2Fjn7Fh%2FAN9ylSZfx%2FD0JHzRlyW%2FQbzd9Gq5L3ghnVfIqvJLQQr%2FyZ%2B3ldMRj6ClmFDcyV8FQYxoXv8046E1ZudJsimkX29PENGzUadQgqAklkTOjL%2FcHaL45MnYgFwQ81LunIvNJuPYpt%2Bh4D6AtUqlmvULH%2B0G3O%2Bx%2Bg8LNy72zzEGxOeOZ3rsYq6BlN%2BWbgbRAXK6suzDgPPAsuRR7jTo3zQwX78t1R47ngimeyIlSkwidNYFiinw1rBlDqBTzC8ovNOUr%2FWqiqNOswm6xSuMN3snM4GOqUBUrTs1%2FlXVtgNeK3lzvlbQLuwhZ78MySnYw%2Bm3TRLfanu6qSbSWlfzf9Fp%2BOqsmbl2IsSxqBIMjYUAUntzYRjUhAsxT3ClUcpEAbvQq8lzxPiIAF6rSsMOQZECchsx%2BAZMdFaPFzhQYA96R2iM%2BqV652jP%2BDMTPFnOe8hFNdKzuayv7BDPp0WmF0aMvbEyww%2BeiDUJ1lcGiMJfjliYCrlikkDLKzH&X-Amz-Signature=2c68a1d63d1f4a5f05d810f67674ea221abd280f6d6c02ef6c9d2799948fa704&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

