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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655ILFNEP%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCBhsmUn4hSJATu7NP9FPqe0jIeXAAlWOd4tlYeOljRQIhANbc9SIM3lOTOe%2B95yYXCqTfNg75QD9fQsHTroZ%2BV31JKv8DCGsQABoMNjM3NDIzMTgzODA1IgzQYSAvtWHbMnde4Voq3APvkQR1VMRprZAalY5BOXuMgS4X0ycGLXFxvPtWny2qAa2Tn2Ihw2qqoe6fz4Y7%2BnJCSp9gVdIKDlnb1c%2BSVjsSvzg02%2BKZlTzlScBr%2BSTpmexstMJ%2BOsTYN7lUggxco0oas4s8vVrxbHTK7CLU22Ilkm8MEaii4vI2iWdCy1R%2FdJj45UndbZnuLSXMTM5QTHhWJNPG%2Bl%2BCknMtzERO1AxoLfvbE6SZXEK4spFCEkCGUPyD7UELdMmXW8LY%2B6RpTc54xDgKFwTfRBP3QfijNAUL2zOhCYma1FCxggA6UcShkVLSfsdQPCx9MwEowvlkEvzLmg%2FPgdRSbRxb8uot02Z8CAmWOq61F2fCAXBBecEIGkkbumCR%2Bqnr6IHqV71ULCqKs6YSamdRlmXn2yqKbrsEai9rXNdrZ3lxg3uBdU1QzxeVoxLbQhsoIxpjEV87zJsQzKb6r2Y1XTzVIlU6IK1jB5JZmlTMAigwzrg0CnYrvKUz6g1zy0rYhgJhK6FqjrLEHTnfMuHRgHWE8wAp1Y2IzLtxDDNcnnSyKCMc2OqExxKb%2BFcKSnMPsCFbulbe9t9%2BT2iVfc3bLhgMBidgUiUl2cELii9ajgT6QsIogJcSecMCedFlA2j3VURNJjCNp87JBjqkAcFum4lH61Hikw9d%2FtdL%2BL1qvDuzZ9BZyG9Lakh5ohCEy6XQgP5ktL%2BEL9Y94tm7Q2mZdETXyw2k8zAFIAzindhpP2uUnRIEzqc7V3FseIxl%2B99nUiNNCjbyl9XGnAhiKMVWivEQiQ9Y3E7X8O2qrU5rqx%2BU7HM8%2FVM%2BPyi5Zv%2FEKrZrR3Sfg7eismwpNdOfuo%2BzLFhlznNRYdTQlscj5MHYgs%2BI&X-Amz-Signature=75ac6bdbd82341e507b50d948ee15bdcc8bae53ee09912ce986076a0597cd92a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655ILFNEP%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCBhsmUn4hSJATu7NP9FPqe0jIeXAAlWOd4tlYeOljRQIhANbc9SIM3lOTOe%2B95yYXCqTfNg75QD9fQsHTroZ%2BV31JKv8DCGsQABoMNjM3NDIzMTgzODA1IgzQYSAvtWHbMnde4Voq3APvkQR1VMRprZAalY5BOXuMgS4X0ycGLXFxvPtWny2qAa2Tn2Ihw2qqoe6fz4Y7%2BnJCSp9gVdIKDlnb1c%2BSVjsSvzg02%2BKZlTzlScBr%2BSTpmexstMJ%2BOsTYN7lUggxco0oas4s8vVrxbHTK7CLU22Ilkm8MEaii4vI2iWdCy1R%2FdJj45UndbZnuLSXMTM5QTHhWJNPG%2Bl%2BCknMtzERO1AxoLfvbE6SZXEK4spFCEkCGUPyD7UELdMmXW8LY%2B6RpTc54xDgKFwTfRBP3QfijNAUL2zOhCYma1FCxggA6UcShkVLSfsdQPCx9MwEowvlkEvzLmg%2FPgdRSbRxb8uot02Z8CAmWOq61F2fCAXBBecEIGkkbumCR%2Bqnr6IHqV71ULCqKs6YSamdRlmXn2yqKbrsEai9rXNdrZ3lxg3uBdU1QzxeVoxLbQhsoIxpjEV87zJsQzKb6r2Y1XTzVIlU6IK1jB5JZmlTMAigwzrg0CnYrvKUz6g1zy0rYhgJhK6FqjrLEHTnfMuHRgHWE8wAp1Y2IzLtxDDNcnnSyKCMc2OqExxKb%2BFcKSnMPsCFbulbe9t9%2BT2iVfc3bLhgMBidgUiUl2cELii9ajgT6QsIogJcSecMCedFlA2j3VURNJjCNp87JBjqkAcFum4lH61Hikw9d%2FtdL%2BL1qvDuzZ9BZyG9Lakh5ohCEy6XQgP5ktL%2BEL9Y94tm7Q2mZdETXyw2k8zAFIAzindhpP2uUnRIEzqc7V3FseIxl%2B99nUiNNCjbyl9XGnAhiKMVWivEQiQ9Y3E7X8O2qrU5rqx%2BU7HM8%2FVM%2BPyi5Zv%2FEKrZrR3Sfg7eismwpNdOfuo%2BzLFhlznNRYdTQlscj5MHYgs%2BI&X-Amz-Signature=de572d1883cf7e086bbfe23d0407b28bdd6dc0d836b060a73f4b46aecff7ec3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

