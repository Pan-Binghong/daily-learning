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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKGKSY4A%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQDc7G0u7B0GpDozA1OLfKRg6YYYY9QlF46wJ8M9Bn8dbQIgCfDxA0UEakhX%2BwRnuWXsWg0D2Kq18mKtHcLSnGUEtWAq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNZTgGYueV%2BLmvG%2B6CrcAxh20EuQPJZFzmwSqCZZ8RcPa%2FRNl%2FbCQIaTn4jqQLmVSNM%2FYZYcDNIqIlv6WgMLbFGVd7e%2B3DYxW5OMcu5kfPi%2FWMCvUwhLfu8W3QICQBQhd%2FXUBXfUAt3ve84MQ6LfsVnm5ZaAYrzqvM2wAusUv5FM51Vj3sgqYn2P5aSYSSxKC%2FSSY0DI%2FWRKlxYzRWNvH2C7vwhHxkS2tVcQL8W0NDXS9aeQcf%2BynDy7jCnDqzWr6vvbPQqnE5%2FTr89HwRcTQwmY6HdYu5BXHVcSdvLAV6rmmk2zUzMjDwoiQieZQWwIgwkjcGtk7zWoXF3iKn8rppURHwglE%2FnGExzerAbU8uke6aWnqMrwx7z5uTuvjIXQ%2B7CpOsK6cW4kQviy8Ig%2FxXvWYHy1nIZSrzA5cn64rIDrHaqqgFw%2FIVVMpy7hcFNf3SUVvCoe1VRtUNJwV3kU8FRJKINjl928OPpS4UE8EWBiMNc9jvZaxaZm48uxyuU0sUgfrWmRpKvRdDnyS%2FDys2ISQ%2FJqyqelw%2FSqnXw1Hqqzb2LCBgsX2m%2F0KUkDyXahvuSbtrDr7UcOT8hSS302Mw6hRGTMAIe6yRJnOe67pe9mDycUdvLjdOIkJnC7wBv7KRaVVhelwbggb08SMJWf%2F8gGOqUBrGxtwNet297SZGMZdy46mtLQGBwHbCsd7bwAF%2Fym%2BX0eQ8CvzvMqKmIZNwzaQn99rrnaHhj0rtq0QOxJIndWbuJBl1qVGv35LeLnnTolfMBYaIcM4WMOkolHeGJ0NU45cNi9fEEh7T%2Fs1sDfc%2BTUndbpd6MWOTKCDTUYcq195JIyyv%2BN%2FyA15dchejyCKXuA17HldEEikKmTZzSeEpLCFarek32r&X-Amz-Signature=71b3f83599a5280da6528500f957aa8c3cd15468d6d9eef5510c4eb794b70a13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKGKSY4A%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQDc7G0u7B0GpDozA1OLfKRg6YYYY9QlF46wJ8M9Bn8dbQIgCfDxA0UEakhX%2BwRnuWXsWg0D2Kq18mKtHcLSnGUEtWAq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNZTgGYueV%2BLmvG%2B6CrcAxh20EuQPJZFzmwSqCZZ8RcPa%2FRNl%2FbCQIaTn4jqQLmVSNM%2FYZYcDNIqIlv6WgMLbFGVd7e%2B3DYxW5OMcu5kfPi%2FWMCvUwhLfu8W3QICQBQhd%2FXUBXfUAt3ve84MQ6LfsVnm5ZaAYrzqvM2wAusUv5FM51Vj3sgqYn2P5aSYSSxKC%2FSSY0DI%2FWRKlxYzRWNvH2C7vwhHxkS2tVcQL8W0NDXS9aeQcf%2BynDy7jCnDqzWr6vvbPQqnE5%2FTr89HwRcTQwmY6HdYu5BXHVcSdvLAV6rmmk2zUzMjDwoiQieZQWwIgwkjcGtk7zWoXF3iKn8rppURHwglE%2FnGExzerAbU8uke6aWnqMrwx7z5uTuvjIXQ%2B7CpOsK6cW4kQviy8Ig%2FxXvWYHy1nIZSrzA5cn64rIDrHaqqgFw%2FIVVMpy7hcFNf3SUVvCoe1VRtUNJwV3kU8FRJKINjl928OPpS4UE8EWBiMNc9jvZaxaZm48uxyuU0sUgfrWmRpKvRdDnyS%2FDys2ISQ%2FJqyqelw%2FSqnXw1Hqqzb2LCBgsX2m%2F0KUkDyXahvuSbtrDr7UcOT8hSS302Mw6hRGTMAIe6yRJnOe67pe9mDycUdvLjdOIkJnC7wBv7KRaVVhelwbggb08SMJWf%2F8gGOqUBrGxtwNet297SZGMZdy46mtLQGBwHbCsd7bwAF%2Fym%2BX0eQ8CvzvMqKmIZNwzaQn99rrnaHhj0rtq0QOxJIndWbuJBl1qVGv35LeLnnTolfMBYaIcM4WMOkolHeGJ0NU45cNi9fEEh7T%2Fs1sDfc%2BTUndbpd6MWOTKCDTUYcq195JIyyv%2BN%2FyA15dchejyCKXuA17HldEEikKmTZzSeEpLCFarek32r&X-Amz-Signature=43791720a98217f3cf151c5927d14a2d9381bbdaee257bbe7d814eda6cb6719a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

