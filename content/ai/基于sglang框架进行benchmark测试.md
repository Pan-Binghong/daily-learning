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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNPKTYGD%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCAnQJT6G%2B0oh7JJBk%2Fn856uOjZJJf1NkeXOz%2Ft6fIDvgIgOgGAKI%2FkbqLw5Ot607EC7iYY0j5%2BdEHxp%2BRE6ITXKzoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDItPTJyF%2F6NewthDyyrcAwoZig%2B7%2FZvKNbkl8TBBF6d%2BbYk1ONB768joPHIII7m%2FYeaTQN32oI0wjTzCn4rSKFBg3PMYsaYAF%2F3qhS9w8hx%2FPJrkDkiVjvV5bOkSSvqRdVMmBgwsGIw0tkauPvx7E3qlcqk3iK3omPkgt7yzp1e4d7SReOsmAXACcnM4mr%2BlMCrnSQvlLzgKONxS8xpEQUovQT7bM99Ma2I8b0y9DKKjib2ibWLL1mo9dW0HwQB0l4YVjYnan58MGCUmGHGZCjwYWjH7CWVwMSqu7hu5UjrKTDl%2FXUGA9%2F04BwMsjK14MOG0%2FVxFNeD5poPYzwHG4jzUo08gPaH8DbsfBdcU%2BpV%2FWDTH4xMNjF0LGUCEyMNxUlB9KiFSp38Qe8kl6Ax3LOVnrrEgq%2F4JqtWAbdzVyzSc5uCDLJ0OoqyjCanTwbWD3OEw0haLFDndbfZlkReL5EWCBCeuFKMeSMzX7B0FAjx1vOD5WJqL8H9%2F8oRWplNh7%2FwaSHaA73jPPbOUNw3%2FG5AKJyfiEDX11ElYCMNVJi7gDG6w7LSNmpiWG9KvwbAoj%2BL28neFB%2B8yARq%2F2Vi3pq6muRL8ybKxub5hJNW5Fq3S5PiLIy0NjZR3i%2BdThmA1EMJrCJ9EpdaROgknMNq2xMgGOqUBBjOGplQr1gvmRkEqxq1hPGx%2FGhztpJDgQJVqQI0wAt8t%2FxywNBcKFnxqtIFCzNib2Th5spjdg8SW5XUTwSkq9tyFZBbEcDbBeQQnXE9Itm%2BkW3f8oqpl1WCt0R7J45vet1y89fzOBGWC%2BwMkl26htEmRLHmzpE94TxKDhOVf7dzKszwMuNcgAWrcK5dbRCbjVWURqhtXN6cKWt5JXCo56VJk8YbD&X-Amz-Signature=168f4c1cf44ca3947d7210201c1361679f19262453993ebc5e855e58390e3b42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNPKTYGD%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQCAnQJT6G%2B0oh7JJBk%2Fn856uOjZJJf1NkeXOz%2Ft6fIDvgIgOgGAKI%2FkbqLw5Ot607EC7iYY0j5%2BdEHxp%2BRE6ITXKzoqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDItPTJyF%2F6NewthDyyrcAwoZig%2B7%2FZvKNbkl8TBBF6d%2BbYk1ONB768joPHIII7m%2FYeaTQN32oI0wjTzCn4rSKFBg3PMYsaYAF%2F3qhS9w8hx%2FPJrkDkiVjvV5bOkSSvqRdVMmBgwsGIw0tkauPvx7E3qlcqk3iK3omPkgt7yzp1e4d7SReOsmAXACcnM4mr%2BlMCrnSQvlLzgKONxS8xpEQUovQT7bM99Ma2I8b0y9DKKjib2ibWLL1mo9dW0HwQB0l4YVjYnan58MGCUmGHGZCjwYWjH7CWVwMSqu7hu5UjrKTDl%2FXUGA9%2F04BwMsjK14MOG0%2FVxFNeD5poPYzwHG4jzUo08gPaH8DbsfBdcU%2BpV%2FWDTH4xMNjF0LGUCEyMNxUlB9KiFSp38Qe8kl6Ax3LOVnrrEgq%2F4JqtWAbdzVyzSc5uCDLJ0OoqyjCanTwbWD3OEw0haLFDndbfZlkReL5EWCBCeuFKMeSMzX7B0FAjx1vOD5WJqL8H9%2F8oRWplNh7%2FwaSHaA73jPPbOUNw3%2FG5AKJyfiEDX11ElYCMNVJi7gDG6w7LSNmpiWG9KvwbAoj%2BL28neFB%2B8yARq%2F2Vi3pq6muRL8ybKxub5hJNW5Fq3S5PiLIy0NjZR3i%2BdThmA1EMJrCJ9EpdaROgknMNq2xMgGOqUBBjOGplQr1gvmRkEqxq1hPGx%2FGhztpJDgQJVqQI0wAt8t%2FxywNBcKFnxqtIFCzNib2Th5spjdg8SW5XUTwSkq9tyFZBbEcDbBeQQnXE9Itm%2BkW3f8oqpl1WCt0R7J45vet1y89fzOBGWC%2BwMkl26htEmRLHmzpE94TxKDhOVf7dzKszwMuNcgAWrcK5dbRCbjVWURqhtXN6cKWt5JXCo56VJk8YbD&X-Amz-Signature=c6bc793249dfa4680d27d1dbbd2d0e3b58ac3f8298443825b2e94916b9dfc7af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

