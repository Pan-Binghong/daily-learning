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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ML7PZVY%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHi%2BcYvEen%2FeNuYuXbNlxsoM5GcytcRfwM1kQXGiR3VFAiBQztYb2BDgoBJShY5LJKgL8IMJStuV36lak3nSma4kpSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcY%2Bv6hJHmld1yyCEKtwDBq%2FQqee5n7KxQMHrO3ZrOiHwXU8dnE1C8eaGmA7vzLDNI7xy4GnnwRVJVGmgxsPEh0Ho7z32zbirwxCBbAH6prvB1SJyAfsLsNJTJvuzu%2BZUkhh97fbPBL%2BktaXn3GtHlunKGp23oRBx9zNbn4KGX6blcp7nFV%2BNdTAQkCggLDGLMqO273Qfe349ltfCZDIK0h5K6cO5jdK42uBYc1oOq4p7Y0yGnNdGMj826qsxKFjB7fJ3brMzZf1EuuxWD%2FraY8AGtrOjGs2G6oWv9BUQUaz7ZZSsLKFgvQ%2BM4%2F4V0fr2bOapTy4hWc0be0OpI3b1d1VrbCVUHb91cFGOP7JU2k7MUxAmvSmY2tMeBPX8OwpZ%2FTsGnL9y0TBrMBbpPhmJ5VVdm4ejjPnT1FnwRz7KZ%2FGZplQpVHjL3cpb0QzWiKSb7oXx5Ghm4XbzYG7Saw38zvrZ%2BxEMzIbCgeo1Ll4St5R8N999WoXtX6GsSNjBIiG6daOEbHm7QwFUs56%2FRPNhxc%2Bpqzz%2FNKg2EIdkwPAQ%2FJSoeScrsbX4yjdfxpZLyX4WiuBierugeZ5HTCYwBOmmjEa5QqprSO0xc3fFL8rLc6bCHhlXVrT2GR91rl6Oz%2Bo3%2Fjn4d90D3kjKb2Awhr%2FdzQY6pgGWVEq1KHG%2Bg6dWtMtf63I2BQbWH03iNQ%2BU752wcZPvErDtf4gcG30IEBHEr%2B2%2BaklS9IRIBnQVhxeCJgYvzYAqUoc12NMFFG4SyjuCFg3wVnrFjIlhdsXUoxyW19LOy1fHwI0spUTM5wjJSdn0nWZx5Q9lzPa9JI9wbU65IEzoe%2Fu50CwejHdtVGJmXgYZ9wQ71PXXTegFLh8kTHHIw2OUkZYr4fzY&X-Amz-Signature=6b391acf6ac2ce9549579efa6968f54ac019cc158f0efae6037031023393c317&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ML7PZVY%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHi%2BcYvEen%2FeNuYuXbNlxsoM5GcytcRfwM1kQXGiR3VFAiBQztYb2BDgoBJShY5LJKgL8IMJStuV36lak3nSma4kpSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcY%2Bv6hJHmld1yyCEKtwDBq%2FQqee5n7KxQMHrO3ZrOiHwXU8dnE1C8eaGmA7vzLDNI7xy4GnnwRVJVGmgxsPEh0Ho7z32zbirwxCBbAH6prvB1SJyAfsLsNJTJvuzu%2BZUkhh97fbPBL%2BktaXn3GtHlunKGp23oRBx9zNbn4KGX6blcp7nFV%2BNdTAQkCggLDGLMqO273Qfe349ltfCZDIK0h5K6cO5jdK42uBYc1oOq4p7Y0yGnNdGMj826qsxKFjB7fJ3brMzZf1EuuxWD%2FraY8AGtrOjGs2G6oWv9BUQUaz7ZZSsLKFgvQ%2BM4%2F4V0fr2bOapTy4hWc0be0OpI3b1d1VrbCVUHb91cFGOP7JU2k7MUxAmvSmY2tMeBPX8OwpZ%2FTsGnL9y0TBrMBbpPhmJ5VVdm4ejjPnT1FnwRz7KZ%2FGZplQpVHjL3cpb0QzWiKSb7oXx5Ghm4XbzYG7Saw38zvrZ%2BxEMzIbCgeo1Ll4St5R8N999WoXtX6GsSNjBIiG6daOEbHm7QwFUs56%2FRPNhxc%2Bpqzz%2FNKg2EIdkwPAQ%2FJSoeScrsbX4yjdfxpZLyX4WiuBierugeZ5HTCYwBOmmjEa5QqprSO0xc3fFL8rLc6bCHhlXVrT2GR91rl6Oz%2Bo3%2Fjn4d90D3kjKb2Awhr%2FdzQY6pgGWVEq1KHG%2Bg6dWtMtf63I2BQbWH03iNQ%2BU752wcZPvErDtf4gcG30IEBHEr%2B2%2BaklS9IRIBnQVhxeCJgYvzYAqUoc12NMFFG4SyjuCFg3wVnrFjIlhdsXUoxyW19LOy1fHwI0spUTM5wjJSdn0nWZx5Q9lzPa9JI9wbU65IEzoe%2Fu50CwejHdtVGJmXgYZ9wQ71PXXTegFLh8kTHHIw2OUkZYr4fzY&X-Amz-Signature=f33a6eb606963c49f1c101609fdfc3ddffbae98238ba5b79d9b51762675ad8d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

