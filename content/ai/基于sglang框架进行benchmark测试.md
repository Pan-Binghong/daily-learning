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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTUQ2QTZ%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSG3fJ%2BC%2B4uMS0U3tvMV1gXqSdlPZE%2FxjdA6vVrKoLcAiEAl1jEgeD6jc05icK36qdsfcp5GdvJ4openYZzTX1NDfsq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDPtovEApx8l8xZPd9CrcAwGLJKqAaPT%2BOebQbiM9IXetqQe1ADSASzpvEr1%2FCSHzNcj83%2Ftz1WfdSmSbrK6PB%2FVZVISvHhJR3fafhsKpZcun6iQkFNWHOjqLeW8nCDvcEtnDwDyKADqipb8w%2Bi9HII89KOxE%2B5wX0nt%2FerzOh%2BLXNjfX2LCFZfcYI5aCBp9qRVj7ZhxtB7wmt31FdKR8nL%2FlZsEWsk%2Fe4FXtNYbX6hA%2BIaItp8zCVzEDStlbvGoRNbvwakndEYl%2FHFlj2tHhbHeYonHqVjdgKRUAN667Vx7ABSkAtbJ3LaY2qYa0fZjFd1ibsebRKqLsBAMlbSsonMINOUN3g0o2teViG7FxV5nKVN963tGUBT%2FNlypmnCgw1sXSR7uFWFaUETi6YEmAHCY2R25xbBGdw03Pp1iIvIF0nvKas30TBgSgIZazdzQg0y4K2WoKshhnKBtWnU8q8%2B%2BoUeWHVGripBlFi8%2FXLBMb7CvZP7u40znqB%2Fk68qN1KwwIMFbOKhTTCVhmmm4bIMgtBne1NgA5fjX1%2B7XrIXqHOFZOYvk74sr3CWqu8oY085LJV%2FoSNWbVoIBV%2BHa61%2B5FI5IXk1Ip3O6Zt0%2BDpZPjQlxqTMRS4WI8h69lV%2FXL8RMEjCy1ey9BYNvHMPrRq8sGOqUB08tPVljtHyJ%2Ftb55j0TdTYqmN6OVHLhgSk%2FxmaxOnFLGefyJnFxfIxY2qyW%2BsGlVANfuOOhqu2NKE2%2B1dfQYIEdJvoBWNeIqEivQHYslpIx8koiuCv3GiJh7ovprCsR4%2FiAJVhMU%2BRXDwT7zDxFemA9WzSxPF9SfYWYuqO%2Ffz0fSjs2RcuNBZE3ocRfK6Qg2Mfj79VBkTFyuaP5SCnSlfyLmGUGF&X-Amz-Signature=299d176155839970d03df0e364ed881892aa12825fbff39a369a1f26869b1a77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTUQ2QTZ%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSG3fJ%2BC%2B4uMS0U3tvMV1gXqSdlPZE%2FxjdA6vVrKoLcAiEAl1jEgeD6jc05icK36qdsfcp5GdvJ4openYZzTX1NDfsq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDPtovEApx8l8xZPd9CrcAwGLJKqAaPT%2BOebQbiM9IXetqQe1ADSASzpvEr1%2FCSHzNcj83%2Ftz1WfdSmSbrK6PB%2FVZVISvHhJR3fafhsKpZcun6iQkFNWHOjqLeW8nCDvcEtnDwDyKADqipb8w%2Bi9HII89KOxE%2B5wX0nt%2FerzOh%2BLXNjfX2LCFZfcYI5aCBp9qRVj7ZhxtB7wmt31FdKR8nL%2FlZsEWsk%2Fe4FXtNYbX6hA%2BIaItp8zCVzEDStlbvGoRNbvwakndEYl%2FHFlj2tHhbHeYonHqVjdgKRUAN667Vx7ABSkAtbJ3LaY2qYa0fZjFd1ibsebRKqLsBAMlbSsonMINOUN3g0o2teViG7FxV5nKVN963tGUBT%2FNlypmnCgw1sXSR7uFWFaUETi6YEmAHCY2R25xbBGdw03Pp1iIvIF0nvKas30TBgSgIZazdzQg0y4K2WoKshhnKBtWnU8q8%2B%2BoUeWHVGripBlFi8%2FXLBMb7CvZP7u40znqB%2Fk68qN1KwwIMFbOKhTTCVhmmm4bIMgtBne1NgA5fjX1%2B7XrIXqHOFZOYvk74sr3CWqu8oY085LJV%2FoSNWbVoIBV%2BHa61%2B5FI5IXk1Ip3O6Zt0%2BDpZPjQlxqTMRS4WI8h69lV%2FXL8RMEjCy1ey9BYNvHMPrRq8sGOqUB08tPVljtHyJ%2Ftb55j0TdTYqmN6OVHLhgSk%2FxmaxOnFLGefyJnFxfIxY2qyW%2BsGlVANfuOOhqu2NKE2%2B1dfQYIEdJvoBWNeIqEivQHYslpIx8koiuCv3GiJh7ovprCsR4%2FiAJVhMU%2BRXDwT7zDxFemA9WzSxPF9SfYWYuqO%2Ffz0fSjs2RcuNBZE3ocRfK6Qg2Mfj79VBkTFyuaP5SCnSlfyLmGUGF&X-Amz-Signature=1860854d77d0cbd5c8ada4703d06e9c0fb0e50dae69c8c5cab69619bc81500b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

