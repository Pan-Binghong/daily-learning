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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PLK4LLR%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHA1%2F7M%2FHT5D5Aw95J5FIXeTNv5YEJpzdVEf3MCy1WJ2AiEAky6SwpNmYPDZi3QM5bKL76mljgWcKjCTIKPz%2FuBafwcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOkfoHzspWJQiOtfCrcA17DhwDMBZ1FDeFH8dNK3IKfpk7rVjQIyWTjM7q0gERuognoKBMLCzwsG9esPeh%2B7I2XoHUtBLhjwmimPIykIVH91BfixUX1TDxaaZlJ96iuMMUZ%2BZNwPRxPx4AR8MTfPULNXRfqFT0NeLdvq3%2BtPSgL78i6ggREuy354z3yu%2F87SbGQhLWUj74lS5VixMJRGePeRSpAoANJrv8k8R9UNLr%2FMNR32Ux5W9uYYJvYmzWjXpsIAT%2BnZdQ2mGz01oAeCzHT9JmuGEojnln7n2nyPjwv1gPauI8zJcyZWt6rtzf4THaP0m6R2UZ0jvcgksOOSBFMWqcS6JEhgHGfVcdPLjjHzaZzITcT%2FeqUGYEJ46WvRlABouluOZ9aKcg5qxKS%2Bj8UGVF0cAoshJUqP%2BWMnSYHSoL8X%2BbutuK0qMY4QVFtm4fBy%2FdixMQU8h4khNworNVzLwf%2F%2F%2FquPyZfK5huPI2JpEC4bxemz2yfc7QMrwCYP44cfJu6YcZkW5v6DrBCxlx73F92k6UoxM55FCYpI2sXVTqHfi9XJYImN8sv%2FJXnGeMNvhzCQzy4W%2BTVPgPE8ylWuAnlCe1ZyHdezKhxrJfpBZE00p3RbmtlunwBIuMVBVV42t9Sgji1ccs5MNLZwMsGOqUBo9YnY%2Fz4fg8WqRp45uLqix2RpywnqRWOehQrUoppeAZPDBSqiqTXGinoUguw71weLzRf5dJBirLiKxNIsVAUvhv9D9xloC%2FNImmvp7ypXUNvXDLp%2FCOp%2BKTHUNAg%2Fo3veRcU2fvZGtCAKbyRrV2gNUxmu73s%2FyP6Srnq1rpfsHkxFxkwHoHRUGRE%2BD4atXQQO5Ralg4wpYg7P8eZYqOLCc2iyEnl&X-Amz-Signature=3a7107fe18883efafb501f876d78e27bfcf2535c1eaf34471d04708268ad7ea7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PLK4LLR%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHA1%2F7M%2FHT5D5Aw95J5FIXeTNv5YEJpzdVEf3MCy1WJ2AiEAky6SwpNmYPDZi3QM5bKL76mljgWcKjCTIKPz%2FuBafwcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOkfoHzspWJQiOtfCrcA17DhwDMBZ1FDeFH8dNK3IKfpk7rVjQIyWTjM7q0gERuognoKBMLCzwsG9esPeh%2B7I2XoHUtBLhjwmimPIykIVH91BfixUX1TDxaaZlJ96iuMMUZ%2BZNwPRxPx4AR8MTfPULNXRfqFT0NeLdvq3%2BtPSgL78i6ggREuy354z3yu%2F87SbGQhLWUj74lS5VixMJRGePeRSpAoANJrv8k8R9UNLr%2FMNR32Ux5W9uYYJvYmzWjXpsIAT%2BnZdQ2mGz01oAeCzHT9JmuGEojnln7n2nyPjwv1gPauI8zJcyZWt6rtzf4THaP0m6R2UZ0jvcgksOOSBFMWqcS6JEhgHGfVcdPLjjHzaZzITcT%2FeqUGYEJ46WvRlABouluOZ9aKcg5qxKS%2Bj8UGVF0cAoshJUqP%2BWMnSYHSoL8X%2BbutuK0qMY4QVFtm4fBy%2FdixMQU8h4khNworNVzLwf%2F%2F%2FquPyZfK5huPI2JpEC4bxemz2yfc7QMrwCYP44cfJu6YcZkW5v6DrBCxlx73F92k6UoxM55FCYpI2sXVTqHfi9XJYImN8sv%2FJXnGeMNvhzCQzy4W%2BTVPgPE8ylWuAnlCe1ZyHdezKhxrJfpBZE00p3RbmtlunwBIuMVBVV42t9Sgji1ccs5MNLZwMsGOqUBo9YnY%2Fz4fg8WqRp45uLqix2RpywnqRWOehQrUoppeAZPDBSqiqTXGinoUguw71weLzRf5dJBirLiKxNIsVAUvhv9D9xloC%2FNImmvp7ypXUNvXDLp%2FCOp%2BKTHUNAg%2Fo3veRcU2fvZGtCAKbyRrV2gNUxmu73s%2FyP6Srnq1rpfsHkxFxkwHoHRUGRE%2BD4atXQQO5Ralg4wpYg7P8eZYqOLCc2iyEnl&X-Amz-Signature=0bc574eda996753dadb6a516ad23313ca4d892a5e76a8df8f484d29b12d406ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PLK4LLR%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHA1%2F7M%2FHT5D5Aw95J5FIXeTNv5YEJpzdVEf3MCy1WJ2AiEAky6SwpNmYPDZi3QM5bKL76mljgWcKjCTIKPz%2FuBafwcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOkfoHzspWJQiOtfCrcA17DhwDMBZ1FDeFH8dNK3IKfpk7rVjQIyWTjM7q0gERuognoKBMLCzwsG9esPeh%2B7I2XoHUtBLhjwmimPIykIVH91BfixUX1TDxaaZlJ96iuMMUZ%2BZNwPRxPx4AR8MTfPULNXRfqFT0NeLdvq3%2BtPSgL78i6ggREuy354z3yu%2F87SbGQhLWUj74lS5VixMJRGePeRSpAoANJrv8k8R9UNLr%2FMNR32Ux5W9uYYJvYmzWjXpsIAT%2BnZdQ2mGz01oAeCzHT9JmuGEojnln7n2nyPjwv1gPauI8zJcyZWt6rtzf4THaP0m6R2UZ0jvcgksOOSBFMWqcS6JEhgHGfVcdPLjjHzaZzITcT%2FeqUGYEJ46WvRlABouluOZ9aKcg5qxKS%2Bj8UGVF0cAoshJUqP%2BWMnSYHSoL8X%2BbutuK0qMY4QVFtm4fBy%2FdixMQU8h4khNworNVzLwf%2F%2F%2FquPyZfK5huPI2JpEC4bxemz2yfc7QMrwCYP44cfJu6YcZkW5v6DrBCxlx73F92k6UoxM55FCYpI2sXVTqHfi9XJYImN8sv%2FJXnGeMNvhzCQzy4W%2BTVPgPE8ylWuAnlCe1ZyHdezKhxrJfpBZE00p3RbmtlunwBIuMVBVV42t9Sgji1ccs5MNLZwMsGOqUBo9YnY%2Fz4fg8WqRp45uLqix2RpywnqRWOehQrUoppeAZPDBSqiqTXGinoUguw71weLzRf5dJBirLiKxNIsVAUvhv9D9xloC%2FNImmvp7ypXUNvXDLp%2FCOp%2BKTHUNAg%2Fo3veRcU2fvZGtCAKbyRrV2gNUxmu73s%2FyP6Srnq1rpfsHkxFxkwHoHRUGRE%2BD4atXQQO5Ralg4wpYg7P8eZYqOLCc2iyEnl&X-Amz-Signature=2f789efcc812198cdca19f168b3d0d74179aa1f11bf90e37e6a540fad2ea57b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PLK4LLR%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHA1%2F7M%2FHT5D5Aw95J5FIXeTNv5YEJpzdVEf3MCy1WJ2AiEAky6SwpNmYPDZi3QM5bKL76mljgWcKjCTIKPz%2FuBafwcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIOkfoHzspWJQiOtfCrcA17DhwDMBZ1FDeFH8dNK3IKfpk7rVjQIyWTjM7q0gERuognoKBMLCzwsG9esPeh%2B7I2XoHUtBLhjwmimPIykIVH91BfixUX1TDxaaZlJ96iuMMUZ%2BZNwPRxPx4AR8MTfPULNXRfqFT0NeLdvq3%2BtPSgL78i6ggREuy354z3yu%2F87SbGQhLWUj74lS5VixMJRGePeRSpAoANJrv8k8R9UNLr%2FMNR32Ux5W9uYYJvYmzWjXpsIAT%2BnZdQ2mGz01oAeCzHT9JmuGEojnln7n2nyPjwv1gPauI8zJcyZWt6rtzf4THaP0m6R2UZ0jvcgksOOSBFMWqcS6JEhgHGfVcdPLjjHzaZzITcT%2FeqUGYEJ46WvRlABouluOZ9aKcg5qxKS%2Bj8UGVF0cAoshJUqP%2BWMnSYHSoL8X%2BbutuK0qMY4QVFtm4fBy%2FdixMQU8h4khNworNVzLwf%2F%2F%2FquPyZfK5huPI2JpEC4bxemz2yfc7QMrwCYP44cfJu6YcZkW5v6DrBCxlx73F92k6UoxM55FCYpI2sXVTqHfi9XJYImN8sv%2FJXnGeMNvhzCQzy4W%2BTVPgPE8ylWuAnlCe1ZyHdezKhxrJfpBZE00p3RbmtlunwBIuMVBVV42t9Sgji1ccs5MNLZwMsGOqUBo9YnY%2Fz4fg8WqRp45uLqix2RpywnqRWOehQrUoppeAZPDBSqiqTXGinoUguw71weLzRf5dJBirLiKxNIsVAUvhv9D9xloC%2FNImmvp7ypXUNvXDLp%2FCOp%2BKTHUNAg%2Fo3veRcU2fvZGtCAKbyRrV2gNUxmu73s%2FyP6Srnq1rpfsHkxFxkwHoHRUGRE%2BD4atXQQO5Ralg4wpYg7P8eZYqOLCc2iyEnl&X-Amz-Signature=0ef89dfdd242b6aa3d08d1af73fae4631bf1f41b853d5b12fc4aaf9a83d29ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



