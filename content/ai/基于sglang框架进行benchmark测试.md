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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWSZBHIL%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCHjHk9I7zxWmaYU07lxtOFk3qhoXo0k%2BaB%2FcHcWQoijQIgUrs3d7bJ297Gwa3rELRwQoxGKaqIptEw0nYtY%2BCtLa0q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDPHEPMBi1kB0uZNj4SrcAzyzAjFnQrwTpi0DtNxRHwrRHFr8qlH3GD3hQK4jrgt8678xH3el1t9cy854UUOJ0j6D9steWqf2T6bb1ZB8mTdIL4DuD3wn1arhLWE5Kg%2F8J6V9vSlSmf0EoFipTk6Siqym%2F3b6tacdEV%2FxtzYp2%2FsMg857%2BCm%2FgF%2FXHOAPy7sdG9EINb6S0fSIkUAXUGNuw%2FOoU74yNVC3Pak%2BKa1wCB8%2BHEfsORybve7JfEyWSYlLeUqSGk21%2BxSKpsNogpTH4sZGMVRL7wq7rljlF2Q9Dh6WjHoCgX%2FLO853DpRzxEDCnNCFCTEGn6KgZeDAthEmvBd%2BbHLXKKgqdjM4EaKoqVS5XCxewuRQLurtt2J9a%2BXoXjEkQI7iUbMqNUAJ2vNYEQXYeH3AWtGKDo2bjZ%2Fr3pPTAUf4cAf80XY3lFR1SbXjnGK7Lds%2FmO6TFD7Bta3aON%2BlQLVBWJaNxp9YhB4JtP43MOifOrc2z9bMmx9%2BBGgKOmwz2n7yy87RBL4uns1HUt9NWZ05SuPR8%2F3ZdNSoSq4faGbXSLEXOU%2BSKn4WVf3DkitfEiyqU8FWPYigA4YWMxzRnQT2gwiL0TtHANvKKhz6%2BTr2%2Frc4N2oGE3ttwiuGeqO1ayiWljFnMZTvMJuz3M4GOqUBXMsyrwDl%2F1xbH7lbikze%2BxnLDfeubbi9PyoHgW3MGY2%2FpkO4yhRc2POPom%2BTpfIz7OcypBlDYre1%2Bl4JE5RanvyqxoNjLvz440R8ZWpTsYzWWdAJgNoFIgQtk6xoDDzDE4sPMZp9YI5zNITdnENV57SGxDFvmmF9rPv9zrt1aMsgJx5sEzeUZgpt506b2vr2%2FvuB5hjhq2cLZakpSnmO5FIu29pI&X-Amz-Signature=f01407be8579041c430b3df0deb6ade95a63eaff898b6f94382762ee4fb3ba88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWSZBHIL%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCHjHk9I7zxWmaYU07lxtOFk3qhoXo0k%2BaB%2FcHcWQoijQIgUrs3d7bJ297Gwa3rELRwQoxGKaqIptEw0nYtY%2BCtLa0q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDPHEPMBi1kB0uZNj4SrcAzyzAjFnQrwTpi0DtNxRHwrRHFr8qlH3GD3hQK4jrgt8678xH3el1t9cy854UUOJ0j6D9steWqf2T6bb1ZB8mTdIL4DuD3wn1arhLWE5Kg%2F8J6V9vSlSmf0EoFipTk6Siqym%2F3b6tacdEV%2FxtzYp2%2FsMg857%2BCm%2FgF%2FXHOAPy7sdG9EINb6S0fSIkUAXUGNuw%2FOoU74yNVC3Pak%2BKa1wCB8%2BHEfsORybve7JfEyWSYlLeUqSGk21%2BxSKpsNogpTH4sZGMVRL7wq7rljlF2Q9Dh6WjHoCgX%2FLO853DpRzxEDCnNCFCTEGn6KgZeDAthEmvBd%2BbHLXKKgqdjM4EaKoqVS5XCxewuRQLurtt2J9a%2BXoXjEkQI7iUbMqNUAJ2vNYEQXYeH3AWtGKDo2bjZ%2Fr3pPTAUf4cAf80XY3lFR1SbXjnGK7Lds%2FmO6TFD7Bta3aON%2BlQLVBWJaNxp9YhB4JtP43MOifOrc2z9bMmx9%2BBGgKOmwz2n7yy87RBL4uns1HUt9NWZ05SuPR8%2F3ZdNSoSq4faGbXSLEXOU%2BSKn4WVf3DkitfEiyqU8FWPYigA4YWMxzRnQT2gwiL0TtHANvKKhz6%2BTr2%2Frc4N2oGE3ttwiuGeqO1ayiWljFnMZTvMJuz3M4GOqUBXMsyrwDl%2F1xbH7lbikze%2BxnLDfeubbi9PyoHgW3MGY2%2FpkO4yhRc2POPom%2BTpfIz7OcypBlDYre1%2Bl4JE5RanvyqxoNjLvz440R8ZWpTsYzWWdAJgNoFIgQtk6xoDDzDE4sPMZp9YI5zNITdnENV57SGxDFvmmF9rPv9zrt1aMsgJx5sEzeUZgpt506b2vr2%2FvuB5hjhq2cLZakpSnmO5FIu29pI&X-Amz-Signature=0133c5733117f8c9d089b14e273dfc0aa8a801f7105c1db8949ca3af7487fbeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

