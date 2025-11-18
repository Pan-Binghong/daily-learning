---
title: Stepvideo-t2v Deployment Manual
date: '2025-04-22T00:43:00.000Z'
lastmod: '2025-04-23T02:58:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 记录部署阶跃星辰发布的stepvideo-ti2v (图片生成视频)模型，全流程。含踩坑记录，以及webui展示代码。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VOYVUXI%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFv5pR1B1mUTXq%2FUjt2y3x9%2BxieTP73HxJjWphFLLOXjAiEApGpSShPDYc2QxnBJr2nmFZwtjk4Rynt4PrA4U%2F9XjJ4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLb6Cl3Zx2LMhTahRircA9TDhf8WuQE4OwrimiOcKxj%2Fb6LGtzME9SFWSd60oWSM6LD%2BwlbKLwoxEjla4D6UM6jb8qpz6VyPPt6dgfnUS8WRwUMG%2FS5aGAZjgDJM7%2FDgS4ddXuvnFG8OHEsn3QcyAoW1101%2ByHWfFDxSJ1tCrsLAh8SIne5Z1y25A7wN7PtWRGCiOjiYgnCggdADuEY7tJu%2FRdFp27BYyJxlf%2BZbI6TBXPxV%2FfjYMr6pz2DO%2B3u1ExovbM73iIx3JXl3ohUp1sjwQZvCEsbj7fYV3xAyWtxCewQrG%2BIv2SNDa1UQVdLw7%2By74ymRmCzPrXtI29EA1XJdUkRxx5ZB4L3m2ZySR0LFkS0kzlhy7lEe5umBb1jBOIWyL5vix8Q4z5VDIxBpdbmmshHf7a0t8O8pVtSDECQbarmifPbD7NrzZB2V50yRHby9kkX4packiUkYcyWvPKnq529%2BtJUzl9Oo6aZeSkfFNHdj3wnCbhj4Fr%2FmSHQFCfLxZL%2FVbteJbgFVYGHppG1dNSbSe9NlK3huZC0%2F5D1v3U10LpEm2IZWXv9sanXiVNHamDJxufZiD7hf6qVdwMLq01gAUH8K8DUD8kLP9sla8gVcMC60rHSnhlZbl%2BVN0jQOnhrK9vkJYiKfMJ6Z78gGOqUBJ%2BOMZC35iHhGF8DTTID3po53kMvpp%2FLrgCGfYLwFj6CkWzM0B5U1SmTXYFlAeKVv%2B0lMxDWFpvi%2F3qhwGTYBUIcgNPZon6%2FnqQ3hX0JRQKF8Ii4FbccZpMKqFHg1SWBZsKY%2FD4kggPJT1NptZgxQGb2QyfytjUfsqV80etuxxF7iip7u9p8dJ3HNPPCYNwAKHNWrsr7Yz5CTNLSsIsJi6xcjL7w3&X-Amz-Signature=505f2362b637ca9da294d4ebbf69ed67e7e0aeb69a411c78329bc56a02feedc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 1. 环境安装

## 1.1 拉取Docker镜像

```bash
docker pull nvcr.io/nvidia/pytorch:23.10-py3
docker run -dit --gpus all --privileged  --ipc=host --net host --name=stepfun--shm-size=100g --ulimit memlock=-1 -v /data/:/data/ 镜像ID  /bin/bash
docker exec -it stepfun /bin/bash
```

推荐拉取该镜像，在此镜像基础上进行模型的安装运行。忽略docker的安装。

## 1.2安装StepVideo环境

演示所用的webui基于streamlit库进行开发，其中的numpy版本与stepvideo有冲突，首先安装streamlit。

```bash
pip install streamlit
```

```bash
git clone https://github.com/stepfun-ai/Step-Video-TI2V.git
cd StepFun-StepVideo
pip install -e .
```

opencv报错：如遇到 xxx 报错，利用opencv-fixer工具进行清理更新

```bash
pip install opencv-fixer==0.2.5
python -c "from opencv_fixer import AutoFix; AutoFix()"
```

<details><summary>requirements.txt</summary>

</details>

---

# 2. 模型下载

```bash
mkdir stepfun
cd stepfun
pip install modelscope
modelscope download --model stepfun-ai/stepvideo-ti2v  --local_dir .
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VOYVUXI%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFv5pR1B1mUTXq%2FUjt2y3x9%2BxieTP73HxJjWphFLLOXjAiEApGpSShPDYc2QxnBJr2nmFZwtjk4Rynt4PrA4U%2F9XjJ4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLb6Cl3Zx2LMhTahRircA9TDhf8WuQE4OwrimiOcKxj%2Fb6LGtzME9SFWSd60oWSM6LD%2BwlbKLwoxEjla4D6UM6jb8qpz6VyPPt6dgfnUS8WRwUMG%2FS5aGAZjgDJM7%2FDgS4ddXuvnFG8OHEsn3QcyAoW1101%2ByHWfFDxSJ1tCrsLAh8SIne5Z1y25A7wN7PtWRGCiOjiYgnCggdADuEY7tJu%2FRdFp27BYyJxlf%2BZbI6TBXPxV%2FfjYMr6pz2DO%2B3u1ExovbM73iIx3JXl3ohUp1sjwQZvCEsbj7fYV3xAyWtxCewQrG%2BIv2SNDa1UQVdLw7%2By74ymRmCzPrXtI29EA1XJdUkRxx5ZB4L3m2ZySR0LFkS0kzlhy7lEe5umBb1jBOIWyL5vix8Q4z5VDIxBpdbmmshHf7a0t8O8pVtSDECQbarmifPbD7NrzZB2V50yRHby9kkX4packiUkYcyWvPKnq529%2BtJUzl9Oo6aZeSkfFNHdj3wnCbhj4Fr%2FmSHQFCfLxZL%2FVbteJbgFVYGHppG1dNSbSe9NlK3huZC0%2F5D1v3U10LpEm2IZWXv9sanXiVNHamDJxufZiD7hf6qVdwMLq01gAUH8K8DUD8kLP9sla8gVcMC60rHSnhlZbl%2BVN0jQOnhrK9vkJYiKfMJ6Z78gGOqUBJ%2BOMZC35iHhGF8DTTID3po53kMvpp%2FLrgCGfYLwFj6CkWzM0B5U1SmTXYFlAeKVv%2B0lMxDWFpvi%2F3qhwGTYBUIcgNPZon6%2FnqQ3hX0JRQKF8Ii4FbccZpMKqFHg1SWBZsKY%2FD4kggPJT1NptZgxQGb2QyfytjUfsqV80etuxxF7iip7u9p8dJ3HNPPCYNwAKHNWrsr7Yz5CTNLSsIsJi6xcjL7w3&X-Amz-Signature=33825e7d3e144462146f4217b265a0c625aa350f514532e18cceacc5b45989e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 3. 推理脚本

## 3.1 启动API服务

```bash
python api/call_remote_server.py --model_dir /data/stepfun & 
```

运行此操作后，可观察到服务器内的最后一张卡，有大约45%的显存占用。

## 3.2 图生视频

> 💡 本次测试环境在H800 * 8的裸金属服务器内，目前模型存在显存过大的问题。如果使用H20（单卡显存141G），可取消标红的配置参数。

```bash
# 优化显存使用，减少碎片
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

```bash
torchrun --nproc_per_node 4 run_parallel.py \
    --model_dir /data/stepfun \ ## 权重路劲
    --vae_url '127.0.0.1' \ ## 第4步运行成功后显示的url
    --caption_url '127.0.0.1' \ ## 第4步运行成功后显示的url
    --ulysses_degree  4 \ ## 4卡运行
    --prompt "男孩快速长大" \ 
    --first_image_path ./assets/demo.png \ ## 图片路径
    --infer_steps 50 \ ## 视频降噪参数
    --save_path ./results \ ## 生成视频保存路径
    --cfg_scale 9.0 \ ## 内置提示词关联度参数，详见config.py
    --motion_score 5.0 \ ## 帧间变化参数
    --time_shift 12.573 \ ## 降噪相关参数
    --use-cpu-offload ## 使用内存加载权重
```

---

# 4. WebUI推理

## 4.1 代码

### 将以下代码放入StepFun-StepVideo文件夹内

---

## 4.2 运行服务

streamlit run webui.py —server.port 8080

---

## 4.3 页面效果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VOYVUXI%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFv5pR1B1mUTXq%2FUjt2y3x9%2BxieTP73HxJjWphFLLOXjAiEApGpSShPDYc2QxnBJr2nmFZwtjk4Rynt4PrA4U%2F9XjJ4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLb6Cl3Zx2LMhTahRircA9TDhf8WuQE4OwrimiOcKxj%2Fb6LGtzME9SFWSd60oWSM6LD%2BwlbKLwoxEjla4D6UM6jb8qpz6VyPPt6dgfnUS8WRwUMG%2FS5aGAZjgDJM7%2FDgS4ddXuvnFG8OHEsn3QcyAoW1101%2ByHWfFDxSJ1tCrsLAh8SIne5Z1y25A7wN7PtWRGCiOjiYgnCggdADuEY7tJu%2FRdFp27BYyJxlf%2BZbI6TBXPxV%2FfjYMr6pz2DO%2B3u1ExovbM73iIx3JXl3ohUp1sjwQZvCEsbj7fYV3xAyWtxCewQrG%2BIv2SNDa1UQVdLw7%2By74ymRmCzPrXtI29EA1XJdUkRxx5ZB4L3m2ZySR0LFkS0kzlhy7lEe5umBb1jBOIWyL5vix8Q4z5VDIxBpdbmmshHf7a0t8O8pVtSDECQbarmifPbD7NrzZB2V50yRHby9kkX4packiUkYcyWvPKnq529%2BtJUzl9Oo6aZeSkfFNHdj3wnCbhj4Fr%2FmSHQFCfLxZL%2FVbteJbgFVYGHppG1dNSbSe9NlK3huZC0%2F5D1v3U10LpEm2IZWXv9sanXiVNHamDJxufZiD7hf6qVdwMLq01gAUH8K8DUD8kLP9sla8gVcMC60rHSnhlZbl%2BVN0jQOnhrK9vkJYiKfMJ6Z78gGOqUBJ%2BOMZC35iHhGF8DTTID3po53kMvpp%2FLrgCGfYLwFj6CkWzM0B5U1SmTXYFlAeKVv%2B0lMxDWFpvi%2F3qhwGTYBUIcgNPZon6%2FnqQ3hX0JRQKF8Ii4FbccZpMKqFHg1SWBZsKY%2FD4kggPJT1NptZgxQGb2QyfytjUfsqV80etuxxF7iip7u9p8dJ3HNPPCYNwAKHNWrsr7Yz5CTNLSsIsJi6xcjL7w3&X-Amz-Signature=6b24c43d5d0780d7c129fb0a6f3ba504aca6b87da4ec2ab71c6f2c30021134e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VOYVUXI%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFv5pR1B1mUTXq%2FUjt2y3x9%2BxieTP73HxJjWphFLLOXjAiEApGpSShPDYc2QxnBJr2nmFZwtjk4Rynt4PrA4U%2F9XjJ4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLb6Cl3Zx2LMhTahRircA9TDhf8WuQE4OwrimiOcKxj%2Fb6LGtzME9SFWSd60oWSM6LD%2BwlbKLwoxEjla4D6UM6jb8qpz6VyPPt6dgfnUS8WRwUMG%2FS5aGAZjgDJM7%2FDgS4ddXuvnFG8OHEsn3QcyAoW1101%2ByHWfFDxSJ1tCrsLAh8SIne5Z1y25A7wN7PtWRGCiOjiYgnCggdADuEY7tJu%2FRdFp27BYyJxlf%2BZbI6TBXPxV%2FfjYMr6pz2DO%2B3u1ExovbM73iIx3JXl3ohUp1sjwQZvCEsbj7fYV3xAyWtxCewQrG%2BIv2SNDa1UQVdLw7%2By74ymRmCzPrXtI29EA1XJdUkRxx5ZB4L3m2ZySR0LFkS0kzlhy7lEe5umBb1jBOIWyL5vix8Q4z5VDIxBpdbmmshHf7a0t8O8pVtSDECQbarmifPbD7NrzZB2V50yRHby9kkX4packiUkYcyWvPKnq529%2BtJUzl9Oo6aZeSkfFNHdj3wnCbhj4Fr%2FmSHQFCfLxZL%2FVbteJbgFVYGHppG1dNSbSe9NlK3huZC0%2F5D1v3U10LpEm2IZWXv9sanXiVNHamDJxufZiD7hf6qVdwMLq01gAUH8K8DUD8kLP9sla8gVcMC60rHSnhlZbl%2BVN0jQOnhrK9vkJYiKfMJ6Z78gGOqUBJ%2BOMZC35iHhGF8DTTID3po53kMvpp%2FLrgCGfYLwFj6CkWzM0B5U1SmTXYFlAeKVv%2B0lMxDWFpvi%2F3qhwGTYBUIcgNPZon6%2FnqQ3hX0JRQKF8Ii4FbccZpMKqFHg1SWBZsKY%2FD4kggPJT1NptZgxQGb2QyfytjUfsqV80etuxxF7iip7u9p8dJ3HNPPCYNwAKHNWrsr7Yz5CTNLSsIsJi6xcjL7w3&X-Amz-Signature=9370410e8af94440f2665ed45ab8b1a869792b2f6ce4802c63da3df6e20409de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



