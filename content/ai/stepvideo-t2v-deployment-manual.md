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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3MH6P2B%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDC%2FLpES0PB7jj05XbcyrWuxmKNba18hBSOFhYk0O16EQIgC8ZIiFIntGJoVSaHUe6b5TtPpvShkYTQsgn2H%2BWrV2sqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpcChXdmUGcG%2FltQyrcAw%2BE3sxvNG18wdsnc0jmGNvROp8uAgiutzwY%2FHT7yU9XmNOl5iDQdU1nAdOsIaEtyZKQPi6%2B8oAtXPoa%2FlRi83gzQbSdX%2BuK6%2Fo1H92WlU%2Bp6giSu8fTxDIfyYx9UbY8uj225VAMbSZ2rKPYwfUmY9CeTNTIWVCdS3cbh3XRBUl2Bn91Ad%2BXp%2BiCsyUtw1xXcFtIM30OyTlR%2BSWFZzAWEYhQW9GzDI38kL3KNNCTMmbkbUhCT%2FMeGCN62QOe8fVBZPzsb8J8bAa%2BStxWAp4SUP6xRhq65VppPpNY%2FA%2BlwgaoJJ7%2BugNRKq2Ok1XlQbtwGmZYNECZxvVjGh5EnGkhBIlq7dm6jChlvl2kuDlWwu4m4sFXBzPudF0LmgEo6wwkVTBECJhNtNfvSfsQB6KJcCUHJrN6x3BoWQbpounzsZNxTHE3wJ43DLMlGL5NcGlBcU4ZXbfX0Wk3dHHdPCcVB6dQD88kHGWPVtucwWWLT34LOidwicAV9TI4qYLoWRg8zv41XXj2Qxc%2F36K0lkNd4gKexr33TwNLPzRugq4w%2BUW%2Fg5j36KdYu3yMbgP5OTwP774IROGCkql4o%2BKBKeJF4%2FhzjpUtwNyotqAwRqbsoo2n4XQPkK81oT%2BD71sMMMDJ9MgGOqUBI0mA%2FAeBGHjMRZPph4AQMibH23ZKa8jhPtmXwvemexTtLZxBtvKfWoiAopPU9NwKcGfi7tSYSQ8K38bYxzz71QOzNO%2FhhY03QDeBumLa0jlzShq6vixWvfSh0Nl2vLvyQPm6NzCvLTUAPqRvJQMSUUY4aD0n1kx2q5he7fvsYjcMZ%2F%2F%2BuExxdfPmUCmci4JHgp9fhLZvYKQ8WYFuUK7Z5PYypAtJ&X-Amz-Signature=002f00a03aea8178d8a5c7fbad00cb45a75f554a2c4952a0717d7da7c0e01444&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3MH6P2B%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDC%2FLpES0PB7jj05XbcyrWuxmKNba18hBSOFhYk0O16EQIgC8ZIiFIntGJoVSaHUe6b5TtPpvShkYTQsgn2H%2BWrV2sqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpcChXdmUGcG%2FltQyrcAw%2BE3sxvNG18wdsnc0jmGNvROp8uAgiutzwY%2FHT7yU9XmNOl5iDQdU1nAdOsIaEtyZKQPi6%2B8oAtXPoa%2FlRi83gzQbSdX%2BuK6%2Fo1H92WlU%2Bp6giSu8fTxDIfyYx9UbY8uj225VAMbSZ2rKPYwfUmY9CeTNTIWVCdS3cbh3XRBUl2Bn91Ad%2BXp%2BiCsyUtw1xXcFtIM30OyTlR%2BSWFZzAWEYhQW9GzDI38kL3KNNCTMmbkbUhCT%2FMeGCN62QOe8fVBZPzsb8J8bAa%2BStxWAp4SUP6xRhq65VppPpNY%2FA%2BlwgaoJJ7%2BugNRKq2Ok1XlQbtwGmZYNECZxvVjGh5EnGkhBIlq7dm6jChlvl2kuDlWwu4m4sFXBzPudF0LmgEo6wwkVTBECJhNtNfvSfsQB6KJcCUHJrN6x3BoWQbpounzsZNxTHE3wJ43DLMlGL5NcGlBcU4ZXbfX0Wk3dHHdPCcVB6dQD88kHGWPVtucwWWLT34LOidwicAV9TI4qYLoWRg8zv41XXj2Qxc%2F36K0lkNd4gKexr33TwNLPzRugq4w%2BUW%2Fg5j36KdYu3yMbgP5OTwP774IROGCkql4o%2BKBKeJF4%2FhzjpUtwNyotqAwRqbsoo2n4XQPkK81oT%2BD71sMMMDJ9MgGOqUBI0mA%2FAeBGHjMRZPph4AQMibH23ZKa8jhPtmXwvemexTtLZxBtvKfWoiAopPU9NwKcGfi7tSYSQ8K38bYxzz71QOzNO%2FhhY03QDeBumLa0jlzShq6vixWvfSh0Nl2vLvyQPm6NzCvLTUAPqRvJQMSUUY4aD0n1kx2q5he7fvsYjcMZ%2F%2F%2BuExxdfPmUCmci4JHgp9fhLZvYKQ8WYFuUK7Z5PYypAtJ&X-Amz-Signature=2232aa4d1035af9e56a9a7092802c444c12851bf7dbda288273687cc9bdd33f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3MH6P2B%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDC%2FLpES0PB7jj05XbcyrWuxmKNba18hBSOFhYk0O16EQIgC8ZIiFIntGJoVSaHUe6b5TtPpvShkYTQsgn2H%2BWrV2sqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpcChXdmUGcG%2FltQyrcAw%2BE3sxvNG18wdsnc0jmGNvROp8uAgiutzwY%2FHT7yU9XmNOl5iDQdU1nAdOsIaEtyZKQPi6%2B8oAtXPoa%2FlRi83gzQbSdX%2BuK6%2Fo1H92WlU%2Bp6giSu8fTxDIfyYx9UbY8uj225VAMbSZ2rKPYwfUmY9CeTNTIWVCdS3cbh3XRBUl2Bn91Ad%2BXp%2BiCsyUtw1xXcFtIM30OyTlR%2BSWFZzAWEYhQW9GzDI38kL3KNNCTMmbkbUhCT%2FMeGCN62QOe8fVBZPzsb8J8bAa%2BStxWAp4SUP6xRhq65VppPpNY%2FA%2BlwgaoJJ7%2BugNRKq2Ok1XlQbtwGmZYNECZxvVjGh5EnGkhBIlq7dm6jChlvl2kuDlWwu4m4sFXBzPudF0LmgEo6wwkVTBECJhNtNfvSfsQB6KJcCUHJrN6x3BoWQbpounzsZNxTHE3wJ43DLMlGL5NcGlBcU4ZXbfX0Wk3dHHdPCcVB6dQD88kHGWPVtucwWWLT34LOidwicAV9TI4qYLoWRg8zv41XXj2Qxc%2F36K0lkNd4gKexr33TwNLPzRugq4w%2BUW%2Fg5j36KdYu3yMbgP5OTwP774IROGCkql4o%2BKBKeJF4%2FhzjpUtwNyotqAwRqbsoo2n4XQPkK81oT%2BD71sMMMDJ9MgGOqUBI0mA%2FAeBGHjMRZPph4AQMibH23ZKa8jhPtmXwvemexTtLZxBtvKfWoiAopPU9NwKcGfi7tSYSQ8K38bYxzz71QOzNO%2FhhY03QDeBumLa0jlzShq6vixWvfSh0Nl2vLvyQPm6NzCvLTUAPqRvJQMSUUY4aD0n1kx2q5he7fvsYjcMZ%2F%2F%2BuExxdfPmUCmci4JHgp9fhLZvYKQ8WYFuUK7Z5PYypAtJ&X-Amz-Signature=3ca13410e6aebc9a202043f6c8345570f993e976c00ab2b4bc897fcc847e4edb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3MH6P2B%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDC%2FLpES0PB7jj05XbcyrWuxmKNba18hBSOFhYk0O16EQIgC8ZIiFIntGJoVSaHUe6b5TtPpvShkYTQsgn2H%2BWrV2sqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBpcChXdmUGcG%2FltQyrcAw%2BE3sxvNG18wdsnc0jmGNvROp8uAgiutzwY%2FHT7yU9XmNOl5iDQdU1nAdOsIaEtyZKQPi6%2B8oAtXPoa%2FlRi83gzQbSdX%2BuK6%2Fo1H92WlU%2Bp6giSu8fTxDIfyYx9UbY8uj225VAMbSZ2rKPYwfUmY9CeTNTIWVCdS3cbh3XRBUl2Bn91Ad%2BXp%2BiCsyUtw1xXcFtIM30OyTlR%2BSWFZzAWEYhQW9GzDI38kL3KNNCTMmbkbUhCT%2FMeGCN62QOe8fVBZPzsb8J8bAa%2BStxWAp4SUP6xRhq65VppPpNY%2FA%2BlwgaoJJ7%2BugNRKq2Ok1XlQbtwGmZYNECZxvVjGh5EnGkhBIlq7dm6jChlvl2kuDlWwu4m4sFXBzPudF0LmgEo6wwkVTBECJhNtNfvSfsQB6KJcCUHJrN6x3BoWQbpounzsZNxTHE3wJ43DLMlGL5NcGlBcU4ZXbfX0Wk3dHHdPCcVB6dQD88kHGWPVtucwWWLT34LOidwicAV9TI4qYLoWRg8zv41XXj2Qxc%2F36K0lkNd4gKexr33TwNLPzRugq4w%2BUW%2Fg5j36KdYu3yMbgP5OTwP774IROGCkql4o%2BKBKeJF4%2FhzjpUtwNyotqAwRqbsoo2n4XQPkK81oT%2BD71sMMMDJ9MgGOqUBI0mA%2FAeBGHjMRZPph4AQMibH23ZKa8jhPtmXwvemexTtLZxBtvKfWoiAopPU9NwKcGfi7tSYSQ8K38bYxzz71QOzNO%2FhhY03QDeBumLa0jlzShq6vixWvfSh0Nl2vLvyQPm6NzCvLTUAPqRvJQMSUUY4aD0n1kx2q5he7fvsYjcMZ%2F%2F%2BuExxdfPmUCmci4JHgp9fhLZvYKQ8WYFuUK7Z5PYypAtJ&X-Amz-Signature=3cd509f71354d8cdae7d6c3eb26b08b88ac31e8fa3c2c41c3ccb3bed38066733&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



