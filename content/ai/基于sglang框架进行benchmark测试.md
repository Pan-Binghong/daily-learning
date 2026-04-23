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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HJSAWKD%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAs78FU6URi7TJqzvEobBZGYHiwRrbWYBAJSlO10ATLVAiAnYwq7C0fXlDfauYkbg1QRvhSZ7Za8ztnl7DihwmA6%2Fir%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMIm5JE8QhyMs765GXKtwDnitADn6T4W4lB8Rm9vWMCckSoUafL5%2Ba7GsNZJbEG4%2FWxstg%2BPf3KcW6%2BeouHHN%2BcVi9adPD4%2B%2FWQDOL3gw0NKnL2WFmimJe4wOjPrRp8HmA8UBx%2BjP991tWCoUj23tXEp4bYb8wbPN57HasEXmMWFreZ%2FptmRqcVZvrMTg609LBeE1VVTFaBEw85ZHxSlM4JjYHHa8Pq5EfKntEAFCO90DaHegwe1cUtATF8sY%2BxCq2ZkMcMd5UbcVtHzKJ6e9aDqM9MLqh6tBQn88nvJ4sBZA%2Bb84SegwLJcC%2FVd7W7bcYDLkqwJD43eUNq5MyGTQpS6anml5fKsbCVRN%2BytekOJezdv1fKwqIAhGzF3uT8Pdd6JsbpEnBudRC5mHH8V%2FOuPiOL1nEWSbBJ8tnnPGlliSR4EZtU%2FyWPSYg%2BQgLoG5cQUAJQHSmVIjKLTs8dymsO9OunM8DN9qkSMKGaB3m9qj6UfCWdry%2FjXTDdtlQtvpebnT4ObAm21T6mMitba%2BWCwZeCO9i8bgaFgQO8Q4pccviYjBui1R%2B1UxZmDssJowhKDFZytHaa5Z1p1u7%2BirzgUGJqCnlkGB9W88ZigBwHDzg6Klxy%2ByAuvgJW796tlNNccO6RfecrQWzmgAwop2mzwY6pgFjdQe6QHW%2BvrdhoDmqvoYhKqWoQB7hQ7ZWpnNpnMcIIEEEb756yjeB8rw1mP%2Fg3V3U%2BGIbYWtbDMjbgTtdKruYZT1%2FPNWdsN8ZLkoJzn%2BDKRXRndHHU9fd9oMdDcdFIEBEA2nD7mTuecURnq63FG02Ybzz8KmS7NuOkY45bv1dBCEjeOPlc1A9lVrY8SEpRy8e60CJJGkie3Wq9w3ZAYGnvljtYIhW&X-Amz-Signature=c59130ff35b5d6e0fd311b1cf7aaf9ad5fd120fb804be27c4130b8316e6185a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HJSAWKD%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAs78FU6URi7TJqzvEobBZGYHiwRrbWYBAJSlO10ATLVAiAnYwq7C0fXlDfauYkbg1QRvhSZ7Za8ztnl7DihwmA6%2Fir%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMIm5JE8QhyMs765GXKtwDnitADn6T4W4lB8Rm9vWMCckSoUafL5%2Ba7GsNZJbEG4%2FWxstg%2BPf3KcW6%2BeouHHN%2BcVi9adPD4%2B%2FWQDOL3gw0NKnL2WFmimJe4wOjPrRp8HmA8UBx%2BjP991tWCoUj23tXEp4bYb8wbPN57HasEXmMWFreZ%2FptmRqcVZvrMTg609LBeE1VVTFaBEw85ZHxSlM4JjYHHa8Pq5EfKntEAFCO90DaHegwe1cUtATF8sY%2BxCq2ZkMcMd5UbcVtHzKJ6e9aDqM9MLqh6tBQn88nvJ4sBZA%2Bb84SegwLJcC%2FVd7W7bcYDLkqwJD43eUNq5MyGTQpS6anml5fKsbCVRN%2BytekOJezdv1fKwqIAhGzF3uT8Pdd6JsbpEnBudRC5mHH8V%2FOuPiOL1nEWSbBJ8tnnPGlliSR4EZtU%2FyWPSYg%2BQgLoG5cQUAJQHSmVIjKLTs8dymsO9OunM8DN9qkSMKGaB3m9qj6UfCWdry%2FjXTDdtlQtvpebnT4ObAm21T6mMitba%2BWCwZeCO9i8bgaFgQO8Q4pccviYjBui1R%2B1UxZmDssJowhKDFZytHaa5Z1p1u7%2BirzgUGJqCnlkGB9W88ZigBwHDzg6Klxy%2ByAuvgJW796tlNNccO6RfecrQWzmgAwop2mzwY6pgFjdQe6QHW%2BvrdhoDmqvoYhKqWoQB7hQ7ZWpnNpnMcIIEEEb756yjeB8rw1mP%2Fg3V3U%2BGIbYWtbDMjbgTtdKruYZT1%2FPNWdsN8ZLkoJzn%2BDKRXRndHHU9fd9oMdDcdFIEBEA2nD7mTuecURnq63FG02Ybzz8KmS7NuOkY45bv1dBCEjeOPlc1A9lVrY8SEpRy8e60CJJGkie3Wq9w3ZAYGnvljtYIhW&X-Amz-Signature=27b1914fa7cd17a10c7cbc0f9bef0ee2a8e5ad70e6e9ad679da8d0642492380b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

