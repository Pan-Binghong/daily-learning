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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YADQ4DV%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQCoHEdUXR2EH%2B4VAEBXqAOnr%2FXyzj90Wr%2FHvsWhONJTRwIhAOmjUw3OqHPs7de5QAz2vMplFuz1GveLo%2F5cZy4tXuJ4Kv8DCDAQABoMNjM3NDIzMTgzODA1IgwG%2B1uoNgBydnSJE1kq3APBP6U4SX7KV4v59dyRyWA4Or08XyEcHx1boHiSliEZ6CM4%2B5rFvYLvoYuHhXFs%2BnOx6KuFpbcuYmDDAe%2B0N41HTIX87AB93ldmdagsPgJKom6jCneo62iOFUDEH5J3sYzEEZn%2BvYLsyvFCQfT8iHJM4X1qUKJ%2BBZKI8uXYnnw7e2VyHqtHBi6%2FOQQoXRFHk8FknMI5zrAAwnWzOD9iJLg1kOYpO6X85JO6FiBC87eneJux1qJN7mRqR%2FjzFoBK3zcoSNvx6PaOWRXErxmgdJ3K7c4v%2FcjLbKJXbAnRayADIUHYeHBjA%2Bi93xN71HyAXfluCT6ElNV%2FkKkEpJBbyuP%2B0xr2PN%2BRVb236odSJndMviw%2F7qC4NkcAKh389OPN88pUFYIpXrv6fAJir%2B%2Fh21cAqoDnJmvH0VoRFCniESgag993qciYGkKfdQpmb2CprRUtSBgebpXhf3zBHeK4L%2BlxH5OdgHMFsLS7bY66cYMgiP20LFI5q4NJndoBRNJs6aXdEbOgDm2nm8pJfIX%2FmV0JGvs6NeR%2FokhWd7KEZmQjGfCvJsZEOZ72%2B3sZsVJlxwy2vVd1EnPpw1tIr6PbeJFogtareIpTALE4K3n1NZENXME%2FwP0Ge1%2FH17an9zCFsdrLBjqkAcPcMggqzGn6TtplBz0X5%2ByvA8Rx9tE9ionV64liW6Vw3XDAEy0EyY34tl%2BC6o7s4PIlKquWfHQl7Q%2BTCkX0YIqh8CFs8g8XMlQys1m19ZWXgmzIS5wjD1WURG22%2BxGawi9WJaMImsocVzIZXLdMU7y8HaScJ6A4j2ax5fpCAXf8OkcZ%2BMzESeseUt%2Bj%2FcZX39ulJ%2FT5WMvu5c7waB4DhYexuJiG&X-Amz-Signature=b8c03b533b1f75a1cee37372dc710e5e7ccacccd1b8426a2dac03932848c0ff8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YADQ4DV%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQCoHEdUXR2EH%2B4VAEBXqAOnr%2FXyzj90Wr%2FHvsWhONJTRwIhAOmjUw3OqHPs7de5QAz2vMplFuz1GveLo%2F5cZy4tXuJ4Kv8DCDAQABoMNjM3NDIzMTgzODA1IgwG%2B1uoNgBydnSJE1kq3APBP6U4SX7KV4v59dyRyWA4Or08XyEcHx1boHiSliEZ6CM4%2B5rFvYLvoYuHhXFs%2BnOx6KuFpbcuYmDDAe%2B0N41HTIX87AB93ldmdagsPgJKom6jCneo62iOFUDEH5J3sYzEEZn%2BvYLsyvFCQfT8iHJM4X1qUKJ%2BBZKI8uXYnnw7e2VyHqtHBi6%2FOQQoXRFHk8FknMI5zrAAwnWzOD9iJLg1kOYpO6X85JO6FiBC87eneJux1qJN7mRqR%2FjzFoBK3zcoSNvx6PaOWRXErxmgdJ3K7c4v%2FcjLbKJXbAnRayADIUHYeHBjA%2Bi93xN71HyAXfluCT6ElNV%2FkKkEpJBbyuP%2B0xr2PN%2BRVb236odSJndMviw%2F7qC4NkcAKh389OPN88pUFYIpXrv6fAJir%2B%2Fh21cAqoDnJmvH0VoRFCniESgag993qciYGkKfdQpmb2CprRUtSBgebpXhf3zBHeK4L%2BlxH5OdgHMFsLS7bY66cYMgiP20LFI5q4NJndoBRNJs6aXdEbOgDm2nm8pJfIX%2FmV0JGvs6NeR%2FokhWd7KEZmQjGfCvJsZEOZ72%2B3sZsVJlxwy2vVd1EnPpw1tIr6PbeJFogtareIpTALE4K3n1NZENXME%2FwP0Ge1%2FH17an9zCFsdrLBjqkAcPcMggqzGn6TtplBz0X5%2ByvA8Rx9tE9ionV64liW6Vw3XDAEy0EyY34tl%2BC6o7s4PIlKquWfHQl7Q%2BTCkX0YIqh8CFs8g8XMlQys1m19ZWXgmzIS5wjD1WURG22%2BxGawi9WJaMImsocVzIZXLdMU7y8HaScJ6A4j2ax5fpCAXf8OkcZ%2BMzESeseUt%2Bj%2FcZX39ulJ%2FT5WMvu5c7waB4DhYexuJiG&X-Amz-Signature=2a4aefdec96abd063ea34f037785363c6da346e022b74bf08f0e8a00d92422c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

