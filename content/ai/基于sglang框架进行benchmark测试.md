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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3HGR6CI%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBkUfJIatWWyzdp1IU5kOQK0wmECZBHMpeWPfuyiDDuNAiBk2BmmZLGArG4rGXBkKZoOgu8UuVJJzFM2I5hNwC%2F9hyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMCSrfeZu9I4QMa8omKtwDAe%2F%2Ff0INU0nS5jGjZ53lLPZSOsjzZSB2qsDr8KCtgmENb6uVRAgbjGUGgwfk3QGiBDyQ9zvgARtzBMJd7Ym4%2Fu%2BKvQpTS4RDM0XL40vbnW%2B9d1nXLn6tYCEcrLO1ILIp%2BNOnncWPjB0czquCjwpsQ8CQ0pBMGNuy7bWQBgpflHWNKCeVlJ3LLwTl9uaNNuR%2F4eIOCszGI9HsQ9BR2UiYFb89ed2f9vTqOdgKOK9zIDFVP7Tel3xzqSZbcBAmq8N5pFLlrRvEzpnNUNtyxaaXlE8EdMjSTIi%2FwiIiyf5VwqviogFgKlF9hXMVvcyD51tq5KPLN6cV6qBNzYFfQfEKNgAZ74EvBlLvR9uWAUY2cW5SI70d1%2FEkJV9G7z8gdixwsaygzXrb43fy8mXFRwkllzlrexlk6%2BNCoHF3yB8FPIS%2BllmYUzwAWExdKNkk8frBsDn%2FsPinqsaSK4lhOk%2FAzE8MGa3BbDcDNbdju9xHGNh%2FA%2BLcw4Ad6yWQkYnwvD094vI9EFs7Y%2Bmkackqw37jh9OUFUB02nOK%2Bjjdl%2B23BbVLiTMF4DXIs%2F7cGuv%2Bf1tfCBQtMIw0gZIlxhRpBThc3hfrF%2BIGHUiU0nt8m%2FFnoJ08ZIHP16odm7Be5aQwodyOyQY6pgFH8UezJNI6yYrZu8bCRg605AdYuJRR6Bnt%2Bnv2I31u%2BQJTie4NVUxHaVARnfYfsOmUzA9IiWjBGnoY6Wjq%2FOORxeWnjDTxRUWDoDx5W0j4%2F0WKMGGa1bHWG9tmIhqlL9FYIDlUzHoGESTGvGcf7rW0PqW63Ol6BPnTNv2wmlHKFJyPYBpmQWJJZQHoSx8ZFBro0q3txvHLk%2BThPvH4%2F9hESBA%2FNloH&X-Amz-Signature=860e3d7b31ae37d9f4ead8ada3f3379f6b13beaf09c2c2d1b6ac0532dad814a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3HGR6CI%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBkUfJIatWWyzdp1IU5kOQK0wmECZBHMpeWPfuyiDDuNAiBk2BmmZLGArG4rGXBkKZoOgu8UuVJJzFM2I5hNwC%2F9hyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMCSrfeZu9I4QMa8omKtwDAe%2F%2Ff0INU0nS5jGjZ53lLPZSOsjzZSB2qsDr8KCtgmENb6uVRAgbjGUGgwfk3QGiBDyQ9zvgARtzBMJd7Ym4%2Fu%2BKvQpTS4RDM0XL40vbnW%2B9d1nXLn6tYCEcrLO1ILIp%2BNOnncWPjB0czquCjwpsQ8CQ0pBMGNuy7bWQBgpflHWNKCeVlJ3LLwTl9uaNNuR%2F4eIOCszGI9HsQ9BR2UiYFb89ed2f9vTqOdgKOK9zIDFVP7Tel3xzqSZbcBAmq8N5pFLlrRvEzpnNUNtyxaaXlE8EdMjSTIi%2FwiIiyf5VwqviogFgKlF9hXMVvcyD51tq5KPLN6cV6qBNzYFfQfEKNgAZ74EvBlLvR9uWAUY2cW5SI70d1%2FEkJV9G7z8gdixwsaygzXrb43fy8mXFRwkllzlrexlk6%2BNCoHF3yB8FPIS%2BllmYUzwAWExdKNkk8frBsDn%2FsPinqsaSK4lhOk%2FAzE8MGa3BbDcDNbdju9xHGNh%2FA%2BLcw4Ad6yWQkYnwvD094vI9EFs7Y%2Bmkackqw37jh9OUFUB02nOK%2Bjjdl%2B23BbVLiTMF4DXIs%2F7cGuv%2Bf1tfCBQtMIw0gZIlxhRpBThc3hfrF%2BIGHUiU0nt8m%2FFnoJ08ZIHP16odm7Be5aQwodyOyQY6pgFH8UezJNI6yYrZu8bCRg605AdYuJRR6Bnt%2Bnv2I31u%2BQJTie4NVUxHaVARnfYfsOmUzA9IiWjBGnoY6Wjq%2FOORxeWnjDTxRUWDoDx5W0j4%2F0WKMGGa1bHWG9tmIhqlL9FYIDlUzHoGESTGvGcf7rW0PqW63Ol6BPnTNv2wmlHKFJyPYBpmQWJJZQHoSx8ZFBro0q3txvHLk%2BThPvH4%2F9hESBA%2FNloH&X-Amz-Signature=ba78a6c99c1c240626eac1e9bc2d982be4f1da66fa8a4cc7170c3cb7a9b3c91b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

