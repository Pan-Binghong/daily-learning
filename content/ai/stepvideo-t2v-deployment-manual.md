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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW4W3XCC%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC1PUQ3f4gPakiSLiKYsv6TuqHYGaNEBIjxtzef1XxyEQIgRy1uROOfdPT5HGm%2Bg3JfXRVqO425Ua8DSVS1qmGxBYQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDF3pJR3OWNjwtJDLeCrcA14JPuoMWaNyNLIvENmgUMWizL7OQci6oDhSwCb04Qw67wFhHJiWCF2CUiOBrcfRe217i%2B7q9MlflVC9zooEAoIqxq5%2BiRONkTNz%2FqMLIxgnTcIT1RQF6fv2R2VhHoKgwK%2BcmZkxnxfN1jVQTY%2Ff%2FH6%2BGWrxt69nJyeihevVGkloVZMLDOu0C6%2FBZsc7HkIZdj6NO3jjh9Dd%2B0CR8gpOKDm4oGzKJTiHESfCyw6w5eP7RVZx5WWz68hEHFrST6L2eMzajcWMbdmg%2BWck0nKtcrqakgu9GClJqycEJ3bOE2prykN%2Bhzi90BT4BuymttBLTQ8lJHEGB9%2B1TmLx%2Fs%2BLWbUjyKYseUvdA6ckdycdFjNhpMPxpq2y%2F06dyte5HAv3oqM1YbraTU6gebHfu321%2BjNrc9Z0ByrpHwGvyleg4MdFGIe0VjYM3plAQkpEZWX%2BCzyzrKW66uPscv3CDAiNGbVqosZs8oTtbHNTQO8WhEZU%2FqK9q3IAT0u5WgzQem7AXQsVZ6O72FApk8OKdG%2BHhvvBCDjTTQqbL2egkNFnkkLyObu0cVmZAwBjfgDxbA%2Fl%2FSAfUOl6qCzitOeN%2Fj3PgPHiDfQOAV4arHTQLVZ5md8ltCigwi8Go7jagUN4MJCcocsGOqUBwA9wqKjPgF8VIFwiWJrsIpDthl%2FXbupck6bwF%2B%2FCOwqrTclmukTLVJ8miFiLk4sjJ%2BJIOsNSPLo6UH9HYj0h13Ix4xXGtPd8OVS7Hj1AxnQjt2XTKTzyGTHDJ7Ue%2F7phF2ZuLWE0Fhralb%2Buhk1CEYDtVUPRiLnp7TJGDgcueZ6xbj13YiPxkn8g6xkXv%2Bvn%2BAxFKKW8JCOHwTgBSdyNp%2BoIDRgR&X-Amz-Signature=972be6b7dd24f63846be55e8478c3b87a9f8f235c46bfb528693f812d45df484&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW4W3XCC%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC1PUQ3f4gPakiSLiKYsv6TuqHYGaNEBIjxtzef1XxyEQIgRy1uROOfdPT5HGm%2Bg3JfXRVqO425Ua8DSVS1qmGxBYQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDF3pJR3OWNjwtJDLeCrcA14JPuoMWaNyNLIvENmgUMWizL7OQci6oDhSwCb04Qw67wFhHJiWCF2CUiOBrcfRe217i%2B7q9MlflVC9zooEAoIqxq5%2BiRONkTNz%2FqMLIxgnTcIT1RQF6fv2R2VhHoKgwK%2BcmZkxnxfN1jVQTY%2Ff%2FH6%2BGWrxt69nJyeihevVGkloVZMLDOu0C6%2FBZsc7HkIZdj6NO3jjh9Dd%2B0CR8gpOKDm4oGzKJTiHESfCyw6w5eP7RVZx5WWz68hEHFrST6L2eMzajcWMbdmg%2BWck0nKtcrqakgu9GClJqycEJ3bOE2prykN%2Bhzi90BT4BuymttBLTQ8lJHEGB9%2B1TmLx%2Fs%2BLWbUjyKYseUvdA6ckdycdFjNhpMPxpq2y%2F06dyte5HAv3oqM1YbraTU6gebHfu321%2BjNrc9Z0ByrpHwGvyleg4MdFGIe0VjYM3plAQkpEZWX%2BCzyzrKW66uPscv3CDAiNGbVqosZs8oTtbHNTQO8WhEZU%2FqK9q3IAT0u5WgzQem7AXQsVZ6O72FApk8OKdG%2BHhvvBCDjTTQqbL2egkNFnkkLyObu0cVmZAwBjfgDxbA%2Fl%2FSAfUOl6qCzitOeN%2Fj3PgPHiDfQOAV4arHTQLVZ5md8ltCigwi8Go7jagUN4MJCcocsGOqUBwA9wqKjPgF8VIFwiWJrsIpDthl%2FXbupck6bwF%2B%2FCOwqrTclmukTLVJ8miFiLk4sjJ%2BJIOsNSPLo6UH9HYj0h13Ix4xXGtPd8OVS7Hj1AxnQjt2XTKTzyGTHDJ7Ue%2F7phF2ZuLWE0Fhralb%2Buhk1CEYDtVUPRiLnp7TJGDgcueZ6xbj13YiPxkn8g6xkXv%2Bvn%2BAxFKKW8JCOHwTgBSdyNp%2BoIDRgR&X-Amz-Signature=544f8b9e52f397e05abc8c5bdf9a3215d7eb59370bc66b489f978700a6c9e0a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW4W3XCC%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC1PUQ3f4gPakiSLiKYsv6TuqHYGaNEBIjxtzef1XxyEQIgRy1uROOfdPT5HGm%2Bg3JfXRVqO425Ua8DSVS1qmGxBYQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDF3pJR3OWNjwtJDLeCrcA14JPuoMWaNyNLIvENmgUMWizL7OQci6oDhSwCb04Qw67wFhHJiWCF2CUiOBrcfRe217i%2B7q9MlflVC9zooEAoIqxq5%2BiRONkTNz%2FqMLIxgnTcIT1RQF6fv2R2VhHoKgwK%2BcmZkxnxfN1jVQTY%2Ff%2FH6%2BGWrxt69nJyeihevVGkloVZMLDOu0C6%2FBZsc7HkIZdj6NO3jjh9Dd%2B0CR8gpOKDm4oGzKJTiHESfCyw6w5eP7RVZx5WWz68hEHFrST6L2eMzajcWMbdmg%2BWck0nKtcrqakgu9GClJqycEJ3bOE2prykN%2Bhzi90BT4BuymttBLTQ8lJHEGB9%2B1TmLx%2Fs%2BLWbUjyKYseUvdA6ckdycdFjNhpMPxpq2y%2F06dyte5HAv3oqM1YbraTU6gebHfu321%2BjNrc9Z0ByrpHwGvyleg4MdFGIe0VjYM3plAQkpEZWX%2BCzyzrKW66uPscv3CDAiNGbVqosZs8oTtbHNTQO8WhEZU%2FqK9q3IAT0u5WgzQem7AXQsVZ6O72FApk8OKdG%2BHhvvBCDjTTQqbL2egkNFnkkLyObu0cVmZAwBjfgDxbA%2Fl%2FSAfUOl6qCzitOeN%2Fj3PgPHiDfQOAV4arHTQLVZ5md8ltCigwi8Go7jagUN4MJCcocsGOqUBwA9wqKjPgF8VIFwiWJrsIpDthl%2FXbupck6bwF%2B%2FCOwqrTclmukTLVJ8miFiLk4sjJ%2BJIOsNSPLo6UH9HYj0h13Ix4xXGtPd8OVS7Hj1AxnQjt2XTKTzyGTHDJ7Ue%2F7phF2ZuLWE0Fhralb%2Buhk1CEYDtVUPRiLnp7TJGDgcueZ6xbj13YiPxkn8g6xkXv%2Bvn%2BAxFKKW8JCOHwTgBSdyNp%2BoIDRgR&X-Amz-Signature=e0d12abd251356ef1f3f6c9f5bc37de85387b99ef9b5c0af6551a1c6382fd3dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW4W3XCC%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC1PUQ3f4gPakiSLiKYsv6TuqHYGaNEBIjxtzef1XxyEQIgRy1uROOfdPT5HGm%2Bg3JfXRVqO425Ua8DSVS1qmGxBYQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDF3pJR3OWNjwtJDLeCrcA14JPuoMWaNyNLIvENmgUMWizL7OQci6oDhSwCb04Qw67wFhHJiWCF2CUiOBrcfRe217i%2B7q9MlflVC9zooEAoIqxq5%2BiRONkTNz%2FqMLIxgnTcIT1RQF6fv2R2VhHoKgwK%2BcmZkxnxfN1jVQTY%2Ff%2FH6%2BGWrxt69nJyeihevVGkloVZMLDOu0C6%2FBZsc7HkIZdj6NO3jjh9Dd%2B0CR8gpOKDm4oGzKJTiHESfCyw6w5eP7RVZx5WWz68hEHFrST6L2eMzajcWMbdmg%2BWck0nKtcrqakgu9GClJqycEJ3bOE2prykN%2Bhzi90BT4BuymttBLTQ8lJHEGB9%2B1TmLx%2Fs%2BLWbUjyKYseUvdA6ckdycdFjNhpMPxpq2y%2F06dyte5HAv3oqM1YbraTU6gebHfu321%2BjNrc9Z0ByrpHwGvyleg4MdFGIe0VjYM3plAQkpEZWX%2BCzyzrKW66uPscv3CDAiNGbVqosZs8oTtbHNTQO8WhEZU%2FqK9q3IAT0u5WgzQem7AXQsVZ6O72FApk8OKdG%2BHhvvBCDjTTQqbL2egkNFnkkLyObu0cVmZAwBjfgDxbA%2Fl%2FSAfUOl6qCzitOeN%2Fj3PgPHiDfQOAV4arHTQLVZ5md8ltCigwi8Go7jagUN4MJCcocsGOqUBwA9wqKjPgF8VIFwiWJrsIpDthl%2FXbupck6bwF%2B%2FCOwqrTclmukTLVJ8miFiLk4sjJ%2BJIOsNSPLo6UH9HYj0h13Ix4xXGtPd8OVS7Hj1AxnQjt2XTKTzyGTHDJ7Ue%2F7phF2ZuLWE0Fhralb%2Buhk1CEYDtVUPRiLnp7TJGDgcueZ6xbj13YiPxkn8g6xkXv%2Bvn%2BAxFKKW8JCOHwTgBSdyNp%2BoIDRgR&X-Amz-Signature=17db331b2527c6319edd1037d73c5c8102047fa1e12b696a51179cf9125e5265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



