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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLIGIABE%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQCkcxy44j89tz9kbFHPJCdRm9TowEHLz0R94%2FQLC1mNzQIhAIE8DZaHFxs8fmbmL3mzq4DH9HuNdS6EfBIKg495ZN4vKv8DCBsQABoMNjM3NDIzMTgzODA1Igx6mU0mrxXRIfnhVwkq3ANpdaVWChhvtvJyJHp%2F1cuKvyE0mDXS4nTfdURp%2F6wwl3zT8r%2Bld1xRZIDWe7T3PRtw3akcPO24%2BDAWDbqS2OQFchr5Q7TOohl6rAisi%2F84Z0TEcyfCh9K0JUHuDEJUqFIG20mS2BANSDS25kZtRkgkgC50w92mcMuX%2BPiMdggqHWjuRjFERfHabkUrqThIxQKQ4H618AGpI85cnXuIj4sxfg%2FuOZO3J73uqTNYxWYwLpPfp%2FZu2Amg0eSj322SkqS9HqBz8j%2F9IWLvs34rX5OWp2TbexsrDaD374zUD68AdoSkuO9nXHGFsCLMGBVGX6g%2Fw2SBDUAs%2Ffp066ZqFeuYju6NegvrUlQ%2B8HjsI5JhEfRGwXjnVaMUC4bOGLbGRDN2UJvRe09IqRJWJ7mcCvviMvfeiRU0OdEOS8FXqyqB3%2FH02ccCyCN2VZIhHv3CZmdBjJD4JaAJMhKV1KmEKeST04YRIfxineLDjzJF0AHRRKb8hzJXwNXRD%2FPGN1eFb%2B7oiwyt0wSCt8axtoWWazo8vwSDJPuuXFJkxR9hhbymRE%2BJdMXrpbvJ4jwlsnCxBMUCBM1q69%2F%2FNZyBk%2BBPdYGIrQfWUcYcnyZLAkqhry6Ky%2BfEYnp7EcOe5Xc5pTC5oYTJBjqkAX7xR6Iz9T86deShiVTJ0P5Kx4Yyv0YqFaTekT2%2BVDoHqMNQsTW9pPhfoPusnGXIXjbra5Y2Wwo9ovWgT89kNjRoeYSwgKrrYUvXnMV1BqARTqdK73Y5OCFfnnF%2BT0zZQsFALvUrzfPxDAxMlMEpHEIIIkKe5iwuyWJ1nzwak4LFhcQYxyqsEFNDRS4blZtTit2hVECewlIWB5eShWaAt8onQruz&X-Amz-Signature=a862073eaa7c220aa9a089899d3c4df10468e632bfd8c4248dc34a7c631dfdbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLIGIABE%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJIMEYCIQCkcxy44j89tz9kbFHPJCdRm9TowEHLz0R94%2FQLC1mNzQIhAIE8DZaHFxs8fmbmL3mzq4DH9HuNdS6EfBIKg495ZN4vKv8DCBsQABoMNjM3NDIzMTgzODA1Igx6mU0mrxXRIfnhVwkq3ANpdaVWChhvtvJyJHp%2F1cuKvyE0mDXS4nTfdURp%2F6wwl3zT8r%2Bld1xRZIDWe7T3PRtw3akcPO24%2BDAWDbqS2OQFchr5Q7TOohl6rAisi%2F84Z0TEcyfCh9K0JUHuDEJUqFIG20mS2BANSDS25kZtRkgkgC50w92mcMuX%2BPiMdggqHWjuRjFERfHabkUrqThIxQKQ4H618AGpI85cnXuIj4sxfg%2FuOZO3J73uqTNYxWYwLpPfp%2FZu2Amg0eSj322SkqS9HqBz8j%2F9IWLvs34rX5OWp2TbexsrDaD374zUD68AdoSkuO9nXHGFsCLMGBVGX6g%2Fw2SBDUAs%2Ffp066ZqFeuYju6NegvrUlQ%2B8HjsI5JhEfRGwXjnVaMUC4bOGLbGRDN2UJvRe09IqRJWJ7mcCvviMvfeiRU0OdEOS8FXqyqB3%2FH02ccCyCN2VZIhHv3CZmdBjJD4JaAJMhKV1KmEKeST04YRIfxineLDjzJF0AHRRKb8hzJXwNXRD%2FPGN1eFb%2B7oiwyt0wSCt8axtoWWazo8vwSDJPuuXFJkxR9hhbymRE%2BJdMXrpbvJ4jwlsnCxBMUCBM1q69%2F%2FNZyBk%2BBPdYGIrQfWUcYcnyZLAkqhry6Ky%2BfEYnp7EcOe5Xc5pTC5oYTJBjqkAX7xR6Iz9T86deShiVTJ0P5Kx4Yyv0YqFaTekT2%2BVDoHqMNQsTW9pPhfoPusnGXIXjbra5Y2Wwo9ovWgT89kNjRoeYSwgKrrYUvXnMV1BqARTqdK73Y5OCFfnnF%2BT0zZQsFALvUrzfPxDAxMlMEpHEIIIkKe5iwuyWJ1nzwak4LFhcQYxyqsEFNDRS4blZtTit2hVECewlIWB5eShWaAt8onQruz&X-Amz-Signature=a1158b206d18481a55d68708e4249994f6452321e4ee5980423b4b70a0fcb9a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

