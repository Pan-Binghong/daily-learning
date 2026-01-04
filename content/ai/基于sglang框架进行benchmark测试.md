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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CDAA4IO%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHYnZ4AaEjNxRPr%2BFMYw1mmC%2FX%2FgqAkq6cV9GGuCzYcWAiB19NvcU2SBTrosytrG3%2B74ljQCx3IIsfXensFuxTok%2Bir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMoS9CIPhdYvRXeApXKtwD1zn%2B75B19qrMIE87vJeiA0B6m69fF95ILVphePyuHQe3Mmee9McslBBv4HRAPDta8dmxfTIf5jolaRje7GqiHycpOAENlhfcTql5PlARTKlX4OsfRfphGKswejp0eyQmlOxJZcCwkZE5OVEerAWqV8oxkxVJ%2BnafegcSeutNzE8oR68JB6eMUbYHfgrDr5ezO5mAZYntmxqrF7Ukwr35xLUp3AlqZXZJ0DvzxI3leDe9oGxDAwYMIe8wsSBa%2FqycQ8NmoiitUP3bTuuwbVd%2B47sLJBivT8ANj5t%2BpaZRISjWxTF2aEPja1gTO5Tu5tWY%2BNQDlBtB5%2Fqbakqy8jRLzXIiJ7IpkV0Ajr%2BxwphMq2ipBRs%2FPJsImFqlI%2B8oBrK1IRu8g8ubpC0%2Be8pKl7yjM8hnFR3eOMHxbE74cJso%2FV0S1vgnrEQCh1VQRyLqCehrXOm4jVd1JBfnDG3gfspSAao0mUdmZeR2wlIuWYjgpP60NW06yfqaZ0NVtwo4uwEhjkliGTEXxMFNkV0TUg%2BqHG8XGsBWTyRRmWf2qepwJXejQ4Oo%2FTbDr4iDnDliCYDmy1a1ik0jqYYiH5YaadFAxsddf00kmDDgJqkwn2AguKd1As3daARtTdxzqU4wgPHmygY6pgEmhrHwCVPqrSEuYKI%2F9jSPhWFKZC6LwdUfywjAoBemNXDOWqyF4t3Z%2BvOceLC09b5%2Bk3xSKmUmn9Yu4GeEXZBgAiXLJoJhRwm6VyYEwb7fIqxkhIytSEWpcMm4Isvu0FfZI0UAMbmSc8GVR%2FVwvn4zjActh%2FffmAXoA%2F8b8KDBwbZBdW1eJRAl5LCbEin8wECQktXc5yoI%2B%2BXmGog5WXAtVEFzmcQy&X-Amz-Signature=793be1ab3e144db1f48dac49835ab959375b687ac4807a5cc09266e58970ebb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CDAA4IO%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHYnZ4AaEjNxRPr%2BFMYw1mmC%2FX%2FgqAkq6cV9GGuCzYcWAiB19NvcU2SBTrosytrG3%2B74ljQCx3IIsfXensFuxTok%2Bir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMoS9CIPhdYvRXeApXKtwD1zn%2B75B19qrMIE87vJeiA0B6m69fF95ILVphePyuHQe3Mmee9McslBBv4HRAPDta8dmxfTIf5jolaRje7GqiHycpOAENlhfcTql5PlARTKlX4OsfRfphGKswejp0eyQmlOxJZcCwkZE5OVEerAWqV8oxkxVJ%2BnafegcSeutNzE8oR68JB6eMUbYHfgrDr5ezO5mAZYntmxqrF7Ukwr35xLUp3AlqZXZJ0DvzxI3leDe9oGxDAwYMIe8wsSBa%2FqycQ8NmoiitUP3bTuuwbVd%2B47sLJBivT8ANj5t%2BpaZRISjWxTF2aEPja1gTO5Tu5tWY%2BNQDlBtB5%2Fqbakqy8jRLzXIiJ7IpkV0Ajr%2BxwphMq2ipBRs%2FPJsImFqlI%2B8oBrK1IRu8g8ubpC0%2Be8pKl7yjM8hnFR3eOMHxbE74cJso%2FV0S1vgnrEQCh1VQRyLqCehrXOm4jVd1JBfnDG3gfspSAao0mUdmZeR2wlIuWYjgpP60NW06yfqaZ0NVtwo4uwEhjkliGTEXxMFNkV0TUg%2BqHG8XGsBWTyRRmWf2qepwJXejQ4Oo%2FTbDr4iDnDliCYDmy1a1ik0jqYYiH5YaadFAxsddf00kmDDgJqkwn2AguKd1As3daARtTdxzqU4wgPHmygY6pgEmhrHwCVPqrSEuYKI%2F9jSPhWFKZC6LwdUfywjAoBemNXDOWqyF4t3Z%2BvOceLC09b5%2Bk3xSKmUmn9Yu4GeEXZBgAiXLJoJhRwm6VyYEwb7fIqxkhIytSEWpcMm4Isvu0FfZI0UAMbmSc8GVR%2FVwvn4zjActh%2FffmAXoA%2F8b8KDBwbZBdW1eJRAl5LCbEin8wECQktXc5yoI%2B%2BXmGog5WXAtVEFzmcQy&X-Amz-Signature=e7e17b550e9aa249ced92ac808b25ea3a8b348cedac844edf4c61a471b1f67e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

