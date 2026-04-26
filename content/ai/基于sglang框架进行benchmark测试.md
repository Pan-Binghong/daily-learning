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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZA3VQ6J%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFkM1sIY67QLekN2GhUHY8hmNX%2BZtiTbf%2Fskv1FogEUdAiEA95Zmr%2FQON%2BTJ87Cy68tcKS6mnh6h9GfUi%2BmfY3GLb5EqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFk9oMr20zW4qaUluCrcAzDXQ3mz%2BI%2BeMbOcBivQFBMDWGMFed8sjieoV6D8bum864R0r%2BGxjpmO03TruJBAPY2nkgbbHAsyTcvFkMIsgHObTnFje%2FtmfnR54KJ4CGSrVXzawG2IVFGmO86fWwMxm3wLb8d2%2FN1dohpz4YWFJeZh9s1Z1%2FDa7v9It38Qenp4rNiNJNT4U36Aw3JytGnRKqplRjWTxGRhAUbMdr6xAhw9W%2BsyjNC%2B2lpx%2Be18MLffg1zs9C8GWwb2bSrkseonv9uQHk8Pr8DDrvtG8g7CDkDvTfD17fmDX4kJ8aIXJgEyJ0f29in9P2SX%2B5p0LGZ9eORroN89Ob%2BOHkZn%2BsjZXYLdXctSR0TMr%2FxGHcT6qu7TfK2GarWFbCqpdL4iy192e%2Bb%2BHlxjx99IA1uWeX0A2BDeBIeg8JlwGQSusucnvPefcmxVbQ51p70jkp7pdqxRR3HG3vXq0a%2F4sT%2Bk4I5kaeme62f1kvhhS9Xa9SS7gmXMTeA11C7RzC0u2JKJIjuhV3Sj5DYaRuBsNcjeRn0C5DOjaOuTdDbEGpb3Fo78NrhhlPUFCStSBjOtsmPEbR0kZ%2BrF27a48LcskNtxCyj4%2FTSW%2FwbPgs4uEK%2Bkqg5zcetzh7u7msoBP%2BxIS0JZMLyPts8GOqUBXU5YHIDpWxuofv7Doetgr1nRt8WzA0mljcLorTgRf3RzHsJdhDFc6ToERaMnIkXOXNmyAvNZdMPBhTR6ePvacjDfaPAGNA0Q6rPggpTIXBylgiFxhr71wkKP6LoXLSLz5g%2BYc%2BHsVsyiz5frn73bstpJ53yP9I1fvQAgnAWVTacx2BjStdKHdv1flwM544%2F%2Flr1L4W26hk0qz7ouuqM8tgRh05DY&X-Amz-Signature=ca75f3ce1fabd9963ac1d9da560ded1ce75af772326fb5e1f210a5d24aecbb36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZA3VQ6J%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFkM1sIY67QLekN2GhUHY8hmNX%2BZtiTbf%2Fskv1FogEUdAiEA95Zmr%2FQON%2BTJ87Cy68tcKS6mnh6h9GfUi%2BmfY3GLb5EqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFk9oMr20zW4qaUluCrcAzDXQ3mz%2BI%2BeMbOcBivQFBMDWGMFed8sjieoV6D8bum864R0r%2BGxjpmO03TruJBAPY2nkgbbHAsyTcvFkMIsgHObTnFje%2FtmfnR54KJ4CGSrVXzawG2IVFGmO86fWwMxm3wLb8d2%2FN1dohpz4YWFJeZh9s1Z1%2FDa7v9It38Qenp4rNiNJNT4U36Aw3JytGnRKqplRjWTxGRhAUbMdr6xAhw9W%2BsyjNC%2B2lpx%2Be18MLffg1zs9C8GWwb2bSrkseonv9uQHk8Pr8DDrvtG8g7CDkDvTfD17fmDX4kJ8aIXJgEyJ0f29in9P2SX%2B5p0LGZ9eORroN89Ob%2BOHkZn%2BsjZXYLdXctSR0TMr%2FxGHcT6qu7TfK2GarWFbCqpdL4iy192e%2Bb%2BHlxjx99IA1uWeX0A2BDeBIeg8JlwGQSusucnvPefcmxVbQ51p70jkp7pdqxRR3HG3vXq0a%2F4sT%2Bk4I5kaeme62f1kvhhS9Xa9SS7gmXMTeA11C7RzC0u2JKJIjuhV3Sj5DYaRuBsNcjeRn0C5DOjaOuTdDbEGpb3Fo78NrhhlPUFCStSBjOtsmPEbR0kZ%2BrF27a48LcskNtxCyj4%2FTSW%2FwbPgs4uEK%2Bkqg5zcetzh7u7msoBP%2BxIS0JZMLyPts8GOqUBXU5YHIDpWxuofv7Doetgr1nRt8WzA0mljcLorTgRf3RzHsJdhDFc6ToERaMnIkXOXNmyAvNZdMPBhTR6ePvacjDfaPAGNA0Q6rPggpTIXBylgiFxhr71wkKP6LoXLSLz5g%2BYc%2BHsVsyiz5frn73bstpJ53yP9I1fvQAgnAWVTacx2BjStdKHdv1flwM544%2F%2Flr1L4W26hk0qz7ouuqM8tgRh05DY&X-Amz-Signature=3ecdd91eea5f045fd64915c7eb919c2f2eccb05d242aec8a1ba2cf476c3bac2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

