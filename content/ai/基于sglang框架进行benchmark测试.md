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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX7SO7RP%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB3ISmGhGtJba3DiX0z7%2F0zQSRXKxkrSYO8SbuhI%2B%2FmAiBZotuW5uPJ3H3ddJQYyOJtM2gzG7Y2ZxeSR4LfEtyPQyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4J9w76FhfegXYqc5KtwD5hzhk91tKdozRBJaZNgZ0%2BefWX19RPmevXny6%2BXQdXQq3Opu5YBha8v4HOD6RVKqqHBoWBVXhdrLgndYPlioCwAF1RbnFQDlL5yb4jJRYcBUyLb3hYIY9lgH4Yb2ej051kUIdO7fVgXSF79KgclAfqDhr3bQN5nq4Fs8cfJ29BA6OaCPn5NPEGYqKEhDUPx5L2uVJ8dhfCQ0ywyMQgs3Jdfg26RzpP0os0%2FmYJQENXd9V1zyLHtQeYhQGabT%2Bfn4pbrQZw8DptTnFUD76QFZXDG7lYu68VLbmceV8dRNiyC6KSO7C125FUI1enn2NjtziVZEEIwW6ua4FLtLKZpv4En9htRcmqI8%2FhVy3r5ryQoXu6HCJV34iDO8CFTMvp2eoPP4x6lMLQIDMVKlfl056ioVkoJGqIt324V8hvkBU3S8wllszdlvkl1ZU%2FLWVeHRwcBOUZ8Ols7nOojRibx4pl41EidSAbhPryL%2BZPxsvJ4TeDKNAkYlAssPH9LkNd7cqjxW1M58bQDtuBybMV5yty9MNup4jlMU8j07v1Dip%2FRLDe9Bf6Ibv%2FnB%2FWz2v9gl3VWOAkAv5%2Bqs25YJ5Jq2PRssQWTJqNas6Ql4mOG%2FLGq9aSffCTNSm%2Foa90gwt%2FD2zgY6pgF3UoB%2FRRERCvwWy2h8DXki2fKpDN562ZylS4LmfKOjYwTiLIjqlC5Re6%2BDPYogqgxfAImuse9knk4fQ88iqp6OvVW0OkhEv%2FwC1y7UPuB47iaMavUglNVb2fsFaFL%2BVNwkBnzX1qeQreyU6QL5mEVU9XvsxI52PO3STGObhED7coTKr47GI2AOdjM2pshEJXYDpIdROdV%2BQTA9CukLNM1Z1R0VewiH&X-Amz-Signature=847fdf83b1db1214b0d4a2da3cf3f6668e8b714e2e62ae515116057fd1c7f34b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX7SO7RP%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB3ISmGhGtJba3DiX0z7%2F0zQSRXKxkrSYO8SbuhI%2B%2FmAiBZotuW5uPJ3H3ddJQYyOJtM2gzG7Y2ZxeSR4LfEtyPQyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4J9w76FhfegXYqc5KtwD5hzhk91tKdozRBJaZNgZ0%2BefWX19RPmevXny6%2BXQdXQq3Opu5YBha8v4HOD6RVKqqHBoWBVXhdrLgndYPlioCwAF1RbnFQDlL5yb4jJRYcBUyLb3hYIY9lgH4Yb2ej051kUIdO7fVgXSF79KgclAfqDhr3bQN5nq4Fs8cfJ29BA6OaCPn5NPEGYqKEhDUPx5L2uVJ8dhfCQ0ywyMQgs3Jdfg26RzpP0os0%2FmYJQENXd9V1zyLHtQeYhQGabT%2Bfn4pbrQZw8DptTnFUD76QFZXDG7lYu68VLbmceV8dRNiyC6KSO7C125FUI1enn2NjtziVZEEIwW6ua4FLtLKZpv4En9htRcmqI8%2FhVy3r5ryQoXu6HCJV34iDO8CFTMvp2eoPP4x6lMLQIDMVKlfl056ioVkoJGqIt324V8hvkBU3S8wllszdlvkl1ZU%2FLWVeHRwcBOUZ8Ols7nOojRibx4pl41EidSAbhPryL%2BZPxsvJ4TeDKNAkYlAssPH9LkNd7cqjxW1M58bQDtuBybMV5yty9MNup4jlMU8j07v1Dip%2FRLDe9Bf6Ibv%2FnB%2FWz2v9gl3VWOAkAv5%2Bqs25YJ5Jq2PRssQWTJqNas6Ql4mOG%2FLGq9aSffCTNSm%2Foa90gwt%2FD2zgY6pgF3UoB%2FRRERCvwWy2h8DXki2fKpDN562ZylS4LmfKOjYwTiLIjqlC5Re6%2BDPYogqgxfAImuse9knk4fQ88iqp6OvVW0OkhEv%2FwC1y7UPuB47iaMavUglNVb2fsFaFL%2BVNwkBnzX1qeQreyU6QL5mEVU9XvsxI52PO3STGObhED7coTKr47GI2AOdjM2pshEJXYDpIdROdV%2BQTA9CukLNM1Z1R0VewiH&X-Amz-Signature=dd5c9d28f09ced33e047dfbed85a356fc3767bf084a7c66424e176154e7a40fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

