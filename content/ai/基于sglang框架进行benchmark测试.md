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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WA57IBY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIGf1v6%2BLh8LDC1M25DgLk7%2FQaiouf%2FqbYCzjzvE%2F57FgAiAV05pKzvsZsS0%2FCsbi8tmj6yGHhU6jtVqZ4hx6zOXmfCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMn7QRToCMjem%2Bc%2F4iKtwDRVetry7u%2B0YyKU6OmWTO53SaCwAViyRyzUUloeZZsuHylyIzYApHDu%2F6jizMPTV5qFT3yThtIH4mL6HXgybCMIZMSpu8g0m5BpH7yEOd%2BO3bqHB%2FcMzQWpjNgf3y2f2kbw0ZcvvdCcIopkhv0OuvCamNPsH75ERoVn%2BMUnt1CQcT%2FN%2BoAp5B21qqhzmpfQTOAl6dhMJvj5FrBv5wK88wyoku6jIBBhkk%2F7q4OClk%2BmllNSFPtR5Ty4WdG7PuLcnHXyCktQJIDR%2BXdl4mPu%2FQKRCHOyU5H8k9gHb%2BrRh%2FcgPUoScIa6GZIRlVNN9r2gL7vaBEU%2B4JHSMzqmuS8fFFPPvXiKqKZCO6b6AvHfkOEMp8Dn5yvylLe%2Fsxp9Rx9WqqFPsfnJZk7HAjV30Ks%2F5hLHu0f9gu19naDvQOTVZmiblZnk4vqSq7CgGlys9%2Fgs5f8yGMF6%2BcM1oYMgaNeYMPsnhaiL7lk8FaO4BNOvXGLq3EacBgw%2B%2FxLWEzY%2FTVfjU%2F1EaiUoLIzmbJZoIr4wZvuX3pSl31YP0NAYeUXAPAmlX7uf1ppH%2FHKu5Puqp3bgBMoGt4DTKEYa6aLxwa6oFqgEieWi19izSRWnqlvgfIkHx7z0FVtUTXzbcC8qQw9ozzyQY6pgGhBKsBTLMHzkjJPz0w0phWEPhgqlzf8E4V6QAWbFcClR7dPO9HRjhRDF1DYLUZuSdpAVg%2FyZSb5a6OdZBGGTDnU08oEVc0Q3ML7ZWUA4Yx3WkHk2Rnuq8d02kw1e8SHNQJ1D0kHwZr9dJTZ0KDkd5esER4yfi2SBBeMQ5V77%2FXBYrjZv1LR%2FNDQ7cIc00SDsqQ5m0YIaOEG89UoYXuIrCo6eE17SOc&X-Amz-Signature=443de2fd62fccca654f59fda8cba2d8bf73a2c084cba9f75b237270b4ad1cd00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WA57IBY%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIGf1v6%2BLh8LDC1M25DgLk7%2FQaiouf%2FqbYCzjzvE%2F57FgAiAV05pKzvsZsS0%2FCsbi8tmj6yGHhU6jtVqZ4hx6zOXmfCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMn7QRToCMjem%2Bc%2F4iKtwDRVetry7u%2B0YyKU6OmWTO53SaCwAViyRyzUUloeZZsuHylyIzYApHDu%2F6jizMPTV5qFT3yThtIH4mL6HXgybCMIZMSpu8g0m5BpH7yEOd%2BO3bqHB%2FcMzQWpjNgf3y2f2kbw0ZcvvdCcIopkhv0OuvCamNPsH75ERoVn%2BMUnt1CQcT%2FN%2BoAp5B21qqhzmpfQTOAl6dhMJvj5FrBv5wK88wyoku6jIBBhkk%2F7q4OClk%2BmllNSFPtR5Ty4WdG7PuLcnHXyCktQJIDR%2BXdl4mPu%2FQKRCHOyU5H8k9gHb%2BrRh%2FcgPUoScIa6GZIRlVNN9r2gL7vaBEU%2B4JHSMzqmuS8fFFPPvXiKqKZCO6b6AvHfkOEMp8Dn5yvylLe%2Fsxp9Rx9WqqFPsfnJZk7HAjV30Ks%2F5hLHu0f9gu19naDvQOTVZmiblZnk4vqSq7CgGlys9%2Fgs5f8yGMF6%2BcM1oYMgaNeYMPsnhaiL7lk8FaO4BNOvXGLq3EacBgw%2B%2FxLWEzY%2FTVfjU%2F1EaiUoLIzmbJZoIr4wZvuX3pSl31YP0NAYeUXAPAmlX7uf1ppH%2FHKu5Puqp3bgBMoGt4DTKEYa6aLxwa6oFqgEieWi19izSRWnqlvgfIkHx7z0FVtUTXzbcC8qQw9ozzyQY6pgGhBKsBTLMHzkjJPz0w0phWEPhgqlzf8E4V6QAWbFcClR7dPO9HRjhRDF1DYLUZuSdpAVg%2FyZSb5a6OdZBGGTDnU08oEVc0Q3ML7ZWUA4Yx3WkHk2Rnuq8d02kw1e8SHNQJ1D0kHwZr9dJTZ0KDkd5esER4yfi2SBBeMQ5V77%2FXBYrjZv1LR%2FNDQ7cIc00SDsqQ5m0YIaOEG89UoYXuIrCo6eE17SOc&X-Amz-Signature=22b50d53a2c65c2da7edb2d446719dd77f5c8863b0d8204bf6390986dee23e3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

