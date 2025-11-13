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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6WC6ZGG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQD1Nz7%2BzZ1TnVf%2F%2F8PYezBRu9AlbYs1Tp05KTDmj76tiwIhAPD4Rvx86AwkxI2UpawE5icRx5uKwyyaBjHgbvVZxZFBKv8DCEMQABoMNjM3NDIzMTgzODA1IgztjFg8fcVjHkMb%2F6kq3AMzAMqFs2RDd5f4CmwUgD4iLvg05iUb%2FIfEh3LApBMdo9CEeEEBmz2W6V%2BUOgiiZh1hYFs8e3t4Txog58C0a02HVSZ7GGA4vB1sCcb%2FmjUJintDVDa8G4kphvRSpbK6NCDlq4zDq89M3ulZKun361z200xOWBzZ7jY6C%2FPaQqooz0hgbd9niV0xXQCFItJqlTgDJ%2F2c0nGrVaZ5aFFTOg0WKwfETy7h7zssni6OAeMK3w9QZFkPTVgAIF6ATHpcDDodMtRsnU%2F4%2B2ccLAwT4%2BYxmWzS2kZB08yzH%2Bm0CJLkL%2FZzTg0rI5L2zys7ffLeG3uQvBkECezQpIfDOKqomVKgzl0zKoKTYPRWdvi19hBTihbRaw1HKdftuKG4VY6HRjNzcJZTv2m9Bcqs3eduPbikg0hLvhroLxzRI5aP37fgywToPa3x%2FWpBnVLxJdsNoLMtMT11Pl4RS62howtM53WxE8MG1GOui7aZtviATUi7V%2BwHCOMDRwMisfoxDlAIoMyHUrG%2Ftpi5XAe9qLteaA7H4siJyjX9y21MMirrIzJSMwaByOkZ2%2BWLOQHKO11guJuz42MfHju7hz8P88av9skG%2Fu9ESuMHHaDeZ0d50gCL6trU4LacH3WZPQEayjDa8dTIBjqkAfnvWu6H8zKpZc5YuwlgTmaXNdNvaviiP%2F%2B2V8zkQFznMeTBM8gaPYzR6G%2FpSRBonsHHL%2BPN0Ejsi4Dx%2BVe0xBjT0sKJKg41aaOtyrRJXEjqDMa3udUYeAv44MRnHrBSykAvDaOM%2F4sssC5i2KJzJZhRU%2FMzXRaGLBI71wVzGt06kDq42ciJLuSehSjK1RNWa4U3uwzxc0krWvgVR1ZdREpPvMM7&X-Amz-Signature=de22e90ef6affb6b4f2b4dcbadebb94ae16fed93dc94b8a57c8a3bb147e56447&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6WC6ZGG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQD1Nz7%2BzZ1TnVf%2F%2F8PYezBRu9AlbYs1Tp05KTDmj76tiwIhAPD4Rvx86AwkxI2UpawE5icRx5uKwyyaBjHgbvVZxZFBKv8DCEMQABoMNjM3NDIzMTgzODA1IgztjFg8fcVjHkMb%2F6kq3AMzAMqFs2RDd5f4CmwUgD4iLvg05iUb%2FIfEh3LApBMdo9CEeEEBmz2W6V%2BUOgiiZh1hYFs8e3t4Txog58C0a02HVSZ7GGA4vB1sCcb%2FmjUJintDVDa8G4kphvRSpbK6NCDlq4zDq89M3ulZKun361z200xOWBzZ7jY6C%2FPaQqooz0hgbd9niV0xXQCFItJqlTgDJ%2F2c0nGrVaZ5aFFTOg0WKwfETy7h7zssni6OAeMK3w9QZFkPTVgAIF6ATHpcDDodMtRsnU%2F4%2B2ccLAwT4%2BYxmWzS2kZB08yzH%2Bm0CJLkL%2FZzTg0rI5L2zys7ffLeG3uQvBkECezQpIfDOKqomVKgzl0zKoKTYPRWdvi19hBTihbRaw1HKdftuKG4VY6HRjNzcJZTv2m9Bcqs3eduPbikg0hLvhroLxzRI5aP37fgywToPa3x%2FWpBnVLxJdsNoLMtMT11Pl4RS62howtM53WxE8MG1GOui7aZtviATUi7V%2BwHCOMDRwMisfoxDlAIoMyHUrG%2Ftpi5XAe9qLteaA7H4siJyjX9y21MMirrIzJSMwaByOkZ2%2BWLOQHKO11guJuz42MfHju7hz8P88av9skG%2Fu9ESuMHHaDeZ0d50gCL6trU4LacH3WZPQEayjDa8dTIBjqkAfnvWu6H8zKpZc5YuwlgTmaXNdNvaviiP%2F%2B2V8zkQFznMeTBM8gaPYzR6G%2FpSRBonsHHL%2BPN0Ejsi4Dx%2BVe0xBjT0sKJKg41aaOtyrRJXEjqDMa3udUYeAv44MRnHrBSykAvDaOM%2F4sssC5i2KJzJZhRU%2FMzXRaGLBI71wVzGt06kDq42ciJLuSehSjK1RNWa4U3uwzxc0krWvgVR1ZdREpPvMM7&X-Amz-Signature=a9c4b598bef7faa105af0b9256d94bb9b43a66fb0630ebf8a55a58239162ac49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6WC6ZGG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQD1Nz7%2BzZ1TnVf%2F%2F8PYezBRu9AlbYs1Tp05KTDmj76tiwIhAPD4Rvx86AwkxI2UpawE5icRx5uKwyyaBjHgbvVZxZFBKv8DCEMQABoMNjM3NDIzMTgzODA1IgztjFg8fcVjHkMb%2F6kq3AMzAMqFs2RDd5f4CmwUgD4iLvg05iUb%2FIfEh3LApBMdo9CEeEEBmz2W6V%2BUOgiiZh1hYFs8e3t4Txog58C0a02HVSZ7GGA4vB1sCcb%2FmjUJintDVDa8G4kphvRSpbK6NCDlq4zDq89M3ulZKun361z200xOWBzZ7jY6C%2FPaQqooz0hgbd9niV0xXQCFItJqlTgDJ%2F2c0nGrVaZ5aFFTOg0WKwfETy7h7zssni6OAeMK3w9QZFkPTVgAIF6ATHpcDDodMtRsnU%2F4%2B2ccLAwT4%2BYxmWzS2kZB08yzH%2Bm0CJLkL%2FZzTg0rI5L2zys7ffLeG3uQvBkECezQpIfDOKqomVKgzl0zKoKTYPRWdvi19hBTihbRaw1HKdftuKG4VY6HRjNzcJZTv2m9Bcqs3eduPbikg0hLvhroLxzRI5aP37fgywToPa3x%2FWpBnVLxJdsNoLMtMT11Pl4RS62howtM53WxE8MG1GOui7aZtviATUi7V%2BwHCOMDRwMisfoxDlAIoMyHUrG%2Ftpi5XAe9qLteaA7H4siJyjX9y21MMirrIzJSMwaByOkZ2%2BWLOQHKO11guJuz42MfHju7hz8P88av9skG%2Fu9ESuMHHaDeZ0d50gCL6trU4LacH3WZPQEayjDa8dTIBjqkAfnvWu6H8zKpZc5YuwlgTmaXNdNvaviiP%2F%2B2V8zkQFznMeTBM8gaPYzR6G%2FpSRBonsHHL%2BPN0Ejsi4Dx%2BVe0xBjT0sKJKg41aaOtyrRJXEjqDMa3udUYeAv44MRnHrBSykAvDaOM%2F4sssC5i2KJzJZhRU%2FMzXRaGLBI71wVzGt06kDq42ciJLuSehSjK1RNWa4U3uwzxc0krWvgVR1ZdREpPvMM7&X-Amz-Signature=33e4a2e822b984f294362d0127f3572f65c4f2bbe642d72463d845014575541a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6WC6ZGG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQD1Nz7%2BzZ1TnVf%2F%2F8PYezBRu9AlbYs1Tp05KTDmj76tiwIhAPD4Rvx86AwkxI2UpawE5icRx5uKwyyaBjHgbvVZxZFBKv8DCEMQABoMNjM3NDIzMTgzODA1IgztjFg8fcVjHkMb%2F6kq3AMzAMqFs2RDd5f4CmwUgD4iLvg05iUb%2FIfEh3LApBMdo9CEeEEBmz2W6V%2BUOgiiZh1hYFs8e3t4Txog58C0a02HVSZ7GGA4vB1sCcb%2FmjUJintDVDa8G4kphvRSpbK6NCDlq4zDq89M3ulZKun361z200xOWBzZ7jY6C%2FPaQqooz0hgbd9niV0xXQCFItJqlTgDJ%2F2c0nGrVaZ5aFFTOg0WKwfETy7h7zssni6OAeMK3w9QZFkPTVgAIF6ATHpcDDodMtRsnU%2F4%2B2ccLAwT4%2BYxmWzS2kZB08yzH%2Bm0CJLkL%2FZzTg0rI5L2zys7ffLeG3uQvBkECezQpIfDOKqomVKgzl0zKoKTYPRWdvi19hBTihbRaw1HKdftuKG4VY6HRjNzcJZTv2m9Bcqs3eduPbikg0hLvhroLxzRI5aP37fgywToPa3x%2FWpBnVLxJdsNoLMtMT11Pl4RS62howtM53WxE8MG1GOui7aZtviATUi7V%2BwHCOMDRwMisfoxDlAIoMyHUrG%2Ftpi5XAe9qLteaA7H4siJyjX9y21MMirrIzJSMwaByOkZ2%2BWLOQHKO11guJuz42MfHju7hz8P88av9skG%2Fu9ESuMHHaDeZ0d50gCL6trU4LacH3WZPQEayjDa8dTIBjqkAfnvWu6H8zKpZc5YuwlgTmaXNdNvaviiP%2F%2B2V8zkQFznMeTBM8gaPYzR6G%2FpSRBonsHHL%2BPN0Ejsi4Dx%2BVe0xBjT0sKJKg41aaOtyrRJXEjqDMa3udUYeAv44MRnHrBSykAvDaOM%2F4sssC5i2KJzJZhRU%2FMzXRaGLBI71wVzGt06kDq42ciJLuSehSjK1RNWa4U3uwzxc0krWvgVR1ZdREpPvMM7&X-Amz-Signature=261332ba5310b3bf5bd2ac13d5c82341dff4b80e6f758f02dc5ed10a863c24ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



