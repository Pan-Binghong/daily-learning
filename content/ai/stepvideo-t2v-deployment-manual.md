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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHMRPM54%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAgSIcR1HjepevUpHs%2FnhLr2pJld0%2BLrVLY8HqFQM6AyAiAYgKnFlNYQZBqkv9D4bgWZF4S0s%2BrBFrl0CkNfxrF8RSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNgupn8JPSbuPconrKtwDRcf0pSI5ezfmsYAdcHl%2Fre6JxmoEMCdsNjGYseLgSgf%2FvGW7PUnu6PLyJw73U4PYDWhvAG7uiRevU4RkIVe1hzF9FrK34Kj4XZV%2FB5CUBoyfcvIDu0I02rb%2F9lwTbCJ2V3WYvgz8XT8EY3rPIUYRPY5DFLtM7qXFU1l3Lkzr39xN237lQaD5RdDOJqRxTbuKV6eKxORP7g%2B5TOrWOESKkq3MXdVTd10oIve5eP7kbkN7t3NFE2pKozzMGikt9qwQpdv2F5AaXVXQdjGqZwhGj9cnTyv%2FQhnfm3kvknMt%2FEWMNxBbAZ1KUFqCQVcN5f9xVcr578drJEnmIYrPqCARsc5cso4kx2F4XbbQqqUnJi6pqUcKNYkIEOFKhrrUR0Slzh8dsDIg%2B0Ln%2FgrxDqztWZdVxB3Jrxt147KxBFzj5FmvmggqsUm874pdoUbg64i7gLPAmPKorRMpJ49tsuvAwDrSCiy7wHchQJ%2Fse03ZSK2T0dJ8BrL466ix1bn7dnmBYesbYmif4hhkynlHM2pYYfu9zpY5MCvqH9I7YzT19wdqmIgecM2xbFgWjDo2L%2B0HIyIbnMqSSK0LqDGZ8rRFUPqGah5w1GIpOten8tXV63CaXnVqJEscSxgR7qsww%2BPPyAY6pgHQu8b41z1hDor5k7xJOAfALiE1zPWFweCjfN4kYKbV24ErNTelnUjoSCuwm%2BnriZUu2Ys8nUPjZbcFq0BYb7yBIeg2QPheYQBThooy2JA3H31NTzLILwxSmsRY%2BresrvtxX7p9EVybNsh4%2FUltVxPHKJ1Ea9gHGU6j7S92YOgR4VpYkXkiwC9U4mLN9hrcCdBBcxEs3P6l32KXQpYSfzvpD3rPOtTe&X-Amz-Signature=2949f8d220722a1c6dfc74e3f1921675b2b467515f8f33464287bfd4613febea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHMRPM54%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAgSIcR1HjepevUpHs%2FnhLr2pJld0%2BLrVLY8HqFQM6AyAiAYgKnFlNYQZBqkv9D4bgWZF4S0s%2BrBFrl0CkNfxrF8RSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNgupn8JPSbuPconrKtwDRcf0pSI5ezfmsYAdcHl%2Fre6JxmoEMCdsNjGYseLgSgf%2FvGW7PUnu6PLyJw73U4PYDWhvAG7uiRevU4RkIVe1hzF9FrK34Kj4XZV%2FB5CUBoyfcvIDu0I02rb%2F9lwTbCJ2V3WYvgz8XT8EY3rPIUYRPY5DFLtM7qXFU1l3Lkzr39xN237lQaD5RdDOJqRxTbuKV6eKxORP7g%2B5TOrWOESKkq3MXdVTd10oIve5eP7kbkN7t3NFE2pKozzMGikt9qwQpdv2F5AaXVXQdjGqZwhGj9cnTyv%2FQhnfm3kvknMt%2FEWMNxBbAZ1KUFqCQVcN5f9xVcr578drJEnmIYrPqCARsc5cso4kx2F4XbbQqqUnJi6pqUcKNYkIEOFKhrrUR0Slzh8dsDIg%2B0Ln%2FgrxDqztWZdVxB3Jrxt147KxBFzj5FmvmggqsUm874pdoUbg64i7gLPAmPKorRMpJ49tsuvAwDrSCiy7wHchQJ%2Fse03ZSK2T0dJ8BrL466ix1bn7dnmBYesbYmif4hhkynlHM2pYYfu9zpY5MCvqH9I7YzT19wdqmIgecM2xbFgWjDo2L%2B0HIyIbnMqSSK0LqDGZ8rRFUPqGah5w1GIpOten8tXV63CaXnVqJEscSxgR7qsww%2BPPyAY6pgHQu8b41z1hDor5k7xJOAfALiE1zPWFweCjfN4kYKbV24ErNTelnUjoSCuwm%2BnriZUu2Ys8nUPjZbcFq0BYb7yBIeg2QPheYQBThooy2JA3H31NTzLILwxSmsRY%2BresrvtxX7p9EVybNsh4%2FUltVxPHKJ1Ea9gHGU6j7S92YOgR4VpYkXkiwC9U4mLN9hrcCdBBcxEs3P6l32KXQpYSfzvpD3rPOtTe&X-Amz-Signature=223a621b9aec675de14520e778c9a86f139e97d6927965431dc206e4a92c97c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHMRPM54%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAgSIcR1HjepevUpHs%2FnhLr2pJld0%2BLrVLY8HqFQM6AyAiAYgKnFlNYQZBqkv9D4bgWZF4S0s%2BrBFrl0CkNfxrF8RSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNgupn8JPSbuPconrKtwDRcf0pSI5ezfmsYAdcHl%2Fre6JxmoEMCdsNjGYseLgSgf%2FvGW7PUnu6PLyJw73U4PYDWhvAG7uiRevU4RkIVe1hzF9FrK34Kj4XZV%2FB5CUBoyfcvIDu0I02rb%2F9lwTbCJ2V3WYvgz8XT8EY3rPIUYRPY5DFLtM7qXFU1l3Lkzr39xN237lQaD5RdDOJqRxTbuKV6eKxORP7g%2B5TOrWOESKkq3MXdVTd10oIve5eP7kbkN7t3NFE2pKozzMGikt9qwQpdv2F5AaXVXQdjGqZwhGj9cnTyv%2FQhnfm3kvknMt%2FEWMNxBbAZ1KUFqCQVcN5f9xVcr578drJEnmIYrPqCARsc5cso4kx2F4XbbQqqUnJi6pqUcKNYkIEOFKhrrUR0Slzh8dsDIg%2B0Ln%2FgrxDqztWZdVxB3Jrxt147KxBFzj5FmvmggqsUm874pdoUbg64i7gLPAmPKorRMpJ49tsuvAwDrSCiy7wHchQJ%2Fse03ZSK2T0dJ8BrL466ix1bn7dnmBYesbYmif4hhkynlHM2pYYfu9zpY5MCvqH9I7YzT19wdqmIgecM2xbFgWjDo2L%2B0HIyIbnMqSSK0LqDGZ8rRFUPqGah5w1GIpOten8tXV63CaXnVqJEscSxgR7qsww%2BPPyAY6pgHQu8b41z1hDor5k7xJOAfALiE1zPWFweCjfN4kYKbV24ErNTelnUjoSCuwm%2BnriZUu2Ys8nUPjZbcFq0BYb7yBIeg2QPheYQBThooy2JA3H31NTzLILwxSmsRY%2BresrvtxX7p9EVybNsh4%2FUltVxPHKJ1Ea9gHGU6j7S92YOgR4VpYkXkiwC9U4mLN9hrcCdBBcxEs3P6l32KXQpYSfzvpD3rPOtTe&X-Amz-Signature=22f0b160c23229c4ebe03c02674015e2dc373d832606a81b2ce7506bb20783cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHMRPM54%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAgSIcR1HjepevUpHs%2FnhLr2pJld0%2BLrVLY8HqFQM6AyAiAYgKnFlNYQZBqkv9D4bgWZF4S0s%2BrBFrl0CkNfxrF8RSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMNgupn8JPSbuPconrKtwDRcf0pSI5ezfmsYAdcHl%2Fre6JxmoEMCdsNjGYseLgSgf%2FvGW7PUnu6PLyJw73U4PYDWhvAG7uiRevU4RkIVe1hzF9FrK34Kj4XZV%2FB5CUBoyfcvIDu0I02rb%2F9lwTbCJ2V3WYvgz8XT8EY3rPIUYRPY5DFLtM7qXFU1l3Lkzr39xN237lQaD5RdDOJqRxTbuKV6eKxORP7g%2B5TOrWOESKkq3MXdVTd10oIve5eP7kbkN7t3NFE2pKozzMGikt9qwQpdv2F5AaXVXQdjGqZwhGj9cnTyv%2FQhnfm3kvknMt%2FEWMNxBbAZ1KUFqCQVcN5f9xVcr578drJEnmIYrPqCARsc5cso4kx2F4XbbQqqUnJi6pqUcKNYkIEOFKhrrUR0Slzh8dsDIg%2B0Ln%2FgrxDqztWZdVxB3Jrxt147KxBFzj5FmvmggqsUm874pdoUbg64i7gLPAmPKorRMpJ49tsuvAwDrSCiy7wHchQJ%2Fse03ZSK2T0dJ8BrL466ix1bn7dnmBYesbYmif4hhkynlHM2pYYfu9zpY5MCvqH9I7YzT19wdqmIgecM2xbFgWjDo2L%2B0HIyIbnMqSSK0LqDGZ8rRFUPqGah5w1GIpOten8tXV63CaXnVqJEscSxgR7qsww%2BPPyAY6pgHQu8b41z1hDor5k7xJOAfALiE1zPWFweCjfN4kYKbV24ErNTelnUjoSCuwm%2BnriZUu2Ys8nUPjZbcFq0BYb7yBIeg2QPheYQBThooy2JA3H31NTzLILwxSmsRY%2BresrvtxX7p9EVybNsh4%2FUltVxPHKJ1Ea9gHGU6j7S92YOgR4VpYkXkiwC9U4mLN9hrcCdBBcxEs3P6l32KXQpYSfzvpD3rPOtTe&X-Amz-Signature=606eeac4a4e41cf2644a9ee7afe18cb832e0dc48f794e1878599bc37ab7015ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



