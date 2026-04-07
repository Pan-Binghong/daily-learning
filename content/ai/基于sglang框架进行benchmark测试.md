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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DJSD5JD%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDYPsaAuTNKecR8i%2FEcqmuO9ckhxbpyYK0ALzNe79tSPAiBApA8vbRPb1Bmw65o3SKn5phc9OrPn19xVtCzaD1T3viqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbvNu0MDKqXsc7jbTKtwD2cJm4hi1gjgoleKl4c2SSSvoBgn4tcCpcB6fgdp89qlOqZfzid3vIi7xE7Qtnjkd8N4TR3SwWmSIYieqDzDh6eR6ROnC1iaWVD%2BgRDkND4AqWSg%2FC8EqILktx7xNLnnAV5EWBc8SZ0QayewpSC59XJZyg50vu2QQyY91PezJPnrrP7tLbUidyHmEDjQ1kmbVZRaMwMrRczvIc%2BRqeBP74y7S%2FJIXcv6ZnxRj3ioEGq3qDFT2xo1mw5V2d%2FetqeiS5GDKCnmrzRbocqPdM67vvPLcXnGfTUqXW7Gy3ixfV9Ee3wTMwUE%2FfuJuljarwdRq3zNN5t60E7jfYo%2FhkZSRK2drcJzYkLeKVKceWr%2FE8aR%2F3aQ2KXOJymapxbc4ArS5RXxVoOoetjDenStOmi5ypfhX8MqbLLSlPQhwd7GMUdj0hjxpKPtJ%2F%2Bwv%2BRhHzhZwNH5KuRseH5nBcGF%2F8%2B6gPqDBrV8C6cFj94pe%2BLoV9AJ2RHHYCIxQ8qZ51DAVFoyeSWewo5u6aAdQkwNCRa50iSYt4jraUuuT%2FC9kzFgkX17B95y8bpMRtoSpyCSJKgYcacQKrWhNUTvoYx6gygDHySNhv4qQpVGTNp4lc93oWxSx91Y7ei1zaQ8YUdgw0%2FbRzgY6pgGuSs88nBjQCVFDVmJMT%2For9TmaYD2DeR51yya%2BlnrVR0SL9pouppL1VdQDBKebQrkWk7nxmXJY0kIa4iOgIvowsOc9xJbCxertyKXLxNmObsAZZInAb7VUlK%2Fps%2FA8jxTAKX13mgtwwIMqRJcq9a%2FxGZv0%2BjI27fvhsTEOOyC2yq57H8rWe8BrT6VzCpUFKu6qJvo3umB2Od%2FNLMNxIcwKrief%2BYX8&X-Amz-Signature=edaaef9a8f708940b78a3d253b0875f63055a75267219fbd14dabef399a52596&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DJSD5JD%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDYPsaAuTNKecR8i%2FEcqmuO9ckhxbpyYK0ALzNe79tSPAiBApA8vbRPb1Bmw65o3SKn5phc9OrPn19xVtCzaD1T3viqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbvNu0MDKqXsc7jbTKtwD2cJm4hi1gjgoleKl4c2SSSvoBgn4tcCpcB6fgdp89qlOqZfzid3vIi7xE7Qtnjkd8N4TR3SwWmSIYieqDzDh6eR6ROnC1iaWVD%2BgRDkND4AqWSg%2FC8EqILktx7xNLnnAV5EWBc8SZ0QayewpSC59XJZyg50vu2QQyY91PezJPnrrP7tLbUidyHmEDjQ1kmbVZRaMwMrRczvIc%2BRqeBP74y7S%2FJIXcv6ZnxRj3ioEGq3qDFT2xo1mw5V2d%2FetqeiS5GDKCnmrzRbocqPdM67vvPLcXnGfTUqXW7Gy3ixfV9Ee3wTMwUE%2FfuJuljarwdRq3zNN5t60E7jfYo%2FhkZSRK2drcJzYkLeKVKceWr%2FE8aR%2F3aQ2KXOJymapxbc4ArS5RXxVoOoetjDenStOmi5ypfhX8MqbLLSlPQhwd7GMUdj0hjxpKPtJ%2F%2Bwv%2BRhHzhZwNH5KuRseH5nBcGF%2F8%2B6gPqDBrV8C6cFj94pe%2BLoV9AJ2RHHYCIxQ8qZ51DAVFoyeSWewo5u6aAdQkwNCRa50iSYt4jraUuuT%2FC9kzFgkX17B95y8bpMRtoSpyCSJKgYcacQKrWhNUTvoYx6gygDHySNhv4qQpVGTNp4lc93oWxSx91Y7ei1zaQ8YUdgw0%2FbRzgY6pgGuSs88nBjQCVFDVmJMT%2For9TmaYD2DeR51yya%2BlnrVR0SL9pouppL1VdQDBKebQrkWk7nxmXJY0kIa4iOgIvowsOc9xJbCxertyKXLxNmObsAZZInAb7VUlK%2Fps%2FA8jxTAKX13mgtwwIMqRJcq9a%2FxGZv0%2BjI27fvhsTEOOyC2yq57H8rWe8BrT6VzCpUFKu6qJvo3umB2Od%2FNLMNxIcwKrief%2BYX8&X-Amz-Signature=888eab36d37437021f689b036675639002829ccad97030bd98a8b71406378176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

