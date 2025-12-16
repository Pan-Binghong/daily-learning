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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632XODAWK%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoSzRb1kj3EIjK37nYVtHbSA9Coo1qjzpv0sW0p9IlxwIhAPCyKcTjKQ7i%2Fx235lhO2yQe0xxuJyVQqM0zybWztBr8Kv8DCFwQABoMNjM3NDIzMTgzODA1IgyQ6mX77VFjR0SMdLQq3ANJd%2FcZRX9tzn%2BOE7q17s9Bh3MUAj0gqO6qEf8DMLSbhhPv1QYIg5So0316pdG7cbfdZRWLA03bthtRwYt60YcI91g5IHxCxjUIdwlPzKawVah%2B29FoiP4CSjjMC1VaV9hw7sdkRV%2BNFhzDknr3CvCM2DY8n0ehFFfrNTqOxlAJJvjoyZNhqSqRZC09X4uOBPIN3xU0FAFOHyNTwA1IMKmRe1FfbNBsrgi%2FefyOVmBbK1L1EOsqb9bZlS4%2FTbEz0Joj%2Fh8qHhRdDDmIBSALxcR%2BgXoYo6H0PQAtTNoFsoa%2FipbFd6XdG6vspz4xGIb17iPwjBXp7a6tWhDkqqGVWGvmtu7Aj07DgIRjjqmSdChpBgTvogs5OkdnqKZIYa5FQHwcW4GWKrzKPeqGHHWZZDdGLsbTAOIeEBoFbr09BNw7DubfI4WezBT52%2FSJM%2Fk7tZvCqwLv2FHOdSbkvsTm2j0JBNPi22N5stP0DKOx%2Bv96cBS2YUmBJRJLAuQq3BXlP6VLR0q%2FPqz%2FS0CskLx%2ButtOrJ8DUZQF5ooTGGRWhoAiBfWpK6yNopcnMVl%2FiQDVXzhusDzRhWnwg9oNsPCL%2F6mYChIT0KPnjvOEGkSWxuGCWqFMr1PrUaxFGs5kTjDujIPKBjqkAWN3Tb3gH8Ue64P54uX6n%2BtF%2BbOEgtCBZm8OMeWj9XNGoADDgtgfs4WA%2FGQbWtWM%2FMv06smAs1WPhSTd5nqWtbatfqLX9x53oBIsu6zel4REmIuqPNxq1%2FIFXDbb%2F%2BqLK0Hrf2weet391KC3LbdPDoo5hI1UZDvAml6Sijx8GNxV%2FWsRJma6gqP832Dchop59VBHMbgTO68xMutDPDBNBnSMdUIa&X-Amz-Signature=673027747eb03b9f4185e696c605ca33dfa2ea1deb0fcaa056950e76788e0ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632XODAWK%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDoSzRb1kj3EIjK37nYVtHbSA9Coo1qjzpv0sW0p9IlxwIhAPCyKcTjKQ7i%2Fx235lhO2yQe0xxuJyVQqM0zybWztBr8Kv8DCFwQABoMNjM3NDIzMTgzODA1IgyQ6mX77VFjR0SMdLQq3ANJd%2FcZRX9tzn%2BOE7q17s9Bh3MUAj0gqO6qEf8DMLSbhhPv1QYIg5So0316pdG7cbfdZRWLA03bthtRwYt60YcI91g5IHxCxjUIdwlPzKawVah%2B29FoiP4CSjjMC1VaV9hw7sdkRV%2BNFhzDknr3CvCM2DY8n0ehFFfrNTqOxlAJJvjoyZNhqSqRZC09X4uOBPIN3xU0FAFOHyNTwA1IMKmRe1FfbNBsrgi%2FefyOVmBbK1L1EOsqb9bZlS4%2FTbEz0Joj%2Fh8qHhRdDDmIBSALxcR%2BgXoYo6H0PQAtTNoFsoa%2FipbFd6XdG6vspz4xGIb17iPwjBXp7a6tWhDkqqGVWGvmtu7Aj07DgIRjjqmSdChpBgTvogs5OkdnqKZIYa5FQHwcW4GWKrzKPeqGHHWZZDdGLsbTAOIeEBoFbr09BNw7DubfI4WezBT52%2FSJM%2Fk7tZvCqwLv2FHOdSbkvsTm2j0JBNPi22N5stP0DKOx%2Bv96cBS2YUmBJRJLAuQq3BXlP6VLR0q%2FPqz%2FS0CskLx%2ButtOrJ8DUZQF5ooTGGRWhoAiBfWpK6yNopcnMVl%2FiQDVXzhusDzRhWnwg9oNsPCL%2F6mYChIT0KPnjvOEGkSWxuGCWqFMr1PrUaxFGs5kTjDujIPKBjqkAWN3Tb3gH8Ue64P54uX6n%2BtF%2BbOEgtCBZm8OMeWj9XNGoADDgtgfs4WA%2FGQbWtWM%2FMv06smAs1WPhSTd5nqWtbatfqLX9x53oBIsu6zel4REmIuqPNxq1%2FIFXDbb%2F%2BqLK0Hrf2weet391KC3LbdPDoo5hI1UZDvAml6Sijx8GNxV%2FWsRJma6gqP832Dchop59VBHMbgTO68xMutDPDBNBnSMdUIa&X-Amz-Signature=92f0fe2ea04072f7a74b9fc451a55a228d44d3ed01604b468c96c2beea73721b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

