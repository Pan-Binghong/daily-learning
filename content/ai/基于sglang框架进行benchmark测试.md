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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIOZTZ5W%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKwVIndgT%2FN0B4cm%2FoyWJEqqmeBW%2B6AaS2VI8z4t9uwAiEApjBS6hzHRFOb%2BPz6qa3V8o3iwdLEwqvo%2FLVJNRXqrkIqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJopojedelUN%2FRxaQircA6e89mbe5AUaGc79jXlnHE7S3mZFvrJAZRWYQKXdiKiwoZ9AePWDicFaDJnmWnrRvnDnb%2B5h0DbZbDiLwAvohza1HldKocAbT4WuRwI0n1yJ1SP0uQf8q8ioDNwYKEXsJM64%2B%2FZ5Kqf1dEc1i3DX0A3ghdZ4huhU0uMechaK8%2F%2BkpLewXU3stE8h2EOfuSlAYYEQbL%2FO0vdWBQZyuT5SaHAFWWLQGBsk3umw1o97MCE1VobRBOh1U%2F%2Fo%2FCNkaLZ5pef4GjEvOoRwABCvM6T7DgFguVe1KQTShyTAFnckWIufwKlGNfhqhYLVks3eG4OIV6T8iQ6FsYEak9%2FTN0%2FLs4hN9M%2BjzAZFeqtwLxRD3ZfSbvPVOROk0pvl6%2BmW5kiNesZR5JT%2FjKkKt0NrOHeJ90aFxpiIyRG%2FRTu4R2lTKe7yuiQkvT5d2ejjHTkm%2FmD8R3LVpiUAGhEAmt5PRkWoK7d37L9Hu7TuhJh08zDNDef7nL0cT80YvbMYJ9pUn1sWjcxq0OIrxmSK1Cf5dYoHE5hg7L3Y%2FvDFmYommchgcrFNW%2FmrsLGnUDyNCXi0tMny8ylpgnBiV3xNU0ZIdqID422UtFazo0%2FBknHgNvWSlv%2BkT9liIkv6Hs9PxUsFMPDiksoGOqUBoX%2Ft22A%2FKzqPNnqxrcE%2FIPpr%2F3LBe7Xkovi2HNG72xlVuqDuqPlm1voqXYepNjRcvZYJPABdB8DOEq8fNCtb%2FcqWfy0NJiVfMSaUBqhQaE61aBYusiSOT6YcMoQJQZo0IOMeN6iGgezsbm9Co2aXvXclu4x61oPIvJfjoplQruXRO4PivYF584mZlgq78SV%2BMNoUWnmEvr94EwoYM85%2F7EtswTlQ&X-Amz-Signature=659c1dc58afb14d4e2a21eb3684cf1f623af91b3166044d2ca2550e9966d16dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIOZTZ5W%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKwVIndgT%2FN0B4cm%2FoyWJEqqmeBW%2B6AaS2VI8z4t9uwAiEApjBS6hzHRFOb%2BPz6qa3V8o3iwdLEwqvo%2FLVJNRXqrkIqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJopojedelUN%2FRxaQircA6e89mbe5AUaGc79jXlnHE7S3mZFvrJAZRWYQKXdiKiwoZ9AePWDicFaDJnmWnrRvnDnb%2B5h0DbZbDiLwAvohza1HldKocAbT4WuRwI0n1yJ1SP0uQf8q8ioDNwYKEXsJM64%2B%2FZ5Kqf1dEc1i3DX0A3ghdZ4huhU0uMechaK8%2F%2BkpLewXU3stE8h2EOfuSlAYYEQbL%2FO0vdWBQZyuT5SaHAFWWLQGBsk3umw1o97MCE1VobRBOh1U%2F%2Fo%2FCNkaLZ5pef4GjEvOoRwABCvM6T7DgFguVe1KQTShyTAFnckWIufwKlGNfhqhYLVks3eG4OIV6T8iQ6FsYEak9%2FTN0%2FLs4hN9M%2BjzAZFeqtwLxRD3ZfSbvPVOROk0pvl6%2BmW5kiNesZR5JT%2FjKkKt0NrOHeJ90aFxpiIyRG%2FRTu4R2lTKe7yuiQkvT5d2ejjHTkm%2FmD8R3LVpiUAGhEAmt5PRkWoK7d37L9Hu7TuhJh08zDNDef7nL0cT80YvbMYJ9pUn1sWjcxq0OIrxmSK1Cf5dYoHE5hg7L3Y%2FvDFmYommchgcrFNW%2FmrsLGnUDyNCXi0tMny8ylpgnBiV3xNU0ZIdqID422UtFazo0%2FBknHgNvWSlv%2BkT9liIkv6Hs9PxUsFMPDiksoGOqUBoX%2Ft22A%2FKzqPNnqxrcE%2FIPpr%2F3LBe7Xkovi2HNG72xlVuqDuqPlm1voqXYepNjRcvZYJPABdB8DOEq8fNCtb%2FcqWfy0NJiVfMSaUBqhQaE61aBYusiSOT6YcMoQJQZo0IOMeN6iGgezsbm9Co2aXvXclu4x61oPIvJfjoplQruXRO4PivYF584mZlgq78SV%2BMNoUWnmEvr94EwoYM85%2F7EtswTlQ&X-Amz-Signature=50c6dad8ee8d98d0dce1cd08bb7f39257b9dd3a66c94ce12f2fb9f3e5349ce67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

