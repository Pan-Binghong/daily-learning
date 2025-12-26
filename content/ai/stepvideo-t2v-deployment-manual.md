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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ4MDBZS%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWK1GGg6yRLPe1zhFPCONUninaD2nYd09y0PiDNHXEuAiEA%2Bi8EdtPx82rKlqnOgcmdPe4UpdGTbkeeKldrYwLt5%2BQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDNH1NyrD0PKkhM92ASrcAzGd4d07J1Kfxyjh%2FnRwRqrD%2FypQi%2BN3kpnobIAchgYRh7Wa6W8fxGSFSDi%2Blkn7wRXC2WSLAy%2BgZC%2BsyBBkINSW6PmSurvh8ZrJXfnh5aX1Tj4Ki31ibapti1SD7EB3viwIabENMLjuo0x7%2Bf%2Ba7%2F1yOFM9YEGPK6P6YBhWNruhCNjH604ZvcImRujSHLBEKssGGwN8q59QIOjLbRQ5UvnQjck8Rk3eqDULJr8ZZqtBf5nIvyTAgGcJx574lm7PMZqkyT80BQPxClp7WQ64xMAgmnsAQm4%2FWY6qmg9MOFfF048DOxKcpsGBTME9ImJ5%2BfhB8LjEVkBtAZmS%2F0ZPhxIMRrcHZrwXAlBBy3y0UzRmXgIdGG9vm6c4pnvtcbuxvG9RBNeRxy1y0bNs9bJIfNnDI2H8%2BrGcChrNNVPD2EbMxda6pdv4xqaR1SNBKZbNJcM%2FlAVGP8gqWUEVu62%2BVGT%2FnkEiqN%2F%2Fh3xJkVzS9ew55F8cW0Q3qHaS9LbjJW%2BfYtwE9COc%2FulLZLtNH4FOKcUlz%2BrCaWPqXvWDJ70ErqSSlzdKgSPSvXB%2FEqZ2psFTM%2BQJtbPcy3LnCJrw7XLM3oZELLI%2FKtQUGjkZ08XPZVJmtwTD4i7c0j6Luy4DMPTOt8oGOqUBv7Oiben6%2BwwrofaJGz%2FDEwE4gMKYG%2BaH8LWyeBsiEu3SKAWkWlfco7BFP29Hm%2F8mYq4%2BT44NXvT7%2F1%2FN%2B5et%2Fdbh9uCaIL1QOx8A7TWIXeE9SeV6mrwSMWE%2FT4SXqc5oaxchZtcz9mNM4IuBa0jTzQDmmH9wCD8Z284EgT6uGTrGiKqr4bdpf4SWaqP7pjbQ3%2B1SekgP5unlIPAah%2BoJKCK3n19H&X-Amz-Signature=b5efb8250eed99ba7eb92226c02b744c2a0c24ec031809b8ddd9470e740eb0c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ4MDBZS%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWK1GGg6yRLPe1zhFPCONUninaD2nYd09y0PiDNHXEuAiEA%2Bi8EdtPx82rKlqnOgcmdPe4UpdGTbkeeKldrYwLt5%2BQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDNH1NyrD0PKkhM92ASrcAzGd4d07J1Kfxyjh%2FnRwRqrD%2FypQi%2BN3kpnobIAchgYRh7Wa6W8fxGSFSDi%2Blkn7wRXC2WSLAy%2BgZC%2BsyBBkINSW6PmSurvh8ZrJXfnh5aX1Tj4Ki31ibapti1SD7EB3viwIabENMLjuo0x7%2Bf%2Ba7%2F1yOFM9YEGPK6P6YBhWNruhCNjH604ZvcImRujSHLBEKssGGwN8q59QIOjLbRQ5UvnQjck8Rk3eqDULJr8ZZqtBf5nIvyTAgGcJx574lm7PMZqkyT80BQPxClp7WQ64xMAgmnsAQm4%2FWY6qmg9MOFfF048DOxKcpsGBTME9ImJ5%2BfhB8LjEVkBtAZmS%2F0ZPhxIMRrcHZrwXAlBBy3y0UzRmXgIdGG9vm6c4pnvtcbuxvG9RBNeRxy1y0bNs9bJIfNnDI2H8%2BrGcChrNNVPD2EbMxda6pdv4xqaR1SNBKZbNJcM%2FlAVGP8gqWUEVu62%2BVGT%2FnkEiqN%2F%2Fh3xJkVzS9ew55F8cW0Q3qHaS9LbjJW%2BfYtwE9COc%2FulLZLtNH4FOKcUlz%2BrCaWPqXvWDJ70ErqSSlzdKgSPSvXB%2FEqZ2psFTM%2BQJtbPcy3LnCJrw7XLM3oZELLI%2FKtQUGjkZ08XPZVJmtwTD4i7c0j6Luy4DMPTOt8oGOqUBv7Oiben6%2BwwrofaJGz%2FDEwE4gMKYG%2BaH8LWyeBsiEu3SKAWkWlfco7BFP29Hm%2F8mYq4%2BT44NXvT7%2F1%2FN%2B5et%2Fdbh9uCaIL1QOx8A7TWIXeE9SeV6mrwSMWE%2FT4SXqc5oaxchZtcz9mNM4IuBa0jTzQDmmH9wCD8Z284EgT6uGTrGiKqr4bdpf4SWaqP7pjbQ3%2B1SekgP5unlIPAah%2BoJKCK3n19H&X-Amz-Signature=15d10697f208f0850c4490bc5fba3639143201653888cec8bb62dc536dcb3114&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ4MDBZS%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWK1GGg6yRLPe1zhFPCONUninaD2nYd09y0PiDNHXEuAiEA%2Bi8EdtPx82rKlqnOgcmdPe4UpdGTbkeeKldrYwLt5%2BQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDNH1NyrD0PKkhM92ASrcAzGd4d07J1Kfxyjh%2FnRwRqrD%2FypQi%2BN3kpnobIAchgYRh7Wa6W8fxGSFSDi%2Blkn7wRXC2WSLAy%2BgZC%2BsyBBkINSW6PmSurvh8ZrJXfnh5aX1Tj4Ki31ibapti1SD7EB3viwIabENMLjuo0x7%2Bf%2Ba7%2F1yOFM9YEGPK6P6YBhWNruhCNjH604ZvcImRujSHLBEKssGGwN8q59QIOjLbRQ5UvnQjck8Rk3eqDULJr8ZZqtBf5nIvyTAgGcJx574lm7PMZqkyT80BQPxClp7WQ64xMAgmnsAQm4%2FWY6qmg9MOFfF048DOxKcpsGBTME9ImJ5%2BfhB8LjEVkBtAZmS%2F0ZPhxIMRrcHZrwXAlBBy3y0UzRmXgIdGG9vm6c4pnvtcbuxvG9RBNeRxy1y0bNs9bJIfNnDI2H8%2BrGcChrNNVPD2EbMxda6pdv4xqaR1SNBKZbNJcM%2FlAVGP8gqWUEVu62%2BVGT%2FnkEiqN%2F%2Fh3xJkVzS9ew55F8cW0Q3qHaS9LbjJW%2BfYtwE9COc%2FulLZLtNH4FOKcUlz%2BrCaWPqXvWDJ70ErqSSlzdKgSPSvXB%2FEqZ2psFTM%2BQJtbPcy3LnCJrw7XLM3oZELLI%2FKtQUGjkZ08XPZVJmtwTD4i7c0j6Luy4DMPTOt8oGOqUBv7Oiben6%2BwwrofaJGz%2FDEwE4gMKYG%2BaH8LWyeBsiEu3SKAWkWlfco7BFP29Hm%2F8mYq4%2BT44NXvT7%2F1%2FN%2B5et%2Fdbh9uCaIL1QOx8A7TWIXeE9SeV6mrwSMWE%2FT4SXqc5oaxchZtcz9mNM4IuBa0jTzQDmmH9wCD8Z284EgT6uGTrGiKqr4bdpf4SWaqP7pjbQ3%2B1SekgP5unlIPAah%2BoJKCK3n19H&X-Amz-Signature=6c6467559971ba1f03e1febf399657df0b291da5e276df560499148c47dba28c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ4MDBZS%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWK1GGg6yRLPe1zhFPCONUninaD2nYd09y0PiDNHXEuAiEA%2Bi8EdtPx82rKlqnOgcmdPe4UpdGTbkeeKldrYwLt5%2BQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDNH1NyrD0PKkhM92ASrcAzGd4d07J1Kfxyjh%2FnRwRqrD%2FypQi%2BN3kpnobIAchgYRh7Wa6W8fxGSFSDi%2Blkn7wRXC2WSLAy%2BgZC%2BsyBBkINSW6PmSurvh8ZrJXfnh5aX1Tj4Ki31ibapti1SD7EB3viwIabENMLjuo0x7%2Bf%2Ba7%2F1yOFM9YEGPK6P6YBhWNruhCNjH604ZvcImRujSHLBEKssGGwN8q59QIOjLbRQ5UvnQjck8Rk3eqDULJr8ZZqtBf5nIvyTAgGcJx574lm7PMZqkyT80BQPxClp7WQ64xMAgmnsAQm4%2FWY6qmg9MOFfF048DOxKcpsGBTME9ImJ5%2BfhB8LjEVkBtAZmS%2F0ZPhxIMRrcHZrwXAlBBy3y0UzRmXgIdGG9vm6c4pnvtcbuxvG9RBNeRxy1y0bNs9bJIfNnDI2H8%2BrGcChrNNVPD2EbMxda6pdv4xqaR1SNBKZbNJcM%2FlAVGP8gqWUEVu62%2BVGT%2FnkEiqN%2F%2Fh3xJkVzS9ew55F8cW0Q3qHaS9LbjJW%2BfYtwE9COc%2FulLZLtNH4FOKcUlz%2BrCaWPqXvWDJ70ErqSSlzdKgSPSvXB%2FEqZ2psFTM%2BQJtbPcy3LnCJrw7XLM3oZELLI%2FKtQUGjkZ08XPZVJmtwTD4i7c0j6Luy4DMPTOt8oGOqUBv7Oiben6%2BwwrofaJGz%2FDEwE4gMKYG%2BaH8LWyeBsiEu3SKAWkWlfco7BFP29Hm%2F8mYq4%2BT44NXvT7%2F1%2FN%2B5et%2Fdbh9uCaIL1QOx8A7TWIXeE9SeV6mrwSMWE%2FT4SXqc5oaxchZtcz9mNM4IuBa0jTzQDmmH9wCD8Z284EgT6uGTrGiKqr4bdpf4SWaqP7pjbQ3%2B1SekgP5unlIPAah%2BoJKCK3n19H&X-Amz-Signature=a82ed24a85be66cd9f1932e70081c7238351984cc89139177a393d94e7e1222e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



