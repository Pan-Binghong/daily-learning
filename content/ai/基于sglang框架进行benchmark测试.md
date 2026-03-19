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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/143320bc-2b56-450b-8b89-4cfa3a20c5e2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WERXK6K%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCeazkaF%2Fei8S97n2DvYWC5wX2aMaLDrD0X19vZkYBbsAIgH8HYLPY9O3g%2FSwGX%2FI3pmLo%2B0d0nw%2FMGR0bOFIPisvoq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDKTSYgKiSu5FKdx%2FHyrcA71YwtmxeocDJrs99zqhkNFwAgajK9VHbtDUKRgmgOu0FGevmf54WmhTU1mxntr97MVsR69zPoYUiCxIrgQnaBVA%2BibzBes7YXiMOylejUUuyNvQf3481E04nKrkGw%2BRgpui5mqAIWfX6UFdKtiq6T9kK%2BsUInzGNo6wOSccjjW%2B05eFOp%2Bq%2B0aDvB%2FIOh7By1%2Fw0ZPpXgQIJBLsSwchLA97vvURfBo6plHnyGD57E0xY1ndKqAMgORKHbcgnwNOXC%2BGlEqwvHrP93OBjSsJcPBbFimVrFGFkibSEzdSmUzzA%2BDJuuB0k02BLQU9OZLvxQTtPAGc3dpZIoRlQbvSidXPeE43EFgpQlutrY706EwT2XhCDL3qDtPsE25NhWECuoqnOj8Cucpi%2FGdi%2BCxm%2FG%2FLbMuOnQmiRkz41ht%2B46y6BXr3rTyPcmOI3VHXdVBy6CyOdKAcMnr2vGAs%2B%2BQNpQdDdAm2xgMKguurTxYqVHOYcBIw4Jw1N4r4y6TD65VJeTiwObuXqtMPvKxXR2QAwc2UYkrjJsgMJJ8%2FdNYw2m%2FrLGLLNo%2FfdNiS83kcNI9iVXAwV7o7C6SUryIdZ7LPYXys%2FYg1ds%2FO1CI%2BJ9GdkIl941NNkjgqO0pD5w9vMKnH7c0GOqUBlBsG56Zfjoq0x1IrdYeyjdXBJr52fGdjyyEX00DQrcbrgYTY1dHNulHznm2r24DbQmsqxWH640aQpIgCfW%2FThAOdbYvOnERHJVerL7LYMxXe%2FvlPhvdP9j3VE8rfcz8j1siRc4AJ6veyuHXK3NeUQwUCp1ChxD67CJDi3XKoYCTyp%2BBDlJka8mudk7UUdxQnWdbB7sL4Sy5xqP8WwqgiXkn2PbPE&X-Amz-Signature=ff166f488cce7d50e2fab8ce1a14f445dfeea94d57aef91055ec462c17fd423f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 路径检查

1. SGLang项目路径：/sgl-workspace/sglang 
1. 模型权重路径：/data/DeepSeek-R1-Distill-Llama-70B
---

# 4. 发布模型服务

```python
python3 -m sglang.launch_server --model-path /data/DeepSeek-R1-Distill-Llama-70B --host 0.0.0.0 --port 30000 --tp-size 4 --enable-p2p-check
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/190ea869-f701-4cc6-b588-27a3855eddb4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WERXK6K%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCeazkaF%2Fei8S97n2DvYWC5wX2aMaLDrD0X19vZkYBbsAIgH8HYLPY9O3g%2FSwGX%2FI3pmLo%2B0d0nw%2FMGR0bOFIPisvoq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDKTSYgKiSu5FKdx%2FHyrcA71YwtmxeocDJrs99zqhkNFwAgajK9VHbtDUKRgmgOu0FGevmf54WmhTU1mxntr97MVsR69zPoYUiCxIrgQnaBVA%2BibzBes7YXiMOylejUUuyNvQf3481E04nKrkGw%2BRgpui5mqAIWfX6UFdKtiq6T9kK%2BsUInzGNo6wOSccjjW%2B05eFOp%2Bq%2B0aDvB%2FIOh7By1%2Fw0ZPpXgQIJBLsSwchLA97vvURfBo6plHnyGD57E0xY1ndKqAMgORKHbcgnwNOXC%2BGlEqwvHrP93OBjSsJcPBbFimVrFGFkibSEzdSmUzzA%2BDJuuB0k02BLQU9OZLvxQTtPAGc3dpZIoRlQbvSidXPeE43EFgpQlutrY706EwT2XhCDL3qDtPsE25NhWECuoqnOj8Cucpi%2FGdi%2BCxm%2FG%2FLbMuOnQmiRkz41ht%2B46y6BXr3rTyPcmOI3VHXdVBy6CyOdKAcMnr2vGAs%2B%2BQNpQdDdAm2xgMKguurTxYqVHOYcBIw4Jw1N4r4y6TD65VJeTiwObuXqtMPvKxXR2QAwc2UYkrjJsgMJJ8%2FdNYw2m%2FrLGLLNo%2FfdNiS83kcNI9iVXAwV7o7C6SUryIdZ7LPYXys%2FYg1ds%2FO1CI%2BJ9GdkIl941NNkjgqO0pD5w9vMKnH7c0GOqUBlBsG56Zfjoq0x1IrdYeyjdXBJr52fGdjyyEX00DQrcbrgYTY1dHNulHznm2r24DbQmsqxWH640aQpIgCfW%2FThAOdbYvOnERHJVerL7LYMxXe%2FvlPhvdP9j3VE8rfcz8j1siRc4AJ6veyuHXK3NeUQwUCp1ChxD67CJDi3XKoYCTyp%2BBDlJka8mudk7UUdxQnWdbB7sL4Sy5xqP8WwqgiXkn2PbPE&X-Amz-Signature=c8e5ebc929cb64af965aeb6f953669410de6a5ba5407d6490e40cec2d2e0c1ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

