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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466336WMKM2%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQD0wPU1YXaG4Wd3YnYhf25tKvAEOwpisBNLqzrNjlnj7gIhAMoeOuZYCxFSFHp9fQdGp52j06HsqvODsw7w2uPWl0pdKv8DCBMQABoMNjM3NDIzMTgzODA1IgxS%2BiDmtecQ2iZ0uMcq3AMjCVPdhjmyPUThgix6QsDQQYVZiKwgdA7wabaq%2Brwbshrt9NyVsAjIz%2FluhOnY70Qsdxfi9igfSZpB2TJMmcpgppIuBuJsceopmsQBTkZG7eexCO301lGTaSrw52Kp333ir2pU%2FHPGgIY4Mk7XekClOG%2BJdY1RpgWeOQE62Lw5nl1jO9kFSjZ13fkMo1tyx3NXhTRkORGKDVLUkpF3viN7I%2FRGXB44NLecJxdsR5YeGtdNupRqF8daCJ7WRrSXWqjP9Hef7vrT4ZxQO0sEwOLokRT%2B1LfZrcIErir3%2Fw5J8NrPPszqQCdd4LUwmqRKARmkgqkMVUz2DcUgtrMWauEo9TsYIfkfEkhjDFR9c2DFiv%2FFiqgNhVnF6lD2LIyzyR9F32acw8MiO35DuEurs4G29DBy0hbtZTZD5TqvTty3uPLNergmfmSDafmpeVEeJnSUl1sT4V3CM4FYYZIabjF56Iw1UZlmotNwmZ5fr2Pku79xRSZIuChuTx%2BXtlyoGYGkSKBBK1E8LDV6vthPMRs5S1Txq0uXqGw%2BGKZ8I5%2FCSP5Ke6hoU%2Bqos08TXs%2FykRCKgupbH9n0024icuMR%2Bo42PIaBWSkL8kmqCvjw0wytG9zOn89hn1Nv4FfyNDCsl5bPBjqkAT3z9T%2BHcq7d6UndNu8W%2BQU5eF5RjdPfQMcKJOFG8iz7q8J8h8TcOmq2TCWDAIjOS%2BCgR0OHLMdJkDmR7c1yVgNEluAI1QPKyYngbnoqXYJuMEe76OddpumffM7bp6qljXbWSvl3aJaYfAoNDXWvZNkD9c69%2BIqGoNF6wpjmGwbbvPTloLXi1g9Ny8SQne3bDlD7jcGTDCr4SfrGnFMZwFEh4dW%2F&X-Amz-Signature=4dceaf99c612acb64637fd6a0ee24e3c14a30cda265a0e69b17aabbbed09a36f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466336WMKM2%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQD0wPU1YXaG4Wd3YnYhf25tKvAEOwpisBNLqzrNjlnj7gIhAMoeOuZYCxFSFHp9fQdGp52j06HsqvODsw7w2uPWl0pdKv8DCBMQABoMNjM3NDIzMTgzODA1IgxS%2BiDmtecQ2iZ0uMcq3AMjCVPdhjmyPUThgix6QsDQQYVZiKwgdA7wabaq%2Brwbshrt9NyVsAjIz%2FluhOnY70Qsdxfi9igfSZpB2TJMmcpgppIuBuJsceopmsQBTkZG7eexCO301lGTaSrw52Kp333ir2pU%2FHPGgIY4Mk7XekClOG%2BJdY1RpgWeOQE62Lw5nl1jO9kFSjZ13fkMo1tyx3NXhTRkORGKDVLUkpF3viN7I%2FRGXB44NLecJxdsR5YeGtdNupRqF8daCJ7WRrSXWqjP9Hef7vrT4ZxQO0sEwOLokRT%2B1LfZrcIErir3%2Fw5J8NrPPszqQCdd4LUwmqRKARmkgqkMVUz2DcUgtrMWauEo9TsYIfkfEkhjDFR9c2DFiv%2FFiqgNhVnF6lD2LIyzyR9F32acw8MiO35DuEurs4G29DBy0hbtZTZD5TqvTty3uPLNergmfmSDafmpeVEeJnSUl1sT4V3CM4FYYZIabjF56Iw1UZlmotNwmZ5fr2Pku79xRSZIuChuTx%2BXtlyoGYGkSKBBK1E8LDV6vthPMRs5S1Txq0uXqGw%2BGKZ8I5%2FCSP5Ke6hoU%2Bqos08TXs%2FykRCKgupbH9n0024icuMR%2Bo42PIaBWSkL8kmqCvjw0wytG9zOn89hn1Nv4FfyNDCsl5bPBjqkAT3z9T%2BHcq7d6UndNu8W%2BQU5eF5RjdPfQMcKJOFG8iz7q8J8h8TcOmq2TCWDAIjOS%2BCgR0OHLMdJkDmR7c1yVgNEluAI1QPKyYngbnoqXYJuMEe76OddpumffM7bp6qljXbWSvl3aJaYfAoNDXWvZNkD9c69%2BIqGoNF6wpjmGwbbvPTloLXi1g9Ny8SQne3bDlD7jcGTDCr4SfrGnFMZwFEh4dW%2F&X-Amz-Signature=cd133cb7ad3cdf17a0f2272bb0354946abb3265b258e2b71898111ac637e9565&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

