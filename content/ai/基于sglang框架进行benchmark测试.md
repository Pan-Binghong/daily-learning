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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJP63A2E%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsKL%2Fpd3%2FK50y%2FUoX7tclrxLczfE7Qfz2BD80Kg1z58wIhAOuTp%2Bf1LiTD6NK3LByzfCXAwB1CgTSSQ0yceco7mjURKv8DCE0QABoMNjM3NDIzMTgzODA1Igxuw9vvxvhopTqJapcq3ANOOJlct%2B%2FCZiklbPe08c7jO4GrQSgJDIS3qW3KtFqugPT0ufaJSijl3cNfRx7i%2F%2Blicu%2Bf4M2FwP%2B6vRyfSyhNkdwjRZz0Ufp6d97DR2x8wTltTZjXK2YiwC%2Bm1ij0qFLQNIMPUm4pHfhNqc6xnFs5aARBGo13j9hG%2F9zIp6DODuD0xV%2FuViNbWaIFGzmOV4Kya7AjuCubbFiLO%2BZuCISavsFF%2F%2FdkudBdNPkDM5g21kFcO%2BAt08Psy9twtJpzr85nvotD7b2SZyXDKRvFufShV%2FMvjjqooX3tPJ%2FFt%2F%2Fw4%2B102PXSlWlaX5kT79lTht2FoFcCCTMaydTqdruM6OvGrePTHi2CE9NylcylHW4GvMYJh%2Ba0Ba7kgvimz%2BlU6ISNqtmSrPIV7cLqiEaXNTh45Ki6FyqYVK22cwzTmzNXICZ81DSMa3QPHlF8%2Bk4iw3%2FkOs7U4tAnV9VkSDtujepMTKa8YpHerTjDcJDDdSwR1R%2BUkyEWn9J0h1cZUyF91z%2BqbODFVjO1HsjcpkACGjKL%2FNmGl%2F2PGUHQV0%2BafL%2Fui17E39i%2FrGyWSiBzaX5qVZyx7VmAF4GqrD8767Tn7ejIwm4nQLlA4mVA4fPQN3qUzoAFI6iXrLDspeFTXTD7oLLOBjqkAcdqF6CeVPawg0GYuwR08%2BjY3l26k3pMMmvJyMXcoHku1f8Diq72sajn%2FsWsrz6H0hsnorp4oAcVcW%2Fa%2BunSUoGs9O1Szeke31mQhm%2FTDsR16lXg0J2g61GvPPEwXY1y8Fho%2BZt5zsmsEQUrNWxBrNkuedBOBG6InarAChMTY9eikSXYea34R%2BW7SYyRrrg2tXsyxC6UmXNdw4L4MUVaJjjJctrl&X-Amz-Signature=39e364506360a3d7813e0dcab90b1e07283edc5ada22f131c861ee3e5e23192a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJP63A2E%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsKL%2Fpd3%2FK50y%2FUoX7tclrxLczfE7Qfz2BD80Kg1z58wIhAOuTp%2Bf1LiTD6NK3LByzfCXAwB1CgTSSQ0yceco7mjURKv8DCE0QABoMNjM3NDIzMTgzODA1Igxuw9vvxvhopTqJapcq3ANOOJlct%2B%2FCZiklbPe08c7jO4GrQSgJDIS3qW3KtFqugPT0ufaJSijl3cNfRx7i%2F%2Blicu%2Bf4M2FwP%2B6vRyfSyhNkdwjRZz0Ufp6d97DR2x8wTltTZjXK2YiwC%2Bm1ij0qFLQNIMPUm4pHfhNqc6xnFs5aARBGo13j9hG%2F9zIp6DODuD0xV%2FuViNbWaIFGzmOV4Kya7AjuCubbFiLO%2BZuCISavsFF%2F%2FdkudBdNPkDM5g21kFcO%2BAt08Psy9twtJpzr85nvotD7b2SZyXDKRvFufShV%2FMvjjqooX3tPJ%2FFt%2F%2Fw4%2B102PXSlWlaX5kT79lTht2FoFcCCTMaydTqdruM6OvGrePTHi2CE9NylcylHW4GvMYJh%2Ba0Ba7kgvimz%2BlU6ISNqtmSrPIV7cLqiEaXNTh45Ki6FyqYVK22cwzTmzNXICZ81DSMa3QPHlF8%2Bk4iw3%2FkOs7U4tAnV9VkSDtujepMTKa8YpHerTjDcJDDdSwR1R%2BUkyEWn9J0h1cZUyF91z%2BqbODFVjO1HsjcpkACGjKL%2FNmGl%2F2PGUHQV0%2BafL%2Fui17E39i%2FrGyWSiBzaX5qVZyx7VmAF4GqrD8767Tn7ejIwm4nQLlA4mVA4fPQN3qUzoAFI6iXrLDspeFTXTD7oLLOBjqkAcdqF6CeVPawg0GYuwR08%2BjY3l26k3pMMmvJyMXcoHku1f8Diq72sajn%2FsWsrz6H0hsnorp4oAcVcW%2Fa%2BunSUoGs9O1Szeke31mQhm%2FTDsR16lXg0J2g61GvPPEwXY1y8Fho%2BZt5zsmsEQUrNWxBrNkuedBOBG6InarAChMTY9eikSXYea34R%2BW7SYyRrrg2tXsyxC6UmXNdw4L4MUVaJjjJctrl&X-Amz-Signature=98740f0cdb89e4c99a3c438f3fb7539a253b4df2dcc67ca4d93ea916e457b0bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

