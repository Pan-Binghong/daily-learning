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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSLB37YY%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDCleUOGhTNZsAzUBnAF3DJVEW5rtjS3VTVefchrKr83wIhAIRdHyfRRp%2FWW9zYNOVJb1OyC3pGxEY%2FW7JkdJbCBJSLKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymUux%2BpkOQ2bhLFJIq3APhLOse%2BN7NqWzyT3x9F9VA7j1hOOb5UZodCN3DbRyOYGpkeGe1vXoKXeFDX6r59gWshaBzqz02pmw5XuztNF7gLqdoVTWcje%2FC3eCyUTpSbAdgdvKxsV60r1DcuFGlQZEbFnkcBY6%2BOnWrVw0H6iadBmxM%2B2Mx77V6UE9qqUkmN8XNbjWGK%2BFnXAoG1%2FXD3w1RaJuS49pkAZhiZT4jpMHM6cgIXV243rkNcNipAfoF4D2M3eb7ga1v3pTrkaOqdiajh73iThtczw72vH7oex0908IowdTCJ9eZhjfvQxMTR7FnB5U00SQe1r1Pdc%2BC8whm4kkO%2FMpYW2OUi5Y30CwCAVOCO8gd0XnFwIRYHkP5QyWpF2jlIECrSDbfG%2FvLphLCZX04qca9Dywb8OsBmJk6e3bg9%2BHqIPfeT45iJY0QsKjrHj6V04Gv%2FN4WowdR6eW%2F3zLEMXyqkiHkPhuUjD8fM6Ayw2sHH3AcVYza18CuQsADTIOyp8m1m30T%2BRGRiwZtFYFPSMcqnejSOUtNlkCxMnMRTCqxesqp%2FDHaqOmYi9gnP3za%2FfzHk%2B6b4fdQgi9Q95uplFbAqd00rBVQpUecQkjpk%2FRk73x%2BMjXKBdEfsBUzTCJpgMfUOfegtjCIk%2B%2FMBjqkAVmUHgLKwUd8j%2BUGrnvSTu72kJXfMrb1Pv2pFNypM%2FKohizcAW3yLeGSNBMf6ImOqjp7rPPBCMm4KrKJCbpnKmXLSQWJGJXK58UASeRNVv8jA98FYoPrkFqNXW67kJL2hkavlr6B76Qmx84q5Yt3NoDE6CrF7V2kIck72r4EiIToeePnNwMnws4XDs%2Fuq3LFDS6PAeGt1crkJfApZSe9Nq2A4vcR&X-Amz-Signature=ff530a47d45199f858f9877a04f0caa9d6134ca2c3c9db76bc121a441f524a83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSLB37YY%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDCleUOGhTNZsAzUBnAF3DJVEW5rtjS3VTVefchrKr83wIhAIRdHyfRRp%2FWW9zYNOVJb1OyC3pGxEY%2FW7JkdJbCBJSLKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymUux%2BpkOQ2bhLFJIq3APhLOse%2BN7NqWzyT3x9F9VA7j1hOOb5UZodCN3DbRyOYGpkeGe1vXoKXeFDX6r59gWshaBzqz02pmw5XuztNF7gLqdoVTWcje%2FC3eCyUTpSbAdgdvKxsV60r1DcuFGlQZEbFnkcBY6%2BOnWrVw0H6iadBmxM%2B2Mx77V6UE9qqUkmN8XNbjWGK%2BFnXAoG1%2FXD3w1RaJuS49pkAZhiZT4jpMHM6cgIXV243rkNcNipAfoF4D2M3eb7ga1v3pTrkaOqdiajh73iThtczw72vH7oex0908IowdTCJ9eZhjfvQxMTR7FnB5U00SQe1r1Pdc%2BC8whm4kkO%2FMpYW2OUi5Y30CwCAVOCO8gd0XnFwIRYHkP5QyWpF2jlIECrSDbfG%2FvLphLCZX04qca9Dywb8OsBmJk6e3bg9%2BHqIPfeT45iJY0QsKjrHj6V04Gv%2FN4WowdR6eW%2F3zLEMXyqkiHkPhuUjD8fM6Ayw2sHH3AcVYza18CuQsADTIOyp8m1m30T%2BRGRiwZtFYFPSMcqnejSOUtNlkCxMnMRTCqxesqp%2FDHaqOmYi9gnP3za%2FfzHk%2B6b4fdQgi9Q95uplFbAqd00rBVQpUecQkjpk%2FRk73x%2BMjXKBdEfsBUzTCJpgMfUOfegtjCIk%2B%2FMBjqkAVmUHgLKwUd8j%2BUGrnvSTu72kJXfMrb1Pv2pFNypM%2FKohizcAW3yLeGSNBMf6ImOqjp7rPPBCMm4KrKJCbpnKmXLSQWJGJXK58UASeRNVv8jA98FYoPrkFqNXW67kJL2hkavlr6B76Qmx84q5Yt3NoDE6CrF7V2kIck72r4EiIToeePnNwMnws4XDs%2Fuq3LFDS6PAeGt1crkJfApZSe9Nq2A4vcR&X-Amz-Signature=245eec98f8a46034e1a55f2d683b6c8bbeaf4d7d740bcdca7fc948a22c502b80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

