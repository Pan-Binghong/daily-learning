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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTNCRAL%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDj3F%2B5D97CVQelHQvdntYaITO4jlMF8iB%2BeDUfnxLd0AiAyIlwLwKTgliYokTEJ1vAFWwKT1cTVuFhYNXAdlHdE8SqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLLrEEbALbFZHN2VkKtwDmD3v%2B%2BmG3bkeCjty3ZnTKjZ2Gl4qBn%2FMtaOctPptqupfwm7bb9oCOG%2FMRuIlVtLH5%2B8PsDa%2Bs7To8%2BVv03PiEmL%2FujtFhydP%2FQ%2BRcPtUCBZiLpvaIg7eeQBBl2A1VWbKoiPGnSk2xUV4LaEZyyqBxCa8vjAQbUIURPbflE6nZy7pQCdyShYO3hBTFXQHrqdnh4SbRmlnFD67wujd2%2FdJ2QFedU%2FFZYIudBR863NPNWIhJcN%2BpfG5nwEoVkKYKkcwVXpmrzKlHQdxbVb%2B0Wcos1BhlEEUFyhIIuNfvJZb3zsvnhf4x74mpj20%2BpZWXJKYyybrA9T4yVuOx7TJn%2BM0%2BpeYh96DtqDGFFv4DUbOeZr3cSY6XXvJRiSOmdiCzl%2BmORLgok1rMqk9D5QEDMmWdv8mpueUmFQ7%2BvBH83CGP7NTAxdfb7Rmi5%2FB78ALRawVWkWHq7dtH9uoKMxuBp50mG5OeWML5IqkiNpBguokY%2FzxDjpGgi%2BgzvC1XKET3txbRv72R5pq8fETDI%2FvulzP9BFmYmwH3hnFBSuh7R5uuvEbcuEEEdqRiv1%2Bk26ZOE0rSSQVzXZn2pSsOfZ2Dbbzoz4YtpidVB8xvC6qkqO4sTOHIT983zOh5pOS8NUwyvGvyAY6pgHJFK8rzXQzAzSS%2Fm61ACfI7bx5B08chkDRMHLGY3ZFQFvR734aTDy%2Bfb%2FQG1K8JODzTxjq%2FAQrgtHymJg2g0%2BlqFkga2rUr%2BTytwodSFKBNLjEF5v24nfhdx4dEKJaiZ6xtfWmSCybXHAFHcrsvPVLLKqpsPeVo%2BpN6%2BB5Tk5i%2FBh9ZG0mvDzcEKtgfNp3c72cQ4PSY31dkaLIAA4vabSVQoiia1aH&X-Amz-Signature=26aeaaba0d780924fd90128feebc81c490f4deda8d93272e828c72f3401632cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSTNCRAL%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDj3F%2B5D97CVQelHQvdntYaITO4jlMF8iB%2BeDUfnxLd0AiAyIlwLwKTgliYokTEJ1vAFWwKT1cTVuFhYNXAdlHdE8SqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLLrEEbALbFZHN2VkKtwDmD3v%2B%2BmG3bkeCjty3ZnTKjZ2Gl4qBn%2FMtaOctPptqupfwm7bb9oCOG%2FMRuIlVtLH5%2B8PsDa%2Bs7To8%2BVv03PiEmL%2FujtFhydP%2FQ%2BRcPtUCBZiLpvaIg7eeQBBl2A1VWbKoiPGnSk2xUV4LaEZyyqBxCa8vjAQbUIURPbflE6nZy7pQCdyShYO3hBTFXQHrqdnh4SbRmlnFD67wujd2%2FdJ2QFedU%2FFZYIudBR863NPNWIhJcN%2BpfG5nwEoVkKYKkcwVXpmrzKlHQdxbVb%2B0Wcos1BhlEEUFyhIIuNfvJZb3zsvnhf4x74mpj20%2BpZWXJKYyybrA9T4yVuOx7TJn%2BM0%2BpeYh96DtqDGFFv4DUbOeZr3cSY6XXvJRiSOmdiCzl%2BmORLgok1rMqk9D5QEDMmWdv8mpueUmFQ7%2BvBH83CGP7NTAxdfb7Rmi5%2FB78ALRawVWkWHq7dtH9uoKMxuBp50mG5OeWML5IqkiNpBguokY%2FzxDjpGgi%2BgzvC1XKET3txbRv72R5pq8fETDI%2FvulzP9BFmYmwH3hnFBSuh7R5uuvEbcuEEEdqRiv1%2Bk26ZOE0rSSQVzXZn2pSsOfZ2Dbbzoz4YtpidVB8xvC6qkqO4sTOHIT983zOh5pOS8NUwyvGvyAY6pgHJFK8rzXQzAzSS%2Fm61ACfI7bx5B08chkDRMHLGY3ZFQFvR734aTDy%2Bfb%2FQG1K8JODzTxjq%2FAQrgtHymJg2g0%2BlqFkga2rUr%2BTytwodSFKBNLjEF5v24nfhdx4dEKJaiZ6xtfWmSCybXHAFHcrsvPVLLKqpsPeVo%2BpN6%2BB5Tk5i%2FBh9ZG0mvDzcEKtgfNp3c72cQ4PSY31dkaLIAA4vabSVQoiia1aH&X-Amz-Signature=a8e3c78b15643e3e89fab63f1d5cc0bd13e453a66741150b0eb0628987676b85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

