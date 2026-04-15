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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYS5YDO6%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDArWXadc%2BNe0S%2FNWHc7Ez6uy1spH3cb1j01cVbUnGXLgIhAMdoXw1PrqcvbwMNkUj7sgKbS21TezYjzRBMY29WQHGeKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS%2Fzw52vRSrTSVKzoq3ANoQFqMJWbXUXL4saHPSId42tKD%2FVzXY9a9bPqbRXaPpT%2B7jrES%2B%2BxhCz3RdaghaUckuYZp49drdGaVtGTVOug588kNIqfOMJ7Q0sP8dELfdCmTUhSI1qOTAVxhBl5vHja0QzX8E2CTEecJocvYnN1Jndo7%2F0zJcty3xlz5n53a1ShDwN3qrm1IkHxvCOl13jc9%2FAeBR6K6GMS0EqB9fL1d%2BxAa6VogjLKl9B4udF2LGLszOToZGqMMqZYZOnZ1d0FVn1bsKvx3lbn0Rr6UZol5%2FcorgcbbZsFFY0XZ1fenyut2P2jSM4YtsUtxzfx8hT6EvI7HxdjGMXk2vIyZPdWbiqwlzQC3VnqBeez0eDS%2BaHbOfWQdoAn39RvGTIVqKzoqZvxlYa1vsjlE0EFyPJfDkw7U6J2%2FpaGM%2Feu5HL2iFkw1ceB7IqGGOFUnQ1AXm5Kdbemd%2FszbK55f0ZCmSS1LLu0KKCf%2Bv%2B8lgNpfObr74QFJo37hKJDGUoXYHbVqFrCpDiXnzxu3TFYy0hOeGAHC3vXFl5bqmNS4VQ35zt2ynrYiNtgnU2JcSgqrkV%2Btz0s%2F1R%2F9jGY%2BNdVn8%2FMkHO7k1ryw3JpbabQA7x9CAY54S2sXo5y8olRSz8GGcTC%2BlfzOBjqkAevTDr0UrqKwV9ZZmP5HhHFpUxd59BAqUL2YvNeMHiJXghQDQlWY8UlfACh4HB2%2FxKOsnM93O%2BxcnBlCROFGo59r5bATSxVOuBQjQWmw17ylvNj%2FSbSNfH2uSc7P8scPzipui8A71EyyIUPbBUexqQLpHxdxBVQqsOi1lWg0S2ukBPImwKRd%2F%2BUhvkmAK%2FKAMDGWRnWJ86%2ByonfQDtpjJXQU3J38&X-Amz-Signature=0a2e4c7c918d949c2f577832a868ae939c0414118d621fe32a41084c618a1c65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYS5YDO6%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDArWXadc%2BNe0S%2FNWHc7Ez6uy1spH3cb1j01cVbUnGXLgIhAMdoXw1PrqcvbwMNkUj7sgKbS21TezYjzRBMY29WQHGeKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS%2Fzw52vRSrTSVKzoq3ANoQFqMJWbXUXL4saHPSId42tKD%2FVzXY9a9bPqbRXaPpT%2B7jrES%2B%2BxhCz3RdaghaUckuYZp49drdGaVtGTVOug588kNIqfOMJ7Q0sP8dELfdCmTUhSI1qOTAVxhBl5vHja0QzX8E2CTEecJocvYnN1Jndo7%2F0zJcty3xlz5n53a1ShDwN3qrm1IkHxvCOl13jc9%2FAeBR6K6GMS0EqB9fL1d%2BxAa6VogjLKl9B4udF2LGLszOToZGqMMqZYZOnZ1d0FVn1bsKvx3lbn0Rr6UZol5%2FcorgcbbZsFFY0XZ1fenyut2P2jSM4YtsUtxzfx8hT6EvI7HxdjGMXk2vIyZPdWbiqwlzQC3VnqBeez0eDS%2BaHbOfWQdoAn39RvGTIVqKzoqZvxlYa1vsjlE0EFyPJfDkw7U6J2%2FpaGM%2Feu5HL2iFkw1ceB7IqGGOFUnQ1AXm5Kdbemd%2FszbK55f0ZCmSS1LLu0KKCf%2Bv%2B8lgNpfObr74QFJo37hKJDGUoXYHbVqFrCpDiXnzxu3TFYy0hOeGAHC3vXFl5bqmNS4VQ35zt2ynrYiNtgnU2JcSgqrkV%2Btz0s%2F1R%2F9jGY%2BNdVn8%2FMkHO7k1ryw3JpbabQA7x9CAY54S2sXo5y8olRSz8GGcTC%2BlfzOBjqkAevTDr0UrqKwV9ZZmP5HhHFpUxd59BAqUL2YvNeMHiJXghQDQlWY8UlfACh4HB2%2FxKOsnM93O%2BxcnBlCROFGo59r5bATSxVOuBQjQWmw17ylvNj%2FSbSNfH2uSc7P8scPzipui8A71EyyIUPbBUexqQLpHxdxBVQqsOi1lWg0S2ukBPImwKRd%2F%2BUhvkmAK%2FKAMDGWRnWJ86%2ByonfQDtpjJXQU3J38&X-Amz-Signature=f7bae5db5b6e32a44ad026178cc6f4f7ae901b355af727b87c312289ee3168b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYS5YDO6%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDArWXadc%2BNe0S%2FNWHc7Ez6uy1spH3cb1j01cVbUnGXLgIhAMdoXw1PrqcvbwMNkUj7sgKbS21TezYjzRBMY29WQHGeKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS%2Fzw52vRSrTSVKzoq3ANoQFqMJWbXUXL4saHPSId42tKD%2FVzXY9a9bPqbRXaPpT%2B7jrES%2B%2BxhCz3RdaghaUckuYZp49drdGaVtGTVOug588kNIqfOMJ7Q0sP8dELfdCmTUhSI1qOTAVxhBl5vHja0QzX8E2CTEecJocvYnN1Jndo7%2F0zJcty3xlz5n53a1ShDwN3qrm1IkHxvCOl13jc9%2FAeBR6K6GMS0EqB9fL1d%2BxAa6VogjLKl9B4udF2LGLszOToZGqMMqZYZOnZ1d0FVn1bsKvx3lbn0Rr6UZol5%2FcorgcbbZsFFY0XZ1fenyut2P2jSM4YtsUtxzfx8hT6EvI7HxdjGMXk2vIyZPdWbiqwlzQC3VnqBeez0eDS%2BaHbOfWQdoAn39RvGTIVqKzoqZvxlYa1vsjlE0EFyPJfDkw7U6J2%2FpaGM%2Feu5HL2iFkw1ceB7IqGGOFUnQ1AXm5Kdbemd%2FszbK55f0ZCmSS1LLu0KKCf%2Bv%2B8lgNpfObr74QFJo37hKJDGUoXYHbVqFrCpDiXnzxu3TFYy0hOeGAHC3vXFl5bqmNS4VQ35zt2ynrYiNtgnU2JcSgqrkV%2Btz0s%2F1R%2F9jGY%2BNdVn8%2FMkHO7k1ryw3JpbabQA7x9CAY54S2sXo5y8olRSz8GGcTC%2BlfzOBjqkAevTDr0UrqKwV9ZZmP5HhHFpUxd59BAqUL2YvNeMHiJXghQDQlWY8UlfACh4HB2%2FxKOsnM93O%2BxcnBlCROFGo59r5bATSxVOuBQjQWmw17ylvNj%2FSbSNfH2uSc7P8scPzipui8A71EyyIUPbBUexqQLpHxdxBVQqsOi1lWg0S2ukBPImwKRd%2F%2BUhvkmAK%2FKAMDGWRnWJ86%2ByonfQDtpjJXQU3J38&X-Amz-Signature=e810c10b2151cd2741b3bb8d76d379a144f17628658edb746fe00c37d852722b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYS5YDO6%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDArWXadc%2BNe0S%2FNWHc7Ez6uy1spH3cb1j01cVbUnGXLgIhAMdoXw1PrqcvbwMNkUj7sgKbS21TezYjzRBMY29WQHGeKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwS%2Fzw52vRSrTSVKzoq3ANoQFqMJWbXUXL4saHPSId42tKD%2FVzXY9a9bPqbRXaPpT%2B7jrES%2B%2BxhCz3RdaghaUckuYZp49drdGaVtGTVOug588kNIqfOMJ7Q0sP8dELfdCmTUhSI1qOTAVxhBl5vHja0QzX8E2CTEecJocvYnN1Jndo7%2F0zJcty3xlz5n53a1ShDwN3qrm1IkHxvCOl13jc9%2FAeBR6K6GMS0EqB9fL1d%2BxAa6VogjLKl9B4udF2LGLszOToZGqMMqZYZOnZ1d0FVn1bsKvx3lbn0Rr6UZol5%2FcorgcbbZsFFY0XZ1fenyut2P2jSM4YtsUtxzfx8hT6EvI7HxdjGMXk2vIyZPdWbiqwlzQC3VnqBeez0eDS%2BaHbOfWQdoAn39RvGTIVqKzoqZvxlYa1vsjlE0EFyPJfDkw7U6J2%2FpaGM%2Feu5HL2iFkw1ceB7IqGGOFUnQ1AXm5Kdbemd%2FszbK55f0ZCmSS1LLu0KKCf%2Bv%2B8lgNpfObr74QFJo37hKJDGUoXYHbVqFrCpDiXnzxu3TFYy0hOeGAHC3vXFl5bqmNS4VQ35zt2ynrYiNtgnU2JcSgqrkV%2Btz0s%2F1R%2F9jGY%2BNdVn8%2FMkHO7k1ryw3JpbabQA7x9CAY54S2sXo5y8olRSz8GGcTC%2BlfzOBjqkAevTDr0UrqKwV9ZZmP5HhHFpUxd59BAqUL2YvNeMHiJXghQDQlWY8UlfACh4HB2%2FxKOsnM93O%2BxcnBlCROFGo59r5bATSxVOuBQjQWmw17ylvNj%2FSbSNfH2uSc7P8scPzipui8A71EyyIUPbBUexqQLpHxdxBVQqsOi1lWg0S2ukBPImwKRd%2F%2BUhvkmAK%2FKAMDGWRnWJ86%2ByonfQDtpjJXQU3J38&X-Amz-Signature=a04853a35f31d0177eea68876206a1a394c9efd26fff5fcceec86268be58c4b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



