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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMRGIWYD%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIENTHpR5CRvPSStBJpT7l00hGa34rzf4NxEGGnnLLN97AiEAs9DKi2OqI43WdUPKr%2F41kDzbyTC%2B8jcXxQrnpv0kpGMqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMzdh8kFHxuyPzKYPCrcAyVl9DCyC0CgDty%2FvkyuAzl6X%2FrMH5m6GOT%2FZ4FqcLnmWcmYY%2BFQCduu141BYJq4CZ9rzbTn1rWoCT1BsUrRnG6vc4hMCuWFjvOf4rnl0oeK%2BIta820sKCmVVfFHBg%2FlD2ed0xBNmqadyXgRaWqsp3TCgI8%2FnNkxfrX4zcZZNm1ZHx%2FwWrV%2FbXVOBGj0dRsTgunT6nkhPeuc3DGDBmyjMWFbdzGmH2GuLsqtdgwZiPN9EngX56QAgwuAM%2FiPM0Mt1NFq3spGfUVdSUcXoiz3xOAPzGZ4OhFJeldTj%2BIgRXUh1isWoPnZlbHFfjHJZympJfpBohLQkVBihxAibKs4ijWz96HaZqeXIsLN0jSZCbyQG69Q0S6xzMbWPWh9kqc5IvqAG0dZOPEwkH2rT%2Bf3UcNaBtL0qC1zbJx6ki5XrGqJP1%2F6qEBXK3DUiz0VIq7Vps8a36LXKKAHU5flF8ZvTbrzn4rqeg1Qg8rkC6lvRUICPTIcw%2BOIMGYJT6zRhBcabKLXAxPz87XZiGBxxBoSLImoDp%2BkutWPTWCBcwgxBn4SQnJNGdBhSINi4KattpBoxdzSoSM7zxMqHqweYGtsxL9vATNCM9ACOR3xLSU9ipv6L7zCuT9H9Y%2BZMQhsMO%2FU7ckGOqUBIGPDdir2ixGPsKSNqMKJ8PN58DQE1ymXeMVxGykxmbYMEL8DVtbo8MMdR80HChk%2Bi3NLlXoYCb2Z1vrH4cFA5eaoF7Fwxt7JDX%2FW0xhD1i8SVoPScsLrVMR7laWodl6%2B9tJewWBqgxIojyryUc7iQTx%2BCAnWnFsJs8xPA081mpOu0FIOH1GbGak386AUlrVUunLKcDuwVNl3TIMu3p%2FLhS0z1O%2FT&X-Amz-Signature=c0e1b8fd434d068d4ff4c95c7eeb5cf82968dafa69ea095a848dc54bd6ec18e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMRGIWYD%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIENTHpR5CRvPSStBJpT7l00hGa34rzf4NxEGGnnLLN97AiEAs9DKi2OqI43WdUPKr%2F41kDzbyTC%2B8jcXxQrnpv0kpGMqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMzdh8kFHxuyPzKYPCrcAyVl9DCyC0CgDty%2FvkyuAzl6X%2FrMH5m6GOT%2FZ4FqcLnmWcmYY%2BFQCduu141BYJq4CZ9rzbTn1rWoCT1BsUrRnG6vc4hMCuWFjvOf4rnl0oeK%2BIta820sKCmVVfFHBg%2FlD2ed0xBNmqadyXgRaWqsp3TCgI8%2FnNkxfrX4zcZZNm1ZHx%2FwWrV%2FbXVOBGj0dRsTgunT6nkhPeuc3DGDBmyjMWFbdzGmH2GuLsqtdgwZiPN9EngX56QAgwuAM%2FiPM0Mt1NFq3spGfUVdSUcXoiz3xOAPzGZ4OhFJeldTj%2BIgRXUh1isWoPnZlbHFfjHJZympJfpBohLQkVBihxAibKs4ijWz96HaZqeXIsLN0jSZCbyQG69Q0S6xzMbWPWh9kqc5IvqAG0dZOPEwkH2rT%2Bf3UcNaBtL0qC1zbJx6ki5XrGqJP1%2F6qEBXK3DUiz0VIq7Vps8a36LXKKAHU5flF8ZvTbrzn4rqeg1Qg8rkC6lvRUICPTIcw%2BOIMGYJT6zRhBcabKLXAxPz87XZiGBxxBoSLImoDp%2BkutWPTWCBcwgxBn4SQnJNGdBhSINi4KattpBoxdzSoSM7zxMqHqweYGtsxL9vATNCM9ACOR3xLSU9ipv6L7zCuT9H9Y%2BZMQhsMO%2FU7ckGOqUBIGPDdir2ixGPsKSNqMKJ8PN58DQE1ymXeMVxGykxmbYMEL8DVtbo8MMdR80HChk%2Bi3NLlXoYCb2Z1vrH4cFA5eaoF7Fwxt7JDX%2FW0xhD1i8SVoPScsLrVMR7laWodl6%2B9tJewWBqgxIojyryUc7iQTx%2BCAnWnFsJs8xPA081mpOu0FIOH1GbGak386AUlrVUunLKcDuwVNl3TIMu3p%2FLhS0z1O%2FT&X-Amz-Signature=7f0aa1685275bfcf0b87eb10b02d5dc1714fda502f2259fd49c8568f4cc70621&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

