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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXSIXACQ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr5%2F3UUUE81sPWGV3oSaOtYtj9oN589MGIBs8IOb1%2BUwIhAN7ix8Gh60EHjN17KEMTIxuCdhtOUFRIEIWUrGnQZeM7KogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbraUxXtL4HKHSM8Iq3APfr3UV9BVHOYV4w4X6jhXY6ZIElL4IyeHeaf%2Br2GssZweQvGpp3jmJ5LgT4fy%2FI1WgKrV5uKOCUYvtYz0mXNKt4TvCIvmoSWYZrK1I4t08YVEowIKhFowIwmWJZ29tpEe0o8KHdiy6bxjDUukICEuD96L4b5piOHcFGGU500ORSrrttfCWHHseA%2BrGdyDMQNz%2B21RnhBNtLlpCKUeNETlON7dzctnVBawJ9UkJT3lU5j4eIUOdmRtWUVID%2B1D5tCv8DCKzmLus0dr5yhtK2oI2bD8lhXLXU2nBaTxOyXzaAEmf5D77J3Pv195E7NnyzItlRo3OVeJv2qJIEwXdbJKJ%2BHOfUvhdEzi66%2FeXrscgyUwI0fwRU8m6bUQk59Wg2ktCguh7KEUh1brM8VcWueqZEplZVIXyAzqR1y%2BaSQjuR2wyYPjqRm%2BIejXmUISAUf1jgp7n%2FARYCL5Z9EreDkLQ0KhegWxAkI%2B7Xy5Oyk84fMwnp7jFhSRw28iLUy6uHbqmoBYJMkHBonWPajCCbSqOr1T85pO%2FrIxo5s3PXM8b1ywf%2BjKg69rPNopIjt6E9cd1%2F2bWaEDTHQoob4AQj%2FRoNZSGyw3EYxXllVQzvZBHtMlWtuT00KmOXzZW4DD9jrbPBjqkAfgyvWF%2Fey4B7kuFl6npnVxgUdkAAVq5XNKaQZ5VzeNoktKVmPvOrgam%2BPorroNCPfkhmbnERq%2B%2FD0IfsWXyyrQDOWHEcZWcnfshoINnUjwJkIzS8lx3kjcnkyraeJ6uxRrLvJ7QLgWy2Fy5KiK%2BdKUXvH11NZJltdNEXLJ570wrJPfkanz7PIUxZNYrAwOJetIsRCVwOOFs9ATB5iZ%2Bl9Ky5Uwo&X-Amz-Signature=5caeeddf006691aa72b5f1664664da02039c230de1ff43fbd6e4c7cdd1308a7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXSIXACQ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr5%2F3UUUE81sPWGV3oSaOtYtj9oN589MGIBs8IOb1%2BUwIhAN7ix8Gh60EHjN17KEMTIxuCdhtOUFRIEIWUrGnQZeM7KogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbraUxXtL4HKHSM8Iq3APfr3UV9BVHOYV4w4X6jhXY6ZIElL4IyeHeaf%2Br2GssZweQvGpp3jmJ5LgT4fy%2FI1WgKrV5uKOCUYvtYz0mXNKt4TvCIvmoSWYZrK1I4t08YVEowIKhFowIwmWJZ29tpEe0o8KHdiy6bxjDUukICEuD96L4b5piOHcFGGU500ORSrrttfCWHHseA%2BrGdyDMQNz%2B21RnhBNtLlpCKUeNETlON7dzctnVBawJ9UkJT3lU5j4eIUOdmRtWUVID%2B1D5tCv8DCKzmLus0dr5yhtK2oI2bD8lhXLXU2nBaTxOyXzaAEmf5D77J3Pv195E7NnyzItlRo3OVeJv2qJIEwXdbJKJ%2BHOfUvhdEzi66%2FeXrscgyUwI0fwRU8m6bUQk59Wg2ktCguh7KEUh1brM8VcWueqZEplZVIXyAzqR1y%2BaSQjuR2wyYPjqRm%2BIejXmUISAUf1jgp7n%2FARYCL5Z9EreDkLQ0KhegWxAkI%2B7Xy5Oyk84fMwnp7jFhSRw28iLUy6uHbqmoBYJMkHBonWPajCCbSqOr1T85pO%2FrIxo5s3PXM8b1ywf%2BjKg69rPNopIjt6E9cd1%2F2bWaEDTHQoob4AQj%2FRoNZSGyw3EYxXllVQzvZBHtMlWtuT00KmOXzZW4DD9jrbPBjqkAfgyvWF%2Fey4B7kuFl6npnVxgUdkAAVq5XNKaQZ5VzeNoktKVmPvOrgam%2BPorroNCPfkhmbnERq%2B%2FD0IfsWXyyrQDOWHEcZWcnfshoINnUjwJkIzS8lx3kjcnkyraeJ6uxRrLvJ7QLgWy2Fy5KiK%2BdKUXvH11NZJltdNEXLJ570wrJPfkanz7PIUxZNYrAwOJetIsRCVwOOFs9ATB5iZ%2Bl9Ky5Uwo&X-Amz-Signature=dff06f40c9f78a003ce68d64109cf4ef97978f492f38b71988327211fe73e821&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXSIXACQ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr5%2F3UUUE81sPWGV3oSaOtYtj9oN589MGIBs8IOb1%2BUwIhAN7ix8Gh60EHjN17KEMTIxuCdhtOUFRIEIWUrGnQZeM7KogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbraUxXtL4HKHSM8Iq3APfr3UV9BVHOYV4w4X6jhXY6ZIElL4IyeHeaf%2Br2GssZweQvGpp3jmJ5LgT4fy%2FI1WgKrV5uKOCUYvtYz0mXNKt4TvCIvmoSWYZrK1I4t08YVEowIKhFowIwmWJZ29tpEe0o8KHdiy6bxjDUukICEuD96L4b5piOHcFGGU500ORSrrttfCWHHseA%2BrGdyDMQNz%2B21RnhBNtLlpCKUeNETlON7dzctnVBawJ9UkJT3lU5j4eIUOdmRtWUVID%2B1D5tCv8DCKzmLus0dr5yhtK2oI2bD8lhXLXU2nBaTxOyXzaAEmf5D77J3Pv195E7NnyzItlRo3OVeJv2qJIEwXdbJKJ%2BHOfUvhdEzi66%2FeXrscgyUwI0fwRU8m6bUQk59Wg2ktCguh7KEUh1brM8VcWueqZEplZVIXyAzqR1y%2BaSQjuR2wyYPjqRm%2BIejXmUISAUf1jgp7n%2FARYCL5Z9EreDkLQ0KhegWxAkI%2B7Xy5Oyk84fMwnp7jFhSRw28iLUy6uHbqmoBYJMkHBonWPajCCbSqOr1T85pO%2FrIxo5s3PXM8b1ywf%2BjKg69rPNopIjt6E9cd1%2F2bWaEDTHQoob4AQj%2FRoNZSGyw3EYxXllVQzvZBHtMlWtuT00KmOXzZW4DD9jrbPBjqkAfgyvWF%2Fey4B7kuFl6npnVxgUdkAAVq5XNKaQZ5VzeNoktKVmPvOrgam%2BPorroNCPfkhmbnERq%2B%2FD0IfsWXyyrQDOWHEcZWcnfshoINnUjwJkIzS8lx3kjcnkyraeJ6uxRrLvJ7QLgWy2Fy5KiK%2BdKUXvH11NZJltdNEXLJ570wrJPfkanz7PIUxZNYrAwOJetIsRCVwOOFs9ATB5iZ%2Bl9Ky5Uwo&X-Amz-Signature=8a9d514a1725a34ba615b6373e563eed4d6ff24fd97278ad5a033e02809ac4ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXSIXACQ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDr5%2F3UUUE81sPWGV3oSaOtYtj9oN589MGIBs8IOb1%2BUwIhAN7ix8Gh60EHjN17KEMTIxuCdhtOUFRIEIWUrGnQZeM7KogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbraUxXtL4HKHSM8Iq3APfr3UV9BVHOYV4w4X6jhXY6ZIElL4IyeHeaf%2Br2GssZweQvGpp3jmJ5LgT4fy%2FI1WgKrV5uKOCUYvtYz0mXNKt4TvCIvmoSWYZrK1I4t08YVEowIKhFowIwmWJZ29tpEe0o8KHdiy6bxjDUukICEuD96L4b5piOHcFGGU500ORSrrttfCWHHseA%2BrGdyDMQNz%2B21RnhBNtLlpCKUeNETlON7dzctnVBawJ9UkJT3lU5j4eIUOdmRtWUVID%2B1D5tCv8DCKzmLus0dr5yhtK2oI2bD8lhXLXU2nBaTxOyXzaAEmf5D77J3Pv195E7NnyzItlRo3OVeJv2qJIEwXdbJKJ%2BHOfUvhdEzi66%2FeXrscgyUwI0fwRU8m6bUQk59Wg2ktCguh7KEUh1brM8VcWueqZEplZVIXyAzqR1y%2BaSQjuR2wyYPjqRm%2BIejXmUISAUf1jgp7n%2FARYCL5Z9EreDkLQ0KhegWxAkI%2B7Xy5Oyk84fMwnp7jFhSRw28iLUy6uHbqmoBYJMkHBonWPajCCbSqOr1T85pO%2FrIxo5s3PXM8b1ywf%2BjKg69rPNopIjt6E9cd1%2F2bWaEDTHQoob4AQj%2FRoNZSGyw3EYxXllVQzvZBHtMlWtuT00KmOXzZW4DD9jrbPBjqkAfgyvWF%2Fey4B7kuFl6npnVxgUdkAAVq5XNKaQZ5VzeNoktKVmPvOrgam%2BPorroNCPfkhmbnERq%2B%2FD0IfsWXyyrQDOWHEcZWcnfshoINnUjwJkIzS8lx3kjcnkyraeJ6uxRrLvJ7QLgWy2Fy5KiK%2BdKUXvH11NZJltdNEXLJ570wrJPfkanz7PIUxZNYrAwOJetIsRCVwOOFs9ATB5iZ%2Bl9Ky5Uwo&X-Amz-Signature=708f62d1fa296b525576f99aee12bd5d1e8bffcfaf4cd17ff76493e9a0ec9b89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



