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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWQXSJNM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9dueB7NY5dev%2F0tPMVdN6xuGD5lr3%2FZXVkhO1IxLPCgIgPB0wZhtfWnpr4FwVsgHUq8qNPc6wWKcbtjx%2F3OxvPPEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDNpPsCg5aG9%2BvmfyryrcA3gLXY%2BVVkNk6UtRkUuw%2FUkhf58Zi%2BB%2FdLd%2BLWMcs6JCUl9kzUpiknyn%2BHNd70EcE683euTCEkw918heSgBfsokAApLqoaARAcFtP%2FQyqDpj5sjQsJsoySUsEGp2jKCBzJwWGyExehi%2BjcSv%2FlpFv7%2FFsY8KZtzuSE8NYvgzkBJZsZf9P2pVs1axVSnBfxSe78junpOpFjJJoWFDq0W2%2FgS03jh9%2BzRLp%2F4wIBuTOK1bDmnv%2BxuokghHSvYoGeEoCYpMJFbGN%2Bgd7Ui%2FIBuSQHmmSwMFnnhGZ1cjtby9dy973xg7a1qFtPnj8IWdlkZcA8Rb6bQdWA7WAWj8aXW2%2Boya4o0QUAVPiWrGsAHcW57vQEbSdPqD0M8AV7STK%2FiY2Tdn0fWOXrWUgAKsdkKdWQVe4eRcohvO1mOxZBmD5c99zSTp3vBI9VlDYQbiIlL9Tz7YJ4AqVSWp2Ol8WGSjwe5NNIGlrrp7fZE0XAbAXCX4QUH7xDKbtsy4JbDHojMTXfPydHPt9wcSNVlvLJKKHys8W%2Bzy9VyFJuUE1FoO9RAB7ELXXZsITrhWUnetnUpwoE9fgDzGkA7Tadheht%2BIRXCGeosr59fDNr3UUHGg56%2FUq83DtQmpodVA2zKdMI6svc4GOqUBczmwWo1iGqqacJn7XukKLLha4H020CIrHh524Ug%2FBG9EK0ZsO%2BoAgwXujvKUVai0q8xrlK%2Bbq%2B9tJPpTHg61mwpfZn2ipRGoPYG0scwHTJEMd3Mft5PCBmxN7ZzhWYP4wlaC5LU8xpRw7Gqxl1Nf8JNAo90eVQ9xFmSiwLkXVVEOf6MGz6ZhlxV5dl4dmEO2tv7XFSnlYn296mDiTiwyVQLSBG8l&X-Amz-Signature=d25044cecc8d43d6f2dc84c16d247b54961c6d3b206aa2e39f18c40f671f2244&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWQXSJNM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9dueB7NY5dev%2F0tPMVdN6xuGD5lr3%2FZXVkhO1IxLPCgIgPB0wZhtfWnpr4FwVsgHUq8qNPc6wWKcbtjx%2F3OxvPPEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDNpPsCg5aG9%2BvmfyryrcA3gLXY%2BVVkNk6UtRkUuw%2FUkhf58Zi%2BB%2FdLd%2BLWMcs6JCUl9kzUpiknyn%2BHNd70EcE683euTCEkw918heSgBfsokAApLqoaARAcFtP%2FQyqDpj5sjQsJsoySUsEGp2jKCBzJwWGyExehi%2BjcSv%2FlpFv7%2FFsY8KZtzuSE8NYvgzkBJZsZf9P2pVs1axVSnBfxSe78junpOpFjJJoWFDq0W2%2FgS03jh9%2BzRLp%2F4wIBuTOK1bDmnv%2BxuokghHSvYoGeEoCYpMJFbGN%2Bgd7Ui%2FIBuSQHmmSwMFnnhGZ1cjtby9dy973xg7a1qFtPnj8IWdlkZcA8Rb6bQdWA7WAWj8aXW2%2Boya4o0QUAVPiWrGsAHcW57vQEbSdPqD0M8AV7STK%2FiY2Tdn0fWOXrWUgAKsdkKdWQVe4eRcohvO1mOxZBmD5c99zSTp3vBI9VlDYQbiIlL9Tz7YJ4AqVSWp2Ol8WGSjwe5NNIGlrrp7fZE0XAbAXCX4QUH7xDKbtsy4JbDHojMTXfPydHPt9wcSNVlvLJKKHys8W%2Bzy9VyFJuUE1FoO9RAB7ELXXZsITrhWUnetnUpwoE9fgDzGkA7Tadheht%2BIRXCGeosr59fDNr3UUHGg56%2FUq83DtQmpodVA2zKdMI6svc4GOqUBczmwWo1iGqqacJn7XukKLLha4H020CIrHh524Ug%2FBG9EK0ZsO%2BoAgwXujvKUVai0q8xrlK%2Bbq%2B9tJPpTHg61mwpfZn2ipRGoPYG0scwHTJEMd3Mft5PCBmxN7ZzhWYP4wlaC5LU8xpRw7Gqxl1Nf8JNAo90eVQ9xFmSiwLkXVVEOf6MGz6ZhlxV5dl4dmEO2tv7XFSnlYn296mDiTiwyVQLSBG8l&X-Amz-Signature=62487bb09d93edb9a06fc3368d8549442a1df1b0d60233333635f6243f323a1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWQXSJNM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9dueB7NY5dev%2F0tPMVdN6xuGD5lr3%2FZXVkhO1IxLPCgIgPB0wZhtfWnpr4FwVsgHUq8qNPc6wWKcbtjx%2F3OxvPPEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDNpPsCg5aG9%2BvmfyryrcA3gLXY%2BVVkNk6UtRkUuw%2FUkhf58Zi%2BB%2FdLd%2BLWMcs6JCUl9kzUpiknyn%2BHNd70EcE683euTCEkw918heSgBfsokAApLqoaARAcFtP%2FQyqDpj5sjQsJsoySUsEGp2jKCBzJwWGyExehi%2BjcSv%2FlpFv7%2FFsY8KZtzuSE8NYvgzkBJZsZf9P2pVs1axVSnBfxSe78junpOpFjJJoWFDq0W2%2FgS03jh9%2BzRLp%2F4wIBuTOK1bDmnv%2BxuokghHSvYoGeEoCYpMJFbGN%2Bgd7Ui%2FIBuSQHmmSwMFnnhGZ1cjtby9dy973xg7a1qFtPnj8IWdlkZcA8Rb6bQdWA7WAWj8aXW2%2Boya4o0QUAVPiWrGsAHcW57vQEbSdPqD0M8AV7STK%2FiY2Tdn0fWOXrWUgAKsdkKdWQVe4eRcohvO1mOxZBmD5c99zSTp3vBI9VlDYQbiIlL9Tz7YJ4AqVSWp2Ol8WGSjwe5NNIGlrrp7fZE0XAbAXCX4QUH7xDKbtsy4JbDHojMTXfPydHPt9wcSNVlvLJKKHys8W%2Bzy9VyFJuUE1FoO9RAB7ELXXZsITrhWUnetnUpwoE9fgDzGkA7Tadheht%2BIRXCGeosr59fDNr3UUHGg56%2FUq83DtQmpodVA2zKdMI6svc4GOqUBczmwWo1iGqqacJn7XukKLLha4H020CIrHh524Ug%2FBG9EK0ZsO%2BoAgwXujvKUVai0q8xrlK%2Bbq%2B9tJPpTHg61mwpfZn2ipRGoPYG0scwHTJEMd3Mft5PCBmxN7ZzhWYP4wlaC5LU8xpRw7Gqxl1Nf8JNAo90eVQ9xFmSiwLkXVVEOf6MGz6ZhlxV5dl4dmEO2tv7XFSnlYn296mDiTiwyVQLSBG8l&X-Amz-Signature=d8beaaf2275b45ddc1d6814be044337e4b8e805999adef464993c8d25cf23944&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWQXSJNM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9dueB7NY5dev%2F0tPMVdN6xuGD5lr3%2FZXVkhO1IxLPCgIgPB0wZhtfWnpr4FwVsgHUq8qNPc6wWKcbtjx%2F3OxvPPEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDNpPsCg5aG9%2BvmfyryrcA3gLXY%2BVVkNk6UtRkUuw%2FUkhf58Zi%2BB%2FdLd%2BLWMcs6JCUl9kzUpiknyn%2BHNd70EcE683euTCEkw918heSgBfsokAApLqoaARAcFtP%2FQyqDpj5sjQsJsoySUsEGp2jKCBzJwWGyExehi%2BjcSv%2FlpFv7%2FFsY8KZtzuSE8NYvgzkBJZsZf9P2pVs1axVSnBfxSe78junpOpFjJJoWFDq0W2%2FgS03jh9%2BzRLp%2F4wIBuTOK1bDmnv%2BxuokghHSvYoGeEoCYpMJFbGN%2Bgd7Ui%2FIBuSQHmmSwMFnnhGZ1cjtby9dy973xg7a1qFtPnj8IWdlkZcA8Rb6bQdWA7WAWj8aXW2%2Boya4o0QUAVPiWrGsAHcW57vQEbSdPqD0M8AV7STK%2FiY2Tdn0fWOXrWUgAKsdkKdWQVe4eRcohvO1mOxZBmD5c99zSTp3vBI9VlDYQbiIlL9Tz7YJ4AqVSWp2Ol8WGSjwe5NNIGlrrp7fZE0XAbAXCX4QUH7xDKbtsy4JbDHojMTXfPydHPt9wcSNVlvLJKKHys8W%2Bzy9VyFJuUE1FoO9RAB7ELXXZsITrhWUnetnUpwoE9fgDzGkA7Tadheht%2BIRXCGeosr59fDNr3UUHGg56%2FUq83DtQmpodVA2zKdMI6svc4GOqUBczmwWo1iGqqacJn7XukKLLha4H020CIrHh524Ug%2FBG9EK0ZsO%2BoAgwXujvKUVai0q8xrlK%2Bbq%2B9tJPpTHg61mwpfZn2ipRGoPYG0scwHTJEMd3Mft5PCBmxN7ZzhWYP4wlaC5LU8xpRw7Gqxl1Nf8JNAo90eVQ9xFmSiwLkXVVEOf6MGz6ZhlxV5dl4dmEO2tv7XFSnlYn296mDiTiwyVQLSBG8l&X-Amz-Signature=c20e619253cf961b0c93fabbe69d461700857f09aad3f52b7636d434c1960052&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



