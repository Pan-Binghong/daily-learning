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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EYSQII4%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDAh7LEk0rx2qGX4ky9Q2ByROaarT9sGcnxh4ZExKY8%2BQIgNK9s%2F%2FSuVlwBqxH%2B%2BMD9rtNdjmu55yRD8CsUhDkdSl8qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvHkpyTExpi5w1qiyrcA1PCbfbyfjV4hNOh0NNvbbr%2B9fmZ7yF8rK7hTIfqQ%2FSk6kDvU%2Fa46OqpKUWkLAgGwihpJcYnw5FK8H%2FPg%2Ffrd2zHiY2WBd%2FEHTbRhnj%2B09pNEM%2FJd9PZnj7lJxR1R5Hm67wGuY4C0lRn53JWggVaqU5E60K5kU%2Bw76hUQI5azMPv4KMrH2sj34%2FDdo9LX%2Fiq3bGoPAkdky9WVqbdzIZqzk7z5TboZZBMxqVDxx%2FS954b2tVxLIWVfTmHTO7jPeFqdD2AhqUyjjWM952NRTR5uVt2B9ww2q21oTGWBAxaBg7kEBJzg3iHc71UVeR0hu6dyJy9DpRxMtytbt7E3aYic3a5SS5%2BKMWcvYqE6D%2BGsnxcl0HvAyzpLk40VE0aLWR0DL%2BkvD12Drw1CNmMvrQaFbtZ8cixs8uGlESCW3mGVULEw0OibtcsqLczgwzJcKT%2FTPgQhpjvxQWMhoN3OBd9ahXbWCyi1AV1cW0NFKhvHa463JNWgdGjryXiaPxAHD9YIAV5%2BaWQr8ciluffWjdZpfKinIXr54yUyqdedVVcuK9PpbNcdzHfFtdLPHOpKany1%2Fq7%2BdWGUIHJS12d2o7Mn2uEuXwBWzNUeK5XqGGaoqP79SDOLG6MbC2ng4Y1MIyti88GOqUBMZKf4X44IulWMiGH9%2B2xHCN0KtbOCXzAd36ygP94GaYI3vfI2HOArR1TiXMjUW9p6m%2FpijIZBav1lBXy7ig6grSjveph6v7ifxMq3Kru2z6vc6GW2cjF0ttFETt1Vd7Oau50O1oCEe%2BaaX6iu7nxPQdJO3omJ7d8dz6M6QyShooaBKe4EuDZE5RHfZ7Muxxw7Y74MM7n45mvzK7dXrJfct3ZD%2BDw&X-Amz-Signature=627a3593624713eebf7ca2ec0c605c313af7f76886d7115ecf37948adb969a5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EYSQII4%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDAh7LEk0rx2qGX4ky9Q2ByROaarT9sGcnxh4ZExKY8%2BQIgNK9s%2F%2FSuVlwBqxH%2B%2BMD9rtNdjmu55yRD8CsUhDkdSl8qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvHkpyTExpi5w1qiyrcA1PCbfbyfjV4hNOh0NNvbbr%2B9fmZ7yF8rK7hTIfqQ%2FSk6kDvU%2Fa46OqpKUWkLAgGwihpJcYnw5FK8H%2FPg%2Ffrd2zHiY2WBd%2FEHTbRhnj%2B09pNEM%2FJd9PZnj7lJxR1R5Hm67wGuY4C0lRn53JWggVaqU5E60K5kU%2Bw76hUQI5azMPv4KMrH2sj34%2FDdo9LX%2Fiq3bGoPAkdky9WVqbdzIZqzk7z5TboZZBMxqVDxx%2FS954b2tVxLIWVfTmHTO7jPeFqdD2AhqUyjjWM952NRTR5uVt2B9ww2q21oTGWBAxaBg7kEBJzg3iHc71UVeR0hu6dyJy9DpRxMtytbt7E3aYic3a5SS5%2BKMWcvYqE6D%2BGsnxcl0HvAyzpLk40VE0aLWR0DL%2BkvD12Drw1CNmMvrQaFbtZ8cixs8uGlESCW3mGVULEw0OibtcsqLczgwzJcKT%2FTPgQhpjvxQWMhoN3OBd9ahXbWCyi1AV1cW0NFKhvHa463JNWgdGjryXiaPxAHD9YIAV5%2BaWQr8ciluffWjdZpfKinIXr54yUyqdedVVcuK9PpbNcdzHfFtdLPHOpKany1%2Fq7%2BdWGUIHJS12d2o7Mn2uEuXwBWzNUeK5XqGGaoqP79SDOLG6MbC2ng4Y1MIyti88GOqUBMZKf4X44IulWMiGH9%2B2xHCN0KtbOCXzAd36ygP94GaYI3vfI2HOArR1TiXMjUW9p6m%2FpijIZBav1lBXy7ig6grSjveph6v7ifxMq3Kru2z6vc6GW2cjF0ttFETt1Vd7Oau50O1oCEe%2BaaX6iu7nxPQdJO3omJ7d8dz6M6QyShooaBKe4EuDZE5RHfZ7Muxxw7Y74MM7n45mvzK7dXrJfct3ZD%2BDw&X-Amz-Signature=120398716bce3dcd4daaa47df8af11669f039135f08f0a18d933b33f5f56c0a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

