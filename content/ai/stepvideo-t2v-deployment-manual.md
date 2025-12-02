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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXJTFFIC%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD1T70vixOMp7Wm1EgzhYJc5qoDgFLh%2FFRB6Jw1920l%2FAIgT5uYcYveIhOHKEmMhtnZ%2FF3Cta4ZDDL1Fte5dFznZLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDIojphC4pWNCba1sqircA3D14un5hbAavRCLlNy3a6gvIj%2F5%2BPksjU7FrQYw7hoc5XWwC1ZDWXvh2ksxkXlJOwJ2k0xLalKbSwhbH0XTvskhVIyBgGE3yEzQpGsTi9MI6RDU09fwItk8xc5GcH2ZdZOlO3cgEZRPb7ZnwRrWPtCwfHvUnKXtoASfvV98Dg28e7SErM8znYvebTydHD5k0XtiTnUgys%2FPo24iP%2B9xf6OEQ2vbp0mQC%2F0RDzy13fSnP4iaHSIg4GTaLxYBP90c82GRdwpkkY8dxWc4gbLEiJu6QM9oGqwbWs8yjXTgGIXipTrZpNUCYAq0xVTNPQufjeOpyCSWH7M4L7QfwjAEcDvJeRgw29gYdgaJA8FmBaW1aTq585ivZzDwpTVML0GBoKC8O%2BQnqGPt4jWMHgTiae81k%2Bj4ahZM3zzjrqlhKDU2JLKRQx3djk67Mj7WZDQfckYkGd%2BecfC8v1t1qtYj%2B7nmyyfqtuW0wyYsvJBvK9Xe5Zyv72yjA5Jcc5L1uPihY2euBaMTtnWs85mGmuz3cUs%2FZVAJfPuXFR632c33YVEUTMB4xm3zMi2%2F2gLEjOTSjQroisbWxbRiVQi%2FC1oeBTNBT9rA0kfWBjpA38Okj25acamnQuc70nsIUR5LMK3euMkGOqUBpiUd9UCxVPgzwRS6UXd6JMrWkhtWNU5WIIv%2FDBK%2Br18GuZ13rWnY2lv8LMDLhbs%2Bq2LBe6gHQWFPNvSe%2B5bNxn1tO8kuIOmDRKQ29GV%2B%2F5LQSQCU%2F1VtQSWAw6p8g2fAiGKgTw3dSg7Mn19g49OZuEUE%2BEmff%2FscWt43oHCaur6ZHAbSDLvVHaCE9qLGyu5RFKcA13Imzh8grQLbHslTIeJSA1Li&X-Amz-Signature=5c71c8b927f6484492f6a640255b23d5dd24330acbc18b257b97386ea1aa18be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXJTFFIC%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD1T70vixOMp7Wm1EgzhYJc5qoDgFLh%2FFRB6Jw1920l%2FAIgT5uYcYveIhOHKEmMhtnZ%2FF3Cta4ZDDL1Fte5dFznZLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDIojphC4pWNCba1sqircA3D14un5hbAavRCLlNy3a6gvIj%2F5%2BPksjU7FrQYw7hoc5XWwC1ZDWXvh2ksxkXlJOwJ2k0xLalKbSwhbH0XTvskhVIyBgGE3yEzQpGsTi9MI6RDU09fwItk8xc5GcH2ZdZOlO3cgEZRPb7ZnwRrWPtCwfHvUnKXtoASfvV98Dg28e7SErM8znYvebTydHD5k0XtiTnUgys%2FPo24iP%2B9xf6OEQ2vbp0mQC%2F0RDzy13fSnP4iaHSIg4GTaLxYBP90c82GRdwpkkY8dxWc4gbLEiJu6QM9oGqwbWs8yjXTgGIXipTrZpNUCYAq0xVTNPQufjeOpyCSWH7M4L7QfwjAEcDvJeRgw29gYdgaJA8FmBaW1aTq585ivZzDwpTVML0GBoKC8O%2BQnqGPt4jWMHgTiae81k%2Bj4ahZM3zzjrqlhKDU2JLKRQx3djk67Mj7WZDQfckYkGd%2BecfC8v1t1qtYj%2B7nmyyfqtuW0wyYsvJBvK9Xe5Zyv72yjA5Jcc5L1uPihY2euBaMTtnWs85mGmuz3cUs%2FZVAJfPuXFR632c33YVEUTMB4xm3zMi2%2F2gLEjOTSjQroisbWxbRiVQi%2FC1oeBTNBT9rA0kfWBjpA38Okj25acamnQuc70nsIUR5LMK3euMkGOqUBpiUd9UCxVPgzwRS6UXd6JMrWkhtWNU5WIIv%2FDBK%2Br18GuZ13rWnY2lv8LMDLhbs%2Bq2LBe6gHQWFPNvSe%2B5bNxn1tO8kuIOmDRKQ29GV%2B%2F5LQSQCU%2F1VtQSWAw6p8g2fAiGKgTw3dSg7Mn19g49OZuEUE%2BEmff%2FscWt43oHCaur6ZHAbSDLvVHaCE9qLGyu5RFKcA13Imzh8grQLbHslTIeJSA1Li&X-Amz-Signature=bbeeffa82d6a21d4a7dc44f700b9ee32910f55a6c901e3f35dd34ab83b06b926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXJTFFIC%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD1T70vixOMp7Wm1EgzhYJc5qoDgFLh%2FFRB6Jw1920l%2FAIgT5uYcYveIhOHKEmMhtnZ%2FF3Cta4ZDDL1Fte5dFznZLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDIojphC4pWNCba1sqircA3D14un5hbAavRCLlNy3a6gvIj%2F5%2BPksjU7FrQYw7hoc5XWwC1ZDWXvh2ksxkXlJOwJ2k0xLalKbSwhbH0XTvskhVIyBgGE3yEzQpGsTi9MI6RDU09fwItk8xc5GcH2ZdZOlO3cgEZRPb7ZnwRrWPtCwfHvUnKXtoASfvV98Dg28e7SErM8znYvebTydHD5k0XtiTnUgys%2FPo24iP%2B9xf6OEQ2vbp0mQC%2F0RDzy13fSnP4iaHSIg4GTaLxYBP90c82GRdwpkkY8dxWc4gbLEiJu6QM9oGqwbWs8yjXTgGIXipTrZpNUCYAq0xVTNPQufjeOpyCSWH7M4L7QfwjAEcDvJeRgw29gYdgaJA8FmBaW1aTq585ivZzDwpTVML0GBoKC8O%2BQnqGPt4jWMHgTiae81k%2Bj4ahZM3zzjrqlhKDU2JLKRQx3djk67Mj7WZDQfckYkGd%2BecfC8v1t1qtYj%2B7nmyyfqtuW0wyYsvJBvK9Xe5Zyv72yjA5Jcc5L1uPihY2euBaMTtnWs85mGmuz3cUs%2FZVAJfPuXFR632c33YVEUTMB4xm3zMi2%2F2gLEjOTSjQroisbWxbRiVQi%2FC1oeBTNBT9rA0kfWBjpA38Okj25acamnQuc70nsIUR5LMK3euMkGOqUBpiUd9UCxVPgzwRS6UXd6JMrWkhtWNU5WIIv%2FDBK%2Br18GuZ13rWnY2lv8LMDLhbs%2Bq2LBe6gHQWFPNvSe%2B5bNxn1tO8kuIOmDRKQ29GV%2B%2F5LQSQCU%2F1VtQSWAw6p8g2fAiGKgTw3dSg7Mn19g49OZuEUE%2BEmff%2FscWt43oHCaur6ZHAbSDLvVHaCE9qLGyu5RFKcA13Imzh8grQLbHslTIeJSA1Li&X-Amz-Signature=d8716c1ee31a934c833ddab1a5f67011276611a93bd360d1d97bbbe02920a75c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXJTFFIC%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQD1T70vixOMp7Wm1EgzhYJc5qoDgFLh%2FFRB6Jw1920l%2FAIgT5uYcYveIhOHKEmMhtnZ%2FF3Cta4ZDDL1Fte5dFznZLQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDIojphC4pWNCba1sqircA3D14un5hbAavRCLlNy3a6gvIj%2F5%2BPksjU7FrQYw7hoc5XWwC1ZDWXvh2ksxkXlJOwJ2k0xLalKbSwhbH0XTvskhVIyBgGE3yEzQpGsTi9MI6RDU09fwItk8xc5GcH2ZdZOlO3cgEZRPb7ZnwRrWPtCwfHvUnKXtoASfvV98Dg28e7SErM8znYvebTydHD5k0XtiTnUgys%2FPo24iP%2B9xf6OEQ2vbp0mQC%2F0RDzy13fSnP4iaHSIg4GTaLxYBP90c82GRdwpkkY8dxWc4gbLEiJu6QM9oGqwbWs8yjXTgGIXipTrZpNUCYAq0xVTNPQufjeOpyCSWH7M4L7QfwjAEcDvJeRgw29gYdgaJA8FmBaW1aTq585ivZzDwpTVML0GBoKC8O%2BQnqGPt4jWMHgTiae81k%2Bj4ahZM3zzjrqlhKDU2JLKRQx3djk67Mj7WZDQfckYkGd%2BecfC8v1t1qtYj%2B7nmyyfqtuW0wyYsvJBvK9Xe5Zyv72yjA5Jcc5L1uPihY2euBaMTtnWs85mGmuz3cUs%2FZVAJfPuXFR632c33YVEUTMB4xm3zMi2%2F2gLEjOTSjQroisbWxbRiVQi%2FC1oeBTNBT9rA0kfWBjpA38Okj25acamnQuc70nsIUR5LMK3euMkGOqUBpiUd9UCxVPgzwRS6UXd6JMrWkhtWNU5WIIv%2FDBK%2Br18GuZ13rWnY2lv8LMDLhbs%2Bq2LBe6gHQWFPNvSe%2B5bNxn1tO8kuIOmDRKQ29GV%2B%2F5LQSQCU%2F1VtQSWAw6p8g2fAiGKgTw3dSg7Mn19g49OZuEUE%2BEmff%2FscWt43oHCaur6ZHAbSDLvVHaCE9qLGyu5RFKcA13Imzh8grQLbHslTIeJSA1Li&X-Amz-Signature=5a4ed89bc11c7543a3394dd64287f05917178c4c9d3759094a557fcf95529388&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



