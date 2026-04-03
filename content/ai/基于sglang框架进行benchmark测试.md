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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXVF4J4U%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnf5eBV%2FPf2lYarK2xy1A41k2ddBOWlqntTZWpYyhd%2BgIgYzKhfZxAGk7J5kT%2FXH7HtUVZhnxMRZC%2Bo3T%2FMbP8X8gqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEFwYAEPs0mXkuGrSircA6xD3NfkO0Xzu13XXu0LtkVdUfb22Ka7qzLLXJIZ7jLHNzbAWW8gjYLkRciOdjrcAYoN9gq6TX7SUQcrUDctmnQsOKp0HApvEVmnxAcXjMcEwCe0RR%2FwUC4NtdVQhGEPwabldLdekE7kTVbYYJ600eqipYtb0bbEfyZiLc8nRvj2T2jMNFIKCHKeqKZLTxwVKcBvB3ic%2Fhx%2BKxflBrqiQVoPtMdlu3walPEpOpBrFgagbTBgsC05VZ4lLxRi15jVVxv6CK0X%2FcoHgqCDKkFaRp1YjIrlY6RNpapHCLSEWpbePzh2g1L0qv%2BDtn%2F2yg4MG44F7CgQhJ%2BY38Htm0qC7t2rdhaPJdkFHlNPdLFlOjmWy24ZUzgovWxhxIChHgfLl%2FFwI3LvXwJY1gzObiwqheZFTpD%2FSN5YtWiHLpo6f1a0EBAPKl%2BRLMksPqpAhXOng0TGp%2FN%2BbQTgBPTpOgr%2B76p5hgwHtZ%2FvVUhptSxA77PtDMM25Sx2aGDC0J0ugqY0NCJ99zkHurltExm%2Bd%2FHFHPcEM%2BbUucGpNKs%2BDff19C2lD2eH0quMCVS0aG0fbw%2BLOuU2g%2BLyK0uTw%2BrbNJ%2BqqyuZ95I8oo0%2FL8SCoSrz9xF7vtfDGOIfA4wzGe5YMJLRvc4GOqUB77q8buE8hsKUC3qNFvFB7AYQqJl81H3t63D9JyjUkg2Qh7Lf05RSXi0QD1u%2BQBU2gUMrafsp8gIFbR7jgCVyPzpQdAwq1WF7FxeKA%2Blw4AXJjmMlwFyWdQjzL1wsivqn4Ly%2B9v9YEtjhBhN7X%2Fq5wo4sDrsn4Mzdlg52f0w8MVDIcuv1MLHGH4L4omJHYoRMK5BQbDBX0gpUCGNPrUXyjtgoKk2a&X-Amz-Signature=5cfd7e4baf0fbc23cd9e3477d494ed3b245e4dc128cd2714560bb1f3e5b412c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXVF4J4U%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnf5eBV%2FPf2lYarK2xy1A41k2ddBOWlqntTZWpYyhd%2BgIgYzKhfZxAGk7J5kT%2FXH7HtUVZhnxMRZC%2Bo3T%2FMbP8X8gqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEFwYAEPs0mXkuGrSircA6xD3NfkO0Xzu13XXu0LtkVdUfb22Ka7qzLLXJIZ7jLHNzbAWW8gjYLkRciOdjrcAYoN9gq6TX7SUQcrUDctmnQsOKp0HApvEVmnxAcXjMcEwCe0RR%2FwUC4NtdVQhGEPwabldLdekE7kTVbYYJ600eqipYtb0bbEfyZiLc8nRvj2T2jMNFIKCHKeqKZLTxwVKcBvB3ic%2Fhx%2BKxflBrqiQVoPtMdlu3walPEpOpBrFgagbTBgsC05VZ4lLxRi15jVVxv6CK0X%2FcoHgqCDKkFaRp1YjIrlY6RNpapHCLSEWpbePzh2g1L0qv%2BDtn%2F2yg4MG44F7CgQhJ%2BY38Htm0qC7t2rdhaPJdkFHlNPdLFlOjmWy24ZUzgovWxhxIChHgfLl%2FFwI3LvXwJY1gzObiwqheZFTpD%2FSN5YtWiHLpo6f1a0EBAPKl%2BRLMksPqpAhXOng0TGp%2FN%2BbQTgBPTpOgr%2B76p5hgwHtZ%2FvVUhptSxA77PtDMM25Sx2aGDC0J0ugqY0NCJ99zkHurltExm%2Bd%2FHFHPcEM%2BbUucGpNKs%2BDff19C2lD2eH0quMCVS0aG0fbw%2BLOuU2g%2BLyK0uTw%2BrbNJ%2BqqyuZ95I8oo0%2FL8SCoSrz9xF7vtfDGOIfA4wzGe5YMJLRvc4GOqUB77q8buE8hsKUC3qNFvFB7AYQqJl81H3t63D9JyjUkg2Qh7Lf05RSXi0QD1u%2BQBU2gUMrafsp8gIFbR7jgCVyPzpQdAwq1WF7FxeKA%2Blw4AXJjmMlwFyWdQjzL1wsivqn4Ly%2B9v9YEtjhBhN7X%2Fq5wo4sDrsn4Mzdlg52f0w8MVDIcuv1MLHGH4L4omJHYoRMK5BQbDBX0gpUCGNPrUXyjtgoKk2a&X-Amz-Signature=ae43444b5b40751df7b2f1a5457ae3eb05336258fa048fdff43b8ae3c9ece171&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

