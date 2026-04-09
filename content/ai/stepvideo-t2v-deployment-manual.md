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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6JDUOFR%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDJlF%2FRNdbx4Idb596rBbUeDvLgCyWrcHjQLzydIpFvXAIgIPy35otHz3TJupBcCkWydZ5VHQ95QWxNU38jR2y7Jcgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDACKARezexCOhk%2BsfircA1PhakZXDGHQXo3Upi21D4B%2BKHxZVZj%2BmUqV9eGjM5RUTTEBs3gbI9IPip7gDT0DNLQ0fN3W5Bjl2zyzrIG0uYSgIDgGK626IenJpOPxqC4kPRHPbSGmn8wL%2FG%2B7h7sLmsNdQzaMUQd3sVIktkR1wPi%2BOwhduAIM9aTjmATf6T6LAECoD6Sha86PgEmBXJJv9wB9nTRM7td9JpDtgd83tEKqToAVkS6mtf42ji4bJIagLdqGhlQU0HBigkwnfJUdgul%2FLv%2Fd5j57VbWaJ1EQyrCFKuvJrE2Yl%2B%2B1tYyi4PDGRA6QTuhIhSptck1osK0QABwbCiwLqB39srMOIDTw8bVEfV4z%2ByZsrJQ4MzyV%2FKU7%2FQ8menRt7ydecDpHePkvJam3Z9BB8ywLEeDoe2KxLfkJNEktT6RKhw1Ows5iC69pmd%2FUewp4aKAsFvnw4JGjqICpqcH%2FC9I0%2FoDO02kKAhcZbg55qbqnlJiwxRunGgh1xIpU8aO7VwEjfKoDKIbRaVVvRNK3IpjEzBZ22c9y0DGNrc5OqYkkb7Cxpd2v3PM%2BRAk5tKoVKCz1gGZHNaZgV3oWmSHUD6il0o77QZVHkONm8kmi4Tzg%2Fm8Gax5EHIAjIg4fwvlvvUMliC3MML2z3M4GOqUBItB8X2E2QoBcjknCo252UumQyAsrqL5im1pa1JnGXs28692NzJdVwgvZuNmsXIc1P7%2BE7yD%2FSRVN6zfei4u0jokVeDBMjwhzmOLjGd0lsBzAuBJROCDNeKbRWZay6efBb4hbKaQOJioSF39i5aOXw970JhnIo61K578bXOXy1koGmL4uON4ohSo6dTjSMiqemPpPPhDE03DIcU5VeXu8I8DPpF5%2F&X-Amz-Signature=0ee63679a46688688f5e21b32507c080357f6e3b0b2c37a7a92d04465c8cbebe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6JDUOFR%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDJlF%2FRNdbx4Idb596rBbUeDvLgCyWrcHjQLzydIpFvXAIgIPy35otHz3TJupBcCkWydZ5VHQ95QWxNU38jR2y7Jcgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDACKARezexCOhk%2BsfircA1PhakZXDGHQXo3Upi21D4B%2BKHxZVZj%2BmUqV9eGjM5RUTTEBs3gbI9IPip7gDT0DNLQ0fN3W5Bjl2zyzrIG0uYSgIDgGK626IenJpOPxqC4kPRHPbSGmn8wL%2FG%2B7h7sLmsNdQzaMUQd3sVIktkR1wPi%2BOwhduAIM9aTjmATf6T6LAECoD6Sha86PgEmBXJJv9wB9nTRM7td9JpDtgd83tEKqToAVkS6mtf42ji4bJIagLdqGhlQU0HBigkwnfJUdgul%2FLv%2Fd5j57VbWaJ1EQyrCFKuvJrE2Yl%2B%2B1tYyi4PDGRA6QTuhIhSptck1osK0QABwbCiwLqB39srMOIDTw8bVEfV4z%2ByZsrJQ4MzyV%2FKU7%2FQ8menRt7ydecDpHePkvJam3Z9BB8ywLEeDoe2KxLfkJNEktT6RKhw1Ows5iC69pmd%2FUewp4aKAsFvnw4JGjqICpqcH%2FC9I0%2FoDO02kKAhcZbg55qbqnlJiwxRunGgh1xIpU8aO7VwEjfKoDKIbRaVVvRNK3IpjEzBZ22c9y0DGNrc5OqYkkb7Cxpd2v3PM%2BRAk5tKoVKCz1gGZHNaZgV3oWmSHUD6il0o77QZVHkONm8kmi4Tzg%2Fm8Gax5EHIAjIg4fwvlvvUMliC3MML2z3M4GOqUBItB8X2E2QoBcjknCo252UumQyAsrqL5im1pa1JnGXs28692NzJdVwgvZuNmsXIc1P7%2BE7yD%2FSRVN6zfei4u0jokVeDBMjwhzmOLjGd0lsBzAuBJROCDNeKbRWZay6efBb4hbKaQOJioSF39i5aOXw970JhnIo61K578bXOXy1koGmL4uON4ohSo6dTjSMiqemPpPPhDE03DIcU5VeXu8I8DPpF5%2F&X-Amz-Signature=c0af5860051bf0717f909cf343120e0e03714050eee2c41e3aaff69fb02c807c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6JDUOFR%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDJlF%2FRNdbx4Idb596rBbUeDvLgCyWrcHjQLzydIpFvXAIgIPy35otHz3TJupBcCkWydZ5VHQ95QWxNU38jR2y7Jcgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDACKARezexCOhk%2BsfircA1PhakZXDGHQXo3Upi21D4B%2BKHxZVZj%2BmUqV9eGjM5RUTTEBs3gbI9IPip7gDT0DNLQ0fN3W5Bjl2zyzrIG0uYSgIDgGK626IenJpOPxqC4kPRHPbSGmn8wL%2FG%2B7h7sLmsNdQzaMUQd3sVIktkR1wPi%2BOwhduAIM9aTjmATf6T6LAECoD6Sha86PgEmBXJJv9wB9nTRM7td9JpDtgd83tEKqToAVkS6mtf42ji4bJIagLdqGhlQU0HBigkwnfJUdgul%2FLv%2Fd5j57VbWaJ1EQyrCFKuvJrE2Yl%2B%2B1tYyi4PDGRA6QTuhIhSptck1osK0QABwbCiwLqB39srMOIDTw8bVEfV4z%2ByZsrJQ4MzyV%2FKU7%2FQ8menRt7ydecDpHePkvJam3Z9BB8ywLEeDoe2KxLfkJNEktT6RKhw1Ows5iC69pmd%2FUewp4aKAsFvnw4JGjqICpqcH%2FC9I0%2FoDO02kKAhcZbg55qbqnlJiwxRunGgh1xIpU8aO7VwEjfKoDKIbRaVVvRNK3IpjEzBZ22c9y0DGNrc5OqYkkb7Cxpd2v3PM%2BRAk5tKoVKCz1gGZHNaZgV3oWmSHUD6il0o77QZVHkONm8kmi4Tzg%2Fm8Gax5EHIAjIg4fwvlvvUMliC3MML2z3M4GOqUBItB8X2E2QoBcjknCo252UumQyAsrqL5im1pa1JnGXs28692NzJdVwgvZuNmsXIc1P7%2BE7yD%2FSRVN6zfei4u0jokVeDBMjwhzmOLjGd0lsBzAuBJROCDNeKbRWZay6efBb4hbKaQOJioSF39i5aOXw970JhnIo61K578bXOXy1koGmL4uON4ohSo6dTjSMiqemPpPPhDE03DIcU5VeXu8I8DPpF5%2F&X-Amz-Signature=7a77fa93a1f823e827f991b1fca8adb8a2fb680e68587ff659a7ab91dfed5076&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6JDUOFR%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDJlF%2FRNdbx4Idb596rBbUeDvLgCyWrcHjQLzydIpFvXAIgIPy35otHz3TJupBcCkWydZ5VHQ95QWxNU38jR2y7Jcgq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDACKARezexCOhk%2BsfircA1PhakZXDGHQXo3Upi21D4B%2BKHxZVZj%2BmUqV9eGjM5RUTTEBs3gbI9IPip7gDT0DNLQ0fN3W5Bjl2zyzrIG0uYSgIDgGK626IenJpOPxqC4kPRHPbSGmn8wL%2FG%2B7h7sLmsNdQzaMUQd3sVIktkR1wPi%2BOwhduAIM9aTjmATf6T6LAECoD6Sha86PgEmBXJJv9wB9nTRM7td9JpDtgd83tEKqToAVkS6mtf42ji4bJIagLdqGhlQU0HBigkwnfJUdgul%2FLv%2Fd5j57VbWaJ1EQyrCFKuvJrE2Yl%2B%2B1tYyi4PDGRA6QTuhIhSptck1osK0QABwbCiwLqB39srMOIDTw8bVEfV4z%2ByZsrJQ4MzyV%2FKU7%2FQ8menRt7ydecDpHePkvJam3Z9BB8ywLEeDoe2KxLfkJNEktT6RKhw1Ows5iC69pmd%2FUewp4aKAsFvnw4JGjqICpqcH%2FC9I0%2FoDO02kKAhcZbg55qbqnlJiwxRunGgh1xIpU8aO7VwEjfKoDKIbRaVVvRNK3IpjEzBZ22c9y0DGNrc5OqYkkb7Cxpd2v3PM%2BRAk5tKoVKCz1gGZHNaZgV3oWmSHUD6il0o77QZVHkONm8kmi4Tzg%2Fm8Gax5EHIAjIg4fwvlvvUMliC3MML2z3M4GOqUBItB8X2E2QoBcjknCo252UumQyAsrqL5im1pa1JnGXs28692NzJdVwgvZuNmsXIc1P7%2BE7yD%2FSRVN6zfei4u0jokVeDBMjwhzmOLjGd0lsBzAuBJROCDNeKbRWZay6efBb4hbKaQOJioSF39i5aOXw970JhnIo61K578bXOXy1koGmL4uON4ohSo6dTjSMiqemPpPPhDE03DIcU5VeXu8I8DPpF5%2F&X-Amz-Signature=48f1b6463b40c1eced61ddf144d3b5262f2b124f1ea304b94f9af99252586780&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



