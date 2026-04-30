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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZLHL2O%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQC%2F5CYBS4hGD07O8HU6HbBsvlOzEtxGluKaSQlCGJNP%2FgIhAOkn%2F97y%2BHYSr0qXGQtW%2BWKidKuLozVW2U0kKCNysTNrKv8DCAkQABoMNjM3NDIzMTgzODA1IgyAHCNPVUd%2BxX%2FVCDQq3ANIOe67TqitbYPOECeGmxYZILeGwZrsgQcojA9wMX%2B%2F2pCurhVMjvkN7LlqnPGw%2FEe66SpXu%2BCpgkxSUTyoygdiZkHbCx0vhHXADpTwjqss20gblEY8jsA3xemre8yh4ELWUT5JwetJNHy9H21K8OQb%2F6hrc33%2BPrCjGR6p%2Bkd%2B3Dd7c80G7YELHVXZnE5iZhr9HO9ylMgoi9dc%2FRzKC6ec%2BHrHH00ODxzEzdxP9kTGtFszuU712xkCgCoItDMCIAKWkNtE9AD3Uv%2BQQ02jNIM5B20Yaa%2BQXwH8qjSD%2BVV0e2b8wULj2OSdidj53W5LiVTiTVzc23qkGuiXrpzEiubeB28hmX2iEug0n7RsTpSXZfiAmJFhV9Z2ElIfw4BldDhZZZcufpOwFirr5%2FcdT7cFNmw59KhU3xotmmiJRxdsbCsBy1AFNuTrL4p4EbKIocGVtWzVYCUYdkEwPyiTonSEduu9jUaK%2FGyRKnnU5oG6Xuiu8SPQ2LtEYAX0rIt9SSRlc4Ngz51vwXJ2uF%2BrIJMXt351J60BjwGCkFDk7FTMXdNTqwjDNhgcnIHhlSaOV0cVfUr1KTLLHCdkZI0K0HtjjDhs8k3JGHEPeBJToNOwaqGiACCmATQb7pp0djC0m8zPBjqkAV2aHeai0S81mngzeo2xhJdPdld7TrO0kJtBfrv1%2BLXNk2%2FgL0BzLRp60gnGDvwd%2F8iY7aZZQq6jtKSGOW8oI%2B2rm5Ad%2BK1fAa81%2BzmtWswF1p8AcxbnCp9z2%2BaAWTKnzQTRFaCTyX%2FFLAjuKYT4TcV2M4VwBzpo7nWWcJS%2FQessUSYZdhmqPRQjMmKCpDHb7i6M28oOxMDpCb38uKjvfApWWg3G&X-Amz-Signature=698439cbfd2dbdf69430a2289c9e8a366fc90b5c08f0574c5cfdad15684083c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZLHL2O%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQC%2F5CYBS4hGD07O8HU6HbBsvlOzEtxGluKaSQlCGJNP%2FgIhAOkn%2F97y%2BHYSr0qXGQtW%2BWKidKuLozVW2U0kKCNysTNrKv8DCAkQABoMNjM3NDIzMTgzODA1IgyAHCNPVUd%2BxX%2FVCDQq3ANIOe67TqitbYPOECeGmxYZILeGwZrsgQcojA9wMX%2B%2F2pCurhVMjvkN7LlqnPGw%2FEe66SpXu%2BCpgkxSUTyoygdiZkHbCx0vhHXADpTwjqss20gblEY8jsA3xemre8yh4ELWUT5JwetJNHy9H21K8OQb%2F6hrc33%2BPrCjGR6p%2Bkd%2B3Dd7c80G7YELHVXZnE5iZhr9HO9ylMgoi9dc%2FRzKC6ec%2BHrHH00ODxzEzdxP9kTGtFszuU712xkCgCoItDMCIAKWkNtE9AD3Uv%2BQQ02jNIM5B20Yaa%2BQXwH8qjSD%2BVV0e2b8wULj2OSdidj53W5LiVTiTVzc23qkGuiXrpzEiubeB28hmX2iEug0n7RsTpSXZfiAmJFhV9Z2ElIfw4BldDhZZZcufpOwFirr5%2FcdT7cFNmw59KhU3xotmmiJRxdsbCsBy1AFNuTrL4p4EbKIocGVtWzVYCUYdkEwPyiTonSEduu9jUaK%2FGyRKnnU5oG6Xuiu8SPQ2LtEYAX0rIt9SSRlc4Ngz51vwXJ2uF%2BrIJMXt351J60BjwGCkFDk7FTMXdNTqwjDNhgcnIHhlSaOV0cVfUr1KTLLHCdkZI0K0HtjjDhs8k3JGHEPeBJToNOwaqGiACCmATQb7pp0djC0m8zPBjqkAV2aHeai0S81mngzeo2xhJdPdld7TrO0kJtBfrv1%2BLXNk2%2FgL0BzLRp60gnGDvwd%2F8iY7aZZQq6jtKSGOW8oI%2B2rm5Ad%2BK1fAa81%2BzmtWswF1p8AcxbnCp9z2%2BaAWTKnzQTRFaCTyX%2FFLAjuKYT4TcV2M4VwBzpo7nWWcJS%2FQessUSYZdhmqPRQjMmKCpDHb7i6M28oOxMDpCb38uKjvfApWWg3G&X-Amz-Signature=0081b3152ac644902ac6c631f33413ed87a63eea6df11553a05de6d2570fb50b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZLHL2O%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQC%2F5CYBS4hGD07O8HU6HbBsvlOzEtxGluKaSQlCGJNP%2FgIhAOkn%2F97y%2BHYSr0qXGQtW%2BWKidKuLozVW2U0kKCNysTNrKv8DCAkQABoMNjM3NDIzMTgzODA1IgyAHCNPVUd%2BxX%2FVCDQq3ANIOe67TqitbYPOECeGmxYZILeGwZrsgQcojA9wMX%2B%2F2pCurhVMjvkN7LlqnPGw%2FEe66SpXu%2BCpgkxSUTyoygdiZkHbCx0vhHXADpTwjqss20gblEY8jsA3xemre8yh4ELWUT5JwetJNHy9H21K8OQb%2F6hrc33%2BPrCjGR6p%2Bkd%2B3Dd7c80G7YELHVXZnE5iZhr9HO9ylMgoi9dc%2FRzKC6ec%2BHrHH00ODxzEzdxP9kTGtFszuU712xkCgCoItDMCIAKWkNtE9AD3Uv%2BQQ02jNIM5B20Yaa%2BQXwH8qjSD%2BVV0e2b8wULj2OSdidj53W5LiVTiTVzc23qkGuiXrpzEiubeB28hmX2iEug0n7RsTpSXZfiAmJFhV9Z2ElIfw4BldDhZZZcufpOwFirr5%2FcdT7cFNmw59KhU3xotmmiJRxdsbCsBy1AFNuTrL4p4EbKIocGVtWzVYCUYdkEwPyiTonSEduu9jUaK%2FGyRKnnU5oG6Xuiu8SPQ2LtEYAX0rIt9SSRlc4Ngz51vwXJ2uF%2BrIJMXt351J60BjwGCkFDk7FTMXdNTqwjDNhgcnIHhlSaOV0cVfUr1KTLLHCdkZI0K0HtjjDhs8k3JGHEPeBJToNOwaqGiACCmATQb7pp0djC0m8zPBjqkAV2aHeai0S81mngzeo2xhJdPdld7TrO0kJtBfrv1%2BLXNk2%2FgL0BzLRp60gnGDvwd%2F8iY7aZZQq6jtKSGOW8oI%2B2rm5Ad%2BK1fAa81%2BzmtWswF1p8AcxbnCp9z2%2BaAWTKnzQTRFaCTyX%2FFLAjuKYT4TcV2M4VwBzpo7nWWcJS%2FQessUSYZdhmqPRQjMmKCpDHb7i6M28oOxMDpCb38uKjvfApWWg3G&X-Amz-Signature=bccf8d42620e9f2131ef9394dcbcf6cc2149442a767877975ae389caea4c6003&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZLHL2O%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQC%2F5CYBS4hGD07O8HU6HbBsvlOzEtxGluKaSQlCGJNP%2FgIhAOkn%2F97y%2BHYSr0qXGQtW%2BWKidKuLozVW2U0kKCNysTNrKv8DCAkQABoMNjM3NDIzMTgzODA1IgyAHCNPVUd%2BxX%2FVCDQq3ANIOe67TqitbYPOECeGmxYZILeGwZrsgQcojA9wMX%2B%2F2pCurhVMjvkN7LlqnPGw%2FEe66SpXu%2BCpgkxSUTyoygdiZkHbCx0vhHXADpTwjqss20gblEY8jsA3xemre8yh4ELWUT5JwetJNHy9H21K8OQb%2F6hrc33%2BPrCjGR6p%2Bkd%2B3Dd7c80G7YELHVXZnE5iZhr9HO9ylMgoi9dc%2FRzKC6ec%2BHrHH00ODxzEzdxP9kTGtFszuU712xkCgCoItDMCIAKWkNtE9AD3Uv%2BQQ02jNIM5B20Yaa%2BQXwH8qjSD%2BVV0e2b8wULj2OSdidj53W5LiVTiTVzc23qkGuiXrpzEiubeB28hmX2iEug0n7RsTpSXZfiAmJFhV9Z2ElIfw4BldDhZZZcufpOwFirr5%2FcdT7cFNmw59KhU3xotmmiJRxdsbCsBy1AFNuTrL4p4EbKIocGVtWzVYCUYdkEwPyiTonSEduu9jUaK%2FGyRKnnU5oG6Xuiu8SPQ2LtEYAX0rIt9SSRlc4Ngz51vwXJ2uF%2BrIJMXt351J60BjwGCkFDk7FTMXdNTqwjDNhgcnIHhlSaOV0cVfUr1KTLLHCdkZI0K0HtjjDhs8k3JGHEPeBJToNOwaqGiACCmATQb7pp0djC0m8zPBjqkAV2aHeai0S81mngzeo2xhJdPdld7TrO0kJtBfrv1%2BLXNk2%2FgL0BzLRp60gnGDvwd%2F8iY7aZZQq6jtKSGOW8oI%2B2rm5Ad%2BK1fAa81%2BzmtWswF1p8AcxbnCp9z2%2BaAWTKnzQTRFaCTyX%2FFLAjuKYT4TcV2M4VwBzpo7nWWcJS%2FQessUSYZdhmqPRQjMmKCpDHb7i6M28oOxMDpCb38uKjvfApWWg3G&X-Amz-Signature=16edac1a83743e65bfd12c50063fb709b5085940655b614b3a71dea96e07dc3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



