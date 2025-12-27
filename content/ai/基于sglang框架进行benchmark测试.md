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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIA7YTHY%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTzHdXSV54zbUYTtR67tnDjtQWR7%2FGjjmfkSRjpAHDcAIgWW7V7Ig8t2oKQUaBuaGmPovjdccRpmJTHOVtEfKBq74q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJF7uE7ci6oI6hKLZircAyXWkHFBNp%2FD8mJ9QJ%2Bo%2BveirPrCUA8A05%2F5lR4jBxElhc3tGN8qyXTSvshFcx%2B6VF2vBJwkgmdr2Lv4KCVsajEDqM7s7yJC5%2B9R9VtdJOoPDg%2Bn4%2BRCGnzddNERM20jqyj%2Fo6ndocWqDX8ObzCzlYdfgZ9fhaGzhp0gPmTJ%2Bf1stFGr66UqGIcZP7rytQ%2B0brXZq5j5GnDqVajd%2F8f7HhzTtspjysXTDgdF%2BBifbL5BfuzZidIuyBpueMVsdxQkNk8Tq0JitsVU7%2BrZjkIiv2MOuaOCXxwKziUkkx3MzRH%2F3g5APPuDnMzw5hmSkzciYiGb6B3Q%2F%2FtGa5hNH6%2F70ngLFtDzu1Q7ljhAHeE5Vz%2BM8qn0KfktVjq7X8zrDpFOaEsE%2BcSOlaDpiTUiNvcjcJC0uLR%2By2zxYDxDcM0wgkWUO%2BLVqYTLiI7fGAA2jisPW%2Fvm5VRjH8mUHM4WbN7wMTJxHtOKJHEvzfieGXI48hSAegMecpWkG15wGIQQBXtweKQMaq7RG78ahkYI73vk3oAHniMC9PIlRjNhKE2iQMrGANvxRzZJu1bUESqVRvNwOWBeG43D7QKgCl2hjB39zD2bbW7hnptlKNVxanOheiwB245iUj8z4Jv0c0v2MKPhvMoGOqUBOEVkda5C%2B%2F5NInLWY6lV3Rkg4kh%2F4R0zeAPg3AE%2FT50bqpuIzukNW%2B4s8CtrJUVJI5b16wf71eLhGJosBCagJ5loHmrKW4pc0ocHz2J974rSc0gzhwutXBPgfHZ7H5Qb6jz00vIcdal2EXmpIdxwJGULvuSP1QAi3actA8v1HdCTF5aL9nZIcFZehrsTAA6D5ZUbbrocxbrC4A%2BijcBJOYbYEsE1&X-Amz-Signature=bc9233e8d7faff4dc7ef77f4f691d602e3569dcf23c111d2e7b075d05e5c6857&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIA7YTHY%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTzHdXSV54zbUYTtR67tnDjtQWR7%2FGjjmfkSRjpAHDcAIgWW7V7Ig8t2oKQUaBuaGmPovjdccRpmJTHOVtEfKBq74q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDJF7uE7ci6oI6hKLZircAyXWkHFBNp%2FD8mJ9QJ%2Bo%2BveirPrCUA8A05%2F5lR4jBxElhc3tGN8qyXTSvshFcx%2B6VF2vBJwkgmdr2Lv4KCVsajEDqM7s7yJC5%2B9R9VtdJOoPDg%2Bn4%2BRCGnzddNERM20jqyj%2Fo6ndocWqDX8ObzCzlYdfgZ9fhaGzhp0gPmTJ%2Bf1stFGr66UqGIcZP7rytQ%2B0brXZq5j5GnDqVajd%2F8f7HhzTtspjysXTDgdF%2BBifbL5BfuzZidIuyBpueMVsdxQkNk8Tq0JitsVU7%2BrZjkIiv2MOuaOCXxwKziUkkx3MzRH%2F3g5APPuDnMzw5hmSkzciYiGb6B3Q%2F%2FtGa5hNH6%2F70ngLFtDzu1Q7ljhAHeE5Vz%2BM8qn0KfktVjq7X8zrDpFOaEsE%2BcSOlaDpiTUiNvcjcJC0uLR%2By2zxYDxDcM0wgkWUO%2BLVqYTLiI7fGAA2jisPW%2Fvm5VRjH8mUHM4WbN7wMTJxHtOKJHEvzfieGXI48hSAegMecpWkG15wGIQQBXtweKQMaq7RG78ahkYI73vk3oAHniMC9PIlRjNhKE2iQMrGANvxRzZJu1bUESqVRvNwOWBeG43D7QKgCl2hjB39zD2bbW7hnptlKNVxanOheiwB245iUj8z4Jv0c0v2MKPhvMoGOqUBOEVkda5C%2B%2F5NInLWY6lV3Rkg4kh%2F4R0zeAPg3AE%2FT50bqpuIzukNW%2B4s8CtrJUVJI5b16wf71eLhGJosBCagJ5loHmrKW4pc0ocHz2J974rSc0gzhwutXBPgfHZ7H5Qb6jz00vIcdal2EXmpIdxwJGULvuSP1QAi3actA8v1HdCTF5aL9nZIcFZehrsTAA6D5ZUbbrocxbrC4A%2BijcBJOYbYEsE1&X-Amz-Signature=43f030d47330878d98579f7d6df8a2d8765e8d40d283e51ce158c1868f0c4b81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

