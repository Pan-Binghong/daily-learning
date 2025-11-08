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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5EWD7DU%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCgyYOXh5YbyBNftbenRLi9WWTAhuTB4vuhvnvPpTYtsAIhAL9O6a9q1QD41QzkRghFRH6zmVrOXpCicwg1Vi2Ne1i0KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWQF5A6AcIajSePqYq3AP%2BCzvLKkMp1Kyncpk%2B3Pa6QIR73HEda4e7f91fXrqFQHjQyQvYZwtyRrfYsQOqsCd23TMwKbIg3w9%2FHI%2BU4ffqThGlTrYK1WnPUrB51ZCrEogWeUbSR%2BHaQ%2FK8Nl5K70ucoEtV3%2BqK3hJAUjGlU%2FuVmjADbZlBMef7RBRWr1udz8KRtPvt3%2BhkxDxehcnovh7oJpGv8kRZEjCdi0Gk508ZpCygHwudOS4y61patf6EC%2BHWH9rb9OGAUWpP0H1CWUv%2BIw%2FAjJQ3Bo0ss52KzzTxvG1etgYFNSORrz3pm9dnpLb%2FVR6iLO%2FcxYwb%2F03QOSeVDKnh4bKv40sthcYfstfCGETHvXs3A1EGkHxXnWhOQPKZyJgmcmEdwPdKqehP7KoYTyRzsJBY8vxLQYyyLFPYICcyI1TxoT5nCcUR2M0VUV1y1rSXOvj6ttzzGeGwvhH4SG65uGac3izpiXuoVEig4qYP4DJEmUkfw6jZhVT0e8yFefcKCDtRfwMu7QmiN1ea0qr%2BB9%2BOcDHxLWlx6tH%2BjqCyDBR3UnCYEa27r1sLD02T0xLHf%2Br7x0C9dW8BeBF9my4K%2BZjeNdY%2F3evrxqtGcDr1hF0jrziz12VJjDLmTkygRfBgF0lXcHxrSDCu0LrIBjqkARQTIzUEULB%2BqlXSe5O%2Bc7GagDl7aTGjK1xhtF0HlY15opQGZK3sgJkA9WaiOpYLX3E08fAdbJEVtUyvxDem5yduDEvnQJELAg%2Boz8%2BbNvu0CbcUU1%2F8QZVl2Wy4OfgFG%2FiDYamFT2cOOpPoGafEOc76KTzjV5A0vX8pukg36EMgbCnO1Et7k34FUZEuybVE3I121gsGRGlYcyHZAOTgdvj%2B%2B8c5&X-Amz-Signature=52b59df51c98459e73b2703144e862ed3a6e2c172cd4682ed3c09b192ed31245&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5EWD7DU%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCgyYOXh5YbyBNftbenRLi9WWTAhuTB4vuhvnvPpTYtsAIhAL9O6a9q1QD41QzkRghFRH6zmVrOXpCicwg1Vi2Ne1i0KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWQF5A6AcIajSePqYq3AP%2BCzvLKkMp1Kyncpk%2B3Pa6QIR73HEda4e7f91fXrqFQHjQyQvYZwtyRrfYsQOqsCd23TMwKbIg3w9%2FHI%2BU4ffqThGlTrYK1WnPUrB51ZCrEogWeUbSR%2BHaQ%2FK8Nl5K70ucoEtV3%2BqK3hJAUjGlU%2FuVmjADbZlBMef7RBRWr1udz8KRtPvt3%2BhkxDxehcnovh7oJpGv8kRZEjCdi0Gk508ZpCygHwudOS4y61patf6EC%2BHWH9rb9OGAUWpP0H1CWUv%2BIw%2FAjJQ3Bo0ss52KzzTxvG1etgYFNSORrz3pm9dnpLb%2FVR6iLO%2FcxYwb%2F03QOSeVDKnh4bKv40sthcYfstfCGETHvXs3A1EGkHxXnWhOQPKZyJgmcmEdwPdKqehP7KoYTyRzsJBY8vxLQYyyLFPYICcyI1TxoT5nCcUR2M0VUV1y1rSXOvj6ttzzGeGwvhH4SG65uGac3izpiXuoVEig4qYP4DJEmUkfw6jZhVT0e8yFefcKCDtRfwMu7QmiN1ea0qr%2BB9%2BOcDHxLWlx6tH%2BjqCyDBR3UnCYEa27r1sLD02T0xLHf%2Br7x0C9dW8BeBF9my4K%2BZjeNdY%2F3evrxqtGcDr1hF0jrziz12VJjDLmTkygRfBgF0lXcHxrSDCu0LrIBjqkARQTIzUEULB%2BqlXSe5O%2Bc7GagDl7aTGjK1xhtF0HlY15opQGZK3sgJkA9WaiOpYLX3E08fAdbJEVtUyvxDem5yduDEvnQJELAg%2Boz8%2BbNvu0CbcUU1%2F8QZVl2Wy4OfgFG%2FiDYamFT2cOOpPoGafEOc76KTzjV5A0vX8pukg36EMgbCnO1Et7k34FUZEuybVE3I121gsGRGlYcyHZAOTgdvj%2B%2B8c5&X-Amz-Signature=51c1c9708abc550e2179385fb1a9ae8048c933771e0c0e9b25b84c1bac287da0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5EWD7DU%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCgyYOXh5YbyBNftbenRLi9WWTAhuTB4vuhvnvPpTYtsAIhAL9O6a9q1QD41QzkRghFRH6zmVrOXpCicwg1Vi2Ne1i0KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWQF5A6AcIajSePqYq3AP%2BCzvLKkMp1Kyncpk%2B3Pa6QIR73HEda4e7f91fXrqFQHjQyQvYZwtyRrfYsQOqsCd23TMwKbIg3w9%2FHI%2BU4ffqThGlTrYK1WnPUrB51ZCrEogWeUbSR%2BHaQ%2FK8Nl5K70ucoEtV3%2BqK3hJAUjGlU%2FuVmjADbZlBMef7RBRWr1udz8KRtPvt3%2BhkxDxehcnovh7oJpGv8kRZEjCdi0Gk508ZpCygHwudOS4y61patf6EC%2BHWH9rb9OGAUWpP0H1CWUv%2BIw%2FAjJQ3Bo0ss52KzzTxvG1etgYFNSORrz3pm9dnpLb%2FVR6iLO%2FcxYwb%2F03QOSeVDKnh4bKv40sthcYfstfCGETHvXs3A1EGkHxXnWhOQPKZyJgmcmEdwPdKqehP7KoYTyRzsJBY8vxLQYyyLFPYICcyI1TxoT5nCcUR2M0VUV1y1rSXOvj6ttzzGeGwvhH4SG65uGac3izpiXuoVEig4qYP4DJEmUkfw6jZhVT0e8yFefcKCDtRfwMu7QmiN1ea0qr%2BB9%2BOcDHxLWlx6tH%2BjqCyDBR3UnCYEa27r1sLD02T0xLHf%2Br7x0C9dW8BeBF9my4K%2BZjeNdY%2F3evrxqtGcDr1hF0jrziz12VJjDLmTkygRfBgF0lXcHxrSDCu0LrIBjqkARQTIzUEULB%2BqlXSe5O%2Bc7GagDl7aTGjK1xhtF0HlY15opQGZK3sgJkA9WaiOpYLX3E08fAdbJEVtUyvxDem5yduDEvnQJELAg%2Boz8%2BbNvu0CbcUU1%2F8QZVl2Wy4OfgFG%2FiDYamFT2cOOpPoGafEOc76KTzjV5A0vX8pukg36EMgbCnO1Et7k34FUZEuybVE3I121gsGRGlYcyHZAOTgdvj%2B%2B8c5&X-Amz-Signature=48c5eaeb1c1f143c1aff46ae524eb8ebb543120fd333ddc507ae7881b88da8db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5EWD7DU%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCgyYOXh5YbyBNftbenRLi9WWTAhuTB4vuhvnvPpTYtsAIhAL9O6a9q1QD41QzkRghFRH6zmVrOXpCicwg1Vi2Ne1i0KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWQF5A6AcIajSePqYq3AP%2BCzvLKkMp1Kyncpk%2B3Pa6QIR73HEda4e7f91fXrqFQHjQyQvYZwtyRrfYsQOqsCd23TMwKbIg3w9%2FHI%2BU4ffqThGlTrYK1WnPUrB51ZCrEogWeUbSR%2BHaQ%2FK8Nl5K70ucoEtV3%2BqK3hJAUjGlU%2FuVmjADbZlBMef7RBRWr1udz8KRtPvt3%2BhkxDxehcnovh7oJpGv8kRZEjCdi0Gk508ZpCygHwudOS4y61patf6EC%2BHWH9rb9OGAUWpP0H1CWUv%2BIw%2FAjJQ3Bo0ss52KzzTxvG1etgYFNSORrz3pm9dnpLb%2FVR6iLO%2FcxYwb%2F03QOSeVDKnh4bKv40sthcYfstfCGETHvXs3A1EGkHxXnWhOQPKZyJgmcmEdwPdKqehP7KoYTyRzsJBY8vxLQYyyLFPYICcyI1TxoT5nCcUR2M0VUV1y1rSXOvj6ttzzGeGwvhH4SG65uGac3izpiXuoVEig4qYP4DJEmUkfw6jZhVT0e8yFefcKCDtRfwMu7QmiN1ea0qr%2BB9%2BOcDHxLWlx6tH%2BjqCyDBR3UnCYEa27r1sLD02T0xLHf%2Br7x0C9dW8BeBF9my4K%2BZjeNdY%2F3evrxqtGcDr1hF0jrziz12VJjDLmTkygRfBgF0lXcHxrSDCu0LrIBjqkARQTIzUEULB%2BqlXSe5O%2Bc7GagDl7aTGjK1xhtF0HlY15opQGZK3sgJkA9WaiOpYLX3E08fAdbJEVtUyvxDem5yduDEvnQJELAg%2Boz8%2BbNvu0CbcUU1%2F8QZVl2Wy4OfgFG%2FiDYamFT2cOOpPoGafEOc76KTzjV5A0vX8pukg36EMgbCnO1Et7k34FUZEuybVE3I121gsGRGlYcyHZAOTgdvj%2B%2B8c5&X-Amz-Signature=36aa2d9277f0c163ff3c3fd11f474a583e0360b254abfb71e1bdf2ae9dc3141c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



