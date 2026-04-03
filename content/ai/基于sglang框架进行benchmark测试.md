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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FSWK5QS%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDjAadj7DXgb71jalV3Y4B6mUi4J90055rs0KznQfmPiAiBdN0tcHBVWgFUUFFi8VFUBIizsZINLmF7f5GzhwDYpHCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMhgLepuvjgIf%2FchbOKtwDldxhxP9V6ioLIi971Nfe9No4jkk6d5uSyM7f86bwkSxEANgKJE3wogUy5b7lsKJ7VMMpn%2F4IdtQ1kl2b%2F9G5N2F8xsRWwKx026u3wPPvafkdhGtxwbozTLLVtHGb21UsxpiBKhjJ4ysAdi7XAmaEVUc3Uq8NH9e6EInRU6%2FKWOnC2nR6%2Fw4npKxcPI1yG0DQRs3rJxdoMwIiGlyLkNeiPHsQENCas32W6rjjtdQ9CKBVv%2B4uy%2FDfHu5Co3Z5Pz3orTYK%2BwAUDm83ERXw%2FIa4xD9xY50Wnsn2BYuUetEKsAlk1tWE5OQke9YrG9gDmXvz91z%2FfHmGvvsovyciJ%2BGV%2BoUJqSoa5Qvb%2FWj4aCr%2FlIvwlwbKO6ulxhLXaOpgvMQfzoMDs%2BlCWyBQjTXv9grXSrq6nynYoMBHVVByuVZZH%2BNdVQvLCdD%2BZXN58RsZSlcHAQfASXGO6C8qS3sx6l56Zb3A8QItyBOY3jzkPRT2bUxb7xqd7uYjJMRQvxeJbTrskQAaRPSbjQ%2Ftias38tFNlZrT2jl8yAAJuCyJMI%2B388nFx2vIR7SNgkznHnZnG4iPxLw6A3KCDD648vUlWiRmZSZjA86RG7af%2F1%2BYS1FRCk6QdxvLLxbs04TtrRIw2ei8zgY6pgEcofhOs8P%2BTv2x2voaYChI4vjZcugOgs1QMY4FDu1TYrvD0AJ1XFOi4MSbiiIoZTQCju9Ki33e%2BPPr8ED8jEpDTdjkwC0bq0r4JSZG5POwaa6bQc1caIC4Kt67OLISdZjSyP%2FAFD0OgMPH5XNhVXuUtsiYm6XSP7GQr8yAOrf13hOyWretCAYwhEnwS0nyaUumn5t6%2Bz5SmTji2Sn1ot8W0XErdYhc&X-Amz-Signature=7e4050033854e89bd3608bf9e97655cb1d42a08c2d7e17ce2b25212f28fc300c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FSWK5QS%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDjAadj7DXgb71jalV3Y4B6mUi4J90055rs0KznQfmPiAiBdN0tcHBVWgFUUFFi8VFUBIizsZINLmF7f5GzhwDYpHCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMhgLepuvjgIf%2FchbOKtwDldxhxP9V6ioLIi971Nfe9No4jkk6d5uSyM7f86bwkSxEANgKJE3wogUy5b7lsKJ7VMMpn%2F4IdtQ1kl2b%2F9G5N2F8xsRWwKx026u3wPPvafkdhGtxwbozTLLVtHGb21UsxpiBKhjJ4ysAdi7XAmaEVUc3Uq8NH9e6EInRU6%2FKWOnC2nR6%2Fw4npKxcPI1yG0DQRs3rJxdoMwIiGlyLkNeiPHsQENCas32W6rjjtdQ9CKBVv%2B4uy%2FDfHu5Co3Z5Pz3orTYK%2BwAUDm83ERXw%2FIa4xD9xY50Wnsn2BYuUetEKsAlk1tWE5OQke9YrG9gDmXvz91z%2FfHmGvvsovyciJ%2BGV%2BoUJqSoa5Qvb%2FWj4aCr%2FlIvwlwbKO6ulxhLXaOpgvMQfzoMDs%2BlCWyBQjTXv9grXSrq6nynYoMBHVVByuVZZH%2BNdVQvLCdD%2BZXN58RsZSlcHAQfASXGO6C8qS3sx6l56Zb3A8QItyBOY3jzkPRT2bUxb7xqd7uYjJMRQvxeJbTrskQAaRPSbjQ%2Ftias38tFNlZrT2jl8yAAJuCyJMI%2B388nFx2vIR7SNgkznHnZnG4iPxLw6A3KCDD648vUlWiRmZSZjA86RG7af%2F1%2BYS1FRCk6QdxvLLxbs04TtrRIw2ei8zgY6pgEcofhOs8P%2BTv2x2voaYChI4vjZcugOgs1QMY4FDu1TYrvD0AJ1XFOi4MSbiiIoZTQCju9Ki33e%2BPPr8ED8jEpDTdjkwC0bq0r4JSZG5POwaa6bQc1caIC4Kt67OLISdZjSyP%2FAFD0OgMPH5XNhVXuUtsiYm6XSP7GQr8yAOrf13hOyWretCAYwhEnwS0nyaUumn5t6%2Bz5SmTji2Sn1ot8W0XErdYhc&X-Amz-Signature=baa6fc37ae960721f480507a526f53d5cf9bcf29dac5ac85c324e039ce09a58b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

