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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIRLNBLU%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCci5SrGXdCJxxhm%2F4YzMUlqpDBE%2BcSfTV3i2IZ5cPg1wIhAIZOGrBOJDb3Ujq8ytB1U49AV5MKwMeeJhipt%2Fy6V9EXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzp0orzlEJedjTLvQwq3ANHlx2baXnDN%2F5Scy%2BlWaJkmMuOmwGCm%2BITUX1yzhW0qisiy8k08LEGD6xibV4QylnL2LwZYFDUVSoQuQf%2BplXe6PjXLicevvWmZo3TvujzY4U6NjfdlSKSwTdn%2F2OtG7QoE8LWIA6BrY87q9Buqznrs9QFASklUOicSVYlrQ%2FXWgXyDoI%2FGJGArZyPqBiuZueBEkF0Kl9JpxswpY41659W40K4pYi76mWP64DLmrrcRXk%2BPfAE6mjx7YZlcrHwFaef7UnFWUXel5oWKdT1kRStoQeLvxk%2BBtb6xRKSsfJlBTETVuQUZ65ZpP%2FWvdak0F9GLT74lygVYXJSO5wHKsc0Ubylh%2FveG3aBkXPYqBuUVY%2FgVRel0uWHjUJye5FYQMn2xovaR5tryqXMl1xPLmWbFYEZT%2BPKJpE4k2%2FI9TzJ4hcUUSaToqrzrv1tOI7Rwa28MXvahxYtS21EM5OjD5GfvTn2O4FJJ0Q3jASY8yjsKD1y%2F5BB6icNkmn6P5AXCfrHeMhaFjiGsXPaydsFeQAlQgGp2Q22U1FIe3iE8qRkcKEVDPw%2FHEtDwbIOPf5ilREHlTRYnc%2Fe3gmYhJ5IjSvoujeUMF9rKk2mQ%2FeI8t7XHWeA2FExKJi%2Fb9E5wjDT%2BJzKBjqkAR7ZvgRC8FuuClQfRatVatVIqicbCIez2etM4QI5jnqyfXYUFCxHobMkqsl6EOtFeRoX2Yx2AAtS%2BmEFoano%2BeKdN%2B%2F%2BBlVB5xtjG0ZOUc3bwi9wirONx62YVuYR2BHKLxsa4M170iFBeR%2BRITJkB0mT4psbnKhNveK3ookZgsfNMSXYz%2B1hEmXuAmPaIQYI8NW8jMzY%2Fxm8NKM6NykKE%2FXnJFPR&X-Amz-Signature=6ab3f8ff4756940a37ab67ac87c5080609a3202e37b782b13d3d18d20dcf03aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIRLNBLU%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCci5SrGXdCJxxhm%2F4YzMUlqpDBE%2BcSfTV3i2IZ5cPg1wIhAIZOGrBOJDb3Ujq8ytB1U49AV5MKwMeeJhipt%2Fy6V9EXKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzp0orzlEJedjTLvQwq3ANHlx2baXnDN%2F5Scy%2BlWaJkmMuOmwGCm%2BITUX1yzhW0qisiy8k08LEGD6xibV4QylnL2LwZYFDUVSoQuQf%2BplXe6PjXLicevvWmZo3TvujzY4U6NjfdlSKSwTdn%2F2OtG7QoE8LWIA6BrY87q9Buqznrs9QFASklUOicSVYlrQ%2FXWgXyDoI%2FGJGArZyPqBiuZueBEkF0Kl9JpxswpY41659W40K4pYi76mWP64DLmrrcRXk%2BPfAE6mjx7YZlcrHwFaef7UnFWUXel5oWKdT1kRStoQeLvxk%2BBtb6xRKSsfJlBTETVuQUZ65ZpP%2FWvdak0F9GLT74lygVYXJSO5wHKsc0Ubylh%2FveG3aBkXPYqBuUVY%2FgVRel0uWHjUJye5FYQMn2xovaR5tryqXMl1xPLmWbFYEZT%2BPKJpE4k2%2FI9TzJ4hcUUSaToqrzrv1tOI7Rwa28MXvahxYtS21EM5OjD5GfvTn2O4FJJ0Q3jASY8yjsKD1y%2F5BB6icNkmn6P5AXCfrHeMhaFjiGsXPaydsFeQAlQgGp2Q22U1FIe3iE8qRkcKEVDPw%2FHEtDwbIOPf5ilREHlTRYnc%2Fe3gmYhJ5IjSvoujeUMF9rKk2mQ%2FeI8t7XHWeA2FExKJi%2Fb9E5wjDT%2BJzKBjqkAR7ZvgRC8FuuClQfRatVatVIqicbCIez2etM4QI5jnqyfXYUFCxHobMkqsl6EOtFeRoX2Yx2AAtS%2BmEFoano%2BeKdN%2B%2F%2BBlVB5xtjG0ZOUc3bwi9wirONx62YVuYR2BHKLxsa4M170iFBeR%2BRITJkB0mT4psbnKhNveK3ookZgsfNMSXYz%2B1hEmXuAmPaIQYI8NW8jMzY%2Fxm8NKM6NykKE%2FXnJFPR&X-Amz-Signature=4085f3c0cc5f010d5aefbf63e08b9d67cfb1415dd32db979353296f010da6e3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

