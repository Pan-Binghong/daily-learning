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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663ZKSMV3%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDO3mo1Y7zDvPuamYDspFwjFYnhLP2uGAo3GY845dGA8AIgYj5jrNLnjmWSLLcDiuf3DZoQftjsL0f6kitV8lNPrsAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJVzFIzsAuvvQzea0yrcA3YyGECt1Ul6X2bHabFuUZqArmnmpVqh2D7ffHDZ4ciIffcfp5LNkaC2AzSd%2BIAK7OVXuL9Xm%2FNeuMGwZQoxIa3TYQ9Z6S2yt5QMlhgIYJW7h5QxcoESKDTM6Ryvj3XEAhzTqtKPadT%2FXc2Jjd5l00r5s5qCs%2BQO87sj3zhBv1wxSMQiqQRyiWGu22K%2F6iELvQCgz96iaXHMhxawHXMKOpck6vZY519rW5leReWAQSWzp3OTqOlMTLdp4ijL29avrVd8daS8axmR%2BKbX%2BsTdJHvRfhmCiyrHLx0stcitIcljAPI%2FDNppEqOqnC82qgxTVufhSrYKiioGNmy6zcC5TzX6K%2FGoEwP5jUYWorKReN1txeZK0Y9D2TdTjHU9lgBB4RIMuvmRIIuzGVZ8DojtZzSgBuX0xijfICI7%2BaNuX6Iwc6y%2BytCXEOq2W2KA70aOS0Wnj4tp6ewWUevR9POc6WLeLf3HdpAD0Tz75QyJMH7iO2rezm16HHIlW8qWs1js7VqJj9r9%2FzP6AhAePasRgG6wP7aQ7F1a7Jzle%2FGcXHGUxQ%2BoCDzZIF%2BRAAkOSw9qLZdzBOEnw7oWccsEHsI5Sjuk9R5JoNIv4vrnr8KAUvbllgymnWyK9E4pexjUMILKp84GOqUBKmSjxDfqe%2BSGlS5g%2FDW%2FdZewPaLvIfVD6qNYiDyKsCFQ2r5rAJx63CBlI7NLfG9b%2FYvbZPRf5sLYBQ3Ve4uVpLdQzSNQp3VwriBS4Ch%2BJvzNBlennYdZbHzSuIHDxgoJdtjOTT%2Fs44m7WFQLGnewG%2BQu8dKgubnjNwY29h%2BaP5nhEFCOuDJCoYM3BMfW5GU%2FAREhQXYN2uN4pw2Kp6vqeAKU%2BjSw&X-Amz-Signature=6979d83099959adaf0ec2888cf9ce310cc1703e3e481511906d59f84c07f61d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663ZKSMV3%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDO3mo1Y7zDvPuamYDspFwjFYnhLP2uGAo3GY845dGA8AIgYj5jrNLnjmWSLLcDiuf3DZoQftjsL0f6kitV8lNPrsAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJVzFIzsAuvvQzea0yrcA3YyGECt1Ul6X2bHabFuUZqArmnmpVqh2D7ffHDZ4ciIffcfp5LNkaC2AzSd%2BIAK7OVXuL9Xm%2FNeuMGwZQoxIa3TYQ9Z6S2yt5QMlhgIYJW7h5QxcoESKDTM6Ryvj3XEAhzTqtKPadT%2FXc2Jjd5l00r5s5qCs%2BQO87sj3zhBv1wxSMQiqQRyiWGu22K%2F6iELvQCgz96iaXHMhxawHXMKOpck6vZY519rW5leReWAQSWzp3OTqOlMTLdp4ijL29avrVd8daS8axmR%2BKbX%2BsTdJHvRfhmCiyrHLx0stcitIcljAPI%2FDNppEqOqnC82qgxTVufhSrYKiioGNmy6zcC5TzX6K%2FGoEwP5jUYWorKReN1txeZK0Y9D2TdTjHU9lgBB4RIMuvmRIIuzGVZ8DojtZzSgBuX0xijfICI7%2BaNuX6Iwc6y%2BytCXEOq2W2KA70aOS0Wnj4tp6ewWUevR9POc6WLeLf3HdpAD0Tz75QyJMH7iO2rezm16HHIlW8qWs1js7VqJj9r9%2FzP6AhAePasRgG6wP7aQ7F1a7Jzle%2FGcXHGUxQ%2BoCDzZIF%2BRAAkOSw9qLZdzBOEnw7oWccsEHsI5Sjuk9R5JoNIv4vrnr8KAUvbllgymnWyK9E4pexjUMILKp84GOqUBKmSjxDfqe%2BSGlS5g%2FDW%2FdZewPaLvIfVD6qNYiDyKsCFQ2r5rAJx63CBlI7NLfG9b%2FYvbZPRf5sLYBQ3Ve4uVpLdQzSNQp3VwriBS4Ch%2BJvzNBlennYdZbHzSuIHDxgoJdtjOTT%2Fs44m7WFQLGnewG%2BQu8dKgubnjNwY29h%2BaP5nhEFCOuDJCoYM3BMfW5GU%2FAREhQXYN2uN4pw2Kp6vqeAKU%2BjSw&X-Amz-Signature=8e709570157331ddaf6bb79968de5814b75feb849e7b5400b2495d2d8d373b88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

