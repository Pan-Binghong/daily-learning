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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NTH3TJV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIDqN9J6RFUk0fwqhJefuBCYAPKmrCpUxvNqFMHli3eXEAiAE7LWqDJrURaj3BbZboIXF9AlR0miuVjRQvwenliyQyCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMcYkI2aNExV7DXL9fKtwDwOe5eHnG6Xp7goAUP2e%2B2pzN7OVqzU0Q3iTOEjduzMggEhtzySabO%2FtkqlTPT0a2rH39ZvJX%2F3M6naEVXBb0oqOAmHgUKPsaOG7z4KktiofAmimCbTwMHquNlKpBcE%2FhqX9jYCqkwR4MYmaqumwJ%2FGJ1vbaVxcOLcWFTlPrfyzrur64u104gWiCcvshDP%2BD6edt3W9ZSFZYFAgndyfBStDtXGpUWwKrqk1fmrBj%2BzgH2eK66KMVUrcJcDPjO663tBvRXsLZ8o6W%2BkmJMUISRaBE%2Fvl%2Fy5J3HQKWC%2F2ybmfW5n4mitx%2BqycdTx4z%2BEsYWQuMUIGihMBkS7eQGnrXKsHC%2BIZp8Fg4%2FJx9wt2bwG5pTN3TsxceuNIaAw68MVFfCTbCwyM9YkMpmKGI9CtFCQgjESMmWbar5BRsRDRqCNIC0rCjcq2P1CbxpGX3XZcAQRgQttw%2BcQkvLe0cwOMDTiRgLM1iUu%2F5ihwI3ti0Qd9pFrF60R0PcwvfbJERkve12jN7W%2BhKktZ3hHfrXUKxnCCwKwRH2sXbamtHhBc8VjbSFzdF2taOEmfG4wUF6PVvxB5L%2FrVkXcA2dYl87uz5MOliRNEg5a5bMSazb7pYLczQ9QN0CgBR3g2p9Inkwkf64zQY6pgFEtWND5SPW0%2BjioWMsKhBNRewM%2BR5%2FoKCAVMgbimbRcKybRnM%2FTmz1jCt%2FtM8xo6ErQqbD3gzQhz3oWq7Vw%2BPTv56QMipOiBXcyYPdQ6QLVMZLXldD0FJHNjvdOvFPRynuwlxmPr8BPfYYUYqVyRgDhEobK%2BoMcV%2Bu9OeYL%2BU%2BkDwLZvbioOQ%2BuUhA4zDXgg8xByQKw2IuIoSO%2F38QRI1Tj0VNvq7U&X-Amz-Signature=9e0ea5782b21ffbdea451b708ee38c71b96c71ea08458e5bbd4c34d6e1aa75ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NTH3TJV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIDqN9J6RFUk0fwqhJefuBCYAPKmrCpUxvNqFMHli3eXEAiAE7LWqDJrURaj3BbZboIXF9AlR0miuVjRQvwenliyQyCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMcYkI2aNExV7DXL9fKtwDwOe5eHnG6Xp7goAUP2e%2B2pzN7OVqzU0Q3iTOEjduzMggEhtzySabO%2FtkqlTPT0a2rH39ZvJX%2F3M6naEVXBb0oqOAmHgUKPsaOG7z4KktiofAmimCbTwMHquNlKpBcE%2FhqX9jYCqkwR4MYmaqumwJ%2FGJ1vbaVxcOLcWFTlPrfyzrur64u104gWiCcvshDP%2BD6edt3W9ZSFZYFAgndyfBStDtXGpUWwKrqk1fmrBj%2BzgH2eK66KMVUrcJcDPjO663tBvRXsLZ8o6W%2BkmJMUISRaBE%2Fvl%2Fy5J3HQKWC%2F2ybmfW5n4mitx%2BqycdTx4z%2BEsYWQuMUIGihMBkS7eQGnrXKsHC%2BIZp8Fg4%2FJx9wt2bwG5pTN3TsxceuNIaAw68MVFfCTbCwyM9YkMpmKGI9CtFCQgjESMmWbar5BRsRDRqCNIC0rCjcq2P1CbxpGX3XZcAQRgQttw%2BcQkvLe0cwOMDTiRgLM1iUu%2F5ihwI3ti0Qd9pFrF60R0PcwvfbJERkve12jN7W%2BhKktZ3hHfrXUKxnCCwKwRH2sXbamtHhBc8VjbSFzdF2taOEmfG4wUF6PVvxB5L%2FrVkXcA2dYl87uz5MOliRNEg5a5bMSazb7pYLczQ9QN0CgBR3g2p9Inkwkf64zQY6pgFEtWND5SPW0%2BjioWMsKhBNRewM%2BR5%2FoKCAVMgbimbRcKybRnM%2FTmz1jCt%2FtM8xo6ErQqbD3gzQhz3oWq7Vw%2BPTv56QMipOiBXcyYPdQ6QLVMZLXldD0FJHNjvdOvFPRynuwlxmPr8BPfYYUYqVyRgDhEobK%2BoMcV%2Bu9OeYL%2BU%2BkDwLZvbioOQ%2BuUhA4zDXgg8xByQKw2IuIoSO%2F38QRI1Tj0VNvq7U&X-Amz-Signature=80cdc8f3b30d04bd8dc5eda60941d2c5168aedd69253912fffc8aee40bc7adb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NTH3TJV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIDqN9J6RFUk0fwqhJefuBCYAPKmrCpUxvNqFMHli3eXEAiAE7LWqDJrURaj3BbZboIXF9AlR0miuVjRQvwenliyQyCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMcYkI2aNExV7DXL9fKtwDwOe5eHnG6Xp7goAUP2e%2B2pzN7OVqzU0Q3iTOEjduzMggEhtzySabO%2FtkqlTPT0a2rH39ZvJX%2F3M6naEVXBb0oqOAmHgUKPsaOG7z4KktiofAmimCbTwMHquNlKpBcE%2FhqX9jYCqkwR4MYmaqumwJ%2FGJ1vbaVxcOLcWFTlPrfyzrur64u104gWiCcvshDP%2BD6edt3W9ZSFZYFAgndyfBStDtXGpUWwKrqk1fmrBj%2BzgH2eK66KMVUrcJcDPjO663tBvRXsLZ8o6W%2BkmJMUISRaBE%2Fvl%2Fy5J3HQKWC%2F2ybmfW5n4mitx%2BqycdTx4z%2BEsYWQuMUIGihMBkS7eQGnrXKsHC%2BIZp8Fg4%2FJx9wt2bwG5pTN3TsxceuNIaAw68MVFfCTbCwyM9YkMpmKGI9CtFCQgjESMmWbar5BRsRDRqCNIC0rCjcq2P1CbxpGX3XZcAQRgQttw%2BcQkvLe0cwOMDTiRgLM1iUu%2F5ihwI3ti0Qd9pFrF60R0PcwvfbJERkve12jN7W%2BhKktZ3hHfrXUKxnCCwKwRH2sXbamtHhBc8VjbSFzdF2taOEmfG4wUF6PVvxB5L%2FrVkXcA2dYl87uz5MOliRNEg5a5bMSazb7pYLczQ9QN0CgBR3g2p9Inkwkf64zQY6pgFEtWND5SPW0%2BjioWMsKhBNRewM%2BR5%2FoKCAVMgbimbRcKybRnM%2FTmz1jCt%2FtM8xo6ErQqbD3gzQhz3oWq7Vw%2BPTv56QMipOiBXcyYPdQ6QLVMZLXldD0FJHNjvdOvFPRynuwlxmPr8BPfYYUYqVyRgDhEobK%2BoMcV%2Bu9OeYL%2BU%2BkDwLZvbioOQ%2BuUhA4zDXgg8xByQKw2IuIoSO%2F38QRI1Tj0VNvq7U&X-Amz-Signature=9e708fa30be159ef448d90e42952f3d2d6c347e451529bd9dbfd30248452f479&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NTH3TJV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIDqN9J6RFUk0fwqhJefuBCYAPKmrCpUxvNqFMHli3eXEAiAE7LWqDJrURaj3BbZboIXF9AlR0miuVjRQvwenliyQyCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMcYkI2aNExV7DXL9fKtwDwOe5eHnG6Xp7goAUP2e%2B2pzN7OVqzU0Q3iTOEjduzMggEhtzySabO%2FtkqlTPT0a2rH39ZvJX%2F3M6naEVXBb0oqOAmHgUKPsaOG7z4KktiofAmimCbTwMHquNlKpBcE%2FhqX9jYCqkwR4MYmaqumwJ%2FGJ1vbaVxcOLcWFTlPrfyzrur64u104gWiCcvshDP%2BD6edt3W9ZSFZYFAgndyfBStDtXGpUWwKrqk1fmrBj%2BzgH2eK66KMVUrcJcDPjO663tBvRXsLZ8o6W%2BkmJMUISRaBE%2Fvl%2Fy5J3HQKWC%2F2ybmfW5n4mitx%2BqycdTx4z%2BEsYWQuMUIGihMBkS7eQGnrXKsHC%2BIZp8Fg4%2FJx9wt2bwG5pTN3TsxceuNIaAw68MVFfCTbCwyM9YkMpmKGI9CtFCQgjESMmWbar5BRsRDRqCNIC0rCjcq2P1CbxpGX3XZcAQRgQttw%2BcQkvLe0cwOMDTiRgLM1iUu%2F5ihwI3ti0Qd9pFrF60R0PcwvfbJERkve12jN7W%2BhKktZ3hHfrXUKxnCCwKwRH2sXbamtHhBc8VjbSFzdF2taOEmfG4wUF6PVvxB5L%2FrVkXcA2dYl87uz5MOliRNEg5a5bMSazb7pYLczQ9QN0CgBR3g2p9Inkwkf64zQY6pgFEtWND5SPW0%2BjioWMsKhBNRewM%2BR5%2FoKCAVMgbimbRcKybRnM%2FTmz1jCt%2FtM8xo6ErQqbD3gzQhz3oWq7Vw%2BPTv56QMipOiBXcyYPdQ6QLVMZLXldD0FJHNjvdOvFPRynuwlxmPr8BPfYYUYqVyRgDhEobK%2BoMcV%2Bu9OeYL%2BU%2BkDwLZvbioOQ%2BuUhA4zDXgg8xByQKw2IuIoSO%2F38QRI1Tj0VNvq7U&X-Amz-Signature=6d13565500a877b52f5db19acc80f291804a53145d6ccfedf9cfc33242d2b8cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



