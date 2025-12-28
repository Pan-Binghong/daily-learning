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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVICVEHB%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzInb20hcX8JqMEO7fZbphtUrbsznBq3s6KSsk9PrOfAIgU4sLvVwf26ETjJsZOpYGb0m81Io8FLJzWyS4F5I6WkIq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDITIknGW6SnaFRtguCrcA1jnCRaZsvaXL2%2Bg%2Fb7qwXWvGtuGEZtkNBoX0E63QGv5u%2BuO0rVYnxJLIqFYVKFfbzR1YniL9s1dEHzFDkLHxVl0kSYdgxOpfeAfWerjFr3hKjr6iuwlP2dIjKRc0MPXxfaaiOOP6Degor4TDvm%2BvafiZa1qDW8X%2BM%2B%2F04MdYEc1fVBCwjyR96Pb64PN%2BLa1B%2FmUNmosfKg%2FXFNxDcm10EEu0k%2FSwwzpT0YX3ik4TNPPC8wlVZgt2i6ZbvLnFp9xwI0YFXwab6x6bFijuZEIMT6OWD6hpTxc%2BZ0QWq29qev4IpAHSrg3GCwiLXbagdo8HZAan2QDVytvIWi3ZoYdhRwP7JGfYedtfVqT7m9aGOv0tTnL6kpHOQ4MWgO73V6yOszt6s%2FklG255ZnDzJKz9RzSr0EO9eAZM%2BIYa0mF6sl9tCDOVB4Fu5WpztSZkHk5MQKYg4laAtkwIoUiHuxjxrKMquT0K5C44hf8cmNjqPz3pRYpuRwbxPzdeQXaVkJ57tBJcCQtQ9P6KhE3k1k4J4O33Y%2BEPkysVCuTv9p2aCEuh5672D4GJRKb%2FXjuJiwh8mhNCm5uputmHMh2LYdcgDDmo6avQOc99kHP0Xq57IyL5YMeSjFstwAB03t1MK7swcoGOqUBJSZXH9TrHwOFN7%2ByqYu04vAXLYD66i%2F9vtebdY8YLSK2c7%2FdUS7n729nrTRQUrq7S84H5IgcZanMVcZzqRI42pepErR7zCOTS0JPX77hm0OCFZ7NhvwyLjvVI0HCxlJYuliNmhoZtnOhBK2YfcbyyjJMxImukxE0i%2BjoI%2FY1LF6uM4tWDgbpPM5s0Gx5C8b6gZDtguSsxRsDf%2Fid4uK0WzEXlDM6&X-Amz-Signature=b0ebef960656fbe79327e68e9257d6320d5178ebfcb790bdf18c8ff27a8fa09e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVICVEHB%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzInb20hcX8JqMEO7fZbphtUrbsznBq3s6KSsk9PrOfAIgU4sLvVwf26ETjJsZOpYGb0m81Io8FLJzWyS4F5I6WkIq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDITIknGW6SnaFRtguCrcA1jnCRaZsvaXL2%2Bg%2Fb7qwXWvGtuGEZtkNBoX0E63QGv5u%2BuO0rVYnxJLIqFYVKFfbzR1YniL9s1dEHzFDkLHxVl0kSYdgxOpfeAfWerjFr3hKjr6iuwlP2dIjKRc0MPXxfaaiOOP6Degor4TDvm%2BvafiZa1qDW8X%2BM%2B%2F04MdYEc1fVBCwjyR96Pb64PN%2BLa1B%2FmUNmosfKg%2FXFNxDcm10EEu0k%2FSwwzpT0YX3ik4TNPPC8wlVZgt2i6ZbvLnFp9xwI0YFXwab6x6bFijuZEIMT6OWD6hpTxc%2BZ0QWq29qev4IpAHSrg3GCwiLXbagdo8HZAan2QDVytvIWi3ZoYdhRwP7JGfYedtfVqT7m9aGOv0tTnL6kpHOQ4MWgO73V6yOszt6s%2FklG255ZnDzJKz9RzSr0EO9eAZM%2BIYa0mF6sl9tCDOVB4Fu5WpztSZkHk5MQKYg4laAtkwIoUiHuxjxrKMquT0K5C44hf8cmNjqPz3pRYpuRwbxPzdeQXaVkJ57tBJcCQtQ9P6KhE3k1k4J4O33Y%2BEPkysVCuTv9p2aCEuh5672D4GJRKb%2FXjuJiwh8mhNCm5uputmHMh2LYdcgDDmo6avQOc99kHP0Xq57IyL5YMeSjFstwAB03t1MK7swcoGOqUBJSZXH9TrHwOFN7%2ByqYu04vAXLYD66i%2F9vtebdY8YLSK2c7%2FdUS7n729nrTRQUrq7S84H5IgcZanMVcZzqRI42pepErR7zCOTS0JPX77hm0OCFZ7NhvwyLjvVI0HCxlJYuliNmhoZtnOhBK2YfcbyyjJMxImukxE0i%2BjoI%2FY1LF6uM4tWDgbpPM5s0Gx5C8b6gZDtguSsxRsDf%2Fid4uK0WzEXlDM6&X-Amz-Signature=a915b7a45729463fe4213fadb783b526809dd9d7178f47c130bfddbc17e8f7ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

