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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVAGYZE%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDqCcN1D2dSjcne2QRzQ0WOMQt9GPdWQsSDiQw72P2DJgIgd%2F2d%2BNGqw6K%2BLJBFaaw5Z4unMTH7GjSOJTS7mkau%2BjQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIQFIcH9dNe1LVuRyrcA06N8wm1daGrZ%2FgJM8U5fujAJS5Zf2to1PY86dk6QmSJiPBzmCSvYu7Av4LbdBx4mF9XBvc7AYpj6UFtGJOSaALEYYypZDYA8ZNz0MG1cBlFRb2NblfY%2BRyxYy%2BfeUu16U1dd%2BNhK28uUTqBtCbenpqdffFFABgDaytS9xl6WVuBqZwTjXpKmElp0Q03LUeiORdVL5Hw%2FxUPV3ZgDkUuy0Z9HZ3y8Y7%2BvZz8a%2FkDJDTpv8l4m9osR59Z8zkiJMRTz92kQyGALzqLOkYTsapQ80ZjzA2pYnO181KlwAv581EQ700yMJBx0TS%2FXO33mUBCvKgNOB%2F3bBC8gwibNERMtI9d96NxLSDJQlFEePDrtwUYVkOrLwL5un%2B88xfTQrvqnRGV0hmuCH%2B1osZKGNgE4SINcqQw3PHuHpluEDhRvQvvrP3xzVklzo95kzwAA7HiCto1hX5bxjuO6ziKr0kWckrKB1Z1i%2BuQXOKGFaLIcFr8eCN8FhD0P41UY04oZsDV63ZCxtNNYLVETItyrKx9BygQiACflcuYKe9CG3qLarNjtqB5MZ%2B3qNVO6R6rr24ajVYoygGDPe1J7Ff4edUqD0kYQvVc3JA2vl8cJu6lVlm3nE5Ma%2FfXOcl0iGL7MILXrckGOqUBjTYHTNypKmj%2B4q1m7nooXalchnnSXv9UHf8Je%2FAzEdR50DOQDAKTVsEItoVAMkli9hhHbLp61cdlT1xLmnbRWrx0InFiZjeQKzNKWV8B5z27XyIxnzAZIcFtFo4sGC%2FIji9Nndxy7MWd38hEDoTuh3DpaYgr7LGEx9NO9xAv1SJIXcPsCZ%2BAR0VVRkV09aqFYdN1EijBMwxje6fRQjw6C2JB4tLz&X-Amz-Signature=c5db51ac4fd92f0b9ba32e23f284175d1cb4d53dc26c85c4d97a4ed4e89815f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQVAGYZE%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDqCcN1D2dSjcne2QRzQ0WOMQt9GPdWQsSDiQw72P2DJgIgd%2F2d%2BNGqw6K%2BLJBFaaw5Z4unMTH7GjSOJTS7mkau%2BjQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAIQFIcH9dNe1LVuRyrcA06N8wm1daGrZ%2FgJM8U5fujAJS5Zf2to1PY86dk6QmSJiPBzmCSvYu7Av4LbdBx4mF9XBvc7AYpj6UFtGJOSaALEYYypZDYA8ZNz0MG1cBlFRb2NblfY%2BRyxYy%2BfeUu16U1dd%2BNhK28uUTqBtCbenpqdffFFABgDaytS9xl6WVuBqZwTjXpKmElp0Q03LUeiORdVL5Hw%2FxUPV3ZgDkUuy0Z9HZ3y8Y7%2BvZz8a%2FkDJDTpv8l4m9osR59Z8zkiJMRTz92kQyGALzqLOkYTsapQ80ZjzA2pYnO181KlwAv581EQ700yMJBx0TS%2FXO33mUBCvKgNOB%2F3bBC8gwibNERMtI9d96NxLSDJQlFEePDrtwUYVkOrLwL5un%2B88xfTQrvqnRGV0hmuCH%2B1osZKGNgE4SINcqQw3PHuHpluEDhRvQvvrP3xzVklzo95kzwAA7HiCto1hX5bxjuO6ziKr0kWckrKB1Z1i%2BuQXOKGFaLIcFr8eCN8FhD0P41UY04oZsDV63ZCxtNNYLVETItyrKx9BygQiACflcuYKe9CG3qLarNjtqB5MZ%2B3qNVO6R6rr24ajVYoygGDPe1J7Ff4edUqD0kYQvVc3JA2vl8cJu6lVlm3nE5Ma%2FfXOcl0iGL7MILXrckGOqUBjTYHTNypKmj%2B4q1m7nooXalchnnSXv9UHf8Je%2FAzEdR50DOQDAKTVsEItoVAMkli9hhHbLp61cdlT1xLmnbRWrx0InFiZjeQKzNKWV8B5z27XyIxnzAZIcFtFo4sGC%2FIji9Nndxy7MWd38hEDoTuh3DpaYgr7LGEx9NO9xAv1SJIXcPsCZ%2BAR0VVRkV09aqFYdN1EijBMwxje6fRQjw6C2JB4tLz&X-Amz-Signature=40518d7d5ab99f738b07b6c395a9a6c3645456fb22582d9b4370f533b62c6a06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

