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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VFONV4X%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIEJ3nNNJqwvDYwnRSlud9TbY1iUk%2BbnJq%2Bpe%2FPaH8Y4ZAiA0Zrk9a8eYo8nbBjrc6teIX8Z6Dzr%2B9ajIsMhLQw%2BosSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkDaAyrOg0dGxo50fKtwDq6zjkJyQzRZv9x1fqn47BnIdD8P3h%2BP0rLYhLK1ciyNp7gi3y%2BHbKFX%2Fd3Br%2BvgwbyHJJFBJmkbzDSUQ9EoTT5BSsO%2BvyQ0fVnppoZRw0uA80ohGVF097egjCucd%2BTt1cIUVnMT6U5SFN6ndpa5qv%2FdfdH74Bg2p0BLqcloTkJlntwTcd5y%2Fvb01FfSRyBDtGsFO8N8R%2B%2FodxrRYYBmqrQrZN3ecMkVsxg1SS1Yr73sBW1O33%2Feq0KwXJDu%2BNdN4lYfeSxqiaEOGPVjnFjcXwDTm%2FK7Wq4iRDx2bidGMIPn9kmwyCpSBvXyvRG%2Bvx3iDRWYMo470O4DKtshe4%2BcN7gqDxUsaZCIL9Bwuxv8Df0PdFmXCnosRyb5wCeYWorB0dHZ9k%2FchuGiyGzLPKDGZUzJjM%2BdeAA3%2FMIfqPrbgg5%2Fp4uYuIHHDIvskNulD5f7u4ICX4z5kgu6lMjxLSiVTapt57kE6fprdIlLxggvA%2BKijes7fiUnXoK0bqXcGhBxplhBfx0tAympKkoqtjYfX86y0O5HBZeQLa8uvVhVp90blaZEp5uVWYt3mhSrDa%2Bs2OXNu1rw0FQFrAI1opE6eMcLaUG2PzBPwVpnFOKkf18f%2BbvuNUNBtgxyb7pUwvNC6yAY6pgFiZVtWUwnm93nP61YqgEANGYWyKj0aM6RUMcf098OsUxvC2F1kupDxaS8eaIQ%2B9Zt33%2Be1VgB65GVbfTHKH7VG6ACrtJThneLpUw5vnIt9Dyb2F82tmlMMw0ZVd0tR1r%2Btk6B9XFxIMjoxSssaGgoA2qGefLWZVmbKnJhUzO0WLj8K6sg8NpXIWWS6iOyA9mu84xwYlpDSoK2wc52N2NjfWAkoRkqM&X-Amz-Signature=e7ff0abb86e42ca897dd05b2440e809c11698b06c6afaa3a733adff9f4303275&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VFONV4X%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIEJ3nNNJqwvDYwnRSlud9TbY1iUk%2BbnJq%2Bpe%2FPaH8Y4ZAiA0Zrk9a8eYo8nbBjrc6teIX8Z6Dzr%2B9ajIsMhLQw%2BosSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkDaAyrOg0dGxo50fKtwDq6zjkJyQzRZv9x1fqn47BnIdD8P3h%2BP0rLYhLK1ciyNp7gi3y%2BHbKFX%2Fd3Br%2BvgwbyHJJFBJmkbzDSUQ9EoTT5BSsO%2BvyQ0fVnppoZRw0uA80ohGVF097egjCucd%2BTt1cIUVnMT6U5SFN6ndpa5qv%2FdfdH74Bg2p0BLqcloTkJlntwTcd5y%2Fvb01FfSRyBDtGsFO8N8R%2B%2FodxrRYYBmqrQrZN3ecMkVsxg1SS1Yr73sBW1O33%2Feq0KwXJDu%2BNdN4lYfeSxqiaEOGPVjnFjcXwDTm%2FK7Wq4iRDx2bidGMIPn9kmwyCpSBvXyvRG%2Bvx3iDRWYMo470O4DKtshe4%2BcN7gqDxUsaZCIL9Bwuxv8Df0PdFmXCnosRyb5wCeYWorB0dHZ9k%2FchuGiyGzLPKDGZUzJjM%2BdeAA3%2FMIfqPrbgg5%2Fp4uYuIHHDIvskNulD5f7u4ICX4z5kgu6lMjxLSiVTapt57kE6fprdIlLxggvA%2BKijes7fiUnXoK0bqXcGhBxplhBfx0tAympKkoqtjYfX86y0O5HBZeQLa8uvVhVp90blaZEp5uVWYt3mhSrDa%2Bs2OXNu1rw0FQFrAI1opE6eMcLaUG2PzBPwVpnFOKkf18f%2BbvuNUNBtgxyb7pUwvNC6yAY6pgFiZVtWUwnm93nP61YqgEANGYWyKj0aM6RUMcf098OsUxvC2F1kupDxaS8eaIQ%2B9Zt33%2Be1VgB65GVbfTHKH7VG6ACrtJThneLpUw5vnIt9Dyb2F82tmlMMw0ZVd0tR1r%2Btk6B9XFxIMjoxSssaGgoA2qGefLWZVmbKnJhUzO0WLj8K6sg8NpXIWWS6iOyA9mu84xwYlpDSoK2wc52N2NjfWAkoRkqM&X-Amz-Signature=4931f68e9196c75c9efefdb0c10823ee2df04e732b9756186a0f33c6cbfeda81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

