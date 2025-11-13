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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VBEG2OZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIEyGysGZcLHVJ9zW%2B2dNo1VUVG%2F3BThz8UR7xv6zQARjAiEA9IeJ0A2ygBBHAoWSt704%2B3b%2BnizYAEMer%2FVHupai1%2Fkq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDAvgM%2BDgnuSyf4oYzyrcAyBY%2F9MuoPNbOknEjhlfD7ksz8QDKuFxJTNP%2FiqZcKk3ShFvwRCOfXf3qQrOCJVfZTfRtJWKu00mIBcDk3nwaMVseh8LtzZH97et7eC7najXGfqY89tIBqrMllLuT63lqUTo2tc4vOxUu87j9PCITCo%2F6yPseaq9o7nIFuowr4Oz692qfdDnjauHfS4dRO9m5fG5lrWNsPptUNxdx29IHfAg1PdSthjUfZFoT%2Bg%2B3sVIXYtxz%2FKXPT2bFdGLXluwGcx0FAm%2FtCH0sTe55I%2BsePVRsKsWhLS0JIGchZA4E6XFt7%2Fhpb3ZAcyidUiymzXjbL2XGigXv8oorj0sB4J2VHMyrqIL%2BTOQVdF8Gt0INy5vgzXZvRmQWm9niq%2FNfKQZzh3JVmKQbcgMBgZ16KdcsKYBQcG9TryRZs6twXdqRTE3hBr%2FCSTg5O%2BDLoDtlOZErfyIQ5pq09moSR0oVKcdfcgYTQlXO8TUdEiRqxEh1ansC5ExHOyX9vleu84KY33eK4Qr0mYFSK%2B5PJIL%2B%2BZxtR8K45lg8W2NOV2TSQXL1KklKLaHJHJ9wSb%2BTHqPj8XKdY7HZ7wkPA700iB6aRjtPqrUy9C8KiRhRGOC7tFTdEWdqSQ2CtvqT%2FwIOGIrMNDx1MgGOqUBtjrmUghihXxeguLbwPLsqqfBoVhxJMD%2BuN2sLxa91h7ZeZ%2B%2FL0vp6jw%2FcK0SJ%2BpO918x%2BAq7eEmHW3HALI8PCd5ptO0fC5a3krYoBCE6T69%2Bv3UgFSZnByMD2VqEwmTo%2FgwhjnHqPHv5aR7PTEsQgFn%2FeD2bc7soY53wR%2Fkb1KMpnJQgkTs2K38k5DjQwEGu4VYw8vitbI6qOhcHKoSd07Lrt%2F8B&X-Amz-Signature=441864c57d12e5d65efa28e008cfcac6e51018a0f91006dc006b3f9e3292a95f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VBEG2OZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIEyGysGZcLHVJ9zW%2B2dNo1VUVG%2F3BThz8UR7xv6zQARjAiEA9IeJ0A2ygBBHAoWSt704%2B3b%2BnizYAEMer%2FVHupai1%2Fkq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDAvgM%2BDgnuSyf4oYzyrcAyBY%2F9MuoPNbOknEjhlfD7ksz8QDKuFxJTNP%2FiqZcKk3ShFvwRCOfXf3qQrOCJVfZTfRtJWKu00mIBcDk3nwaMVseh8LtzZH97et7eC7najXGfqY89tIBqrMllLuT63lqUTo2tc4vOxUu87j9PCITCo%2F6yPseaq9o7nIFuowr4Oz692qfdDnjauHfS4dRO9m5fG5lrWNsPptUNxdx29IHfAg1PdSthjUfZFoT%2Bg%2B3sVIXYtxz%2FKXPT2bFdGLXluwGcx0FAm%2FtCH0sTe55I%2BsePVRsKsWhLS0JIGchZA4E6XFt7%2Fhpb3ZAcyidUiymzXjbL2XGigXv8oorj0sB4J2VHMyrqIL%2BTOQVdF8Gt0INy5vgzXZvRmQWm9niq%2FNfKQZzh3JVmKQbcgMBgZ16KdcsKYBQcG9TryRZs6twXdqRTE3hBr%2FCSTg5O%2BDLoDtlOZErfyIQ5pq09moSR0oVKcdfcgYTQlXO8TUdEiRqxEh1ansC5ExHOyX9vleu84KY33eK4Qr0mYFSK%2B5PJIL%2B%2BZxtR8K45lg8W2NOV2TSQXL1KklKLaHJHJ9wSb%2BTHqPj8XKdY7HZ7wkPA700iB6aRjtPqrUy9C8KiRhRGOC7tFTdEWdqSQ2CtvqT%2FwIOGIrMNDx1MgGOqUBtjrmUghihXxeguLbwPLsqqfBoVhxJMD%2BuN2sLxa91h7ZeZ%2B%2FL0vp6jw%2FcK0SJ%2BpO918x%2BAq7eEmHW3HALI8PCd5ptO0fC5a3krYoBCE6T69%2Bv3UgFSZnByMD2VqEwmTo%2FgwhjnHqPHv5aR7PTEsQgFn%2FeD2bc7soY53wR%2Fkb1KMpnJQgkTs2K38k5DjQwEGu4VYw8vitbI6qOhcHKoSd07Lrt%2F8B&X-Amz-Signature=b7076d42102172de5f2ced0facaa9d842a3a1053c32a0d03dd07fa3a3dbb1acc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

