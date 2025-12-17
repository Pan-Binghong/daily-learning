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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZL6HP5E%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8Gr7ECDtPR%2F1tK%2BHm8ShIwSVxkT8qcMeYJOW0EUBc3AiEAxe2rFd6AN%2Bi2nUGqSMbWtlpADNcNI5QZm6AaCuFCOYUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDBUjdzX6LBEBU9VzbircA1BLVepPWou8%2Bn6WUeonX8DW0owv044i3uoK4hd9rsUQKMYCRXKKygVWRDVOkIuuYSzVwoDi0Bc1oDIotTzlkpAb2ACE2O1VRwvAoksrHhoMg%2BFVsZL%2BEnu5T5DWSg%2Fc5OI2ZtWwiT9TOAISYtDxv9n8zbIzfpKqUZU%2B%2BTrjw1g0ew1M01%2BwTZrNMCNAsUC9LgxGlgThddIYKJtRTmNQb57gH0Hz4cJK%2BHaX59qstquiK8Pg6NVp7RqFkMwx6%2FOFpRvwFBwKFIBq3Z3Tthc7NuatcbTu4dXjKRJ%2F3SIeyqiCFBdyapd7MEgHr5r2M%2F%2BvrW3sYYSawkCLpkXB5WtJSz6cdRP9tj7szpKoD0THxQ5AmmRnIvWfItjwpBllL%2Bmia7%2FPB2anARtPVrxTMDmWC71pdqDpXPNScV%2F9vKFIL9lT45bXnYYZBxpq3JG0IBLJElRQyMcP7Q6ldUAWjqntRlu3BkFWfnAuXnAXUAGRpBdzsX9Z2roOcbTcfPo4inEtneZOGVv6Jpsf%2FDa4tKy9DsimT2%2B7vy4XiaGieejo9nzLXt3lfmMeiC9RTLoUNzYc%2BodZF7cphbyoedOWzaumy01%2Fs67fpQNQN%2FUPKAN%2BULCUBdhO7CtY2a%2Fp65a2MM6yiMoGOqUBRpEaYur1eBr70TlpkPb11n8bmhfg94LLbjf9otrDx2i9WEanuKe%2BCmbuFmh09V%2BHIR0G2cvV5WBVXzbN%2BxHdVF046E38OFtvwraqgY9EzCF7dt4fZWhAsKXPKkQIR2hDLr1XJa6%2FRu3Wtoayn3ta2FrCy%2FRtmPDP5Tzp7O6mG1nnkcJ6cc9cWONfaeAg5SGnrWdQYC0B7HPhyhGYZx%2F6i3BPUOii&X-Amz-Signature=84f213b5b5e0f340daedce3d083ff944b4ebbc0f93bad00767ff47c7905a44e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZL6HP5E%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8Gr7ECDtPR%2F1tK%2BHm8ShIwSVxkT8qcMeYJOW0EUBc3AiEAxe2rFd6AN%2Bi2nUGqSMbWtlpADNcNI5QZm6AaCuFCOYUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDBUjdzX6LBEBU9VzbircA1BLVepPWou8%2Bn6WUeonX8DW0owv044i3uoK4hd9rsUQKMYCRXKKygVWRDVOkIuuYSzVwoDi0Bc1oDIotTzlkpAb2ACE2O1VRwvAoksrHhoMg%2BFVsZL%2BEnu5T5DWSg%2Fc5OI2ZtWwiT9TOAISYtDxv9n8zbIzfpKqUZU%2B%2BTrjw1g0ew1M01%2BwTZrNMCNAsUC9LgxGlgThddIYKJtRTmNQb57gH0Hz4cJK%2BHaX59qstquiK8Pg6NVp7RqFkMwx6%2FOFpRvwFBwKFIBq3Z3Tthc7NuatcbTu4dXjKRJ%2F3SIeyqiCFBdyapd7MEgHr5r2M%2F%2BvrW3sYYSawkCLpkXB5WtJSz6cdRP9tj7szpKoD0THxQ5AmmRnIvWfItjwpBllL%2Bmia7%2FPB2anARtPVrxTMDmWC71pdqDpXPNScV%2F9vKFIL9lT45bXnYYZBxpq3JG0IBLJElRQyMcP7Q6ldUAWjqntRlu3BkFWfnAuXnAXUAGRpBdzsX9Z2roOcbTcfPo4inEtneZOGVv6Jpsf%2FDa4tKy9DsimT2%2B7vy4XiaGieejo9nzLXt3lfmMeiC9RTLoUNzYc%2BodZF7cphbyoedOWzaumy01%2Fs67fpQNQN%2FUPKAN%2BULCUBdhO7CtY2a%2Fp65a2MM6yiMoGOqUBRpEaYur1eBr70TlpkPb11n8bmhfg94LLbjf9otrDx2i9WEanuKe%2BCmbuFmh09V%2BHIR0G2cvV5WBVXzbN%2BxHdVF046E38OFtvwraqgY9EzCF7dt4fZWhAsKXPKkQIR2hDLr1XJa6%2FRu3Wtoayn3ta2FrCy%2FRtmPDP5Tzp7O6mG1nnkcJ6cc9cWONfaeAg5SGnrWdQYC0B7HPhyhGYZx%2F6i3BPUOii&X-Amz-Signature=7b1be1950d8a273325e43f7820d4126f2f8173b556e3d2d10825bab18220bd2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

