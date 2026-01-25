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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FNNZXFS%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDf%2Bf54oxs4j%2FCtK3ac8HPr%2FhtUVybh6tkGLC6LP39jEgIgWENiS268GXpN323fEN27H8YppoCxfAKxu0panJ2%2FCC8q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDKs9smYsYRIH3Lqr6CrcA35IAzRLSswtr8REfgJxCVd59tXAheA1c2rSs7aY0%2Bwjg2zb%2FAIrby6cyD4Tcok%2FoGtw91fDrLUf0SmT3djGU%2Byc0PXcwiLWnxNUqG7JF1skunnVoQPQjDrScJKlY65H2pjV6fnQQvrrE5Tnuho9DivfVPkkDGPb14uYEp1O1fpOPcQGxx2nkjO2xCpRhshYp3x5DtatAt93phrEzmHmT7chbo%2BaMdSow%2BJI%2FHkLDm2IwmG0ChbFWjIteJHNjOhyqSIjz13R3KEQmmqaKLQmZu2NsHdxAsKITG%2BzUXCotWx45ldpARD39cI8dAWy7ElEuWPpfv6DChbJnhcp4YlxtNGzuAxiW7z%2BGbOlRM0KOPSeqM2Go70AaS05pfgvBUGozMhHbHqmdrPoWbtJMJoQB%2Fc6ZsM6HbBj71nprlQvEYVxMEKW9wVKMB4af3qcof%2BsO8GqgTWtPePmBOYEcGx%2FJQSVnv79tOaUOXfb%2BY2eBY0onQmlaeKASjmI1%2FHr7893rPqWXmTByzFdhh2Cq8ykFaXCHDSSyl71GgNiLQkwOz%2FrNydhVCA1zanbW%2FDinNWK11Vf9TTRGT%2FiImsy4P1OCzVvJD1U5PQ7hSbrzYQqqEVvZWG%2Fd8XfeXHObeDxMOOF1ssGOqUBvngBq8RrS%2Fn5J%2BopNuhigHpm1A9ryEnESItd40C3NppYFJjURhd6VbhDxutmm1eLXFtDWAQikmTvu1ZvY10kZOqNSc1Osbu%2BPQghnaUbudQHE8ZAUsu8K2gJw1CgViStPzVU3%2FL2%2Ftzjh1jyMx3cDpJm1H8Z9Cnew8VRtSyqdNY0MOytOcmhOqcsB0xEkPSItcmb0dxSr1kivPlcla%2BKDzJ05bsq&X-Amz-Signature=95995fb22503601d2b643ec6ddd9508bcbfe9b3010d3165d816ce05e675acdd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FNNZXFS%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDf%2Bf54oxs4j%2FCtK3ac8HPr%2FhtUVybh6tkGLC6LP39jEgIgWENiS268GXpN323fEN27H8YppoCxfAKxu0panJ2%2FCC8q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDKs9smYsYRIH3Lqr6CrcA35IAzRLSswtr8REfgJxCVd59tXAheA1c2rSs7aY0%2Bwjg2zb%2FAIrby6cyD4Tcok%2FoGtw91fDrLUf0SmT3djGU%2Byc0PXcwiLWnxNUqG7JF1skunnVoQPQjDrScJKlY65H2pjV6fnQQvrrE5Tnuho9DivfVPkkDGPb14uYEp1O1fpOPcQGxx2nkjO2xCpRhshYp3x5DtatAt93phrEzmHmT7chbo%2BaMdSow%2BJI%2FHkLDm2IwmG0ChbFWjIteJHNjOhyqSIjz13R3KEQmmqaKLQmZu2NsHdxAsKITG%2BzUXCotWx45ldpARD39cI8dAWy7ElEuWPpfv6DChbJnhcp4YlxtNGzuAxiW7z%2BGbOlRM0KOPSeqM2Go70AaS05pfgvBUGozMhHbHqmdrPoWbtJMJoQB%2Fc6ZsM6HbBj71nprlQvEYVxMEKW9wVKMB4af3qcof%2BsO8GqgTWtPePmBOYEcGx%2FJQSVnv79tOaUOXfb%2BY2eBY0onQmlaeKASjmI1%2FHr7893rPqWXmTByzFdhh2Cq8ykFaXCHDSSyl71GgNiLQkwOz%2FrNydhVCA1zanbW%2FDinNWK11Vf9TTRGT%2FiImsy4P1OCzVvJD1U5PQ7hSbrzYQqqEVvZWG%2Fd8XfeXHObeDxMOOF1ssGOqUBvngBq8RrS%2Fn5J%2BopNuhigHpm1A9ryEnESItd40C3NppYFJjURhd6VbhDxutmm1eLXFtDWAQikmTvu1ZvY10kZOqNSc1Osbu%2BPQghnaUbudQHE8ZAUsu8K2gJw1CgViStPzVU3%2FL2%2Ftzjh1jyMx3cDpJm1H8Z9Cnew8VRtSyqdNY0MOytOcmhOqcsB0xEkPSItcmb0dxSr1kivPlcla%2BKDzJ05bsq&X-Amz-Signature=3c77951cb92bfc09d7a5aae15a0baffe2d74d4cd45b41ee7178c8c219ed05c55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

