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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOZ7UGOZ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHPK8rBefG5CCAszQJNNGY23lH%2BhCnzjEDXOVp1xhzV%2BAiBeHElgkSxQiM8foj56ZwH4Jg7wR4b%2BecuT%2BwOxrYaxsir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMu%2FlytII1atF9V%2FxWKtwD0pqxJ%2BTK4ocBYw6CFqs047ZigomlQM8gvR62%2FB13Tzg%2FeMsAu5NWsEVTJmWRWsoBtP8LzbxZsB7K3Vkgv%2FH881P4iewWKf8XHqSOb0FPUl90MTEv2unwMMPgZzcSS5j%2BzM94u1N4m6rM6mkWuLgzPlPe%2FIwxaEeKrize%2BJGPeX0%2FgEMFtU28TOFANoho7VJ43BGxo8olHlaQWabL2N%2BhkQZDkBQ2PInN6nnhlhD6qoi3CJHroCacB%2BWJMIWlQ9LECXEzIOYQ2dxb7oLetm5%2FofzRpo2jNYxMxfgAYTgP8jMOvXRg7%2BRQ380%2FM5ilIkwWrzKZKTBlAvNpsY%2BdNy1U4QShWWd%2B2z8PUOzvCpzeUenHiLY6N0kB9y3LIaCup38izQB6nbWs6yhvuEloyfHnYQXG%2Bq2IEHqLR3a%2FLj%2FDPDDfQwUKETh30t%2BTpQL5GqDwgMZOq1Q2MdKWSCZtRiFIHSVW07An24nwwgN4gE1lwB%2FVIHtCZhp4LIoVdxl%2BPd75XRK2DmkQAX4d00Sqa7sQ4lwsybx7Szq6cz%2Fkruw2JbSqBNyle0rPhmupSwWKwfAlZvi6V551EfcSflZf4XJGnxS54tdNovzOEBVn0hPeQEmhjikW4jdDTfzQJqEwpcDDzQY6pgGl1HqqvS%2Bqc%2Fv7YeCD51nXDPXzyzkxLgscqj3MZzXRvLrX67zINuN4la6Y%2Frnx65c4NPf7i8nHhfQ7bon4PHnwpcOnrGmtY3QN%2BCC9bjS1QaBAFZZVs41zFg51fQX6%2BGANHnQ%2FoGPtzK1ejAMU%2BjJPm1nhuGm%2BY7hg0hfX8e3s16kND3dvXvcN5dUWA%2B5KMCbxOHwdRxAnptWtYb7ULHyvym87WJ4%2B&X-Amz-Signature=42abb0fb6c8eca80ca26f4e0c3378678e7f9c5e6185771a6c882d6585dade7fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOZ7UGOZ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHPK8rBefG5CCAszQJNNGY23lH%2BhCnzjEDXOVp1xhzV%2BAiBeHElgkSxQiM8foj56ZwH4Jg7wR4b%2BecuT%2BwOxrYaxsir%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMu%2FlytII1atF9V%2FxWKtwD0pqxJ%2BTK4ocBYw6CFqs047ZigomlQM8gvR62%2FB13Tzg%2FeMsAu5NWsEVTJmWRWsoBtP8LzbxZsB7K3Vkgv%2FH881P4iewWKf8XHqSOb0FPUl90MTEv2unwMMPgZzcSS5j%2BzM94u1N4m6rM6mkWuLgzPlPe%2FIwxaEeKrize%2BJGPeX0%2FgEMFtU28TOFANoho7VJ43BGxo8olHlaQWabL2N%2BhkQZDkBQ2PInN6nnhlhD6qoi3CJHroCacB%2BWJMIWlQ9LECXEzIOYQ2dxb7oLetm5%2FofzRpo2jNYxMxfgAYTgP8jMOvXRg7%2BRQ380%2FM5ilIkwWrzKZKTBlAvNpsY%2BdNy1U4QShWWd%2B2z8PUOzvCpzeUenHiLY6N0kB9y3LIaCup38izQB6nbWs6yhvuEloyfHnYQXG%2Bq2IEHqLR3a%2FLj%2FDPDDfQwUKETh30t%2BTpQL5GqDwgMZOq1Q2MdKWSCZtRiFIHSVW07An24nwwgN4gE1lwB%2FVIHtCZhp4LIoVdxl%2BPd75XRK2DmkQAX4d00Sqa7sQ4lwsybx7Szq6cz%2Fkruw2JbSqBNyle0rPhmupSwWKwfAlZvi6V551EfcSflZf4XJGnxS54tdNovzOEBVn0hPeQEmhjikW4jdDTfzQJqEwpcDDzQY6pgGl1HqqvS%2Bqc%2Fv7YeCD51nXDPXzyzkxLgscqj3MZzXRvLrX67zINuN4la6Y%2Frnx65c4NPf7i8nHhfQ7bon4PHnwpcOnrGmtY3QN%2BCC9bjS1QaBAFZZVs41zFg51fQX6%2BGANHnQ%2FoGPtzK1ejAMU%2BjJPm1nhuGm%2BY7hg0hfX8e3s16kND3dvXvcN5dUWA%2B5KMCbxOHwdRxAnptWtYb7ULHyvym87WJ4%2B&X-Amz-Signature=d00b88aa0faeb64a33fd0d2a39c81b00ad120d72a007492951f6fb5afe3d83c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

