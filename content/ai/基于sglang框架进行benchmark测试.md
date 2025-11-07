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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XILBJEOD%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1LUs3vrjfenc6luWgoNhOskWymnxWFcIbqIZ7Hq0SPwIgFqBGRybdm7D6fwGB1vtUNP5xpkcVmTXKrmY4s4fqMoYqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHd%2F3OhwK5yx%2FtqGFircAypTas%2FRBhysbS7KHi3dzlUaOlSBa0X2sAlL0UhY2yep%2BPjHPNI%2B501VejDhTrUM7xZX9bXUTte4om1uGY0sIUcdRCfiLWpS42YQtGUvolg5Dz8Em1vh%2BiCWqm8NdFJHTIPsesCeFfTqc5cf%2FnjjAb%2BRvr2XieHPoOBCSaxHarIwxNzwapoU32kObZch%2B6DfJ%2BK53inrCV8pgET7jaqhhV9M29w9mGWOQMPGM%2B368H1zokk8if4j3Gqknxk%2FG5gjWTJFb10IJ5cz%2Bj9hc3%2FC%2F2Qaz1Gr839jEAqNywoWDrMPzeRGN17fyqQDl3PYhtGk%2FBCuaImdoiXB9twvH%2B0sqyhSiM1r8COeamPLXtpfxRHiKghI%2F62OSGVsI2qcJAJJrOe28Hu3cX5Yb3KIrLGcnnzPgXm3S4WyvpLaSYR9OkRP722zGzoyPcNw7BZxzRbn0w5cufkl41FzOtqtOVQpMYuXdsfCZzIRvfYJUKB%2BBzcEJJRBKz%2FANSA9Tuk6kilz4mbxR1TG39AhRnq%2FTytowIz4LMaIP4x7Z5Bpp%2B8MpNcnvW2gsBxmVb0lM7Pw73A7VVG60Hcc1WV%2B9WuEVf6igBcobMmRNGvTU7M0%2BDqK2kXcIAxU6zLt7zxalkS0MOO0tcgGOqUBWbFL1%2BtZupypP0WxqGIjNe%2FwwXctz5g7%2Flqd7FwrmweAmwNYBazzFSI%2Bk68rA2ArVIyejPIam67grNLac0T%2B3y7SmdKFgqCM1K9djqPSJ8lVT12wmAIEDjTYtgIlGYjp8t8QGmdUUpSa5txtj0VfgzxWENfAjLbLx5sP0roGeBzU%2BxCgxIX54%2BsRHExVsvvqBKBPE29U3SQoVmiFp0EU7hvdSwqY&X-Amz-Signature=c876072a0b306ad10ebd14bd4de1d46ba2f709f391f55f38819213ff28763d62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XILBJEOD%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1LUs3vrjfenc6luWgoNhOskWymnxWFcIbqIZ7Hq0SPwIgFqBGRybdm7D6fwGB1vtUNP5xpkcVmTXKrmY4s4fqMoYqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHd%2F3OhwK5yx%2FtqGFircAypTas%2FRBhysbS7KHi3dzlUaOlSBa0X2sAlL0UhY2yep%2BPjHPNI%2B501VejDhTrUM7xZX9bXUTte4om1uGY0sIUcdRCfiLWpS42YQtGUvolg5Dz8Em1vh%2BiCWqm8NdFJHTIPsesCeFfTqc5cf%2FnjjAb%2BRvr2XieHPoOBCSaxHarIwxNzwapoU32kObZch%2B6DfJ%2BK53inrCV8pgET7jaqhhV9M29w9mGWOQMPGM%2B368H1zokk8if4j3Gqknxk%2FG5gjWTJFb10IJ5cz%2Bj9hc3%2FC%2F2Qaz1Gr839jEAqNywoWDrMPzeRGN17fyqQDl3PYhtGk%2FBCuaImdoiXB9twvH%2B0sqyhSiM1r8COeamPLXtpfxRHiKghI%2F62OSGVsI2qcJAJJrOe28Hu3cX5Yb3KIrLGcnnzPgXm3S4WyvpLaSYR9OkRP722zGzoyPcNw7BZxzRbn0w5cufkl41FzOtqtOVQpMYuXdsfCZzIRvfYJUKB%2BBzcEJJRBKz%2FANSA9Tuk6kilz4mbxR1TG39AhRnq%2FTytowIz4LMaIP4x7Z5Bpp%2B8MpNcnvW2gsBxmVb0lM7Pw73A7VVG60Hcc1WV%2B9WuEVf6igBcobMmRNGvTU7M0%2BDqK2kXcIAxU6zLt7zxalkS0MOO0tcgGOqUBWbFL1%2BtZupypP0WxqGIjNe%2FwwXctz5g7%2Flqd7FwrmweAmwNYBazzFSI%2Bk68rA2ArVIyejPIam67grNLac0T%2B3y7SmdKFgqCM1K9djqPSJ8lVT12wmAIEDjTYtgIlGYjp8t8QGmdUUpSa5txtj0VfgzxWENfAjLbLx5sP0roGeBzU%2BxCgxIX54%2BsRHExVsvvqBKBPE29U3SQoVmiFp0EU7hvdSwqY&X-Amz-Signature=c27064003c3638f5482f85820eb010f40cc32813feafc322897769c65cf666ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

