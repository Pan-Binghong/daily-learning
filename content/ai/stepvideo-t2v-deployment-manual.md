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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUYQS6ZM%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjDrBml%2B8ItGAVYZaxcqnso7Rhw8lr6uEbcH6Ctny7rwIhAN38fjAldDquAyRvY0e1XmYaFsZDu75RDevfK6YfrndCKv8DCHQQABoMNjM3NDIzMTgzODA1IgwkQlOhS3%2Bs%2BoSjqz8q3AOc2e%2FqKv1AdcSlutnn9znp6olrW4J3VpOCz%2BK5DvnfQfg9ie3i6t4M36lMH88CGGbLRvEVCMCQmWr4%2BVvSWstlIyXOQEPvg8thv%2B9wl7zhgk8By45sfY6NxkSqi3Ljif%2FI2dXnOBT7Vp3fG27YTODiBH0886U8%2BE4cW0qodBLRxY2UcZzsDm84VNtvw8Nw54EXm1xoIVGEAvj8J2GZdccpuENnUNhqY2vcTxOHku1Wkcl7q%2BxIWmrJMMsOOHqmh2celHoLgNM8CAfJqcA9HMgPcJPW3IHxhmZASsUqMu%2FTDYiuhsm59JKQRYzWxcUpkeNCW9jwsVLPpSAZNp8XmKi12jzLwpcG%2FwjtQCSPmjIHFKILBSp4UuzSiDPlIGlwbTnUMV6EAD%2BCDfRiYz1AQck6UIwe963RrLErI%2FlMUhISrMIDetvLyqoD%2FPJQNLqAmU%2FGdU%2BtPsGtn%2BIoyGVm29cspSvDponR6Be781LLxm79cKQ7gaUiLaoCwMPCXTmNO5KA5FJCkJ5kyoEU6WlVFmJkX7Qe8B1961NFjPaS9w9LVblfFk1XGIXWe6VMBrupLXfixy2lYXjTBVJ6WgAVoEYWKoAgbMC4O4WzUrer9LbAouZ6WdsA8lDDl0WDkDDR5ILOBjqkAW5m3%2BnoZdGDuYE5LZMswaaD%2FleHZkFJwtCbzVMNN3CIkeDZcHRAbwGcuC8ZPGphPRfVGqUpHsekD8rG0n5ypnrwFE0ei%2Fws8IPbjYYj4Ya3RQmD9cRVazOwgrY5m4FqImc6bOTdHtCECK%2BBSfMr9vCpOWPnUFMlVmCNy%2Fw7KQcYJm%2BzYUEOy2OaUHfN6AWQ7eV9iZ20dvJi8DtkP7zVvJybSAdJ&X-Amz-Signature=6d532469e1c4b54260b2ed81d10f84d2c5dda657c47a9009c224566efe7e02d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUYQS6ZM%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjDrBml%2B8ItGAVYZaxcqnso7Rhw8lr6uEbcH6Ctny7rwIhAN38fjAldDquAyRvY0e1XmYaFsZDu75RDevfK6YfrndCKv8DCHQQABoMNjM3NDIzMTgzODA1IgwkQlOhS3%2Bs%2BoSjqz8q3AOc2e%2FqKv1AdcSlutnn9znp6olrW4J3VpOCz%2BK5DvnfQfg9ie3i6t4M36lMH88CGGbLRvEVCMCQmWr4%2BVvSWstlIyXOQEPvg8thv%2B9wl7zhgk8By45sfY6NxkSqi3Ljif%2FI2dXnOBT7Vp3fG27YTODiBH0886U8%2BE4cW0qodBLRxY2UcZzsDm84VNtvw8Nw54EXm1xoIVGEAvj8J2GZdccpuENnUNhqY2vcTxOHku1Wkcl7q%2BxIWmrJMMsOOHqmh2celHoLgNM8CAfJqcA9HMgPcJPW3IHxhmZASsUqMu%2FTDYiuhsm59JKQRYzWxcUpkeNCW9jwsVLPpSAZNp8XmKi12jzLwpcG%2FwjtQCSPmjIHFKILBSp4UuzSiDPlIGlwbTnUMV6EAD%2BCDfRiYz1AQck6UIwe963RrLErI%2FlMUhISrMIDetvLyqoD%2FPJQNLqAmU%2FGdU%2BtPsGtn%2BIoyGVm29cspSvDponR6Be781LLxm79cKQ7gaUiLaoCwMPCXTmNO5KA5FJCkJ5kyoEU6WlVFmJkX7Qe8B1961NFjPaS9w9LVblfFk1XGIXWe6VMBrupLXfixy2lYXjTBVJ6WgAVoEYWKoAgbMC4O4WzUrer9LbAouZ6WdsA8lDDl0WDkDDR5ILOBjqkAW5m3%2BnoZdGDuYE5LZMswaaD%2FleHZkFJwtCbzVMNN3CIkeDZcHRAbwGcuC8ZPGphPRfVGqUpHsekD8rG0n5ypnrwFE0ei%2Fws8IPbjYYj4Ya3RQmD9cRVazOwgrY5m4FqImc6bOTdHtCECK%2BBSfMr9vCpOWPnUFMlVmCNy%2Fw7KQcYJm%2BzYUEOy2OaUHfN6AWQ7eV9iZ20dvJi8DtkP7zVvJybSAdJ&X-Amz-Signature=911a2c5b5be0dc19e765b253e92a0b32f5692cd97a1ef0a127ebce304a125eee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUYQS6ZM%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjDrBml%2B8ItGAVYZaxcqnso7Rhw8lr6uEbcH6Ctny7rwIhAN38fjAldDquAyRvY0e1XmYaFsZDu75RDevfK6YfrndCKv8DCHQQABoMNjM3NDIzMTgzODA1IgwkQlOhS3%2Bs%2BoSjqz8q3AOc2e%2FqKv1AdcSlutnn9znp6olrW4J3VpOCz%2BK5DvnfQfg9ie3i6t4M36lMH88CGGbLRvEVCMCQmWr4%2BVvSWstlIyXOQEPvg8thv%2B9wl7zhgk8By45sfY6NxkSqi3Ljif%2FI2dXnOBT7Vp3fG27YTODiBH0886U8%2BE4cW0qodBLRxY2UcZzsDm84VNtvw8Nw54EXm1xoIVGEAvj8J2GZdccpuENnUNhqY2vcTxOHku1Wkcl7q%2BxIWmrJMMsOOHqmh2celHoLgNM8CAfJqcA9HMgPcJPW3IHxhmZASsUqMu%2FTDYiuhsm59JKQRYzWxcUpkeNCW9jwsVLPpSAZNp8XmKi12jzLwpcG%2FwjtQCSPmjIHFKILBSp4UuzSiDPlIGlwbTnUMV6EAD%2BCDfRiYz1AQck6UIwe963RrLErI%2FlMUhISrMIDetvLyqoD%2FPJQNLqAmU%2FGdU%2BtPsGtn%2BIoyGVm29cspSvDponR6Be781LLxm79cKQ7gaUiLaoCwMPCXTmNO5KA5FJCkJ5kyoEU6WlVFmJkX7Qe8B1961NFjPaS9w9LVblfFk1XGIXWe6VMBrupLXfixy2lYXjTBVJ6WgAVoEYWKoAgbMC4O4WzUrer9LbAouZ6WdsA8lDDl0WDkDDR5ILOBjqkAW5m3%2BnoZdGDuYE5LZMswaaD%2FleHZkFJwtCbzVMNN3CIkeDZcHRAbwGcuC8ZPGphPRfVGqUpHsekD8rG0n5ypnrwFE0ei%2Fws8IPbjYYj4Ya3RQmD9cRVazOwgrY5m4FqImc6bOTdHtCECK%2BBSfMr9vCpOWPnUFMlVmCNy%2Fw7KQcYJm%2BzYUEOy2OaUHfN6AWQ7eV9iZ20dvJi8DtkP7zVvJybSAdJ&X-Amz-Signature=624152ec4095c846915201b21ef3fb333e28cdcf010ba20a717eb4db7df9af68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUYQS6ZM%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCjDrBml%2B8ItGAVYZaxcqnso7Rhw8lr6uEbcH6Ctny7rwIhAN38fjAldDquAyRvY0e1XmYaFsZDu75RDevfK6YfrndCKv8DCHQQABoMNjM3NDIzMTgzODA1IgwkQlOhS3%2Bs%2BoSjqz8q3AOc2e%2FqKv1AdcSlutnn9znp6olrW4J3VpOCz%2BK5DvnfQfg9ie3i6t4M36lMH88CGGbLRvEVCMCQmWr4%2BVvSWstlIyXOQEPvg8thv%2B9wl7zhgk8By45sfY6NxkSqi3Ljif%2FI2dXnOBT7Vp3fG27YTODiBH0886U8%2BE4cW0qodBLRxY2UcZzsDm84VNtvw8Nw54EXm1xoIVGEAvj8J2GZdccpuENnUNhqY2vcTxOHku1Wkcl7q%2BxIWmrJMMsOOHqmh2celHoLgNM8CAfJqcA9HMgPcJPW3IHxhmZASsUqMu%2FTDYiuhsm59JKQRYzWxcUpkeNCW9jwsVLPpSAZNp8XmKi12jzLwpcG%2FwjtQCSPmjIHFKILBSp4UuzSiDPlIGlwbTnUMV6EAD%2BCDfRiYz1AQck6UIwe963RrLErI%2FlMUhISrMIDetvLyqoD%2FPJQNLqAmU%2FGdU%2BtPsGtn%2BIoyGVm29cspSvDponR6Be781LLxm79cKQ7gaUiLaoCwMPCXTmNO5KA5FJCkJ5kyoEU6WlVFmJkX7Qe8B1961NFjPaS9w9LVblfFk1XGIXWe6VMBrupLXfixy2lYXjTBVJ6WgAVoEYWKoAgbMC4O4WzUrer9LbAouZ6WdsA8lDDl0WDkDDR5ILOBjqkAW5m3%2BnoZdGDuYE5LZMswaaD%2FleHZkFJwtCbzVMNN3CIkeDZcHRAbwGcuC8ZPGphPRfVGqUpHsekD8rG0n5ypnrwFE0ei%2Fws8IPbjYYj4Ya3RQmD9cRVazOwgrY5m4FqImc6bOTdHtCECK%2BBSfMr9vCpOWPnUFMlVmCNy%2Fw7KQcYJm%2BzYUEOy2OaUHfN6AWQ7eV9iZ20dvJi8DtkP7zVvJybSAdJ&X-Amz-Signature=a0b48396b224c2b075ff504038d4c841ffd52efa7996a2477ded3f12a730b03f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



