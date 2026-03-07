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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RS7EXOJ%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQD0ihvKmrSz%2BIN50BziC8dFjEG%2BS2%2BMCZdy3cfGegCHnAIhAPOz%2Bo4rCc2b%2BGpjEV1YmGJw5sjBKAaqN2H7%2BdXRpqnJKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1jyn9yZaTd%2FzQQBQq3AON0CjeDgyhsQ2CWUaHTGmeMIPkl7IUcyXEmD165T6CrPxMydSq8zIRrQVzefzX1M1IvU%2BAsa12DdUGsQMQESwJnWucI8e75cFQV23XyHZGEzt2V5XJPIqJHTr90sERxhu4e9CV46AhHyk16XYDtb4j5NF3rqsTYg%2BrlWsuWstGSh3DvbYGdRtVkyqO4K3BIy3W9KOi2PJMfAjk6Kp27Ky3vJzabW5pdGsekejiUM9mQlBEd3zquX2P8GubBzOQB1ibRAYbSazpJLwgKZbc4auqPXcflm8Ev2FosCAXdxkGaUnA3UEYbeBMqKYYpMuyk29KlT78r1tjmGiA3oR2eI2Yf0xpYmLDrCZhAl40BxNb45KZvNxjed%2FIVFPgylZF%2FVJZBYovGdERensmhokEf3WgOc8Rc6%2Fd%2F3sfa7n8vfAIqjLppi%2F4sk4ij1%2F7blBofXx2OBvgOg5AcRt9t%2FfGEjjWEM34mQ8v8dDflFO9on13x6crwL2A793Vgkw0dzB3q1Nc%2FQdQS26bacIuyyhuxBJLwpkO7jtBLIsgEiI24YUU5ILrtht896xBAhRryMecwtmv4xEJ1x6EJSLnbtDBiwMfwxUsVSWzYOTjX7HgrB8gs20rCdkGoWmIrk7XRTCGlK7NBjqkAa0hTUjiGb2qMFKf3uGxrjMbQswGxNUOWo3X0dNtSNaf0w%2BdxruvwaybgktLgL1WfTpqvUTUKZTfh3pKLN32F8ohhQposcGjCi4uoALEGlyyKynEnztYlkcu9i3lplW0RXLq5QsqbqPYhsVrSpc39rhWBTlHDRlOYDAkBmx5fp%2BsqnG6%2BK%2F1Ea86lZwvt4m%2F7YIK8Mvqx2%2FKikoSwhMKoTWT%2FuIS&X-Amz-Signature=42c14f0989afa0e5e956c19dc941801911414db04817a97e9d529eaf735424b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RS7EXOJ%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQD0ihvKmrSz%2BIN50BziC8dFjEG%2BS2%2BMCZdy3cfGegCHnAIhAPOz%2Bo4rCc2b%2BGpjEV1YmGJw5sjBKAaqN2H7%2BdXRpqnJKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1jyn9yZaTd%2FzQQBQq3AON0CjeDgyhsQ2CWUaHTGmeMIPkl7IUcyXEmD165T6CrPxMydSq8zIRrQVzefzX1M1IvU%2BAsa12DdUGsQMQESwJnWucI8e75cFQV23XyHZGEzt2V5XJPIqJHTr90sERxhu4e9CV46AhHyk16XYDtb4j5NF3rqsTYg%2BrlWsuWstGSh3DvbYGdRtVkyqO4K3BIy3W9KOi2PJMfAjk6Kp27Ky3vJzabW5pdGsekejiUM9mQlBEd3zquX2P8GubBzOQB1ibRAYbSazpJLwgKZbc4auqPXcflm8Ev2FosCAXdxkGaUnA3UEYbeBMqKYYpMuyk29KlT78r1tjmGiA3oR2eI2Yf0xpYmLDrCZhAl40BxNb45KZvNxjed%2FIVFPgylZF%2FVJZBYovGdERensmhokEf3WgOc8Rc6%2Fd%2F3sfa7n8vfAIqjLppi%2F4sk4ij1%2F7blBofXx2OBvgOg5AcRt9t%2FfGEjjWEM34mQ8v8dDflFO9on13x6crwL2A793Vgkw0dzB3q1Nc%2FQdQS26bacIuyyhuxBJLwpkO7jtBLIsgEiI24YUU5ILrtht896xBAhRryMecwtmv4xEJ1x6EJSLnbtDBiwMfwxUsVSWzYOTjX7HgrB8gs20rCdkGoWmIrk7XRTCGlK7NBjqkAa0hTUjiGb2qMFKf3uGxrjMbQswGxNUOWo3X0dNtSNaf0w%2BdxruvwaybgktLgL1WfTpqvUTUKZTfh3pKLN32F8ohhQposcGjCi4uoALEGlyyKynEnztYlkcu9i3lplW0RXLq5QsqbqPYhsVrSpc39rhWBTlHDRlOYDAkBmx5fp%2BsqnG6%2BK%2F1Ea86lZwvt4m%2F7YIK8Mvqx2%2FKikoSwhMKoTWT%2FuIS&X-Amz-Signature=313229e78b698e3aff395ac6a9701b8b8970dc89c7313f6d5384b98a65dca190&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

