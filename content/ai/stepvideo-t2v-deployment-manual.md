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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X56PG72A%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIFGpzEQvcjCrQqSDtMMK03WHX0gSfiaBBJZgnfYNiK%2FAAiEAt6SB42sC4CvNo5ZbCHb27Y1mESIPGIl6rRqspWozDcsq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDMnodkFCHaIi14nboSrcA4JNd7C2bSQzElxtI6VB7MoklULuiZ6%2F36XQ4e1bQidjKATWUCSrbLVuftxTsNOVJrnzccxQRgfGPH6p20MlSxHI4nBEdw8KJsrMi2MQjBjKbjMywNdnZfDahjaMaeCS1Jv1oLj2jiXi81yyAFX8RWkYvtBSHBdEQUvYYc%2B9%2FpW1h1FUVWx9%2Fgrh9Tq5D3a5HRRXkVG0O3RMIloSYbqd7BC2CeLoRWqJT587o7GSrCN9ZqQtSaGGIhxOxFc3utOwFCR%2FG454U78b%2F46DJXkKIjs486YkA%2B4XKV1JBazDM5bmsIZ2VM9cq1X5y%2Bq5U7Bc8pCKLyO3v8%2BROFg%2FTNjZjL91p93XLZWkqWeFe8fZ8rqwrz9qlKLbo%2BQuF%2FQoGuNufjonDjC3Eo74hfvJeT%2FLvd3oIhZDmcljDlc%2FaiE0ZM%2Bqg%2FwzI8H0tw0eGZhE9khoQwVFQIpufZ3MlPbZiToeNeennPhm8bghnYoRW%2F4FvefA0URV67SYDIwtaY72dXHWiPCM7p2fuFWKo6QWludRM%2BEoat2KW%2FsmanB5VD%2Fy9aS36Y1ChT1k9cThGTKSWhD%2BnnorW4P7trZU0kWQ14Q4juZ7i3H5zsJvkDqV5IkCI%2B397WOJf8aebZuP3KviMLT94coGOqUBvWnHDBm4eRgOab1fOQ4HJcmtKAzMKCziMclL9bdI%2BqUduIAeDeWOAv1bJmkXRlxrKcJY2DOu15LMJ6zzAaJtmmG6SYP2%2BlgUBUv1CInO0W5foMRdU4Jl4P0NU2yVh1s6UI6VDQRZjOs1m%2BxqttVgTdD5SpmdXvO7QrNtO7ze0Z3JxfUpcSrou3JUIDuGarn1f2YnPyGocV1uetxh85TnfOr72mMd&X-Amz-Signature=13f75deece2761c27d1a376a998a26cb7938ce57b12dce115fe5bff0e244edf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X56PG72A%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIFGpzEQvcjCrQqSDtMMK03WHX0gSfiaBBJZgnfYNiK%2FAAiEAt6SB42sC4CvNo5ZbCHb27Y1mESIPGIl6rRqspWozDcsq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDMnodkFCHaIi14nboSrcA4JNd7C2bSQzElxtI6VB7MoklULuiZ6%2F36XQ4e1bQidjKATWUCSrbLVuftxTsNOVJrnzccxQRgfGPH6p20MlSxHI4nBEdw8KJsrMi2MQjBjKbjMywNdnZfDahjaMaeCS1Jv1oLj2jiXi81yyAFX8RWkYvtBSHBdEQUvYYc%2B9%2FpW1h1FUVWx9%2Fgrh9Tq5D3a5HRRXkVG0O3RMIloSYbqd7BC2CeLoRWqJT587o7GSrCN9ZqQtSaGGIhxOxFc3utOwFCR%2FG454U78b%2F46DJXkKIjs486YkA%2B4XKV1JBazDM5bmsIZ2VM9cq1X5y%2Bq5U7Bc8pCKLyO3v8%2BROFg%2FTNjZjL91p93XLZWkqWeFe8fZ8rqwrz9qlKLbo%2BQuF%2FQoGuNufjonDjC3Eo74hfvJeT%2FLvd3oIhZDmcljDlc%2FaiE0ZM%2Bqg%2FwzI8H0tw0eGZhE9khoQwVFQIpufZ3MlPbZiToeNeennPhm8bghnYoRW%2F4FvefA0URV67SYDIwtaY72dXHWiPCM7p2fuFWKo6QWludRM%2BEoat2KW%2FsmanB5VD%2Fy9aS36Y1ChT1k9cThGTKSWhD%2BnnorW4P7trZU0kWQ14Q4juZ7i3H5zsJvkDqV5IkCI%2B397WOJf8aebZuP3KviMLT94coGOqUBvWnHDBm4eRgOab1fOQ4HJcmtKAzMKCziMclL9bdI%2BqUduIAeDeWOAv1bJmkXRlxrKcJY2DOu15LMJ6zzAaJtmmG6SYP2%2BlgUBUv1CInO0W5foMRdU4Jl4P0NU2yVh1s6UI6VDQRZjOs1m%2BxqttVgTdD5SpmdXvO7QrNtO7ze0Z3JxfUpcSrou3JUIDuGarn1f2YnPyGocV1uetxh85TnfOr72mMd&X-Amz-Signature=ededd1195338d89cc7a04aa66116722495ae258241e1ff65f9e4ea2fdec080ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X56PG72A%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIFGpzEQvcjCrQqSDtMMK03WHX0gSfiaBBJZgnfYNiK%2FAAiEAt6SB42sC4CvNo5ZbCHb27Y1mESIPGIl6rRqspWozDcsq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDMnodkFCHaIi14nboSrcA4JNd7C2bSQzElxtI6VB7MoklULuiZ6%2F36XQ4e1bQidjKATWUCSrbLVuftxTsNOVJrnzccxQRgfGPH6p20MlSxHI4nBEdw8KJsrMi2MQjBjKbjMywNdnZfDahjaMaeCS1Jv1oLj2jiXi81yyAFX8RWkYvtBSHBdEQUvYYc%2B9%2FpW1h1FUVWx9%2Fgrh9Tq5D3a5HRRXkVG0O3RMIloSYbqd7BC2CeLoRWqJT587o7GSrCN9ZqQtSaGGIhxOxFc3utOwFCR%2FG454U78b%2F46DJXkKIjs486YkA%2B4XKV1JBazDM5bmsIZ2VM9cq1X5y%2Bq5U7Bc8pCKLyO3v8%2BROFg%2FTNjZjL91p93XLZWkqWeFe8fZ8rqwrz9qlKLbo%2BQuF%2FQoGuNufjonDjC3Eo74hfvJeT%2FLvd3oIhZDmcljDlc%2FaiE0ZM%2Bqg%2FwzI8H0tw0eGZhE9khoQwVFQIpufZ3MlPbZiToeNeennPhm8bghnYoRW%2F4FvefA0URV67SYDIwtaY72dXHWiPCM7p2fuFWKo6QWludRM%2BEoat2KW%2FsmanB5VD%2Fy9aS36Y1ChT1k9cThGTKSWhD%2BnnorW4P7trZU0kWQ14Q4juZ7i3H5zsJvkDqV5IkCI%2B397WOJf8aebZuP3KviMLT94coGOqUBvWnHDBm4eRgOab1fOQ4HJcmtKAzMKCziMclL9bdI%2BqUduIAeDeWOAv1bJmkXRlxrKcJY2DOu15LMJ6zzAaJtmmG6SYP2%2BlgUBUv1CInO0W5foMRdU4Jl4P0NU2yVh1s6UI6VDQRZjOs1m%2BxqttVgTdD5SpmdXvO7QrNtO7ze0Z3JxfUpcSrou3JUIDuGarn1f2YnPyGocV1uetxh85TnfOr72mMd&X-Amz-Signature=569447efba6682ac946103fdb3ea1390424c6c5dbaf2b93bfab90bd364b4416a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X56PG72A%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIFGpzEQvcjCrQqSDtMMK03WHX0gSfiaBBJZgnfYNiK%2FAAiEAt6SB42sC4CvNo5ZbCHb27Y1mESIPGIl6rRqspWozDcsq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDMnodkFCHaIi14nboSrcA4JNd7C2bSQzElxtI6VB7MoklULuiZ6%2F36XQ4e1bQidjKATWUCSrbLVuftxTsNOVJrnzccxQRgfGPH6p20MlSxHI4nBEdw8KJsrMi2MQjBjKbjMywNdnZfDahjaMaeCS1Jv1oLj2jiXi81yyAFX8RWkYvtBSHBdEQUvYYc%2B9%2FpW1h1FUVWx9%2Fgrh9Tq5D3a5HRRXkVG0O3RMIloSYbqd7BC2CeLoRWqJT587o7GSrCN9ZqQtSaGGIhxOxFc3utOwFCR%2FG454U78b%2F46DJXkKIjs486YkA%2B4XKV1JBazDM5bmsIZ2VM9cq1X5y%2Bq5U7Bc8pCKLyO3v8%2BROFg%2FTNjZjL91p93XLZWkqWeFe8fZ8rqwrz9qlKLbo%2BQuF%2FQoGuNufjonDjC3Eo74hfvJeT%2FLvd3oIhZDmcljDlc%2FaiE0ZM%2Bqg%2FwzI8H0tw0eGZhE9khoQwVFQIpufZ3MlPbZiToeNeennPhm8bghnYoRW%2F4FvefA0URV67SYDIwtaY72dXHWiPCM7p2fuFWKo6QWludRM%2BEoat2KW%2FsmanB5VD%2Fy9aS36Y1ChT1k9cThGTKSWhD%2BnnorW4P7trZU0kWQ14Q4juZ7i3H5zsJvkDqV5IkCI%2B397WOJf8aebZuP3KviMLT94coGOqUBvWnHDBm4eRgOab1fOQ4HJcmtKAzMKCziMclL9bdI%2BqUduIAeDeWOAv1bJmkXRlxrKcJY2DOu15LMJ6zzAaJtmmG6SYP2%2BlgUBUv1CInO0W5foMRdU4Jl4P0NU2yVh1s6UI6VDQRZjOs1m%2BxqttVgTdD5SpmdXvO7QrNtO7ze0Z3JxfUpcSrou3JUIDuGarn1f2YnPyGocV1uetxh85TnfOr72mMd&X-Amz-Signature=3dcfca026b92808585780f3b61978e0a2a8922b8c39b0c96ed74a59ae6c8dd99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



