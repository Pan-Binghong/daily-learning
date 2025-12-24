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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VH7QMED%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCGLcDDkJMErLgmbFA0iXHEjFRjAzyPMKHr9uxTUI6PVQIhAOAsSLs19etL%2FvlJ3iUHfCAdZt%2F7ztQVOy%2FM7aJO7bcmKv8DCBkQABoMNjM3NDIzMTgzODA1IgyJrY7qWRKipPvCccEq3AP6Hne07YGAUHJAJ2Ic1M%2Ba8pBVZOE9h23%2BXH7AuypXALrzKAkm03rpy64AjBIv43YErN8qeQt7AQhifAL2eroVmfHbg7KqprYX6TfsARADHqj0bOQGeno2jeXcbeysikpFnWPmSKx%2BYTLWCeyUz9%2FV%2BX0D%2FhqoIrvCjDNK5Y5x4Ixw1jdjJmT6T4GMGWg7OiFdeFdNVy7KwZpG%2F9q3H4wUD2g5NZUy%2FPjB%2FUt%2BDR33izKSIqRMVrvwnCcFcGS21IheGYlIpoNz9VtKc3J8qQJc9n5fKEg3Ev%2FiYFYY6vblODoGE0bmWSbFkTDK5iFDaZX0%2BfpHJW87cii2BZpMN1t8rTZIFJr8Kn2Y%2FiQ0nOBQWmhxRaqPoxk67zCp6IEohX7Bpyu9pzrrXsJnrZcgusNNC6a6GsRyQ8zp%2Br3ASLBQWk8AMoAZFnnSMasIRAjbRhVhr0DpVJmzJFXuzkQOz%2FenCGklW8hw6NyXySD8fjtpuXuulWpzH5%2BUyV8RaSGP3iOdh%2FcYUsoP3poy1%2Fx1DBTHu8EOAXkrmQOv9aQFPXelrKONeTGS7Rm7T1M%2FWi16CRJ6qGm6v9jVkdwh9y5MzkTuFTKpgSflHkQFBDQvThga7A2qqWlOCD%2FCA%2FaM%2FDDM4KzKBjqkAVrzPz7y%2FZbbzq%2FlWq5ZP96D5l%2FcKo7048YrQwhPGvknEzgBDz6%2BHwBlR9cQECMQNfQQrZMPPun3kSZX65KXZGsffJKXIZ6jY4H5zQjn7E%2F1yPldNq0dnwpoYt1HkjJmZN2qIKvTp7uK9H7UxIc3LdJAryeOOvBwR%2B5sTnzWx17JoG5HsNo2mkXqDwfXC%2BQZk%2BS9SdU7o5ujmq%2FZ1ypRNm5MtOKB&X-Amz-Signature=659649af1f6cbcd07e9891409a265389f8985793bd8f90905bed9fcd123a5433&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VH7QMED%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCGLcDDkJMErLgmbFA0iXHEjFRjAzyPMKHr9uxTUI6PVQIhAOAsSLs19etL%2FvlJ3iUHfCAdZt%2F7ztQVOy%2FM7aJO7bcmKv8DCBkQABoMNjM3NDIzMTgzODA1IgyJrY7qWRKipPvCccEq3AP6Hne07YGAUHJAJ2Ic1M%2Ba8pBVZOE9h23%2BXH7AuypXALrzKAkm03rpy64AjBIv43YErN8qeQt7AQhifAL2eroVmfHbg7KqprYX6TfsARADHqj0bOQGeno2jeXcbeysikpFnWPmSKx%2BYTLWCeyUz9%2FV%2BX0D%2FhqoIrvCjDNK5Y5x4Ixw1jdjJmT6T4GMGWg7OiFdeFdNVy7KwZpG%2F9q3H4wUD2g5NZUy%2FPjB%2FUt%2BDR33izKSIqRMVrvwnCcFcGS21IheGYlIpoNz9VtKc3J8qQJc9n5fKEg3Ev%2FiYFYY6vblODoGE0bmWSbFkTDK5iFDaZX0%2BfpHJW87cii2BZpMN1t8rTZIFJr8Kn2Y%2FiQ0nOBQWmhxRaqPoxk67zCp6IEohX7Bpyu9pzrrXsJnrZcgusNNC6a6GsRyQ8zp%2Br3ASLBQWk8AMoAZFnnSMasIRAjbRhVhr0DpVJmzJFXuzkQOz%2FenCGklW8hw6NyXySD8fjtpuXuulWpzH5%2BUyV8RaSGP3iOdh%2FcYUsoP3poy1%2Fx1DBTHu8EOAXkrmQOv9aQFPXelrKONeTGS7Rm7T1M%2FWi16CRJ6qGm6v9jVkdwh9y5MzkTuFTKpgSflHkQFBDQvThga7A2qqWlOCD%2FCA%2FaM%2FDDM4KzKBjqkAVrzPz7y%2FZbbzq%2FlWq5ZP96D5l%2FcKo7048YrQwhPGvknEzgBDz6%2BHwBlR9cQECMQNfQQrZMPPun3kSZX65KXZGsffJKXIZ6jY4H5zQjn7E%2F1yPldNq0dnwpoYt1HkjJmZN2qIKvTp7uK9H7UxIc3LdJAryeOOvBwR%2B5sTnzWx17JoG5HsNo2mkXqDwfXC%2BQZk%2BS9SdU7o5ujmq%2FZ1ypRNm5MtOKB&X-Amz-Signature=5c2de68a386587e128ef6cd6dab97feae692d46e0f00ea660a98fb02c7f1e834&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

