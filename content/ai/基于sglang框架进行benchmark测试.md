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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2Y7RL3E%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQCXJlPToBrE%2Fe2lyw66UYBAOw7CzrYj%2FVF%2FF%2BoznY2X3wIhAPKf%2Bfsj%2BJAtibuF%2FpteP6B74TqgnNJSZzkKlWVx7wu0Kv8DCCQQABoMNjM3NDIzMTgzODA1IgySheRbyBzCy9FOtL0q3AMs5FET8brYft7%2BdVkeGNB9jbUGbDCq%2FbTe6JamjDMmPiw%2BLRgEiGXEATgRcpSEtX7QpR%2BIvKPR6rHlf%2BfQJz1JRQWDtjBS1%2B%2F66JcR%2FR1ymIHeytdz0ARMFGCQ340RCt6TiRRCDBADSjFja%2F4oYnYaooErCvWPkPamJeQyLxtn1fmph2O6U9%2BpDSGtrPuP4%2F4wc5cLt7o5L%2B6ohAnRDa7R4qLiZWcGVQGGOJ0Og3qBFgjStMu7cWVWhHb7Q8FOuxyaBTsatMn7vVaouY%2BsU2zq6GFCFCSDtTY%2BRYy5n6pRGAv29G0cB%2F02jOYsGbRXUFurj6ZSMB6866m7CGct9Mwk%2F7UuhK%2BheORJmxCCIgPWd8LzLT6JzLvXb0NdGOiVONo32tuoC46pg8HPbB9WqjQ42uqQN%2BJlyK%2B3mxZ9Dsz%2FSssBS93M9poEFz1x0CAdVpHPoMpKBb%2F6fvyOyiGCeXoSGfxEeMiLG5nFJCru%2BDVGhsVJwEcKWc3S8cVfBOmZZHTOKgZe0fdS2ROKUNm1n4uFUKy4Akg62lr9%2BFtnEW2S46ygHUsZ8uYhktaqRgzE6U4Qo23YIEMaM0tUVxQLx7ONLvGUaIP5lSbSNHxjquVqmFQCkAtxA0ZtnA5C2jDok5DMBjqkAVZjWsErFL0FFB4Jr2ywB4erPjNaZSZc3A0bfmSEqruvXtMQRVAjsA8atlAaPFZwCqCLq60XrwgYmoRcF43zFRKeQ7ntzIl1GoqfXA%2F7DLnukdDD1nwX6W2IIhAB%2B9EXwZaJamHiqQycHisz6U9g%2FTV4mGITuDWyntRrurgN1p51U9WHGV6yAuLfLzi8a2RWy%2BQ%2BUCk6mbdzS%2Fua4pkokHDPffY2&X-Amz-Signature=7022f41c2b7a650d640413d28ba9a3dda848d8cc8f8fc4ffdf99395444801f23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2Y7RL3E%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQCXJlPToBrE%2Fe2lyw66UYBAOw7CzrYj%2FVF%2FF%2BoznY2X3wIhAPKf%2Bfsj%2BJAtibuF%2FpteP6B74TqgnNJSZzkKlWVx7wu0Kv8DCCQQABoMNjM3NDIzMTgzODA1IgySheRbyBzCy9FOtL0q3AMs5FET8brYft7%2BdVkeGNB9jbUGbDCq%2FbTe6JamjDMmPiw%2BLRgEiGXEATgRcpSEtX7QpR%2BIvKPR6rHlf%2BfQJz1JRQWDtjBS1%2B%2F66JcR%2FR1ymIHeytdz0ARMFGCQ340RCt6TiRRCDBADSjFja%2F4oYnYaooErCvWPkPamJeQyLxtn1fmph2O6U9%2BpDSGtrPuP4%2F4wc5cLt7o5L%2B6ohAnRDa7R4qLiZWcGVQGGOJ0Og3qBFgjStMu7cWVWhHb7Q8FOuxyaBTsatMn7vVaouY%2BsU2zq6GFCFCSDtTY%2BRYy5n6pRGAv29G0cB%2F02jOYsGbRXUFurj6ZSMB6866m7CGct9Mwk%2F7UuhK%2BheORJmxCCIgPWd8LzLT6JzLvXb0NdGOiVONo32tuoC46pg8HPbB9WqjQ42uqQN%2BJlyK%2B3mxZ9Dsz%2FSssBS93M9poEFz1x0CAdVpHPoMpKBb%2F6fvyOyiGCeXoSGfxEeMiLG5nFJCru%2BDVGhsVJwEcKWc3S8cVfBOmZZHTOKgZe0fdS2ROKUNm1n4uFUKy4Akg62lr9%2BFtnEW2S46ygHUsZ8uYhktaqRgzE6U4Qo23YIEMaM0tUVxQLx7ONLvGUaIP5lSbSNHxjquVqmFQCkAtxA0ZtnA5C2jDok5DMBjqkAVZjWsErFL0FFB4Jr2ywB4erPjNaZSZc3A0bfmSEqruvXtMQRVAjsA8atlAaPFZwCqCLq60XrwgYmoRcF43zFRKeQ7ntzIl1GoqfXA%2F7DLnukdDD1nwX6W2IIhAB%2B9EXwZaJamHiqQycHisz6U9g%2FTV4mGITuDWyntRrurgN1p51U9WHGV6yAuLfLzi8a2RWy%2BQ%2BUCk6mbdzS%2Fua4pkokHDPffY2&X-Amz-Signature=a4af86cfc14a7a5d77fbba328fd5625a1a7e89a6d5265d207c9f486137cd0698&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

