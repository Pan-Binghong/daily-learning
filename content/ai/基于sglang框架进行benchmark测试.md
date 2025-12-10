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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMLZ3FN%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIF56EIYl9LW0XDtUV0XxZI3jM3ru%2F6khYrY78HR2vhjpAiAEUl2UICEsEtzMHr9nRr4v4jK4CiISo6YsNxMr9eukhyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TemQDJm%2BXe2qRSUKtwD3gf5i2Im99P80ACwyjaxRM12lIjmObbxA0ZaAa98KHwR8rohr4BgGXFCQkZyMpKdNs4WZz0VX4gKyIODOSANI38UEfTlk3v5ZnlG35cTyH3bTseHUHSIe0NuFtt0f0VSEJ7wuLsbggpu8eebtsta%2FSG192n0QctVEQdg4MQYrfkFRRrMAVGobsc0PCzfiMC6NWlnYQmjTBaM88Ry%2FTa5K%2FjfkpB7FDfRnLmAIQVsGvnlgt4vRwS0sMBcv6zZaQb29rMpZ4PhsEOffOwNPtGEKFiEVSzMMIo5Mo3RKhyDAuvcONUoMb7dEZM7Dc2qdQ9xRkLkfW1%2B3yR%2BncyAvQ2RsZ90ocxZwyqZQEZESczYvQrUCHAMhOV6lzAAENF%2B6%2B7YxAk4fzs%2BJUxTd7jkp9qy2Api7Qj%2FFzp6avRuWn9b7bmPGklo%2FF8PrjEmPgDpaCfm9xRi6UrEVKS7OFnFV8zNh9K96J3wIluPUncAZJBlrYwJTf76iA3ZP8qJu4R6ZPqKWuY4z991GUNGeSKZTbrVP0prKPasOCf%2BUsuquPxfPbhGDTJ0ZH298TaG15Su%2FmOE5esPg6vmwXanFB1ehqNQXmyDoEOi3NAgPtfjIvGmngWFJbVieUBl%2FvMOHogw%2BL%2FjyQY6pgG0dkBIkQl33ZilGd754DKKfEAi8jbrqR0eldA5jkeNZ%2Bbxt2Fv%2BXfuYiA2ieMWENBzjYkPKweQV2s%2FXtapsv7OhVdu9vcLJ0ZHYdrF5Am8BTPjh7igxwogANZV%2B%2B248pujHXjvgf%2BjiHvvuKL5tlE4gtUqO7EVJ9hPk97NIyYWKXslmUgXRHjqsWPfYpqsCpJERu6gFMwz00fieggEqtVyx%2BFxEpuJ&X-Amz-Signature=11b043022eddf7ba52cce0fce461fec3a9a82077362631922d73123c397092ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIMLZ3FN%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIF56EIYl9LW0XDtUV0XxZI3jM3ru%2F6khYrY78HR2vhjpAiAEUl2UICEsEtzMHr9nRr4v4jK4CiISo6YsNxMr9eukhyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8TemQDJm%2BXe2qRSUKtwD3gf5i2Im99P80ACwyjaxRM12lIjmObbxA0ZaAa98KHwR8rohr4BgGXFCQkZyMpKdNs4WZz0VX4gKyIODOSANI38UEfTlk3v5ZnlG35cTyH3bTseHUHSIe0NuFtt0f0VSEJ7wuLsbggpu8eebtsta%2FSG192n0QctVEQdg4MQYrfkFRRrMAVGobsc0PCzfiMC6NWlnYQmjTBaM88Ry%2FTa5K%2FjfkpB7FDfRnLmAIQVsGvnlgt4vRwS0sMBcv6zZaQb29rMpZ4PhsEOffOwNPtGEKFiEVSzMMIo5Mo3RKhyDAuvcONUoMb7dEZM7Dc2qdQ9xRkLkfW1%2B3yR%2BncyAvQ2RsZ90ocxZwyqZQEZESczYvQrUCHAMhOV6lzAAENF%2B6%2B7YxAk4fzs%2BJUxTd7jkp9qy2Api7Qj%2FFzp6avRuWn9b7bmPGklo%2FF8PrjEmPgDpaCfm9xRi6UrEVKS7OFnFV8zNh9K96J3wIluPUncAZJBlrYwJTf76iA3ZP8qJu4R6ZPqKWuY4z991GUNGeSKZTbrVP0prKPasOCf%2BUsuquPxfPbhGDTJ0ZH298TaG15Su%2FmOE5esPg6vmwXanFB1ehqNQXmyDoEOi3NAgPtfjIvGmngWFJbVieUBl%2FvMOHogw%2BL%2FjyQY6pgG0dkBIkQl33ZilGd754DKKfEAi8jbrqR0eldA5jkeNZ%2Bbxt2Fv%2BXfuYiA2ieMWENBzjYkPKweQV2s%2FXtapsv7OhVdu9vcLJ0ZHYdrF5Am8BTPjh7igxwogANZV%2B%2B248pujHXjvgf%2BjiHvvuKL5tlE4gtUqO7EVJ9hPk97NIyYWKXslmUgXRHjqsWPfYpqsCpJERu6gFMwz00fieggEqtVyx%2BFxEpuJ&X-Amz-Signature=33616233952c66d8c69389dceb149c44e76948f17e761d1f7f01109c2c6a57c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

