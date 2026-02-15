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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSIOHCPR%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDZPJGHgsnV4rolZCgeB9OMqO3NSldvhrYXmkasU2UqjgIhAII6kNc98x7BTiuVxaBp82D786RkDpclRKqLaYDbXRGgKv8DCBEQABoMNjM3NDIzMTgzODA1IgywyfbHoiJRCkxlBAcq3ANdCi664qNT%2BruDcmd30hrlKKRoWgLIggjBOnr8QJ9yz3ub94%2B8B%2F3bbwZqYijEs%2B7yr0134tdJwYjq2tJ1zMIJm%2Fla%2B6E4nQoM6zcKih5shNXNG0uMVDgR%2FqH%2BjkCxbNomplhRyZ3Z3PgOPfPxQjGrIm0TFZb%2BaU%2Bggp379T4DZyjUJ6UjGXuXp9enikucOQDEdf7LjraFrLR4klOy6VbIENs6W1K4hO3AdzAZmhOqLVXV8NtNK5V%2FHejrDThC1vHdzbHiR%2B47hsgxJN1YYZzRWMxwFB09MLY%2FdUwkRHBhtkRzn3ve%2FCSlZrC5BEQAJBKDWIyaU9zx87nvrFUB8w5n4PaEA%2ByZSx2KH46Syqdnx6jNKrwmMxSXvGR%2FSFAkTi1LtMf3KfD7ppD%2F%2FLvXmc19NRPw3Ohz%2F84ZTZyKsKRY9texrxFj0siKw2KppIeVpODG7uD8XyDvr2R%2F6i81KDoXFA2NhEdqY0cU4Lm51th2vST4%2FA4FWVplgDKtBWiJcTBGarMxjcpSikZS00GqgI5IL3%2BAJnrQ1yLv%2Bokdg%2FNuz3lM90cy8APS8U9%2F6lD4DwHfujcRi2sTJxv%2B%2FP%2F%2BE80aVKHT9l%2FuWsVsBKpgAci93JNWLW6bnpwZNjMvEDCGn8TMBjqkAYGvlFT6xNWc89XT6cFrprMNegt16wVAVr6N6gwfSRqaWEN7aZDPqqvwtJm5A9evNhpeFli5b%2BmpL1GD8nFB1zl5E1UPIi%2FDuCCbywKn2ri1krXcPZarrpHQpPAOyx%2FJZqpny%2BbwaXs4LCw5YGA5%2FgVBDee3f82UaenYNkayytbW3c15xlbFcFYU4BUHn0GJc7RIhhTbG4t8VVcO95hfOk8V8HQd&X-Amz-Signature=0c806ccbcf264e6a855e6424a3e569521672c9983f4b47cff02911833747dbe5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSIOHCPR%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDZPJGHgsnV4rolZCgeB9OMqO3NSldvhrYXmkasU2UqjgIhAII6kNc98x7BTiuVxaBp82D786RkDpclRKqLaYDbXRGgKv8DCBEQABoMNjM3NDIzMTgzODA1IgywyfbHoiJRCkxlBAcq3ANdCi664qNT%2BruDcmd30hrlKKRoWgLIggjBOnr8QJ9yz3ub94%2B8B%2F3bbwZqYijEs%2B7yr0134tdJwYjq2tJ1zMIJm%2Fla%2B6E4nQoM6zcKih5shNXNG0uMVDgR%2FqH%2BjkCxbNomplhRyZ3Z3PgOPfPxQjGrIm0TFZb%2BaU%2Bggp379T4DZyjUJ6UjGXuXp9enikucOQDEdf7LjraFrLR4klOy6VbIENs6W1K4hO3AdzAZmhOqLVXV8NtNK5V%2FHejrDThC1vHdzbHiR%2B47hsgxJN1YYZzRWMxwFB09MLY%2FdUwkRHBhtkRzn3ve%2FCSlZrC5BEQAJBKDWIyaU9zx87nvrFUB8w5n4PaEA%2ByZSx2KH46Syqdnx6jNKrwmMxSXvGR%2FSFAkTi1LtMf3KfD7ppD%2F%2FLvXmc19NRPw3Ohz%2F84ZTZyKsKRY9texrxFj0siKw2KppIeVpODG7uD8XyDvr2R%2F6i81KDoXFA2NhEdqY0cU4Lm51th2vST4%2FA4FWVplgDKtBWiJcTBGarMxjcpSikZS00GqgI5IL3%2BAJnrQ1yLv%2Bokdg%2FNuz3lM90cy8APS8U9%2F6lD4DwHfujcRi2sTJxv%2B%2FP%2F%2BE80aVKHT9l%2FuWsVsBKpgAci93JNWLW6bnpwZNjMvEDCGn8TMBjqkAYGvlFT6xNWc89XT6cFrprMNegt16wVAVr6N6gwfSRqaWEN7aZDPqqvwtJm5A9evNhpeFli5b%2BmpL1GD8nFB1zl5E1UPIi%2FDuCCbywKn2ri1krXcPZarrpHQpPAOyx%2FJZqpny%2BbwaXs4LCw5YGA5%2FgVBDee3f82UaenYNkayytbW3c15xlbFcFYU4BUHn0GJc7RIhhTbG4t8VVcO95hfOk8V8HQd&X-Amz-Signature=1e26518c5e3d91bf369f3624507b13406a6d76f440e640cff85435bcc1e157ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

