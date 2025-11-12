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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GQASJNW%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC9voDGfsrOwkeo5658fdjXHwD3zQQ%2FTg7cvEgCwqEVdwIgHpqdHQ4d7h2nGJ%2BnFouGhdnsg3qoC2et2QKFIha5s2oq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDMxx0lQwVfO7b6TRHCrcAxiNYXvSXpoM7yTc%2BQaSqmQ8UkSZQovijN%2FAF438prVx06CuPxOvdo1n03BPY4OOPLHafXAvqziNvSBefj4d7C9ZSTJqJyxs%2B1cc6MjMvVgWz6W%2FgBiahwHVGY4m1PYb9HQyltEz7xnYYEYRQxoJ35tWccrmlGDq7bjsks03ZB3nDpgQVwvV2dkdJO8jGPgaLwjkOHUSJjVhPdD1NhS6LSKabIEGRCYqm%2BGykhWMNMx8jG%2BCyRcPE95C5D15dGk%2BTD%2FEOQq5DEoJCdRTQ%2FvP5vKW33eDkrbJdNIkIIxQHP6CvtrUfHzMBVzX%2BC4RYuYNss7ycH8kyujPo7UEjm6cEAQWcbcWTRNj%2FWrylZiIGIJLyrmwRUeyNnwRnDE7919LnxumBKe3QLrcqRpIcgH5VfYpN7%2BE5GH6x5YY7qKhMP%2B4ej5TSBPwfpBh2V%2B7570q3SmCipGsv9tDYCZu2J4DMJYoiObDkyTgV43y76ELEzMPGTlL4lgVcYly5xMx5nyf%2BQwSYlDVTw8%2F1FYAAZZfT8Qe7d3vVK5KxwqwUhH%2BqsSkxKt24CddCGmEM3lQc5raLSxxT13aR66saIj5m2N%2Bh56ewoQf7mwtKF3XMa3m0JfHWtk1A115IOYY3kOlMMzjz8gGOqUBxu3jC2pmP4FoMe3JiH7cgvvRIUBlMVaYkyPK4B3bu%2FjzwT1YKwGkH6hoNcV9%2BA%2FYlvBELeJLYZmK6pAI6TUvnwcmjHssyM6ZhjLjYsu%2Firuypq4XAdxDq6x2w0vscwoFjlUsdy0HXJen0UBb3XxzUUMXxOFZdW4vHmKp6z3GKXPX4tXnwi0Bh1QD4RYWokzpI97JCmezmqKFz%2F%2FKbeYBAHW4vnNh&X-Amz-Signature=6d6c560b5cb7fa153183e1323a3dd0b791a3c038ac944db4aea860aaa9fabaa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GQASJNW%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC9voDGfsrOwkeo5658fdjXHwD3zQQ%2FTg7cvEgCwqEVdwIgHpqdHQ4d7h2nGJ%2BnFouGhdnsg3qoC2et2QKFIha5s2oq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDMxx0lQwVfO7b6TRHCrcAxiNYXvSXpoM7yTc%2BQaSqmQ8UkSZQovijN%2FAF438prVx06CuPxOvdo1n03BPY4OOPLHafXAvqziNvSBefj4d7C9ZSTJqJyxs%2B1cc6MjMvVgWz6W%2FgBiahwHVGY4m1PYb9HQyltEz7xnYYEYRQxoJ35tWccrmlGDq7bjsks03ZB3nDpgQVwvV2dkdJO8jGPgaLwjkOHUSJjVhPdD1NhS6LSKabIEGRCYqm%2BGykhWMNMx8jG%2BCyRcPE95C5D15dGk%2BTD%2FEOQq5DEoJCdRTQ%2FvP5vKW33eDkrbJdNIkIIxQHP6CvtrUfHzMBVzX%2BC4RYuYNss7ycH8kyujPo7UEjm6cEAQWcbcWTRNj%2FWrylZiIGIJLyrmwRUeyNnwRnDE7919LnxumBKe3QLrcqRpIcgH5VfYpN7%2BE5GH6x5YY7qKhMP%2B4ej5TSBPwfpBh2V%2B7570q3SmCipGsv9tDYCZu2J4DMJYoiObDkyTgV43y76ELEzMPGTlL4lgVcYly5xMx5nyf%2BQwSYlDVTw8%2F1FYAAZZfT8Qe7d3vVK5KxwqwUhH%2BqsSkxKt24CddCGmEM3lQc5raLSxxT13aR66saIj5m2N%2Bh56ewoQf7mwtKF3XMa3m0JfHWtk1A115IOYY3kOlMMzjz8gGOqUBxu3jC2pmP4FoMe3JiH7cgvvRIUBlMVaYkyPK4B3bu%2FjzwT1YKwGkH6hoNcV9%2BA%2FYlvBELeJLYZmK6pAI6TUvnwcmjHssyM6ZhjLjYsu%2Firuypq4XAdxDq6x2w0vscwoFjlUsdy0HXJen0UBb3XxzUUMXxOFZdW4vHmKp6z3GKXPX4tXnwi0Bh1QD4RYWokzpI97JCmezmqKFz%2F%2FKbeYBAHW4vnNh&X-Amz-Signature=79cf784858d52a3849e6193309f2295a0ac4753d28a0707e0a27278d67279371&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

