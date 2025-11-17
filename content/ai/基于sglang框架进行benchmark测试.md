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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646LAKRFE%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYf45S%2FRQWTcwfJT0525EUF5Rqi2H0v83RDom8TcsUHwIhAJCujZLnNXy9keIC4F%2Bdb6MAZPFPafIPnOpPsX8LrK5GKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZVgrO8930zXuV4vsq3APZ2dNFVpLQoZS6IvnM3DKQBSN9vaGwi%2BYaPlJMe4JOVTbx1tQo1Vjpvw73CltK594Bt8jADnHsG10HiUc3m62eP5KYU544X0OR%2BIdAVO5UrYthlpzBOch1GtQffo5OkP1jSbK0%2Fz9whj1a3YIvD13iT%2BOTGlKG%2FrZGVKYmlhEbYo2j49RFoVVQ%2BFPw0WIKtbptTNUye%2FnmOZurn3aQSqlTKOSlQhD7bH7yOa05yXgv6EDiMbuvDSZMNNg4c5C2Lt6GQ7ItZPr4tgZEWmcS6NY09eLERFxAig10g64HsG0ZNBmVQIE2MncAgDicyRHkK%2B%2FaAhecpTenzxhNB%2F4zuAXl9gpV04vweW%2B1K9q4b2Oo8wjmtf1YbEk7f2lVOaNcP8yv3zvseuuoGnxhaKsRmnyBSQl1roRmi71psGcoLZ8tGj54teXiqktnK5ank1zo%2FWRX2g2G0M66kIWHeHyWZsY4a3LPZx8ZPMYU4O3JbqMh59bgM40b196cYVcNWhIy0TuI%2BsdA154r0ZeJQuADfnPgg1jO6l4X%2BUH9qgd26a%2FVP93GfkHcDTu3HUk9xdm%2B%2FpOzjyRJf5EWAYKcoAGqEEuhog7EmN9z1DCnjk%2Fj9U3RtmbuTYiMp8ImC8qo1DCVh%2BrIBjqkAQFFXSh3AgyhsJbUImvfx%2Fgfe%2Beqdh809zDbT7Zajdoq%2FmfZrrianopIBWllQb71Muk3rG%2Fzq2ECznvN3DgwFjv%2BdDiOryooRg3NT67IHN4O%2BhWNqphd0kJQBYq%2BPiojfQHrq0O46tDFoeWg4eMIRCKW4snTYTeVgCZ7tFhsbj9rAHqh58qZIO4IbV2x74qxLF4qD738p%2FD%2BA2X%2BJupqEgvMe93N&X-Amz-Signature=6ff41a493d2b3e998797f6aa2d0644d6629697cf3d35acd3fff5f3d33c8686a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646LAKRFE%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYf45S%2FRQWTcwfJT0525EUF5Rqi2H0v83RDom8TcsUHwIhAJCujZLnNXy9keIC4F%2Bdb6MAZPFPafIPnOpPsX8LrK5GKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZVgrO8930zXuV4vsq3APZ2dNFVpLQoZS6IvnM3DKQBSN9vaGwi%2BYaPlJMe4JOVTbx1tQo1Vjpvw73CltK594Bt8jADnHsG10HiUc3m62eP5KYU544X0OR%2BIdAVO5UrYthlpzBOch1GtQffo5OkP1jSbK0%2Fz9whj1a3YIvD13iT%2BOTGlKG%2FrZGVKYmlhEbYo2j49RFoVVQ%2BFPw0WIKtbptTNUye%2FnmOZurn3aQSqlTKOSlQhD7bH7yOa05yXgv6EDiMbuvDSZMNNg4c5C2Lt6GQ7ItZPr4tgZEWmcS6NY09eLERFxAig10g64HsG0ZNBmVQIE2MncAgDicyRHkK%2B%2FaAhecpTenzxhNB%2F4zuAXl9gpV04vweW%2B1K9q4b2Oo8wjmtf1YbEk7f2lVOaNcP8yv3zvseuuoGnxhaKsRmnyBSQl1roRmi71psGcoLZ8tGj54teXiqktnK5ank1zo%2FWRX2g2G0M66kIWHeHyWZsY4a3LPZx8ZPMYU4O3JbqMh59bgM40b196cYVcNWhIy0TuI%2BsdA154r0ZeJQuADfnPgg1jO6l4X%2BUH9qgd26a%2FVP93GfkHcDTu3HUk9xdm%2B%2FpOzjyRJf5EWAYKcoAGqEEuhog7EmN9z1DCnjk%2Fj9U3RtmbuTYiMp8ImC8qo1DCVh%2BrIBjqkAQFFXSh3AgyhsJbUImvfx%2Fgfe%2Beqdh809zDbT7Zajdoq%2FmfZrrianopIBWllQb71Muk3rG%2Fzq2ECznvN3DgwFjv%2BdDiOryooRg3NT67IHN4O%2BhWNqphd0kJQBYq%2BPiojfQHrq0O46tDFoeWg4eMIRCKW4snTYTeVgCZ7tFhsbj9rAHqh58qZIO4IbV2x74qxLF4qD738p%2FD%2BA2X%2BJupqEgvMe93N&X-Amz-Signature=4162e9cc63bff4e1ebf8293c1db80f4876ff87f6a12ff9117f04842c729747c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

