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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV2LPGV%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSJoXLOSvzWAT13ms6SI%2F96j1Q3GRTbowInszkm2II4AIhAIpDogpWWoEIhm78r5JmgIKWbY7ylnvOlZnFntmmQe5UKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxT68nUB5DblvXOzXsq3APq5nurzHh5q6hmReXtjAnkexV3ZiDr5kUFBZHNMsA9GaBS5w4pUUbC7xW4qkcUW44wQiNUxVd8%2F8AwQt5sl5CvkZPfJh3p%2FH6HXklVzI%2BxWaIhkjGxwbLhYkZEFUbJwvhVnL3YwJgMuNanpA6BxNL8Dflr9juk6dMh%2FrWrTGgCKYwRE8K158X9QMp0%2FRN93W7auwwuKuTYHlO9r%2FXj%2FX018ef2UHIiUbQQFWAbLoHMIN0UrOMqY6sel9QQBOJb8L6LLZSlax6T2y8zTKAOSXmQZ2BLVBo6EHmgGJVBxf1%2FMTMeAjYPq6JtA3Ev1t16VuGM%2BkAndnTM5q9KNtV8V4IdalPS%2BiybXnBy%2B0DKPdYIcc5Ovc7b7vNYbsocxAQakYAW2lCVNA2QIH%2FsOuh%2BtjtsGayOKqWhsAZUscTg4CPKy46dUvC8cU47vXMusNKm%2BahXGB1O0N7wAeCPFSFb%2FiH5oOmPI1Se2Uss2E7OwAz8uhwLy0sQZvTLfgOwlUMyQNtoVt2k8cqHx9ID42O%2FqXwHjNm53I%2FEDqtDaLMkyHOcqWifYrqLEWdRWv5o6VyXG01Z4Yp9MnHuu%2F9h%2BUWwZHWQtLiBJIztWc87wXoEMaNKpDp8yQhfGb27N6NBcTD8qPzKBjqkAR2ExYsS6jxJj4KFosD9MFVZTGjmx3x%2FFbvrhR%2BtU%2FOrV2NOHYdNDHWy335z0qDDSY5BTBf2BWfqnG8Vvedd2b4pKpUFbLk7D%2Bno5VfQuqpswtNwAXbGHxQUnjMkI95zBnyOjTKPBA9l65RascKV6Im9ExfFpoj%2BW%2BqH2IoaWocOZ0lTPVlwWbDJPTqNtCK%2BA2Z3t1DC6ZKiq1bcrqKapGZN8iQV&X-Amz-Signature=07aa2bc1d5e40e4de4015cf28675093b36d88f879bd758edf8fb0f6d2b168504&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USV2LPGV%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSJoXLOSvzWAT13ms6SI%2F96j1Q3GRTbowInszkm2II4AIhAIpDogpWWoEIhm78r5JmgIKWbY7ylnvOlZnFntmmQe5UKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxT68nUB5DblvXOzXsq3APq5nurzHh5q6hmReXtjAnkexV3ZiDr5kUFBZHNMsA9GaBS5w4pUUbC7xW4qkcUW44wQiNUxVd8%2F8AwQt5sl5CvkZPfJh3p%2FH6HXklVzI%2BxWaIhkjGxwbLhYkZEFUbJwvhVnL3YwJgMuNanpA6BxNL8Dflr9juk6dMh%2FrWrTGgCKYwRE8K158X9QMp0%2FRN93W7auwwuKuTYHlO9r%2FXj%2FX018ef2UHIiUbQQFWAbLoHMIN0UrOMqY6sel9QQBOJb8L6LLZSlax6T2y8zTKAOSXmQZ2BLVBo6EHmgGJVBxf1%2FMTMeAjYPq6JtA3Ev1t16VuGM%2BkAndnTM5q9KNtV8V4IdalPS%2BiybXnBy%2B0DKPdYIcc5Ovc7b7vNYbsocxAQakYAW2lCVNA2QIH%2FsOuh%2BtjtsGayOKqWhsAZUscTg4CPKy46dUvC8cU47vXMusNKm%2BahXGB1O0N7wAeCPFSFb%2FiH5oOmPI1Se2Uss2E7OwAz8uhwLy0sQZvTLfgOwlUMyQNtoVt2k8cqHx9ID42O%2FqXwHjNm53I%2FEDqtDaLMkyHOcqWifYrqLEWdRWv5o6VyXG01Z4Yp9MnHuu%2F9h%2BUWwZHWQtLiBJIztWc87wXoEMaNKpDp8yQhfGb27N6NBcTD8qPzKBjqkAR2ExYsS6jxJj4KFosD9MFVZTGjmx3x%2FFbvrhR%2BtU%2FOrV2NOHYdNDHWy335z0qDDSY5BTBf2BWfqnG8Vvedd2b4pKpUFbLk7D%2Bno5VfQuqpswtNwAXbGHxQUnjMkI95zBnyOjTKPBA9l65RascKV6Im9ExfFpoj%2BW%2BqH2IoaWocOZ0lTPVlwWbDJPTqNtCK%2BA2Z3t1DC6ZKiq1bcrqKapGZN8iQV&X-Amz-Signature=e8f37dc679377550569b79ba9bca6ae77e73b07a533664c1a144200fcf5fcd7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

