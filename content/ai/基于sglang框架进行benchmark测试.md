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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AGCG6VI%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIEyXXhVXOXPfVEB8DqVYoh%2FdkPrxlBABkbkLsg7Dn6KIAiEA6qgGhK0IP4hh%2FKJJT%2FcrhIn4hMtC7mLCG6w9TJlEvI4qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDNYHZiEnEeMPqAvSrcA8ADFDNKCJPcMsw29V2VWBsCkujp91mQr6gFw9cX44xB5Fpfgdg4jgLpGn0L2PpezgTIzjvqNv42x2iijqKwlcKObEsdq0IqwCFpk%2FhJGbw20raNGi3q%2FFGWboo2rk8M8owFiEvsNl0z2o0WG%2FD%2BchZjOxMGUJ5vY3qzoPNcO4JWWPm7Lgz3K5K8Fp4sDtx2bS51aTkYrXh5gECfJOJdKmMWDoRA6l%2FGhVtPnvWymd3JEg3qOecuhwKp5ctAzxOsn9vzaCBWZZDzpe5ZfEywiDAiF%2FdNYg3to71AX9eiNpMN5wmTe2pFQ2RRortyRJx7SzAX%2BRbgwD2g74Y%2FeV7wA5%2Bkd8WKnXLl6aTWsxz7GKhX57gbubFlwAvtlinwK31fvH6BYw8mJWoS8n67Fp5NS2nZu8pJmLKKcWSOCqXjA3QYMaJSnOTbVIM4phwiIHLegwnyJhMK1RHr%2BEGf7r1rlLPG1OffZWI6ugOZimcbr1C9m7SWHjVc4foRzSbJLHufNchWUAdvDskTgh3iBsF0sZb%2BnJxp8rH7jEVsxNYsdIY%2BTPMKz566RFF69iA%2FzWN3oPL4VDlUtJip0%2Fx1fqT%2F%2BajtDy%2BPxHCu84%2FD8qAsPJcUQoXk21Avt68%2BzGOUMKHAv8wGOqUB0WK3u3euOV73jNMe9fxf9%2FPyRo%2F%2FSVN7DIPbaei%2ByzYnUI5ZZQlhqI6GzyUmrQRFTrc%2BEJg25bn1fd40Sopbl7Huf6ZzbsLW8M8CSaeZrhl%2BEe%2F2nDYd%2Byht47z3RxaMAT7qqego7sLnGK1Pfhcl2oQo6h%2BtZMGhb0lkUWNykE%2F4sMCSWzR8E1mdSCVuG2aAGiCqBHbSaRJ1wdbg2kq6m8IJhj09&X-Amz-Signature=9a1a1b0d887649287c8b7ea2c648e86b7c155856d814117373ab46a26fab3919&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AGCG6VI%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIEyXXhVXOXPfVEB8DqVYoh%2FdkPrxlBABkbkLsg7Dn6KIAiEA6qgGhK0IP4hh%2FKJJT%2FcrhIn4hMtC7mLCG6w9TJlEvI4qiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDNYHZiEnEeMPqAvSrcA8ADFDNKCJPcMsw29V2VWBsCkujp91mQr6gFw9cX44xB5Fpfgdg4jgLpGn0L2PpezgTIzjvqNv42x2iijqKwlcKObEsdq0IqwCFpk%2FhJGbw20raNGi3q%2FFGWboo2rk8M8owFiEvsNl0z2o0WG%2FD%2BchZjOxMGUJ5vY3qzoPNcO4JWWPm7Lgz3K5K8Fp4sDtx2bS51aTkYrXh5gECfJOJdKmMWDoRA6l%2FGhVtPnvWymd3JEg3qOecuhwKp5ctAzxOsn9vzaCBWZZDzpe5ZfEywiDAiF%2FdNYg3to71AX9eiNpMN5wmTe2pFQ2RRortyRJx7SzAX%2BRbgwD2g74Y%2FeV7wA5%2Bkd8WKnXLl6aTWsxz7GKhX57gbubFlwAvtlinwK31fvH6BYw8mJWoS8n67Fp5NS2nZu8pJmLKKcWSOCqXjA3QYMaJSnOTbVIM4phwiIHLegwnyJhMK1RHr%2BEGf7r1rlLPG1OffZWI6ugOZimcbr1C9m7SWHjVc4foRzSbJLHufNchWUAdvDskTgh3iBsF0sZb%2BnJxp8rH7jEVsxNYsdIY%2BTPMKz566RFF69iA%2FzWN3oPL4VDlUtJip0%2Fx1fqT%2F%2BajtDy%2BPxHCu84%2FD8qAsPJcUQoXk21Avt68%2BzGOUMKHAv8wGOqUB0WK3u3euOV73jNMe9fxf9%2FPyRo%2F%2FSVN7DIPbaei%2ByzYnUI5ZZQlhqI6GzyUmrQRFTrc%2BEJg25bn1fd40Sopbl7Huf6ZzbsLW8M8CSaeZrhl%2BEe%2F2nDYd%2Byht47z3RxaMAT7qqego7sLnGK1Pfhcl2oQo6h%2BtZMGhb0lkUWNykE%2F4sMCSWzR8E1mdSCVuG2aAGiCqBHbSaRJ1wdbg2kq6m8IJhj09&X-Amz-Signature=9b9a935b40665ac35fd9b4d0ca3eca1f018a5f1295cc8700c1b656079c9a28d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

