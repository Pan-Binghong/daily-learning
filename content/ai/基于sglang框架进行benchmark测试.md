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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQ5GVRN%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFOq4XWfNAvOXanDfE4DhZaOkmabj5HhiOomBlFGrd4MAiAA4p9wuoXE5v05FmI3M9HsZAkDZx%2FicBnM1cghsYmp%2Byr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMLD5gNS0zdiZyr1lPKtwDCEZnh33%2FRgK70kE28mYGGve6Sp6iJ8u0eTMY0541corkpn6kkWgUqRkOBOnOvJ2B9T8vhU8ByvyTVXcuwyxA2hBUjkTx8xlwjq%2B8sAk3PcNt65fpBL%2BBOpKij5osqxDK5SFa1Tj3EC1jZi5l9rezQi%2F3pGyHMiiGVkzTQzmoxNVd2Ze0OYGktuZ2r%2FgIX9Vn%2BRWJm2BGwKRVLmVvvEd3dPaTTgEQeNR2t6TaSWq%2BnHYN8fNL%2BZK0PnKDFBXCn06gtIQ3F1UYZK9ySnclWs0cnrHYIh2Yw6rR%2BVslwerOuvHRmb3fi35brgS6dvLmS2m2Oyz%2Fj%2B3PaQstKc%2FOZzv2RGyWIHLmGzA3NkYgmnwiGUYxDH2x3uI8HzqjzIyBhZYJ4VVbKwbFhRaBAkjt73VhRTRfY08iC8Uqe8pfT6GBwmOSxlbjhEEYEt1UibtbCv%2Fn3yPYW%2FYhqinf%2Bd9rqG4R34VHI8%2FkUjAuEUWkL46j8XuEdpxFNQEgYkEXdhM42oIOB7R6twx1aVFX9u96NsSLRZq1VU9KB7mHPTkTqhLvjcp7BPgBl8s7YeuKmQ6uPJM5AISQBOeV2Bs3EViHVqgTt69%2FE0hPZxiJ0%2B9GHlLdoQOqfb7HZk9ag7yBirww8dPgywY6pgF2zIgUxeTXfsGFUTStiSfJWZwtDE4Xp0npkjy5FaaAZzxDHMhKg4xOmxil%2BQr1NkHdt7euktnAp4tcWvjf2pLqQcTPPWX7ruDpLKOdCOF0lQWzkpgoJc8bNew49JeHza0Vf9EYEddIv75mnKPZFmhROCN9P6rY0owY56%2Fffl0MAORlnjnKt5jelIz1t4o9LOzHmlySxEbbeXWwqJ1LoEnETjVFjmKE&X-Amz-Signature=1403077b090713933d14c50fa228bf233d6bbcdaeb7484588abf4dfbcddc6758&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAQ5GVRN%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFOq4XWfNAvOXanDfE4DhZaOkmabj5HhiOomBlFGrd4MAiAA4p9wuoXE5v05FmI3M9HsZAkDZx%2FicBnM1cghsYmp%2Byr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMLD5gNS0zdiZyr1lPKtwDCEZnh33%2FRgK70kE28mYGGve6Sp6iJ8u0eTMY0541corkpn6kkWgUqRkOBOnOvJ2B9T8vhU8ByvyTVXcuwyxA2hBUjkTx8xlwjq%2B8sAk3PcNt65fpBL%2BBOpKij5osqxDK5SFa1Tj3EC1jZi5l9rezQi%2F3pGyHMiiGVkzTQzmoxNVd2Ze0OYGktuZ2r%2FgIX9Vn%2BRWJm2BGwKRVLmVvvEd3dPaTTgEQeNR2t6TaSWq%2BnHYN8fNL%2BZK0PnKDFBXCn06gtIQ3F1UYZK9ySnclWs0cnrHYIh2Yw6rR%2BVslwerOuvHRmb3fi35brgS6dvLmS2m2Oyz%2Fj%2B3PaQstKc%2FOZzv2RGyWIHLmGzA3NkYgmnwiGUYxDH2x3uI8HzqjzIyBhZYJ4VVbKwbFhRaBAkjt73VhRTRfY08iC8Uqe8pfT6GBwmOSxlbjhEEYEt1UibtbCv%2Fn3yPYW%2FYhqinf%2Bd9rqG4R34VHI8%2FkUjAuEUWkL46j8XuEdpxFNQEgYkEXdhM42oIOB7R6twx1aVFX9u96NsSLRZq1VU9KB7mHPTkTqhLvjcp7BPgBl8s7YeuKmQ6uPJM5AISQBOeV2Bs3EViHVqgTt69%2FE0hPZxiJ0%2B9GHlLdoQOqfb7HZk9ag7yBirww8dPgywY6pgF2zIgUxeTXfsGFUTStiSfJWZwtDE4Xp0npkjy5FaaAZzxDHMhKg4xOmxil%2BQr1NkHdt7euktnAp4tcWvjf2pLqQcTPPWX7ruDpLKOdCOF0lQWzkpgoJc8bNew49JeHza0Vf9EYEddIv75mnKPZFmhROCN9P6rY0owY56%2Fffl0MAORlnjnKt5jelIz1t4o9LOzHmlySxEbbeXWwqJ1LoEnETjVFjmKE&X-Amz-Signature=e000f05e1face82df404c1081bf5225800ec4061eef77d8451278229dcc0b9d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

