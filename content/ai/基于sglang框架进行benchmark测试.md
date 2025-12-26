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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3GVZ5LB%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXxrk%2FsFoFvgH6F0A%2Bq29cb6cPXXsyrZGV54Xdb%2FgsLgIgHLYB1ADRGIflvQ%2BmPEbYv%2BOBWaySzRpTWB8yMUbdgv8q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDPKdUYaNvw1banB5lircA6R4Xybnbg3YsF6%2BhQ4Dk0DArEv0uGio7J03pb7M7zeNc2mR8GRbQOAgFBOIeyGRoFAWLEJ4jsxMpb7c7rcoWOhxSUS8qlnTp18GW4tTNm6Ab2MTgYfSjNLhLHVDKlbUOEn83tqiNDGG%2F7ueHS4%2BPrDNxUxufW8%2BE4ZrNFZICj3i2e8zMv5HCCANhUPO8OBEpFDNrh0goRtJIxYpbMY5oVzoZDm%2FQKM4RCLNis9ty7F72ntNI0bQgYebDoNCkjyHamcG1MKZiYXlAlV%2F5QlcmGMW%2B7P3kmVHqv%2FBnFgfRelsSvX0tzrW6YVTiQyXmQQ%2F0cKPhBD%2Bb84MUlJ5yfEjAZHCvvDgnrulIJ7Xi7tjKRT5Rs9cgfQ0PsilyxNFhdjt7NYFwM8CLxGbSbWCS%2Fh59rfE2yLmntJzIMGvcxuX222uPuCWD3mEwf3ihkZBvlQUPuDxqcqCwTycDjJMLMkFDcx%2Fgrw%2BiH4z%2FbEwbo2sozwQEFo0hx4iEK1pEWWf2u52k5aqW2J9FgoSkM2C6%2FfBib6mgl6QtVldvZv4ucCPeGCw4WW%2BuL%2BbxaHs%2Bv84zmNwBK64FBchZPOLUY4aO9c4HRGhh4JEl9lGlEus4Njk5UtALDvnQv59RpJxgJFWMMrXt8oGOqUBZ9i82RpuM2AmMICE7nukyt%2Bscz2fXlFnNrSKwAWkDOLe%2Fcap%2FpzKS5xzhQnRW3TXVoFoPT2wl7W9NTzYlMRL3NDC1tG9Vwh8fP1zcN2t4NXGOgWd9jRZCMy4PQL2v13hO8w987Tptqu9tONQd60nOyvEtwTus5%2B8hoBgDsZ1IqstGAsvDEYTBXrOz1wIBEcdwKdQvd9oRfoKaE0OPMRgxckV4qd%2B&X-Amz-Signature=2165ceb026ce15134f3b630076a9c331e6170cc145d7c7baf5727154c92dfd06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3GVZ5LB%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXxrk%2FsFoFvgH6F0A%2Bq29cb6cPXXsyrZGV54Xdb%2FgsLgIgHLYB1ADRGIflvQ%2BmPEbYv%2BOBWaySzRpTWB8yMUbdgv8q%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDPKdUYaNvw1banB5lircA6R4Xybnbg3YsF6%2BhQ4Dk0DArEv0uGio7J03pb7M7zeNc2mR8GRbQOAgFBOIeyGRoFAWLEJ4jsxMpb7c7rcoWOhxSUS8qlnTp18GW4tTNm6Ab2MTgYfSjNLhLHVDKlbUOEn83tqiNDGG%2F7ueHS4%2BPrDNxUxufW8%2BE4ZrNFZICj3i2e8zMv5HCCANhUPO8OBEpFDNrh0goRtJIxYpbMY5oVzoZDm%2FQKM4RCLNis9ty7F72ntNI0bQgYebDoNCkjyHamcG1MKZiYXlAlV%2F5QlcmGMW%2B7P3kmVHqv%2FBnFgfRelsSvX0tzrW6YVTiQyXmQQ%2F0cKPhBD%2Bb84MUlJ5yfEjAZHCvvDgnrulIJ7Xi7tjKRT5Rs9cgfQ0PsilyxNFhdjt7NYFwM8CLxGbSbWCS%2Fh59rfE2yLmntJzIMGvcxuX222uPuCWD3mEwf3ihkZBvlQUPuDxqcqCwTycDjJMLMkFDcx%2Fgrw%2BiH4z%2FbEwbo2sozwQEFo0hx4iEK1pEWWf2u52k5aqW2J9FgoSkM2C6%2FfBib6mgl6QtVldvZv4ucCPeGCw4WW%2BuL%2BbxaHs%2Bv84zmNwBK64FBchZPOLUY4aO9c4HRGhh4JEl9lGlEus4Njk5UtALDvnQv59RpJxgJFWMMrXt8oGOqUBZ9i82RpuM2AmMICE7nukyt%2Bscz2fXlFnNrSKwAWkDOLe%2Fcap%2FpzKS5xzhQnRW3TXVoFoPT2wl7W9NTzYlMRL3NDC1tG9Vwh8fP1zcN2t4NXGOgWd9jRZCMy4PQL2v13hO8w987Tptqu9tONQd60nOyvEtwTus5%2B8hoBgDsZ1IqstGAsvDEYTBXrOz1wIBEcdwKdQvd9oRfoKaE0OPMRgxckV4qd%2B&X-Amz-Signature=e38b8979477e7e17d63a3db1057fbfb0c2a0b2d428d3691030f4cb436dfc013f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

