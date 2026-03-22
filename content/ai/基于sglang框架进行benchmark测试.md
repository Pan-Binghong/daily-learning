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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CWUYG5P%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH6T%2FzrAytiJU2LT0JtlFQDKGoUUtK%2BfpuygeQpU%2F4QmAiEAor3I1e2E3xMoidRtZs9xou9tEZJiAZ7AtptYS8Fu7ysq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDlk1Zj1bOxPATWOVSrcA3qqFWcPM5a7eNZRi%2Fc8k44fbGUTRmHKkWuDSJQHXgUJWxM6zCpdA3n1%2BENOWNJQJtM8w8YUEYMiMbkrItJAk%2BkuuwurXMQQ%2F8GWCw7lGtUe5brNBj8Xyd%2F9zmF2JxB3HGP7FRCnWel4cUgbEL5XTapeIxpoNotzTHCj6tF5ZlDPG0JgIDkk%2Fw2SIvY6MloreDPJ3MKRA2%2FRydMxn8wSsQX0oono2Jv0w6TeLROERQNRVzcm6lBsxMSD1bzxtJGEqQSDyrHXat9jialMMT3a5cP%2F%2FbSC9RfAF4PyJgn3Osq2bgHl0C59XPooyvVvXiOu1s9ZEkbYNwLaUikADwBiElrm5Y4s8yuqFTCrMhfDPaG240G4ks064tA4e89JWoCUtL%2BX0z0v9SfCKt%2BVA91SoZVCChBiHYGxJOXR5TjNgoxVOV00v95%2BwlGBkVyerlTjkClfwIaYibnHeu6%2BLd4dG0l6jJOE4t99zDbHLkjTgiF90dur%2FNxsuu60vy5OFmO410ETdPgTKPaYsmA5lS0Vw2aoxUBswnaNHPR5PhPZdz1IwGLKoVYnw0KZYs3wlbNFfkMfFlF0nXI%2FVo%2FJt%2BdbQ9ojWo1ThcWEYNZy5whGeGppUT0XCgVqnM6%2FnE9rMJCt%2Fc0GOqUBAIZf6jacGGjEQYYckIlo6uGIf1skZyRXB3voxYFIfWpaih4cXVuC6nucalg5t4CSgHf1H%2FXvZM4HGW1qvSWwPBs1AOtywD7e7%2BG12jiZMszyuYIN4hZaPQKHbBe6faS5kh9wyMyEDfdrUk%2BTqxvsl8rTwCVyNZEjS9KFmk%2BkL0tAdQu1crWpHwUZKlj2QcJqNV5d9o3%2BclXJOJbudCY%2BqYljwKtY&X-Amz-Signature=9f20b40cf6e2e29fc8c69765d9f17e603c245f0580564d4fcf7e8bb003209df0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CWUYG5P%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH6T%2FzrAytiJU2LT0JtlFQDKGoUUtK%2BfpuygeQpU%2F4QmAiEAor3I1e2E3xMoidRtZs9xou9tEZJiAZ7AtptYS8Fu7ysq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDlk1Zj1bOxPATWOVSrcA3qqFWcPM5a7eNZRi%2Fc8k44fbGUTRmHKkWuDSJQHXgUJWxM6zCpdA3n1%2BENOWNJQJtM8w8YUEYMiMbkrItJAk%2BkuuwurXMQQ%2F8GWCw7lGtUe5brNBj8Xyd%2F9zmF2JxB3HGP7FRCnWel4cUgbEL5XTapeIxpoNotzTHCj6tF5ZlDPG0JgIDkk%2Fw2SIvY6MloreDPJ3MKRA2%2FRydMxn8wSsQX0oono2Jv0w6TeLROERQNRVzcm6lBsxMSD1bzxtJGEqQSDyrHXat9jialMMT3a5cP%2F%2FbSC9RfAF4PyJgn3Osq2bgHl0C59XPooyvVvXiOu1s9ZEkbYNwLaUikADwBiElrm5Y4s8yuqFTCrMhfDPaG240G4ks064tA4e89JWoCUtL%2BX0z0v9SfCKt%2BVA91SoZVCChBiHYGxJOXR5TjNgoxVOV00v95%2BwlGBkVyerlTjkClfwIaYibnHeu6%2BLd4dG0l6jJOE4t99zDbHLkjTgiF90dur%2FNxsuu60vy5OFmO410ETdPgTKPaYsmA5lS0Vw2aoxUBswnaNHPR5PhPZdz1IwGLKoVYnw0KZYs3wlbNFfkMfFlF0nXI%2FVo%2FJt%2BdbQ9ojWo1ThcWEYNZy5whGeGppUT0XCgVqnM6%2FnE9rMJCt%2Fc0GOqUBAIZf6jacGGjEQYYckIlo6uGIf1skZyRXB3voxYFIfWpaih4cXVuC6nucalg5t4CSgHf1H%2FXvZM4HGW1qvSWwPBs1AOtywD7e7%2BG12jiZMszyuYIN4hZaPQKHbBe6faS5kh9wyMyEDfdrUk%2BTqxvsl8rTwCVyNZEjS9KFmk%2BkL0tAdQu1crWpHwUZKlj2QcJqNV5d9o3%2BclXJOJbudCY%2BqYljwKtY&X-Amz-Signature=85a96d3bddd9cec29efa3fd751251d3a7981b14a2614d45cfa7ab09482b583af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

