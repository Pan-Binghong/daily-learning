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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CDFWKPP%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVG1m6DHBifnOnwF1asw%2BdtnKxHGC9eyvwp2lIBUqs2QIgap3NREm1GS3maD3FEHrbsCjqE8YSrz3HajUHGKH72fkq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDLMhtK5Kg%2BHHKsAh%2FircA1uhDlA1xHLnf7%2BKL2krI9sjiPWA8mfCjGiMg6gGOeIZ65YFfhBKqekvPLbqAtpw4uplUZdfipXVNg8VtIikhv4vzhiLkIBjfQmWCKN%2FHHYx4fU9BPlgvdPG6T9PBcgQHIAqoN666kbBRdDJpMQhKS84AQRiH4raNRcdXGV3W5sPa%2FaWV2bdP8FZnjlN0nibozBOrXQzbB9uLM72YM%2BIJbcL9rMgHYSC0BtMKQG11O%2Fxwkq7l4qy6PzL4B48Q7HoziO24wwQfIN5ybaB3XWc2CrB9HcPK5DJTPZ2r0r9dslC44DNgKSt6ZgVQBLzX%2Bf%2Fc89fL5LUL6L%2BoaXntn4Nfd5sK1Yr0VTpX%2F8fgKTzHIT10vZVtE1doxGNU7fcTAxmDaUhSNbxlv0GfonMRn56RNGOpRyXVyjnEuB64g%2Bn07eZgE07NefpOm2JNq61BskFW0TtZX3wAbxzg9Hbd9lPbNcNXOlgVvTHAjcPJhHROd3rRoVcKQMyJm%2FvH%2BJTxVslmrBMyN762iV5trJnq0uxVH3G0wWjmtBlWAyBYs%2Byi2Ta%2FYyCfhdGQUbzYjnJXoVZiGzlpbM5%2FxklUhGS1mGHPS%2FsabwThKnMK7DvJyQ19q2%2BjWj1f5kEOpSK1SU3MNexmckGOqUBvhzfCAwg%2Bj8ouyBn3VA6XfpDOcLeebWi7Bgf0bIb7%2BrP%2BP6KJ48p002VPxKU1u7GZ5SW1v8sPedTYqgUDBUfn4mdsSJC2mckVEMkE2cQS3DA8J%2FxovsxkpPmBpYg4dfBUUL7BWeq98DCdVUNcxF3m0mtmpdGkwUr6tJLA36WWNBNQZjD21dJxDLQrVBV5c%2FZjU8tfX7aWmYki2HJ3Mg677oD5QEE&X-Amz-Signature=503b143445b0de13eb8546ba53599c67700336dcd211471cad051fd686ff6e1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CDFWKPP%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVG1m6DHBifnOnwF1asw%2BdtnKxHGC9eyvwp2lIBUqs2QIgap3NREm1GS3maD3FEHrbsCjqE8YSrz3HajUHGKH72fkq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDLMhtK5Kg%2BHHKsAh%2FircA1uhDlA1xHLnf7%2BKL2krI9sjiPWA8mfCjGiMg6gGOeIZ65YFfhBKqekvPLbqAtpw4uplUZdfipXVNg8VtIikhv4vzhiLkIBjfQmWCKN%2FHHYx4fU9BPlgvdPG6T9PBcgQHIAqoN666kbBRdDJpMQhKS84AQRiH4raNRcdXGV3W5sPa%2FaWV2bdP8FZnjlN0nibozBOrXQzbB9uLM72YM%2BIJbcL9rMgHYSC0BtMKQG11O%2Fxwkq7l4qy6PzL4B48Q7HoziO24wwQfIN5ybaB3XWc2CrB9HcPK5DJTPZ2r0r9dslC44DNgKSt6ZgVQBLzX%2Bf%2Fc89fL5LUL6L%2BoaXntn4Nfd5sK1Yr0VTpX%2F8fgKTzHIT10vZVtE1doxGNU7fcTAxmDaUhSNbxlv0GfonMRn56RNGOpRyXVyjnEuB64g%2Bn07eZgE07NefpOm2JNq61BskFW0TtZX3wAbxzg9Hbd9lPbNcNXOlgVvTHAjcPJhHROd3rRoVcKQMyJm%2FvH%2BJTxVslmrBMyN762iV5trJnq0uxVH3G0wWjmtBlWAyBYs%2Byi2Ta%2FYyCfhdGQUbzYjnJXoVZiGzlpbM5%2FxklUhGS1mGHPS%2FsabwThKnMK7DvJyQ19q2%2BjWj1f5kEOpSK1SU3MNexmckGOqUBvhzfCAwg%2Bj8ouyBn3VA6XfpDOcLeebWi7Bgf0bIb7%2BrP%2BP6KJ48p002VPxKU1u7GZ5SW1v8sPedTYqgUDBUfn4mdsSJC2mckVEMkE2cQS3DA8J%2FxovsxkpPmBpYg4dfBUUL7BWeq98DCdVUNcxF3m0mtmpdGkwUr6tJLA36WWNBNQZjD21dJxDLQrVBV5c%2FZjU8tfX7aWmYki2HJ3Mg677oD5QEE&X-Amz-Signature=5cba9edd5598c1df8cbd5edfbbcaa6cd5b4a7e1483c2e8ec26f26ec2aa78b18b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

