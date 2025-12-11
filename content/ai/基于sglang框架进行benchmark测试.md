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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXS2ACUE%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDYq4smgKYpOb0xruJ3jPighZkX8FMZRorNsh1fCOPKkAiAfXO0%2B7j17vQ3fvMGg%2FdSCjUrdL7UviYWXQlbGckN3biqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0T%2FQG6bdVlVO1ChsKtwDXn%2Ftok7k23UT1VwSbXFzdQ8RZ96XYBKRC2jJt6i%2BdoEZZpiVeagN9ZM5Y42wK8rrBESoylFe4pi8KVT1WxTmlYFX1AWjGWRjcbgy3np24Id7z%2F4vYMXbz1D0BA4j1qajYCE7ELAltlFj9KyL7XJtT7ypn9C5gZj0MB5aiCUelR6JnYW8FWzPJmHHBVv7nVGvSvFzNz5XLKXaMiTlEUa3%2FvINHr9k5pE%2BzzFKCcqjS9XDBpJlxoxUyJakZVfUSCFGxZUMARCy7j1Ts1tXGLHevEzHnHgtg6nPWwWbiuEKhn7575tjHA6Yu0RZRzSa%2BXBUFqmTKndpu%2BquhY0TJFDkSwxpdFNJ1r0NVFp596vAFYMxxmDZQ1D9DqHKe3xxRbuq7qv08h%2BRj7PFZwX%2BahYy74mN5cgasdctexXtp27iu6Wguv7HvsuiwrddWl0RhqcLE6%2FM9%2BsZJu7vbzs8pCw4E2Kp1OJOkIgNVvTZvaWCjj1HQh4A0TYWA7GaP%2FiOEBl8Znk98G0OncXCRlmDGy7bDjC1rH%2FiUeCTIzULtiE4XvLCblkctk6LUeUVJTfvF2vB5L%2BkohU%2F%2FTcHI2imx9BdFJnwzaMTolKnyO3buV%2FyNCjhlBji%2F13cs3F6AwkwjrXoyQY6pgHyxLcPelKgXMTV8UBP1T%2FjI8Mrh09QVrKdAgWg%2BU1N5LF7edq4rRcoczqUii%2FlHEockyYlAu8ZZaDubvFDKA7GS%2Fog5Xf06EJ1rrnxmGq%2F2LuSumsMYGcrbyX6cFsXd2lKrdcCXkchDZCsSyBLBJp1hFNlHvLMUibscVBpDeaL6kSOIaCp%2FgqhZnscSyiRjkSikVhX4FCD0YIm%2FVpNuTcWqlk11d9A&X-Amz-Signature=1bb6a43c258f87ee7f16884c9b9794958a11e8ecaee20f4095ebe323c95e372c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXS2ACUE%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDYq4smgKYpOb0xruJ3jPighZkX8FMZRorNsh1fCOPKkAiAfXO0%2B7j17vQ3fvMGg%2FdSCjUrdL7UviYWXQlbGckN3biqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0T%2FQG6bdVlVO1ChsKtwDXn%2Ftok7k23UT1VwSbXFzdQ8RZ96XYBKRC2jJt6i%2BdoEZZpiVeagN9ZM5Y42wK8rrBESoylFe4pi8KVT1WxTmlYFX1AWjGWRjcbgy3np24Id7z%2F4vYMXbz1D0BA4j1qajYCE7ELAltlFj9KyL7XJtT7ypn9C5gZj0MB5aiCUelR6JnYW8FWzPJmHHBVv7nVGvSvFzNz5XLKXaMiTlEUa3%2FvINHr9k5pE%2BzzFKCcqjS9XDBpJlxoxUyJakZVfUSCFGxZUMARCy7j1Ts1tXGLHevEzHnHgtg6nPWwWbiuEKhn7575tjHA6Yu0RZRzSa%2BXBUFqmTKndpu%2BquhY0TJFDkSwxpdFNJ1r0NVFp596vAFYMxxmDZQ1D9DqHKe3xxRbuq7qv08h%2BRj7PFZwX%2BahYy74mN5cgasdctexXtp27iu6Wguv7HvsuiwrddWl0RhqcLE6%2FM9%2BsZJu7vbzs8pCw4E2Kp1OJOkIgNVvTZvaWCjj1HQh4A0TYWA7GaP%2FiOEBl8Znk98G0OncXCRlmDGy7bDjC1rH%2FiUeCTIzULtiE4XvLCblkctk6LUeUVJTfvF2vB5L%2BkohU%2F%2FTcHI2imx9BdFJnwzaMTolKnyO3buV%2FyNCjhlBji%2F13cs3F6AwkwjrXoyQY6pgHyxLcPelKgXMTV8UBP1T%2FjI8Mrh09QVrKdAgWg%2BU1N5LF7edq4rRcoczqUii%2FlHEockyYlAu8ZZaDubvFDKA7GS%2Fog5Xf06EJ1rrnxmGq%2F2LuSumsMYGcrbyX6cFsXd2lKrdcCXkchDZCsSyBLBJp1hFNlHvLMUibscVBpDeaL6kSOIaCp%2FgqhZnscSyiRjkSikVhX4FCD0YIm%2FVpNuTcWqlk11d9A&X-Amz-Signature=6844a3c6ab955c42e28ab615bb9a478cf894a30ecfb358787e5a6ac47d947501&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

