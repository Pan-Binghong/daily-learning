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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666GEG4PD%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fzm09o1Ur5JB%2FpIn1nlzwdbXtWkQxafIskg0hRWP2XAIgITLDV4Nfaa%2F%2BboejPHkjJTMw6iLsa9Mf%2FSTAis9TiYoqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2FYfnmVUzoq6Z7fBSrcA1vaisJJbba1%2F0InaqbX7IOR20jGZZf8JpTAX4pNs5rSzXLxZ0Q1MHTJL%2B97Cj5mk5aKXc5GIwnyb1LcwWL5WkpcJHIJEVb7BH%2FuIjQFlKhDQ%2FQxPholaJThRLBOt%2FpyRd0kBRdmkSo7dRp3CKg31hEzVl5ZymplMts2APMyDTqjrTbY2YPLsn4Mh8qg3XBT8zK6dewbSQ4BuHPk4wOwbzP2VgVp4mNDyeNQFIL2xxjE2plppi8idcXBF3Y%2BUybBMYcVixUOYp6dimxopO6uT7j2i1CFEUYh%2BhyNU3WsetYotNFZR0p45Biz5Eud%2BlEk%2F18x7brBadoOCd0G98EektCPjwZIcj2sWHwN6pfpI2RUoxN4mzM9poA4FiLzdj4GZbxJMzln5AtFhqADdlIhBHq%2BE1t5f3mDKK1r4v2K6JBQRoF2RnczVghv75FYvLWmA6hJITzUp7RiAQoKugbyckiiOVI4WnTZfJExTOHiAOaXePdvzbWoBQNmM7zvQrLxj63xTGAGqkUmltzkGWA4rfBYYugUeDBpMwXtGBw3BRBf7CxJXJpY0B0tZi%2BgiafcVI%2FaQDCGQipO8iYFWEWBGWpNk9flhXFoHTW3fIIDGuLL4xQ2LNK3UXOYKG8DMP30ussGOqUBEZyyP80xhTIl478pPzVLHg54H%2F2JHUjUVblBxEJ716eHCrvYbyIlb6T5ysE%2BAC1%2FS7DL9%2F%2FzPn1sTcNDLLUdgniCmV4YHsFj6oTvjZNWL6fMKX3DJUWWeyZhUZQzrJ8VdUs6VAOn2TN%2BkfyT3lK0ReTonbYXFHoShKEohTIzKCKvr6OA0Yqw5mQfztDqWLKtq6ZTsEKtGLJZruD4BiLFf4Xn0FfZ&X-Amz-Signature=6abac247f7f89b99519037ab7637f340fd047be96e9ab77a795f580a5a8054a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666GEG4PD%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fzm09o1Ur5JB%2FpIn1nlzwdbXtWkQxafIskg0hRWP2XAIgITLDV4Nfaa%2F%2BboejPHkjJTMw6iLsa9Mf%2FSTAis9TiYoqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2FYfnmVUzoq6Z7fBSrcA1vaisJJbba1%2F0InaqbX7IOR20jGZZf8JpTAX4pNs5rSzXLxZ0Q1MHTJL%2B97Cj5mk5aKXc5GIwnyb1LcwWL5WkpcJHIJEVb7BH%2FuIjQFlKhDQ%2FQxPholaJThRLBOt%2FpyRd0kBRdmkSo7dRp3CKg31hEzVl5ZymplMts2APMyDTqjrTbY2YPLsn4Mh8qg3XBT8zK6dewbSQ4BuHPk4wOwbzP2VgVp4mNDyeNQFIL2xxjE2plppi8idcXBF3Y%2BUybBMYcVixUOYp6dimxopO6uT7j2i1CFEUYh%2BhyNU3WsetYotNFZR0p45Biz5Eud%2BlEk%2F18x7brBadoOCd0G98EektCPjwZIcj2sWHwN6pfpI2RUoxN4mzM9poA4FiLzdj4GZbxJMzln5AtFhqADdlIhBHq%2BE1t5f3mDKK1r4v2K6JBQRoF2RnczVghv75FYvLWmA6hJITzUp7RiAQoKugbyckiiOVI4WnTZfJExTOHiAOaXePdvzbWoBQNmM7zvQrLxj63xTGAGqkUmltzkGWA4rfBYYugUeDBpMwXtGBw3BRBf7CxJXJpY0B0tZi%2BgiafcVI%2FaQDCGQipO8iYFWEWBGWpNk9flhXFoHTW3fIIDGuLL4xQ2LNK3UXOYKG8DMP30ussGOqUBEZyyP80xhTIl478pPzVLHg54H%2F2JHUjUVblBxEJ716eHCrvYbyIlb6T5ysE%2BAC1%2FS7DL9%2F%2FzPn1sTcNDLLUdgniCmV4YHsFj6oTvjZNWL6fMKX3DJUWWeyZhUZQzrJ8VdUs6VAOn2TN%2BkfyT3lK0ReTonbYXFHoShKEohTIzKCKvr6OA0Yqw5mQfztDqWLKtq6ZTsEKtGLJZruD4BiLFf4Xn0FfZ&X-Amz-Signature=d0fc52940d8a003356555c6542977a6604db037a9f18be61f452947782d00621&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666GEG4PD%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fzm09o1Ur5JB%2FpIn1nlzwdbXtWkQxafIskg0hRWP2XAIgITLDV4Nfaa%2F%2BboejPHkjJTMw6iLsa9Mf%2FSTAis9TiYoqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2FYfnmVUzoq6Z7fBSrcA1vaisJJbba1%2F0InaqbX7IOR20jGZZf8JpTAX4pNs5rSzXLxZ0Q1MHTJL%2B97Cj5mk5aKXc5GIwnyb1LcwWL5WkpcJHIJEVb7BH%2FuIjQFlKhDQ%2FQxPholaJThRLBOt%2FpyRd0kBRdmkSo7dRp3CKg31hEzVl5ZymplMts2APMyDTqjrTbY2YPLsn4Mh8qg3XBT8zK6dewbSQ4BuHPk4wOwbzP2VgVp4mNDyeNQFIL2xxjE2plppi8idcXBF3Y%2BUybBMYcVixUOYp6dimxopO6uT7j2i1CFEUYh%2BhyNU3WsetYotNFZR0p45Biz5Eud%2BlEk%2F18x7brBadoOCd0G98EektCPjwZIcj2sWHwN6pfpI2RUoxN4mzM9poA4FiLzdj4GZbxJMzln5AtFhqADdlIhBHq%2BE1t5f3mDKK1r4v2K6JBQRoF2RnczVghv75FYvLWmA6hJITzUp7RiAQoKugbyckiiOVI4WnTZfJExTOHiAOaXePdvzbWoBQNmM7zvQrLxj63xTGAGqkUmltzkGWA4rfBYYugUeDBpMwXtGBw3BRBf7CxJXJpY0B0tZi%2BgiafcVI%2FaQDCGQipO8iYFWEWBGWpNk9flhXFoHTW3fIIDGuLL4xQ2LNK3UXOYKG8DMP30ussGOqUBEZyyP80xhTIl478pPzVLHg54H%2F2JHUjUVblBxEJ716eHCrvYbyIlb6T5ysE%2BAC1%2FS7DL9%2F%2FzPn1sTcNDLLUdgniCmV4YHsFj6oTvjZNWL6fMKX3DJUWWeyZhUZQzrJ8VdUs6VAOn2TN%2BkfyT3lK0ReTonbYXFHoShKEohTIzKCKvr6OA0Yqw5mQfztDqWLKtq6ZTsEKtGLJZruD4BiLFf4Xn0FfZ&X-Amz-Signature=7c2d8759a884b6c22532bd4ffe216f787ad7c3e8e2101f2a2fb19d29f44c2176&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666GEG4PD%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2Fzm09o1Ur5JB%2FpIn1nlzwdbXtWkQxafIskg0hRWP2XAIgITLDV4Nfaa%2F%2BboejPHkjJTMw6iLsa9Mf%2FSTAis9TiYoqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2FYfnmVUzoq6Z7fBSrcA1vaisJJbba1%2F0InaqbX7IOR20jGZZf8JpTAX4pNs5rSzXLxZ0Q1MHTJL%2B97Cj5mk5aKXc5GIwnyb1LcwWL5WkpcJHIJEVb7BH%2FuIjQFlKhDQ%2FQxPholaJThRLBOt%2FpyRd0kBRdmkSo7dRp3CKg31hEzVl5ZymplMts2APMyDTqjrTbY2YPLsn4Mh8qg3XBT8zK6dewbSQ4BuHPk4wOwbzP2VgVp4mNDyeNQFIL2xxjE2plppi8idcXBF3Y%2BUybBMYcVixUOYp6dimxopO6uT7j2i1CFEUYh%2BhyNU3WsetYotNFZR0p45Biz5Eud%2BlEk%2F18x7brBadoOCd0G98EektCPjwZIcj2sWHwN6pfpI2RUoxN4mzM9poA4FiLzdj4GZbxJMzln5AtFhqADdlIhBHq%2BE1t5f3mDKK1r4v2K6JBQRoF2RnczVghv75FYvLWmA6hJITzUp7RiAQoKugbyckiiOVI4WnTZfJExTOHiAOaXePdvzbWoBQNmM7zvQrLxj63xTGAGqkUmltzkGWA4rfBYYugUeDBpMwXtGBw3BRBf7CxJXJpY0B0tZi%2BgiafcVI%2FaQDCGQipO8iYFWEWBGWpNk9flhXFoHTW3fIIDGuLL4xQ2LNK3UXOYKG8DMP30ussGOqUBEZyyP80xhTIl478pPzVLHg54H%2F2JHUjUVblBxEJ716eHCrvYbyIlb6T5ysE%2BAC1%2FS7DL9%2F%2FzPn1sTcNDLLUdgniCmV4YHsFj6oTvjZNWL6fMKX3DJUWWeyZhUZQzrJ8VdUs6VAOn2TN%2BkfyT3lK0ReTonbYXFHoShKEohTIzKCKvr6OA0Yqw5mQfztDqWLKtq6ZTsEKtGLJZruD4BiLFf4Xn0FfZ&X-Amz-Signature=98fbca1c61f5a6fe51536605711e24973e092a29dd47931815b41f96f2e10ea1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



