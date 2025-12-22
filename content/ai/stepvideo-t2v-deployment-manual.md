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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UUSBOC5%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDHwuV3LF%2BCzoTi%2BnpwChQRAKwQit62G25LesXZwvGeRQIhAPr6m%2F0leIu6%2FMF3O9bxfTxJazY%2ByA0swy%2FGfYo1cycZKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwBR5eMnYOrX69%2BLcq3ANbDDcFNvQ9O3zga%2Bf4xRBQFdDEmfwS0t%2BNUQ7ecqvxsJ5pYm3VUU%2F%2FkzVjAeQWpw3Syb9kejIaGcLL%2F6uWRNknkOA8cDhxBnIBc12Gg1j004JJGNWmRxz5GJknFWxNh6ngM2DCwxjj5xuPX4FCq90DsqoZO3IIKiCo6kC05I9i6bVHyV9reDMoryrUhGph9OE6Tb9BDIPiY%2FqkcXzB452byZvmifjD6nL6iuGH9TAZzrJIUY6NU36MfgsOetimwHJd22Biy0rglaYpKdKN2VJ01aYQz3G0QihBU5fmvHQJ3JfqgcpKIDJCiMLO1cTD7GB%2BoykB2Oi4hYWDfEa3QAqkKGR%2B6mbdCoYfL6ijGQVuVWx0eeX3BzqXB12V43wv%2F5%2BaFfrGM9ERmCaaJqZpbg8YxndLWml3UB5z60vr047gxUi6X5NE5fLKFOIFmx9In5fjj7N7QzDeRrbLOmNiaIMdoF%2BCejYazwNDrZ1S4bZ1BeLKAnJBGsy6y0ZXmhO4l9pjEOG0mpCY6xiPDT7gRajxAIxPTQ7gzZeq0cb7dyM%2Bmma1nEIz2fcxXtoKkPmfZspteRnPiSMR0cZRoDLYR6%2FuWvweFkti29%2Bmj8gP4p%2Fw9WqxiJkSNyxo%2BOxwHDDn5KLKBjqkAY6GiordQHYNSw7Ee1YzDpDDImfQU4V80vQgINr4%2BEDDIKxJbYGzWZPXvG%2FYuQEskonWMZOlHcbn9EfVyq%2FBgnjsBHtkSqSzLSAnESBztn5ZgTcDvyIwBE%2BNTc%2BftQuSv0UQ1HeLRW2uT9NG4wOITVvgYTreSTVNP0MRa%2F838%2BJyLLBQ7AyOAf%2FxnnTbDFeayR5us6CsYCZ0YiT404mWa7p3mlgT&X-Amz-Signature=8f9f6ebbe2eb8a1f68992c5e961256bdc0712873d69d24bb2ce7a9d86cb7f94a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UUSBOC5%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDHwuV3LF%2BCzoTi%2BnpwChQRAKwQit62G25LesXZwvGeRQIhAPr6m%2F0leIu6%2FMF3O9bxfTxJazY%2ByA0swy%2FGfYo1cycZKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwBR5eMnYOrX69%2BLcq3ANbDDcFNvQ9O3zga%2Bf4xRBQFdDEmfwS0t%2BNUQ7ecqvxsJ5pYm3VUU%2F%2FkzVjAeQWpw3Syb9kejIaGcLL%2F6uWRNknkOA8cDhxBnIBc12Gg1j004JJGNWmRxz5GJknFWxNh6ngM2DCwxjj5xuPX4FCq90DsqoZO3IIKiCo6kC05I9i6bVHyV9reDMoryrUhGph9OE6Tb9BDIPiY%2FqkcXzB452byZvmifjD6nL6iuGH9TAZzrJIUY6NU36MfgsOetimwHJd22Biy0rglaYpKdKN2VJ01aYQz3G0QihBU5fmvHQJ3JfqgcpKIDJCiMLO1cTD7GB%2BoykB2Oi4hYWDfEa3QAqkKGR%2B6mbdCoYfL6ijGQVuVWx0eeX3BzqXB12V43wv%2F5%2BaFfrGM9ERmCaaJqZpbg8YxndLWml3UB5z60vr047gxUi6X5NE5fLKFOIFmx9In5fjj7N7QzDeRrbLOmNiaIMdoF%2BCejYazwNDrZ1S4bZ1BeLKAnJBGsy6y0ZXmhO4l9pjEOG0mpCY6xiPDT7gRajxAIxPTQ7gzZeq0cb7dyM%2Bmma1nEIz2fcxXtoKkPmfZspteRnPiSMR0cZRoDLYR6%2FuWvweFkti29%2Bmj8gP4p%2Fw9WqxiJkSNyxo%2BOxwHDDn5KLKBjqkAY6GiordQHYNSw7Ee1YzDpDDImfQU4V80vQgINr4%2BEDDIKxJbYGzWZPXvG%2FYuQEskonWMZOlHcbn9EfVyq%2FBgnjsBHtkSqSzLSAnESBztn5ZgTcDvyIwBE%2BNTc%2BftQuSv0UQ1HeLRW2uT9NG4wOITVvgYTreSTVNP0MRa%2F838%2BJyLLBQ7AyOAf%2FxnnTbDFeayR5us6CsYCZ0YiT404mWa7p3mlgT&X-Amz-Signature=7e425d4dfa1bb8e21e5b1e01fb7a8bdcc681dbb92184e9fe9b4d49167cea92f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UUSBOC5%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDHwuV3LF%2BCzoTi%2BnpwChQRAKwQit62G25LesXZwvGeRQIhAPr6m%2F0leIu6%2FMF3O9bxfTxJazY%2ByA0swy%2FGfYo1cycZKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwBR5eMnYOrX69%2BLcq3ANbDDcFNvQ9O3zga%2Bf4xRBQFdDEmfwS0t%2BNUQ7ecqvxsJ5pYm3VUU%2F%2FkzVjAeQWpw3Syb9kejIaGcLL%2F6uWRNknkOA8cDhxBnIBc12Gg1j004JJGNWmRxz5GJknFWxNh6ngM2DCwxjj5xuPX4FCq90DsqoZO3IIKiCo6kC05I9i6bVHyV9reDMoryrUhGph9OE6Tb9BDIPiY%2FqkcXzB452byZvmifjD6nL6iuGH9TAZzrJIUY6NU36MfgsOetimwHJd22Biy0rglaYpKdKN2VJ01aYQz3G0QihBU5fmvHQJ3JfqgcpKIDJCiMLO1cTD7GB%2BoykB2Oi4hYWDfEa3QAqkKGR%2B6mbdCoYfL6ijGQVuVWx0eeX3BzqXB12V43wv%2F5%2BaFfrGM9ERmCaaJqZpbg8YxndLWml3UB5z60vr047gxUi6X5NE5fLKFOIFmx9In5fjj7N7QzDeRrbLOmNiaIMdoF%2BCejYazwNDrZ1S4bZ1BeLKAnJBGsy6y0ZXmhO4l9pjEOG0mpCY6xiPDT7gRajxAIxPTQ7gzZeq0cb7dyM%2Bmma1nEIz2fcxXtoKkPmfZspteRnPiSMR0cZRoDLYR6%2FuWvweFkti29%2Bmj8gP4p%2Fw9WqxiJkSNyxo%2BOxwHDDn5KLKBjqkAY6GiordQHYNSw7Ee1YzDpDDImfQU4V80vQgINr4%2BEDDIKxJbYGzWZPXvG%2FYuQEskonWMZOlHcbn9EfVyq%2FBgnjsBHtkSqSzLSAnESBztn5ZgTcDvyIwBE%2BNTc%2BftQuSv0UQ1HeLRW2uT9NG4wOITVvgYTreSTVNP0MRa%2F838%2BJyLLBQ7AyOAf%2FxnnTbDFeayR5us6CsYCZ0YiT404mWa7p3mlgT&X-Amz-Signature=9c94b64a8308811a6bb035c6666d8e5434a7737564945c9cbc2a9fa243bda3a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UUSBOC5%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDHwuV3LF%2BCzoTi%2BnpwChQRAKwQit62G25LesXZwvGeRQIhAPr6m%2F0leIu6%2FMF3O9bxfTxJazY%2ByA0swy%2FGfYo1cycZKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwBR5eMnYOrX69%2BLcq3ANbDDcFNvQ9O3zga%2Bf4xRBQFdDEmfwS0t%2BNUQ7ecqvxsJ5pYm3VUU%2F%2FkzVjAeQWpw3Syb9kejIaGcLL%2F6uWRNknkOA8cDhxBnIBc12Gg1j004JJGNWmRxz5GJknFWxNh6ngM2DCwxjj5xuPX4FCq90DsqoZO3IIKiCo6kC05I9i6bVHyV9reDMoryrUhGph9OE6Tb9BDIPiY%2FqkcXzB452byZvmifjD6nL6iuGH9TAZzrJIUY6NU36MfgsOetimwHJd22Biy0rglaYpKdKN2VJ01aYQz3G0QihBU5fmvHQJ3JfqgcpKIDJCiMLO1cTD7GB%2BoykB2Oi4hYWDfEa3QAqkKGR%2B6mbdCoYfL6ijGQVuVWx0eeX3BzqXB12V43wv%2F5%2BaFfrGM9ERmCaaJqZpbg8YxndLWml3UB5z60vr047gxUi6X5NE5fLKFOIFmx9In5fjj7N7QzDeRrbLOmNiaIMdoF%2BCejYazwNDrZ1S4bZ1BeLKAnJBGsy6y0ZXmhO4l9pjEOG0mpCY6xiPDT7gRajxAIxPTQ7gzZeq0cb7dyM%2Bmma1nEIz2fcxXtoKkPmfZspteRnPiSMR0cZRoDLYR6%2FuWvweFkti29%2Bmj8gP4p%2Fw9WqxiJkSNyxo%2BOxwHDDn5KLKBjqkAY6GiordQHYNSw7Ee1YzDpDDImfQU4V80vQgINr4%2BEDDIKxJbYGzWZPXvG%2FYuQEskonWMZOlHcbn9EfVyq%2FBgnjsBHtkSqSzLSAnESBztn5ZgTcDvyIwBE%2BNTc%2BftQuSv0UQ1HeLRW2uT9NG4wOITVvgYTreSTVNP0MRa%2F838%2BJyLLBQ7AyOAf%2FxnnTbDFeayR5us6CsYCZ0YiT404mWa7p3mlgT&X-Amz-Signature=bc01674ebac077898733855555039fa967a6306debc4209048215525b7383734&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



