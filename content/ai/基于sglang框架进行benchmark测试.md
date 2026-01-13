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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466253LWWNN%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQDfJCJg2JKTB%2B%2BKAuot%2FzX%2BKhC92XSs0VG13KWcXzLekwIgfAC5JBEtnxVsDyaK%2BIcu6xZgI%2FJlJBPWZA%2FmOXvuyWsqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEmw2BcLjsy7Ma6VnSrcAw9vUk6Q%2BS%2FEKQxgE1GSoBFuMtJTbPHvn1l4yKAgZudXWdZXwQZMlnXwjHYSLhkAI%2BIytEBDKShchNO9ity9SR%2FFspV%2FAYtUgUGT4ssZ3q%2B5tkgLmhbAIS9mL7zLKxGfUt72qKypEvnFy5%2BOjMxC6dUibBaW1Yn5fu6TYdwII5fiiJpKk4%2B3jixFdeYc0%2F8agsWDKLvPlV2g0tOuClfolMCiM48PW69cDOrnKIlTAJH5%2FUnIwB1MOed7cS4cArr%2Fl1FPvgN9vZ%2BoqN8uMw%2BbY%2BJZr5bOCqGWQZxpCXoW5JA1EWwqprfMOKAcUDym%2FWkCoAzuLLpAWEo9Bd%2BntPJ0d6gHyDaoe7dmEHs8DcLBhEcqIGn63ePQDJiwn1VMUM%2BX%2BC%2BdIwEgIX4q977KyEez3tj3HAo9so0OAeyHFnKhrUNAKqzk%2B2v%2FBQILJxEHppWg8AxbjlLLmximOjdwWCXNapx8fSuVYS2SPaq2pxIFAcygBoZ4lEuLEjgxPKf1rTaqCUReAaTdgvC77z77T%2BsjLUbnaZThHgBI0hz6Q4frNsLTIxtwaVN7XjCanHT%2BxX8fPIYVltbF%2B5FFvx5p9QZk1QbY9iYpGW6DQTPeaNH7ShTs6om0nrj48UlPYuaOMNrllssGOqUBtnKzma%2FOqxvDrfWl%2F72EkocDAEAKBG3s5gtIrBwJDxpKC1c%2B3DDySfjvagMH4oZCvwke%2BWpoQgM7IQdDo2T0jyLB2icwJNs1CISrzteUESkGZsvMHoUpFRjXjS35Kkqfviu3kV7YXbx6B7YaqWqaf094i5jQTBXWJq4PGklp4LWwBTczFTkLvbHUOLQUDO%2Fv9BCXZN8j4JhX6JzYD7HBn9j4n61K&X-Amz-Signature=0d037f376540af9defcc9331c4bfc6f87f9a2610e6fd7f8b118fd722318a404c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466253LWWNN%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQDfJCJg2JKTB%2B%2BKAuot%2FzX%2BKhC92XSs0VG13KWcXzLekwIgfAC5JBEtnxVsDyaK%2BIcu6xZgI%2FJlJBPWZA%2FmOXvuyWsqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEmw2BcLjsy7Ma6VnSrcAw9vUk6Q%2BS%2FEKQxgE1GSoBFuMtJTbPHvn1l4yKAgZudXWdZXwQZMlnXwjHYSLhkAI%2BIytEBDKShchNO9ity9SR%2FFspV%2FAYtUgUGT4ssZ3q%2B5tkgLmhbAIS9mL7zLKxGfUt72qKypEvnFy5%2BOjMxC6dUibBaW1Yn5fu6TYdwII5fiiJpKk4%2B3jixFdeYc0%2F8agsWDKLvPlV2g0tOuClfolMCiM48PW69cDOrnKIlTAJH5%2FUnIwB1MOed7cS4cArr%2Fl1FPvgN9vZ%2BoqN8uMw%2BbY%2BJZr5bOCqGWQZxpCXoW5JA1EWwqprfMOKAcUDym%2FWkCoAzuLLpAWEo9Bd%2BntPJ0d6gHyDaoe7dmEHs8DcLBhEcqIGn63ePQDJiwn1VMUM%2BX%2BC%2BdIwEgIX4q977KyEez3tj3HAo9so0OAeyHFnKhrUNAKqzk%2B2v%2FBQILJxEHppWg8AxbjlLLmximOjdwWCXNapx8fSuVYS2SPaq2pxIFAcygBoZ4lEuLEjgxPKf1rTaqCUReAaTdgvC77z77T%2BsjLUbnaZThHgBI0hz6Q4frNsLTIxtwaVN7XjCanHT%2BxX8fPIYVltbF%2B5FFvx5p9QZk1QbY9iYpGW6DQTPeaNH7ShTs6om0nrj48UlPYuaOMNrllssGOqUBtnKzma%2FOqxvDrfWl%2F72EkocDAEAKBG3s5gtIrBwJDxpKC1c%2B3DDySfjvagMH4oZCvwke%2BWpoQgM7IQdDo2T0jyLB2icwJNs1CISrzteUESkGZsvMHoUpFRjXjS35Kkqfviu3kV7YXbx6B7YaqWqaf094i5jQTBXWJq4PGklp4LWwBTczFTkLvbHUOLQUDO%2Fv9BCXZN8j4JhX6JzYD7HBn9j4n61K&X-Amz-Signature=f02b78c1e062ace6fed44aa19bc69642a2239fb19ebb2a8427c40aa25aab20c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

