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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q73HEHQK%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCRIJds5nDCCMoGpEc8CSn9UDxs9eTKvSAuJqC8sVnpAiAwM5zbJUablNuhopm3tyz7S9nnTAzvCXvGuQmCSKCneCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3%2B62PJ3Hs7L6BqSyKtwDsFJVDivm2Edvvm%2BlsquAOS6nEvuGkcyj6jQQbxoLV2U7I%2FNBpW79uUaRSjPRQBgySE%2BuLS1PXZY%2BbUspLEIW55tqMeUFzJ00XBsOaSZB%2BR1S3AZxbFiAcpQ4z%2Bm1sJD7rx0WV%2FSLl1iIExvBixg3QHPOdDgwQcRtkYPhW4eDApo67zOqi5W8iWAffnn9iT1KKF7UymnGtr9NtaZRotoWyzvJ0kE3Pghi%2B8HutGEh9Hisekr%2BsNeuYs3iQDZ1FHVlOJfZ9cLZLLglLwv1NSAzWCdEytUJKeXz50O76BGDpNeaBrOZ0Il5qj6ebRzQO5gNl9Gq1ZFDupmI2L%2BpPE9ugw8WhEasEGgaTQNujGXP6grlrlcmt2BagYXGjkKTuByU7ZB05BIZe00Z55PTUcOymctqVv9z%2FbsmN%2FaT8RGtQbE3gG7pJ6FcqfGf2NbaVv6fS80lBmGFPfFu63zvomUcCf3T8rbjAbqH5ezhs5brHjbGplNOyFkommSFz%2FQmsSDRHpc6kI66n4I59zal9TpjY3A3kIItyl16e06aOpZQCaQ80B6O1G1WwGq3REEvN1xHlqUnUQUiNgZCC%2BxOf63vcpsZuCHAVy8fEAyE%2FCU3GbQ0BxGqz1pTyPAXgBIw%2B5P7ywY6pgFK6XFPBpR0qdJoJAXAjorsC0AIKzWXG5IEt44PWPDV9f1CXgECxCyJnELvJ6bcOrqUiGMv57QpSRXAf9Vt91YuyT5ASGIW2ZqjKsGtJ%2BLjjl5E3L8AeTgm8rYhqyITMe7JzukbNQPpuJxjnRYKcT4vJ6Ez2rAQ0HLTKuDLAiSVOg72xzr%2Ff97KgPCPD8%2FxI3%2FVX%2FfvTrCOoadx1ioJ509KzOnne5qL&X-Amz-Signature=a71f36436ba492904420b1029abd341690596887ffb7e1f3df1333e6b3bbdbca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q73HEHQK%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCRIJds5nDCCMoGpEc8CSn9UDxs9eTKvSAuJqC8sVnpAiAwM5zbJUablNuhopm3tyz7S9nnTAzvCXvGuQmCSKCneCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3%2B62PJ3Hs7L6BqSyKtwDsFJVDivm2Edvvm%2BlsquAOS6nEvuGkcyj6jQQbxoLV2U7I%2FNBpW79uUaRSjPRQBgySE%2BuLS1PXZY%2BbUspLEIW55tqMeUFzJ00XBsOaSZB%2BR1S3AZxbFiAcpQ4z%2Bm1sJD7rx0WV%2FSLl1iIExvBixg3QHPOdDgwQcRtkYPhW4eDApo67zOqi5W8iWAffnn9iT1KKF7UymnGtr9NtaZRotoWyzvJ0kE3Pghi%2B8HutGEh9Hisekr%2BsNeuYs3iQDZ1FHVlOJfZ9cLZLLglLwv1NSAzWCdEytUJKeXz50O76BGDpNeaBrOZ0Il5qj6ebRzQO5gNl9Gq1ZFDupmI2L%2BpPE9ugw8WhEasEGgaTQNujGXP6grlrlcmt2BagYXGjkKTuByU7ZB05BIZe00Z55PTUcOymctqVv9z%2FbsmN%2FaT8RGtQbE3gG7pJ6FcqfGf2NbaVv6fS80lBmGFPfFu63zvomUcCf3T8rbjAbqH5ezhs5brHjbGplNOyFkommSFz%2FQmsSDRHpc6kI66n4I59zal9TpjY3A3kIItyl16e06aOpZQCaQ80B6O1G1WwGq3REEvN1xHlqUnUQUiNgZCC%2BxOf63vcpsZuCHAVy8fEAyE%2FCU3GbQ0BxGqz1pTyPAXgBIw%2B5P7ywY6pgFK6XFPBpR0qdJoJAXAjorsC0AIKzWXG5IEt44PWPDV9f1CXgECxCyJnELvJ6bcOrqUiGMv57QpSRXAf9Vt91YuyT5ASGIW2ZqjKsGtJ%2BLjjl5E3L8AeTgm8rYhqyITMe7JzukbNQPpuJxjnRYKcT4vJ6Ez2rAQ0HLTKuDLAiSVOg72xzr%2Ff97KgPCPD8%2FxI3%2FVX%2FfvTrCOoadx1ioJ509KzOnne5qL&X-Amz-Signature=92dc1c2837840583e2c60c424f193908ea815a6220b532579db7a78b3e679aca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

