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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UJGP6YS%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJv338oJD7Xe87KTh9XurRycrSCgYIz2utfoprbXgZQAIgZ0bQB3oiVZ9FbHpWdhXGjFsFGJThdg4ihcHdDyc1Xh8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0o1Dek4g7Yzn2fyrcAwAli6uXXG1Z2IFB1FLt9mEW75bvE2kGqy6VTudv6fEnRGnTi6MWzxgl%2FIgJ4IJ4jqyX6cdvHXS6YcM96f0qqr8XnL%2Fwmj%2BI6rQftwBZcvN3UsJ%2BCmr9cLN7d0G6h6hpLtysMlZCukek4PNc%2FREMSPTf3k%2BiE3lgYeUJ4RGLACWoiF32OS5qt5bjCP8rrnymlG86obPLaVegnW6x2h08j6PEkNWIoY6rmbStG%2BsuK1FJh%2Bl3PWCbSFzChhmuoG3iWkILvj0i1WHX7SxoprB7ZxaH6RR9YLNuDoy5Z4C%2FUvrhnbMocujBn3Kbld0CeeO10IdGPhc6s245KiCa66NrK4%2BjOXBo8KFQ7N130R%2F3XvshIrvHtq6Pobj3kftrrdvqxaVqFTRib7sw%2B6dMobo4y8Zsh8%2F4o5xhdewC6ewQT6sW5%2B8ySxmHVHNtasZAu86x4C9a4%2Fyo4Wa9%2FcoUAppFjNpu5%2ByT9y9cyZpM6isVgEvvTIavLnc%2BK3v9cm1MoUWhUpX%2Biq99Uqyd4oULgzAvFEP5N4VwohF1z6s32vU%2FQTYjq8pUj0aHf4WLreUcBS%2F5BSY4C4OZ90ENeyDRM8nEMGNJDNuEEyrwmRm14BqD8ze%2FmCZt9g01cGtMrXpaMNff5MgGOqUBqwW6E2anLvwtJHvfZN5Akc4EoUWIDL7c4TQ8P98FMAug8H5UsO0hWnmzfBGuwKjOOW3VGhpNbox4%2Fb5N1A0BcWepQoCoUtCXhTtYhQXCIJ1lEvrAIUTf8cw9IvTWYmLrP8cT4GJhf4zlHcud1%2BJsBRCnajLK42FiqDU21cEXmgdwMi%2FVKI8CQv6b%2BbPOGBAMP4pamnfMbe9YswRn8QNgxAJlPv4X&X-Amz-Signature=bbeb93377c37dd4b8d7c407242eae1cc9ca3a4735f8617466d5a43edfacfa528&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UJGP6YS%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJv338oJD7Xe87KTh9XurRycrSCgYIz2utfoprbXgZQAIgZ0bQB3oiVZ9FbHpWdhXGjFsFGJThdg4ihcHdDyc1Xh8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0o1Dek4g7Yzn2fyrcAwAli6uXXG1Z2IFB1FLt9mEW75bvE2kGqy6VTudv6fEnRGnTi6MWzxgl%2FIgJ4IJ4jqyX6cdvHXS6YcM96f0qqr8XnL%2Fwmj%2BI6rQftwBZcvN3UsJ%2BCmr9cLN7d0G6h6hpLtysMlZCukek4PNc%2FREMSPTf3k%2BiE3lgYeUJ4RGLACWoiF32OS5qt5bjCP8rrnymlG86obPLaVegnW6x2h08j6PEkNWIoY6rmbStG%2BsuK1FJh%2Bl3PWCbSFzChhmuoG3iWkILvj0i1WHX7SxoprB7ZxaH6RR9YLNuDoy5Z4C%2FUvrhnbMocujBn3Kbld0CeeO10IdGPhc6s245KiCa66NrK4%2BjOXBo8KFQ7N130R%2F3XvshIrvHtq6Pobj3kftrrdvqxaVqFTRib7sw%2B6dMobo4y8Zsh8%2F4o5xhdewC6ewQT6sW5%2B8ySxmHVHNtasZAu86x4C9a4%2Fyo4Wa9%2FcoUAppFjNpu5%2ByT9y9cyZpM6isVgEvvTIavLnc%2BK3v9cm1MoUWhUpX%2Biq99Uqyd4oULgzAvFEP5N4VwohF1z6s32vU%2FQTYjq8pUj0aHf4WLreUcBS%2F5BSY4C4OZ90ENeyDRM8nEMGNJDNuEEyrwmRm14BqD8ze%2FmCZt9g01cGtMrXpaMNff5MgGOqUBqwW6E2anLvwtJHvfZN5Akc4EoUWIDL7c4TQ8P98FMAug8H5UsO0hWnmzfBGuwKjOOW3VGhpNbox4%2Fb5N1A0BcWepQoCoUtCXhTtYhQXCIJ1lEvrAIUTf8cw9IvTWYmLrP8cT4GJhf4zlHcud1%2BJsBRCnajLK42FiqDU21cEXmgdwMi%2FVKI8CQv6b%2BbPOGBAMP4pamnfMbe9YswRn8QNgxAJlPv4X&X-Amz-Signature=74dabcac1ebb326227f02d5956835a945bfadaf5ea4fc0d73ff71e2f27626ecb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UJGP6YS%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJv338oJD7Xe87KTh9XurRycrSCgYIz2utfoprbXgZQAIgZ0bQB3oiVZ9FbHpWdhXGjFsFGJThdg4ihcHdDyc1Xh8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0o1Dek4g7Yzn2fyrcAwAli6uXXG1Z2IFB1FLt9mEW75bvE2kGqy6VTudv6fEnRGnTi6MWzxgl%2FIgJ4IJ4jqyX6cdvHXS6YcM96f0qqr8XnL%2Fwmj%2BI6rQftwBZcvN3UsJ%2BCmr9cLN7d0G6h6hpLtysMlZCukek4PNc%2FREMSPTf3k%2BiE3lgYeUJ4RGLACWoiF32OS5qt5bjCP8rrnymlG86obPLaVegnW6x2h08j6PEkNWIoY6rmbStG%2BsuK1FJh%2Bl3PWCbSFzChhmuoG3iWkILvj0i1WHX7SxoprB7ZxaH6RR9YLNuDoy5Z4C%2FUvrhnbMocujBn3Kbld0CeeO10IdGPhc6s245KiCa66NrK4%2BjOXBo8KFQ7N130R%2F3XvshIrvHtq6Pobj3kftrrdvqxaVqFTRib7sw%2B6dMobo4y8Zsh8%2F4o5xhdewC6ewQT6sW5%2B8ySxmHVHNtasZAu86x4C9a4%2Fyo4Wa9%2FcoUAppFjNpu5%2ByT9y9cyZpM6isVgEvvTIavLnc%2BK3v9cm1MoUWhUpX%2Biq99Uqyd4oULgzAvFEP5N4VwohF1z6s32vU%2FQTYjq8pUj0aHf4WLreUcBS%2F5BSY4C4OZ90ENeyDRM8nEMGNJDNuEEyrwmRm14BqD8ze%2FmCZt9g01cGtMrXpaMNff5MgGOqUBqwW6E2anLvwtJHvfZN5Akc4EoUWIDL7c4TQ8P98FMAug8H5UsO0hWnmzfBGuwKjOOW3VGhpNbox4%2Fb5N1A0BcWepQoCoUtCXhTtYhQXCIJ1lEvrAIUTf8cw9IvTWYmLrP8cT4GJhf4zlHcud1%2BJsBRCnajLK42FiqDU21cEXmgdwMi%2FVKI8CQv6b%2BbPOGBAMP4pamnfMbe9YswRn8QNgxAJlPv4X&X-Amz-Signature=2577ec5094ac2388a92863e5a134e0e2325f6bc77135b819982661a642e7ec18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UJGP6YS%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJv338oJD7Xe87KTh9XurRycrSCgYIz2utfoprbXgZQAIgZ0bQB3oiVZ9FbHpWdhXGjFsFGJThdg4ihcHdDyc1Xh8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAg0o1Dek4g7Yzn2fyrcAwAli6uXXG1Z2IFB1FLt9mEW75bvE2kGqy6VTudv6fEnRGnTi6MWzxgl%2FIgJ4IJ4jqyX6cdvHXS6YcM96f0qqr8XnL%2Fwmj%2BI6rQftwBZcvN3UsJ%2BCmr9cLN7d0G6h6hpLtysMlZCukek4PNc%2FREMSPTf3k%2BiE3lgYeUJ4RGLACWoiF32OS5qt5bjCP8rrnymlG86obPLaVegnW6x2h08j6PEkNWIoY6rmbStG%2BsuK1FJh%2Bl3PWCbSFzChhmuoG3iWkILvj0i1WHX7SxoprB7ZxaH6RR9YLNuDoy5Z4C%2FUvrhnbMocujBn3Kbld0CeeO10IdGPhc6s245KiCa66NrK4%2BjOXBo8KFQ7N130R%2F3XvshIrvHtq6Pobj3kftrrdvqxaVqFTRib7sw%2B6dMobo4y8Zsh8%2F4o5xhdewC6ewQT6sW5%2B8ySxmHVHNtasZAu86x4C9a4%2Fyo4Wa9%2FcoUAppFjNpu5%2ByT9y9cyZpM6isVgEvvTIavLnc%2BK3v9cm1MoUWhUpX%2Biq99Uqyd4oULgzAvFEP5N4VwohF1z6s32vU%2FQTYjq8pUj0aHf4WLreUcBS%2F5BSY4C4OZ90ENeyDRM8nEMGNJDNuEEyrwmRm14BqD8ze%2FmCZt9g01cGtMrXpaMNff5MgGOqUBqwW6E2anLvwtJHvfZN5Akc4EoUWIDL7c4TQ8P98FMAug8H5UsO0hWnmzfBGuwKjOOW3VGhpNbox4%2Fb5N1A0BcWepQoCoUtCXhTtYhQXCIJ1lEvrAIUTf8cw9IvTWYmLrP8cT4GJhf4zlHcud1%2BJsBRCnajLK42FiqDU21cEXmgdwMi%2FVKI8CQv6b%2BbPOGBAMP4pamnfMbe9YswRn8QNgxAJlPv4X&X-Amz-Signature=8ff5c560bc444d72251d78f1d7e2918f2cf42771badd884c6cc1ce8ad088810b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



