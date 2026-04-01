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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DPR4RSA%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6zugCpwlzxQY%2FXPUdDKXbgmbTUoaSp%2F8dvu1to8BAAAIhALMqHUvv%2FdJqz5JT5GOGYwwbHMa3Z8LA1Oh%2F1kWsLd1NKv8DCE0QABoMNjM3NDIzMTgzODA1IgyogMJzMy3HNyUzcQMq3AN5Tsfl6HxepSqIXfmEf%2FvBVg8rlk6y6xQAbENRUj3QJyvterVwweIUpq8RHAZ1dcTTEDe4LjQ4Dadp6X5DD5oJJO9kki9lgpbiq2Rl%2FWOVy6qGx7OuH9g1rkGbWUUQ%2FNrdANbeJJwZKF4DtzZ7V3wmtPAKAJkMKnI7axGBHYe13WfbFRafJ6jBS%2FVuUxCPek4trphdBy%2FGy8WfVy53SP0qQuDoO3cmCAmnAqwahJpX1gAEV%2FpdbBOLIjCV8lOMFlXrE3AbH3KRx73A1rApxVEqKBrYRIX%2FzUJCbJGe11dSWdTyNpORxX5P6WT7EzzDdPLK%2Fir5i4LaIFIHtBdFI6cUje9jqUdF6eWQkTrp0lollw%2BKAEhHz1aqasZR1GRIuUNNX5dGm7jW9lvb8uKx%2F3SSyLbkDb8wtS3tzQrXx43TxEddZK6k7RxDDmIG4UypqIbL990yGB9OlZ0avMDK1jrV9q3DsXBDUAI%2F9orvSfhJ%2BntHEe27oPX4PdIdh8Uz6H2P2zTreH%2BHzlAll46xpKAfbBq0Wfn2TdQs2G9tdRNJIZSXhAm7uyStZ6JcR%2FxOainbblbCI8bAK50097CN3SVxKc3523jizxGdgjB4DnjTirNZLktaH0KSrByVWzCGo7LOBjqkAY9bgK2PJNPgWXJYPIuzZQPmhzEMNUAnSaPUY0TWUy1%2Bz3YEy24LP8kECiMhOgZiP15xmNZAdMAhZ57HwnPsACpKUIkStUGTbrgsznt18CdcIZYKZBfPdXVu2Fq1tJt3hQBjy22MhAJfIAheKsPRla%2BLmEIVDCk3fk7scV9Bj12R5uMp35wOZnuHOsMVTm3jtheevEH6BUa75s8oouqgwuZusZHZ&X-Amz-Signature=604130a7eba261507f57f38ce44ad0dabb5e9fa019cfea843fe035ae31ac74b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DPR4RSA%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6zugCpwlzxQY%2FXPUdDKXbgmbTUoaSp%2F8dvu1to8BAAAIhALMqHUvv%2FdJqz5JT5GOGYwwbHMa3Z8LA1Oh%2F1kWsLd1NKv8DCE0QABoMNjM3NDIzMTgzODA1IgyogMJzMy3HNyUzcQMq3AN5Tsfl6HxepSqIXfmEf%2FvBVg8rlk6y6xQAbENRUj3QJyvterVwweIUpq8RHAZ1dcTTEDe4LjQ4Dadp6X5DD5oJJO9kki9lgpbiq2Rl%2FWOVy6qGx7OuH9g1rkGbWUUQ%2FNrdANbeJJwZKF4DtzZ7V3wmtPAKAJkMKnI7axGBHYe13WfbFRafJ6jBS%2FVuUxCPek4trphdBy%2FGy8WfVy53SP0qQuDoO3cmCAmnAqwahJpX1gAEV%2FpdbBOLIjCV8lOMFlXrE3AbH3KRx73A1rApxVEqKBrYRIX%2FzUJCbJGe11dSWdTyNpORxX5P6WT7EzzDdPLK%2Fir5i4LaIFIHtBdFI6cUje9jqUdF6eWQkTrp0lollw%2BKAEhHz1aqasZR1GRIuUNNX5dGm7jW9lvb8uKx%2F3SSyLbkDb8wtS3tzQrXx43TxEddZK6k7RxDDmIG4UypqIbL990yGB9OlZ0avMDK1jrV9q3DsXBDUAI%2F9orvSfhJ%2BntHEe27oPX4PdIdh8Uz6H2P2zTreH%2BHzlAll46xpKAfbBq0Wfn2TdQs2G9tdRNJIZSXhAm7uyStZ6JcR%2FxOainbblbCI8bAK50097CN3SVxKc3523jizxGdgjB4DnjTirNZLktaH0KSrByVWzCGo7LOBjqkAY9bgK2PJNPgWXJYPIuzZQPmhzEMNUAnSaPUY0TWUy1%2Bz3YEy24LP8kECiMhOgZiP15xmNZAdMAhZ57HwnPsACpKUIkStUGTbrgsznt18CdcIZYKZBfPdXVu2Fq1tJt3hQBjy22MhAJfIAheKsPRla%2BLmEIVDCk3fk7scV9Bj12R5uMp35wOZnuHOsMVTm3jtheevEH6BUa75s8oouqgwuZusZHZ&X-Amz-Signature=e52c58fca8636adae93ac04307606c6935571de47e1d4279c7bb391a24eb255f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DPR4RSA%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6zugCpwlzxQY%2FXPUdDKXbgmbTUoaSp%2F8dvu1to8BAAAIhALMqHUvv%2FdJqz5JT5GOGYwwbHMa3Z8LA1Oh%2F1kWsLd1NKv8DCE0QABoMNjM3NDIzMTgzODA1IgyogMJzMy3HNyUzcQMq3AN5Tsfl6HxepSqIXfmEf%2FvBVg8rlk6y6xQAbENRUj3QJyvterVwweIUpq8RHAZ1dcTTEDe4LjQ4Dadp6X5DD5oJJO9kki9lgpbiq2Rl%2FWOVy6qGx7OuH9g1rkGbWUUQ%2FNrdANbeJJwZKF4DtzZ7V3wmtPAKAJkMKnI7axGBHYe13WfbFRafJ6jBS%2FVuUxCPek4trphdBy%2FGy8WfVy53SP0qQuDoO3cmCAmnAqwahJpX1gAEV%2FpdbBOLIjCV8lOMFlXrE3AbH3KRx73A1rApxVEqKBrYRIX%2FzUJCbJGe11dSWdTyNpORxX5P6WT7EzzDdPLK%2Fir5i4LaIFIHtBdFI6cUje9jqUdF6eWQkTrp0lollw%2BKAEhHz1aqasZR1GRIuUNNX5dGm7jW9lvb8uKx%2F3SSyLbkDb8wtS3tzQrXx43TxEddZK6k7RxDDmIG4UypqIbL990yGB9OlZ0avMDK1jrV9q3DsXBDUAI%2F9orvSfhJ%2BntHEe27oPX4PdIdh8Uz6H2P2zTreH%2BHzlAll46xpKAfbBq0Wfn2TdQs2G9tdRNJIZSXhAm7uyStZ6JcR%2FxOainbblbCI8bAK50097CN3SVxKc3523jizxGdgjB4DnjTirNZLktaH0KSrByVWzCGo7LOBjqkAY9bgK2PJNPgWXJYPIuzZQPmhzEMNUAnSaPUY0TWUy1%2Bz3YEy24LP8kECiMhOgZiP15xmNZAdMAhZ57HwnPsACpKUIkStUGTbrgsznt18CdcIZYKZBfPdXVu2Fq1tJt3hQBjy22MhAJfIAheKsPRla%2BLmEIVDCk3fk7scV9Bj12R5uMp35wOZnuHOsMVTm3jtheevEH6BUa75s8oouqgwuZusZHZ&X-Amz-Signature=5911da9925219c1d2aa9d8850f915881f8448b7f13d61c91f01f811d5529430f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DPR4RSA%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6zugCpwlzxQY%2FXPUdDKXbgmbTUoaSp%2F8dvu1to8BAAAIhALMqHUvv%2FdJqz5JT5GOGYwwbHMa3Z8LA1Oh%2F1kWsLd1NKv8DCE0QABoMNjM3NDIzMTgzODA1IgyogMJzMy3HNyUzcQMq3AN5Tsfl6HxepSqIXfmEf%2FvBVg8rlk6y6xQAbENRUj3QJyvterVwweIUpq8RHAZ1dcTTEDe4LjQ4Dadp6X5DD5oJJO9kki9lgpbiq2Rl%2FWOVy6qGx7OuH9g1rkGbWUUQ%2FNrdANbeJJwZKF4DtzZ7V3wmtPAKAJkMKnI7axGBHYe13WfbFRafJ6jBS%2FVuUxCPek4trphdBy%2FGy8WfVy53SP0qQuDoO3cmCAmnAqwahJpX1gAEV%2FpdbBOLIjCV8lOMFlXrE3AbH3KRx73A1rApxVEqKBrYRIX%2FzUJCbJGe11dSWdTyNpORxX5P6WT7EzzDdPLK%2Fir5i4LaIFIHtBdFI6cUje9jqUdF6eWQkTrp0lollw%2BKAEhHz1aqasZR1GRIuUNNX5dGm7jW9lvb8uKx%2F3SSyLbkDb8wtS3tzQrXx43TxEddZK6k7RxDDmIG4UypqIbL990yGB9OlZ0avMDK1jrV9q3DsXBDUAI%2F9orvSfhJ%2BntHEe27oPX4PdIdh8Uz6H2P2zTreH%2BHzlAll46xpKAfbBq0Wfn2TdQs2G9tdRNJIZSXhAm7uyStZ6JcR%2FxOainbblbCI8bAK50097CN3SVxKc3523jizxGdgjB4DnjTirNZLktaH0KSrByVWzCGo7LOBjqkAY9bgK2PJNPgWXJYPIuzZQPmhzEMNUAnSaPUY0TWUy1%2Bz3YEy24LP8kECiMhOgZiP15xmNZAdMAhZ57HwnPsACpKUIkStUGTbrgsznt18CdcIZYKZBfPdXVu2Fq1tJt3hQBjy22MhAJfIAheKsPRla%2BLmEIVDCk3fk7scV9Bj12R5uMp35wOZnuHOsMVTm3jtheevEH6BUa75s8oouqgwuZusZHZ&X-Amz-Signature=3b3d71af899b4c8966879c01db179a8cb3bc1d8b6f391741a0fcdf26faee03e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



