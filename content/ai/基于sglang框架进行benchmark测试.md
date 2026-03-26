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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVCT7FV%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdsEXq579u%2Bw5LLxz86qhxx4OBSE7rQ21QHEA5wZN%2FPAiEA1hYRI9tcnVRdf4LrkCKyns21fUYV84Tlivpwb3TK6%2F8qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQciAWxWAMHAIf9SCrcA0tHw5oF2AKNZmYpMe0yp9Y0IAcz2%2F39ep8CIoAHeFiTrr98cb0Kjo5lSO4tCCJh9a5P1jTwm8yjzZsVpNnBjDD634MmEplRKZtX1r8Q4Sib2fNAE%2BuYEvdsvzCxUAPLYikCiLYe4PaB6a8ZQiUu3iPwGjKlfVC6oBsl3YjzxswIlilm4lg1d22VzImC58vAfj6WO0sm6XcWKnfr7wjyBXeo3kndaSCMW7yYBgnROU86s0WlTiHLng8w5ZOzzV0zugcvrf6Q%2FvgaqysKUyNjFPweywaR4m4lJmbwn9Y2ehaR0%2FQEriMWO7c%2FIQjg%2FAu%2FlzmcGgVcMDrOVjgNsk1cFHms9yJ4bVSXYNywKNSl8ihF%2BMKeG9kph6mJZTlhqQGi6wPuthCsy57%2FO8nBEcyLZXYHIDWbvFD5nnoffkDPbKWSN8N1XBg0rVh2uKOPT7d7vuWeQI8LKL%2FyjpeZZl%2Bm9tZhNqK2me5BAkhI5s9%2F4kz%2BMqbykZYe%2BEqBSgFC2ITYU6Xsq6Dx8SjF0p8XhpjVOFXolVTcJKrpydcbbCp4uytBuCBDyhmOUYvjVCF9vuPOeUkeQfUinny5na4%2FZotQ8P9KOtCVi3O9ZIESu%2Fnbw44Dv9h%2BygWxDD8SevemMNXLks4GOqUBWW3Zgtavz%2FtkMLMjdYzIHgxsCNRqvhe8NCPMHjXmViN5fG0uEmSTdfCuWklzoP%2BXurGq7VyLSJVvafJxIbgLBUzBPO0PsAf6vdjnS4wLa4wigE%2Fj6ryO1ocpDQ7vg6iiI%2BpU4KAg8jMp%2FySgdfLfjaDEStO76NJL%2FhmSGs0GSXF2eMcC9NqKxHoKfN9MzRMcT%2FBDNW1k3kb2wTPao4Jxzfm%2BPnSl&X-Amz-Signature=958d027fc23132a14afbbe649ec222978a72f7611661919d26118f53d70e36b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVCT7FV%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdsEXq579u%2Bw5LLxz86qhxx4OBSE7rQ21QHEA5wZN%2FPAiEA1hYRI9tcnVRdf4LrkCKyns21fUYV84Tlivpwb3TK6%2F8qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQciAWxWAMHAIf9SCrcA0tHw5oF2AKNZmYpMe0yp9Y0IAcz2%2F39ep8CIoAHeFiTrr98cb0Kjo5lSO4tCCJh9a5P1jTwm8yjzZsVpNnBjDD634MmEplRKZtX1r8Q4Sib2fNAE%2BuYEvdsvzCxUAPLYikCiLYe4PaB6a8ZQiUu3iPwGjKlfVC6oBsl3YjzxswIlilm4lg1d22VzImC58vAfj6WO0sm6XcWKnfr7wjyBXeo3kndaSCMW7yYBgnROU86s0WlTiHLng8w5ZOzzV0zugcvrf6Q%2FvgaqysKUyNjFPweywaR4m4lJmbwn9Y2ehaR0%2FQEriMWO7c%2FIQjg%2FAu%2FlzmcGgVcMDrOVjgNsk1cFHms9yJ4bVSXYNywKNSl8ihF%2BMKeG9kph6mJZTlhqQGi6wPuthCsy57%2FO8nBEcyLZXYHIDWbvFD5nnoffkDPbKWSN8N1XBg0rVh2uKOPT7d7vuWeQI8LKL%2FyjpeZZl%2Bm9tZhNqK2me5BAkhI5s9%2F4kz%2BMqbykZYe%2BEqBSgFC2ITYU6Xsq6Dx8SjF0p8XhpjVOFXolVTcJKrpydcbbCp4uytBuCBDyhmOUYvjVCF9vuPOeUkeQfUinny5na4%2FZotQ8P9KOtCVi3O9ZIESu%2Fnbw44Dv9h%2BygWxDD8SevemMNXLks4GOqUBWW3Zgtavz%2FtkMLMjdYzIHgxsCNRqvhe8NCPMHjXmViN5fG0uEmSTdfCuWklzoP%2BXurGq7VyLSJVvafJxIbgLBUzBPO0PsAf6vdjnS4wLa4wigE%2Fj6ryO1ocpDQ7vg6iiI%2BpU4KAg8jMp%2FySgdfLfjaDEStO76NJL%2FhmSGs0GSXF2eMcC9NqKxHoKfN9MzRMcT%2FBDNW1k3kb2wTPao4Jxzfm%2BPnSl&X-Amz-Signature=911cfa11263cf55a057159b5cf9a2955a67436a86b2c5becf197f30751e59a32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

