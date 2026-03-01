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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52S3MTE%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFPUdCTa4YoCy56mC%2B%2BAKqlKgAN1A6cnahbrxbLQR9ZAIhAOgMe0vBkfHh6jVvZz0KSXf5qfZZHcei1NYe8mPJH0ERKv8DCGQQABoMNjM3NDIzMTgzODA1Igw1DmJPJXo9Y9ftF8sq3AP5s56xHc7KrL%2Bg%2F7LnkuQU0Ooht4umbnYtNmrkiFlvGN3Z3IErivA8dwIZbqzI6Ev%2BAeJdg7HacgqW8Z2IFTJsrteyYyI8hAgDmNCusqYM6l4duFJqFUr0IuEJZp2IsSAFojLNjk61ze5SJ3HescAOPBfr3QkDEPyM7C8J%2B%2BdO7%2BeKGIZwioNpE6OeSoIV0cSH4I6TzaZKo4JQWwLDNfN9VuQhDC0rqGC5t40dPa%2FVWKJLv0gQyI8X77PM5AbzeE0DOk18Ew2hGNxW2kUd9DaSlWaI1U5pKSu%2FxFDf%2FPdd4FtWsAznsv5TR%2BTUSkk1rZd%2FshwKCrTuloYVmCyjPaPKXMbTtFlvwXR4tTk%2FWi9GmWYTSxT7ohr5%2FVSyxbyyD9YFaVub9hzttViswT%2FM%2BqKeq7EVJ7213AVmNfL4%2FWVGzpq1tR5UXPEOoa9ySxQwKc1GSWfpeyBhEmoIguR%2F5ho1yJcJWYPWnqOY4WScCmDLB9DGhoiJo8UuaoawZTxpA6rIHFDwdDhad5J2itZF2CGzDfjb7KrBBaai3GFHg3a94G3f4M8eEO1cKX9rVH6o47TBaif3obU1Blr2gVzjWFaiYd6ywR6MuYcKdPGtZ66RVOYqWMnMgWDaPHAF7DDbzY7NBjqkATCaWqriBWpMDFprW19tZv0BC4s8SzBUki12KasnPsv3BrQV8uueUwmGmha7VU2ct5l12FT0dsMbpC2dMnf7lWRh%2Boxh8g%2FM574firskHrIiRtmYDh%2BuMKWeBYidVCxHqQINokfE1Y6zXYO1BhO2DAYadDDqFA5%2BD6Ns%2BdNUyRWTi2YhOfspurT4m7AnFnW0MpzWcEerV7Q0sY1NmyTGiFSsg%2FbW&X-Amz-Signature=78d20d8fe8f9fb9180eaf942ab217572a320c944c7350dbb547a0629024b6700&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52S3MTE%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFPUdCTa4YoCy56mC%2B%2BAKqlKgAN1A6cnahbrxbLQR9ZAIhAOgMe0vBkfHh6jVvZz0KSXf5qfZZHcei1NYe8mPJH0ERKv8DCGQQABoMNjM3NDIzMTgzODA1Igw1DmJPJXo9Y9ftF8sq3AP5s56xHc7KrL%2Bg%2F7LnkuQU0Ooht4umbnYtNmrkiFlvGN3Z3IErivA8dwIZbqzI6Ev%2BAeJdg7HacgqW8Z2IFTJsrteyYyI8hAgDmNCusqYM6l4duFJqFUr0IuEJZp2IsSAFojLNjk61ze5SJ3HescAOPBfr3QkDEPyM7C8J%2B%2BdO7%2BeKGIZwioNpE6OeSoIV0cSH4I6TzaZKo4JQWwLDNfN9VuQhDC0rqGC5t40dPa%2FVWKJLv0gQyI8X77PM5AbzeE0DOk18Ew2hGNxW2kUd9DaSlWaI1U5pKSu%2FxFDf%2FPdd4FtWsAznsv5TR%2BTUSkk1rZd%2FshwKCrTuloYVmCyjPaPKXMbTtFlvwXR4tTk%2FWi9GmWYTSxT7ohr5%2FVSyxbyyD9YFaVub9hzttViswT%2FM%2BqKeq7EVJ7213AVmNfL4%2FWVGzpq1tR5UXPEOoa9ySxQwKc1GSWfpeyBhEmoIguR%2F5ho1yJcJWYPWnqOY4WScCmDLB9DGhoiJo8UuaoawZTxpA6rIHFDwdDhad5J2itZF2CGzDfjb7KrBBaai3GFHg3a94G3f4M8eEO1cKX9rVH6o47TBaif3obU1Blr2gVzjWFaiYd6ywR6MuYcKdPGtZ66RVOYqWMnMgWDaPHAF7DDbzY7NBjqkATCaWqriBWpMDFprW19tZv0BC4s8SzBUki12KasnPsv3BrQV8uueUwmGmha7VU2ct5l12FT0dsMbpC2dMnf7lWRh%2Boxh8g%2FM574firskHrIiRtmYDh%2BuMKWeBYidVCxHqQINokfE1Y6zXYO1BhO2DAYadDDqFA5%2BD6Ns%2BdNUyRWTi2YhOfspurT4m7AnFnW0MpzWcEerV7Q0sY1NmyTGiFSsg%2FbW&X-Amz-Signature=3c5d07ff93ea73131c76b1ca1fa5d33d95cba43746a925c52cb12cc0d8468acc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52S3MTE%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFPUdCTa4YoCy56mC%2B%2BAKqlKgAN1A6cnahbrxbLQR9ZAIhAOgMe0vBkfHh6jVvZz0KSXf5qfZZHcei1NYe8mPJH0ERKv8DCGQQABoMNjM3NDIzMTgzODA1Igw1DmJPJXo9Y9ftF8sq3AP5s56xHc7KrL%2Bg%2F7LnkuQU0Ooht4umbnYtNmrkiFlvGN3Z3IErivA8dwIZbqzI6Ev%2BAeJdg7HacgqW8Z2IFTJsrteyYyI8hAgDmNCusqYM6l4duFJqFUr0IuEJZp2IsSAFojLNjk61ze5SJ3HescAOPBfr3QkDEPyM7C8J%2B%2BdO7%2BeKGIZwioNpE6OeSoIV0cSH4I6TzaZKo4JQWwLDNfN9VuQhDC0rqGC5t40dPa%2FVWKJLv0gQyI8X77PM5AbzeE0DOk18Ew2hGNxW2kUd9DaSlWaI1U5pKSu%2FxFDf%2FPdd4FtWsAznsv5TR%2BTUSkk1rZd%2FshwKCrTuloYVmCyjPaPKXMbTtFlvwXR4tTk%2FWi9GmWYTSxT7ohr5%2FVSyxbyyD9YFaVub9hzttViswT%2FM%2BqKeq7EVJ7213AVmNfL4%2FWVGzpq1tR5UXPEOoa9ySxQwKc1GSWfpeyBhEmoIguR%2F5ho1yJcJWYPWnqOY4WScCmDLB9DGhoiJo8UuaoawZTxpA6rIHFDwdDhad5J2itZF2CGzDfjb7KrBBaai3GFHg3a94G3f4M8eEO1cKX9rVH6o47TBaif3obU1Blr2gVzjWFaiYd6ywR6MuYcKdPGtZ66RVOYqWMnMgWDaPHAF7DDbzY7NBjqkATCaWqriBWpMDFprW19tZv0BC4s8SzBUki12KasnPsv3BrQV8uueUwmGmha7VU2ct5l12FT0dsMbpC2dMnf7lWRh%2Boxh8g%2FM574firskHrIiRtmYDh%2BuMKWeBYidVCxHqQINokfE1Y6zXYO1BhO2DAYadDDqFA5%2BD6Ns%2BdNUyRWTi2YhOfspurT4m7AnFnW0MpzWcEerV7Q0sY1NmyTGiFSsg%2FbW&X-Amz-Signature=9798dbab6a894f9db1a33b3467e14cfe02d4e3532f4860e5688e3fc3454cdb92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52S3MTE%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFPUdCTa4YoCy56mC%2B%2BAKqlKgAN1A6cnahbrxbLQR9ZAIhAOgMe0vBkfHh6jVvZz0KSXf5qfZZHcei1NYe8mPJH0ERKv8DCGQQABoMNjM3NDIzMTgzODA1Igw1DmJPJXo9Y9ftF8sq3AP5s56xHc7KrL%2Bg%2F7LnkuQU0Ooht4umbnYtNmrkiFlvGN3Z3IErivA8dwIZbqzI6Ev%2BAeJdg7HacgqW8Z2IFTJsrteyYyI8hAgDmNCusqYM6l4duFJqFUr0IuEJZp2IsSAFojLNjk61ze5SJ3HescAOPBfr3QkDEPyM7C8J%2B%2BdO7%2BeKGIZwioNpE6OeSoIV0cSH4I6TzaZKo4JQWwLDNfN9VuQhDC0rqGC5t40dPa%2FVWKJLv0gQyI8X77PM5AbzeE0DOk18Ew2hGNxW2kUd9DaSlWaI1U5pKSu%2FxFDf%2FPdd4FtWsAznsv5TR%2BTUSkk1rZd%2FshwKCrTuloYVmCyjPaPKXMbTtFlvwXR4tTk%2FWi9GmWYTSxT7ohr5%2FVSyxbyyD9YFaVub9hzttViswT%2FM%2BqKeq7EVJ7213AVmNfL4%2FWVGzpq1tR5UXPEOoa9ySxQwKc1GSWfpeyBhEmoIguR%2F5ho1yJcJWYPWnqOY4WScCmDLB9DGhoiJo8UuaoawZTxpA6rIHFDwdDhad5J2itZF2CGzDfjb7KrBBaai3GFHg3a94G3f4M8eEO1cKX9rVH6o47TBaif3obU1Blr2gVzjWFaiYd6ywR6MuYcKdPGtZ66RVOYqWMnMgWDaPHAF7DDbzY7NBjqkATCaWqriBWpMDFprW19tZv0BC4s8SzBUki12KasnPsv3BrQV8uueUwmGmha7VU2ct5l12FT0dsMbpC2dMnf7lWRh%2Boxh8g%2FM574firskHrIiRtmYDh%2BuMKWeBYidVCxHqQINokfE1Y6zXYO1BhO2DAYadDDqFA5%2BD6Ns%2BdNUyRWTi2YhOfspurT4m7AnFnW0MpzWcEerV7Q0sY1NmyTGiFSsg%2FbW&X-Amz-Signature=c5219680fb9192ccff0464090afdc013bf247404c3cb6c383de1b9199022acb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



