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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOP2LFZF%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCHDTWAY%2FOJCcJvjeaUbC77Ywu6cPVuUS8g9v3%2Fo63w6gIhANY%2F87Ncm6IWHQeDMPRZt5KC9rFFGD9%2BJIRg6ViARnU%2FKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzARCeK6r5TfyBSRqUq3ANzdCB0yDAYzlaPUxTUW6lIgudWwcNNzdEBd2KwqqJL0j3S49WoE15mLrRghIMch175%2BPSi3AxDN3ckoC4jazQ1de%2BCqJf7IXb%2BObXjBbVHf6cJAP1Tck1tyvfsy4RmgNtisgNy9yvPk4nfbOG6XX0mhrHSo8asQtDwwKNrDpDa%2F55ZnHgkwiTdNRWTe5ZoV%2BbrYXwnYNl3vwY5LN6py%2BpGI%2FeGHrfKAjW2v6NhQD7Wugq53tqFALNmNkmUi2fkOEoUwLMhA3Q7LLNeM8wwHxr3quD3KXJOkOnITe4x70Df9nsOlE4ZQWoNru38CnWF1587SNDYCkh19JFu1SAWciZzX5PjzTFR%2FcNMlSOZg3M1tArYs59F0NJ%2BFG6%2B9qcX%2F%2Br0zxMu7FBxT1vOBq%2Ba9zjU9z7YrhQPzxZ%2BAywpSepBsDhsemk%2BWvMVZnLagMaKRnrSpf9eF2GKm0SHOgwacl0Paoa5DGexDEA5zFXFG6DeCAw7nL53V8%2Fz1%2Fs2c05q2nV9zOjH2Wxh0LLlpFTKUq16zQjbPc9H%2FIgWfGjsvHhaEnCeRc6yVtjLFUyX8%2BzQGbWEcZXOfY9%2FrJy1Dul24nT6mkA3LW2HJblvCmbowBfbUyQdh%2FPqJiOFwjg%2FODDskrXMBjqkAW%2BYP8Bj7hYoENzfnAsOOzu6oBB52qjVg9r%2ByKnLovPJaWOW%2BNGGS7p9akfYcx%2BJgEG9UcR2ekAwJ1tX%2BaRz2SLxjnDZUL1aNZ7fXTaocSxopfJ0i0NDhi%2FtqkI2%2Bc52BADKzhdrmDdHJaRwsXAaQS3uDZ%2B22C4CxT3RNmzgLLsu7YfGJs4A9C8bOni6v0CtF1LdT8ES0eUSir21TB1U0RA26Z0p&X-Amz-Signature=ee61f1d02457207da70b2da09fe72649f1b7aadd51212642b099a7b0aaf833ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOP2LFZF%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCHDTWAY%2FOJCcJvjeaUbC77Ywu6cPVuUS8g9v3%2Fo63w6gIhANY%2F87Ncm6IWHQeDMPRZt5KC9rFFGD9%2BJIRg6ViARnU%2FKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzARCeK6r5TfyBSRqUq3ANzdCB0yDAYzlaPUxTUW6lIgudWwcNNzdEBd2KwqqJL0j3S49WoE15mLrRghIMch175%2BPSi3AxDN3ckoC4jazQ1de%2BCqJf7IXb%2BObXjBbVHf6cJAP1Tck1tyvfsy4RmgNtisgNy9yvPk4nfbOG6XX0mhrHSo8asQtDwwKNrDpDa%2F55ZnHgkwiTdNRWTe5ZoV%2BbrYXwnYNl3vwY5LN6py%2BpGI%2FeGHrfKAjW2v6NhQD7Wugq53tqFALNmNkmUi2fkOEoUwLMhA3Q7LLNeM8wwHxr3quD3KXJOkOnITe4x70Df9nsOlE4ZQWoNru38CnWF1587SNDYCkh19JFu1SAWciZzX5PjzTFR%2FcNMlSOZg3M1tArYs59F0NJ%2BFG6%2B9qcX%2F%2Br0zxMu7FBxT1vOBq%2Ba9zjU9z7YrhQPzxZ%2BAywpSepBsDhsemk%2BWvMVZnLagMaKRnrSpf9eF2GKm0SHOgwacl0Paoa5DGexDEA5zFXFG6DeCAw7nL53V8%2Fz1%2Fs2c05q2nV9zOjH2Wxh0LLlpFTKUq16zQjbPc9H%2FIgWfGjsvHhaEnCeRc6yVtjLFUyX8%2BzQGbWEcZXOfY9%2FrJy1Dul24nT6mkA3LW2HJblvCmbowBfbUyQdh%2FPqJiOFwjg%2FODDskrXMBjqkAW%2BYP8Bj7hYoENzfnAsOOzu6oBB52qjVg9r%2ByKnLovPJaWOW%2BNGGS7p9akfYcx%2BJgEG9UcR2ekAwJ1tX%2BaRz2SLxjnDZUL1aNZ7fXTaocSxopfJ0i0NDhi%2FtqkI2%2Bc52BADKzhdrmDdHJaRwsXAaQS3uDZ%2B22C4CxT3RNmzgLLsu7YfGJs4A9C8bOni6v0CtF1LdT8ES0eUSir21TB1U0RA26Z0p&X-Amz-Signature=5af27d3cdd20f9f834300a1e03506674556ae6968a6bbf5ab284e2a6ece805af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

