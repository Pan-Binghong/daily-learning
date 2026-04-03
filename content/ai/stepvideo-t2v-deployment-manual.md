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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLDHE7SE%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV%2FEnRvo8BJqwes8oALvXE5MPlw7zFwXbfE%2FlD4MKsrAIgEHuuXOYZyXZDXYOoTAQ4ji8TrVLUxrguqc5MlvnUfysq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFcxCvM0xOu36otdRircA55WklyfroS7YiyJdKk3vI%2FZeG96P4UrZbDRiTV4yaiKI76j68Dnni8IEhggpkpYCOEhRo5y4ezyXs9rM3P1p1Q4FOQJ%2F8zRnQE5vG9Kc4XSSTXP0TiK0piYI7EEVTy60UMT3AE6A0PKAvS7%2F35JoHUIfLImOFLlI8Q1pcFQJ4o5MpMw7PC2iBg0SYZc4vsT5bGkmmUSm%2FnKfxLBq4JIRGuxmXFRh2Kj6c9aaMTMxjTDgwsITewedxMEuIB0aeAwv8kZFrRr4mqXSueTCgmlykgCk4Ho8j3AITctPcPgtUbyNxkfO%2F%2Fowlxdvrtmcs5wieKf377DIlB1CW7PmI9I6zb4O8fXcTTxQEuu4Jv2Ry%2F%2F4h4q6BkbyYRPZe%2BeUHtkwk7G9h%2ByNJkbXuq44mywWUGqoI5%2FZ2Hvj4MzmKsoQsWEesFy3ixtzOXepyNw0qYlMhP92jEG3m5hpUGWae3F8uu5ONKaH0bz1sLB9FG4NDkqA963WOTP7Aj8GK7ict948oDJr6R9fT17%2B4KHRNYWB%2Bye46r%2B7xaR%2FFs0xezdIY9DFusPHh8%2B4btu%2Fmqir%2B%2BKhTuF7tH18ALonKNInEjd4R6AxFAiaiatBx5jxAhBNnHVh8Ul%2FQMSJFFKzzD9MIyvvc4GOqUBXJ4OLgVSWqWAGVFxRKakKGZFQXDsR%2F0JCM78EmuV7ygaGRjK8KQyU8d8UByJg1rIWncrF1AHnX%2Btwn5DFLMkc%2B15i6ZgmyVNrjKU%2F41QLy%2BVoer2Y1p0%2FW%2FItL7ck4SKTlP6YaXHS8MaB1DlxQarH84Vr9UicmF0FqHTLKHBSXhMyIXXfJvHjpPzhd8Xgf5RYqBnVbz3LzRynPEXWatLyrIl6F5C&X-Amz-Signature=f51cc7ebefbd3a1293df061fed2156fb1d8a4a9268cc3932e939cd0233a3d5d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLDHE7SE%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV%2FEnRvo8BJqwes8oALvXE5MPlw7zFwXbfE%2FlD4MKsrAIgEHuuXOYZyXZDXYOoTAQ4ji8TrVLUxrguqc5MlvnUfysq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFcxCvM0xOu36otdRircA55WklyfroS7YiyJdKk3vI%2FZeG96P4UrZbDRiTV4yaiKI76j68Dnni8IEhggpkpYCOEhRo5y4ezyXs9rM3P1p1Q4FOQJ%2F8zRnQE5vG9Kc4XSSTXP0TiK0piYI7EEVTy60UMT3AE6A0PKAvS7%2F35JoHUIfLImOFLlI8Q1pcFQJ4o5MpMw7PC2iBg0SYZc4vsT5bGkmmUSm%2FnKfxLBq4JIRGuxmXFRh2Kj6c9aaMTMxjTDgwsITewedxMEuIB0aeAwv8kZFrRr4mqXSueTCgmlykgCk4Ho8j3AITctPcPgtUbyNxkfO%2F%2Fowlxdvrtmcs5wieKf377DIlB1CW7PmI9I6zb4O8fXcTTxQEuu4Jv2Ry%2F%2F4h4q6BkbyYRPZe%2BeUHtkwk7G9h%2ByNJkbXuq44mywWUGqoI5%2FZ2Hvj4MzmKsoQsWEesFy3ixtzOXepyNw0qYlMhP92jEG3m5hpUGWae3F8uu5ONKaH0bz1sLB9FG4NDkqA963WOTP7Aj8GK7ict948oDJr6R9fT17%2B4KHRNYWB%2Bye46r%2B7xaR%2FFs0xezdIY9DFusPHh8%2B4btu%2Fmqir%2B%2BKhTuF7tH18ALonKNInEjd4R6AxFAiaiatBx5jxAhBNnHVh8Ul%2FQMSJFFKzzD9MIyvvc4GOqUBXJ4OLgVSWqWAGVFxRKakKGZFQXDsR%2F0JCM78EmuV7ygaGRjK8KQyU8d8UByJg1rIWncrF1AHnX%2Btwn5DFLMkc%2B15i6ZgmyVNrjKU%2F41QLy%2BVoer2Y1p0%2FW%2FItL7ck4SKTlP6YaXHS8MaB1DlxQarH84Vr9UicmF0FqHTLKHBSXhMyIXXfJvHjpPzhd8Xgf5RYqBnVbz3LzRynPEXWatLyrIl6F5C&X-Amz-Signature=c60494c1ecff0c7819e6b77b4c103c09e66b0250a1251d105eea7ed2e7240471&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLDHE7SE%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV%2FEnRvo8BJqwes8oALvXE5MPlw7zFwXbfE%2FlD4MKsrAIgEHuuXOYZyXZDXYOoTAQ4ji8TrVLUxrguqc5MlvnUfysq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFcxCvM0xOu36otdRircA55WklyfroS7YiyJdKk3vI%2FZeG96P4UrZbDRiTV4yaiKI76j68Dnni8IEhggpkpYCOEhRo5y4ezyXs9rM3P1p1Q4FOQJ%2F8zRnQE5vG9Kc4XSSTXP0TiK0piYI7EEVTy60UMT3AE6A0PKAvS7%2F35JoHUIfLImOFLlI8Q1pcFQJ4o5MpMw7PC2iBg0SYZc4vsT5bGkmmUSm%2FnKfxLBq4JIRGuxmXFRh2Kj6c9aaMTMxjTDgwsITewedxMEuIB0aeAwv8kZFrRr4mqXSueTCgmlykgCk4Ho8j3AITctPcPgtUbyNxkfO%2F%2Fowlxdvrtmcs5wieKf377DIlB1CW7PmI9I6zb4O8fXcTTxQEuu4Jv2Ry%2F%2F4h4q6BkbyYRPZe%2BeUHtkwk7G9h%2ByNJkbXuq44mywWUGqoI5%2FZ2Hvj4MzmKsoQsWEesFy3ixtzOXepyNw0qYlMhP92jEG3m5hpUGWae3F8uu5ONKaH0bz1sLB9FG4NDkqA963WOTP7Aj8GK7ict948oDJr6R9fT17%2B4KHRNYWB%2Bye46r%2B7xaR%2FFs0xezdIY9DFusPHh8%2B4btu%2Fmqir%2B%2BKhTuF7tH18ALonKNInEjd4R6AxFAiaiatBx5jxAhBNnHVh8Ul%2FQMSJFFKzzD9MIyvvc4GOqUBXJ4OLgVSWqWAGVFxRKakKGZFQXDsR%2F0JCM78EmuV7ygaGRjK8KQyU8d8UByJg1rIWncrF1AHnX%2Btwn5DFLMkc%2B15i6ZgmyVNrjKU%2F41QLy%2BVoer2Y1p0%2FW%2FItL7ck4SKTlP6YaXHS8MaB1DlxQarH84Vr9UicmF0FqHTLKHBSXhMyIXXfJvHjpPzhd8Xgf5RYqBnVbz3LzRynPEXWatLyrIl6F5C&X-Amz-Signature=3c9b28ff52fb38065e40b927bd3dcbd1dccf90f05efc74c2936d2f4ccc9b266d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLDHE7SE%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDV%2FEnRvo8BJqwes8oALvXE5MPlw7zFwXbfE%2FlD4MKsrAIgEHuuXOYZyXZDXYOoTAQ4ji8TrVLUxrguqc5MlvnUfysq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFcxCvM0xOu36otdRircA55WklyfroS7YiyJdKk3vI%2FZeG96P4UrZbDRiTV4yaiKI76j68Dnni8IEhggpkpYCOEhRo5y4ezyXs9rM3P1p1Q4FOQJ%2F8zRnQE5vG9Kc4XSSTXP0TiK0piYI7EEVTy60UMT3AE6A0PKAvS7%2F35JoHUIfLImOFLlI8Q1pcFQJ4o5MpMw7PC2iBg0SYZc4vsT5bGkmmUSm%2FnKfxLBq4JIRGuxmXFRh2Kj6c9aaMTMxjTDgwsITewedxMEuIB0aeAwv8kZFrRr4mqXSueTCgmlykgCk4Ho8j3AITctPcPgtUbyNxkfO%2F%2Fowlxdvrtmcs5wieKf377DIlB1CW7PmI9I6zb4O8fXcTTxQEuu4Jv2Ry%2F%2F4h4q6BkbyYRPZe%2BeUHtkwk7G9h%2ByNJkbXuq44mywWUGqoI5%2FZ2Hvj4MzmKsoQsWEesFy3ixtzOXepyNw0qYlMhP92jEG3m5hpUGWae3F8uu5ONKaH0bz1sLB9FG4NDkqA963WOTP7Aj8GK7ict948oDJr6R9fT17%2B4KHRNYWB%2Bye46r%2B7xaR%2FFs0xezdIY9DFusPHh8%2B4btu%2Fmqir%2B%2BKhTuF7tH18ALonKNInEjd4R6AxFAiaiatBx5jxAhBNnHVh8Ul%2FQMSJFFKzzD9MIyvvc4GOqUBXJ4OLgVSWqWAGVFxRKakKGZFQXDsR%2F0JCM78EmuV7ygaGRjK8KQyU8d8UByJg1rIWncrF1AHnX%2Btwn5DFLMkc%2B15i6ZgmyVNrjKU%2F41QLy%2BVoer2Y1p0%2FW%2FItL7ck4SKTlP6YaXHS8MaB1DlxQarH84Vr9UicmF0FqHTLKHBSXhMyIXXfJvHjpPzhd8Xgf5RYqBnVbz3LzRynPEXWatLyrIl6F5C&X-Amz-Signature=1c787bd237c0eef2298492d8223131407b969e831494c6f646219e4ecaf3482b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



