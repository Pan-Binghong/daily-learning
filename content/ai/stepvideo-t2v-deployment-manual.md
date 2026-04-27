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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7O5TWTW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa%2Fb%2BIiJXljT%2FL76U7nm5FdZSyZRMw%2BsPLT7fNU6yaBQIgKcZYrQ2CUd07gj42M2hk0c8VfWyNtKvvI8TuF70jC00qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BDWV5pjTbztlE5%2BircAzoOodHjFGS4AqVWCO%2Bm8lacnI3y09G9fwXrlqI1T0Mk9ZkMK0wW1gkVCKB9anc8BUi2cEdffHotVi%2B1MBaMsvJaZuOX%2F0SwCuspHv90O7xhUuAYzyKpQov5eDCGQlsz0rP4vR1sCSV%2BjATIjk8icJkAXqkD18hOrS3He%2FuEC%2Fva7RhH2e7h8A357DOZlVxQLqn%2FeVBP2Yg%2FB40DdjAFCx6isdyDCqJnilRl9Vxk2Pe%2F04GQDAwUvpjk7S9ShRS12FbPXBub5evxnD%2FqrS09KRaycSKPKQgY09Hqq5Y4yb1ayI6FPu49Lhdce0R9sfq7iD6Gg%2FXQfizmu5I06R7y%2FHd7SMO2hdwWa7FOD8xNGZinaOd6HJxkZ4viegUka037kFS4vfDS6H8l8v07kAJcZtl5aJfxRg8cCUnMfOYCDx8XU5UfuutcogZjm%2FUbvls38pk7hj%2FGSNa2OGhKdyuHVHNv7eL%2B0VIp7okw8lS3B7uOrwMdCgTJPe5mZdRKFzSSbZJanBsq88QH5l5GxIoe8wKH%2B5Rr%2FucqzcUmtJKrpXgbHmLvhG%2BlHYgQkHws3%2BRDlrPgU1voMwy3WLnNdsISfoncj4ib7aCv2Z7DUeo2j7kq2wP2scAgG3VpAepBML%2B2u88GOqUBtSfqsOGWvruvP6DzE6KhJ7Ap3WMH4n4y7jsmmOSSz2xaGh7W8h%2F7ooiKqHxRv5gDZ2xXW2nP9PQ5MVXn5uj3aK67wjFX4RqfJnbcEDrlAybnCimtzDBlnHxcbFSMEpOEQgCWwnM4w8JVfmjpOrB5VLqEHOiRhJJ5ETekyXnwVZ8oNR8rUJeAR8oX1Af%2Fd1aNA5LbN%2B%2Fve2xVNffqt1GYQ2sqyCDO&X-Amz-Signature=cb53c5af7b9a37e1ea6d32a24626b1a595c396e6ef00ba32a7a8d6e32260ceae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7O5TWTW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa%2Fb%2BIiJXljT%2FL76U7nm5FdZSyZRMw%2BsPLT7fNU6yaBQIgKcZYrQ2CUd07gj42M2hk0c8VfWyNtKvvI8TuF70jC00qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BDWV5pjTbztlE5%2BircAzoOodHjFGS4AqVWCO%2Bm8lacnI3y09G9fwXrlqI1T0Mk9ZkMK0wW1gkVCKB9anc8BUi2cEdffHotVi%2B1MBaMsvJaZuOX%2F0SwCuspHv90O7xhUuAYzyKpQov5eDCGQlsz0rP4vR1sCSV%2BjATIjk8icJkAXqkD18hOrS3He%2FuEC%2Fva7RhH2e7h8A357DOZlVxQLqn%2FeVBP2Yg%2FB40DdjAFCx6isdyDCqJnilRl9Vxk2Pe%2F04GQDAwUvpjk7S9ShRS12FbPXBub5evxnD%2FqrS09KRaycSKPKQgY09Hqq5Y4yb1ayI6FPu49Lhdce0R9sfq7iD6Gg%2FXQfizmu5I06R7y%2FHd7SMO2hdwWa7FOD8xNGZinaOd6HJxkZ4viegUka037kFS4vfDS6H8l8v07kAJcZtl5aJfxRg8cCUnMfOYCDx8XU5UfuutcogZjm%2FUbvls38pk7hj%2FGSNa2OGhKdyuHVHNv7eL%2B0VIp7okw8lS3B7uOrwMdCgTJPe5mZdRKFzSSbZJanBsq88QH5l5GxIoe8wKH%2B5Rr%2FucqzcUmtJKrpXgbHmLvhG%2BlHYgQkHws3%2BRDlrPgU1voMwy3WLnNdsISfoncj4ib7aCv2Z7DUeo2j7kq2wP2scAgG3VpAepBML%2B2u88GOqUBtSfqsOGWvruvP6DzE6KhJ7Ap3WMH4n4y7jsmmOSSz2xaGh7W8h%2F7ooiKqHxRv5gDZ2xXW2nP9PQ5MVXn5uj3aK67wjFX4RqfJnbcEDrlAybnCimtzDBlnHxcbFSMEpOEQgCWwnM4w8JVfmjpOrB5VLqEHOiRhJJ5ETekyXnwVZ8oNR8rUJeAR8oX1Af%2Fd1aNA5LbN%2B%2Fve2xVNffqt1GYQ2sqyCDO&X-Amz-Signature=7fab5870c41a4d35bab04e453e227c33c26fdc911a32daab2f0f340b66931f27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7O5TWTW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa%2Fb%2BIiJXljT%2FL76U7nm5FdZSyZRMw%2BsPLT7fNU6yaBQIgKcZYrQ2CUd07gj42M2hk0c8VfWyNtKvvI8TuF70jC00qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BDWV5pjTbztlE5%2BircAzoOodHjFGS4AqVWCO%2Bm8lacnI3y09G9fwXrlqI1T0Mk9ZkMK0wW1gkVCKB9anc8BUi2cEdffHotVi%2B1MBaMsvJaZuOX%2F0SwCuspHv90O7xhUuAYzyKpQov5eDCGQlsz0rP4vR1sCSV%2BjATIjk8icJkAXqkD18hOrS3He%2FuEC%2Fva7RhH2e7h8A357DOZlVxQLqn%2FeVBP2Yg%2FB40DdjAFCx6isdyDCqJnilRl9Vxk2Pe%2F04GQDAwUvpjk7S9ShRS12FbPXBub5evxnD%2FqrS09KRaycSKPKQgY09Hqq5Y4yb1ayI6FPu49Lhdce0R9sfq7iD6Gg%2FXQfizmu5I06R7y%2FHd7SMO2hdwWa7FOD8xNGZinaOd6HJxkZ4viegUka037kFS4vfDS6H8l8v07kAJcZtl5aJfxRg8cCUnMfOYCDx8XU5UfuutcogZjm%2FUbvls38pk7hj%2FGSNa2OGhKdyuHVHNv7eL%2B0VIp7okw8lS3B7uOrwMdCgTJPe5mZdRKFzSSbZJanBsq88QH5l5GxIoe8wKH%2B5Rr%2FucqzcUmtJKrpXgbHmLvhG%2BlHYgQkHws3%2BRDlrPgU1voMwy3WLnNdsISfoncj4ib7aCv2Z7DUeo2j7kq2wP2scAgG3VpAepBML%2B2u88GOqUBtSfqsOGWvruvP6DzE6KhJ7Ap3WMH4n4y7jsmmOSSz2xaGh7W8h%2F7ooiKqHxRv5gDZ2xXW2nP9PQ5MVXn5uj3aK67wjFX4RqfJnbcEDrlAybnCimtzDBlnHxcbFSMEpOEQgCWwnM4w8JVfmjpOrB5VLqEHOiRhJJ5ETekyXnwVZ8oNR8rUJeAR8oX1Af%2Fd1aNA5LbN%2B%2Fve2xVNffqt1GYQ2sqyCDO&X-Amz-Signature=b40aed8e4d3a4d24b7f62fb6287cfe83b2ae05e0b6082f1e9bdff6e8ca1e5839&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7O5TWTW%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCa%2Fb%2BIiJXljT%2FL76U7nm5FdZSyZRMw%2BsPLT7fNU6yaBQIgKcZYrQ2CUd07gj42M2hk0c8VfWyNtKvvI8TuF70jC00qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2BDWV5pjTbztlE5%2BircAzoOodHjFGS4AqVWCO%2Bm8lacnI3y09G9fwXrlqI1T0Mk9ZkMK0wW1gkVCKB9anc8BUi2cEdffHotVi%2B1MBaMsvJaZuOX%2F0SwCuspHv90O7xhUuAYzyKpQov5eDCGQlsz0rP4vR1sCSV%2BjATIjk8icJkAXqkD18hOrS3He%2FuEC%2Fva7RhH2e7h8A357DOZlVxQLqn%2FeVBP2Yg%2FB40DdjAFCx6isdyDCqJnilRl9Vxk2Pe%2F04GQDAwUvpjk7S9ShRS12FbPXBub5evxnD%2FqrS09KRaycSKPKQgY09Hqq5Y4yb1ayI6FPu49Lhdce0R9sfq7iD6Gg%2FXQfizmu5I06R7y%2FHd7SMO2hdwWa7FOD8xNGZinaOd6HJxkZ4viegUka037kFS4vfDS6H8l8v07kAJcZtl5aJfxRg8cCUnMfOYCDx8XU5UfuutcogZjm%2FUbvls38pk7hj%2FGSNa2OGhKdyuHVHNv7eL%2B0VIp7okw8lS3B7uOrwMdCgTJPe5mZdRKFzSSbZJanBsq88QH5l5GxIoe8wKH%2B5Rr%2FucqzcUmtJKrpXgbHmLvhG%2BlHYgQkHws3%2BRDlrPgU1voMwy3WLnNdsISfoncj4ib7aCv2Z7DUeo2j7kq2wP2scAgG3VpAepBML%2B2u88GOqUBtSfqsOGWvruvP6DzE6KhJ7Ap3WMH4n4y7jsmmOSSz2xaGh7W8h%2F7ooiKqHxRv5gDZ2xXW2nP9PQ5MVXn5uj3aK67wjFX4RqfJnbcEDrlAybnCimtzDBlnHxcbFSMEpOEQgCWwnM4w8JVfmjpOrB5VLqEHOiRhJJ5ETekyXnwVZ8oNR8rUJeAR8oX1Af%2Fd1aNA5LbN%2B%2Fve2xVNffqt1GYQ2sqyCDO&X-Amz-Signature=d7071d32ce89832bf2eb211a67c6ad327b343be5b60f56c6c247943bb47c4042&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



