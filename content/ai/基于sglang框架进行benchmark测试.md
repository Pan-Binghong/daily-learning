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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Q6NXVTB%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCICpJmKNlQ%2FLZD65JegQbEQAT4d4cqL65zydoqKu1m1T%2BAiEA2qTYU%2BLbcGEC%2BX6Z8%2Ff5IoYdNNgOfFzYZ1vcz9iVcE8q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDOF4IkmVozyLC%2FrGCrcAxUcADyDI%2B4LTs4O4hZirK26H5%2BZC8C%2FMw1tXSSE18CaOWV6ZdXSGaO9aOdDZS6QjwqScORHoPzqCby58y5PsSnYXs%2BpIrwKxKuA0tkmvyfBX2W31xLTvwR02LoP8xNzxqv%2BHUG9U4a88Em%2BN%2B6ndHS7YHdV77X7yIg0NHnB5jvf09avQ%2F0yvi4i5FK1dSNFuRptnbubIdWGOtbfjnsZl0C7PMUsdmDiKAyFTfI%2B6bSdGXwvqL22h8XjEZCLezPEn462Z1a8LOW%2BU7qZxhtT3JBH2a0UiuSy9z24WHK1aNxF73MtV6u1sopVIl3EhPDin8O1JuruGvQnjwKTKh6eabwNm1dEBtAPNBkYLYbqfRNAsemB1GZyFCSsDvoAEwi0TShhfIL2YOfgBmmJhfu1mJagY1oA6usfgFPQ2v9CaKAcDiMINPoPDl%2FddgS0rlOvbs14wII2ajOSDsMFjKJfFtiFfcXzZcwqdNwmP594QVJo20cuuhxiWohPWFnb0vmFprKbqyPJfE7DgmNKQm%2BV47Au8jLzB5luGxhfLMPH%2BJeEzJI49oDmWDYKSDwcQub%2FZ1VVQtYqGINFt6l1vC6bWZuUZcBYSrZAjO%2FdZfAhLWGfbtsIkhc7Ur2gRaSfMIuUyswGOqUBXPUxMiJI501Cjzsah%2FwDnvcVgbWWAdRy249MBK1xCXrNcwOGmr00Uuc6YiRxGOtncReJ8AsfbSDl56zOcMXvdJReneMbYCPkpJeF7EoW%2B8Q8qbH8V1LH%2B%2F5Cpoj57oQbVJNyitTlZl%2Fs4MozOJtGVdwOEDz2thUjN2gss%2B0i51oNuL7vNoWUUJRNSdo1ImUbcItIeK%2B032ZDcvIgnBiDcTAmn75a&X-Amz-Signature=de82a8b9545f8d446a78d64631e944e6450091fa95f589c4213d513400093fd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Q6NXVTB%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCICpJmKNlQ%2FLZD65JegQbEQAT4d4cqL65zydoqKu1m1T%2BAiEA2qTYU%2BLbcGEC%2BX6Z8%2Ff5IoYdNNgOfFzYZ1vcz9iVcE8q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDOF4IkmVozyLC%2FrGCrcAxUcADyDI%2B4LTs4O4hZirK26H5%2BZC8C%2FMw1tXSSE18CaOWV6ZdXSGaO9aOdDZS6QjwqScORHoPzqCby58y5PsSnYXs%2BpIrwKxKuA0tkmvyfBX2W31xLTvwR02LoP8xNzxqv%2BHUG9U4a88Em%2BN%2B6ndHS7YHdV77X7yIg0NHnB5jvf09avQ%2F0yvi4i5FK1dSNFuRptnbubIdWGOtbfjnsZl0C7PMUsdmDiKAyFTfI%2B6bSdGXwvqL22h8XjEZCLezPEn462Z1a8LOW%2BU7qZxhtT3JBH2a0UiuSy9z24WHK1aNxF73MtV6u1sopVIl3EhPDin8O1JuruGvQnjwKTKh6eabwNm1dEBtAPNBkYLYbqfRNAsemB1GZyFCSsDvoAEwi0TShhfIL2YOfgBmmJhfu1mJagY1oA6usfgFPQ2v9CaKAcDiMINPoPDl%2FddgS0rlOvbs14wII2ajOSDsMFjKJfFtiFfcXzZcwqdNwmP594QVJo20cuuhxiWohPWFnb0vmFprKbqyPJfE7DgmNKQm%2BV47Au8jLzB5luGxhfLMPH%2BJeEzJI49oDmWDYKSDwcQub%2FZ1VVQtYqGINFt6l1vC6bWZuUZcBYSrZAjO%2FdZfAhLWGfbtsIkhc7Ur2gRaSfMIuUyswGOqUBXPUxMiJI501Cjzsah%2FwDnvcVgbWWAdRy249MBK1xCXrNcwOGmr00Uuc6YiRxGOtncReJ8AsfbSDl56zOcMXvdJReneMbYCPkpJeF7EoW%2B8Q8qbH8V1LH%2B%2F5Cpoj57oQbVJNyitTlZl%2Fs4MozOJtGVdwOEDz2thUjN2gss%2B0i51oNuL7vNoWUUJRNSdo1ImUbcItIeK%2B032ZDcvIgnBiDcTAmn75a&X-Amz-Signature=68b2ec73589ee0ea2dd9fa7b62d882403ee5bddc3d46c2f43b01021860117fa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

