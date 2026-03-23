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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466762WQAY6%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3sjWtk8JpaJoa6KEPdvnsR5rKEtK2Q2ymw%2F67RoZMawIhAKaB4sokhrZXlN4%2BHIm58CGTi6%2BeE%2FfXd4t%2BhBypywSmKv8DCHQQABoMNjM3NDIzMTgzODA1Igzp5se2Dpwuj7%2FiCAsq3APzIa099Kxc26dg7bB%2BBTgRnefUyijmHirjeVB7NvMp8Y%2Bss8HFRAeREiHEiGgjbQ90DC8OWB4CWzPIQl%2FoyPLQfsNMJRuIjLN%2BGGvPR24oH1k5GFwhpBrcyz5mZUzam211Rnyo104o%2BR3HhIgbS%2BtFuZVpWgYGMY60A%2BjtpF%2FNSI7huCYlxcQGdFstL9FeeVsLTKR1HcRBpj1zNjx7nhfwVUmn4IvbHE84Dli3KtmmMC2PxraVWiWMpe9l9%2FH7J0cWEtVCjMmaGDLQ4XemYYPhQtenGFB5TSR%2BMB3%2FGVUP7NwHXuP8WFMLt%2BMBN2GhqGZQTTpvPcVB62BgGAO62NiQZZTyFQCcatDJziep4nz3yu%2B7M7eAom%2FBdSVXtjRCbO1L71BWx8f%2B%2FJYi042wbQ%2BnyeTHYptVxpuiQjtSb48gwmaW57YNfNV%2FSn35EbXEVyLz3JwTSbOhYMCedWWis8VpH1H9h5ODXRN6NSyaM1WfuDHSPLmQtww4xz9jd9Chk%2BZozO8JJaDNbviEC%2BPo0SKgLWVu5hv3W3Y0lo5wz6qf6rwr2022xvsOyqyj2LltUcUYXB2Cys0xH0b57%2Bs8wkrhSSNtznrk7mBHNzYy0inT4wss%2Fpdj%2FdvtipT1sjCf5YLOBjqkAde0Dyl6B%2BQR0%2BkLE6aDimDXrV0VSxFf1EWH8sjTs0L%2FNCOeCmMBpxgs7%2FU4UzgrtZXerhnynq1Ql1ExiOyCM%2FbGl9vTBwwOcJseWoYwN2QC0sIbQE3NjdTDJ7hN%2BdATyk4lvzEBSm9sS2StYBzDjmMiYJSxHNJGNUrweCAE92vKqWD7eqy34jkGVl5ONPIGSpm8XwoF2feheAymYd6WLCwyBIdP&X-Amz-Signature=e506a1249ad14805bff1c4daba4a8eb5f10003e087baeb9bf7a0cdaca8901526&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466762WQAY6%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3sjWtk8JpaJoa6KEPdvnsR5rKEtK2Q2ymw%2F67RoZMawIhAKaB4sokhrZXlN4%2BHIm58CGTi6%2BeE%2FfXd4t%2BhBypywSmKv8DCHQQABoMNjM3NDIzMTgzODA1Igzp5se2Dpwuj7%2FiCAsq3APzIa099Kxc26dg7bB%2BBTgRnefUyijmHirjeVB7NvMp8Y%2Bss8HFRAeREiHEiGgjbQ90DC8OWB4CWzPIQl%2FoyPLQfsNMJRuIjLN%2BGGvPR24oH1k5GFwhpBrcyz5mZUzam211Rnyo104o%2BR3HhIgbS%2BtFuZVpWgYGMY60A%2BjtpF%2FNSI7huCYlxcQGdFstL9FeeVsLTKR1HcRBpj1zNjx7nhfwVUmn4IvbHE84Dli3KtmmMC2PxraVWiWMpe9l9%2FH7J0cWEtVCjMmaGDLQ4XemYYPhQtenGFB5TSR%2BMB3%2FGVUP7NwHXuP8WFMLt%2BMBN2GhqGZQTTpvPcVB62BgGAO62NiQZZTyFQCcatDJziep4nz3yu%2B7M7eAom%2FBdSVXtjRCbO1L71BWx8f%2B%2FJYi042wbQ%2BnyeTHYptVxpuiQjtSb48gwmaW57YNfNV%2FSn35EbXEVyLz3JwTSbOhYMCedWWis8VpH1H9h5ODXRN6NSyaM1WfuDHSPLmQtww4xz9jd9Chk%2BZozO8JJaDNbviEC%2BPo0SKgLWVu5hv3W3Y0lo5wz6qf6rwr2022xvsOyqyj2LltUcUYXB2Cys0xH0b57%2Bs8wkrhSSNtznrk7mBHNzYy0inT4wss%2Fpdj%2FdvtipT1sjCf5YLOBjqkAde0Dyl6B%2BQR0%2BkLE6aDimDXrV0VSxFf1EWH8sjTs0L%2FNCOeCmMBpxgs7%2FU4UzgrtZXerhnynq1Ql1ExiOyCM%2FbGl9vTBwwOcJseWoYwN2QC0sIbQE3NjdTDJ7hN%2BdATyk4lvzEBSm9sS2StYBzDjmMiYJSxHNJGNUrweCAE92vKqWD7eqy34jkGVl5ONPIGSpm8XwoF2feheAymYd6WLCwyBIdP&X-Amz-Signature=921801c5579d671064f565360a4d84f311f923c6b852eb61fb05a0b65d5cbd17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

