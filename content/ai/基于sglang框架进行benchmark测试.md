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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664X3YTZW7%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIFQlKFIV%2F6Vmh5kEpRyks8%2F%2BbACpKikjO1wTDqjVuHW9AiEA7axPbljbjbxm5NQm%2BhqqrfhKhoLcXdPGHV2QQAN%2FyZEqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJl%2Fem4vdUtEtlfdCrcA%2BSxv93jdAqBmJ2aHSvlSQ45XPozYBR2Ny0TYz%2F5MXH%2F03ETy7ALUq6C%2FWrmbBQcz2nSex6MQfIFwBcXSmo3uJOm%2F%2BBLEXiOiNyKYu9GycMnnSZkmwfRNB6jhYbte%2F8q9aK5k0x7PSwsnBIrfE8LpP5BVoGGL5pJZ6qbjVcddzLTVjDkPU2DdEIXliVJksOvr22BiN6DJQcVQlJKcsJZ1UFXQRaUJnRXqb0PmqXjeJDyXR5eUN1pia7rLciHQiDwoYY60zOTKMp1qjheCD8sl%2B3pVfesbkx%2BO6fczIOfXwPR9ob228XAptC9DR9aik961OQh5BcS9oagnMbp8sebzCz%2BDtDr6O%2BKwedQxJTVLsEqoH9sUfSJ3lZUjzP7h6lfro6X9tnyXzlcSt2wu5x%2BrUkEZhcQNIZ3VJilvZz6y7tZ6qEJ8uT5GWR%2BOYea4Y4kHWEM7IS2KzfTpaYFADtP5KAnqXxypATSyNJcAw3OXosq8wrRxcfnmu22TO%2FmS4JGa%2F%2FigT2NC2UUjj8xl1X7ROFlXJHruY%2FydrUZ7vWMaNPv1GzAL0zNIUWDt8qKuG2qRIjdNgoJg8Wy1DmMNIW2%2FLsR9CawQc4oxWQ9Ig%2BApMlpL%2BBbNgH7yyM8WxtdMOq5uswGOqUBjBK%2Bvqj%2BqcwMdofpIY8ZuFE%2B11LVStwPEMcq0tWI5c3eAf0FeUaeVdnQSkrZ%2B740dT8PiuM%2FMZHmTSwY21umPH9TIKmMYvDr2Vjo2bR8IFDk%2F1sBhgu1PjAsOJQjYpF7SIeMjKTFfoGWlnDSfRtLOoDgu8RBDF2Db%2Bmd8N4ipnvFYwUSNvo6m%2BaXCXPV%2B6C%2FwDNH6Iu8S6C5s39Em%2FL62vnKAqn%2B&X-Amz-Signature=fd4d7e37c586b27f95c5b53e76bdb440d6de48f273e12bcf0f3bdd243f9ee04e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664X3YTZW7%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIFQlKFIV%2F6Vmh5kEpRyks8%2F%2BbACpKikjO1wTDqjVuHW9AiEA7axPbljbjbxm5NQm%2BhqqrfhKhoLcXdPGHV2QQAN%2FyZEqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJl%2Fem4vdUtEtlfdCrcA%2BSxv93jdAqBmJ2aHSvlSQ45XPozYBR2Ny0TYz%2F5MXH%2F03ETy7ALUq6C%2FWrmbBQcz2nSex6MQfIFwBcXSmo3uJOm%2F%2BBLEXiOiNyKYu9GycMnnSZkmwfRNB6jhYbte%2F8q9aK5k0x7PSwsnBIrfE8LpP5BVoGGL5pJZ6qbjVcddzLTVjDkPU2DdEIXliVJksOvr22BiN6DJQcVQlJKcsJZ1UFXQRaUJnRXqb0PmqXjeJDyXR5eUN1pia7rLciHQiDwoYY60zOTKMp1qjheCD8sl%2B3pVfesbkx%2BO6fczIOfXwPR9ob228XAptC9DR9aik961OQh5BcS9oagnMbp8sebzCz%2BDtDr6O%2BKwedQxJTVLsEqoH9sUfSJ3lZUjzP7h6lfro6X9tnyXzlcSt2wu5x%2BrUkEZhcQNIZ3VJilvZz6y7tZ6qEJ8uT5GWR%2BOYea4Y4kHWEM7IS2KzfTpaYFADtP5KAnqXxypATSyNJcAw3OXosq8wrRxcfnmu22TO%2FmS4JGa%2F%2FigT2NC2UUjj8xl1X7ROFlXJHruY%2FydrUZ7vWMaNPv1GzAL0zNIUWDt8qKuG2qRIjdNgoJg8Wy1DmMNIW2%2FLsR9CawQc4oxWQ9Ig%2BApMlpL%2BBbNgH7yyM8WxtdMOq5uswGOqUBjBK%2Bvqj%2BqcwMdofpIY8ZuFE%2B11LVStwPEMcq0tWI5c3eAf0FeUaeVdnQSkrZ%2B740dT8PiuM%2FMZHmTSwY21umPH9TIKmMYvDr2Vjo2bR8IFDk%2F1sBhgu1PjAsOJQjYpF7SIeMjKTFfoGWlnDSfRtLOoDgu8RBDF2Db%2Bmd8N4ipnvFYwUSNvo6m%2BaXCXPV%2B6C%2FwDNH6Iu8S6C5s39Em%2FL62vnKAqn%2B&X-Amz-Signature=53eb165bb1833b2902c580539a4a8556f5506e8c94eb0ebdb32b5700165055d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

