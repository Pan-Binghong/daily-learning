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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LHX7JUA%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzmxiQsexrsPejpebNlG21JeJzQZ5QD3Muu8zjq2puyQIgBQn8eel1dAmpvWE9rfrKVWu9TV4Y4vRIv1FZ7RCv3zYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJu%2FgzyAH4CSFjaI%2FCrcA%2Bp6jc8VrjROUrKDhVscc2iCDlsOTw8lQhLX50T4LzwE6IQLCd0OLs%2F15dus%2FxwpY54ktFKM%2FIRuLQf9UXMrwXQmKop6tOmRcDMJx1fjGg4uNXFifx8eEgQdVU%2FpObPXRy45ohDf2amNPm0Sk9MbrrGagZNlLRg6xS7UZmLGRKrCaxQtg2NUSNdjEBwdJvbPfEq7v7s0QPR3Zd7Ob5b%2BWwuMF2fsl23q2wEzLMeBh8heGt14noujWn4HfHZbCnVqeGrHG4UatM0jS8AWxksQXiukI5BLA6MvCGN71Zjcl%2BTirzl88oXTyg7ErGady8tuXoethMROOy8556F9ZHa2gKbdJV8z0PzIcxpzGCkQVqWAtZmR%2BsgloC83JNmoMiSSNlzSIDXBEThR8%2Bt%2BMHY90Xl7vbPTjVNIrx3%2FJhanaOzWLKwOSLd4St9ruVGsSbqIaqW3IHG8fC2zj4n7NS%2BFVgtuknow6HATEy16cVJ7AD1soIUXPy9G1a3uQFajznjGnVALjeN5eimo5EUp5ORx7HrOd6txr2U%2FqsreMExWKqjezgOS0jdlGmTIEqSHfS7vPjqNleNYnLIINQSmRWoh6TsSGl1Tn%2Fc4nwM7BmgbdZwvar3HXZ%2BonH7qBlv2MNuC080GOqUBNaj6UouaMWDO%2BwC2bUbFhveZl6yP46VOqA083tLRzEGez29%2BoZNw67dTavS8v3aVxuMykc8n%2BdvEtj%2FXufN5R4sEWDik9Gg8I8800R0I62upMdRscu0U8dvf%2FNra0k4ma%2BJNfTxsBmXCa7KbhnVouxOxXDtQZMCScywU1STA3wA37vsr2MQdKyx94vujXZhWXiZ97ANbgJOAyEISZlBoHF17U%2BpO&X-Amz-Signature=af8510c0416f712ccb8e894b5185de2d8ace6a0c50fa39265a927a28fde32671&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LHX7JUA%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzmxiQsexrsPejpebNlG21JeJzQZ5QD3Muu8zjq2puyQIgBQn8eel1dAmpvWE9rfrKVWu9TV4Y4vRIv1FZ7RCv3zYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJu%2FgzyAH4CSFjaI%2FCrcA%2Bp6jc8VrjROUrKDhVscc2iCDlsOTw8lQhLX50T4LzwE6IQLCd0OLs%2F15dus%2FxwpY54ktFKM%2FIRuLQf9UXMrwXQmKop6tOmRcDMJx1fjGg4uNXFifx8eEgQdVU%2FpObPXRy45ohDf2amNPm0Sk9MbrrGagZNlLRg6xS7UZmLGRKrCaxQtg2NUSNdjEBwdJvbPfEq7v7s0QPR3Zd7Ob5b%2BWwuMF2fsl23q2wEzLMeBh8heGt14noujWn4HfHZbCnVqeGrHG4UatM0jS8AWxksQXiukI5BLA6MvCGN71Zjcl%2BTirzl88oXTyg7ErGady8tuXoethMROOy8556F9ZHa2gKbdJV8z0PzIcxpzGCkQVqWAtZmR%2BsgloC83JNmoMiSSNlzSIDXBEThR8%2Bt%2BMHY90Xl7vbPTjVNIrx3%2FJhanaOzWLKwOSLd4St9ruVGsSbqIaqW3IHG8fC2zj4n7NS%2BFVgtuknow6HATEy16cVJ7AD1soIUXPy9G1a3uQFajznjGnVALjeN5eimo5EUp5ORx7HrOd6txr2U%2FqsreMExWKqjezgOS0jdlGmTIEqSHfS7vPjqNleNYnLIINQSmRWoh6TsSGl1Tn%2Fc4nwM7BmgbdZwvar3HXZ%2BonH7qBlv2MNuC080GOqUBNaj6UouaMWDO%2BwC2bUbFhveZl6yP46VOqA083tLRzEGez29%2BoZNw67dTavS8v3aVxuMykc8n%2BdvEtj%2FXufN5R4sEWDik9Gg8I8800R0I62upMdRscu0U8dvf%2FNra0k4ma%2BJNfTxsBmXCa7KbhnVouxOxXDtQZMCScywU1STA3wA37vsr2MQdKyx94vujXZhWXiZ97ANbgJOAyEISZlBoHF17U%2BpO&X-Amz-Signature=b9f3d8f586763507c5b6c792a439d89a21b1c704acc9a2ef5ba4ea331b6cb92b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LHX7JUA%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzmxiQsexrsPejpebNlG21JeJzQZ5QD3Muu8zjq2puyQIgBQn8eel1dAmpvWE9rfrKVWu9TV4Y4vRIv1FZ7RCv3zYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJu%2FgzyAH4CSFjaI%2FCrcA%2Bp6jc8VrjROUrKDhVscc2iCDlsOTw8lQhLX50T4LzwE6IQLCd0OLs%2F15dus%2FxwpY54ktFKM%2FIRuLQf9UXMrwXQmKop6tOmRcDMJx1fjGg4uNXFifx8eEgQdVU%2FpObPXRy45ohDf2amNPm0Sk9MbrrGagZNlLRg6xS7UZmLGRKrCaxQtg2NUSNdjEBwdJvbPfEq7v7s0QPR3Zd7Ob5b%2BWwuMF2fsl23q2wEzLMeBh8heGt14noujWn4HfHZbCnVqeGrHG4UatM0jS8AWxksQXiukI5BLA6MvCGN71Zjcl%2BTirzl88oXTyg7ErGady8tuXoethMROOy8556F9ZHa2gKbdJV8z0PzIcxpzGCkQVqWAtZmR%2BsgloC83JNmoMiSSNlzSIDXBEThR8%2Bt%2BMHY90Xl7vbPTjVNIrx3%2FJhanaOzWLKwOSLd4St9ruVGsSbqIaqW3IHG8fC2zj4n7NS%2BFVgtuknow6HATEy16cVJ7AD1soIUXPy9G1a3uQFajznjGnVALjeN5eimo5EUp5ORx7HrOd6txr2U%2FqsreMExWKqjezgOS0jdlGmTIEqSHfS7vPjqNleNYnLIINQSmRWoh6TsSGl1Tn%2Fc4nwM7BmgbdZwvar3HXZ%2BonH7qBlv2MNuC080GOqUBNaj6UouaMWDO%2BwC2bUbFhveZl6yP46VOqA083tLRzEGez29%2BoZNw67dTavS8v3aVxuMykc8n%2BdvEtj%2FXufN5R4sEWDik9Gg8I8800R0I62upMdRscu0U8dvf%2FNra0k4ma%2BJNfTxsBmXCa7KbhnVouxOxXDtQZMCScywU1STA3wA37vsr2MQdKyx94vujXZhWXiZ97ANbgJOAyEISZlBoHF17U%2BpO&X-Amz-Signature=1a830aae0c1c23b991b7e03163f20f724a989ca728a444d6e55e1c7053cb55b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LHX7JUA%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDzmxiQsexrsPejpebNlG21JeJzQZ5QD3Muu8zjq2puyQIgBQn8eel1dAmpvWE9rfrKVWu9TV4Y4vRIv1FZ7RCv3zYqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJu%2FgzyAH4CSFjaI%2FCrcA%2Bp6jc8VrjROUrKDhVscc2iCDlsOTw8lQhLX50T4LzwE6IQLCd0OLs%2F15dus%2FxwpY54ktFKM%2FIRuLQf9UXMrwXQmKop6tOmRcDMJx1fjGg4uNXFifx8eEgQdVU%2FpObPXRy45ohDf2amNPm0Sk9MbrrGagZNlLRg6xS7UZmLGRKrCaxQtg2NUSNdjEBwdJvbPfEq7v7s0QPR3Zd7Ob5b%2BWwuMF2fsl23q2wEzLMeBh8heGt14noujWn4HfHZbCnVqeGrHG4UatM0jS8AWxksQXiukI5BLA6MvCGN71Zjcl%2BTirzl88oXTyg7ErGady8tuXoethMROOy8556F9ZHa2gKbdJV8z0PzIcxpzGCkQVqWAtZmR%2BsgloC83JNmoMiSSNlzSIDXBEThR8%2Bt%2BMHY90Xl7vbPTjVNIrx3%2FJhanaOzWLKwOSLd4St9ruVGsSbqIaqW3IHG8fC2zj4n7NS%2BFVgtuknow6HATEy16cVJ7AD1soIUXPy9G1a3uQFajznjGnVALjeN5eimo5EUp5ORx7HrOd6txr2U%2FqsreMExWKqjezgOS0jdlGmTIEqSHfS7vPjqNleNYnLIINQSmRWoh6TsSGl1Tn%2Fc4nwM7BmgbdZwvar3HXZ%2BonH7qBlv2MNuC080GOqUBNaj6UouaMWDO%2BwC2bUbFhveZl6yP46VOqA083tLRzEGez29%2BoZNw67dTavS8v3aVxuMykc8n%2BdvEtj%2FXufN5R4sEWDik9Gg8I8800R0I62upMdRscu0U8dvf%2FNra0k4ma%2BJNfTxsBmXCa7KbhnVouxOxXDtQZMCScywU1STA3wA37vsr2MQdKyx94vujXZhWXiZ97ANbgJOAyEISZlBoHF17U%2BpO&X-Amz-Signature=dc43a9d0386f149fff72ec0164a95d23d66e312dd359830bc08bc2b2f2b458c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



