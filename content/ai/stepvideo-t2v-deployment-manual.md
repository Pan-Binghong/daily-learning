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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A6CT5TW%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH68KNihuzoKy2islu%2F5XDM%2F%2BXU9FpXeB3hMzU3RjAffAiBYQ4RflSrn%2BldUYiG6acoIkGwRHXHr9wHLuNU1JAogyyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY0aWCTJm27lm698zKtwD57K7OLNKe4Jk9%2FiPWVCtB9zbqPG2wlChxFqyV4OWE5KtcKQzX4ghW%2FK0fqp9GvevrBp83Ogx5QMXDrF45pnY4XE379oqz7FA01lCm2YVnkEbH0HV30wiYJDLTUGQuZbdpvtgxkW%2BdWp%2B5EKhbK4K68bku3zBddLMfpN1wUDG%2F35pJaMawzLTIpncZVZqWwGzUq3lV%2BuuzokJC3FTu2ayn%2FG28oeLKXrDuR79UONaNcIWJsCSm4%2FHQkMjXAI7t19H9YQ7y0ezvQF0j8ZhklEMBjQJxnWR%2FSO4FVHYEkeb%2BAxPC2f0wuD7W9m2R7lSIkpumzvs5QnbKAkALOs65MLNN%2FwhB5AptId98vt7alCGNvnqAWmKt0oVweLK1wlVwPXT5nxJQivq4Dhv0nwpzBi86VeQx2BMlVcMAj3WgPItKXBIlPZUhjEfSyzqyH%2BF6vchzKfZTaNNY3Isw2N7otUPNIZTIbTgVEQyovt6cYUtW%2BqKrl4GDhAXQ%2F%2BTg24UrpV%2F6%2Fipxe5f03ZyWDIlAW0mUI0mvlHT4SjE199q0j3T3fnhh36L7tcjf%2BCox5MSg0n6Dy5rYvbUH3P5f0bShXYQMfKEnwL75GdrI5dZ7MuE56l2xm6sA4OrgYzROM0w1%2F3SyQY6pgEZaTosO%2F9u5SPB6H65GlveoWsUIhqWW%2B8Wil7%2BGIHNEYeNV4nErP6nAEmyUe%2FVALAu0RMSlq9UzoWInhuMFOFCJ9HHD2LR9f4koBznE7qdk1yBVy90ZPk3%2Fotaz567UUpHvxou6j5dQ7vDWKJXI2gWilzTWXIbxdsQU2eerWz5GutbwmXsUFhkrlS%2Bbw7Q4VIIGiEfme0Mn8%2B%2FRo%2BVbPLYCV53XlGo&X-Amz-Signature=ffef50541c194c7f23a08ac2f71a6eb72817ac4edbfe7b7d1f21a96fb837e8d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A6CT5TW%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH68KNihuzoKy2islu%2F5XDM%2F%2BXU9FpXeB3hMzU3RjAffAiBYQ4RflSrn%2BldUYiG6acoIkGwRHXHr9wHLuNU1JAogyyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY0aWCTJm27lm698zKtwD57K7OLNKe4Jk9%2FiPWVCtB9zbqPG2wlChxFqyV4OWE5KtcKQzX4ghW%2FK0fqp9GvevrBp83Ogx5QMXDrF45pnY4XE379oqz7FA01lCm2YVnkEbH0HV30wiYJDLTUGQuZbdpvtgxkW%2BdWp%2B5EKhbK4K68bku3zBddLMfpN1wUDG%2F35pJaMawzLTIpncZVZqWwGzUq3lV%2BuuzokJC3FTu2ayn%2FG28oeLKXrDuR79UONaNcIWJsCSm4%2FHQkMjXAI7t19H9YQ7y0ezvQF0j8ZhklEMBjQJxnWR%2FSO4FVHYEkeb%2BAxPC2f0wuD7W9m2R7lSIkpumzvs5QnbKAkALOs65MLNN%2FwhB5AptId98vt7alCGNvnqAWmKt0oVweLK1wlVwPXT5nxJQivq4Dhv0nwpzBi86VeQx2BMlVcMAj3WgPItKXBIlPZUhjEfSyzqyH%2BF6vchzKfZTaNNY3Isw2N7otUPNIZTIbTgVEQyovt6cYUtW%2BqKrl4GDhAXQ%2F%2BTg24UrpV%2F6%2Fipxe5f03ZyWDIlAW0mUI0mvlHT4SjE199q0j3T3fnhh36L7tcjf%2BCox5MSg0n6Dy5rYvbUH3P5f0bShXYQMfKEnwL75GdrI5dZ7MuE56l2xm6sA4OrgYzROM0w1%2F3SyQY6pgEZaTosO%2F9u5SPB6H65GlveoWsUIhqWW%2B8Wil7%2BGIHNEYeNV4nErP6nAEmyUe%2FVALAu0RMSlq9UzoWInhuMFOFCJ9HHD2LR9f4koBznE7qdk1yBVy90ZPk3%2Fotaz567UUpHvxou6j5dQ7vDWKJXI2gWilzTWXIbxdsQU2eerWz5GutbwmXsUFhkrlS%2Bbw7Q4VIIGiEfme0Mn8%2B%2FRo%2BVbPLYCV53XlGo&X-Amz-Signature=cb82a78f30463974568e166fcab4ad7a87e9e50132d1eb5df7d30bc51966d6c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A6CT5TW%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH68KNihuzoKy2islu%2F5XDM%2F%2BXU9FpXeB3hMzU3RjAffAiBYQ4RflSrn%2BldUYiG6acoIkGwRHXHr9wHLuNU1JAogyyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY0aWCTJm27lm698zKtwD57K7OLNKe4Jk9%2FiPWVCtB9zbqPG2wlChxFqyV4OWE5KtcKQzX4ghW%2FK0fqp9GvevrBp83Ogx5QMXDrF45pnY4XE379oqz7FA01lCm2YVnkEbH0HV30wiYJDLTUGQuZbdpvtgxkW%2BdWp%2B5EKhbK4K68bku3zBddLMfpN1wUDG%2F35pJaMawzLTIpncZVZqWwGzUq3lV%2BuuzokJC3FTu2ayn%2FG28oeLKXrDuR79UONaNcIWJsCSm4%2FHQkMjXAI7t19H9YQ7y0ezvQF0j8ZhklEMBjQJxnWR%2FSO4FVHYEkeb%2BAxPC2f0wuD7W9m2R7lSIkpumzvs5QnbKAkALOs65MLNN%2FwhB5AptId98vt7alCGNvnqAWmKt0oVweLK1wlVwPXT5nxJQivq4Dhv0nwpzBi86VeQx2BMlVcMAj3WgPItKXBIlPZUhjEfSyzqyH%2BF6vchzKfZTaNNY3Isw2N7otUPNIZTIbTgVEQyovt6cYUtW%2BqKrl4GDhAXQ%2F%2BTg24UrpV%2F6%2Fipxe5f03ZyWDIlAW0mUI0mvlHT4SjE199q0j3T3fnhh36L7tcjf%2BCox5MSg0n6Dy5rYvbUH3P5f0bShXYQMfKEnwL75GdrI5dZ7MuE56l2xm6sA4OrgYzROM0w1%2F3SyQY6pgEZaTosO%2F9u5SPB6H65GlveoWsUIhqWW%2B8Wil7%2BGIHNEYeNV4nErP6nAEmyUe%2FVALAu0RMSlq9UzoWInhuMFOFCJ9HHD2LR9f4koBznE7qdk1yBVy90ZPk3%2Fotaz567UUpHvxou6j5dQ7vDWKJXI2gWilzTWXIbxdsQU2eerWz5GutbwmXsUFhkrlS%2Bbw7Q4VIIGiEfme0Mn8%2B%2FRo%2BVbPLYCV53XlGo&X-Amz-Signature=9ecbb0f0ccc3774a63755ac3c4dcba2410a2ceced7f18bf6ac7afcc339d1f0b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A6CT5TW%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH68KNihuzoKy2islu%2F5XDM%2F%2BXU9FpXeB3hMzU3RjAffAiBYQ4RflSrn%2BldUYiG6acoIkGwRHXHr9wHLuNU1JAogyyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMY0aWCTJm27lm698zKtwD57K7OLNKe4Jk9%2FiPWVCtB9zbqPG2wlChxFqyV4OWE5KtcKQzX4ghW%2FK0fqp9GvevrBp83Ogx5QMXDrF45pnY4XE379oqz7FA01lCm2YVnkEbH0HV30wiYJDLTUGQuZbdpvtgxkW%2BdWp%2B5EKhbK4K68bku3zBddLMfpN1wUDG%2F35pJaMawzLTIpncZVZqWwGzUq3lV%2BuuzokJC3FTu2ayn%2FG28oeLKXrDuR79UONaNcIWJsCSm4%2FHQkMjXAI7t19H9YQ7y0ezvQF0j8ZhklEMBjQJxnWR%2FSO4FVHYEkeb%2BAxPC2f0wuD7W9m2R7lSIkpumzvs5QnbKAkALOs65MLNN%2FwhB5AptId98vt7alCGNvnqAWmKt0oVweLK1wlVwPXT5nxJQivq4Dhv0nwpzBi86VeQx2BMlVcMAj3WgPItKXBIlPZUhjEfSyzqyH%2BF6vchzKfZTaNNY3Isw2N7otUPNIZTIbTgVEQyovt6cYUtW%2BqKrl4GDhAXQ%2F%2BTg24UrpV%2F6%2Fipxe5f03ZyWDIlAW0mUI0mvlHT4SjE199q0j3T3fnhh36L7tcjf%2BCox5MSg0n6Dy5rYvbUH3P5f0bShXYQMfKEnwL75GdrI5dZ7MuE56l2xm6sA4OrgYzROM0w1%2F3SyQY6pgEZaTosO%2F9u5SPB6H65GlveoWsUIhqWW%2B8Wil7%2BGIHNEYeNV4nErP6nAEmyUe%2FVALAu0RMSlq9UzoWInhuMFOFCJ9HHD2LR9f4koBznE7qdk1yBVy90ZPk3%2Fotaz567UUpHvxou6j5dQ7vDWKJXI2gWilzTWXIbxdsQU2eerWz5GutbwmXsUFhkrlS%2Bbw7Q4VIIGiEfme0Mn8%2B%2FRo%2BVbPLYCV53XlGo&X-Amz-Signature=93f4b7c6ca30d1921b92fa052cd0fb3c55898863107f0d71b07320ed6b3367d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



