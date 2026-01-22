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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QMY7YL3%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCRTmoLG4fn7If6S8xPlZvpH3%2Fs%2FppuX99pn%2FRVOG%2FisQIgeTObBne2nTTQwGUFIgkOjpC18X4urv1nM2UihJZtRvoqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbaEbOlJdssdw%2FRiircA0akVzA9oRiDIrGcXeSAFxooJohiZ%2FotHr%2BZc4DTiNptO%2Br3YNdn%2BXsE0AhAQDm05E7LiZJYJNNZuFKEHNYmjKabWyL1wk95MI00cxrIxZvVDaNLLqBNZaRAl1siNcDfc7FeYx%2FKbYcUf2Vk7kyIrXw%2F4KPilnvivtATzC4WZXnQtGLTDDRD7GU2JaijHiF3mj70YeeqIQPGW5CSo2gKEzQrLjthcOmfEQghe9jdjW3VRGe0dza12sqi5J%2F%2BT4s8zsr24ZmC8Ca21NTvSrpr9Y08ubXjADPCEqOy%2F46UKOqyiz6g%2FmyLkceGhCxYsUS1CZamXXgEquJ5NqPLEEyDAUgmaNdLesbT7xAsngCUG%2Fk1fi6k6yHYWvvl7QXhM81ewN5yFIpOkL5TYFEcFuMbdsakrLd7jC4PdZgd0gBladxl9FQBBj9LttAMDkd9tFuEmkYmHQSql6IF1clFJSJBWHRwIKrvJwyRCzwvUpbUBneUTYAH76Op3gf69R8R34F6w4booIMHO9YRueJPg5MCdWR8C1YkDgMwFDu7oErGJDMgwXY%2F0flewnIximpAXfoKSIOtja%2Bwrcaj5oR7hWNws6exC7Cor5XPQ%2BAuTtPQbq9ZaksFbeFoAluoAQrhMJDXxcsGOqUBX0kvdNBhWHzyQq2h8Ri14ERw47LXJDuFY84lwLZD7BoPLnGMK4afthEasoOaqhu4ml46YhV1abPHjSh%2FK0lRPrhlzl47qO1cuPs1k5vAYVBbx%2FdWRO6D7DtI6GU2QyAdnLQsJ1iN%2F9SFvkcIXOt%2Fc6cZjE2gdAj0hvW%2ByqKTJ8JsLBRH6J0bxzWOpGeKdynuy6D5%2FxnVgAuqMYcFHJylyP%2BKUqrF&X-Amz-Signature=5931ee9f17cf79af52a27f8773c6652b7b2ac8c10fff58d39f42894e5936edfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QMY7YL3%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCRTmoLG4fn7If6S8xPlZvpH3%2Fs%2FppuX99pn%2FRVOG%2FisQIgeTObBne2nTTQwGUFIgkOjpC18X4urv1nM2UihJZtRvoqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbaEbOlJdssdw%2FRiircA0akVzA9oRiDIrGcXeSAFxooJohiZ%2FotHr%2BZc4DTiNptO%2Br3YNdn%2BXsE0AhAQDm05E7LiZJYJNNZuFKEHNYmjKabWyL1wk95MI00cxrIxZvVDaNLLqBNZaRAl1siNcDfc7FeYx%2FKbYcUf2Vk7kyIrXw%2F4KPilnvivtATzC4WZXnQtGLTDDRD7GU2JaijHiF3mj70YeeqIQPGW5CSo2gKEzQrLjthcOmfEQghe9jdjW3VRGe0dza12sqi5J%2F%2BT4s8zsr24ZmC8Ca21NTvSrpr9Y08ubXjADPCEqOy%2F46UKOqyiz6g%2FmyLkceGhCxYsUS1CZamXXgEquJ5NqPLEEyDAUgmaNdLesbT7xAsngCUG%2Fk1fi6k6yHYWvvl7QXhM81ewN5yFIpOkL5TYFEcFuMbdsakrLd7jC4PdZgd0gBladxl9FQBBj9LttAMDkd9tFuEmkYmHQSql6IF1clFJSJBWHRwIKrvJwyRCzwvUpbUBneUTYAH76Op3gf69R8R34F6w4booIMHO9YRueJPg5MCdWR8C1YkDgMwFDu7oErGJDMgwXY%2F0flewnIximpAXfoKSIOtja%2Bwrcaj5oR7hWNws6exC7Cor5XPQ%2BAuTtPQbq9ZaksFbeFoAluoAQrhMJDXxcsGOqUBX0kvdNBhWHzyQq2h8Ri14ERw47LXJDuFY84lwLZD7BoPLnGMK4afthEasoOaqhu4ml46YhV1abPHjSh%2FK0lRPrhlzl47qO1cuPs1k5vAYVBbx%2FdWRO6D7DtI6GU2QyAdnLQsJ1iN%2F9SFvkcIXOt%2Fc6cZjE2gdAj0hvW%2ByqKTJ8JsLBRH6J0bxzWOpGeKdynuy6D5%2FxnVgAuqMYcFHJylyP%2BKUqrF&X-Amz-Signature=e6880ee70f793cc4ea4c0aa228f34506c2e46f161f3c7b846539d1b419908c86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

