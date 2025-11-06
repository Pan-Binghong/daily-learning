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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJ2UA5N3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDJvTNXjucRDmFm2zPpCdIgYYP0%2Fh8KnrB%2Bz9vVNrUHAiAQFivE%2BgCJKqKDT8NFcPcf8Wh0Zhbb0Mkf3FfQQlCBJiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc6pzTCwgFyAcsCoLKtwDpxybBKNWH6mrngTrpp8APnGrEYt0%2BAnyWoyhYSV6w7WkcWudauhWmyMTSubLvN0af7AEDZ8DIciJkhjwfTgEr5uf0iaO%2FuYef0wCNICV5cV2VfsDlaD1YmgscmtHEJu40q9%2F2U1fm6MCo69D7JOIAjaXlEqymkMllUk2z%2BqBCirMBM%2BlJuA2DLH801%2BqHo4W%2F8TfFqLJHmhTsKdp4IS%2Bx9wNvovVd1cLFP0Q%2F4ozl0e2hx4RRY79vjx7smyUZ9fAga5pO%2Bs1EIc6npclgRXYj%2BVOIvjfj3Hv2ii6hvPTQvd%2FHQbPNxmvUopjSUQ8Mvo%2FluhvkNyeoLmM%2FGTHRMHaHUycvIUkyySK1CGuwtkaQHangkRFiWuM%2BTZIvrMCfx39I1calp04LblyPtYhurlb3AX1Mhlib9TzaCp84vx2gcC5M6cyXNkK6ii6FlyhWzXOjaHlRhTGaZH1%2FoiBw4vj3NrmTkGRetOdNOu7dkCC3OuBqktURPocyn7oAX%2FchNiR8Td%2FDMGwm0ka4HHCg6KFgofMUysrVp5aBM2YiYvLaoNpVgwsAG%2ByzIHwOJivcK%2FYWYWcjlzV2lni%2BCpK0ppMPez9NsGdHxC1jv5eoSAK7Rcq%2Bhfd%2F3e5OmoiFlwwpfKvyAY6pgHiD1QMIULB0vmT3Ddh3ukHh54qoeWpQycEMETRBy9HIsQWjmH8la2DlBedjpzodS3%2Barh%2F5A12agMG1kO%2BZyxWYenEYfvwwctJrAyT%2B2bp%2F3G9JBnhX%2FxcdN4R5Yf4G9pW3GZ30wYX82e8%2F0%2BtB2svruB8hunV%2BRWVFb1mKbT8yXSuVxHpix9Qp8%2F2xhZkCt7SyWuqdl83pdnSl%2B%2BwgCse0g0L3FCx&X-Amz-Signature=4680f35e6ebfdb6cb6c12c9b445707dcf67ce3aaf4bb2213371dca2006ed73d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJ2UA5N3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFDJvTNXjucRDmFm2zPpCdIgYYP0%2Fh8KnrB%2Bz9vVNrUHAiAQFivE%2BgCJKqKDT8NFcPcf8Wh0Zhbb0Mkf3FfQQlCBJiqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc6pzTCwgFyAcsCoLKtwDpxybBKNWH6mrngTrpp8APnGrEYt0%2BAnyWoyhYSV6w7WkcWudauhWmyMTSubLvN0af7AEDZ8DIciJkhjwfTgEr5uf0iaO%2FuYef0wCNICV5cV2VfsDlaD1YmgscmtHEJu40q9%2F2U1fm6MCo69D7JOIAjaXlEqymkMllUk2z%2BqBCirMBM%2BlJuA2DLH801%2BqHo4W%2F8TfFqLJHmhTsKdp4IS%2Bx9wNvovVd1cLFP0Q%2F4ozl0e2hx4RRY79vjx7smyUZ9fAga5pO%2Bs1EIc6npclgRXYj%2BVOIvjfj3Hv2ii6hvPTQvd%2FHQbPNxmvUopjSUQ8Mvo%2FluhvkNyeoLmM%2FGTHRMHaHUycvIUkyySK1CGuwtkaQHangkRFiWuM%2BTZIvrMCfx39I1calp04LblyPtYhurlb3AX1Mhlib9TzaCp84vx2gcC5M6cyXNkK6ii6FlyhWzXOjaHlRhTGaZH1%2FoiBw4vj3NrmTkGRetOdNOu7dkCC3OuBqktURPocyn7oAX%2FchNiR8Td%2FDMGwm0ka4HHCg6KFgofMUysrVp5aBM2YiYvLaoNpVgwsAG%2ByzIHwOJivcK%2FYWYWcjlzV2lni%2BCpK0ppMPez9NsGdHxC1jv5eoSAK7Rcq%2Bhfd%2F3e5OmoiFlwwpfKvyAY6pgHiD1QMIULB0vmT3Ddh3ukHh54qoeWpQycEMETRBy9HIsQWjmH8la2DlBedjpzodS3%2Barh%2F5A12agMG1kO%2BZyxWYenEYfvwwctJrAyT%2B2bp%2F3G9JBnhX%2FxcdN4R5Yf4G9pW3GZ30wYX82e8%2F0%2BtB2svruB8hunV%2BRWVFb1mKbT8yXSuVxHpix9Qp8%2F2xhZkCt7SyWuqdl83pdnSl%2B%2BwgCse0g0L3FCx&X-Amz-Signature=3b2230e14b9f43aa5de785dacabf7b8111117197cedd6df73ac2a56477afed8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

