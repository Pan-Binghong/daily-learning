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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JNTS6PB%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS17QoRA2lvmyuGjqgVic%2B7PQpEnCHdbjD0dP0GhTCqwIgJH2dmkgHHfoP5WvRNMr2IOT30pthTGA4lUnhMSW8hMQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLUZRkmBsZIVyVQr4ircA4gZ%2FJkUDsD12d%2BY6aesblHJz7UFljj54RgcBpWE4%2Bk0Hc8GZ43Zctpb3fnFULXnI9GyzCBbNlkDx8Sl14mGEfOibXnifwRTckA97b73fbRZav0%2Bn0ea4aQDrOTzFAfVao7jbmTNorQSxKdnh8ZTeaePTpyhlmKxfnatLO2TUSzyFlJ8Wu%2FUev3DDQIbZE7n2gtGLLHdxKX6hJJShkPBCJp3QuAMwKnkOYlow15mMfavy9U1r4oYhP2TJ8wTNu0ZyRWut5folhTXMHydi9mIMjqOyfcgCRkcS8pazppQLnsDonKYjAIZp5WUBT9lroAQFFlWX8y09tZ5g8iZn6ewtETHOOSOe5F3oO2%2FxwbQwrOL1eHljoYsgVq5OAOhmmeWLVioJLmLLAyRdyJczGIRiudvEFM8eWda0Mf1qbtZWmxtxINhs4JzZnQDCyHf93HZHyEiD1shhf2%2BYTZrlip3vVZz4acbC6z6tr0LtAglzZEsvlcKxfuYOGtyOzScE9r4AnmI8OmGwlRkpmuPMa94hO52nV2fjM%2FsFx%2BtbxUCQnoaBwD2PoRnKQgFSNwIc4cPwOsUElOUJt3EEi4jTqfui83ixFgfNIcsvM8xbs%2FOLYbXif7vqQ40vb%2FGxW%2B8MOaYns0GOqUBCuGOj%2F8VB6BJJoZ1Eu8hhpLhzI1ucphPsNMHLb1HbM7yVYW%2Fcn0NA63CTd9TwGjTAy9nLKsJhGb6rQfMseALb35v4j5G9wosLzGNbw7%2FjVvMMohkBadFrmg%2FM2lgmmHmDoHAYtD22kbC93ksvi82ZZxpBxjzQ8etY2kWFAkPvZNo9KpeLzEzJuSUac0Be5RHAjzSyUUK3S9HnsqfbiX9Bz8Lf93W&X-Amz-Signature=e89c6b59d1352ad1e29a29334223e3b22bcf9fde451cf5a7426d1c95bcc248ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JNTS6PB%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS17QoRA2lvmyuGjqgVic%2B7PQpEnCHdbjD0dP0GhTCqwIgJH2dmkgHHfoP5WvRNMr2IOT30pthTGA4lUnhMSW8hMQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLUZRkmBsZIVyVQr4ircA4gZ%2FJkUDsD12d%2BY6aesblHJz7UFljj54RgcBpWE4%2Bk0Hc8GZ43Zctpb3fnFULXnI9GyzCBbNlkDx8Sl14mGEfOibXnifwRTckA97b73fbRZav0%2Bn0ea4aQDrOTzFAfVao7jbmTNorQSxKdnh8ZTeaePTpyhlmKxfnatLO2TUSzyFlJ8Wu%2FUev3DDQIbZE7n2gtGLLHdxKX6hJJShkPBCJp3QuAMwKnkOYlow15mMfavy9U1r4oYhP2TJ8wTNu0ZyRWut5folhTXMHydi9mIMjqOyfcgCRkcS8pazppQLnsDonKYjAIZp5WUBT9lroAQFFlWX8y09tZ5g8iZn6ewtETHOOSOe5F3oO2%2FxwbQwrOL1eHljoYsgVq5OAOhmmeWLVioJLmLLAyRdyJczGIRiudvEFM8eWda0Mf1qbtZWmxtxINhs4JzZnQDCyHf93HZHyEiD1shhf2%2BYTZrlip3vVZz4acbC6z6tr0LtAglzZEsvlcKxfuYOGtyOzScE9r4AnmI8OmGwlRkpmuPMa94hO52nV2fjM%2FsFx%2BtbxUCQnoaBwD2PoRnKQgFSNwIc4cPwOsUElOUJt3EEi4jTqfui83ixFgfNIcsvM8xbs%2FOLYbXif7vqQ40vb%2FGxW%2B8MOaYns0GOqUBCuGOj%2F8VB6BJJoZ1Eu8hhpLhzI1ucphPsNMHLb1HbM7yVYW%2Fcn0NA63CTd9TwGjTAy9nLKsJhGb6rQfMseALb35v4j5G9wosLzGNbw7%2FjVvMMohkBadFrmg%2FM2lgmmHmDoHAYtD22kbC93ksvi82ZZxpBxjzQ8etY2kWFAkPvZNo9KpeLzEzJuSUac0Be5RHAjzSyUUK3S9HnsqfbiX9Bz8Lf93W&X-Amz-Signature=f718514c4a7e0e33fbdaaa7c1bdc9eb28dcb3edc264062fcd8218a86d7d962c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JNTS6PB%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS17QoRA2lvmyuGjqgVic%2B7PQpEnCHdbjD0dP0GhTCqwIgJH2dmkgHHfoP5WvRNMr2IOT30pthTGA4lUnhMSW8hMQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLUZRkmBsZIVyVQr4ircA4gZ%2FJkUDsD12d%2BY6aesblHJz7UFljj54RgcBpWE4%2Bk0Hc8GZ43Zctpb3fnFULXnI9GyzCBbNlkDx8Sl14mGEfOibXnifwRTckA97b73fbRZav0%2Bn0ea4aQDrOTzFAfVao7jbmTNorQSxKdnh8ZTeaePTpyhlmKxfnatLO2TUSzyFlJ8Wu%2FUev3DDQIbZE7n2gtGLLHdxKX6hJJShkPBCJp3QuAMwKnkOYlow15mMfavy9U1r4oYhP2TJ8wTNu0ZyRWut5folhTXMHydi9mIMjqOyfcgCRkcS8pazppQLnsDonKYjAIZp5WUBT9lroAQFFlWX8y09tZ5g8iZn6ewtETHOOSOe5F3oO2%2FxwbQwrOL1eHljoYsgVq5OAOhmmeWLVioJLmLLAyRdyJczGIRiudvEFM8eWda0Mf1qbtZWmxtxINhs4JzZnQDCyHf93HZHyEiD1shhf2%2BYTZrlip3vVZz4acbC6z6tr0LtAglzZEsvlcKxfuYOGtyOzScE9r4AnmI8OmGwlRkpmuPMa94hO52nV2fjM%2FsFx%2BtbxUCQnoaBwD2PoRnKQgFSNwIc4cPwOsUElOUJt3EEi4jTqfui83ixFgfNIcsvM8xbs%2FOLYbXif7vqQ40vb%2FGxW%2B8MOaYns0GOqUBCuGOj%2F8VB6BJJoZ1Eu8hhpLhzI1ucphPsNMHLb1HbM7yVYW%2Fcn0NA63CTd9TwGjTAy9nLKsJhGb6rQfMseALb35v4j5G9wosLzGNbw7%2FjVvMMohkBadFrmg%2FM2lgmmHmDoHAYtD22kbC93ksvi82ZZxpBxjzQ8etY2kWFAkPvZNo9KpeLzEzJuSUac0Be5RHAjzSyUUK3S9HnsqfbiX9Bz8Lf93W&X-Amz-Signature=35feeb77e857ae753cbabad4a34fbf9058a80f8fba181c19fe93c982e488a6b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JNTS6PB%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS17QoRA2lvmyuGjqgVic%2B7PQpEnCHdbjD0dP0GhTCqwIgJH2dmkgHHfoP5WvRNMr2IOT30pthTGA4lUnhMSW8hMQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLUZRkmBsZIVyVQr4ircA4gZ%2FJkUDsD12d%2BY6aesblHJz7UFljj54RgcBpWE4%2Bk0Hc8GZ43Zctpb3fnFULXnI9GyzCBbNlkDx8Sl14mGEfOibXnifwRTckA97b73fbRZav0%2Bn0ea4aQDrOTzFAfVao7jbmTNorQSxKdnh8ZTeaePTpyhlmKxfnatLO2TUSzyFlJ8Wu%2FUev3DDQIbZE7n2gtGLLHdxKX6hJJShkPBCJp3QuAMwKnkOYlow15mMfavy9U1r4oYhP2TJ8wTNu0ZyRWut5folhTXMHydi9mIMjqOyfcgCRkcS8pazppQLnsDonKYjAIZp5WUBT9lroAQFFlWX8y09tZ5g8iZn6ewtETHOOSOe5F3oO2%2FxwbQwrOL1eHljoYsgVq5OAOhmmeWLVioJLmLLAyRdyJczGIRiudvEFM8eWda0Mf1qbtZWmxtxINhs4JzZnQDCyHf93HZHyEiD1shhf2%2BYTZrlip3vVZz4acbC6z6tr0LtAglzZEsvlcKxfuYOGtyOzScE9r4AnmI8OmGwlRkpmuPMa94hO52nV2fjM%2FsFx%2BtbxUCQnoaBwD2PoRnKQgFSNwIc4cPwOsUElOUJt3EEi4jTqfui83ixFgfNIcsvM8xbs%2FOLYbXif7vqQ40vb%2FGxW%2B8MOaYns0GOqUBCuGOj%2F8VB6BJJoZ1Eu8hhpLhzI1ucphPsNMHLb1HbM7yVYW%2Fcn0NA63CTd9TwGjTAy9nLKsJhGb6rQfMseALb35v4j5G9wosLzGNbw7%2FjVvMMohkBadFrmg%2FM2lgmmHmDoHAYtD22kbC93ksvi82ZZxpBxjzQ8etY2kWFAkPvZNo9KpeLzEzJuSUac0Be5RHAjzSyUUK3S9HnsqfbiX9Bz8Lf93W&X-Amz-Signature=a1e967e4d23f77e8343a8bc5a6df76ba5444847b53a9fd046c79df92dc7ee886&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



