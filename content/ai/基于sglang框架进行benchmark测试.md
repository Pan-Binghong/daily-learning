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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6FLZ5PF%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCICV%2FXrlUUULZOjSXih7T0VMYd1NzTQzX%2B50PEjsTOz6UAiBkh4yUYvInC7HOwQHFBhulfQ6qsBQdiW1ncGBKyPXYaiqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf9xIaSfciLc8AOKMKtwDS5WCKOMrH2b1sWkbWdr30WXnm5rzVZMBmFENundyoK3%2FZoJ6M1x3BfEs3yYS0BTMqV49Tjtjc1dzKuDoMfEgFKLYKeOqfPujt2c%2BVRwuYx31l6F3JZDqKio3JUXl4RqTBLlVG3HW%2BHTT8K%2FX%2Bun6OoXpSFsW%2BnWy8dh2pYSWvV2jaBNk7E%2FMlmAP4vVEsJKQhK9ycs5iIGY%2BZJHqTGcxBNmF5NWdwoTAvtwyZqxVzAUYEZ%2FK%2FiTJ4fD7%2FTNZHx3aMSHqJxKYNTbe%2FCEQjbBuEqrE3AmA4XgzWiN%2FjPF9sR0Qn1OuYmbEEbWxrSd9A7q47maI%2FwDWXVZ2Uk8mfg3SOHK67Dxt5QBgpt8hGQNzDGRGZrD2sYPRMhFJxQnnrV29NY4QTj%2BrzPYGhCAzANbMcN0EA8FrK20WyQ%2BBzxXi3eIu8ZKnYjiYhRKPOoMi5YzftfFa0cK5JnFS6bxLrn2qgY2TrlTnPirx%2BXI5KYuK7umgvpebcOTgwcpjVW5tOdL5%2FUyaOAP8d56SESkCcn4xjWMi3Smb7rL6Uzl1MYISsTeqBSsSyh%2FyhfPUwidI4ZyvdQIA8SZgPOgnkH3m%2BkgOqXzWRvwd4wxF6IRStsttVv%2BWDe5NfEu9xn%2F05hcwstyQzwY6pgE%2B1%2FdQ%2B3qEqijkj7GZIGoC4zxOG2ZNbEqkHsT3VGKVNHKqkHnERadYGutDlzZ9Av%2FbIUa2BPpDPV%2BBtZGbZ0OR6Zi7u4K94XvgCsh8HDLXprmgxAmj9YuHsm9pkPtnkBzgX6Z7S4QlbCXfpiHcbbznHTdD1K7lbyMfXSU59WpMV78El1hIpMJXe%2FmQVrbxi7fisiavO7g1jLklbWnEQ%2BvRIPWII7v6&X-Amz-Signature=71c66de60805e439828ece8977de7726a7b5d15271bc2eeb1a3efc00800ce58f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6FLZ5PF%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCICV%2FXrlUUULZOjSXih7T0VMYd1NzTQzX%2B50PEjsTOz6UAiBkh4yUYvInC7HOwQHFBhulfQ6qsBQdiW1ncGBKyPXYaiqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMf9xIaSfciLc8AOKMKtwDS5WCKOMrH2b1sWkbWdr30WXnm5rzVZMBmFENundyoK3%2FZoJ6M1x3BfEs3yYS0BTMqV49Tjtjc1dzKuDoMfEgFKLYKeOqfPujt2c%2BVRwuYx31l6F3JZDqKio3JUXl4RqTBLlVG3HW%2BHTT8K%2FX%2Bun6OoXpSFsW%2BnWy8dh2pYSWvV2jaBNk7E%2FMlmAP4vVEsJKQhK9ycs5iIGY%2BZJHqTGcxBNmF5NWdwoTAvtwyZqxVzAUYEZ%2FK%2FiTJ4fD7%2FTNZHx3aMSHqJxKYNTbe%2FCEQjbBuEqrE3AmA4XgzWiN%2FjPF9sR0Qn1OuYmbEEbWxrSd9A7q47maI%2FwDWXVZ2Uk8mfg3SOHK67Dxt5QBgpt8hGQNzDGRGZrD2sYPRMhFJxQnnrV29NY4QTj%2BrzPYGhCAzANbMcN0EA8FrK20WyQ%2BBzxXi3eIu8ZKnYjiYhRKPOoMi5YzftfFa0cK5JnFS6bxLrn2qgY2TrlTnPirx%2BXI5KYuK7umgvpebcOTgwcpjVW5tOdL5%2FUyaOAP8d56SESkCcn4xjWMi3Smb7rL6Uzl1MYISsTeqBSsSyh%2FyhfPUwidI4ZyvdQIA8SZgPOgnkH3m%2BkgOqXzWRvwd4wxF6IRStsttVv%2BWDe5NfEu9xn%2F05hcwstyQzwY6pgE%2B1%2FdQ%2B3qEqijkj7GZIGoC4zxOG2ZNbEqkHsT3VGKVNHKqkHnERadYGutDlzZ9Av%2FbIUa2BPpDPV%2BBtZGbZ0OR6Zi7u4K94XvgCsh8HDLXprmgxAmj9YuHsm9pkPtnkBzgX6Z7S4QlbCXfpiHcbbznHTdD1K7lbyMfXSU59WpMV78El1hIpMJXe%2FmQVrbxi7fisiavO7g1jLklbWnEQ%2BvRIPWII7v6&X-Amz-Signature=c06658c1e11003398fb7fddb19c843aa8a7cd1ea94dcf4eca876d9a674dd5e64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

