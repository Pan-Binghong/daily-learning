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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643WSYTZ5%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BsOn%2FUDpGRBVSOkb1Rq3KRX5pWg5n7ynQZvpkyWZv5QIhAILZ7%2Fgv%2FqD6vVD68QFUIp5%2FG9XurhfCnRjfy%2FnVEbEhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQyiOd9eS7RlnMNjMq3APdKaJy6RwRn2smXfXQNnJ7AWujkp4JqYlmm3Du4vDGa051F2wggYt7PyCZUABZqtxoX4k61Ht42GRCy10uTXpfQ7WWjB2fFg0eje1j%2Fzr0kvGK8mpeBHcb%2F7yjtbrl09aQuEkQLhamFLqeK6R8aZgWNc2sn1tYYaE%2Frnm5U8UdaNWf%2F6k8wzUNcEkzZwYspC8t42oxQmHe6i%2FYNzu6BzUmSiWjeuhKRqbClxaHIETFxlNCoXGAf9XO%2FVPlzucWR5rN8BDG5Ia1LdUeWKyyjrzl0sE%2BaT%2B%2FZPxbVNibGl5d3ViM6yI1bAa%2BCxji61sQPRE0913xQLsfgdnd8swJ%2BTZR89zraIVt%2FLpGWax3%2BBwhjUhW6vXR%2F9PTqowCt6b1lHjHi%2BYcrYyMaFJ64UeNVlrbKouc5TT9A8mDgMFZDpToBF9q%2Fezp7NNoWyysrsABhYuXdbudFnN%2FQ3pM2Olmty5vxLlVmR2C4mEkXcOZ5HbeH0Xv5vbOqK8NWKopTBNKgCgNCTJb5FY4HRRfUmgz7QVc5BD5UWErT%2BXLo4pXwuxfjXAn1imqNh3OXOeHV2a5%2BVfMWssE37PolP%2BmkuDOm7e%2Fr2DXVdclLcnFV92O78v60hwZ0bsKAa5y8uX2iDCJ1o7OBjqkAR%2BCq%2B9ULmleDImVo7eSBPh97JD%2FiCN%2F3txFNGO22m%2Fv6x%2FqT2s9wjvSO16mSI8GD6EglCqg65VEVUYGOVCdMy7RJ54oTd6Nahb0ZQx%2BudATxQcv1cwn0yBkIkj3m1bvk2ivHUQOVb1G5m9HQEKPGgIlRfxXQ9rF4DWq1CNx5diyZhEaIF952X1w0azF42FZZlG6myc%2B3AlswGoGr4FKi46bXIa%2B&X-Amz-Signature=daef91bd4176b29c767e9783d40d505cd2caf15783f0ce714f9b9b67441b6355&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643WSYTZ5%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BsOn%2FUDpGRBVSOkb1Rq3KRX5pWg5n7ynQZvpkyWZv5QIhAILZ7%2Fgv%2FqD6vVD68QFUIp5%2FG9XurhfCnRjfy%2FnVEbEhKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQyiOd9eS7RlnMNjMq3APdKaJy6RwRn2smXfXQNnJ7AWujkp4JqYlmm3Du4vDGa051F2wggYt7PyCZUABZqtxoX4k61Ht42GRCy10uTXpfQ7WWjB2fFg0eje1j%2Fzr0kvGK8mpeBHcb%2F7yjtbrl09aQuEkQLhamFLqeK6R8aZgWNc2sn1tYYaE%2Frnm5U8UdaNWf%2F6k8wzUNcEkzZwYspC8t42oxQmHe6i%2FYNzu6BzUmSiWjeuhKRqbClxaHIETFxlNCoXGAf9XO%2FVPlzucWR5rN8BDG5Ia1LdUeWKyyjrzl0sE%2BaT%2B%2FZPxbVNibGl5d3ViM6yI1bAa%2BCxji61sQPRE0913xQLsfgdnd8swJ%2BTZR89zraIVt%2FLpGWax3%2BBwhjUhW6vXR%2F9PTqowCt6b1lHjHi%2BYcrYyMaFJ64UeNVlrbKouc5TT9A8mDgMFZDpToBF9q%2Fezp7NNoWyysrsABhYuXdbudFnN%2FQ3pM2Olmty5vxLlVmR2C4mEkXcOZ5HbeH0Xv5vbOqK8NWKopTBNKgCgNCTJb5FY4HRRfUmgz7QVc5BD5UWErT%2BXLo4pXwuxfjXAn1imqNh3OXOeHV2a5%2BVfMWssE37PolP%2BmkuDOm7e%2Fr2DXVdclLcnFV92O78v60hwZ0bsKAa5y8uX2iDCJ1o7OBjqkAR%2BCq%2B9ULmleDImVo7eSBPh97JD%2FiCN%2F3txFNGO22m%2Fv6x%2FqT2s9wjvSO16mSI8GD6EglCqg65VEVUYGOVCdMy7RJ54oTd6Nahb0ZQx%2BudATxQcv1cwn0yBkIkj3m1bvk2ivHUQOVb1G5m9HQEKPGgIlRfxXQ9rF4DWq1CNx5diyZhEaIF952X1w0azF42FZZlG6myc%2B3AlswGoGr4FKi46bXIa%2B&X-Amz-Signature=9f15de818dc550e4cb5dee67c2f6fbb64220dff18053175069d08e120b53ffa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

