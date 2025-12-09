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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BJ6TFRL%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICG1ZcKfSwbVfWZrbZi5JNRh%2BYs5y8QxqyOcj0Khl1YxAiBJEl2zU%2B2rejEtM6l%2BiP2jvH4C3Q8pV5F9Tdi%2BNmA3yCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnQSpf7BYUNQbYJHSKtwDock08dNDPo8BIgJDZJrVvE0dw61Lq2Ng76bOQAfzKgiGTlGJylj4sZIFcmFjr6MRBAFKHgmSwXmtAx4XB9275piMcde3odxT7%2BO2f7Ola7ycp6AK6dVr4xWuwVxK9xHCsdM3lxaHdxtzSeg%2F4OeK36W78iGC8GzkJoKKQ%2Bt69Abbp%2FU4gKxdKz5o7B8QLdJQikP%2BmSz8n9Gu6m358w0ZE1INCA7LAiPMpuAWuYMPVl0VtO9ZlkHQ%2BrqoFoGdOgPAqMKUJRzDqdEgTzKqb8OZCbQvExx%2BYCycyxIRI3y4XPGq281hI1TWExKxJsumNMZZN%2BeKW4rxzLKGbmB1APAi6SMajP%2FXMWIk39nn%2FxwkZcjXI9ip3BMkzMwExAsRix7NbtsuKP2X4iH%2FjkIV1kbvIcoOkcUD6dN78sMe9Ae6GuhLFfBUK%2FWOL5duBo%2BxouOPz03lq2zgBLOv%2BenTTeKrddeHfhJioQLWKsDz3AybsWFpX7UkVpPbu1m%2BEEVYu%2BYe3RK1kkatTqA73aXExS2OnqadMmPd4LHw6gM97afzWQS8eT8rhWfjDWElFg0tc0vjbXr12JHE9f6WAQ82IjQMiG%2Fq29OluoueWr1wjw0pHlzHsH221jjQoosw2rcw8I7eyQY6pgHPx%2BroCrqLR4ldlHnSvPf6hKGxvO7yvPxbaxaSX02S%2F6xOJETxkc30X6IjRSQ0DQPwh9JVw3VlwhUaJMwRBJUrcBnlvcUYUeqwcWyqGIh49dVEAnwDyUte%2FY5d1525DEhjOuW81T6eUmOEuQhQGKW%2FoUChekaHbP4MAkWmEFhxC%2F7mctH2jsufulSPAkZ6sPuqejJfbb3MtokNST66HZW60tWHAbf3&X-Amz-Signature=cb5eb41d9fa2a4f8503a509fc346d45b55071507f6217cab639df175898a6062&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BJ6TFRL%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICG1ZcKfSwbVfWZrbZi5JNRh%2BYs5y8QxqyOcj0Khl1YxAiBJEl2zU%2B2rejEtM6l%2BiP2jvH4C3Q8pV5F9Tdi%2BNmA3yCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnQSpf7BYUNQbYJHSKtwDock08dNDPo8BIgJDZJrVvE0dw61Lq2Ng76bOQAfzKgiGTlGJylj4sZIFcmFjr6MRBAFKHgmSwXmtAx4XB9275piMcde3odxT7%2BO2f7Ola7ycp6AK6dVr4xWuwVxK9xHCsdM3lxaHdxtzSeg%2F4OeK36W78iGC8GzkJoKKQ%2Bt69Abbp%2FU4gKxdKz5o7B8QLdJQikP%2BmSz8n9Gu6m358w0ZE1INCA7LAiPMpuAWuYMPVl0VtO9ZlkHQ%2BrqoFoGdOgPAqMKUJRzDqdEgTzKqb8OZCbQvExx%2BYCycyxIRI3y4XPGq281hI1TWExKxJsumNMZZN%2BeKW4rxzLKGbmB1APAi6SMajP%2FXMWIk39nn%2FxwkZcjXI9ip3BMkzMwExAsRix7NbtsuKP2X4iH%2FjkIV1kbvIcoOkcUD6dN78sMe9Ae6GuhLFfBUK%2FWOL5duBo%2BxouOPz03lq2zgBLOv%2BenTTeKrddeHfhJioQLWKsDz3AybsWFpX7UkVpPbu1m%2BEEVYu%2BYe3RK1kkatTqA73aXExS2OnqadMmPd4LHw6gM97afzWQS8eT8rhWfjDWElFg0tc0vjbXr12JHE9f6WAQ82IjQMiG%2Fq29OluoueWr1wjw0pHlzHsH221jjQoosw2rcw8I7eyQY6pgHPx%2BroCrqLR4ldlHnSvPf6hKGxvO7yvPxbaxaSX02S%2F6xOJETxkc30X6IjRSQ0DQPwh9JVw3VlwhUaJMwRBJUrcBnlvcUYUeqwcWyqGIh49dVEAnwDyUte%2FY5d1525DEhjOuW81T6eUmOEuQhQGKW%2FoUChekaHbP4MAkWmEFhxC%2F7mctH2jsufulSPAkZ6sPuqejJfbb3MtokNST66HZW60tWHAbf3&X-Amz-Signature=536f5d4775428c7a3986aed8f7f4a00d2cdc4553f6fcfff9eb4e4ee2fa2bfbc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

