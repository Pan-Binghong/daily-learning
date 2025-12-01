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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VB3HBRR%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCvro%2BkSgLxQamEo1G8s8uFRHtbz3ZIyvMuH9w8A%2B9FkAIhAN5%2B8Lsc9HB7ZAOF5hLUECs1gC0S6jaDQkMqD9M8dQTCKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzr72QcKG%2F6oHKPB5Aq3APJXq%2FhFlvIKdzRibM6r3k3MTG2ruQl0zGtYaSIkYw6MuLU4zLOxOomx0Hm33p98L7DrrvqjXj1OAT%2FV6vFK%2BZVcRK23h9IYXIetlrxOivsIVjmxGpl2I%2FwzKM2SLue%2Bk%2FkqgDzOiJbCIz7nwvaoqY9vJ1lY%2FijGEs4TimP4hPBhuyrq3Ky8FNtA%2FW81LKoRBbyv72IX3Cy9nt7C%2FRmcJ%2F%2BOJOtZ5lqqeSOf6ro2X44YOH3bItIT%2Bg59uXA6YNkYvKjlSoLaGULKUagUJ3275%2F%2B5ITkCQzyOjHRgvNws%2FeTNK9t7a8yALyXJto1z%2FkVcjqRaZXXvrE4BTEslzwXhPmfyguPmXsQxgff5cg2l6FK5sf%2BjrytHAcNAnSBBVhvRgof3HlYLtM1BFWiO530TU98ShDbgrrwr6I8GUegajfmB1iyEHL1sdg7dlp1sTGN7MF8OyXWBeVRw4qjEcJUSCsUlmwY3pdTlf%2Fgr0QnE%2BF5fPn0AvG0CX6agZnsbQAxC4HuPTFdQATorJkruvInHeggBciJnV1g7070flIBEZqRWur8zKc6yGLzkAP0YLwkj5DQ1HMPIGH5aKq%2BHstv2Ofxfh9UqGVDHRT%2Bd%2FrXFbnbq40ebHZVyt2IYYFdsTCZ87LJBjqkAXVCbK9bWXWZXQ72PFBV1XaZ4E2ZI6NrAA3aWIOkidBAg7T5mrPX9qQzRw5u5evdkRbA0rFwro3nJygqwjtuot64aVFNivwsd%2F3nOIxm3jD45raOQ%2FspAaYfWYmF6fHoXBEPfo%2BKdj9g7%2F76DVTuK2T5bpwHZHCGg12dUyRZqh8z0E1qSTUxiV3qsIAK8tYYDUXcEwjle0JGKLukH9jmpnjSIMgd&X-Amz-Signature=38d2b900cbba8f61862cc18ad66fd3f64cb6e9e8316edfe1b20b602c12b2ac66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VB3HBRR%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCvro%2BkSgLxQamEo1G8s8uFRHtbz3ZIyvMuH9w8A%2B9FkAIhAN5%2B8Lsc9HB7ZAOF5hLUECs1gC0S6jaDQkMqD9M8dQTCKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzr72QcKG%2F6oHKPB5Aq3APJXq%2FhFlvIKdzRibM6r3k3MTG2ruQl0zGtYaSIkYw6MuLU4zLOxOomx0Hm33p98L7DrrvqjXj1OAT%2FV6vFK%2BZVcRK23h9IYXIetlrxOivsIVjmxGpl2I%2FwzKM2SLue%2Bk%2FkqgDzOiJbCIz7nwvaoqY9vJ1lY%2FijGEs4TimP4hPBhuyrq3Ky8FNtA%2FW81LKoRBbyv72IX3Cy9nt7C%2FRmcJ%2F%2BOJOtZ5lqqeSOf6ro2X44YOH3bItIT%2Bg59uXA6YNkYvKjlSoLaGULKUagUJ3275%2F%2B5ITkCQzyOjHRgvNws%2FeTNK9t7a8yALyXJto1z%2FkVcjqRaZXXvrE4BTEslzwXhPmfyguPmXsQxgff5cg2l6FK5sf%2BjrytHAcNAnSBBVhvRgof3HlYLtM1BFWiO530TU98ShDbgrrwr6I8GUegajfmB1iyEHL1sdg7dlp1sTGN7MF8OyXWBeVRw4qjEcJUSCsUlmwY3pdTlf%2Fgr0QnE%2BF5fPn0AvG0CX6agZnsbQAxC4HuPTFdQATorJkruvInHeggBciJnV1g7070flIBEZqRWur8zKc6yGLzkAP0YLwkj5DQ1HMPIGH5aKq%2BHstv2Ofxfh9UqGVDHRT%2Bd%2FrXFbnbq40ebHZVyt2IYYFdsTCZ87LJBjqkAXVCbK9bWXWZXQ72PFBV1XaZ4E2ZI6NrAA3aWIOkidBAg7T5mrPX9qQzRw5u5evdkRbA0rFwro3nJygqwjtuot64aVFNivwsd%2F3nOIxm3jD45raOQ%2FspAaYfWYmF6fHoXBEPfo%2BKdj9g7%2F76DVTuK2T5bpwHZHCGg12dUyRZqh8z0E1qSTUxiV3qsIAK8tYYDUXcEwjle0JGKLukH9jmpnjSIMgd&X-Amz-Signature=076995651021ae2f14507930006f6268246e64818807b8c14caabc04d1b6af26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VB3HBRR%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCvro%2BkSgLxQamEo1G8s8uFRHtbz3ZIyvMuH9w8A%2B9FkAIhAN5%2B8Lsc9HB7ZAOF5hLUECs1gC0S6jaDQkMqD9M8dQTCKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzr72QcKG%2F6oHKPB5Aq3APJXq%2FhFlvIKdzRibM6r3k3MTG2ruQl0zGtYaSIkYw6MuLU4zLOxOomx0Hm33p98L7DrrvqjXj1OAT%2FV6vFK%2BZVcRK23h9IYXIetlrxOivsIVjmxGpl2I%2FwzKM2SLue%2Bk%2FkqgDzOiJbCIz7nwvaoqY9vJ1lY%2FijGEs4TimP4hPBhuyrq3Ky8FNtA%2FW81LKoRBbyv72IX3Cy9nt7C%2FRmcJ%2F%2BOJOtZ5lqqeSOf6ro2X44YOH3bItIT%2Bg59uXA6YNkYvKjlSoLaGULKUagUJ3275%2F%2B5ITkCQzyOjHRgvNws%2FeTNK9t7a8yALyXJto1z%2FkVcjqRaZXXvrE4BTEslzwXhPmfyguPmXsQxgff5cg2l6FK5sf%2BjrytHAcNAnSBBVhvRgof3HlYLtM1BFWiO530TU98ShDbgrrwr6I8GUegajfmB1iyEHL1sdg7dlp1sTGN7MF8OyXWBeVRw4qjEcJUSCsUlmwY3pdTlf%2Fgr0QnE%2BF5fPn0AvG0CX6agZnsbQAxC4HuPTFdQATorJkruvInHeggBciJnV1g7070flIBEZqRWur8zKc6yGLzkAP0YLwkj5DQ1HMPIGH5aKq%2BHstv2Ofxfh9UqGVDHRT%2Bd%2FrXFbnbq40ebHZVyt2IYYFdsTCZ87LJBjqkAXVCbK9bWXWZXQ72PFBV1XaZ4E2ZI6NrAA3aWIOkidBAg7T5mrPX9qQzRw5u5evdkRbA0rFwro3nJygqwjtuot64aVFNivwsd%2F3nOIxm3jD45raOQ%2FspAaYfWYmF6fHoXBEPfo%2BKdj9g7%2F76DVTuK2T5bpwHZHCGg12dUyRZqh8z0E1qSTUxiV3qsIAK8tYYDUXcEwjle0JGKLukH9jmpnjSIMgd&X-Amz-Signature=8f1cdcf89e4e8e8bc8db3e84673031f2a2dd7752aeb87d3817e0eac7493fa83b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VB3HBRR%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCvro%2BkSgLxQamEo1G8s8uFRHtbz3ZIyvMuH9w8A%2B9FkAIhAN5%2B8Lsc9HB7ZAOF5hLUECs1gC0S6jaDQkMqD9M8dQTCKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzr72QcKG%2F6oHKPB5Aq3APJXq%2FhFlvIKdzRibM6r3k3MTG2ruQl0zGtYaSIkYw6MuLU4zLOxOomx0Hm33p98L7DrrvqjXj1OAT%2FV6vFK%2BZVcRK23h9IYXIetlrxOivsIVjmxGpl2I%2FwzKM2SLue%2Bk%2FkqgDzOiJbCIz7nwvaoqY9vJ1lY%2FijGEs4TimP4hPBhuyrq3Ky8FNtA%2FW81LKoRBbyv72IX3Cy9nt7C%2FRmcJ%2F%2BOJOtZ5lqqeSOf6ro2X44YOH3bItIT%2Bg59uXA6YNkYvKjlSoLaGULKUagUJ3275%2F%2B5ITkCQzyOjHRgvNws%2FeTNK9t7a8yALyXJto1z%2FkVcjqRaZXXvrE4BTEslzwXhPmfyguPmXsQxgff5cg2l6FK5sf%2BjrytHAcNAnSBBVhvRgof3HlYLtM1BFWiO530TU98ShDbgrrwr6I8GUegajfmB1iyEHL1sdg7dlp1sTGN7MF8OyXWBeVRw4qjEcJUSCsUlmwY3pdTlf%2Fgr0QnE%2BF5fPn0AvG0CX6agZnsbQAxC4HuPTFdQATorJkruvInHeggBciJnV1g7070flIBEZqRWur8zKc6yGLzkAP0YLwkj5DQ1HMPIGH5aKq%2BHstv2Ofxfh9UqGVDHRT%2Bd%2FrXFbnbq40ebHZVyt2IYYFdsTCZ87LJBjqkAXVCbK9bWXWZXQ72PFBV1XaZ4E2ZI6NrAA3aWIOkidBAg7T5mrPX9qQzRw5u5evdkRbA0rFwro3nJygqwjtuot64aVFNivwsd%2F3nOIxm3jD45raOQ%2FspAaYfWYmF6fHoXBEPfo%2BKdj9g7%2F76DVTuK2T5bpwHZHCGg12dUyRZqh8z0E1qSTUxiV3qsIAK8tYYDUXcEwjle0JGKLukH9jmpnjSIMgd&X-Amz-Signature=f0946c6bb315f8942bc14e2bd401c5f968cb3ee41c41f33ce843abc6f42b790a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



