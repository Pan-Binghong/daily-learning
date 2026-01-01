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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MHZ3ZQ6%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIFkqNVOLMvR7qOJvxdjNci%2BoC9tE6jhhd12qIwPNuubsAiANl8sl8m0K45knJ9QK4SaDweQnLd3fX4tGEmKf31LkliqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvh92%2BDwrTOhEEtp8KtwDlQw%2FEJdQgTovlkltIJ5dOxCvlr3tVBSEJHtcBTNMtv4LUQtMaUd46Lv%2BcDywYz26O7ULL%2FqhspnlCBZRfpbUT1s0tSHdLSstN%2FvXQrX%2FRaN597%2FfYI6d%2BIx%2F88kxx5cxetER5asOpBGeLVwpIopsnUU3haKoVUmK5TXXpevTfO%2FVrQ3dOqQ%2FHGTkRbsuH2iBxcmgHHC5b7hbmEorleLG5tBKXDsSLZ3fl%2Fimia11kr2leDT0blhTygtpNfLJTQPZcOm5aICpNRP9ZEs1yVDz8DCrIeq1N7uIS2AiSlECd5DXAHyGsT8ZTvTibzIabCXWAQ5TVnlQ9kL1jtLR37cgYgD%2Bw7GleY9nV%2BSBnIapWnmaH6FW1qt64KHxGgneMB%2BDj7lHART0IyPungi3NpQFeGRMKHmP73hZIojdW2tOPD2Z6JldE1IE%2F%2Bo5Z%2Bume6IFzwnhYRb6jrHplWaIGDxO2aN83EGqwdwF5uLVmSUHjgBKOU5qNW6BkiR%2BJGxuYdXGtywIcE51nJRHppGe%2ForuqrD8%2FGZY%2F1ZM8Kmv6MS9OTmZxoy2jRmg1S6WBPNy9cbA%2BRpB6JDKsna4ZV4QVBmrhQreeUwEKrmyWDn3B5ML9Iq2UkMCN3VPzOTH0r0wxaPXygY6pgH5RojqkgEG0%2BFgaveZyv3jCL6wnyNJjaXPbhJLLeL9mwAJGe%2BaqovjDyEkqqvm3mjnMmo3Wvfnfi%2Fk9geDkemhhmE5psLCDvBa3f1IAo7ZVXB9p%2FfntSHaPLochbwN1zQSZz15LBKfgb5Scxvpjsjh6AkL1LL4PYszuljmL9ML06l6KjA927c%2BCiAMi7ir%2FwZQTPEJLe14HQ2kDEMdrxdRqPsdcZUn&X-Amz-Signature=05d5100a6057d453f47673e3274062d0e7f852adbac8c8c2e082380c507aa246&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MHZ3ZQ6%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIFkqNVOLMvR7qOJvxdjNci%2BoC9tE6jhhd12qIwPNuubsAiANl8sl8m0K45knJ9QK4SaDweQnLd3fX4tGEmKf31LkliqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvh92%2BDwrTOhEEtp8KtwDlQw%2FEJdQgTovlkltIJ5dOxCvlr3tVBSEJHtcBTNMtv4LUQtMaUd46Lv%2BcDywYz26O7ULL%2FqhspnlCBZRfpbUT1s0tSHdLSstN%2FvXQrX%2FRaN597%2FfYI6d%2BIx%2F88kxx5cxetER5asOpBGeLVwpIopsnUU3haKoVUmK5TXXpevTfO%2FVrQ3dOqQ%2FHGTkRbsuH2iBxcmgHHC5b7hbmEorleLG5tBKXDsSLZ3fl%2Fimia11kr2leDT0blhTygtpNfLJTQPZcOm5aICpNRP9ZEs1yVDz8DCrIeq1N7uIS2AiSlECd5DXAHyGsT8ZTvTibzIabCXWAQ5TVnlQ9kL1jtLR37cgYgD%2Bw7GleY9nV%2BSBnIapWnmaH6FW1qt64KHxGgneMB%2BDj7lHART0IyPungi3NpQFeGRMKHmP73hZIojdW2tOPD2Z6JldE1IE%2F%2Bo5Z%2Bume6IFzwnhYRb6jrHplWaIGDxO2aN83EGqwdwF5uLVmSUHjgBKOU5qNW6BkiR%2BJGxuYdXGtywIcE51nJRHppGe%2ForuqrD8%2FGZY%2F1ZM8Kmv6MS9OTmZxoy2jRmg1S6WBPNy9cbA%2BRpB6JDKsna4ZV4QVBmrhQreeUwEKrmyWDn3B5ML9Iq2UkMCN3VPzOTH0r0wxaPXygY6pgH5RojqkgEG0%2BFgaveZyv3jCL6wnyNJjaXPbhJLLeL9mwAJGe%2BaqovjDyEkqqvm3mjnMmo3Wvfnfi%2Fk9geDkemhhmE5psLCDvBa3f1IAo7ZVXB9p%2FfntSHaPLochbwN1zQSZz15LBKfgb5Scxvpjsjh6AkL1LL4PYszuljmL9ML06l6KjA927c%2BCiAMi7ir%2FwZQTPEJLe14HQ2kDEMdrxdRqPsdcZUn&X-Amz-Signature=cbed1636492b4cda1305891983d5f6c643b44f8ad1b5b995769c33adcfc035bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

