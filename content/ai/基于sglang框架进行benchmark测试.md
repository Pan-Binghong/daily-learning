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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRIF5ZYW%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDl9pVSdl3k3t8zxbSe16x3yshBQU3hJqwHlq%2FUjOtgqwIgCQbmzi3YeLCQSLi8pz%2B7%2FRMKz2w0m0bQa4erRUp%2FSMQqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFeaqxSHX7MzRpWeaSrcA2DPpePu%2BgdWfbSMxUaKRqekeAy2oLkY9DrMigQ8CZRldf0KUb0l6SHeZnqxw54n4bF5YVCGRK4DuW780Atw2KyD2XMzy5IIsgHnpHHr2b%2FOHHOlb%2B7HTaL5i6UOZVmFls6Bo7REZSx5viuvVUlTEm2ryaIlN5mcw9C2AS60xsYbHGBzs2LdItAY0yigmqQofRXcOIy8TPNel2WBhyOO0lHSRBXMqDr5tMAzfylruBzGk0N0NQLQVLRoyQpK7fvgXp6Ag7JnrISW0OLc8lAPZAWfAGVZZ1%2BF8EYEoCTPoDH%2FgsEObj0dZIhfjf%2Fo3r8zibl4lXc%2Ba1Xwxof%2FdGqB8GRlhlJXz30QN0a6FTwTDBZMIlhOndMwv%2FVZgttZoCyKEuofXZTOUdwG9IN%2FzWnUJoIumBHfxs08XhGmgQrs%2FdpIglsgvVoKLlfnTPBYchNdrl0%2Fyqbdi%2BtbU%2F%2BamIbYUiRvypp2Ff1grUru746yrHlcEIDVssMvm0tT3ZQuVQX6EgoaDSaXAWdXGwlHEhQ%2FPUdYT6mMD%2BOuW3oMre3PtzDt4I%2FKhG8mbhijHJzTWzGD9Bs4cbFcPqYpaK5agw3Fdo3TMFs%2Fm5fY0M5If32GpWcKcLiWTHC0mXjcX9tbMK%2BDs8kGOqUBk%2Fk7HrAjYw3yukK1ytAfKHZjywfEpcp8%2FYOUnk6JBd%2By6xnv0Qeg1SwU455qje9KGJ1Rz8bI4lIbpetA4h9bGlNV6OL6m7ryYMGb5PFnMQcALpibksNKLol7DcAasqKLagskWHbKxlLe9tvFf%2F9BbG4Gya9JEgxlpp1xnldQ8MqI4DVsOWcEr8%2F4K%2FDVBEiPxbKeOmL6T8zvGbr5XKVlfFd1Dkde&X-Amz-Signature=cdb8a741ca5c5d4556365898d67bcfd8a5592cd385439cfd61c37a8bb413396c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRIF5ZYW%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDl9pVSdl3k3t8zxbSe16x3yshBQU3hJqwHlq%2FUjOtgqwIgCQbmzi3YeLCQSLi8pz%2B7%2FRMKz2w0m0bQa4erRUp%2FSMQqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFeaqxSHX7MzRpWeaSrcA2DPpePu%2BgdWfbSMxUaKRqekeAy2oLkY9DrMigQ8CZRldf0KUb0l6SHeZnqxw54n4bF5YVCGRK4DuW780Atw2KyD2XMzy5IIsgHnpHHr2b%2FOHHOlb%2B7HTaL5i6UOZVmFls6Bo7REZSx5viuvVUlTEm2ryaIlN5mcw9C2AS60xsYbHGBzs2LdItAY0yigmqQofRXcOIy8TPNel2WBhyOO0lHSRBXMqDr5tMAzfylruBzGk0N0NQLQVLRoyQpK7fvgXp6Ag7JnrISW0OLc8lAPZAWfAGVZZ1%2BF8EYEoCTPoDH%2FgsEObj0dZIhfjf%2Fo3r8zibl4lXc%2Ba1Xwxof%2FdGqB8GRlhlJXz30QN0a6FTwTDBZMIlhOndMwv%2FVZgttZoCyKEuofXZTOUdwG9IN%2FzWnUJoIumBHfxs08XhGmgQrs%2FdpIglsgvVoKLlfnTPBYchNdrl0%2Fyqbdi%2BtbU%2F%2BamIbYUiRvypp2Ff1grUru746yrHlcEIDVssMvm0tT3ZQuVQX6EgoaDSaXAWdXGwlHEhQ%2FPUdYT6mMD%2BOuW3oMre3PtzDt4I%2FKhG8mbhijHJzTWzGD9Bs4cbFcPqYpaK5agw3Fdo3TMFs%2Fm5fY0M5If32GpWcKcLiWTHC0mXjcX9tbMK%2BDs8kGOqUBk%2Fk7HrAjYw3yukK1ytAfKHZjywfEpcp8%2FYOUnk6JBd%2By6xnv0Qeg1SwU455qje9KGJ1Rz8bI4lIbpetA4h9bGlNV6OL6m7ryYMGb5PFnMQcALpibksNKLol7DcAasqKLagskWHbKxlLe9tvFf%2F9BbG4Gya9JEgxlpp1xnldQ8MqI4DVsOWcEr8%2F4K%2FDVBEiPxbKeOmL6T8zvGbr5XKVlfFd1Dkde&X-Amz-Signature=fc2aa08597bf74c02332910b84f58fdd146d3ab64b8b576eb320d8150fbd8add&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

