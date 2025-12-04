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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAR7MWPR%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQDhSqFKXr2zc8jyBB9l1x11uCGtv%2BkhKGqq1YZ6ByAGFAIhAPyAwrp1oVU%2F%2FxadYRXwjRGr56LNtfJx8f6uPTaLVpBAKv8DCDsQABoMNjM3NDIzMTgzODA1Igyy0gZVLB3meY6s2Jwq3ANmVsNuJbqbNtGY%2FpduNouob1VFcGtnqSTvkzcR77BE3UGgnYFMwtbAlT9lDeMW1LiJUWWMnlmQZ%2FwuFhkpydXAJ0hNXTeELstU5iApJxTPUTZFdMTJ6R8Ez%2BBWUkVVolS6EBLVJ5%2BPhHidHygVnBJur%2BOozktKG5npDJObQfAPcorY7FW9RIZPU9plg3rRZQXTiHmak0XqxX7F2Lt%2BIa9hr2C%2BLm9Ee8vkK%2Bk6nBBbIJ%2Brm4CABxVpYtf2FB5efUxvrkHkVcEjIUNX24gObv6nK%2FEbyZ8i9p5uCgekGiLviNdXZB%2B16ugTvUI%2BAHhQJjC3x1wHXImI2e%2Fu%2FcPEPBCVRE0hot1z%2B8MSSICd452bYSfUSfshWQgvb19zr%2BJi4dEcqdyjws6XHwK8bmAfNxH5uK3%2FvqJ3ATUoOi%2FQ59C9MEGjR8L%2Bkg0RjCNqX9bwWuB75W9%2BL6DaG6oGvjz1%2FE0%2BQV9zRW9%2FqSXTYNJ7Mph%2BoLI2hpO0jsQCx4BB%2F2mksY00PJHOBWjy4VuGD0a6wI5lnpGrU%2Ffr2z3r3Z8erz%2BO9%2B%2Bfl419A6l1lCWkmMEnlZKg14iKyuJTMIrAjMF%2B5nyrW7QuphjkbHCxzNdaP8fy%2Fod15McUR7qDF%2FX8XDC51MPJBjqkATtP%2BcaCfHd1BOBiNsEZrQs4TnPTy08ByMEkU6aI4fKqdxazRGpvHShu4duz8w6ot2qE3E%2BuqsVtha2wOIs0A4spbhz2OAm3QeJous7YzUeQ5CX%2BPyFFfgdm05XeudFYiRyvEO4KYaQu3NFyISTrhoAKHflv8wDjAj3m5EE%2FOmgowrBeW1cUhiVIAYFqXY294O3A1vYJnCZ6Ssqdw3lyXVsne11Z&X-Amz-Signature=7237087329d1ba545be5b2af021c6f3ddadde2fe2d1b28a0daf0e8647ab06517&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAR7MWPR%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQDhSqFKXr2zc8jyBB9l1x11uCGtv%2BkhKGqq1YZ6ByAGFAIhAPyAwrp1oVU%2F%2FxadYRXwjRGr56LNtfJx8f6uPTaLVpBAKv8DCDsQABoMNjM3NDIzMTgzODA1Igyy0gZVLB3meY6s2Jwq3ANmVsNuJbqbNtGY%2FpduNouob1VFcGtnqSTvkzcR77BE3UGgnYFMwtbAlT9lDeMW1LiJUWWMnlmQZ%2FwuFhkpydXAJ0hNXTeELstU5iApJxTPUTZFdMTJ6R8Ez%2BBWUkVVolS6EBLVJ5%2BPhHidHygVnBJur%2BOozktKG5npDJObQfAPcorY7FW9RIZPU9plg3rRZQXTiHmak0XqxX7F2Lt%2BIa9hr2C%2BLm9Ee8vkK%2Bk6nBBbIJ%2Brm4CABxVpYtf2FB5efUxvrkHkVcEjIUNX24gObv6nK%2FEbyZ8i9p5uCgekGiLviNdXZB%2B16ugTvUI%2BAHhQJjC3x1wHXImI2e%2Fu%2FcPEPBCVRE0hot1z%2B8MSSICd452bYSfUSfshWQgvb19zr%2BJi4dEcqdyjws6XHwK8bmAfNxH5uK3%2FvqJ3ATUoOi%2FQ59C9MEGjR8L%2Bkg0RjCNqX9bwWuB75W9%2BL6DaG6oGvjz1%2FE0%2BQV9zRW9%2FqSXTYNJ7Mph%2BoLI2hpO0jsQCx4BB%2F2mksY00PJHOBWjy4VuGD0a6wI5lnpGrU%2Ffr2z3r3Z8erz%2BO9%2B%2Bfl419A6l1lCWkmMEnlZKg14iKyuJTMIrAjMF%2B5nyrW7QuphjkbHCxzNdaP8fy%2Fod15McUR7qDF%2FX8XDC51MPJBjqkATtP%2BcaCfHd1BOBiNsEZrQs4TnPTy08ByMEkU6aI4fKqdxazRGpvHShu4duz8w6ot2qE3E%2BuqsVtha2wOIs0A4spbhz2OAm3QeJous7YzUeQ5CX%2BPyFFfgdm05XeudFYiRyvEO4KYaQu3NFyISTrhoAKHflv8wDjAj3m5EE%2FOmgowrBeW1cUhiVIAYFqXY294O3A1vYJnCZ6Ssqdw3lyXVsne11Z&X-Amz-Signature=171da6462061f6a9b9a5c93e0bda232bd5becebc7fc9e3cdd9760530380adf80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAR7MWPR%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQDhSqFKXr2zc8jyBB9l1x11uCGtv%2BkhKGqq1YZ6ByAGFAIhAPyAwrp1oVU%2F%2FxadYRXwjRGr56LNtfJx8f6uPTaLVpBAKv8DCDsQABoMNjM3NDIzMTgzODA1Igyy0gZVLB3meY6s2Jwq3ANmVsNuJbqbNtGY%2FpduNouob1VFcGtnqSTvkzcR77BE3UGgnYFMwtbAlT9lDeMW1LiJUWWMnlmQZ%2FwuFhkpydXAJ0hNXTeELstU5iApJxTPUTZFdMTJ6R8Ez%2BBWUkVVolS6EBLVJ5%2BPhHidHygVnBJur%2BOozktKG5npDJObQfAPcorY7FW9RIZPU9plg3rRZQXTiHmak0XqxX7F2Lt%2BIa9hr2C%2BLm9Ee8vkK%2Bk6nBBbIJ%2Brm4CABxVpYtf2FB5efUxvrkHkVcEjIUNX24gObv6nK%2FEbyZ8i9p5uCgekGiLviNdXZB%2B16ugTvUI%2BAHhQJjC3x1wHXImI2e%2Fu%2FcPEPBCVRE0hot1z%2B8MSSICd452bYSfUSfshWQgvb19zr%2BJi4dEcqdyjws6XHwK8bmAfNxH5uK3%2FvqJ3ATUoOi%2FQ59C9MEGjR8L%2Bkg0RjCNqX9bwWuB75W9%2BL6DaG6oGvjz1%2FE0%2BQV9zRW9%2FqSXTYNJ7Mph%2BoLI2hpO0jsQCx4BB%2F2mksY00PJHOBWjy4VuGD0a6wI5lnpGrU%2Ffr2z3r3Z8erz%2BO9%2B%2Bfl419A6l1lCWkmMEnlZKg14iKyuJTMIrAjMF%2B5nyrW7QuphjkbHCxzNdaP8fy%2Fod15McUR7qDF%2FX8XDC51MPJBjqkATtP%2BcaCfHd1BOBiNsEZrQs4TnPTy08ByMEkU6aI4fKqdxazRGpvHShu4duz8w6ot2qE3E%2BuqsVtha2wOIs0A4spbhz2OAm3QeJous7YzUeQ5CX%2BPyFFfgdm05XeudFYiRyvEO4KYaQu3NFyISTrhoAKHflv8wDjAj3m5EE%2FOmgowrBeW1cUhiVIAYFqXY294O3A1vYJnCZ6Ssqdw3lyXVsne11Z&X-Amz-Signature=b5f664d88837cfa66310fb0b2117bfe75fa926c49149760710ca67a0b953afce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAR7MWPR%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQDhSqFKXr2zc8jyBB9l1x11uCGtv%2BkhKGqq1YZ6ByAGFAIhAPyAwrp1oVU%2F%2FxadYRXwjRGr56LNtfJx8f6uPTaLVpBAKv8DCDsQABoMNjM3NDIzMTgzODA1Igyy0gZVLB3meY6s2Jwq3ANmVsNuJbqbNtGY%2FpduNouob1VFcGtnqSTvkzcR77BE3UGgnYFMwtbAlT9lDeMW1LiJUWWMnlmQZ%2FwuFhkpydXAJ0hNXTeELstU5iApJxTPUTZFdMTJ6R8Ez%2BBWUkVVolS6EBLVJ5%2BPhHidHygVnBJur%2BOozktKG5npDJObQfAPcorY7FW9RIZPU9plg3rRZQXTiHmak0XqxX7F2Lt%2BIa9hr2C%2BLm9Ee8vkK%2Bk6nBBbIJ%2Brm4CABxVpYtf2FB5efUxvrkHkVcEjIUNX24gObv6nK%2FEbyZ8i9p5uCgekGiLviNdXZB%2B16ugTvUI%2BAHhQJjC3x1wHXImI2e%2Fu%2FcPEPBCVRE0hot1z%2B8MSSICd452bYSfUSfshWQgvb19zr%2BJi4dEcqdyjws6XHwK8bmAfNxH5uK3%2FvqJ3ATUoOi%2FQ59C9MEGjR8L%2Bkg0RjCNqX9bwWuB75W9%2BL6DaG6oGvjz1%2FE0%2BQV9zRW9%2FqSXTYNJ7Mph%2BoLI2hpO0jsQCx4BB%2F2mksY00PJHOBWjy4VuGD0a6wI5lnpGrU%2Ffr2z3r3Z8erz%2BO9%2B%2Bfl419A6l1lCWkmMEnlZKg14iKyuJTMIrAjMF%2B5nyrW7QuphjkbHCxzNdaP8fy%2Fod15McUR7qDF%2FX8XDC51MPJBjqkATtP%2BcaCfHd1BOBiNsEZrQs4TnPTy08ByMEkU6aI4fKqdxazRGpvHShu4duz8w6ot2qE3E%2BuqsVtha2wOIs0A4spbhz2OAm3QeJous7YzUeQ5CX%2BPyFFfgdm05XeudFYiRyvEO4KYaQu3NFyISTrhoAKHflv8wDjAj3m5EE%2FOmgowrBeW1cUhiVIAYFqXY294O3A1vYJnCZ6Ssqdw3lyXVsne11Z&X-Amz-Signature=dcacbf5e5b37a7853302a674dbbdde586a0f5333ad45e85d0725e941942d399d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



