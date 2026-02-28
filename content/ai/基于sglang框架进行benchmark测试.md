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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX4VR5UB%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAqHbjHaOjwx3Y%2FJiPKBeOa6F043A0m5eSTTIgtKRkBAiAis1iwXhiCJGBPJrVvmDDsJK0IneviWuZ666WmBZqzZyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMZMscEBKERXP6rBTBKtwDxFe5Bb0y5IhU%2Fnd3ks3JxHzxbHqNexSHaHrq3SuELXzvIAbni%2FGsbQNEcqYI1fcpNvucQM9%2BXK%2BcBo8jRxIFQ%2FuSWAO9UKG1HaW4z%2FyCJaDmQ5Z%2FaHcoAcrPfNWvLQMqfqo8Ksqqwzg6h1oefoDxHSQAQ5qkvFynfcm%2FoAIzE8Yc6B7W2zTGY9us84lDURMIHXCcq08pjnacBP0lI0x0txQkMWvEOsy7mVrc9j3OEYgSACpr%2BULYsL6G2mxpQFUQWET060rD0dfkdpqBTcTTxqBYXVOYKHUf3C%2FvQMvye00u0p6rZahHHZkDgZy0AxJX9r8nC9fErUvB0Lhc1Y0gcm8%2FoST8IlwTfVHdFqjM5FpxKPHWAMWJTiLt8I0MCEjlUk4YTFhBxhJsMYye4B0us7ZqQ%2Fp8kADbYJ7jI6d4gf6UAQ9oyt7pgnc1x%2FC%2BNR9691OzOCdO%2Fwtn0mrQlPD%2FsVxEp8jOq0EQ1wXH61H7ciSsgrm8NZThbRhEEjPY%2FIBEd6VKoq0f4qy4pRmE0x%2Fm7oT%2FrHzWcQ4ayysTysEVZKTP84%2F8K3O6JGoZMzh6HP7q69%2BZfUu%2FG4gHtX5YNqXLD77%2FO9ANRUvjLjISQtk7TowosZIRz08UyWmOIpUwwZaJzQY6pgGU%2FDeN2Qj%2BAOIxDYy3LQ0WnlgCUKSqp0qRouSbJM%2F%2FEfu%2F8wvQnXRlvJ8gcZaIHXjiM07fHE4F138m8%2Bb0odjHglXnPOC0YJRwSBspQGZ4QnYHnGjXXjVt%2BBy0oXMlipx4s8T67gnliAhqAqrPTqqD68RQBn99iyjBFyuqoMa9MXEnycqK%2BJPPt48TYZa%2BwUg4TwxcSMCxvaB17qhFf%2FVyf6MYFn95&X-Amz-Signature=eaab499fb684fd48265390521aef772e546c54652d59a3ce55b895a0260af05d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX4VR5UB%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBAqHbjHaOjwx3Y%2FJiPKBeOa6F043A0m5eSTTIgtKRkBAiAis1iwXhiCJGBPJrVvmDDsJK0IneviWuZ666WmBZqzZyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMZMscEBKERXP6rBTBKtwDxFe5Bb0y5IhU%2Fnd3ks3JxHzxbHqNexSHaHrq3SuELXzvIAbni%2FGsbQNEcqYI1fcpNvucQM9%2BXK%2BcBo8jRxIFQ%2FuSWAO9UKG1HaW4z%2FyCJaDmQ5Z%2FaHcoAcrPfNWvLQMqfqo8Ksqqwzg6h1oefoDxHSQAQ5qkvFynfcm%2FoAIzE8Yc6B7W2zTGY9us84lDURMIHXCcq08pjnacBP0lI0x0txQkMWvEOsy7mVrc9j3OEYgSACpr%2BULYsL6G2mxpQFUQWET060rD0dfkdpqBTcTTxqBYXVOYKHUf3C%2FvQMvye00u0p6rZahHHZkDgZy0AxJX9r8nC9fErUvB0Lhc1Y0gcm8%2FoST8IlwTfVHdFqjM5FpxKPHWAMWJTiLt8I0MCEjlUk4YTFhBxhJsMYye4B0us7ZqQ%2Fp8kADbYJ7jI6d4gf6UAQ9oyt7pgnc1x%2FC%2BNR9691OzOCdO%2Fwtn0mrQlPD%2FsVxEp8jOq0EQ1wXH61H7ciSsgrm8NZThbRhEEjPY%2FIBEd6VKoq0f4qy4pRmE0x%2Fm7oT%2FrHzWcQ4ayysTysEVZKTP84%2F8K3O6JGoZMzh6HP7q69%2BZfUu%2FG4gHtX5YNqXLD77%2FO9ANRUvjLjISQtk7TowosZIRz08UyWmOIpUwwZaJzQY6pgGU%2FDeN2Qj%2BAOIxDYy3LQ0WnlgCUKSqp0qRouSbJM%2F%2FEfu%2F8wvQnXRlvJ8gcZaIHXjiM07fHE4F138m8%2Bb0odjHglXnPOC0YJRwSBspQGZ4QnYHnGjXXjVt%2BBy0oXMlipx4s8T67gnliAhqAqrPTqqD68RQBn99iyjBFyuqoMa9MXEnycqK%2BJPPt48TYZa%2BwUg4TwxcSMCxvaB17qhFf%2FVyf6MYFn95&X-Amz-Signature=f70bd32595a7d34d32b03d9059e7f3e534a81123319f86ed54762cdcf400eb99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

