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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QALCOXQV%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIEi%2BfwIcrqSebxSrUoBE%2BPcXcjJLbinsDhBjWie1brxBAiAUUS7bTo5FXvQZfSNBkZOHbN7eHEB2%2Fb5moSDrh5RzSyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMoUOVvovxu8XVpwaLKtwDxb5F%2F9QqCFCnklkP5lOg47weN00uTRNnuMzLr2%2Bvyme62LWKZOwkWaXqv53N31q%2BcHUMqiR9lz%2FN8aaXe6BNu3%2Face%2B9XCFRz4iIyEcud5G2SVrCmPg7RhHaGU%2BRCeOF2%2FavntGFXCmPp051QTArO0LqO1MdFCqzGN3f68IhgjttPkzeCb6MAb64ESg0SrlofwjtaSa685pFpmQVmUeNPu7XIoNioCk78t%2F0LuUTaSvZ0oEwRqkjio27VxnL2%2Bn07VPfgeG%2BBMEPoq0r0YMoGwGi8N07Q2KZ3IPtzbccsPeGE27UupUyOJoIrHZOLSJXUkQQ6PGW7uDpZdJ8UQDwb25LKSdGKSirL%2BlunRt1dNdH3ECcJnnja0q%2BaSOuZVmGghy5hQ7zde7QKdHH8Dd3LR7KL4rCoQ%2FnR%2FMqKmbnyi2b82EjtBlzsj3z0EHIL%2BLTyvHWXJiwkYGBpWQH%2BLRGoiV7yDwBICg4vaRpN1qyNwfqpzxepZwdq%2FgBzNki8nd5HjN8FLgCK%2Bv47iBe8kXfsu99D4SaeArzzNbT8vMIFSwJ5eMTwZWdVpYZOPdfmerHy1mLO1%2F16aAdEqhofMkJR16iTvKvd75GoxjgmMsJ4ZCa7zMK6avdo8g89pwwsu6bywY6pgELpB8DErm86XTIaikFD51MtKmjW9ECiX4bPeGIrqByaz2YmE3adA6v6LU2TDYSFMKD8GDARtnM%2Bq00wN%2F4iEbwR7ACCalzS0ptIvX97lX1tFjxLFhbUooVfUOg9lvfwJzIRF4wlUCBKLaLq1T%2FMHlgi10q%2FJ%2FNNtFIHR91WM2VT9TTEbr2BQ%2FGE9kkVnwYrVc2GEYuFDKz4Ad61mqrjXxpdAUD1pO4&X-Amz-Signature=fba7b4415b98cc57e43e342df61c55c5c9e59c92bb5fbe5877cd97004f1a1189&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QALCOXQV%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIEi%2BfwIcrqSebxSrUoBE%2BPcXcjJLbinsDhBjWie1brxBAiAUUS7bTo5FXvQZfSNBkZOHbN7eHEB2%2Fb5moSDrh5RzSyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMoUOVvovxu8XVpwaLKtwDxb5F%2F9QqCFCnklkP5lOg47weN00uTRNnuMzLr2%2Bvyme62LWKZOwkWaXqv53N31q%2BcHUMqiR9lz%2FN8aaXe6BNu3%2Face%2B9XCFRz4iIyEcud5G2SVrCmPg7RhHaGU%2BRCeOF2%2FavntGFXCmPp051QTArO0LqO1MdFCqzGN3f68IhgjttPkzeCb6MAb64ESg0SrlofwjtaSa685pFpmQVmUeNPu7XIoNioCk78t%2F0LuUTaSvZ0oEwRqkjio27VxnL2%2Bn07VPfgeG%2BBMEPoq0r0YMoGwGi8N07Q2KZ3IPtzbccsPeGE27UupUyOJoIrHZOLSJXUkQQ6PGW7uDpZdJ8UQDwb25LKSdGKSirL%2BlunRt1dNdH3ECcJnnja0q%2BaSOuZVmGghy5hQ7zde7QKdHH8Dd3LR7KL4rCoQ%2FnR%2FMqKmbnyi2b82EjtBlzsj3z0EHIL%2BLTyvHWXJiwkYGBpWQH%2BLRGoiV7yDwBICg4vaRpN1qyNwfqpzxepZwdq%2FgBzNki8nd5HjN8FLgCK%2Bv47iBe8kXfsu99D4SaeArzzNbT8vMIFSwJ5eMTwZWdVpYZOPdfmerHy1mLO1%2F16aAdEqhofMkJR16iTvKvd75GoxjgmMsJ4ZCa7zMK6avdo8g89pwwsu6bywY6pgELpB8DErm86XTIaikFD51MtKmjW9ECiX4bPeGIrqByaz2YmE3adA6v6LU2TDYSFMKD8GDARtnM%2Bq00wN%2F4iEbwR7ACCalzS0ptIvX97lX1tFjxLFhbUooVfUOg9lvfwJzIRF4wlUCBKLaLq1T%2FMHlgi10q%2FJ%2FNNtFIHR91WM2VT9TTEbr2BQ%2FGE9kkVnwYrVc2GEYuFDKz4Ad61mqrjXxpdAUD1pO4&X-Amz-Signature=a006a998b2247e131aaeb13ab99272867c1ef5862d67a89dac6974ed85ebeea8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QALCOXQV%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIEi%2BfwIcrqSebxSrUoBE%2BPcXcjJLbinsDhBjWie1brxBAiAUUS7bTo5FXvQZfSNBkZOHbN7eHEB2%2Fb5moSDrh5RzSyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMoUOVvovxu8XVpwaLKtwDxb5F%2F9QqCFCnklkP5lOg47weN00uTRNnuMzLr2%2Bvyme62LWKZOwkWaXqv53N31q%2BcHUMqiR9lz%2FN8aaXe6BNu3%2Face%2B9XCFRz4iIyEcud5G2SVrCmPg7RhHaGU%2BRCeOF2%2FavntGFXCmPp051QTArO0LqO1MdFCqzGN3f68IhgjttPkzeCb6MAb64ESg0SrlofwjtaSa685pFpmQVmUeNPu7XIoNioCk78t%2F0LuUTaSvZ0oEwRqkjio27VxnL2%2Bn07VPfgeG%2BBMEPoq0r0YMoGwGi8N07Q2KZ3IPtzbccsPeGE27UupUyOJoIrHZOLSJXUkQQ6PGW7uDpZdJ8UQDwb25LKSdGKSirL%2BlunRt1dNdH3ECcJnnja0q%2BaSOuZVmGghy5hQ7zde7QKdHH8Dd3LR7KL4rCoQ%2FnR%2FMqKmbnyi2b82EjtBlzsj3z0EHIL%2BLTyvHWXJiwkYGBpWQH%2BLRGoiV7yDwBICg4vaRpN1qyNwfqpzxepZwdq%2FgBzNki8nd5HjN8FLgCK%2Bv47iBe8kXfsu99D4SaeArzzNbT8vMIFSwJ5eMTwZWdVpYZOPdfmerHy1mLO1%2F16aAdEqhofMkJR16iTvKvd75GoxjgmMsJ4ZCa7zMK6avdo8g89pwwsu6bywY6pgELpB8DErm86XTIaikFD51MtKmjW9ECiX4bPeGIrqByaz2YmE3adA6v6LU2TDYSFMKD8GDARtnM%2Bq00wN%2F4iEbwR7ACCalzS0ptIvX97lX1tFjxLFhbUooVfUOg9lvfwJzIRF4wlUCBKLaLq1T%2FMHlgi10q%2FJ%2FNNtFIHR91WM2VT9TTEbr2BQ%2FGE9kkVnwYrVc2GEYuFDKz4Ad61mqrjXxpdAUD1pO4&X-Amz-Signature=0d2b9a4edbbf48caa6ed57fd2a8904a3caca0587b635a1fbb66894aea5d52392&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QALCOXQV%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIEi%2BfwIcrqSebxSrUoBE%2BPcXcjJLbinsDhBjWie1brxBAiAUUS7bTo5FXvQZfSNBkZOHbN7eHEB2%2Fb5moSDrh5RzSyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMoUOVvovxu8XVpwaLKtwDxb5F%2F9QqCFCnklkP5lOg47weN00uTRNnuMzLr2%2Bvyme62LWKZOwkWaXqv53N31q%2BcHUMqiR9lz%2FN8aaXe6BNu3%2Face%2B9XCFRz4iIyEcud5G2SVrCmPg7RhHaGU%2BRCeOF2%2FavntGFXCmPp051QTArO0LqO1MdFCqzGN3f68IhgjttPkzeCb6MAb64ESg0SrlofwjtaSa685pFpmQVmUeNPu7XIoNioCk78t%2F0LuUTaSvZ0oEwRqkjio27VxnL2%2Bn07VPfgeG%2BBMEPoq0r0YMoGwGi8N07Q2KZ3IPtzbccsPeGE27UupUyOJoIrHZOLSJXUkQQ6PGW7uDpZdJ8UQDwb25LKSdGKSirL%2BlunRt1dNdH3ECcJnnja0q%2BaSOuZVmGghy5hQ7zde7QKdHH8Dd3LR7KL4rCoQ%2FnR%2FMqKmbnyi2b82EjtBlzsj3z0EHIL%2BLTyvHWXJiwkYGBpWQH%2BLRGoiV7yDwBICg4vaRpN1qyNwfqpzxepZwdq%2FgBzNki8nd5HjN8FLgCK%2Bv47iBe8kXfsu99D4SaeArzzNbT8vMIFSwJ5eMTwZWdVpYZOPdfmerHy1mLO1%2F16aAdEqhofMkJR16iTvKvd75GoxjgmMsJ4ZCa7zMK6avdo8g89pwwsu6bywY6pgELpB8DErm86XTIaikFD51MtKmjW9ECiX4bPeGIrqByaz2YmE3adA6v6LU2TDYSFMKD8GDARtnM%2Bq00wN%2F4iEbwR7ACCalzS0ptIvX97lX1tFjxLFhbUooVfUOg9lvfwJzIRF4wlUCBKLaLq1T%2FMHlgi10q%2FJ%2FNNtFIHR91WM2VT9TTEbr2BQ%2FGE9kkVnwYrVc2GEYuFDKz4Ad61mqrjXxpdAUD1pO4&X-Amz-Signature=8b4e9ad2fe46a2b5981222b26fa796e96b535d88cc1be75a5c46486bbad3a9be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



