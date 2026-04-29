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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJEEZ37U%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQDi50i5v4TVOAfg4OqEgJ7JM1BeU9KITwhPBJ30nEZDNgIge0frpy3%2BU1oqx6NOkbqHoa1YqdRrXxbGaebbULVxLAgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMdOE%2FNIlOUzgFp%2FgCrcA%2BARJQWkaGTSmGpkuGyX927fqf1zO2nwhG0XAE8dvKOs0s%2FT%2Bf%2BUSlfNrZuUnAZNcxHo%2BzJh7fdbHs52LnHJrgevHoyCFOa7%2FtWrTAHvx6SmiCnhC4TALskJ3x4CZg%2BNs%2FxIi9cPrwobGbkorgXybyyvte8o%2F6lDxKo7%2FSKF9T9YhU5I15L3phsx%2FuhDlQNbqHuqitsPUNgoILQywW9ehIVN8%2BMBFXarZGaBuYEBCVbnXvRcS%2BDUraZU%2BNSY%2F8d35Pn1vCrXRpdduQ2Y3MLtNa%2BkdfvPqhmF04AsDDHf6qPJZbsQzHll3kQ24owad0Oj6YmBlJ7UVmaj6kKKFskTpCOCvn2%2FwRvLkPr07Dl73bf1EDL%2BT%2BiqA%2BGwHaF6qKiT%2Bm%2FvZXXHFrEwE1R0Ldgehw3L0kZnjVV2VB0%2FxOYh%2BJZMq5tR02N26M55%2BZtKiBYtVe2w6Nw0nyYh2qllX8SnM3KfktSEl4PHWRKNGFQN5%2FNsTvanN4sz%2B04okDVzJEJcaxTwcSc%2Bvc5AzChRWGPSWQfOykjgA%2FOXZbrXKU9Mfrl4ksg6xQuQrrE4jNk4PD%2FJJyahP7EqJSKEtQ4RTHIJdgoUoD3%2BsVVUrofeGvANOZC0bpOp0gTNEgfW0UaHMMSSxs8GOqUBm1xQSnerwQtoqlvY6l61SFIvR9MdqH5FNbN3drWjxFxWBzcw%2F00aGyS9es9XhT4NZXBk8J3%2Bn7zglO6pxnCkLdWM8XB9XbFCy4i656ihgHzwjKyGkW1We2QlFiI2w5hAWBXnnaBqUf8pf%2FblmAvWiZuRQ3J1SMOPU8ijsgBvpzdYO0rUmF5%2FNpfFhwvdKTj2SN%2BJA39lpPi450l5Aw4UGj%2FHQUFP&X-Amz-Signature=94ad776dd64ce8cf72f6819c60d2addfc0a41b15c574fee952fd23c77ad488c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJEEZ37U%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQDi50i5v4TVOAfg4OqEgJ7JM1BeU9KITwhPBJ30nEZDNgIge0frpy3%2BU1oqx6NOkbqHoa1YqdRrXxbGaebbULVxLAgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMdOE%2FNIlOUzgFp%2FgCrcA%2BARJQWkaGTSmGpkuGyX927fqf1zO2nwhG0XAE8dvKOs0s%2FT%2Bf%2BUSlfNrZuUnAZNcxHo%2BzJh7fdbHs52LnHJrgevHoyCFOa7%2FtWrTAHvx6SmiCnhC4TALskJ3x4CZg%2BNs%2FxIi9cPrwobGbkorgXybyyvte8o%2F6lDxKo7%2FSKF9T9YhU5I15L3phsx%2FuhDlQNbqHuqitsPUNgoILQywW9ehIVN8%2BMBFXarZGaBuYEBCVbnXvRcS%2BDUraZU%2BNSY%2F8d35Pn1vCrXRpdduQ2Y3MLtNa%2BkdfvPqhmF04AsDDHf6qPJZbsQzHll3kQ24owad0Oj6YmBlJ7UVmaj6kKKFskTpCOCvn2%2FwRvLkPr07Dl73bf1EDL%2BT%2BiqA%2BGwHaF6qKiT%2Bm%2FvZXXHFrEwE1R0Ldgehw3L0kZnjVV2VB0%2FxOYh%2BJZMq5tR02N26M55%2BZtKiBYtVe2w6Nw0nyYh2qllX8SnM3KfktSEl4PHWRKNGFQN5%2FNsTvanN4sz%2B04okDVzJEJcaxTwcSc%2Bvc5AzChRWGPSWQfOykjgA%2FOXZbrXKU9Mfrl4ksg6xQuQrrE4jNk4PD%2FJJyahP7EqJSKEtQ4RTHIJdgoUoD3%2BsVVUrofeGvANOZC0bpOp0gTNEgfW0UaHMMSSxs8GOqUBm1xQSnerwQtoqlvY6l61SFIvR9MdqH5FNbN3drWjxFxWBzcw%2F00aGyS9es9XhT4NZXBk8J3%2Bn7zglO6pxnCkLdWM8XB9XbFCy4i656ihgHzwjKyGkW1We2QlFiI2w5hAWBXnnaBqUf8pf%2FblmAvWiZuRQ3J1SMOPU8ijsgBvpzdYO0rUmF5%2FNpfFhwvdKTj2SN%2BJA39lpPi450l5Aw4UGj%2FHQUFP&X-Amz-Signature=ffe4fa56122273684effb5181ab6cbc0994bc6129694e3106d38bcad3421f6c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

