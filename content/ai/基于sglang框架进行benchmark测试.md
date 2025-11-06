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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UKVTOBW%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHYVtKaa%2BHBtNNoPYXd04WhsLEqUmDYFMi%2FnZDwFkh2DAiBd0vTsc%2B%2BiPyvaujJtIq5SaUtPVSULZrw7%2FcnrNpA6KSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyxxACYrtx2mIKHdeKtwDzq5CSPi5A6nzdj9v4l9NZeHLBlpH7hs0dYzUUR3bhN7c0QmhDWDGR4jgtjPwljBPCMNK1JMsEApNCuBQzTJk8mailoBmiNr9Qm6bwzsTWQlYUe%2BxJGDc7IY%2FxlHhgM%2F9FRFzYOwvnVFyUeIHkUpE47S2JlrhvwH5MtYBjfxcb6PeHu0xcbzcgilAiM7O5PVpTbmZq5aJtzpcSMA3pJR8Kk0jlnBw5cTxDWwC1nzb5greWDsGlhUawUaGwH1pYhsEFFh3vOQKH%2FH%2BvAiGpeYl%2BEKIQSD6%2BVK3bQdnhZ5RVc%2BLTkZjSVT%2BNtXpY9ldlKQLpoK%2BnIDzh1MLooaL4zjViadGOB6kdmxH9PucdLVx7yoPh7%2Bh3W6SW78JkCFos1uW0VayXAT%2FFS2NdHL8KfwEKZWgl9nesSOlk9vmKxuq8RpqNknnJz2RqF%2FXy%2FujBWD5sLv0KzUNjNtr76hwMWa0hkbaAoBc0KdM%2FH9XYpOA%2BktAhz8xKQiFTYpDU0k7B0t%2B1xZP7uAbwDv3rORwTGPGY6KKPbmFcCcABb41gOKA%2FF3IGlaZpMWk2JJlgiv3cojNzImmHu5czjhnrvPIjUzx3ZOIo8f%2FiRX6Wq%2B%2BgugHzWyo77wYtaoahDWhFhAw7%2FGvyAY6pgEhj0fpP4lMTl4i9pfUMGzZEa3w4GBamYlzIZrcvpOvk18kBBNuTX6lxkISVmIx%2FSbV%2F6Q1Xb6PhN3wiFVfaFi4Gv3MxY0HQN%2BQXmlT9nNfNrz%2BzrhIcgUw5dcG%2BjSwNnazEeivdq8SM0DKbxTNiH97kZsFlQwMv3Vl4ahzldw8ZsNxTMtEDWWibrkolHlIuPqb5MbLMHXhQvqovXVAb%2Fe60D%2BqqGAd&X-Amz-Signature=7bdf168336e48471ef7531355a7b491723cd07e69d758e5386b6c79c6675b2ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UKVTOBW%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHYVtKaa%2BHBtNNoPYXd04WhsLEqUmDYFMi%2FnZDwFkh2DAiBd0vTsc%2B%2BiPyvaujJtIq5SaUtPVSULZrw7%2FcnrNpA6KSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyxxACYrtx2mIKHdeKtwDzq5CSPi5A6nzdj9v4l9NZeHLBlpH7hs0dYzUUR3bhN7c0QmhDWDGR4jgtjPwljBPCMNK1JMsEApNCuBQzTJk8mailoBmiNr9Qm6bwzsTWQlYUe%2BxJGDc7IY%2FxlHhgM%2F9FRFzYOwvnVFyUeIHkUpE47S2JlrhvwH5MtYBjfxcb6PeHu0xcbzcgilAiM7O5PVpTbmZq5aJtzpcSMA3pJR8Kk0jlnBw5cTxDWwC1nzb5greWDsGlhUawUaGwH1pYhsEFFh3vOQKH%2FH%2BvAiGpeYl%2BEKIQSD6%2BVK3bQdnhZ5RVc%2BLTkZjSVT%2BNtXpY9ldlKQLpoK%2BnIDzh1MLooaL4zjViadGOB6kdmxH9PucdLVx7yoPh7%2Bh3W6SW78JkCFos1uW0VayXAT%2FFS2NdHL8KfwEKZWgl9nesSOlk9vmKxuq8RpqNknnJz2RqF%2FXy%2FujBWD5sLv0KzUNjNtr76hwMWa0hkbaAoBc0KdM%2FH9XYpOA%2BktAhz8xKQiFTYpDU0k7B0t%2B1xZP7uAbwDv3rORwTGPGY6KKPbmFcCcABb41gOKA%2FF3IGlaZpMWk2JJlgiv3cojNzImmHu5czjhnrvPIjUzx3ZOIo8f%2FiRX6Wq%2B%2BgugHzWyo77wYtaoahDWhFhAw7%2FGvyAY6pgEhj0fpP4lMTl4i9pfUMGzZEa3w4GBamYlzIZrcvpOvk18kBBNuTX6lxkISVmIx%2FSbV%2F6Q1Xb6PhN3wiFVfaFi4Gv3MxY0HQN%2BQXmlT9nNfNrz%2BzrhIcgUw5dcG%2BjSwNnazEeivdq8SM0DKbxTNiH97kZsFlQwMv3Vl4ahzldw8ZsNxTMtEDWWibrkolHlIuPqb5MbLMHXhQvqovXVAb%2Fe60D%2BqqGAd&X-Amz-Signature=83d4f6a640a8e16c000102a9eddaceab5af8efdf0a2cd2e8b788c87905158f67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

