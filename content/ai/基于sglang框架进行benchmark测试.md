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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSNLWBFI%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIybC3gI6G8n%2FZ9b2SoWtcx0TTG8PA67y%2FW2%2FnRqpZQIhALkYv8ZQlqxNfr8Vq2ql%2FVVSKJq66U5OpVPcqTTn5GwSKv8DCFQQABoMNjM3NDIzMTgzODA1Igy5nvHW6BsYq%2BObmOkq3AO0MqpIifb1nuj9dRj8SZ2qVL64eu5AJ5jMoqG9STgjPi4NmZD9H16s0eqYGouS4cOXCc1fbkqfcVaHVCcqRJQi3RCY1tn9TIweRicgnyvWEOmOjnoXNzgyh5LcU%2Bh7uMhx8jai25xYVIr0I3zzdQGSuXJgEve27tcEG%2Fp%2Fz2JSrSdqBhJ%2FMmd9VL5gbWg256obU%2BTDdqShSlHBcjJIoIKyoFOa4QSIBGAWmEExOCuocaeMV0XPqHwxlldG3SXsDa0XRk0RB29Co45GWMZnNfyfxhQJ4rZOVIZKCrUGbZlUfEyfFalrFqfsGihWFz12w6NL%2FTvKRSowyF8eZIZHUaaVq113tyvw54Dx%2FjwLjD7hXSNBH2cbrfYULpfQVZACNshFbC1OGPJeMOxaQAvmE24ZLjwin0ZO6%2BrPCHrvNBNqdT05Rc6JgwR%2Fm3bbpMLOkx%2BORrnHwSiPoRBVwAYhmnmrkzMyftPcim0prJK9Da7OUFrtI%2F8bc4%2Bsr3wKGPQuZ4oWUqbbrln7PIzoz%2Bp9Y3czqeQO9B2T7Hf10x5Y2zuTk5g3go3MUXwPSDDxhUIwMI%2FN4G%2B9uFeU1VTc7rr6j56J2oKcpgXoeCvX0DirV1fD7WdgfvWDHiziM1ywEjDyiOzOBjqkAVEhJBclLv0f07hjLpteBylhqCa4suTf%2FqA1jaz6pvQkGnp8fvhZQ%2BwzRm3idhbyZozmpClnzGNJ4tZzjbldNRorQ5qE4Degxa7ijCnFxHhSzzq9Uw4CRxNvd2y6l8QlCiqAG%2BJ97imzn9uvOKjaJ791k3jyCI2U9Ay3jMnsh%2FV%2Ft1Kj40zP8c1PVbFiYihisTl1TZuSad8DAH1wtpg%2BfgP3jT7O&X-Amz-Signature=ed5c7208ab0352d417d92fa1cf5018a6241f58e122229679571dd89e64afe55c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSNLWBFI%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBIybC3gI6G8n%2FZ9b2SoWtcx0TTG8PA67y%2FW2%2FnRqpZQIhALkYv8ZQlqxNfr8Vq2ql%2FVVSKJq66U5OpVPcqTTn5GwSKv8DCFQQABoMNjM3NDIzMTgzODA1Igy5nvHW6BsYq%2BObmOkq3AO0MqpIifb1nuj9dRj8SZ2qVL64eu5AJ5jMoqG9STgjPi4NmZD9H16s0eqYGouS4cOXCc1fbkqfcVaHVCcqRJQi3RCY1tn9TIweRicgnyvWEOmOjnoXNzgyh5LcU%2Bh7uMhx8jai25xYVIr0I3zzdQGSuXJgEve27tcEG%2Fp%2Fz2JSrSdqBhJ%2FMmd9VL5gbWg256obU%2BTDdqShSlHBcjJIoIKyoFOa4QSIBGAWmEExOCuocaeMV0XPqHwxlldG3SXsDa0XRk0RB29Co45GWMZnNfyfxhQJ4rZOVIZKCrUGbZlUfEyfFalrFqfsGihWFz12w6NL%2FTvKRSowyF8eZIZHUaaVq113tyvw54Dx%2FjwLjD7hXSNBH2cbrfYULpfQVZACNshFbC1OGPJeMOxaQAvmE24ZLjwin0ZO6%2BrPCHrvNBNqdT05Rc6JgwR%2Fm3bbpMLOkx%2BORrnHwSiPoRBVwAYhmnmrkzMyftPcim0prJK9Da7OUFrtI%2F8bc4%2Bsr3wKGPQuZ4oWUqbbrln7PIzoz%2Bp9Y3czqeQO9B2T7Hf10x5Y2zuTk5g3go3MUXwPSDDxhUIwMI%2FN4G%2B9uFeU1VTc7rr6j56J2oKcpgXoeCvX0DirV1fD7WdgfvWDHiziM1ywEjDyiOzOBjqkAVEhJBclLv0f07hjLpteBylhqCa4suTf%2FqA1jaz6pvQkGnp8fvhZQ%2BwzRm3idhbyZozmpClnzGNJ4tZzjbldNRorQ5qE4Degxa7ijCnFxHhSzzq9Uw4CRxNvd2y6l8QlCiqAG%2BJ97imzn9uvOKjaJ791k3jyCI2U9Ay3jMnsh%2FV%2Ft1Kj40zP8c1PVbFiYihisTl1TZuSad8DAH1wtpg%2BfgP3jT7O&X-Amz-Signature=a9fb646c2a77958be9b9e59031fcbeecf9d449a0e17cf7c658e4737028bee721&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

