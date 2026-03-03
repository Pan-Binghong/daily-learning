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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CSTSLS6%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBwXGzRahsh04kFO4JCfjywrhvGtlYMd1MhV63AoCE2gAiEAzaVSvyXXV6Pt2n0u%2B63oy7LcX5%2F0MXbIQKP7GcLbbqQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOxTrsw2YrCWISez%2ByrcA0%2B3uSLqr8uAn4W0F19DQiQZxdccK2WEAiqcWYIjr08GcsEtjoUNaLpFrC3dkcyOr1ECTRX96AoreEdZjUj69ACjscz5sLKwiGVdY2qUckccNkTeQ6Ikvr32TIkSPDuAPmk2w3c6iYeQMX%2FdRXBz0uf%2BBcFST3wilNiDxlEdSxkqaZvPRS8qr2EJjhj7vH0Fa9b9Ba840UOgSWfNKNIZMeQW3h2G0%2FDf3br0nowBefkeIgRdLW6WMYQEnqmTPiRjpMAh5MkrCN0Rp1Vov%2BjFTkldO3aboOEX8mWz6Q3xv3Qt509kUzd%2FZVCMNDkH1GfTSFpK1UzEGRdcwJ4nZuM5YMSQfizUr5LznQQWBL7qoy1LiUJOfi%2FrdcA78WpZETX01x65PA%2BtD2nrRcJd%2FCn8%2BSfF1jjR6swgXvJsOTxZiT4Sm25RI%2FWLlriSCeBLQZYZXOn1b0Be0HLvcpMjCUpkanIkXyFU5CgoEkPsPVITWztpCifzV6nqEfAln8MVFzh9Uw0T2mhvnffUj1o7bNSWmTeGB8gjdmKPw14biTXK8%2B0TiuZUDaSc9GfEszjPco6%2BsqiuzGI%2BHGKq6Jhu5q0Atzp6hTXcFHkT9sea9RH1dafQukTh1xjznQrtiACXMLi2mM0GOqUBaKXsrncyF8J6Q%2FH5VPB%2BvlJ16%2F%2FhBMR07JAfpgiDWUmRSdjyWRQpMPu22Rflikfp70wdiWWlwieX7UwO7AeHAmYmwzt4Yedcsaet03RhsWmfo2dy4rcDlJzh03ZhDhlkJWxfGZpiXf1%2B8nyV5iNIdMFM82FsPfJegQJNAl1PcaBUku8XhcHk2zaVV8rcuk3rZIKdCQuUFk%2BDEGcTgseI1IHKyeUs&X-Amz-Signature=085e29c31aedbbf7cd58c449a63af7203eb7a64a1dd0220d3024f606b7a6b733&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CSTSLS6%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBwXGzRahsh04kFO4JCfjywrhvGtlYMd1MhV63AoCE2gAiEAzaVSvyXXV6Pt2n0u%2B63oy7LcX5%2F0MXbIQKP7GcLbbqQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOxTrsw2YrCWISez%2ByrcA0%2B3uSLqr8uAn4W0F19DQiQZxdccK2WEAiqcWYIjr08GcsEtjoUNaLpFrC3dkcyOr1ECTRX96AoreEdZjUj69ACjscz5sLKwiGVdY2qUckccNkTeQ6Ikvr32TIkSPDuAPmk2w3c6iYeQMX%2FdRXBz0uf%2BBcFST3wilNiDxlEdSxkqaZvPRS8qr2EJjhj7vH0Fa9b9Ba840UOgSWfNKNIZMeQW3h2G0%2FDf3br0nowBefkeIgRdLW6WMYQEnqmTPiRjpMAh5MkrCN0Rp1Vov%2BjFTkldO3aboOEX8mWz6Q3xv3Qt509kUzd%2FZVCMNDkH1GfTSFpK1UzEGRdcwJ4nZuM5YMSQfizUr5LznQQWBL7qoy1LiUJOfi%2FrdcA78WpZETX01x65PA%2BtD2nrRcJd%2FCn8%2BSfF1jjR6swgXvJsOTxZiT4Sm25RI%2FWLlriSCeBLQZYZXOn1b0Be0HLvcpMjCUpkanIkXyFU5CgoEkPsPVITWztpCifzV6nqEfAln8MVFzh9Uw0T2mhvnffUj1o7bNSWmTeGB8gjdmKPw14biTXK8%2B0TiuZUDaSc9GfEszjPco6%2BsqiuzGI%2BHGKq6Jhu5q0Atzp6hTXcFHkT9sea9RH1dafQukTh1xjznQrtiACXMLi2mM0GOqUBaKXsrncyF8J6Q%2FH5VPB%2BvlJ16%2F%2FhBMR07JAfpgiDWUmRSdjyWRQpMPu22Rflikfp70wdiWWlwieX7UwO7AeHAmYmwzt4Yedcsaet03RhsWmfo2dy4rcDlJzh03ZhDhlkJWxfGZpiXf1%2B8nyV5iNIdMFM82FsPfJegQJNAl1PcaBUku8XhcHk2zaVV8rcuk3rZIKdCQuUFk%2BDEGcTgseI1IHKyeUs&X-Amz-Signature=8a66889c9c2dc30e0941f0c5830d631c0584275f38e38b3abd678afcbcd625d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

