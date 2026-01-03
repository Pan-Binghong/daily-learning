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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZKYL66I%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQDkNeYFv0L4PNMWWCtbBHACQU4M3XHsWqNrnvH6W10qJgIgL1%2F5Z%2B1iSoQK%2Ftv0u3sKDTPZaII5PWAlkcZWLeBhrFQq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDMfgPAPxscXxdeSKvyrcA%2Fa%2Fw%2FSpZ530wvPGGIhzLOD8qCsiAKDtfb3p7i%2Ftj9XFL8L1YNh1TLE3QIIg3JiOXm7Nj%2B%2Bm3PB0EUvQ0U9JgcDqKTFcn21xr6tcJrkgaCJHuZ4NAOrieHZ8BTBBsZd6YtM6hofZJlSuchXxJfntdnnp3XV513Xe9ffrxXy014yeEM2Lq%2BfTZ6LOuban68hxEWp3ZxTeNWeZqbzwcGp5GC9L5PVkhAeb7A2zvHz5EOp8n7CRpfMdGgxf%2BYVSHB1lC8wgFA8B7yTC9cPynvm4x9Y7%2FMra2ZxwHePrN7rP5K4wY10JVaXAdrH4gW989miq%2FkD3XavgUGSMjvSdoSpYzLXxfPJLPu33Vl%2Fw4iLzb7d9uUiMz%2F%2B8LOVrNgfOss2JeQ9cO%2FxAxHJAtLInHQn0D7LRTICvb2FXqoL4pt5i5AVx4WZc2ktCrf6ihmAerlu9fD1%2F5ICCh0jHX3kiuJnoLwS1j1Jcz%2FFiAXqqbvnLp%2BpiEkUg9Fa%2BQ5Q69kUy9j3cO0uUJgMvD5WaTT1x8jhWOZ7xfQYc0k3Suxg7ayEgo1h4c58MX%2FtN8gSzypoTu3te8M%2BJAU90o2%2FU%2BSg3ghQuGI7qc7evivJSBeN%2FBImVsE0H%2FXVdLoe441lm%2FrlJMLXw4coGOqUBHK%2FO7%2FhucoCJNk95%2FobTq6hxa7hMgHRLE6STEipIxRNgmi6wrK%2ByTaXau2JHyq8B%2BdWOS7PHyOhgrUQQ8x3N4r78cymOWOp2WkOTr2xx2ZhzNcrOt%2F%2FGBDP1urtEWeK%2B6HQObgSHmjR4TnYVL0yf7vAFCdoe0fSb1ZdYCAsWiFxP8aHgrza7mfqg9BgEfgS7DqskV2M0kMQj12QqIzjjOlDnDuV5&X-Amz-Signature=a9044f0850e9fb65fb4a4ede4f55bf9bfa87247318307d7ad94aee93c1a349de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZKYL66I%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQDkNeYFv0L4PNMWWCtbBHACQU4M3XHsWqNrnvH6W10qJgIgL1%2F5Z%2B1iSoQK%2Ftv0u3sKDTPZaII5PWAlkcZWLeBhrFQq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDMfgPAPxscXxdeSKvyrcA%2Fa%2Fw%2FSpZ530wvPGGIhzLOD8qCsiAKDtfb3p7i%2Ftj9XFL8L1YNh1TLE3QIIg3JiOXm7Nj%2B%2Bm3PB0EUvQ0U9JgcDqKTFcn21xr6tcJrkgaCJHuZ4NAOrieHZ8BTBBsZd6YtM6hofZJlSuchXxJfntdnnp3XV513Xe9ffrxXy014yeEM2Lq%2BfTZ6LOuban68hxEWp3ZxTeNWeZqbzwcGp5GC9L5PVkhAeb7A2zvHz5EOp8n7CRpfMdGgxf%2BYVSHB1lC8wgFA8B7yTC9cPynvm4x9Y7%2FMra2ZxwHePrN7rP5K4wY10JVaXAdrH4gW989miq%2FkD3XavgUGSMjvSdoSpYzLXxfPJLPu33Vl%2Fw4iLzb7d9uUiMz%2F%2B8LOVrNgfOss2JeQ9cO%2FxAxHJAtLInHQn0D7LRTICvb2FXqoL4pt5i5AVx4WZc2ktCrf6ihmAerlu9fD1%2F5ICCh0jHX3kiuJnoLwS1j1Jcz%2FFiAXqqbvnLp%2BpiEkUg9Fa%2BQ5Q69kUy9j3cO0uUJgMvD5WaTT1x8jhWOZ7xfQYc0k3Suxg7ayEgo1h4c58MX%2FtN8gSzypoTu3te8M%2BJAU90o2%2FU%2BSg3ghQuGI7qc7evivJSBeN%2FBImVsE0H%2FXVdLoe441lm%2FrlJMLXw4coGOqUBHK%2FO7%2FhucoCJNk95%2FobTq6hxa7hMgHRLE6STEipIxRNgmi6wrK%2ByTaXau2JHyq8B%2BdWOS7PHyOhgrUQQ8x3N4r78cymOWOp2WkOTr2xx2ZhzNcrOt%2F%2FGBDP1urtEWeK%2B6HQObgSHmjR4TnYVL0yf7vAFCdoe0fSb1ZdYCAsWiFxP8aHgrza7mfqg9BgEfgS7DqskV2M0kMQj12QqIzjjOlDnDuV5&X-Amz-Signature=30978d296196ee597277e1ca97c5e2c7506d45ac634c43d16a4ac952a7d552e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

