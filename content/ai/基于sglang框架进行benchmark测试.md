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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NET2JWR%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRR3F9qI6PJ%2B%2BIn6Z3C8QwR72KvgFW%2FcvIUxn%2F17KMrgIhAMV7vs9XjJQtbQV%2B20QIBTQy9asuMf4qb52VZeQ574pcKv8DCFoQABoMNjM3NDIzMTgzODA1Igy%2F0EiIn0obCg7z9gQq3AOrgJeNwlISiAPQ4F4dhe7Yr2GXGigmU9%2FcMxYiaE2bAwZgFIhd7hFzNdW%2BRUioMoLJ5iBx048j4tnsGY8H29iFRsWa03lJQ4vYs3uQIViEs%2Bt0unzbiORlxrLM2Gql%2B55IEM%2Bjb%2Fyt4DYBUnR68%2BU%2FEja5kCLTCb%2BJdvR4KCvIoY%2BUOEhN%2Bq9p%2FO%2BR%2BYthC4J2tMg9F6ogqy8speqiCdW9Xbt1DcXbtQpG1DTCyoK1RIuT6KTz4PGLku98pm5Q6S9IXIv%2FCmob86DB6SwYD4LNUAxSxGdZr2f9FYM3pRn5JALcdp9w4x7iphp9%2FHw6h7C5kjgqJfgRxyJ4nRlVPJ2GLV%2BZdYiNFy1m%2FzA6q8gY5Jjp%2Ba5IXZdePVL2bvT8CRx47e%2F5W7t5lZT1HWAzULyPuhSZj0Q%2BSmjSAkS%2Bc4CQC%2Fseleu3GJSx3103CSBheCDwU7PWWsFfw6%2FSvMM3%2BAFFUlw2NvpY28Kn%2FjIuoSdAEh25oh86omTX6CK6wfvG48rKQm%2BWF%2BjPwer9XbEz8U81IGuaH47%2BGUcTVhEujrgoSbl3WokEBhU29F5CiCcuAVKQmE8i6O95qbZjVB4lg37bwjW17X2i7DfhtLpFY8%2Bu402E9s4S3xZUsg8%2F%2BDDEoNTMBjqkAUIWM6hQZ9dn%2BDMjgEgcaLMJEMYacpwEjTIYCjsiGLMWFcBOojSDyDLEfSBgCjXwqwmeqlIrNcNrR35hm9tZvwNKceJxQYvc4kfPu13hst7bga4VlmlKa0VP7%2B4RTgnC%2BbHJsFTcwEBVvW%2B3dV4GqTmYP1CcUXAmSepJY%2Ft3QBdyDF%2B5EsTAuEwoY6A3htdolWBW3j68qAnF7OrV2gDONZBXgdYI&X-Amz-Signature=725274563f3830bae871991bca481070c9ab46de2fbba5ed9dcda0e769003968&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NET2JWR%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRR3F9qI6PJ%2B%2BIn6Z3C8QwR72KvgFW%2FcvIUxn%2F17KMrgIhAMV7vs9XjJQtbQV%2B20QIBTQy9asuMf4qb52VZeQ574pcKv8DCFoQABoMNjM3NDIzMTgzODA1Igy%2F0EiIn0obCg7z9gQq3AOrgJeNwlISiAPQ4F4dhe7Yr2GXGigmU9%2FcMxYiaE2bAwZgFIhd7hFzNdW%2BRUioMoLJ5iBx048j4tnsGY8H29iFRsWa03lJQ4vYs3uQIViEs%2Bt0unzbiORlxrLM2Gql%2B55IEM%2Bjb%2Fyt4DYBUnR68%2BU%2FEja5kCLTCb%2BJdvR4KCvIoY%2BUOEhN%2Bq9p%2FO%2BR%2BYthC4J2tMg9F6ogqy8speqiCdW9Xbt1DcXbtQpG1DTCyoK1RIuT6KTz4PGLku98pm5Q6S9IXIv%2FCmob86DB6SwYD4LNUAxSxGdZr2f9FYM3pRn5JALcdp9w4x7iphp9%2FHw6h7C5kjgqJfgRxyJ4nRlVPJ2GLV%2BZdYiNFy1m%2FzA6q8gY5Jjp%2Ba5IXZdePVL2bvT8CRx47e%2F5W7t5lZT1HWAzULyPuhSZj0Q%2BSmjSAkS%2Bc4CQC%2Fseleu3GJSx3103CSBheCDwU7PWWsFfw6%2FSvMM3%2BAFFUlw2NvpY28Kn%2FjIuoSdAEh25oh86omTX6CK6wfvG48rKQm%2BWF%2BjPwer9XbEz8U81IGuaH47%2BGUcTVhEujrgoSbl3WokEBhU29F5CiCcuAVKQmE8i6O95qbZjVB4lg37bwjW17X2i7DfhtLpFY8%2Bu402E9s4S3xZUsg8%2F%2BDDEoNTMBjqkAUIWM6hQZ9dn%2BDMjgEgcaLMJEMYacpwEjTIYCjsiGLMWFcBOojSDyDLEfSBgCjXwqwmeqlIrNcNrR35hm9tZvwNKceJxQYvc4kfPu13hst7bga4VlmlKa0VP7%2B4RTgnC%2BbHJsFTcwEBVvW%2B3dV4GqTmYP1CcUXAmSepJY%2Ft3QBdyDF%2B5EsTAuEwoY6A3htdolWBW3j68qAnF7OrV2gDONZBXgdYI&X-Amz-Signature=9243be10c94a85e59b99dfbf480d939b9b147052743489c6769c54f66ffe5dbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

