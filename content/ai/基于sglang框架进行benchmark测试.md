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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZES3FIVE%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd0LWfpR2Pw%2F5tPUd%2Fz8OlQ7yoyytSajCx1fZRITKG9wIhAPy7GghNxWaztlHqfuHzcmv1d3yB8dm61dVXOl7q9GeJKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzED71sO5GjVhgkW%2BAq3AO9RnFiqky18vubh4tqtRUgitaDHtRJs%2BWCTulNQq5Xj3uQzLQz5hh%2F9btaGUSHTJP81NVn9KWU3D%2FERXYolQRpkwxtdVVww5K1C%2F0Sp7T33w%2FhXXpq4QPFr4w4sIFsCrxV2rI6xk0kn9PnwBQe6gIGus0dDe69FpTlbmANeJtr975oa%2Bx8IcHuKBRXXtaUVklKH7ROA3Q%2FBUGWiELUYHj8dvvC4HxMaGpRT%2BS6bVwaPZB%2BcDkFCt6kY0%2BdigEHO%2FG9BaBUCQSGep2bsK5rQ%2FHfa9xbTpUEjbsdixNn%2FLJOjsv8c2iZwlgtBMXl5OPeNFsTDehpOqj2iWX4NwpVtDF9U%2FNWbxpKIcALxgg7%2BO3%2Fk%2B6NPIn4edy3KeJQ%2FYkKHLmQctCPqO7I7GpwWIj8jOxyjMJ0HBxF8yQG4kgr49whdIC4%2FDlgf9W67JC9y45XjhRxw6rVDKEf%2ByFTK89HJf8p3RR3qk5CGOGcpfI8jwKw47YG3hEYreFr2q5CSEulB5MM%2FXkBOxVQ4J6%2B6Yt8IiMpwfREvan%2BHq%2FNHqXjVgum%2B1tWhhZyXjelGxHaatsk7A6bU9yrc2pJvyA4IWNubHc%2BCxooQ2iaLHJhboZHLbGIy7%2FMEOfWlzmtXO%2BquDDJlZ7NBjqkAf6feRbu%2FUt6lnG9wD84okFW7A95N3wEGSThahg7PCsl4hiQDaNIQ0Tgj6hzQZarlqAN60vZ5gmOyx4svq5OP29Z9OsHcH5b8Q8nB4Si5RHdFKXZRnCPUijqm6NtwcV59y4QSyojsH5qSe9c4N20GNZIJHQokQVYmFfVEn2KR3nnLn6Le5N4rP2gzYGlPG5ACJ7G8qbjl4T8aOBwtIpffvRnpsXg&X-Amz-Signature=8b0cb95254d0be859f30dbe3b0f32245d4533e7778e5802d7bed67a909269f6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZES3FIVE%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDd0LWfpR2Pw%2F5tPUd%2Fz8OlQ7yoyytSajCx1fZRITKG9wIhAPy7GghNxWaztlHqfuHzcmv1d3yB8dm61dVXOl7q9GeJKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzED71sO5GjVhgkW%2BAq3AO9RnFiqky18vubh4tqtRUgitaDHtRJs%2BWCTulNQq5Xj3uQzLQz5hh%2F9btaGUSHTJP81NVn9KWU3D%2FERXYolQRpkwxtdVVww5K1C%2F0Sp7T33w%2FhXXpq4QPFr4w4sIFsCrxV2rI6xk0kn9PnwBQe6gIGus0dDe69FpTlbmANeJtr975oa%2Bx8IcHuKBRXXtaUVklKH7ROA3Q%2FBUGWiELUYHj8dvvC4HxMaGpRT%2BS6bVwaPZB%2BcDkFCt6kY0%2BdigEHO%2FG9BaBUCQSGep2bsK5rQ%2FHfa9xbTpUEjbsdixNn%2FLJOjsv8c2iZwlgtBMXl5OPeNFsTDehpOqj2iWX4NwpVtDF9U%2FNWbxpKIcALxgg7%2BO3%2Fk%2B6NPIn4edy3KeJQ%2FYkKHLmQctCPqO7I7GpwWIj8jOxyjMJ0HBxF8yQG4kgr49whdIC4%2FDlgf9W67JC9y45XjhRxw6rVDKEf%2ByFTK89HJf8p3RR3qk5CGOGcpfI8jwKw47YG3hEYreFr2q5CSEulB5MM%2FXkBOxVQ4J6%2B6Yt8IiMpwfREvan%2BHq%2FNHqXjVgum%2B1tWhhZyXjelGxHaatsk7A6bU9yrc2pJvyA4IWNubHc%2BCxooQ2iaLHJhboZHLbGIy7%2FMEOfWlzmtXO%2BquDDJlZ7NBjqkAf6feRbu%2FUt6lnG9wD84okFW7A95N3wEGSThahg7PCsl4hiQDaNIQ0Tgj6hzQZarlqAN60vZ5gmOyx4svq5OP29Z9OsHcH5b8Q8nB4Si5RHdFKXZRnCPUijqm6NtwcV59y4QSyojsH5qSe9c4N20GNZIJHQokQVYmFfVEn2KR3nnLn6Le5N4rP2gzYGlPG5ACJ7G8qbjl4T8aOBwtIpffvRnpsXg&X-Amz-Signature=869a35b5500556f1cc3d386cbc247c19158e36bcedaad764da449fde59a095b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

