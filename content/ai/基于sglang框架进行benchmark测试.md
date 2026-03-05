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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666VINTQ7%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENt1XQxEjOumXImXJouCkihODIYjDA5kfCii9qHYG6CAiBFkmY0Hu01HBs6kDzbgJFrPyuU88zGNzPurudOghupwSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlr%2F3CIY%2B2NSut%2FDgKtwDYdP%2B%2BjWJbZa4TLhm2qfCJnmU5uJ9FDra%2B9Y9iRHGKbLxu%2FDgHS1Tj9wKiI%2BWR08c4uVaCpULB7I5eq4DbSitYjBv9lwA%2ByXx6lZYEII%2Bh0BsBi9%2BQaJdSVQU%2FnEqmDbXrDajjOoNkhTTJqLi1eRot25hspMeqEjEIz3SR5QrM5IReVeWTs6DjYs2%2FEXjCHS1%2FEYmqAlkJ%2Fm7zqDkO9uCBERTYaGc5M9fwlB196Hc2ot9Skbkz6XmDUDl0RtSYyUFNedY22aVUYDrsrI2sl0dFEHQDZc5Lsn%2F5WvGEARIFLDKI4SevSNaYE2IRjsDViMh4i4JCA6NGeiFhyreIubj7vOZtdh0jOZv6eXMdxXWrZEddoGDmNybrqLW%2B9q6Bx3oq9yp%2Bkz3N0rf7gnZHfvXp%2F1ZXRkDSCDUO%2F5bRdxB0WeGqR%2BFwTN9at%2BUrhZeLd%2Bnan1uVSqtCdDWP%2BZrPnNsxCRHXtIkmnlFQ43PyKoIKyC%2Bj8QZKieq5NIlxYteC0pjmCJfM2c8rZ4HN6GaSnDCa%2Bl9fV57DnE%2BtNaKBwyRGYLQDfQNJHkiMHiJEmTJtvbqn07bARooANJyNl28O7YCSkRlyPEUhOOYQLobm4Mu30%2BvW8ECwXvb8lQ%2BxCwwl96jzQY6pgGjjY%2BaTJnjHF4oy2x65BkXL5PwQVZz4CeYDDEru%2Fn3e5KSvQdjVUoo0E3ll%2FHc4rW4Ypl79U6pw7y%2FCSaP%2B90Kc0kZhVy77tNd0N0ZhKXDXTnHbtE3cfY24twfL4Me%2BoSF%2FQybIU1Cg5ixbg2SamdYXP7ZGJCwz2XwXwciBcJW24s7NtixOgG4MPiw%2Bs0DmHMK2ZNylwRyEbTfjggwWDQnjw9kgtcb&X-Amz-Signature=c2ce9ab7d0af8269490be9e5c766f38c51f94ab46c7d848baa68225eb2b7049e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666VINTQ7%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENt1XQxEjOumXImXJouCkihODIYjDA5kfCii9qHYG6CAiBFkmY0Hu01HBs6kDzbgJFrPyuU88zGNzPurudOghupwSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlr%2F3CIY%2B2NSut%2FDgKtwDYdP%2B%2BjWJbZa4TLhm2qfCJnmU5uJ9FDra%2B9Y9iRHGKbLxu%2FDgHS1Tj9wKiI%2BWR08c4uVaCpULB7I5eq4DbSitYjBv9lwA%2ByXx6lZYEII%2Bh0BsBi9%2BQaJdSVQU%2FnEqmDbXrDajjOoNkhTTJqLi1eRot25hspMeqEjEIz3SR5QrM5IReVeWTs6DjYs2%2FEXjCHS1%2FEYmqAlkJ%2Fm7zqDkO9uCBERTYaGc5M9fwlB196Hc2ot9Skbkz6XmDUDl0RtSYyUFNedY22aVUYDrsrI2sl0dFEHQDZc5Lsn%2F5WvGEARIFLDKI4SevSNaYE2IRjsDViMh4i4JCA6NGeiFhyreIubj7vOZtdh0jOZv6eXMdxXWrZEddoGDmNybrqLW%2B9q6Bx3oq9yp%2Bkz3N0rf7gnZHfvXp%2F1ZXRkDSCDUO%2F5bRdxB0WeGqR%2BFwTN9at%2BUrhZeLd%2Bnan1uVSqtCdDWP%2BZrPnNsxCRHXtIkmnlFQ43PyKoIKyC%2Bj8QZKieq5NIlxYteC0pjmCJfM2c8rZ4HN6GaSnDCa%2Bl9fV57DnE%2BtNaKBwyRGYLQDfQNJHkiMHiJEmTJtvbqn07bARooANJyNl28O7YCSkRlyPEUhOOYQLobm4Mu30%2BvW8ECwXvb8lQ%2BxCwwl96jzQY6pgGjjY%2BaTJnjHF4oy2x65BkXL5PwQVZz4CeYDDEru%2Fn3e5KSvQdjVUoo0E3ll%2FHc4rW4Ypl79U6pw7y%2FCSaP%2B90Kc0kZhVy77tNd0N0ZhKXDXTnHbtE3cfY24twfL4Me%2BoSF%2FQybIU1Cg5ixbg2SamdYXP7ZGJCwz2XwXwciBcJW24s7NtixOgG4MPiw%2Bs0DmHMK2ZNylwRyEbTfjggwWDQnjw9kgtcb&X-Amz-Signature=b8b98c91e8784e56af6ea210c0047a76979a67656bdfd3b18c3531c4f8826c1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

