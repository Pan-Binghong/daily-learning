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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAX6SVFG%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK327WUJcGKsG4SfWmESKrck33Ms5X7kmmSrFFF0LZGQIgRECNuNNq8sBivTwKYZnt1h3VQYolSR5MpMh8bPeCcDYqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQpBH58CBeq49ok8CrcA44LSQdhc%2FQEhZiV8CLWwNLqSI4%2BYMAb8ulzl1cwFXKKoGW%2BcDFoG7O2htd%2FiuyPOo5MDvnhtrWX5eAtc2xEhtCjii2%2BLsF1LNIGlxFeL%2FzZri3Ak6z3cZf%2Fp5BqjfkxIjIzB4q94cde5gq5npMMtQJizskVBZL4S6SmRK4NpIaaVcY1679Zm%2Fl3a3jncumYzeZtiX7k4QBEqoCvcbC47EKsFtscPPlLDWzI3ZVF4%2FrLuq9Jt8dzNyUaDvEHBczsfQ2Ssx67e0n91bXRCAgbLjrJvgjDF9Y3QGK8INsb%2Bhcdzw9Eg43sbBOr%2BxOGypPxjwDtqRX7HORdLvmP1oHJF%2B6apGzMMVfX49BU%2F4hTV7k4VOjZFTTAqAnkixt8e%2FWTcOk19LujSt610WpCTfBkHpZFqtSMV%2FK0klhZO43bAbS6zMFWJdlsYYasGrSuQtQaSJTd%2FRUGrnmNQGzO9MWm8kH2CLVpyd1QEMUBeZ1R0bssr3RAjAfPDe%2FRvTvriZEp9MO0vy1x%2FJKpM8m%2FZPCkWlIkbdTxIn%2FV2B%2Foywdf%2FoG6tSrb5vY0FtKzLcGdHKlWw2QTxdxgdlw7ZCyL9hjcUQpD0Xq7HcFbV7NnyZYoL2mKkJtciUNG%2FwA%2BBpVnMMrwr8gGOqUBdqHIpGudblarnntXDwjtfEUJoTkXARyGEe6Qv84hawVwZMS2P9FBJlmH8iflFbCs%2BTCAZLJXotXqdRT6vi3tO8eXSvGxciDIU5mLcN0WrKeDR5Xulf3rpku%2FR8j9VvLGcId5LkCigpIgfnDseXEjgB%2FNSwqi5Zh4y1xxyG5vne%2BMBaQiQsYlRHCd3Z8OXgQMttCFlvvbcclhnzq9Xp2%2F%2BCikj1c5&X-Amz-Signature=d45cbe37b295f595a301970ac19c6c5b24cedd8573191f6853d7fb3849db15d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAX6SVFG%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK327WUJcGKsG4SfWmESKrck33Ms5X7kmmSrFFF0LZGQIgRECNuNNq8sBivTwKYZnt1h3VQYolSR5MpMh8bPeCcDYqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQpBH58CBeq49ok8CrcA44LSQdhc%2FQEhZiV8CLWwNLqSI4%2BYMAb8ulzl1cwFXKKoGW%2BcDFoG7O2htd%2FiuyPOo5MDvnhtrWX5eAtc2xEhtCjii2%2BLsF1LNIGlxFeL%2FzZri3Ak6z3cZf%2Fp5BqjfkxIjIzB4q94cde5gq5npMMtQJizskVBZL4S6SmRK4NpIaaVcY1679Zm%2Fl3a3jncumYzeZtiX7k4QBEqoCvcbC47EKsFtscPPlLDWzI3ZVF4%2FrLuq9Jt8dzNyUaDvEHBczsfQ2Ssx67e0n91bXRCAgbLjrJvgjDF9Y3QGK8INsb%2Bhcdzw9Eg43sbBOr%2BxOGypPxjwDtqRX7HORdLvmP1oHJF%2B6apGzMMVfX49BU%2F4hTV7k4VOjZFTTAqAnkixt8e%2FWTcOk19LujSt610WpCTfBkHpZFqtSMV%2FK0klhZO43bAbS6zMFWJdlsYYasGrSuQtQaSJTd%2FRUGrnmNQGzO9MWm8kH2CLVpyd1QEMUBeZ1R0bssr3RAjAfPDe%2FRvTvriZEp9MO0vy1x%2FJKpM8m%2FZPCkWlIkbdTxIn%2FV2B%2Foywdf%2FoG6tSrb5vY0FtKzLcGdHKlWw2QTxdxgdlw7ZCyL9hjcUQpD0Xq7HcFbV7NnyZYoL2mKkJtciUNG%2FwA%2BBpVnMMrwr8gGOqUBdqHIpGudblarnntXDwjtfEUJoTkXARyGEe6Qv84hawVwZMS2P9FBJlmH8iflFbCs%2BTCAZLJXotXqdRT6vi3tO8eXSvGxciDIU5mLcN0WrKeDR5Xulf3rpku%2FR8j9VvLGcId5LkCigpIgfnDseXEjgB%2FNSwqi5Zh4y1xxyG5vne%2BMBaQiQsYlRHCd3Z8OXgQMttCFlvvbcclhnzq9Xp2%2F%2BCikj1c5&X-Amz-Signature=01d02b3495ff2244ea49e87a54c1ff1ffd723d1b3b8fcb114d5341bafd2cb465&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAX6SVFG%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK327WUJcGKsG4SfWmESKrck33Ms5X7kmmSrFFF0LZGQIgRECNuNNq8sBivTwKYZnt1h3VQYolSR5MpMh8bPeCcDYqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQpBH58CBeq49ok8CrcA44LSQdhc%2FQEhZiV8CLWwNLqSI4%2BYMAb8ulzl1cwFXKKoGW%2BcDFoG7O2htd%2FiuyPOo5MDvnhtrWX5eAtc2xEhtCjii2%2BLsF1LNIGlxFeL%2FzZri3Ak6z3cZf%2Fp5BqjfkxIjIzB4q94cde5gq5npMMtQJizskVBZL4S6SmRK4NpIaaVcY1679Zm%2Fl3a3jncumYzeZtiX7k4QBEqoCvcbC47EKsFtscPPlLDWzI3ZVF4%2FrLuq9Jt8dzNyUaDvEHBczsfQ2Ssx67e0n91bXRCAgbLjrJvgjDF9Y3QGK8INsb%2Bhcdzw9Eg43sbBOr%2BxOGypPxjwDtqRX7HORdLvmP1oHJF%2B6apGzMMVfX49BU%2F4hTV7k4VOjZFTTAqAnkixt8e%2FWTcOk19LujSt610WpCTfBkHpZFqtSMV%2FK0klhZO43bAbS6zMFWJdlsYYasGrSuQtQaSJTd%2FRUGrnmNQGzO9MWm8kH2CLVpyd1QEMUBeZ1R0bssr3RAjAfPDe%2FRvTvriZEp9MO0vy1x%2FJKpM8m%2FZPCkWlIkbdTxIn%2FV2B%2Foywdf%2FoG6tSrb5vY0FtKzLcGdHKlWw2QTxdxgdlw7ZCyL9hjcUQpD0Xq7HcFbV7NnyZYoL2mKkJtciUNG%2FwA%2BBpVnMMrwr8gGOqUBdqHIpGudblarnntXDwjtfEUJoTkXARyGEe6Qv84hawVwZMS2P9FBJlmH8iflFbCs%2BTCAZLJXotXqdRT6vi3tO8eXSvGxciDIU5mLcN0WrKeDR5Xulf3rpku%2FR8j9VvLGcId5LkCigpIgfnDseXEjgB%2FNSwqi5Zh4y1xxyG5vne%2BMBaQiQsYlRHCd3Z8OXgQMttCFlvvbcclhnzq9Xp2%2F%2BCikj1c5&X-Amz-Signature=831f1df72d7329c1ad3cd7e1815ac80c6e8ec0eaca9c051b74abd57432afa82f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAX6SVFG%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDK327WUJcGKsG4SfWmESKrck33Ms5X7kmmSrFFF0LZGQIgRECNuNNq8sBivTwKYZnt1h3VQYolSR5MpMh8bPeCcDYqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQpBH58CBeq49ok8CrcA44LSQdhc%2FQEhZiV8CLWwNLqSI4%2BYMAb8ulzl1cwFXKKoGW%2BcDFoG7O2htd%2FiuyPOo5MDvnhtrWX5eAtc2xEhtCjii2%2BLsF1LNIGlxFeL%2FzZri3Ak6z3cZf%2Fp5BqjfkxIjIzB4q94cde5gq5npMMtQJizskVBZL4S6SmRK4NpIaaVcY1679Zm%2Fl3a3jncumYzeZtiX7k4QBEqoCvcbC47EKsFtscPPlLDWzI3ZVF4%2FrLuq9Jt8dzNyUaDvEHBczsfQ2Ssx67e0n91bXRCAgbLjrJvgjDF9Y3QGK8INsb%2Bhcdzw9Eg43sbBOr%2BxOGypPxjwDtqRX7HORdLvmP1oHJF%2B6apGzMMVfX49BU%2F4hTV7k4VOjZFTTAqAnkixt8e%2FWTcOk19LujSt610WpCTfBkHpZFqtSMV%2FK0klhZO43bAbS6zMFWJdlsYYasGrSuQtQaSJTd%2FRUGrnmNQGzO9MWm8kH2CLVpyd1QEMUBeZ1R0bssr3RAjAfPDe%2FRvTvriZEp9MO0vy1x%2FJKpM8m%2FZPCkWlIkbdTxIn%2FV2B%2Foywdf%2FoG6tSrb5vY0FtKzLcGdHKlWw2QTxdxgdlw7ZCyL9hjcUQpD0Xq7HcFbV7NnyZYoL2mKkJtciUNG%2FwA%2BBpVnMMrwr8gGOqUBdqHIpGudblarnntXDwjtfEUJoTkXARyGEe6Qv84hawVwZMS2P9FBJlmH8iflFbCs%2BTCAZLJXotXqdRT6vi3tO8eXSvGxciDIU5mLcN0WrKeDR5Xulf3rpku%2FR8j9VvLGcId5LkCigpIgfnDseXEjgB%2FNSwqi5Zh4y1xxyG5vne%2BMBaQiQsYlRHCd3Z8OXgQMttCFlvvbcclhnzq9Xp2%2F%2BCikj1c5&X-Amz-Signature=d9a1deb24e161c3f2a50cb3b720bb243f6a95882bfcb97329cb15e5904ef070e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



