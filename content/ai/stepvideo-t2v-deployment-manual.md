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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GOCVP7W%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEjMzOU%2BH%2BLcABYUM3S%2BX48KcwmEwrbrOdPPAHsgUQBpAiEAs8pk55B1InYIhVwztNy7Bzo%2BUSYwFgsdYUsFfVwEzkwq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDMD%2F8jDBwLd8oCgcnCrcAwW74rZ%2FJIXcZXbmCD5t68jjz0MasFUddDIxob8jKHXYlzwYtNoiW%2FvLAUQsSYfLYs37wXb3R1cf9TrwSjE3mD57Wp0GQJpwW464S1n2fPSPT8iwxUhFFgVC2LhOstprw3FkX7YhObFxxuFzOdUZmrtEkZieuW9ZvsTN7QKk1NQypdU9hiZNZfJFjeG10tXOcFhx7Sj6sv7sEu2jyd3Ty3%2BigAsxHD7b6CSzm6tU6FfLIz32RHGPqVJGzUp%2BkgT8q0Jd3he6isziRT24psitVFJPWGqNjDHQ%2F08zYWenhvUxUGBDoWzWu%2FvvkdVHNk%2FMUOBAUF%2BE%2BIp5C3ZnOd3h%2B0rL1YRKz2bdBaSYCH5hUodk%2F6PlBu1U1Y41BmZwvF3DNUP0mi25FkRv0sHXLSVpp%2Fg2lsDi6UCiFDXq0U36qhRXAc%2FZaf4vJzz7R1LYgz9C%2B8ftdTmzOF%2FP%2FKrGl%2B9huy1QqcIyb45RoVaTIsFPdzvu0w9SYpA6SFpv8yGQJ9Fs0G1Jzs68TVT%2B%2Fq8bxZxBvuKVshpFGcgAv5h3l%2BGmQOmH4i79zuWDCs%2BJkps51zp51RzvSN3aXrIKJK%2FjJuUH5ItoWZFeDSJmcGSHIVvDjE3jhKyp1SgO8oDFRjypMIa%2Fos4GOqUB27tuGnWfOLbbFKK%2FCwcvZM9k3M0E%2BYGDZ7PFc58JPEKnwvHsVLt%2Fj%2FcCe5A5M3n6MzYdGUq0K0tIPAcqUSpV2qTKhpRF28GCt0IsQ6EoHCqGcyEd5sSSf6yMu0Q%2Baa8MpntTz%2BW6YFdvFJhHcs2ALbeDt5F30xSmZaQOHIOIrBhHM8q%2BF3JamXnUm%2B%2F17HlyjmzOrLg8NRX3ldf9hYG%2BsbyGJhmf&X-Amz-Signature=a744f3d3950e10516122fe3ad5ec89cf002e1e6e2f6b58bac291d24af3e8001d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GOCVP7W%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEjMzOU%2BH%2BLcABYUM3S%2BX48KcwmEwrbrOdPPAHsgUQBpAiEAs8pk55B1InYIhVwztNy7Bzo%2BUSYwFgsdYUsFfVwEzkwq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDMD%2F8jDBwLd8oCgcnCrcAwW74rZ%2FJIXcZXbmCD5t68jjz0MasFUddDIxob8jKHXYlzwYtNoiW%2FvLAUQsSYfLYs37wXb3R1cf9TrwSjE3mD57Wp0GQJpwW464S1n2fPSPT8iwxUhFFgVC2LhOstprw3FkX7YhObFxxuFzOdUZmrtEkZieuW9ZvsTN7QKk1NQypdU9hiZNZfJFjeG10tXOcFhx7Sj6sv7sEu2jyd3Ty3%2BigAsxHD7b6CSzm6tU6FfLIz32RHGPqVJGzUp%2BkgT8q0Jd3he6isziRT24psitVFJPWGqNjDHQ%2F08zYWenhvUxUGBDoWzWu%2FvvkdVHNk%2FMUOBAUF%2BE%2BIp5C3ZnOd3h%2B0rL1YRKz2bdBaSYCH5hUodk%2F6PlBu1U1Y41BmZwvF3DNUP0mi25FkRv0sHXLSVpp%2Fg2lsDi6UCiFDXq0U36qhRXAc%2FZaf4vJzz7R1LYgz9C%2B8ftdTmzOF%2FP%2FKrGl%2B9huy1QqcIyb45RoVaTIsFPdzvu0w9SYpA6SFpv8yGQJ9Fs0G1Jzs68TVT%2B%2Fq8bxZxBvuKVshpFGcgAv5h3l%2BGmQOmH4i79zuWDCs%2BJkps51zp51RzvSN3aXrIKJK%2FjJuUH5ItoWZFeDSJmcGSHIVvDjE3jhKyp1SgO8oDFRjypMIa%2Fos4GOqUB27tuGnWfOLbbFKK%2FCwcvZM9k3M0E%2BYGDZ7PFc58JPEKnwvHsVLt%2Fj%2FcCe5A5M3n6MzYdGUq0K0tIPAcqUSpV2qTKhpRF28GCt0IsQ6EoHCqGcyEd5sSSf6yMu0Q%2Baa8MpntTz%2BW6YFdvFJhHcs2ALbeDt5F30xSmZaQOHIOIrBhHM8q%2BF3JamXnUm%2B%2F17HlyjmzOrLg8NRX3ldf9hYG%2BsbyGJhmf&X-Amz-Signature=a6f2b078ba498494ae95fc883e88c3c8f6e1d71b2eadf9b3124037b01526102d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GOCVP7W%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEjMzOU%2BH%2BLcABYUM3S%2BX48KcwmEwrbrOdPPAHsgUQBpAiEAs8pk55B1InYIhVwztNy7Bzo%2BUSYwFgsdYUsFfVwEzkwq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDMD%2F8jDBwLd8oCgcnCrcAwW74rZ%2FJIXcZXbmCD5t68jjz0MasFUddDIxob8jKHXYlzwYtNoiW%2FvLAUQsSYfLYs37wXb3R1cf9TrwSjE3mD57Wp0GQJpwW464S1n2fPSPT8iwxUhFFgVC2LhOstprw3FkX7YhObFxxuFzOdUZmrtEkZieuW9ZvsTN7QKk1NQypdU9hiZNZfJFjeG10tXOcFhx7Sj6sv7sEu2jyd3Ty3%2BigAsxHD7b6CSzm6tU6FfLIz32RHGPqVJGzUp%2BkgT8q0Jd3he6isziRT24psitVFJPWGqNjDHQ%2F08zYWenhvUxUGBDoWzWu%2FvvkdVHNk%2FMUOBAUF%2BE%2BIp5C3ZnOd3h%2B0rL1YRKz2bdBaSYCH5hUodk%2F6PlBu1U1Y41BmZwvF3DNUP0mi25FkRv0sHXLSVpp%2Fg2lsDi6UCiFDXq0U36qhRXAc%2FZaf4vJzz7R1LYgz9C%2B8ftdTmzOF%2FP%2FKrGl%2B9huy1QqcIyb45RoVaTIsFPdzvu0w9SYpA6SFpv8yGQJ9Fs0G1Jzs68TVT%2B%2Fq8bxZxBvuKVshpFGcgAv5h3l%2BGmQOmH4i79zuWDCs%2BJkps51zp51RzvSN3aXrIKJK%2FjJuUH5ItoWZFeDSJmcGSHIVvDjE3jhKyp1SgO8oDFRjypMIa%2Fos4GOqUB27tuGnWfOLbbFKK%2FCwcvZM9k3M0E%2BYGDZ7PFc58JPEKnwvHsVLt%2Fj%2FcCe5A5M3n6MzYdGUq0K0tIPAcqUSpV2qTKhpRF28GCt0IsQ6EoHCqGcyEd5sSSf6yMu0Q%2Baa8MpntTz%2BW6YFdvFJhHcs2ALbeDt5F30xSmZaQOHIOIrBhHM8q%2BF3JamXnUm%2B%2F17HlyjmzOrLg8NRX3ldf9hYG%2BsbyGJhmf&X-Amz-Signature=1939bcccb847f716d15b1685e89b2906ea9e73354d2a106cbaa837e6c9d3060f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GOCVP7W%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEjMzOU%2BH%2BLcABYUM3S%2BX48KcwmEwrbrOdPPAHsgUQBpAiEAs8pk55B1InYIhVwztNy7Bzo%2BUSYwFgsdYUsFfVwEzkwq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDMD%2F8jDBwLd8oCgcnCrcAwW74rZ%2FJIXcZXbmCD5t68jjz0MasFUddDIxob8jKHXYlzwYtNoiW%2FvLAUQsSYfLYs37wXb3R1cf9TrwSjE3mD57Wp0GQJpwW464S1n2fPSPT8iwxUhFFgVC2LhOstprw3FkX7YhObFxxuFzOdUZmrtEkZieuW9ZvsTN7QKk1NQypdU9hiZNZfJFjeG10tXOcFhx7Sj6sv7sEu2jyd3Ty3%2BigAsxHD7b6CSzm6tU6FfLIz32RHGPqVJGzUp%2BkgT8q0Jd3he6isziRT24psitVFJPWGqNjDHQ%2F08zYWenhvUxUGBDoWzWu%2FvvkdVHNk%2FMUOBAUF%2BE%2BIp5C3ZnOd3h%2B0rL1YRKz2bdBaSYCH5hUodk%2F6PlBu1U1Y41BmZwvF3DNUP0mi25FkRv0sHXLSVpp%2Fg2lsDi6UCiFDXq0U36qhRXAc%2FZaf4vJzz7R1LYgz9C%2B8ftdTmzOF%2FP%2FKrGl%2B9huy1QqcIyb45RoVaTIsFPdzvu0w9SYpA6SFpv8yGQJ9Fs0G1Jzs68TVT%2B%2Fq8bxZxBvuKVshpFGcgAv5h3l%2BGmQOmH4i79zuWDCs%2BJkps51zp51RzvSN3aXrIKJK%2FjJuUH5ItoWZFeDSJmcGSHIVvDjE3jhKyp1SgO8oDFRjypMIa%2Fos4GOqUB27tuGnWfOLbbFKK%2FCwcvZM9k3M0E%2BYGDZ7PFc58JPEKnwvHsVLt%2Fj%2FcCe5A5M3n6MzYdGUq0K0tIPAcqUSpV2qTKhpRF28GCt0IsQ6EoHCqGcyEd5sSSf6yMu0Q%2Baa8MpntTz%2BW6YFdvFJhHcs2ALbeDt5F30xSmZaQOHIOIrBhHM8q%2BF3JamXnUm%2B%2F17HlyjmzOrLg8NRX3ldf9hYG%2BsbyGJhmf&X-Amz-Signature=5bbe2f890b895403961423189fe661eaa10fc7e6188e35a3ccf3e5509e38a0a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



