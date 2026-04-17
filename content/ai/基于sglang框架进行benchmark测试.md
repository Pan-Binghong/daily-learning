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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OMSLSIU%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQD1OT4%2Bi28QqGjVkvcd42yVbu6hKRblxmrpI3dblgg1cQIhAPpWItuZ%2F2E4X3OG1%2Fk%2B7iKGh%2BeP0iacvvvnf%2B7F6TuvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIjYYVwiAOjLfekKYq3AOoVSP6FGDYmkPZvFtSCmkhD0fwDy2H0nx89frHcUomqBZuc6jsdTyO6PWigol47MeyS6Zm55p9J%2BTC6VI30ZZQxfppN3bdRLRDipHadMHBDjughc2Ziq1m9pU%2FJ2psAqCSdidPDIhPzKK2261CrnYySIQD5E%2FDuQ1fnVC5dkcJ%2B5j4lNOgH%2FQp499Jt3qn6qDyvt3uO8KLH9OPhrH5AjKYV%2Bm%2Fws5T42vfqr3ms2ZiCYKdL%2FTmQdzxGXNB5PAsQfNdg0QxU%2FGeG0NjInVS6BH%2Bv%2BEiTflb2CC95vG%2FIHHSjScp1SAOnWLG4f0Q76KzE97WWVwIBrjCL%2Fih%2B3LuiU1eaCIdtSKnS4NjgX82cedWvUBvKOT2%2FfgXmrvb7W%2FCIIdDd5Mz9bctbCCAtTfUeSc5s9ePpyjqOXCsiuOoSH2pP9%2B2bqtAzcPbFApKtQwigkWQr%2FR%2F2TML0qY6RscDJm8l5YKV05WGh20JcyZ3P0i18sIFuLqsBpc8bj9%2BjR3nf0%2BGoEDdQ7uQvDsGfQ0hs7hhL9DFxAR6Q5HVIcZ9nmdhCVL6qDWXWNNjOCPVJsryBdSEEipyT82nhos%2BxPdcPO1rWkxXH%2B1KZDkg0Y0hXjJG1MyPVRYa8waN1S%2B7MzDVvIbPBjqkAbZmn5lnmaVkNbNMmzWT%2BosBpioV%2BJXQrCh%2FUT9u0G9KEZtbUa%2Bs5Ngg2%2Fif9c9kt0HNoGUUcjAKBZJz4gzqjSxaL1wfRyK55ZMFb32rDO%2F4Y3EYn4fK2IsDr4WZGsFEu45bn3pPEmexG2Sv6vBdu5%2Bji04OuFVMOoNstt%2B0IjPFK7ZOIgaCw9nQu1QH5v0C9xfgfSzBC87ubtLGIYESg7BaMrdh&X-Amz-Signature=493c54f23dddc164958ac95a6f17f8e77351e068d5b9b1d0e1e08d3e23b8ee6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OMSLSIU%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQD1OT4%2Bi28QqGjVkvcd42yVbu6hKRblxmrpI3dblgg1cQIhAPpWItuZ%2F2E4X3OG1%2Fk%2B7iKGh%2BeP0iacvvvnf%2B7F6TuvKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIjYYVwiAOjLfekKYq3AOoVSP6FGDYmkPZvFtSCmkhD0fwDy2H0nx89frHcUomqBZuc6jsdTyO6PWigol47MeyS6Zm55p9J%2BTC6VI30ZZQxfppN3bdRLRDipHadMHBDjughc2Ziq1m9pU%2FJ2psAqCSdidPDIhPzKK2261CrnYySIQD5E%2FDuQ1fnVC5dkcJ%2B5j4lNOgH%2FQp499Jt3qn6qDyvt3uO8KLH9OPhrH5AjKYV%2Bm%2Fws5T42vfqr3ms2ZiCYKdL%2FTmQdzxGXNB5PAsQfNdg0QxU%2FGeG0NjInVS6BH%2Bv%2BEiTflb2CC95vG%2FIHHSjScp1SAOnWLG4f0Q76KzE97WWVwIBrjCL%2Fih%2B3LuiU1eaCIdtSKnS4NjgX82cedWvUBvKOT2%2FfgXmrvb7W%2FCIIdDd5Mz9bctbCCAtTfUeSc5s9ePpyjqOXCsiuOoSH2pP9%2B2bqtAzcPbFApKtQwigkWQr%2FR%2F2TML0qY6RscDJm8l5YKV05WGh20JcyZ3P0i18sIFuLqsBpc8bj9%2BjR3nf0%2BGoEDdQ7uQvDsGfQ0hs7hhL9DFxAR6Q5HVIcZ9nmdhCVL6qDWXWNNjOCPVJsryBdSEEipyT82nhos%2BxPdcPO1rWkxXH%2B1KZDkg0Y0hXjJG1MyPVRYa8waN1S%2B7MzDVvIbPBjqkAbZmn5lnmaVkNbNMmzWT%2BosBpioV%2BJXQrCh%2FUT9u0G9KEZtbUa%2Bs5Ngg2%2Fif9c9kt0HNoGUUcjAKBZJz4gzqjSxaL1wfRyK55ZMFb32rDO%2F4Y3EYn4fK2IsDr4WZGsFEu45bn3pPEmexG2Sv6vBdu5%2Bji04OuFVMOoNstt%2B0IjPFK7ZOIgaCw9nQu1QH5v0C9xfgfSzBC87ubtLGIYESg7BaMrdh&X-Amz-Signature=fdec43f7dd2754dfdf1638b019cac2072094ac5eabb7b0941ff69970a7819c44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

