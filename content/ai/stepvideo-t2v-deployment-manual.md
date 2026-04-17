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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLZKVRHK%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHRIYAB9O8rpYulTDTjTX1eUKIB8rPpNy%2FiLwSgjF8H%2FAiEA0uor17Gu9ZNaD0WS3IxRoFCy6FTYDvtWLri9%2BewSxBQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt8ROCilsH5pAyaaCrcA8ITGWxYREpF4mITeJaYR%2Bl9iylRwiM2gXXzGFdV%2FdrntyPBZMl7KDdzdzhIMwWm62d4SRkMhtZJSNieYnG2m8sGtCayFMxhMNO7G8%2BYkKUAfOZsGz%2F4tT5LZvxHU%2BnRvpDRl0wYQBEiwEmNBJt19YekH1YapmXSOUN%2BKhlrRiAHuTcUTw%2BOqB2IMugl7IUDPc2LABakM9Okt%2FdvedN6VHnrrUgaYO7P1CzgYrmQaqDV3VGtX37jqirUOumu%2BD6PV7SujVjMOiK%2Bn6KXGM5aJTFo9btOwrf9ikH4Pu77GyGjId2R3xKFAntprc%2FlCDmImwPFwNJs3w3QKUSL043szPYEFjzcoQkyD%2BcS%2F7yKzk0S%2F6De%2FXP4d2oRrIjTuzQmIceRODxFjeRZME1hGN%2B349NvF42F3IdRk7%2BSaGlNAeMTPSZ01PeTiJjXRa5wf%2FYR4CLTlgXkflK6ae7YOnx%2BG1LQ6qxY6njZXtclVI5AhlCBV4hy0CRclzmP4rVS1s5eCWvc%2FAI0VvgP3YlQCUVzRQeXnuCwQ3U13rRMYFf0bVE7mom9FVNkycvEKwWjHgMnTygbONHh0JzBJIWkHnrjQVk66%2FUG5NlDDSYgFcBZ2z%2FNepMtJg%2Bt%2B4ZF4MdvMOO7hs8GOqUBO8FoxaLdopGHE50PDxv8b%2BtG6Pu7iG5LR215UrogNa7ljM%2BTobHwpa%2Fvj1inS97%2B79h0zo7IM1pniO9avZw1%2FLEBUAtDLy0YYNaWBzGuvDMcDD0KjUtsIUdU93Nf6KT0lgmX8%2BE%2Fg52mw08kKw%2B%2BKA35tGDvOVSKtYVs25HYs4UOcvn3mh2wUX%2BpcVsne7ISUfHL%2FQW4z7puLlnV7fA10jkNp6Tr&X-Amz-Signature=b1f66caa361d5001f1bda71463a1e5982d65b3c210dc93f5a89abeed0b1b06d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLZKVRHK%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHRIYAB9O8rpYulTDTjTX1eUKIB8rPpNy%2FiLwSgjF8H%2FAiEA0uor17Gu9ZNaD0WS3IxRoFCy6FTYDvtWLri9%2BewSxBQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt8ROCilsH5pAyaaCrcA8ITGWxYREpF4mITeJaYR%2Bl9iylRwiM2gXXzGFdV%2FdrntyPBZMl7KDdzdzhIMwWm62d4SRkMhtZJSNieYnG2m8sGtCayFMxhMNO7G8%2BYkKUAfOZsGz%2F4tT5LZvxHU%2BnRvpDRl0wYQBEiwEmNBJt19YekH1YapmXSOUN%2BKhlrRiAHuTcUTw%2BOqB2IMugl7IUDPc2LABakM9Okt%2FdvedN6VHnrrUgaYO7P1CzgYrmQaqDV3VGtX37jqirUOumu%2BD6PV7SujVjMOiK%2Bn6KXGM5aJTFo9btOwrf9ikH4Pu77GyGjId2R3xKFAntprc%2FlCDmImwPFwNJs3w3QKUSL043szPYEFjzcoQkyD%2BcS%2F7yKzk0S%2F6De%2FXP4d2oRrIjTuzQmIceRODxFjeRZME1hGN%2B349NvF42F3IdRk7%2BSaGlNAeMTPSZ01PeTiJjXRa5wf%2FYR4CLTlgXkflK6ae7YOnx%2BG1LQ6qxY6njZXtclVI5AhlCBV4hy0CRclzmP4rVS1s5eCWvc%2FAI0VvgP3YlQCUVzRQeXnuCwQ3U13rRMYFf0bVE7mom9FVNkycvEKwWjHgMnTygbONHh0JzBJIWkHnrjQVk66%2FUG5NlDDSYgFcBZ2z%2FNepMtJg%2Bt%2B4ZF4MdvMOO7hs8GOqUBO8FoxaLdopGHE50PDxv8b%2BtG6Pu7iG5LR215UrogNa7ljM%2BTobHwpa%2Fvj1inS97%2B79h0zo7IM1pniO9avZw1%2FLEBUAtDLy0YYNaWBzGuvDMcDD0KjUtsIUdU93Nf6KT0lgmX8%2BE%2Fg52mw08kKw%2B%2BKA35tGDvOVSKtYVs25HYs4UOcvn3mh2wUX%2BpcVsne7ISUfHL%2FQW4z7puLlnV7fA10jkNp6Tr&X-Amz-Signature=50061995f1f86129bbd9ade26fdc3dc726f7863a0cb3beab00e21f30b6e0acc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLZKVRHK%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHRIYAB9O8rpYulTDTjTX1eUKIB8rPpNy%2FiLwSgjF8H%2FAiEA0uor17Gu9ZNaD0WS3IxRoFCy6FTYDvtWLri9%2BewSxBQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt8ROCilsH5pAyaaCrcA8ITGWxYREpF4mITeJaYR%2Bl9iylRwiM2gXXzGFdV%2FdrntyPBZMl7KDdzdzhIMwWm62d4SRkMhtZJSNieYnG2m8sGtCayFMxhMNO7G8%2BYkKUAfOZsGz%2F4tT5LZvxHU%2BnRvpDRl0wYQBEiwEmNBJt19YekH1YapmXSOUN%2BKhlrRiAHuTcUTw%2BOqB2IMugl7IUDPc2LABakM9Okt%2FdvedN6VHnrrUgaYO7P1CzgYrmQaqDV3VGtX37jqirUOumu%2BD6PV7SujVjMOiK%2Bn6KXGM5aJTFo9btOwrf9ikH4Pu77GyGjId2R3xKFAntprc%2FlCDmImwPFwNJs3w3QKUSL043szPYEFjzcoQkyD%2BcS%2F7yKzk0S%2F6De%2FXP4d2oRrIjTuzQmIceRODxFjeRZME1hGN%2B349NvF42F3IdRk7%2BSaGlNAeMTPSZ01PeTiJjXRa5wf%2FYR4CLTlgXkflK6ae7YOnx%2BG1LQ6qxY6njZXtclVI5AhlCBV4hy0CRclzmP4rVS1s5eCWvc%2FAI0VvgP3YlQCUVzRQeXnuCwQ3U13rRMYFf0bVE7mom9FVNkycvEKwWjHgMnTygbONHh0JzBJIWkHnrjQVk66%2FUG5NlDDSYgFcBZ2z%2FNepMtJg%2Bt%2B4ZF4MdvMOO7hs8GOqUBO8FoxaLdopGHE50PDxv8b%2BtG6Pu7iG5LR215UrogNa7ljM%2BTobHwpa%2Fvj1inS97%2B79h0zo7IM1pniO9avZw1%2FLEBUAtDLy0YYNaWBzGuvDMcDD0KjUtsIUdU93Nf6KT0lgmX8%2BE%2Fg52mw08kKw%2B%2BKA35tGDvOVSKtYVs25HYs4UOcvn3mh2wUX%2BpcVsne7ISUfHL%2FQW4z7puLlnV7fA10jkNp6Tr&X-Amz-Signature=59cf352e47b1c54f441e3633b598976b61213b958dce0c65ff87a4266ceb5aad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLZKVRHK%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHRIYAB9O8rpYulTDTjTX1eUKIB8rPpNy%2FiLwSgjF8H%2FAiEA0uor17Gu9ZNaD0WS3IxRoFCy6FTYDvtWLri9%2BewSxBQqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKt8ROCilsH5pAyaaCrcA8ITGWxYREpF4mITeJaYR%2Bl9iylRwiM2gXXzGFdV%2FdrntyPBZMl7KDdzdzhIMwWm62d4SRkMhtZJSNieYnG2m8sGtCayFMxhMNO7G8%2BYkKUAfOZsGz%2F4tT5LZvxHU%2BnRvpDRl0wYQBEiwEmNBJt19YekH1YapmXSOUN%2BKhlrRiAHuTcUTw%2BOqB2IMugl7IUDPc2LABakM9Okt%2FdvedN6VHnrrUgaYO7P1CzgYrmQaqDV3VGtX37jqirUOumu%2BD6PV7SujVjMOiK%2Bn6KXGM5aJTFo9btOwrf9ikH4Pu77GyGjId2R3xKFAntprc%2FlCDmImwPFwNJs3w3QKUSL043szPYEFjzcoQkyD%2BcS%2F7yKzk0S%2F6De%2FXP4d2oRrIjTuzQmIceRODxFjeRZME1hGN%2B349NvF42F3IdRk7%2BSaGlNAeMTPSZ01PeTiJjXRa5wf%2FYR4CLTlgXkflK6ae7YOnx%2BG1LQ6qxY6njZXtclVI5AhlCBV4hy0CRclzmP4rVS1s5eCWvc%2FAI0VvgP3YlQCUVzRQeXnuCwQ3U13rRMYFf0bVE7mom9FVNkycvEKwWjHgMnTygbONHh0JzBJIWkHnrjQVk66%2FUG5NlDDSYgFcBZ2z%2FNepMtJg%2Bt%2B4ZF4MdvMOO7hs8GOqUBO8FoxaLdopGHE50PDxv8b%2BtG6Pu7iG5LR215UrogNa7ljM%2BTobHwpa%2Fvj1inS97%2B79h0zo7IM1pniO9avZw1%2FLEBUAtDLy0YYNaWBzGuvDMcDD0KjUtsIUdU93Nf6KT0lgmX8%2BE%2Fg52mw08kKw%2B%2BKA35tGDvOVSKtYVs25HYs4UOcvn3mh2wUX%2BpcVsne7ISUfHL%2FQW4z7puLlnV7fA10jkNp6Tr&X-Amz-Signature=a921e2da2fab22b273163a4ec760227db29cbb516f59c96e52a6fb6532aa5365&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



