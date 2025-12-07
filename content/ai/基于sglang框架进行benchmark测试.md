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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6JY4JSH%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUZ8u2B28%2BTlMLvsxOTfVTJZlHWFULhsjjvxVDg%2FXdTgIhAOZI7bPD2e84P5L%2FuDIN57XmrRfc4mVzuPbLAflhMExVKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyyuiIBh%2BtdmRr6U64q3AOOog80godXrj8jqFESp1uoW0HJnIbXhlFNGxJpt7ZPUZH4LiquYCiQeRBCG4IUR600IQqlnLgYF01eCqBMhCO6vx3TZK%2BPl3RKZJ2tfC7X0VMkwrF79iO6OxRKxfOrtWePN9GT07bv2jVPFH%2Fw0wS9xkcsDichEoZV6FwbHvccdhzXwBbZuveKPOZQmtB3KScVVC7hoQjFaOzhLn6Vu7dJf%2Fsvri7RhSHQBxcRbMfGjigom1XB4pD3OvjPtWgJslUBTiS%2FI%2FmcllLUhsJjfadwgkljrvZh5A1qKHHfpEjedIhEqrcfUX%2BlH%2Ff7ELvQ0V19uukszWH2QUB6zO7fTTRNtT0sCXgz%2F1sFRULM4fo%2Btoli9anz7PDL0BPoN23FknA9bhWeFCw1j2y95gcDFFbk75am3t9Jl83t%2Bb9Znjy6oxrBqT3QS%2F42EEtrw9lryJ%2BX5r7qRTHAtmIQYoDBT5SWXWI1BVokcktSK8U%2Fj%2BlI%2FKhZ%2Fo%2F325zz%2Bu%2F1CSGPj4792hzeRocR%2BSxhyxtPMEa2Jbkiastf3PreMqGAPPSHnEQy61Uh7rdQZ0PI%2FdcCTAfWS8Kp4KucLSI68sx2KF0ZsULkeQDi7RMmjFTSOjCrGuRaU3Zx4s0Y2tZwADDy%2FdLJBjqkAe9J3hIyWwunpkqkrFl%2FETfwF3MDid1TbbSKadzO6cqIRfdZpuBR9EStYkFcd%2FXf11Nv%2B%2Faha0g%2BZPal97AtLl7v6a7qYLZ9TOJ%2BQRQ66mV%2F8nvHZellENzlDh3cSvmhfJkdCkW11242FswIIk2aD2RiKUq%2F0IET3hvPWuwlgoIFBMzZ3IPf%2Be7KeVwNneF87DG9UPWM77vNZR7zhI2TzfNKST%2F7&X-Amz-Signature=33fa8ebe66994ba57abafcebdaae92adbd8654f107382725efa1151f0060d91e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6JY4JSH%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUZ8u2B28%2BTlMLvsxOTfVTJZlHWFULhsjjvxVDg%2FXdTgIhAOZI7bPD2e84P5L%2FuDIN57XmrRfc4mVzuPbLAflhMExVKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyyuiIBh%2BtdmRr6U64q3AOOog80godXrj8jqFESp1uoW0HJnIbXhlFNGxJpt7ZPUZH4LiquYCiQeRBCG4IUR600IQqlnLgYF01eCqBMhCO6vx3TZK%2BPl3RKZJ2tfC7X0VMkwrF79iO6OxRKxfOrtWePN9GT07bv2jVPFH%2Fw0wS9xkcsDichEoZV6FwbHvccdhzXwBbZuveKPOZQmtB3KScVVC7hoQjFaOzhLn6Vu7dJf%2Fsvri7RhSHQBxcRbMfGjigom1XB4pD3OvjPtWgJslUBTiS%2FI%2FmcllLUhsJjfadwgkljrvZh5A1qKHHfpEjedIhEqrcfUX%2BlH%2Ff7ELvQ0V19uukszWH2QUB6zO7fTTRNtT0sCXgz%2F1sFRULM4fo%2Btoli9anz7PDL0BPoN23FknA9bhWeFCw1j2y95gcDFFbk75am3t9Jl83t%2Bb9Znjy6oxrBqT3QS%2F42EEtrw9lryJ%2BX5r7qRTHAtmIQYoDBT5SWXWI1BVokcktSK8U%2Fj%2BlI%2FKhZ%2Fo%2F325zz%2Bu%2F1CSGPj4792hzeRocR%2BSxhyxtPMEa2Jbkiastf3PreMqGAPPSHnEQy61Uh7rdQZ0PI%2FdcCTAfWS8Kp4KucLSI68sx2KF0ZsULkeQDi7RMmjFTSOjCrGuRaU3Zx4s0Y2tZwADDy%2FdLJBjqkAe9J3hIyWwunpkqkrFl%2FETfwF3MDid1TbbSKadzO6cqIRfdZpuBR9EStYkFcd%2FXf11Nv%2B%2Faha0g%2BZPal97AtLl7v6a7qYLZ9TOJ%2BQRQ66mV%2F8nvHZellENzlDh3cSvmhfJkdCkW11242FswIIk2aD2RiKUq%2F0IET3hvPWuwlgoIFBMzZ3IPf%2Be7KeVwNneF87DG9UPWM77vNZR7zhI2TzfNKST%2F7&X-Amz-Signature=9d4cdaa78551fe582817dec76e22f4504d03bb54ac442b5ad534f5861533eb3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

