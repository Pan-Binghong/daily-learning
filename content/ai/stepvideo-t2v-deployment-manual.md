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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZWKWRPI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdU4QLlwXrazyS6gpPxQmRDk7bW3PbgjkwwloifsI9wAiEAu82Ea08V6SXFfTtpOfXd%2FQHE%2FTjNlAN4uyODcNjQGCkq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEs0Lh2pQozl7os22SrcA8Kbgt4Iq63mYKzy55hWblUjgY%2Fo7SgljXBEGkSq%2BisaLrATsMRCfEUgUAt7ipFIZlB2bvv4kXf%2BdrPQrtC4S%2BjXefimD8j%2BzRi40MMP4pSMhUeAw4jPJ4aLodWpIWNJ5hAdXTTB7Antg%2B%2F7Sx6%2FbI53%2FTohf3CrAygwTIdJjhmlJjORlLUMJD4XuyvSi%2FLsx2C0aXj7okrZON8T%2BuoUUPEwxLCGFWMGMeuIJ0E6TGcQ59PZoI%2B4GocqsEnMq3DVLahiSHIAaGTnPofO%2FN7bvRcQYPHPFAG3rEVApMZzHBNj2DDcCZkEiT7t6o74NCPA8cTW32mh2CM9jqg90fxFU%2FdsPJln%2FXwxRA4p792kZz97IoQSZ%2FyavGekzrvwLHgsup8jAbRi8Hu4c5PZE0xoEiHkGIPHBwiLR36oiqBAfecaeUV32qf18XYWMwDJNZIS1mHacpL%2FRdcIATwZsOWXJweZbnLVWVkLMFc9vYE8RaU0%2B52Ph519Ub8KeXOChTFH6Dr3PN4vDt5w2IJiznV7Pai6zwiGETExX2O6tO0LX4fIynFp0H6MyfvtymCPA9KmNkr9cJVFx%2BX6SpkTEj3DT8BlK9uJMLJqvG6jWQkceHr1%2FKHhiyDgQeuHjLpBMMny2cwGOqUBQZx9Nc0G2gEYCu4E7W4RZOlhA%2FXbT68kiVu8SQBxMnbrXYIX8atn%2BUhB80914FOTZjg2ZgFXHGoOs1fmZdtt13KUf1oytRmZlBxt%2BYle4AlgNZGHF37%2F0AE5C1Uq2LPc4AAU4d42Gvez%2F%2FfZKLm7s3LVXHD3y0VRkALT3Vx7vRAjmdG41e7X3VhyLugnV7rgDH4rA7HFyuP4kDT7BxG5rXkJZf6o&X-Amz-Signature=ce8e4c849254c91f1185c341677d804bba73bb6af4b34983463cbf89467dc9ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZWKWRPI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdU4QLlwXrazyS6gpPxQmRDk7bW3PbgjkwwloifsI9wAiEAu82Ea08V6SXFfTtpOfXd%2FQHE%2FTjNlAN4uyODcNjQGCkq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEs0Lh2pQozl7os22SrcA8Kbgt4Iq63mYKzy55hWblUjgY%2Fo7SgljXBEGkSq%2BisaLrATsMRCfEUgUAt7ipFIZlB2bvv4kXf%2BdrPQrtC4S%2BjXefimD8j%2BzRi40MMP4pSMhUeAw4jPJ4aLodWpIWNJ5hAdXTTB7Antg%2B%2F7Sx6%2FbI53%2FTohf3CrAygwTIdJjhmlJjORlLUMJD4XuyvSi%2FLsx2C0aXj7okrZON8T%2BuoUUPEwxLCGFWMGMeuIJ0E6TGcQ59PZoI%2B4GocqsEnMq3DVLahiSHIAaGTnPofO%2FN7bvRcQYPHPFAG3rEVApMZzHBNj2DDcCZkEiT7t6o74NCPA8cTW32mh2CM9jqg90fxFU%2FdsPJln%2FXwxRA4p792kZz97IoQSZ%2FyavGekzrvwLHgsup8jAbRi8Hu4c5PZE0xoEiHkGIPHBwiLR36oiqBAfecaeUV32qf18XYWMwDJNZIS1mHacpL%2FRdcIATwZsOWXJweZbnLVWVkLMFc9vYE8RaU0%2B52Ph519Ub8KeXOChTFH6Dr3PN4vDt5w2IJiznV7Pai6zwiGETExX2O6tO0LX4fIynFp0H6MyfvtymCPA9KmNkr9cJVFx%2BX6SpkTEj3DT8BlK9uJMLJqvG6jWQkceHr1%2FKHhiyDgQeuHjLpBMMny2cwGOqUBQZx9Nc0G2gEYCu4E7W4RZOlhA%2FXbT68kiVu8SQBxMnbrXYIX8atn%2BUhB80914FOTZjg2ZgFXHGoOs1fmZdtt13KUf1oytRmZlBxt%2BYle4AlgNZGHF37%2F0AE5C1Uq2LPc4AAU4d42Gvez%2F%2FfZKLm7s3LVXHD3y0VRkALT3Vx7vRAjmdG41e7X3VhyLugnV7rgDH4rA7HFyuP4kDT7BxG5rXkJZf6o&X-Amz-Signature=84c9a03fb845e53ef96275f2cc0668213d86e31aa36aa38c569390c33bcb1f27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZWKWRPI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdU4QLlwXrazyS6gpPxQmRDk7bW3PbgjkwwloifsI9wAiEAu82Ea08V6SXFfTtpOfXd%2FQHE%2FTjNlAN4uyODcNjQGCkq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEs0Lh2pQozl7os22SrcA8Kbgt4Iq63mYKzy55hWblUjgY%2Fo7SgljXBEGkSq%2BisaLrATsMRCfEUgUAt7ipFIZlB2bvv4kXf%2BdrPQrtC4S%2BjXefimD8j%2BzRi40MMP4pSMhUeAw4jPJ4aLodWpIWNJ5hAdXTTB7Antg%2B%2F7Sx6%2FbI53%2FTohf3CrAygwTIdJjhmlJjORlLUMJD4XuyvSi%2FLsx2C0aXj7okrZON8T%2BuoUUPEwxLCGFWMGMeuIJ0E6TGcQ59PZoI%2B4GocqsEnMq3DVLahiSHIAaGTnPofO%2FN7bvRcQYPHPFAG3rEVApMZzHBNj2DDcCZkEiT7t6o74NCPA8cTW32mh2CM9jqg90fxFU%2FdsPJln%2FXwxRA4p792kZz97IoQSZ%2FyavGekzrvwLHgsup8jAbRi8Hu4c5PZE0xoEiHkGIPHBwiLR36oiqBAfecaeUV32qf18XYWMwDJNZIS1mHacpL%2FRdcIATwZsOWXJweZbnLVWVkLMFc9vYE8RaU0%2B52Ph519Ub8KeXOChTFH6Dr3PN4vDt5w2IJiznV7Pai6zwiGETExX2O6tO0LX4fIynFp0H6MyfvtymCPA9KmNkr9cJVFx%2BX6SpkTEj3DT8BlK9uJMLJqvG6jWQkceHr1%2FKHhiyDgQeuHjLpBMMny2cwGOqUBQZx9Nc0G2gEYCu4E7W4RZOlhA%2FXbT68kiVu8SQBxMnbrXYIX8atn%2BUhB80914FOTZjg2ZgFXHGoOs1fmZdtt13KUf1oytRmZlBxt%2BYle4AlgNZGHF37%2F0AE5C1Uq2LPc4AAU4d42Gvez%2F%2FfZKLm7s3LVXHD3y0VRkALT3Vx7vRAjmdG41e7X3VhyLugnV7rgDH4rA7HFyuP4kDT7BxG5rXkJZf6o&X-Amz-Signature=30335f862a74ca7f115392445b33161e5f31424dc4518c55886b32213843ee43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZWKWRPI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEdU4QLlwXrazyS6gpPxQmRDk7bW3PbgjkwwloifsI9wAiEAu82Ea08V6SXFfTtpOfXd%2FQHE%2FTjNlAN4uyODcNjQGCkq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEs0Lh2pQozl7os22SrcA8Kbgt4Iq63mYKzy55hWblUjgY%2Fo7SgljXBEGkSq%2BisaLrATsMRCfEUgUAt7ipFIZlB2bvv4kXf%2BdrPQrtC4S%2BjXefimD8j%2BzRi40MMP4pSMhUeAw4jPJ4aLodWpIWNJ5hAdXTTB7Antg%2B%2F7Sx6%2FbI53%2FTohf3CrAygwTIdJjhmlJjORlLUMJD4XuyvSi%2FLsx2C0aXj7okrZON8T%2BuoUUPEwxLCGFWMGMeuIJ0E6TGcQ59PZoI%2B4GocqsEnMq3DVLahiSHIAaGTnPofO%2FN7bvRcQYPHPFAG3rEVApMZzHBNj2DDcCZkEiT7t6o74NCPA8cTW32mh2CM9jqg90fxFU%2FdsPJln%2FXwxRA4p792kZz97IoQSZ%2FyavGekzrvwLHgsup8jAbRi8Hu4c5PZE0xoEiHkGIPHBwiLR36oiqBAfecaeUV32qf18XYWMwDJNZIS1mHacpL%2FRdcIATwZsOWXJweZbnLVWVkLMFc9vYE8RaU0%2B52Ph519Ub8KeXOChTFH6Dr3PN4vDt5w2IJiznV7Pai6zwiGETExX2O6tO0LX4fIynFp0H6MyfvtymCPA9KmNkr9cJVFx%2BX6SpkTEj3DT8BlK9uJMLJqvG6jWQkceHr1%2FKHhiyDgQeuHjLpBMMny2cwGOqUBQZx9Nc0G2gEYCu4E7W4RZOlhA%2FXbT68kiVu8SQBxMnbrXYIX8atn%2BUhB80914FOTZjg2ZgFXHGoOs1fmZdtt13KUf1oytRmZlBxt%2BYle4AlgNZGHF37%2F0AE5C1Uq2LPc4AAU4d42Gvez%2F%2FfZKLm7s3LVXHD3y0VRkALT3Vx7vRAjmdG41e7X3VhyLugnV7rgDH4rA7HFyuP4kDT7BxG5rXkJZf6o&X-Amz-Signature=7754b19000d1e48b6027747b991b2eb4ce40b8d6cfbbc66a312bc39bfaa2df3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



