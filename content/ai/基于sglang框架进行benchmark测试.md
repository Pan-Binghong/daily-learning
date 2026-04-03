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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UQQ5RHZ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBonxslX7x1K86vA7A%2FvcrMc56M0j4M%2Bkeh7pLFtutynAiEAyaPRQhnSzv7Tg4XyiR%2BYhXcS6bZ3hulD%2BuhLfX0HmScq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDC0zAZCvTxFcBhLppircA4U2gircaa8LTvn8LM%2FeVyR5n9Gm0kvgVOfUxhkYX7sLeUXcczFYYzpzANywNipbrmKiHg8uIN0iFhzt8hWNns%2BFqG%2Fl74OOYZQ%2FSgtkCIseTw%2FZN%2BV%2FIjEsulsk2g9IYhMFSJnH01S6rS%2BxA7UaMzFvjR4TkuCs12%2FEHow99QKCXlM5zeqdy6UqFhbrwehlt9W8sI9DdXVZKsNhFoCLlsbwUnfYs51tIykF9V%2B9SMpB2Wua7%2F1EGxjelYZVOhB%2BSAS9Km7xQSPqyi6rZPQzSL%2BLLXEYDMntf068i9QVzseS%2BvR%2F5AoyGwLIbErySfHu58XEJPx3TxV0Z2tJbyWMNda7gx9ZZRC7MpTNdG1uYFTDnYkW7JNNHiOBOCsnI6A8eV7fHi5pb%2Fw%2BJzAJzoVHJVtLRf2Fdb9UjONCsHezlDRHWYWp3hvyUa2ByVJIFo4r24t9nUTZ1Z8unaZtx4ggTfj72c9x%2F5HHa4Mps6%2FTq05hwGV4Npr%2BwRLI9qV8YThT4dw7%2BoQFl50y8owhc%2FikMrawHcKb8fC8IyZ41GetUbJEQvuzq7vDjNaMEgmmutaklE%2FI7fmEVkFeL9FA%2FP65lcWvStxRIRfNn8wb9jRpEQo0wcM0uDhwyQCVbxLlMKavvc4GOqUBsvumOpD%2BwZRoc%2FYBVZHdSgMK6VW6U5nFkxF5apN0POdtu7x6HI0%2FrL0KcdrXg3zZKT4Jwy3t9Bgantp28jvwna5I4ArbHcaiV8NYnD%2Fn8%2F1NWShoblY8wqBErAi8MA5XXzSxa6SNryhKuDTCoNmLjVB2ODIylEYZcZJePSkxj1hgVvQ003NF8jgaSBDUdop5w4%2BIjrUzgIvJkBrxdPYkI18eIHJZ&X-Amz-Signature=1f6475eba68ea142deeb895989f75f56a5d8ef436bd5600893dd4fad4b0529a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UQQ5RHZ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBonxslX7x1K86vA7A%2FvcrMc56M0j4M%2Bkeh7pLFtutynAiEAyaPRQhnSzv7Tg4XyiR%2BYhXcS6bZ3hulD%2BuhLfX0HmScq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDC0zAZCvTxFcBhLppircA4U2gircaa8LTvn8LM%2FeVyR5n9Gm0kvgVOfUxhkYX7sLeUXcczFYYzpzANywNipbrmKiHg8uIN0iFhzt8hWNns%2BFqG%2Fl74OOYZQ%2FSgtkCIseTw%2FZN%2BV%2FIjEsulsk2g9IYhMFSJnH01S6rS%2BxA7UaMzFvjR4TkuCs12%2FEHow99QKCXlM5zeqdy6UqFhbrwehlt9W8sI9DdXVZKsNhFoCLlsbwUnfYs51tIykF9V%2B9SMpB2Wua7%2F1EGxjelYZVOhB%2BSAS9Km7xQSPqyi6rZPQzSL%2BLLXEYDMntf068i9QVzseS%2BvR%2F5AoyGwLIbErySfHu58XEJPx3TxV0Z2tJbyWMNda7gx9ZZRC7MpTNdG1uYFTDnYkW7JNNHiOBOCsnI6A8eV7fHi5pb%2Fw%2BJzAJzoVHJVtLRf2Fdb9UjONCsHezlDRHWYWp3hvyUa2ByVJIFo4r24t9nUTZ1Z8unaZtx4ggTfj72c9x%2F5HHa4Mps6%2FTq05hwGV4Npr%2BwRLI9qV8YThT4dw7%2BoQFl50y8owhc%2FikMrawHcKb8fC8IyZ41GetUbJEQvuzq7vDjNaMEgmmutaklE%2FI7fmEVkFeL9FA%2FP65lcWvStxRIRfNn8wb9jRpEQo0wcM0uDhwyQCVbxLlMKavvc4GOqUBsvumOpD%2BwZRoc%2FYBVZHdSgMK6VW6U5nFkxF5apN0POdtu7x6HI0%2FrL0KcdrXg3zZKT4Jwy3t9Bgantp28jvwna5I4ArbHcaiV8NYnD%2Fn8%2F1NWShoblY8wqBErAi8MA5XXzSxa6SNryhKuDTCoNmLjVB2ODIylEYZcZJePSkxj1hgVvQ003NF8jgaSBDUdop5w4%2BIjrUzgIvJkBrxdPYkI18eIHJZ&X-Amz-Signature=c0850d1541987c28f58ba646fd58694b86093c72a6731dd455f676412c045478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

