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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M3WF6IT%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYWYAo5vBF4Q3ePBPN%2F%2F7NfdgubQrDKcvwPgKEVS8tmAiBZ8q8ptpGTRdNPfRm3HtnwxbBiNDRUBLcQ%2B4%2B%2BmP%2BXKSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSQ%2BSQwgTrjmScHI%2BKtwDsuJQiYgpNAAT2XNspBfgB35BiV22n%2FW3HtaV4438oRsipdcSuMN0b3hVZ43PIJx77GV8yXIGTfENUGBy6CKK9OsEwNet9N%2FlfJqQI7Yti%2FzbQ9qHjH959N2H6jbbYkRc1qo3jk9SgL2P9yggvlCT4dMmRweSilbrXT93Sl%2B8BQ9z1O0Og9l9bHmVbrGp2a3cNx33CfWhdI6YiDIw9nZ%2BjBOH1o78%2BEsExLksUgmZ2gLpT0fLUWyX6La3C7ylQRdoDFhYrrYkEK7mfGV%2Fy8JNptPjfx%2BW2wm32HBR%2BP3r8mOvE%2FeyIASGcWvFYOFh63ZhsVKlZwpm8%2FfNKxcaXxElY13ybk%2B53LNA7dG7sZeMPNkn060MaRIa1IzgGHNCQrTvIFOyzNB8KLOZrf8jRZ2O%2FtN489DfMwRyjDE9JrbOx0CSR1CIbXt4x8poSBEVWK80SveS7%2Fd3tm%2FZiDoX5XJKsV9p76xRSR666VZWdWfIZE48cjS72u5Lpa1jcd%2FL%2BpM9kg3g4J3R%2FOrYy%2FMF0yWf9DleB2AvRlZXuYYqzT3OcFF%2F%2FVwOL1p5qH50%2BfKiphMKUfonNuhvTr0BoihZyG6KSEWLAVDQMK7ky4VNPwRk1FnRUqh1lfF5%2FykWnG4wp%2BqjyQY6pgFJZ1ffVD6tXLueQ7VtBIVHX3cxvnJn%2B6Hz0%2BWb9%2Ffo9tSf96O5rV7OpgG1oNE%2FZg3sBkesx5cdAWJSvJ%2FHIVH9fITG5Rd9Iu9QunaMXixT%2BgTiKx8W%2Bo3%2BpZk6vPcyNSNqQeLrLExL7lT2qn1ITw8Hlb6Pw29QAmUazxcspxooQ8ioGzBEVezWUqO9qLp8dI%2Brw9qN8%2B710REoGf3X6lTF5JRow8JZ&X-Amz-Signature=a3dcdc157f68e19629892c816deb998be6fac345c01e010bc961ecdebb8872bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M3WF6IT%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYWYAo5vBF4Q3ePBPN%2F%2F7NfdgubQrDKcvwPgKEVS8tmAiBZ8q8ptpGTRdNPfRm3HtnwxbBiNDRUBLcQ%2B4%2B%2BmP%2BXKSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSQ%2BSQwgTrjmScHI%2BKtwDsuJQiYgpNAAT2XNspBfgB35BiV22n%2FW3HtaV4438oRsipdcSuMN0b3hVZ43PIJx77GV8yXIGTfENUGBy6CKK9OsEwNet9N%2FlfJqQI7Yti%2FzbQ9qHjH959N2H6jbbYkRc1qo3jk9SgL2P9yggvlCT4dMmRweSilbrXT93Sl%2B8BQ9z1O0Og9l9bHmVbrGp2a3cNx33CfWhdI6YiDIw9nZ%2BjBOH1o78%2BEsExLksUgmZ2gLpT0fLUWyX6La3C7ylQRdoDFhYrrYkEK7mfGV%2Fy8JNptPjfx%2BW2wm32HBR%2BP3r8mOvE%2FeyIASGcWvFYOFh63ZhsVKlZwpm8%2FfNKxcaXxElY13ybk%2B53LNA7dG7sZeMPNkn060MaRIa1IzgGHNCQrTvIFOyzNB8KLOZrf8jRZ2O%2FtN489DfMwRyjDE9JrbOx0CSR1CIbXt4x8poSBEVWK80SveS7%2Fd3tm%2FZiDoX5XJKsV9p76xRSR666VZWdWfIZE48cjS72u5Lpa1jcd%2FL%2BpM9kg3g4J3R%2FOrYy%2FMF0yWf9DleB2AvRlZXuYYqzT3OcFF%2F%2FVwOL1p5qH50%2BfKiphMKUfonNuhvTr0BoihZyG6KSEWLAVDQMK7ky4VNPwRk1FnRUqh1lfF5%2FykWnG4wp%2BqjyQY6pgFJZ1ffVD6tXLueQ7VtBIVHX3cxvnJn%2B6Hz0%2BWb9%2Ffo9tSf96O5rV7OpgG1oNE%2FZg3sBkesx5cdAWJSvJ%2FHIVH9fITG5Rd9Iu9QunaMXixT%2BgTiKx8W%2Bo3%2BpZk6vPcyNSNqQeLrLExL7lT2qn1ITw8Hlb6Pw29QAmUazxcspxooQ8ioGzBEVezWUqO9qLp8dI%2Brw9qN8%2B710REoGf3X6lTF5JRow8JZ&X-Amz-Signature=994a02ffe90b0aade276b39160dd6d586e6ad097b1f9b4264df8836c40dbd838&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M3WF6IT%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYWYAo5vBF4Q3ePBPN%2F%2F7NfdgubQrDKcvwPgKEVS8tmAiBZ8q8ptpGTRdNPfRm3HtnwxbBiNDRUBLcQ%2B4%2B%2BmP%2BXKSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSQ%2BSQwgTrjmScHI%2BKtwDsuJQiYgpNAAT2XNspBfgB35BiV22n%2FW3HtaV4438oRsipdcSuMN0b3hVZ43PIJx77GV8yXIGTfENUGBy6CKK9OsEwNet9N%2FlfJqQI7Yti%2FzbQ9qHjH959N2H6jbbYkRc1qo3jk9SgL2P9yggvlCT4dMmRweSilbrXT93Sl%2B8BQ9z1O0Og9l9bHmVbrGp2a3cNx33CfWhdI6YiDIw9nZ%2BjBOH1o78%2BEsExLksUgmZ2gLpT0fLUWyX6La3C7ylQRdoDFhYrrYkEK7mfGV%2Fy8JNptPjfx%2BW2wm32HBR%2BP3r8mOvE%2FeyIASGcWvFYOFh63ZhsVKlZwpm8%2FfNKxcaXxElY13ybk%2B53LNA7dG7sZeMPNkn060MaRIa1IzgGHNCQrTvIFOyzNB8KLOZrf8jRZ2O%2FtN489DfMwRyjDE9JrbOx0CSR1CIbXt4x8poSBEVWK80SveS7%2Fd3tm%2FZiDoX5XJKsV9p76xRSR666VZWdWfIZE48cjS72u5Lpa1jcd%2FL%2BpM9kg3g4J3R%2FOrYy%2FMF0yWf9DleB2AvRlZXuYYqzT3OcFF%2F%2FVwOL1p5qH50%2BfKiphMKUfonNuhvTr0BoihZyG6KSEWLAVDQMK7ky4VNPwRk1FnRUqh1lfF5%2FykWnG4wp%2BqjyQY6pgFJZ1ffVD6tXLueQ7VtBIVHX3cxvnJn%2B6Hz0%2BWb9%2Ffo9tSf96O5rV7OpgG1oNE%2FZg3sBkesx5cdAWJSvJ%2FHIVH9fITG5Rd9Iu9QunaMXixT%2BgTiKx8W%2Bo3%2BpZk6vPcyNSNqQeLrLExL7lT2qn1ITw8Hlb6Pw29QAmUazxcspxooQ8ioGzBEVezWUqO9qLp8dI%2Brw9qN8%2B710REoGf3X6lTF5JRow8JZ&X-Amz-Signature=174ac4585023ada480ca392c4e93939ff5a0cf8903ac5723fb0086b5b91d24f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664M3WF6IT%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYWYAo5vBF4Q3ePBPN%2F%2F7NfdgubQrDKcvwPgKEVS8tmAiBZ8q8ptpGTRdNPfRm3HtnwxbBiNDRUBLcQ%2B4%2B%2BmP%2BXKSqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSQ%2BSQwgTrjmScHI%2BKtwDsuJQiYgpNAAT2XNspBfgB35BiV22n%2FW3HtaV4438oRsipdcSuMN0b3hVZ43PIJx77GV8yXIGTfENUGBy6CKK9OsEwNet9N%2FlfJqQI7Yti%2FzbQ9qHjH959N2H6jbbYkRc1qo3jk9SgL2P9yggvlCT4dMmRweSilbrXT93Sl%2B8BQ9z1O0Og9l9bHmVbrGp2a3cNx33CfWhdI6YiDIw9nZ%2BjBOH1o78%2BEsExLksUgmZ2gLpT0fLUWyX6La3C7ylQRdoDFhYrrYkEK7mfGV%2Fy8JNptPjfx%2BW2wm32HBR%2BP3r8mOvE%2FeyIASGcWvFYOFh63ZhsVKlZwpm8%2FfNKxcaXxElY13ybk%2B53LNA7dG7sZeMPNkn060MaRIa1IzgGHNCQrTvIFOyzNB8KLOZrf8jRZ2O%2FtN489DfMwRyjDE9JrbOx0CSR1CIbXt4x8poSBEVWK80SveS7%2Fd3tm%2FZiDoX5XJKsV9p76xRSR666VZWdWfIZE48cjS72u5Lpa1jcd%2FL%2BpM9kg3g4J3R%2FOrYy%2FMF0yWf9DleB2AvRlZXuYYqzT3OcFF%2F%2FVwOL1p5qH50%2BfKiphMKUfonNuhvTr0BoihZyG6KSEWLAVDQMK7ky4VNPwRk1FnRUqh1lfF5%2FykWnG4wp%2BqjyQY6pgFJZ1ffVD6tXLueQ7VtBIVHX3cxvnJn%2B6Hz0%2BWb9%2Ffo9tSf96O5rV7OpgG1oNE%2FZg3sBkesx5cdAWJSvJ%2FHIVH9fITG5Rd9Iu9QunaMXixT%2BgTiKx8W%2Bo3%2BpZk6vPcyNSNqQeLrLExL7lT2qn1ITw8Hlb6Pw29QAmUazxcspxooQ8ioGzBEVezWUqO9qLp8dI%2Brw9qN8%2B710REoGf3X6lTF5JRow8JZ&X-Amz-Signature=0df2c0f79dbfb82c3480f8526df1a7096ba99158cce712d384e2f433051590c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



