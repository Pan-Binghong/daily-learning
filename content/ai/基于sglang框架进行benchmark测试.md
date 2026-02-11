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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JJ6KYFP%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGqheYCAUNBkX%2BHtZbt5Fv%2BNa1X8TICE5XcUrlgJe6TwIgZOcirTim15QKvxZj5gVRHLAhWr2YM3YIsQhcGLdD6DEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDWNffLUdyqDBkZ8ircA2BWY1nJp78S0X77Zqhv9BWKPjHdqc8YZ3yxFFzKK%2FqTELOpw2%2FIjvgV5tHmTq%2Fcp2aPRk23F0syb%2BKhcX7SlZXGWAKFpvH0AdJI83pf1HXPYXgLwdgmtL1pJIFvfZHggSbN2LlSb8uUb3f80lx5AvyQLnr7vQyvnF2K9RApkgWxbTFTCgIwTIDPZhplLjajTLBsrkqJt6E4CrlXqJ%2FDjbZyEweIeMOtQC052Ik2ZgPKXbpzuzEp8bvzVL6EVEwHBVKyybIYbgsVZiCM32enEAhHfdgqDF%2BA8JQ4lSnY2%2BRHznuMwqn5KXzlaPtikzpM2ETadt4Gn1loSkPdEAamL2N%2BoNZW7grJqsYGOLNj%2Fi6CCQBR0seo87GUHiZvyyG2fXUXvkUydBDXwdeiGqyL%2BQxoHxfccD5Ouzi5CMEnb%2Bal7Ugd7mtkYOEGlCDPlklqCBefh%2Bju%2BVGoG2ieZLdznLqKGFRkTcaETNxwsSP0uY0cmhBp09AuLuOBEbfGqovPlJYP8Dj4k%2BHrbU%2FSsj3m%2BQdw7PKNmkH2julZKkqQ04ljhAH%2BvidDALSIIuT4YwcmtCJgzoSHLrcjW7hH3SMK3e0ZN0dP9Gn9EV6lC2cvFbWvOFtu2bSAzmFNY94wMJHMr8wGOqUBWI8xWjPpCz3PBF0c5%2FKkEaR%2BJAf3qWPeRciSNlD3ZMHr0wRMhqXuTcRf%2Fpx85rQ4PK4wcYQ2bn5qzdaDhafe%2F11naPfz1t5xdsVw8SOUtoqWgjquy%2BJCR9zEHx%2FNhon1vHYGdxVXOhEqy8I7jgq%2F4h6kXUJS1R7qMQmeoT6C1zgaXjHbdtKkFLONkRsAFQhuWtfU7UJ%2BzlOhvus3uTC8SCCjZ9uV&X-Amz-Signature=81d8f2a00e53616596e2e773ab56db8c0162448279bfa050d9533678ee2e5284&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JJ6KYFP%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGqheYCAUNBkX%2BHtZbt5Fv%2BNa1X8TICE5XcUrlgJe6TwIgZOcirTim15QKvxZj5gVRHLAhWr2YM3YIsQhcGLdD6DEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKDWNffLUdyqDBkZ8ircA2BWY1nJp78S0X77Zqhv9BWKPjHdqc8YZ3yxFFzKK%2FqTELOpw2%2FIjvgV5tHmTq%2Fcp2aPRk23F0syb%2BKhcX7SlZXGWAKFpvH0AdJI83pf1HXPYXgLwdgmtL1pJIFvfZHggSbN2LlSb8uUb3f80lx5AvyQLnr7vQyvnF2K9RApkgWxbTFTCgIwTIDPZhplLjajTLBsrkqJt6E4CrlXqJ%2FDjbZyEweIeMOtQC052Ik2ZgPKXbpzuzEp8bvzVL6EVEwHBVKyybIYbgsVZiCM32enEAhHfdgqDF%2BA8JQ4lSnY2%2BRHznuMwqn5KXzlaPtikzpM2ETadt4Gn1loSkPdEAamL2N%2BoNZW7grJqsYGOLNj%2Fi6CCQBR0seo87GUHiZvyyG2fXUXvkUydBDXwdeiGqyL%2BQxoHxfccD5Ouzi5CMEnb%2Bal7Ugd7mtkYOEGlCDPlklqCBefh%2Bju%2BVGoG2ieZLdznLqKGFRkTcaETNxwsSP0uY0cmhBp09AuLuOBEbfGqovPlJYP8Dj4k%2BHrbU%2FSsj3m%2BQdw7PKNmkH2julZKkqQ04ljhAH%2BvidDALSIIuT4YwcmtCJgzoSHLrcjW7hH3SMK3e0ZN0dP9Gn9EV6lC2cvFbWvOFtu2bSAzmFNY94wMJHMr8wGOqUBWI8xWjPpCz3PBF0c5%2FKkEaR%2BJAf3qWPeRciSNlD3ZMHr0wRMhqXuTcRf%2Fpx85rQ4PK4wcYQ2bn5qzdaDhafe%2F11naPfz1t5xdsVw8SOUtoqWgjquy%2BJCR9zEHx%2FNhon1vHYGdxVXOhEqy8I7jgq%2F4h6kXUJS1R7qMQmeoT6C1zgaXjHbdtKkFLONkRsAFQhuWtfU7UJ%2BzlOhvus3uTC8SCCjZ9uV&X-Amz-Signature=843988265c696bcbd913c149f6f07be5ea8f412e2219e25f789d21c82a123efe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

