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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGKS4IJQ%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQC7mU57q8h47kdeuhvbWuKtpF93MznoXuhbUkDP4TrqcgIgJ5x6tHecHjbRkf8NA%2Fc3ErI8lvPqbeumj%2Borfa%2FWlucq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE0KVXBYdbxIlyQ0ayrcA20wDCCefbDNnvvI9%2FT7BsNq05wjNIC87F%2Fe8QawcqAWpbL5xvfXjxwx9tBogZ9KppzA6IOiEfc6S2cBzyd8fWgc%2F%2F%2BsmyvHj%2FaRH5jn6Cl0Tl9mi1jFAu1RzSJ6kBIWCy7xID2VYm%2B%2FA29F1aXK1lGZaSknrnCVwujV6iEypWLaLqyZ8tFqgCW9dWrmGGP9gQIDmp1SNpMpC9JW9CJuIneCr%2BzpG0eDN5S3SFUiY3EjjrRVk8Hursqte9qGXG%2Fxd7C1Sj6TLAs5JjQM3tiNILw6TwIKOf6hJRyO2NHNWnrU%2FcK6uPTI%2FgXAEIHVzLowcPlZ345QzqBNDY0vzM0Hb6Hw6qHcjdnhSyEgs4EbWDfowz69rlqybmRXNLwelO70f7huCkiLsQU4qPrmCR9ncU9I2RzzZEhqMsMyQ%2BOd2WXGHly5Olq%2B%2B5Hfm5aVzCpYfywdPkpn%2BJ6kKM5o9E%2B7kJw3qFOR0V7p08MUCBTQOaeIVI1KqIEfF4hXQSKUXpba5rBAvoqEIdR5YIEjvJbtV9RhdXUguA%2F9Jw%2BxMiAhlFrRPfDWrpoO03SMSEJ2Kbx3BbaeM%2BlbK7tWsr%2BDLbmCXxeMp%2Fh%2F8DpDsZaMnAwzWkiBVIZo5yoox%2BlpjDexMJGP%2BM0GOqUBHLYj%2FvIaY1%2BwfqvNi2OymqJBc86fT%2BIgnLvvwqfPdBQkdIqI8jtqUv%2BlJ4bE3w6AHaqNABjnZ88X%2FtXN%2FABo1dmngGPKUfU%2Bp5Y2Z3bE5EDy3P49Vz6vRuODO0jLkqEFAo4WITLevJYoKd3%2BuglFdHPjDOQRnw7om70jIrgvLSM1OT%2BLi7yesPhi%2FeGctCSxQGtzyMnxtpmugLG4KhuyUpJjYHKw&X-Amz-Signature=d5c79be15e5a881e478d616a9c4656666309557223cf35f4b02246ba354a07bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGKS4IJQ%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQC7mU57q8h47kdeuhvbWuKtpF93MznoXuhbUkDP4TrqcgIgJ5x6tHecHjbRkf8NA%2Fc3ErI8lvPqbeumj%2Borfa%2FWlucq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDE0KVXBYdbxIlyQ0ayrcA20wDCCefbDNnvvI9%2FT7BsNq05wjNIC87F%2Fe8QawcqAWpbL5xvfXjxwx9tBogZ9KppzA6IOiEfc6S2cBzyd8fWgc%2F%2F%2BsmyvHj%2FaRH5jn6Cl0Tl9mi1jFAu1RzSJ6kBIWCy7xID2VYm%2B%2FA29F1aXK1lGZaSknrnCVwujV6iEypWLaLqyZ8tFqgCW9dWrmGGP9gQIDmp1SNpMpC9JW9CJuIneCr%2BzpG0eDN5S3SFUiY3EjjrRVk8Hursqte9qGXG%2Fxd7C1Sj6TLAs5JjQM3tiNILw6TwIKOf6hJRyO2NHNWnrU%2FcK6uPTI%2FgXAEIHVzLowcPlZ345QzqBNDY0vzM0Hb6Hw6qHcjdnhSyEgs4EbWDfowz69rlqybmRXNLwelO70f7huCkiLsQU4qPrmCR9ncU9I2RzzZEhqMsMyQ%2BOd2WXGHly5Olq%2B%2B5Hfm5aVzCpYfywdPkpn%2BJ6kKM5o9E%2B7kJw3qFOR0V7p08MUCBTQOaeIVI1KqIEfF4hXQSKUXpba5rBAvoqEIdR5YIEjvJbtV9RhdXUguA%2F9Jw%2BxMiAhlFrRPfDWrpoO03SMSEJ2Kbx3BbaeM%2BlbK7tWsr%2BDLbmCXxeMp%2Fh%2F8DpDsZaMnAwzWkiBVIZo5yoox%2BlpjDexMJGP%2BM0GOqUBHLYj%2FvIaY1%2BwfqvNi2OymqJBc86fT%2BIgnLvvwqfPdBQkdIqI8jtqUv%2BlJ4bE3w6AHaqNABjnZ88X%2FtXN%2FABo1dmngGPKUfU%2Bp5Y2Z3bE5EDy3P49Vz6vRuODO0jLkqEFAo4WITLevJYoKd3%2BuglFdHPjDOQRnw7om70jIrgvLSM1OT%2BLi7yesPhi%2FeGctCSxQGtzyMnxtpmugLG4KhuyUpJjYHKw&X-Amz-Signature=d3e36374f47d715ed2725eb4509db67990d7b64a19135a9d7d2a3cf8dc98688d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

