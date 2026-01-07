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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGLZPY3M%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEy7g%2BxYc4LWNqayiFEHcZioaE5QZg1gYqm4diDwhYHVAiA5D4zlVQdF8fjGHKWNYbg7oatXkWKoo1z2yj5a76QmYyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMY3v29%2BVKvoWOkYZwKtwDxwu3%2BuQIzMTv3qqK80TkGrCgIIUxh5efY6uCV%2B%2Bug8%2FYkHjIkM6K7kUaIJdvZuFgHEXem8nnwtssvsfG8c3TtPbbMF%2FmWIb%2F4Q62GCaaJfCT%2B3SwhSsTWyVxjDlP5ZyXnl3uHNEtsvGDWiIf2UYWjHu1KXdjlD1idCVdN6AeiveJF1BmOifRzh1WXGTlPXT0aRsVWUvJ1y10r4lXuGOAc1YR253q86r53jYWPGqUH6s8pwx%2FALzoR4vaeYLxdnS%2BfcnYNYSx3KxXVugl7su4on6LJ1IT5ltCqQ8nyHOnNfmc9pS2uY9tajpALnb%2FjoX8PFI9nyJRC6GU0JSX3kFPBLoW1Oh8azJvFJ1%2BD3o8Z9%2FP3gU%2FkhO7Mxq5Fbb9px%2BTGkFldKV%2FNECuo%2FrsBzfMYw6fqkw7vakQkQYYzHc9VYWxQUKwcb1Wuiox84C0gQjJO3SYdqngmK39tune2WP8GHwOUepEEjCOsB7mFrO4KUZ0MW%2FD2NunaHsorgq%2F6wYMt5%2BtKqFQqBqTJNl13Updp8JzFAuNwl0JMItafgueOsvhh4oQcBF2flDunMVdsz%2BKNUJiU74EonkDCZ4D7YMBigx2rB16sZcCREd7xffdwWPr%2FDVEK%2Fh%2B8OsindgwxY73ygY6pgH3rV8mC9PmdEBxYZXKgs%2F%2BK4s4uQHC5dx2uwGxfW9joUV%2BKZmyACEBrE8DhXIzbj6v6l9PU3AauI2uq%2BPtCHj7eK27NUYC04tuh1QYsZ%2FxtUK9a9693b0lBpUuSc%2FEqqnhZ0BZEbS3FfO3Ng%2BcE0L5KRwF49OztKFmje4dG%2FMoMJtA4ddY%2BpreECd9PjRV9Lv82ytPNxP0%2FPqBXPmvbx6Z6SPdYf96&X-Amz-Signature=c498776ea1d895922eee84129b4c4d86d465b6b9a599ef70c74c69ab7becaf08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGLZPY3M%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEy7g%2BxYc4LWNqayiFEHcZioaE5QZg1gYqm4diDwhYHVAiA5D4zlVQdF8fjGHKWNYbg7oatXkWKoo1z2yj5a76QmYyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMY3v29%2BVKvoWOkYZwKtwDxwu3%2BuQIzMTv3qqK80TkGrCgIIUxh5efY6uCV%2B%2Bug8%2FYkHjIkM6K7kUaIJdvZuFgHEXem8nnwtssvsfG8c3TtPbbMF%2FmWIb%2F4Q62GCaaJfCT%2B3SwhSsTWyVxjDlP5ZyXnl3uHNEtsvGDWiIf2UYWjHu1KXdjlD1idCVdN6AeiveJF1BmOifRzh1WXGTlPXT0aRsVWUvJ1y10r4lXuGOAc1YR253q86r53jYWPGqUH6s8pwx%2FALzoR4vaeYLxdnS%2BfcnYNYSx3KxXVugl7su4on6LJ1IT5ltCqQ8nyHOnNfmc9pS2uY9tajpALnb%2FjoX8PFI9nyJRC6GU0JSX3kFPBLoW1Oh8azJvFJ1%2BD3o8Z9%2FP3gU%2FkhO7Mxq5Fbb9px%2BTGkFldKV%2FNECuo%2FrsBzfMYw6fqkw7vakQkQYYzHc9VYWxQUKwcb1Wuiox84C0gQjJO3SYdqngmK39tune2WP8GHwOUepEEjCOsB7mFrO4KUZ0MW%2FD2NunaHsorgq%2F6wYMt5%2BtKqFQqBqTJNl13Updp8JzFAuNwl0JMItafgueOsvhh4oQcBF2flDunMVdsz%2BKNUJiU74EonkDCZ4D7YMBigx2rB16sZcCREd7xffdwWPr%2FDVEK%2Fh%2B8OsindgwxY73ygY6pgH3rV8mC9PmdEBxYZXKgs%2F%2BK4s4uQHC5dx2uwGxfW9joUV%2BKZmyACEBrE8DhXIzbj6v6l9PU3AauI2uq%2BPtCHj7eK27NUYC04tuh1QYsZ%2FxtUK9a9693b0lBpUuSc%2FEqqnhZ0BZEbS3FfO3Ng%2BcE0L5KRwF49OztKFmje4dG%2FMoMJtA4ddY%2BpreECd9PjRV9Lv82ytPNxP0%2FPqBXPmvbx6Z6SPdYf96&X-Amz-Signature=b50160a7f3ecd0ae2d8387c10cd41ac7a967e7e878f281b57d26ad1aea932658&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

