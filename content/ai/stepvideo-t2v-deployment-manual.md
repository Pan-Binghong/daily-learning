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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GRVXRB%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0SC%2FRftlXov4F28aw3%2Fl%2FfOC3ZclyGDkz1N0ah2cD3AiEAnXZffjpF%2B%2FiSgIDEVM7nmB9g6LmY%2Fiig28Thjs6rG7oqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDo1ohHF2VbIcj14wSrcA5zBVI3h4h9YCOmsglHYl48tHaOvOGQsUYI%2FrpdjjFTbahbhGQh2ZV6E1YQ5QsOiPJidyTuYhlYtLGBCx7vszL2ILTMvscdV%2BVxqU3iz8G5KUdaNsRYRJWfB%2FxDqAZwwGdNba1sp187336WkQCVtiJNedv7DKGv9qZ84hTkvXOXB9nOTu152V1b0O7DPejSpw2fXVTrMi1QJGyAQ2Z9Ryx0lC5TtxZykRYj7aiStBgHWueyirLQwJO5WYKpaGzCkRdaXhj8I4yc9XEtl9gQ4b55OQQ8wSQgpCdSkknKBvRWE75GoVtrxPEiN15%2BmvKw0L1T9a%2B5mnJCHxrNQ2Wf1%2BJw9gxEn8KUsX0FaEj7mCWcMbg41MXsScehYM8by9FMJEw%2B%2BKext6z%2BWvQcxO0bN6AMSKigex8FNjw6ekK4aDPZFLq9SsElf0VwDuLF%2FYsINGb%2B%2FwdAnrPIzalx4%2BPsAFVr6JTuEJIhbVROh3KX2GdVPwGfmZWxMJSe8XoNxuQwn8%2FixAJATUcRmKtCYNPICcJb3BNTdV9uvcaNnyryPqrO8FWLFpH02RoxlICDub2DKxzLisSi863k5H9d9emdrzOcFjHZXMRTdqAfJwlU8uSeqGE4lRb8s82Pkc68sMKOq%2FMoGOqUByNDx4L7mK5lFrkwePidLP%2BtR1ue25Nh6v46Fivy752UTdWPP8pqqC%2FP7AunyjwoEvXRkb1jAxwJztfb47HLf05AVQfyV1RhFmEsTUkPKeqmCiS0YNWiIrk8dUQvkkWeBZPTCNDMHMVa2Y2upo2qhy7Z1daLgbaSRZGwu2tV1yUyaT%2Bj%2F%2FglmGrQMuFdWEO6dj%2BfaQNV5V49CqxqPSk6eohs7o5EO&X-Amz-Signature=e8a3c9173ecdc294202376f990ce012dc790168546613d4754b3b7773e7e7d7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GRVXRB%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0SC%2FRftlXov4F28aw3%2Fl%2FfOC3ZclyGDkz1N0ah2cD3AiEAnXZffjpF%2B%2FiSgIDEVM7nmB9g6LmY%2Fiig28Thjs6rG7oqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDo1ohHF2VbIcj14wSrcA5zBVI3h4h9YCOmsglHYl48tHaOvOGQsUYI%2FrpdjjFTbahbhGQh2ZV6E1YQ5QsOiPJidyTuYhlYtLGBCx7vszL2ILTMvscdV%2BVxqU3iz8G5KUdaNsRYRJWfB%2FxDqAZwwGdNba1sp187336WkQCVtiJNedv7DKGv9qZ84hTkvXOXB9nOTu152V1b0O7DPejSpw2fXVTrMi1QJGyAQ2Z9Ryx0lC5TtxZykRYj7aiStBgHWueyirLQwJO5WYKpaGzCkRdaXhj8I4yc9XEtl9gQ4b55OQQ8wSQgpCdSkknKBvRWE75GoVtrxPEiN15%2BmvKw0L1T9a%2B5mnJCHxrNQ2Wf1%2BJw9gxEn8KUsX0FaEj7mCWcMbg41MXsScehYM8by9FMJEw%2B%2BKext6z%2BWvQcxO0bN6AMSKigex8FNjw6ekK4aDPZFLq9SsElf0VwDuLF%2FYsINGb%2B%2FwdAnrPIzalx4%2BPsAFVr6JTuEJIhbVROh3KX2GdVPwGfmZWxMJSe8XoNxuQwn8%2FixAJATUcRmKtCYNPICcJb3BNTdV9uvcaNnyryPqrO8FWLFpH02RoxlICDub2DKxzLisSi863k5H9d9emdrzOcFjHZXMRTdqAfJwlU8uSeqGE4lRb8s82Pkc68sMKOq%2FMoGOqUByNDx4L7mK5lFrkwePidLP%2BtR1ue25Nh6v46Fivy752UTdWPP8pqqC%2FP7AunyjwoEvXRkb1jAxwJztfb47HLf05AVQfyV1RhFmEsTUkPKeqmCiS0YNWiIrk8dUQvkkWeBZPTCNDMHMVa2Y2upo2qhy7Z1daLgbaSRZGwu2tV1yUyaT%2Bj%2F%2FglmGrQMuFdWEO6dj%2BfaQNV5V49CqxqPSk6eohs7o5EO&X-Amz-Signature=89a38f3a9afb58a7c0fbd3e9652d1270fb1c1c6de3880b8127b3ba192c6f3a46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GRVXRB%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0SC%2FRftlXov4F28aw3%2Fl%2FfOC3ZclyGDkz1N0ah2cD3AiEAnXZffjpF%2B%2FiSgIDEVM7nmB9g6LmY%2Fiig28Thjs6rG7oqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDo1ohHF2VbIcj14wSrcA5zBVI3h4h9YCOmsglHYl48tHaOvOGQsUYI%2FrpdjjFTbahbhGQh2ZV6E1YQ5QsOiPJidyTuYhlYtLGBCx7vszL2ILTMvscdV%2BVxqU3iz8G5KUdaNsRYRJWfB%2FxDqAZwwGdNba1sp187336WkQCVtiJNedv7DKGv9qZ84hTkvXOXB9nOTu152V1b0O7DPejSpw2fXVTrMi1QJGyAQ2Z9Ryx0lC5TtxZykRYj7aiStBgHWueyirLQwJO5WYKpaGzCkRdaXhj8I4yc9XEtl9gQ4b55OQQ8wSQgpCdSkknKBvRWE75GoVtrxPEiN15%2BmvKw0L1T9a%2B5mnJCHxrNQ2Wf1%2BJw9gxEn8KUsX0FaEj7mCWcMbg41MXsScehYM8by9FMJEw%2B%2BKext6z%2BWvQcxO0bN6AMSKigex8FNjw6ekK4aDPZFLq9SsElf0VwDuLF%2FYsINGb%2B%2FwdAnrPIzalx4%2BPsAFVr6JTuEJIhbVROh3KX2GdVPwGfmZWxMJSe8XoNxuQwn8%2FixAJATUcRmKtCYNPICcJb3BNTdV9uvcaNnyryPqrO8FWLFpH02RoxlICDub2DKxzLisSi863k5H9d9emdrzOcFjHZXMRTdqAfJwlU8uSeqGE4lRb8s82Pkc68sMKOq%2FMoGOqUByNDx4L7mK5lFrkwePidLP%2BtR1ue25Nh6v46Fivy752UTdWPP8pqqC%2FP7AunyjwoEvXRkb1jAxwJztfb47HLf05AVQfyV1RhFmEsTUkPKeqmCiS0YNWiIrk8dUQvkkWeBZPTCNDMHMVa2Y2upo2qhy7Z1daLgbaSRZGwu2tV1yUyaT%2Bj%2F%2FglmGrQMuFdWEO6dj%2BfaQNV5V49CqxqPSk6eohs7o5EO&X-Amz-Signature=c29907ce92c5335817c0a38a0bf1588051bd9121cc4b8dd56317b8730eeb2a0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GRVXRB%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0SC%2FRftlXov4F28aw3%2Fl%2FfOC3ZclyGDkz1N0ah2cD3AiEAnXZffjpF%2B%2FiSgIDEVM7nmB9g6LmY%2Fiig28Thjs6rG7oqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDo1ohHF2VbIcj14wSrcA5zBVI3h4h9YCOmsglHYl48tHaOvOGQsUYI%2FrpdjjFTbahbhGQh2ZV6E1YQ5QsOiPJidyTuYhlYtLGBCx7vszL2ILTMvscdV%2BVxqU3iz8G5KUdaNsRYRJWfB%2FxDqAZwwGdNba1sp187336WkQCVtiJNedv7DKGv9qZ84hTkvXOXB9nOTu152V1b0O7DPejSpw2fXVTrMi1QJGyAQ2Z9Ryx0lC5TtxZykRYj7aiStBgHWueyirLQwJO5WYKpaGzCkRdaXhj8I4yc9XEtl9gQ4b55OQQ8wSQgpCdSkknKBvRWE75GoVtrxPEiN15%2BmvKw0L1T9a%2B5mnJCHxrNQ2Wf1%2BJw9gxEn8KUsX0FaEj7mCWcMbg41MXsScehYM8by9FMJEw%2B%2BKext6z%2BWvQcxO0bN6AMSKigex8FNjw6ekK4aDPZFLq9SsElf0VwDuLF%2FYsINGb%2B%2FwdAnrPIzalx4%2BPsAFVr6JTuEJIhbVROh3KX2GdVPwGfmZWxMJSe8XoNxuQwn8%2FixAJATUcRmKtCYNPICcJb3BNTdV9uvcaNnyryPqrO8FWLFpH02RoxlICDub2DKxzLisSi863k5H9d9emdrzOcFjHZXMRTdqAfJwlU8uSeqGE4lRb8s82Pkc68sMKOq%2FMoGOqUByNDx4L7mK5lFrkwePidLP%2BtR1ue25Nh6v46Fivy752UTdWPP8pqqC%2FP7AunyjwoEvXRkb1jAxwJztfb47HLf05AVQfyV1RhFmEsTUkPKeqmCiS0YNWiIrk8dUQvkkWeBZPTCNDMHMVa2Y2upo2qhy7Z1daLgbaSRZGwu2tV1yUyaT%2Bj%2F%2FglmGrQMuFdWEO6dj%2BfaQNV5V49CqxqPSk6eohs7o5EO&X-Amz-Signature=0647de3a4279c97a8b061e8ad6e24700686c37eaa7fe7bf9e8c12b7efc714c1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



