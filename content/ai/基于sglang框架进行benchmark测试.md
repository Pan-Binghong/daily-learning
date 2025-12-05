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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM44OPNQ%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfAmbiKn33rc3H0UwqjoRZgaRC2P0N18iWvuYXhBi6fgIhAP17S1V5n8B2HVdSFUX28JQ03%2FaArOtUHBqiwn%2BVGmZ5Kv8DCE8QABoMNjM3NDIzMTgzODA1IgxCkQ98I2uJ0KFqQNYq3APMgojNQunTuLIu3M91CQScGVHPI4ZOg0jp9HYld7GljYr5ab1pZ1p7YW0WqX7tMWU%2BIh%2FcHTyXMspqsZmNoOBhAm3kztxijafPXdQwTYH8hmzF1W%2FFh%2BKXL3%2By3j3k6LIMbwh943KbS%2BA2H26TlSsMYBQDY7HuH4Z2msSqoQB1n0B3r1HM9Whr9CJQxWQ5mD1EMPVaa4tFLHZfafe1BO%2F%2BnP9UWMAjyXlQmRch2LTq%2FBBHboeVZ%2FhEk5MxjesYLsw%2BmFTe%2FVzeSProahtFxOaNVT%2FudLcSxc4Vdy%2BO%2Bi%2Br0obO5SwTnISo9sMf1P3D2YrGjYDJDqQvqJYJBuOsedphMaX%2FHScMI6iXXP9gXSc6Ks5tmS95cuEKSyIg6B%2B7jUU2XTLv%2Fv5PRbtYc1pa6hPFrVqrxCxo6GTpeNWWksJ92vWfukh11HfUUeQ2%2F83Z9Jo%2F4IaYtJT7gFcGcGFw1vKxMsfAL5qoOFzplW1ErnWEgS6xab5WIf%2Bk4Xaqfo%2F1DLoipKNzp6dirxG2nPwwOpZuMXojyoz8A3Di4pjOeDOeA4ToQ5hC%2B%2Bp%2F1%2BPet7W6lg0xkaOYiFJnD02RMbRlw5ISy4zv3BbClEEsDBk3Hj9WSRCy3gZ4E0tptbGsNzCXjMjJBjqkAQgwb1weh0bS88lTlEw%2F3sHxI%2Bf71Rb5e3KZ1z0MGTT7pK2xqbkdpFocD5irwsEjXRtzI8rorMLozI8ipO%2BKltDiiv5mYb5R8z588L1towyKbrRBwGqShWz6P2G%2FjLsmMtS3%2BAWd%2BPqW5c7Oae12ZhGfhZkFH1iMGIcQoC4nrGOWQOTOuT2botCMTM6RjydHnzTqdUiiRKrq7s4ysr3J%2FJUr%2BrXX&X-Amz-Signature=704d15979d983d38cc41ee8308cee85492112b75101228fb13a7449732dbe175&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM44OPNQ%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfAmbiKn33rc3H0UwqjoRZgaRC2P0N18iWvuYXhBi6fgIhAP17S1V5n8B2HVdSFUX28JQ03%2FaArOtUHBqiwn%2BVGmZ5Kv8DCE8QABoMNjM3NDIzMTgzODA1IgxCkQ98I2uJ0KFqQNYq3APMgojNQunTuLIu3M91CQScGVHPI4ZOg0jp9HYld7GljYr5ab1pZ1p7YW0WqX7tMWU%2BIh%2FcHTyXMspqsZmNoOBhAm3kztxijafPXdQwTYH8hmzF1W%2FFh%2BKXL3%2By3j3k6LIMbwh943KbS%2BA2H26TlSsMYBQDY7HuH4Z2msSqoQB1n0B3r1HM9Whr9CJQxWQ5mD1EMPVaa4tFLHZfafe1BO%2F%2BnP9UWMAjyXlQmRch2LTq%2FBBHboeVZ%2FhEk5MxjesYLsw%2BmFTe%2FVzeSProahtFxOaNVT%2FudLcSxc4Vdy%2BO%2Bi%2Br0obO5SwTnISo9sMf1P3D2YrGjYDJDqQvqJYJBuOsedphMaX%2FHScMI6iXXP9gXSc6Ks5tmS95cuEKSyIg6B%2B7jUU2XTLv%2Fv5PRbtYc1pa6hPFrVqrxCxo6GTpeNWWksJ92vWfukh11HfUUeQ2%2F83Z9Jo%2F4IaYtJT7gFcGcGFw1vKxMsfAL5qoOFzplW1ErnWEgS6xab5WIf%2Bk4Xaqfo%2F1DLoipKNzp6dirxG2nPwwOpZuMXojyoz8A3Di4pjOeDOeA4ToQ5hC%2B%2Bp%2F1%2BPet7W6lg0xkaOYiFJnD02RMbRlw5ISy4zv3BbClEEsDBk3Hj9WSRCy3gZ4E0tptbGsNzCXjMjJBjqkAQgwb1weh0bS88lTlEw%2F3sHxI%2Bf71Rb5e3KZ1z0MGTT7pK2xqbkdpFocD5irwsEjXRtzI8rorMLozI8ipO%2BKltDiiv5mYb5R8z588L1towyKbrRBwGqShWz6P2G%2FjLsmMtS3%2BAWd%2BPqW5c7Oae12ZhGfhZkFH1iMGIcQoC4nrGOWQOTOuT2botCMTM6RjydHnzTqdUiiRKrq7s4ysr3J%2FJUr%2BrXX&X-Amz-Signature=5db85605445b63202ee9fadc8eb3eaa4bed843ce9b2e76a66e8fb354976d3661&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

