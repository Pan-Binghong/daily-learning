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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EOFGVQ3%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEI%2BA6YjJcM5Vq07NNKlgCShW6EKcbo5cNJ0SRmuUapdAiEAiDGoqGXChfTkJpbRRv7%2F5J4Rir7YWujZv72XN%2Fo%2B7c4q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDCP7S%2FqZmMRCACfyqSrcA2%2FbpPm0OuWyozsvND7qIzuGh%2B8FrHHtVLzcK8%2FSRfpLeMJ4UXCENCu6hnUHXXpinGf3sYeLeLC%2BEgRdGvmzZxge3NOlBiQnKwBKx1ER2atk5akYVpm7k7SO8ct04NQ2KX2COFKqTPP9K3BGsgaMW4VAhqPZf5lpswgicV28%2BoBfm6x3VdYhsalGarr3yk1ydEsSf0m4KulPogPCSZGaNbqOne%2B9OROZkEC63bFlHpJe0CswTYdQLSvb3RhCZfcduhE6xdwjipbyckXcUDBgPKVElENFYaFgTFZTF8XOeH1oDZ2O8iqRUevsIddE7Tf3rXtQPMdkFwBJd01ReI%2ByCJeB1LI%2FnhVKtToiUH4VjEc%2Fa9r%2FlusClglca7EQG3wyjMZR8Z%2Bs4YmKCev46xeML1A%2BMSINfzKYyEyZXch6Dm%2F3q05FC07JRB5%2FayB8mhy6eKxKiqcAMDl9R4HObeDADhMeLgRNOW8xqALaqEznqE1%2B6hwXm1iUF2XzuLq1yrB40D%2Bcud%2FCb4cykkwLoxMY%2F3eqX021tcxOLJC1NNMsjabED13y9zIFTwQgvZNzYQMOb4XI2lBpyFA9yq4S687aej6WvpLAgrZhDNXs5DxqfMjrScDmjC9lebhwgBO%2FMMyslMkGOqUBSkql9XNE%2F5EQ7A0sPnUXWMzna6NHAbFeobXk9vzkwRsXilSHMLeuLJNykDlBnbbqty6Y1mKGFx%2F6TWe%2FWqmh85SdBWmq4ASm6WY2MArkDyhDjpL97zkg0qWCMmbxhNAA6nfQQKCaEpzTorp%2Bm2yulyzOz4Z8nF16VNGzNquz1%2B911pKJzVHc2%2FFIuRXbYhrDuPEJZK5QoXJ8RsVlTBbxSuG%2BE2L5&X-Amz-Signature=5429c0631c1524c05b2f59be02300f97bc9633b6e31c858fd46d4268c357b701&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EOFGVQ3%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEI%2BA6YjJcM5Vq07NNKlgCShW6EKcbo5cNJ0SRmuUapdAiEAiDGoqGXChfTkJpbRRv7%2F5J4Rir7YWujZv72XN%2Fo%2B7c4q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDCP7S%2FqZmMRCACfyqSrcA2%2FbpPm0OuWyozsvND7qIzuGh%2B8FrHHtVLzcK8%2FSRfpLeMJ4UXCENCu6hnUHXXpinGf3sYeLeLC%2BEgRdGvmzZxge3NOlBiQnKwBKx1ER2atk5akYVpm7k7SO8ct04NQ2KX2COFKqTPP9K3BGsgaMW4VAhqPZf5lpswgicV28%2BoBfm6x3VdYhsalGarr3yk1ydEsSf0m4KulPogPCSZGaNbqOne%2B9OROZkEC63bFlHpJe0CswTYdQLSvb3RhCZfcduhE6xdwjipbyckXcUDBgPKVElENFYaFgTFZTF8XOeH1oDZ2O8iqRUevsIddE7Tf3rXtQPMdkFwBJd01ReI%2ByCJeB1LI%2FnhVKtToiUH4VjEc%2Fa9r%2FlusClglca7EQG3wyjMZR8Z%2Bs4YmKCev46xeML1A%2BMSINfzKYyEyZXch6Dm%2F3q05FC07JRB5%2FayB8mhy6eKxKiqcAMDl9R4HObeDADhMeLgRNOW8xqALaqEznqE1%2B6hwXm1iUF2XzuLq1yrB40D%2Bcud%2FCb4cykkwLoxMY%2F3eqX021tcxOLJC1NNMsjabED13y9zIFTwQgvZNzYQMOb4XI2lBpyFA9yq4S687aej6WvpLAgrZhDNXs5DxqfMjrScDmjC9lebhwgBO%2FMMyslMkGOqUBSkql9XNE%2F5EQ7A0sPnUXWMzna6NHAbFeobXk9vzkwRsXilSHMLeuLJNykDlBnbbqty6Y1mKGFx%2F6TWe%2FWqmh85SdBWmq4ASm6WY2MArkDyhDjpL97zkg0qWCMmbxhNAA6nfQQKCaEpzTorp%2Bm2yulyzOz4Z8nF16VNGzNquz1%2B911pKJzVHc2%2FFIuRXbYhrDuPEJZK5QoXJ8RsVlTBbxSuG%2BE2L5&X-Amz-Signature=e6f43c4dbd4ddfac25927627129971a8efc725c06c5af90483877212e23c70b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

