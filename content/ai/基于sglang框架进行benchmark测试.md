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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Y7YCLRF%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFWKJt7iA5veiQ%2FkpfBpGZOSuZjMWtIJOguliTJcOq2AiEAgP%2Fa%2FaCAd9oMcP2hZXh5vBhRZhBc2a1qLs9VAXykEAYqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTS9a7M%2FaQpNi3itCrcA%2BZxTWe9q%2FZf0fN8Ur0CAvMMBnXhdaKNj3v3dS2O6G2qcn18DZ%2Blm4h5Qj48Qci7QCD3hGy%2FuB1IOIDdMScain7kiqLzm0ZxudTGuPysd7n9eKrtljCjYKHxMGRQVqzLFAA%2BW%2F29AxD5nv6795hVESPpxRScE8mcmSEaGa2%2FCHVnW1EFktTZvBPuCLxPJtzvwJI0S4V%2B2dcFIIgcGccs5oriFR86n6MC7jr0k%2BtS6%2F4QKn4jWgZ%2FlB75I5y0HlekkI0pVaNlND4sta9V7Lc4N6o%2BH5vlxHH%2Bhv0Fjp9%2FWmgiCBJng2I3D4WNx0dieqxnWmnXw26g%2FcJvlCe2B6LJ%2BAn%2BJIs97%2FWToGDSVTAIKwFhwR%2FjmWA0MsWPP%2FxXINMKWa9f3maJAL2ini8PMKZdrJ%2FTSvUTYNDTLhuqwLGunK5wB7hmxwAdbnJNzIWQdgr%2FrKB2ONWnPWFwAfRIT1Qh2IoD605Ajm8Mi%2BI3q2nxdFciOxJqYszmVATCwTH07BaJN8FA17k%2BElDpRMiL4o1ftD1NFisN6TTs7u5L60K9%2FMk0m%2FkiPWlKkvo9lvtwqOma1Brgf79PnIEmn8yzJqRpGLx2iNhfmpCxzR%2FZnzS%2BDWoZaHclIHxmy2RDnVkJMPCUqckGOqUBgw0CrPziDE9aWbqJ9Tp4%2FYF%2FCclPQXGEKEHuvnNCZauap9GNE789AkaVjM1b34mHrbNzW9M5IDGD1AcFCRSOZPgGuz%2FDVA%2Fk2Px7UCKJw45SQ%2FygJ5pQjLhFmgyLcm9Ci7TPHmNdALYKWAc7PJtNxehKZHSKMPgdCAuqJLJLv68ArMryTz%2BFiHENIYnhN6Ys15vTSBT6li%2FLpWE7oGKIgCZCZJbp&X-Amz-Signature=dd8692f08bdaf41ebd49aa5aebda8d78ef948d6a293d44440427ac963bba35de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Y7YCLRF%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFWKJt7iA5veiQ%2FkpfBpGZOSuZjMWtIJOguliTJcOq2AiEAgP%2Fa%2FaCAd9oMcP2hZXh5vBhRZhBc2a1qLs9VAXykEAYqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTS9a7M%2FaQpNi3itCrcA%2BZxTWe9q%2FZf0fN8Ur0CAvMMBnXhdaKNj3v3dS2O6G2qcn18DZ%2Blm4h5Qj48Qci7QCD3hGy%2FuB1IOIDdMScain7kiqLzm0ZxudTGuPysd7n9eKrtljCjYKHxMGRQVqzLFAA%2BW%2F29AxD5nv6795hVESPpxRScE8mcmSEaGa2%2FCHVnW1EFktTZvBPuCLxPJtzvwJI0S4V%2B2dcFIIgcGccs5oriFR86n6MC7jr0k%2BtS6%2F4QKn4jWgZ%2FlB75I5y0HlekkI0pVaNlND4sta9V7Lc4N6o%2BH5vlxHH%2Bhv0Fjp9%2FWmgiCBJng2I3D4WNx0dieqxnWmnXw26g%2FcJvlCe2B6LJ%2BAn%2BJIs97%2FWToGDSVTAIKwFhwR%2FjmWA0MsWPP%2FxXINMKWa9f3maJAL2ini8PMKZdrJ%2FTSvUTYNDTLhuqwLGunK5wB7hmxwAdbnJNzIWQdgr%2FrKB2ONWnPWFwAfRIT1Qh2IoD605Ajm8Mi%2BI3q2nxdFciOxJqYszmVATCwTH07BaJN8FA17k%2BElDpRMiL4o1ftD1NFisN6TTs7u5L60K9%2FMk0m%2FkiPWlKkvo9lvtwqOma1Brgf79PnIEmn8yzJqRpGLx2iNhfmpCxzR%2FZnzS%2BDWoZaHclIHxmy2RDnVkJMPCUqckGOqUBgw0CrPziDE9aWbqJ9Tp4%2FYF%2FCclPQXGEKEHuvnNCZauap9GNE789AkaVjM1b34mHrbNzW9M5IDGD1AcFCRSOZPgGuz%2FDVA%2Fk2Px7UCKJw45SQ%2FygJ5pQjLhFmgyLcm9Ci7TPHmNdALYKWAc7PJtNxehKZHSKMPgdCAuqJLJLv68ArMryTz%2BFiHENIYnhN6Ys15vTSBT6li%2FLpWE7oGKIgCZCZJbp&X-Amz-Signature=89c3f3b25ab2014b08c002f13663865cce0ad1861f2c058a06a4d255971f32d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

