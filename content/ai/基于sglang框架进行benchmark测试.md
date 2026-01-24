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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHYUMHWY%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDGYymXR0HtcJtl7xNHriLhpzJ7twj7LxK3%2BVtLxnDAOgIhAOvlAwhPpokv1uHRdaiiNGzUbdqwveK6S944A1B1QhQOKv8DCAMQABoMNjM3NDIzMTgzODA1Igwnv7U%2FWnUO%2FhvhqQQq3AMZ6h7GmFSqOQgSJcEEZzJSd0yD0vMsT%2BX3OjvgytLZWblSs97Yl8hq8QoH1tMD7dV098QVyhhPnr7Lr74wY9CY63wDQKNCwhMpzCEsioDhckdarQs9piRLICJFEoIEAmFVd4sYwqlsnl3FQ6xLX6GgXymafM0vAMKqQwVwscfj%2Bzp7BXRM494Z62zRRBfxG61X5xqobi4yCkeiOUEC5b1cAbHUFuTiUshkaXZ2ZIE3%2FOKK0hsbcIq6%2B5Gfzel%2FCi07KQEYLIlfyaoYPlqvCwH57W1jfgepnY%2BDMWvfYPV0QHWCdyubvM64T1EbS6zuvRjmPgdZTvHPwGDzgQF2AmdzQJAklNjVigcSvAank%2FqpYxKJ5VvoT0U%2FqkYui5Xc83qDD3npA8Q8uM9mtI6DGEu%2BlTyewuoSdQapsxOLGrIZ6IvyV7xjxtYSKnhLf6MXmnQFedHEaN0OGdsu9T1VcDB4U39STH%2F%2F3rZenV8%2FUETm4bcN7c%2F%2BggF8OHG9kYKUUjFNBMwxkR0HvnGgVtTWRPUF%2Fu6YkKmAoOOMrGYX%2BoJNCy1AQF3KiEmUY6z6zivWu4rJapQeBnydRldoOXakVS0z2HGcPg8h3uUc32LjHawtWkYApw10cF8yuTZXPzC7ztDLBjqkAa%2Fnn0WS1NMVDHaL%2FmoReBBjEde0KfJqGJXSAPfI3gcj4hB0CSwLJR6SHwUvo0MP8K4OL3CJoC9WH2ZpHW%2BzRvWEOCafA%2FrrgTzf3Vj55OhfNHYvRQ7p8%2FSY2UUKkwiqtmsSRTvvWZNibrHZVe7D0JL6f5ESbJy8%2Fvt5BVFwxqYow4fjLHI9SZpS%2F%2FabCItODTW6jUNyS9W%2FZmCDvbnpaZB70FZF&X-Amz-Signature=cbe4e4e7b8cd107196a72b8056fd6130c722b8aee57fa32e3f2fd81ddc7c8a17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHYUMHWY%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDGYymXR0HtcJtl7xNHriLhpzJ7twj7LxK3%2BVtLxnDAOgIhAOvlAwhPpokv1uHRdaiiNGzUbdqwveK6S944A1B1QhQOKv8DCAMQABoMNjM3NDIzMTgzODA1Igwnv7U%2FWnUO%2FhvhqQQq3AMZ6h7GmFSqOQgSJcEEZzJSd0yD0vMsT%2BX3OjvgytLZWblSs97Yl8hq8QoH1tMD7dV098QVyhhPnr7Lr74wY9CY63wDQKNCwhMpzCEsioDhckdarQs9piRLICJFEoIEAmFVd4sYwqlsnl3FQ6xLX6GgXymafM0vAMKqQwVwscfj%2Bzp7BXRM494Z62zRRBfxG61X5xqobi4yCkeiOUEC5b1cAbHUFuTiUshkaXZ2ZIE3%2FOKK0hsbcIq6%2B5Gfzel%2FCi07KQEYLIlfyaoYPlqvCwH57W1jfgepnY%2BDMWvfYPV0QHWCdyubvM64T1EbS6zuvRjmPgdZTvHPwGDzgQF2AmdzQJAklNjVigcSvAank%2FqpYxKJ5VvoT0U%2FqkYui5Xc83qDD3npA8Q8uM9mtI6DGEu%2BlTyewuoSdQapsxOLGrIZ6IvyV7xjxtYSKnhLf6MXmnQFedHEaN0OGdsu9T1VcDB4U39STH%2F%2F3rZenV8%2FUETm4bcN7c%2F%2BggF8OHG9kYKUUjFNBMwxkR0HvnGgVtTWRPUF%2Fu6YkKmAoOOMrGYX%2BoJNCy1AQF3KiEmUY6z6zivWu4rJapQeBnydRldoOXakVS0z2HGcPg8h3uUc32LjHawtWkYApw10cF8yuTZXPzC7ztDLBjqkAa%2Fnn0WS1NMVDHaL%2FmoReBBjEde0KfJqGJXSAPfI3gcj4hB0CSwLJR6SHwUvo0MP8K4OL3CJoC9WH2ZpHW%2BzRvWEOCafA%2FrrgTzf3Vj55OhfNHYvRQ7p8%2FSY2UUKkwiqtmsSRTvvWZNibrHZVe7D0JL6f5ESbJy8%2Fvt5BVFwxqYow4fjLHI9SZpS%2F%2FabCItODTW6jUNyS9W%2FZmCDvbnpaZB70FZF&X-Amz-Signature=f47e7da9597bdf70876e03abed1de51ffdfe5d461cb713fdcda801f2b5f2c9ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

