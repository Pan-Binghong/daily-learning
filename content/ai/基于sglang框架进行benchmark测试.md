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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5DIQKUU%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXo1uwDoSXBChf2pmSHRwI0Cr2kElnIUJjwiKE4a0vLAiEA%2FFhQPQrLvENItx6jYe%2Fk2b7NjRvZggoKbV%2FBgH0BLiAq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDF3bZGRe11RFN1twbCrcA4rVigKBI9QX%2FRRJye8W11xyC9HG9GIKGvQ0eUCKLd83oDW7DvUfPcvyUPGI8h4pPsb3LHw6efQ7qdaydN5BFkWPEi31Z4dAYK29E9Q7isLg1f8PgLTwESNNyIAOJEua2JO9Y40y8dbxnzFSPwOm20PjyQmDvJ23d%2FOgE7GflJ6%2FXU37mRyozEq72DJXYBRtg%2BdB3Qry5yEzpuNpSxDKwnPNSV%2B8nQ7gJdfkfJqg9oYT6DqY91SnVjHD5zWWh8SoLO98ZfKEW0o%2BOFLklqrGnnTiIfYxpos9tsoWNjOS4jnvxnPqT7ZSEbOATplfN1LgoJrN8Y5e78%2B%2FyLww%2BFua%2BlGBiLGNS7PDNfabhfZbvKQMbx3qlPBSNzToc8B51qKIld7xNiqdu6M660tNUZZB8Uive3NsuHa%2BIY8hZIZ5gc759fJ6dcjQmw%2BMgD0zq191Ld0hGImBSk%2F%2BiZ9BDc5gKFxxmd2dyn3VAT6MgWeWCQsDHULxB38wm9biQfXYjiHJvDfZ9tOKVdJOpvhFdS40b%2BxdNRL6wXJ2fYG2CVDIRq4CMuscCP7fK0MVH1MWlF%2FfLFw3FirR5%2FrZnrk6UD0qzJAzOaFoimdcHI6sGk6LnIlQIdFhQlqkV%2BliLEunMIGi68sGOqUBsAO6qDoZ7oJA%2FIktUil8orpC23wb4SqaDfZExhmxkFvYa0uQpbm7ya3MPiJ3Nkehf6CiMxRdFmRpVaqyaW%2F0x1HplDJBxpNB3UT4mJ8A%2Fg9Wy3lhkgYyxbl54%2FvXiV4rKJ6F%2BEj%2BWe%2B%2F2Wr0UqlxLd1cHzdQ8JXZAad5QyNgRzxxY2tMRiIKxrT%2B31XbNO0GpCJzmN%2FIWHsvtkz89Nqs4vlu6Kur&X-Amz-Signature=eff16394f8d4511d67c6a9f0c6bf943e96d0b479c0fe45c49bf49279a70c1f25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5DIQKUU%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXo1uwDoSXBChf2pmSHRwI0Cr2kElnIUJjwiKE4a0vLAiEA%2FFhQPQrLvENItx6jYe%2Fk2b7NjRvZggoKbV%2FBgH0BLiAq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDF3bZGRe11RFN1twbCrcA4rVigKBI9QX%2FRRJye8W11xyC9HG9GIKGvQ0eUCKLd83oDW7DvUfPcvyUPGI8h4pPsb3LHw6efQ7qdaydN5BFkWPEi31Z4dAYK29E9Q7isLg1f8PgLTwESNNyIAOJEua2JO9Y40y8dbxnzFSPwOm20PjyQmDvJ23d%2FOgE7GflJ6%2FXU37mRyozEq72DJXYBRtg%2BdB3Qry5yEzpuNpSxDKwnPNSV%2B8nQ7gJdfkfJqg9oYT6DqY91SnVjHD5zWWh8SoLO98ZfKEW0o%2BOFLklqrGnnTiIfYxpos9tsoWNjOS4jnvxnPqT7ZSEbOATplfN1LgoJrN8Y5e78%2B%2FyLww%2BFua%2BlGBiLGNS7PDNfabhfZbvKQMbx3qlPBSNzToc8B51qKIld7xNiqdu6M660tNUZZB8Uive3NsuHa%2BIY8hZIZ5gc759fJ6dcjQmw%2BMgD0zq191Ld0hGImBSk%2F%2BiZ9BDc5gKFxxmd2dyn3VAT6MgWeWCQsDHULxB38wm9biQfXYjiHJvDfZ9tOKVdJOpvhFdS40b%2BxdNRL6wXJ2fYG2CVDIRq4CMuscCP7fK0MVH1MWlF%2FfLFw3FirR5%2FrZnrk6UD0qzJAzOaFoimdcHI6sGk6LnIlQIdFhQlqkV%2BliLEunMIGi68sGOqUBsAO6qDoZ7oJA%2FIktUil8orpC23wb4SqaDfZExhmxkFvYa0uQpbm7ya3MPiJ3Nkehf6CiMxRdFmRpVaqyaW%2F0x1HplDJBxpNB3UT4mJ8A%2Fg9Wy3lhkgYyxbl54%2FvXiV4rKJ6F%2BEj%2BWe%2B%2F2Wr0UqlxLd1cHzdQ8JXZAad5QyNgRzxxY2tMRiIKxrT%2B31XbNO0GpCJzmN%2FIWHsvtkz89Nqs4vlu6Kur&X-Amz-Signature=6749db063c4f892e034b09f1ff0d9bed905c4d085f54f990480f7f18377d1c78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

