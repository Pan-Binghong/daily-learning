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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WD55ERY%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F%2FmHhtbN4mMtdbbsNwaLSJyCcEkXKIgj%2BH9QcjK6wFgIgNHyWEUrzeOvsSSL%2B8r328kDS8pbupF9UF1eTNtye020qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLveS4RwutLZ1FdQUyrcA%2FVRSj9K8zjiSCyHBHjajQRn%2FMgOg2Pd5LXx3w4wHwD0Q5c2FdYL6UDOR%2BKpSTRW7asIyY6Cz0BmqhUEaJLpyXy%2FqVINwCiIj7mRX4MIC5gCdUEpMoEc%2Bi9%2FLr101XfJBld2ubSp2XBSdnZp0JPQrjNhhEOxqO0FeKRFVHoz%2Fpa0AcfkdRbkhXPGYkJ%2BiHGk8ZxOqbDGq5kx3Ei%2BChBPFCXWsY8pfcCcTXg0a9wi0fAk1o8iacGlPY4lEATEirzaJlENU0xz1t%2F2lIKeiJdQ2VjZzh4Amkt35%2B4eKGbiUjYsS4vxs4KJhT%2FeyrKEwU%2BdgSIT0difZACTK%2BUZzUKJ5N7KMCtf36UZTG%2Bu1IvvW618PD5FFpmHs4FoK9sIEiFa1sQ7etuSb0bL22LiIPnpIaop6C21ZoCT5wYJf%2BZaKQUw03zzFPna5acp8TedM%2F6RRkq801oMkkgzXS5%2FlSDt%2Fcco89b0Tc4dEThy8Dw8e6X3vAtR0oJw9nHL0gqQIduBQQOlI6DPqw%2B0MvSLrs3Ji%2BdLwmCVNTxjiaw0vyBhU6igRQ5aEjHg80i81Ijv8ObvYRMrDBhonpoXF%2FcAug7NYhd09elhWb1Sw6%2FzSzrl4fJdX6sYAS0FbOu7lkJIMMnVzMoGOqUBqzsgPSsVAFCNdj%2B2y%2BTaxyIwySTTCawUU99QFpwRSPJiLohBaKgN8G5HN2Smpi80eGigpXs70i7TZgHKYrmZBbw9WLjzKiamJ8VSa%2FX1wXhI%2FvVCk%2FCjYoKeUAoYde892MX%2FPyi3iEhLJC6CFi3gaTvm01rvRLuzRwsd4Z8%2BWeKUDQTvPeYm5V0lAfgEUyzC4%2BY%2FNT4qHkkFIGgIsxcYqZnDM8Hy&X-Amz-Signature=cabaf129adc23cd0c7ef24f51c6a063f1e0c8cf816ecb010428f0f5ccf8a9d9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WD55ERY%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F%2FmHhtbN4mMtdbbsNwaLSJyCcEkXKIgj%2BH9QcjK6wFgIgNHyWEUrzeOvsSSL%2B8r328kDS8pbupF9UF1eTNtye020qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLveS4RwutLZ1FdQUyrcA%2FVRSj9K8zjiSCyHBHjajQRn%2FMgOg2Pd5LXx3w4wHwD0Q5c2FdYL6UDOR%2BKpSTRW7asIyY6Cz0BmqhUEaJLpyXy%2FqVINwCiIj7mRX4MIC5gCdUEpMoEc%2Bi9%2FLr101XfJBld2ubSp2XBSdnZp0JPQrjNhhEOxqO0FeKRFVHoz%2Fpa0AcfkdRbkhXPGYkJ%2BiHGk8ZxOqbDGq5kx3Ei%2BChBPFCXWsY8pfcCcTXg0a9wi0fAk1o8iacGlPY4lEATEirzaJlENU0xz1t%2F2lIKeiJdQ2VjZzh4Amkt35%2B4eKGbiUjYsS4vxs4KJhT%2FeyrKEwU%2BdgSIT0difZACTK%2BUZzUKJ5N7KMCtf36UZTG%2Bu1IvvW618PD5FFpmHs4FoK9sIEiFa1sQ7etuSb0bL22LiIPnpIaop6C21ZoCT5wYJf%2BZaKQUw03zzFPna5acp8TedM%2F6RRkq801oMkkgzXS5%2FlSDt%2Fcco89b0Tc4dEThy8Dw8e6X3vAtR0oJw9nHL0gqQIduBQQOlI6DPqw%2B0MvSLrs3Ji%2BdLwmCVNTxjiaw0vyBhU6igRQ5aEjHg80i81Ijv8ObvYRMrDBhonpoXF%2FcAug7NYhd09elhWb1Sw6%2FzSzrl4fJdX6sYAS0FbOu7lkJIMMnVzMoGOqUBqzsgPSsVAFCNdj%2B2y%2BTaxyIwySTTCawUU99QFpwRSPJiLohBaKgN8G5HN2Smpi80eGigpXs70i7TZgHKYrmZBbw9WLjzKiamJ8VSa%2FX1wXhI%2FvVCk%2FCjYoKeUAoYde892MX%2FPyi3iEhLJC6CFi3gaTvm01rvRLuzRwsd4Z8%2BWeKUDQTvPeYm5V0lAfgEUyzC4%2BY%2FNT4qHkkFIGgIsxcYqZnDM8Hy&X-Amz-Signature=11eb9fc3fad687e8496d94d46a3330bd40ab79b028c5da1cbcc727d4b498da58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

