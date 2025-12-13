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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJ3RV2HQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDrFOJTmLthWgLgp0q6np6H8L1zbinJFGPnm8WYsUvd3gIhAMvZjsZaLDPLJl4i%2B66Bt1clP1dAiCoYiO2SG8EX1pFEKv8DCBMQABoMNjM3NDIzMTgzODA1Igx9DC4iZCS68WwGzVgq3ANd%2F%2FMeIW%2BwuMVqh9Z4tzDcizyue5FhnCf9fDjyNBB5AIyvISRvib8XFseeoJ9i1hBfOzfrf1ra1XUH8ZnrJ%2BIWHPZTnSMenPTFutDP%2B7fhZJ1QUBffdT1mMifWW5xtjm0nsVSunbkTktxNY1ZCucdalBXAETRlhZ3VShZ8K6zh%2Binw90tacCk9fMJwj%2BK3c9oyN2KWAWLhNaexA4sCILiCIA9wSy3kUN3r16KspeLL2z9CxJC4OMOibJZsQxa53kKWM0JZrdTa0iBt5Wa2%2FbLX2D3u3ByXDvJeBPO9ty7hY80hjeQpd%2F8QzIVnVJXfQOfccBd9bVsMu5zrl0XGkzUySVAeiLWMmi9T3AfWJLkU2YHxsxl0uQPdqjdxYEqeJLSPxhxTHstSluq1p5ccE0r%2F9BV4F1aT8ZcZl3ULryX7E0laweU1vVDo%2BaCNMq2MaxeF%2Ffi7K381lGwb99Wt7DFIKHOIy6zw7%2BNOp29M0NPFKnasipj3dZQXMCAOwDYtNDDc99ez8ol5FubNb4SRke21HUWKt4ARBbaxX4g22W14u3%2FkavofMNlpjjuq7QX%2FoGe%2BdLzRhd7EYzDVpMOOyKU4NKOWQ%2B0waQJ8y8db5LzAgtLoV0vrJFO9VToqrTCJjfPJBjqkAYdoR9%2BqxhadsLmouvtjMerOo%2FT8u5eq1ym206%2Fi6jSZnGk547GfYjZXwnxn03r%2FzGXNZG3f3z7H%2F1FSSbEFHRRHNtuI%2BT0NJ32YHCMtNX9xuy0EV9ldr8qnXNKm%2Biiur5Z5aVXCspRP9Pdfp6JGE2bMAOrSxgGUV%2FmX5lSiJBbXbqbiXcyHpSG8prwEE4MkjtCqWX2FKMA9xXJrBBYE%2Fejka6rI&X-Amz-Signature=6567ff622be337a399e52c0677e7d88adf5401e3c58b5e4003979ce06e6dab1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJ3RV2HQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDrFOJTmLthWgLgp0q6np6H8L1zbinJFGPnm8WYsUvd3gIhAMvZjsZaLDPLJl4i%2B66Bt1clP1dAiCoYiO2SG8EX1pFEKv8DCBMQABoMNjM3NDIzMTgzODA1Igx9DC4iZCS68WwGzVgq3ANd%2F%2FMeIW%2BwuMVqh9Z4tzDcizyue5FhnCf9fDjyNBB5AIyvISRvib8XFseeoJ9i1hBfOzfrf1ra1XUH8ZnrJ%2BIWHPZTnSMenPTFutDP%2B7fhZJ1QUBffdT1mMifWW5xtjm0nsVSunbkTktxNY1ZCucdalBXAETRlhZ3VShZ8K6zh%2Binw90tacCk9fMJwj%2BK3c9oyN2KWAWLhNaexA4sCILiCIA9wSy3kUN3r16KspeLL2z9CxJC4OMOibJZsQxa53kKWM0JZrdTa0iBt5Wa2%2FbLX2D3u3ByXDvJeBPO9ty7hY80hjeQpd%2F8QzIVnVJXfQOfccBd9bVsMu5zrl0XGkzUySVAeiLWMmi9T3AfWJLkU2YHxsxl0uQPdqjdxYEqeJLSPxhxTHstSluq1p5ccE0r%2F9BV4F1aT8ZcZl3ULryX7E0laweU1vVDo%2BaCNMq2MaxeF%2Ffi7K381lGwb99Wt7DFIKHOIy6zw7%2BNOp29M0NPFKnasipj3dZQXMCAOwDYtNDDc99ez8ol5FubNb4SRke21HUWKt4ARBbaxX4g22W14u3%2FkavofMNlpjjuq7QX%2FoGe%2BdLzRhd7EYzDVpMOOyKU4NKOWQ%2B0waQJ8y8db5LzAgtLoV0vrJFO9VToqrTCJjfPJBjqkAYdoR9%2BqxhadsLmouvtjMerOo%2FT8u5eq1ym206%2Fi6jSZnGk547GfYjZXwnxn03r%2FzGXNZG3f3z7H%2F1FSSbEFHRRHNtuI%2BT0NJ32YHCMtNX9xuy0EV9ldr8qnXNKm%2Biiur5Z5aVXCspRP9Pdfp6JGE2bMAOrSxgGUV%2FmX5lSiJBbXbqbiXcyHpSG8prwEE4MkjtCqWX2FKMA9xXJrBBYE%2Fejka6rI&X-Amz-Signature=d37c47e1d05783f24cbb457b749b87a67aa1688d98024a0c98a070124a93eb1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJ3RV2HQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDrFOJTmLthWgLgp0q6np6H8L1zbinJFGPnm8WYsUvd3gIhAMvZjsZaLDPLJl4i%2B66Bt1clP1dAiCoYiO2SG8EX1pFEKv8DCBMQABoMNjM3NDIzMTgzODA1Igx9DC4iZCS68WwGzVgq3ANd%2F%2FMeIW%2BwuMVqh9Z4tzDcizyue5FhnCf9fDjyNBB5AIyvISRvib8XFseeoJ9i1hBfOzfrf1ra1XUH8ZnrJ%2BIWHPZTnSMenPTFutDP%2B7fhZJ1QUBffdT1mMifWW5xtjm0nsVSunbkTktxNY1ZCucdalBXAETRlhZ3VShZ8K6zh%2Binw90tacCk9fMJwj%2BK3c9oyN2KWAWLhNaexA4sCILiCIA9wSy3kUN3r16KspeLL2z9CxJC4OMOibJZsQxa53kKWM0JZrdTa0iBt5Wa2%2FbLX2D3u3ByXDvJeBPO9ty7hY80hjeQpd%2F8QzIVnVJXfQOfccBd9bVsMu5zrl0XGkzUySVAeiLWMmi9T3AfWJLkU2YHxsxl0uQPdqjdxYEqeJLSPxhxTHstSluq1p5ccE0r%2F9BV4F1aT8ZcZl3ULryX7E0laweU1vVDo%2BaCNMq2MaxeF%2Ffi7K381lGwb99Wt7DFIKHOIy6zw7%2BNOp29M0NPFKnasipj3dZQXMCAOwDYtNDDc99ez8ol5FubNb4SRke21HUWKt4ARBbaxX4g22W14u3%2FkavofMNlpjjuq7QX%2FoGe%2BdLzRhd7EYzDVpMOOyKU4NKOWQ%2B0waQJ8y8db5LzAgtLoV0vrJFO9VToqrTCJjfPJBjqkAYdoR9%2BqxhadsLmouvtjMerOo%2FT8u5eq1ym206%2Fi6jSZnGk547GfYjZXwnxn03r%2FzGXNZG3f3z7H%2F1FSSbEFHRRHNtuI%2BT0NJ32YHCMtNX9xuy0EV9ldr8qnXNKm%2Biiur5Z5aVXCspRP9Pdfp6JGE2bMAOrSxgGUV%2FmX5lSiJBbXbqbiXcyHpSG8prwEE4MkjtCqWX2FKMA9xXJrBBYE%2Fejka6rI&X-Amz-Signature=1c1d4633df762ac8f9acc39445b8bd803f6d737f5fee26fbc06b0c388a5e5ccd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJ3RV2HQ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDrFOJTmLthWgLgp0q6np6H8L1zbinJFGPnm8WYsUvd3gIhAMvZjsZaLDPLJl4i%2B66Bt1clP1dAiCoYiO2SG8EX1pFEKv8DCBMQABoMNjM3NDIzMTgzODA1Igx9DC4iZCS68WwGzVgq3ANd%2F%2FMeIW%2BwuMVqh9Z4tzDcizyue5FhnCf9fDjyNBB5AIyvISRvib8XFseeoJ9i1hBfOzfrf1ra1XUH8ZnrJ%2BIWHPZTnSMenPTFutDP%2B7fhZJ1QUBffdT1mMifWW5xtjm0nsVSunbkTktxNY1ZCucdalBXAETRlhZ3VShZ8K6zh%2Binw90tacCk9fMJwj%2BK3c9oyN2KWAWLhNaexA4sCILiCIA9wSy3kUN3r16KspeLL2z9CxJC4OMOibJZsQxa53kKWM0JZrdTa0iBt5Wa2%2FbLX2D3u3ByXDvJeBPO9ty7hY80hjeQpd%2F8QzIVnVJXfQOfccBd9bVsMu5zrl0XGkzUySVAeiLWMmi9T3AfWJLkU2YHxsxl0uQPdqjdxYEqeJLSPxhxTHstSluq1p5ccE0r%2F9BV4F1aT8ZcZl3ULryX7E0laweU1vVDo%2BaCNMq2MaxeF%2Ffi7K381lGwb99Wt7DFIKHOIy6zw7%2BNOp29M0NPFKnasipj3dZQXMCAOwDYtNDDc99ez8ol5FubNb4SRke21HUWKt4ARBbaxX4g22W14u3%2FkavofMNlpjjuq7QX%2FoGe%2BdLzRhd7EYzDVpMOOyKU4NKOWQ%2B0waQJ8y8db5LzAgtLoV0vrJFO9VToqrTCJjfPJBjqkAYdoR9%2BqxhadsLmouvtjMerOo%2FT8u5eq1ym206%2Fi6jSZnGk547GfYjZXwnxn03r%2FzGXNZG3f3z7H%2F1FSSbEFHRRHNtuI%2BT0NJ32YHCMtNX9xuy0EV9ldr8qnXNKm%2Biiur5Z5aVXCspRP9Pdfp6JGE2bMAOrSxgGUV%2FmX5lSiJBbXbqbiXcyHpSG8prwEE4MkjtCqWX2FKMA9xXJrBBYE%2Fejka6rI&X-Amz-Signature=e765aede2419d9cc3ede8e37af84976cf3f6e48a103b29e7103c9d0a437884fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



