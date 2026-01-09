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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KF7TGPM%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk%2FKDSt7cxx%2B0wr10vaUTzoUeqMU0d5QhTPCkLnLXpKAIgQQTjimeHwo%2Fbf3jXU9w7QChHEN90L6G08RASEMyw9sUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiW51jb%2F6BfOcsOjyrcA9m%2BbsSZXicnL2R0s8jlmuIjsOklYw2H10hNiiJSWxRAwN64j4siN9My6oFd9ZRsn1hmbfXx%2F62%2Fpp8qljqYICgigt7Msxd%2B3htOYPGuEZzl%2B%2FRkJoewTANS8ulVoo7WlcxNrVlDTU07eJlBWtqmhxOsS5sjt2j6kDuS6udh7kymf5y5cPZyw6hYhK1ndSOFDlZBYJX07Ft2AdY0TBsTfpt5Qf0LjKY%2FS0FQhXlURefZ%2Faj4OlwL0e1PByF%2FPZSZq%2BzFBo1MxU2UudUT6%2B8exltD6SUcbeOoTeiT3NcKXcotYgZwFQ0IO8%2F8yrp9tM8jXGTOE6r1tDWzi%2BU4BhT1hzXmihJ%2FHWE%2FdfoUQzQHILiIemqyh9EtR%2Br8G0BNWLOKW8scSDiUClFYV%2FlCInq6hA93hrwvAxkcjp0du7sJBPuBNzM99fKUcFRVPCTdrte8SMaf42W7Ug50FNtJZnkkAblgd%2FPXOIiyUYrc3PN2WEKpd5Ie%2BxmH7bthFU2cT9nT43HoRROQu4OMlh5lLhGm2itpnczIF%2FLadjvzFXFAXKHRgJS6Mz9hszSUdlyl1bBnsqMYSCoLTxlCUuisdV1epz75t2qSbWzLg1RZVFg8sec9wH1ZRpxdliaPUg7vMMjEgcsGOqUBamH5iBz3mKbPrvYrTnslDpb2DJlvG%2BbB5ipTeEWUf6UV9WB5d4gZiNIpMWuXfZ35PAlNEvIrlMaQrVIrnPQE%2FdBDLZHwPnpwZI6RKDbfKblZPxlzVq84%2FEfdI5dE2qIjUtZokocbzRXKuEEG54rjpuC%2FoRIa203at8bfpJTT22Dg6Ljl7mCJ5RrSExxQ84zBoASyQLLwvR9pH6jrDWqLRCiDfS0D&X-Amz-Signature=03ae0102b906d59354b6632165a5b4f0d08805fa5fc8a1091dd724f4179f2a78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KF7TGPM%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk%2FKDSt7cxx%2B0wr10vaUTzoUeqMU0d5QhTPCkLnLXpKAIgQQTjimeHwo%2Fbf3jXU9w7QChHEN90L6G08RASEMyw9sUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAiW51jb%2F6BfOcsOjyrcA9m%2BbsSZXicnL2R0s8jlmuIjsOklYw2H10hNiiJSWxRAwN64j4siN9My6oFd9ZRsn1hmbfXx%2F62%2Fpp8qljqYICgigt7Msxd%2B3htOYPGuEZzl%2B%2FRkJoewTANS8ulVoo7WlcxNrVlDTU07eJlBWtqmhxOsS5sjt2j6kDuS6udh7kymf5y5cPZyw6hYhK1ndSOFDlZBYJX07Ft2AdY0TBsTfpt5Qf0LjKY%2FS0FQhXlURefZ%2Faj4OlwL0e1PByF%2FPZSZq%2BzFBo1MxU2UudUT6%2B8exltD6SUcbeOoTeiT3NcKXcotYgZwFQ0IO8%2F8yrp9tM8jXGTOE6r1tDWzi%2BU4BhT1hzXmihJ%2FHWE%2FdfoUQzQHILiIemqyh9EtR%2Br8G0BNWLOKW8scSDiUClFYV%2FlCInq6hA93hrwvAxkcjp0du7sJBPuBNzM99fKUcFRVPCTdrte8SMaf42W7Ug50FNtJZnkkAblgd%2FPXOIiyUYrc3PN2WEKpd5Ie%2BxmH7bthFU2cT9nT43HoRROQu4OMlh5lLhGm2itpnczIF%2FLadjvzFXFAXKHRgJS6Mz9hszSUdlyl1bBnsqMYSCoLTxlCUuisdV1epz75t2qSbWzLg1RZVFg8sec9wH1ZRpxdliaPUg7vMMjEgcsGOqUBamH5iBz3mKbPrvYrTnslDpb2DJlvG%2BbB5ipTeEWUf6UV9WB5d4gZiNIpMWuXfZ35PAlNEvIrlMaQrVIrnPQE%2FdBDLZHwPnpwZI6RKDbfKblZPxlzVq84%2FEfdI5dE2qIjUtZokocbzRXKuEEG54rjpuC%2FoRIa203at8bfpJTT22Dg6Ljl7mCJ5RrSExxQ84zBoASyQLLwvR9pH6jrDWqLRCiDfS0D&X-Amz-Signature=bf7fe90b658edd5cac9c668d0b847ca751297a23714d0785a825cdfd009062f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

