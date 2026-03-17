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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROPKS5Z3%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCaD6QU2xA%2Fu%2BaOXY1XI8yUbC6EZO73bTO6FjhjhsuZjgIgfcHtFxlI%2BpeO%2Bti90KHLBJQySRVNe5e7%2F7kloR%2FkbE8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgOpIoTsLsVP4%2Fu2ircA43zrz1QhZJJJyX8APkNHAy0gPoMeZATGSCc0HSrR3JGL7KhtEWFdyDdKMb1EbCbHv6Tb%2BMCF%2FHajlVgpG%2FVlPxko%2FPOznm98waWBWvecw5CqMyysSZ2%2FVskjhQCqfyiBpgmKhAe9bW6aoTCZ7%2BTCEls%2BMWVW0yAdr7bcZGhZriCfSK50X7eEqE8e91gJQ9MDR%2BydML85kPrRsZPpLqXE%2Bp%2B7RryC7zEJrRkrsiKtyRwkCGd%2F9uy1gMchQdBTKwNiglPXMUnfvL%2Bkpg0cbPFg%2BrKubhaBJ9EtcsykrQ%2FomumvincTWZ%2FIHlpVmrIuwPw%2FCDFg1jDGl83jBHtHrKtwSCKvCAznSi8bRKCGUNvaIuNhsHxXeOb50mtahLckz4kwxgCLBqEUwE8zjFAGv7gFTxrQkn%2FazNIaAHJeM%2F0unbVPLePbPn8wPwFPQejVpL8HqEZ6fcKlG9tWmNwuAPXSEjIka8v3pnKObtXCbsWaqzKCSQeMPLsZKj0%2B7jxQ0adirVbvOHQKdWLNcfqtOBQwejt6OP2ScTyckiKk0zZwc74By9qgUEeaCu22JgKsGuf%2F9cwxCnLWN6O1Z%2F%2FSlqyAVL6ZcHY3WnrfNp0iFh1qTCGO2keJvTCe6HBGDuNMIjp4s0GOqUBLBiM57sQiTY2otcOhoIlIHuNGqpZNQw1Xsh3ODArPmhI46y3jgYLTOBVtX2TlvD5ezzx%2BWtjkQLLt1cBO4grZoiXKZng681jzG0Njh%2B20uRDFieNjxgLupVz6LeZVq3VYslvM02Ah0mamdHdRJf7xWq6B%2FFLCre1mt%2F6JCGMglco0DNCvdew8m0gpGZy7GLx2WljBLDz7f%2FPdoRrYwgITMSKGAgy&X-Amz-Signature=9763e82c4cb4b835cf991558fb942def67834fbddf2502b6fa15e9bd9495c7ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROPKS5Z3%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCaD6QU2xA%2Fu%2BaOXY1XI8yUbC6EZO73bTO6FjhjhsuZjgIgfcHtFxlI%2BpeO%2Bti90KHLBJQySRVNe5e7%2F7kloR%2FkbE8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgOpIoTsLsVP4%2Fu2ircA43zrz1QhZJJJyX8APkNHAy0gPoMeZATGSCc0HSrR3JGL7KhtEWFdyDdKMb1EbCbHv6Tb%2BMCF%2FHajlVgpG%2FVlPxko%2FPOznm98waWBWvecw5CqMyysSZ2%2FVskjhQCqfyiBpgmKhAe9bW6aoTCZ7%2BTCEls%2BMWVW0yAdr7bcZGhZriCfSK50X7eEqE8e91gJQ9MDR%2BydML85kPrRsZPpLqXE%2Bp%2B7RryC7zEJrRkrsiKtyRwkCGd%2F9uy1gMchQdBTKwNiglPXMUnfvL%2Bkpg0cbPFg%2BrKubhaBJ9EtcsykrQ%2FomumvincTWZ%2FIHlpVmrIuwPw%2FCDFg1jDGl83jBHtHrKtwSCKvCAznSi8bRKCGUNvaIuNhsHxXeOb50mtahLckz4kwxgCLBqEUwE8zjFAGv7gFTxrQkn%2FazNIaAHJeM%2F0unbVPLePbPn8wPwFPQejVpL8HqEZ6fcKlG9tWmNwuAPXSEjIka8v3pnKObtXCbsWaqzKCSQeMPLsZKj0%2B7jxQ0adirVbvOHQKdWLNcfqtOBQwejt6OP2ScTyckiKk0zZwc74By9qgUEeaCu22JgKsGuf%2F9cwxCnLWN6O1Z%2F%2FSlqyAVL6ZcHY3WnrfNp0iFh1qTCGO2keJvTCe6HBGDuNMIjp4s0GOqUBLBiM57sQiTY2otcOhoIlIHuNGqpZNQw1Xsh3ODArPmhI46y3jgYLTOBVtX2TlvD5ezzx%2BWtjkQLLt1cBO4grZoiXKZng681jzG0Njh%2B20uRDFieNjxgLupVz6LeZVq3VYslvM02Ah0mamdHdRJf7xWq6B%2FFLCre1mt%2F6JCGMglco0DNCvdew8m0gpGZy7GLx2WljBLDz7f%2FPdoRrYwgITMSKGAgy&X-Amz-Signature=32a6ecfed9ec620ebf590f3c509eaaf4c9d9ea6b86e2e7ae6a8ce3ccf82454e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROPKS5Z3%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCaD6QU2xA%2Fu%2BaOXY1XI8yUbC6EZO73bTO6FjhjhsuZjgIgfcHtFxlI%2BpeO%2Bti90KHLBJQySRVNe5e7%2F7kloR%2FkbE8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgOpIoTsLsVP4%2Fu2ircA43zrz1QhZJJJyX8APkNHAy0gPoMeZATGSCc0HSrR3JGL7KhtEWFdyDdKMb1EbCbHv6Tb%2BMCF%2FHajlVgpG%2FVlPxko%2FPOznm98waWBWvecw5CqMyysSZ2%2FVskjhQCqfyiBpgmKhAe9bW6aoTCZ7%2BTCEls%2BMWVW0yAdr7bcZGhZriCfSK50X7eEqE8e91gJQ9MDR%2BydML85kPrRsZPpLqXE%2Bp%2B7RryC7zEJrRkrsiKtyRwkCGd%2F9uy1gMchQdBTKwNiglPXMUnfvL%2Bkpg0cbPFg%2BrKubhaBJ9EtcsykrQ%2FomumvincTWZ%2FIHlpVmrIuwPw%2FCDFg1jDGl83jBHtHrKtwSCKvCAznSi8bRKCGUNvaIuNhsHxXeOb50mtahLckz4kwxgCLBqEUwE8zjFAGv7gFTxrQkn%2FazNIaAHJeM%2F0unbVPLePbPn8wPwFPQejVpL8HqEZ6fcKlG9tWmNwuAPXSEjIka8v3pnKObtXCbsWaqzKCSQeMPLsZKj0%2B7jxQ0adirVbvOHQKdWLNcfqtOBQwejt6OP2ScTyckiKk0zZwc74By9qgUEeaCu22JgKsGuf%2F9cwxCnLWN6O1Z%2F%2FSlqyAVL6ZcHY3WnrfNp0iFh1qTCGO2keJvTCe6HBGDuNMIjp4s0GOqUBLBiM57sQiTY2otcOhoIlIHuNGqpZNQw1Xsh3ODArPmhI46y3jgYLTOBVtX2TlvD5ezzx%2BWtjkQLLt1cBO4grZoiXKZng681jzG0Njh%2B20uRDFieNjxgLupVz6LeZVq3VYslvM02Ah0mamdHdRJf7xWq6B%2FFLCre1mt%2F6JCGMglco0DNCvdew8m0gpGZy7GLx2WljBLDz7f%2FPdoRrYwgITMSKGAgy&X-Amz-Signature=daaf77734a5c4a1fc0e017b871b6dee05029dcb70eb6f2f54cf28a1589cd864d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROPKS5Z3%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCaD6QU2xA%2Fu%2BaOXY1XI8yUbC6EZO73bTO6FjhjhsuZjgIgfcHtFxlI%2BpeO%2Bti90KHLBJQySRVNe5e7%2F7kloR%2FkbE8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgOpIoTsLsVP4%2Fu2ircA43zrz1QhZJJJyX8APkNHAy0gPoMeZATGSCc0HSrR3JGL7KhtEWFdyDdKMb1EbCbHv6Tb%2BMCF%2FHajlVgpG%2FVlPxko%2FPOznm98waWBWvecw5CqMyysSZ2%2FVskjhQCqfyiBpgmKhAe9bW6aoTCZ7%2BTCEls%2BMWVW0yAdr7bcZGhZriCfSK50X7eEqE8e91gJQ9MDR%2BydML85kPrRsZPpLqXE%2Bp%2B7RryC7zEJrRkrsiKtyRwkCGd%2F9uy1gMchQdBTKwNiglPXMUnfvL%2Bkpg0cbPFg%2BrKubhaBJ9EtcsykrQ%2FomumvincTWZ%2FIHlpVmrIuwPw%2FCDFg1jDGl83jBHtHrKtwSCKvCAznSi8bRKCGUNvaIuNhsHxXeOb50mtahLckz4kwxgCLBqEUwE8zjFAGv7gFTxrQkn%2FazNIaAHJeM%2F0unbVPLePbPn8wPwFPQejVpL8HqEZ6fcKlG9tWmNwuAPXSEjIka8v3pnKObtXCbsWaqzKCSQeMPLsZKj0%2B7jxQ0adirVbvOHQKdWLNcfqtOBQwejt6OP2ScTyckiKk0zZwc74By9qgUEeaCu22JgKsGuf%2F9cwxCnLWN6O1Z%2F%2FSlqyAVL6ZcHY3WnrfNp0iFh1qTCGO2keJvTCe6HBGDuNMIjp4s0GOqUBLBiM57sQiTY2otcOhoIlIHuNGqpZNQw1Xsh3ODArPmhI46y3jgYLTOBVtX2TlvD5ezzx%2BWtjkQLLt1cBO4grZoiXKZng681jzG0Njh%2B20uRDFieNjxgLupVz6LeZVq3VYslvM02Ah0mamdHdRJf7xWq6B%2FFLCre1mt%2F6JCGMglco0DNCvdew8m0gpGZy7GLx2WljBLDz7f%2FPdoRrYwgITMSKGAgy&X-Amz-Signature=c19a8e9c3b5d0cb81510b182ffaaf5a234aa01bf357ddca60873d1e4b68ab4b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



