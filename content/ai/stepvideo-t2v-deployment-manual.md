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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH33HYQ4%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHIgkNow6KXQ3cukiTaKJ1MXdd8QK6E%2FQPpd2khkp2YAiBRopxNUm4xDzRd6cwnIb%2FdlHvtcJ5siOWGjSjkpRXKqyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMK%2FlOPxsT0i2iQ8UeKtwDOpqtEOY4TmpVYPpZXmlvLvTpdA%2F8pk6bIWjkjcGP7wOmgUIoqK7C9eEM2qZpd2sXHEj6nYyeCJKZfgYcinj0Y7pkPHHmzmTXNde1b4tVysjz5kBhmf6HbON6hGOgBLu%2FQzJ7DK0QAY9mv8uC0pHZkkF6DiSurfNhKfmt6zi7tW0nZlkZnVE6%2FwEkJXgG56UtZeXCBt5Jf7Rik0I%2B4fX%2BrKIFnxmsQBuWhSL1z76GuwCt24ucMml4g5QhrQsRQLbecoRsTtYF0I8kusbI5SbYcyeH0YRXWpeLqGVEr93DpquUY8oVquGfsYADSpwRIytXTEXVPgVMf4OUtF9zmnihdYaqQDTBTgM99tpnI96renMGCNGiSWi9x3ysk7bvt9GEX4a4h7FUsmKklr8UOqqGYb97Ia%2FhjFXgrzYQ9ZqNUv%2BONquV%2FPC%2BuvOW1r%2FCAQenTBlbVwildGSHKRjmQDRCUICLdRwzYasxWHDbK%2BBcr4HWE8%2FF1sE3JM6ZMEPuXJ%2FVAZ7SeDSQvesqL%2FR7iVEQgm3QPCmvUE1q35YjH291ezViKLjOXqbsT3MPTf42bBODGdwM5%2Fhv7O8ahrm6ziSfy1MOXJkP1hu15Nh8ZaxrzD1n1B9geX4TMaGEEH4wy4bszgY6pgHR9zuyV6fcMoFOpAijR8PSf%2BOT3KMAYZyP5XQ%2B3537PhirHrai61dVgO6CxXAgcUwFogxgQ1PLGRXWYiQfVzB6j%2FDBiZ3pxy9uygksf7x18ixAeIv7AcbQ7qOeXnrvhLVEjXI2LSv1RGKGDdUyd0s0AI901v8RUyHVhzGxat%2BArTvnf0eY%2B8GpVQFHQdNH2dUdrcJTdoMXGxckeKVe%2FhUZLJgG7v9H&X-Amz-Signature=94067c0600f61b7cd2be0717a06082f941edca2271f1d7e93fc872dd3b2f54c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH33HYQ4%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHIgkNow6KXQ3cukiTaKJ1MXdd8QK6E%2FQPpd2khkp2YAiBRopxNUm4xDzRd6cwnIb%2FdlHvtcJ5siOWGjSjkpRXKqyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMK%2FlOPxsT0i2iQ8UeKtwDOpqtEOY4TmpVYPpZXmlvLvTpdA%2F8pk6bIWjkjcGP7wOmgUIoqK7C9eEM2qZpd2sXHEj6nYyeCJKZfgYcinj0Y7pkPHHmzmTXNde1b4tVysjz5kBhmf6HbON6hGOgBLu%2FQzJ7DK0QAY9mv8uC0pHZkkF6DiSurfNhKfmt6zi7tW0nZlkZnVE6%2FwEkJXgG56UtZeXCBt5Jf7Rik0I%2B4fX%2BrKIFnxmsQBuWhSL1z76GuwCt24ucMml4g5QhrQsRQLbecoRsTtYF0I8kusbI5SbYcyeH0YRXWpeLqGVEr93DpquUY8oVquGfsYADSpwRIytXTEXVPgVMf4OUtF9zmnihdYaqQDTBTgM99tpnI96renMGCNGiSWi9x3ysk7bvt9GEX4a4h7FUsmKklr8UOqqGYb97Ia%2FhjFXgrzYQ9ZqNUv%2BONquV%2FPC%2BuvOW1r%2FCAQenTBlbVwildGSHKRjmQDRCUICLdRwzYasxWHDbK%2BBcr4HWE8%2FF1sE3JM6ZMEPuXJ%2FVAZ7SeDSQvesqL%2FR7iVEQgm3QPCmvUE1q35YjH291ezViKLjOXqbsT3MPTf42bBODGdwM5%2Fhv7O8ahrm6ziSfy1MOXJkP1hu15Nh8ZaxrzD1n1B9geX4TMaGEEH4wy4bszgY6pgHR9zuyV6fcMoFOpAijR8PSf%2BOT3KMAYZyP5XQ%2B3537PhirHrai61dVgO6CxXAgcUwFogxgQ1PLGRXWYiQfVzB6j%2FDBiZ3pxy9uygksf7x18ixAeIv7AcbQ7qOeXnrvhLVEjXI2LSv1RGKGDdUyd0s0AI901v8RUyHVhzGxat%2BArTvnf0eY%2B8GpVQFHQdNH2dUdrcJTdoMXGxckeKVe%2FhUZLJgG7v9H&X-Amz-Signature=24e66abfc8738b5a3e8f225897cb2377e77f64ea0f8e510bb5af8255d8d498c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH33HYQ4%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHIgkNow6KXQ3cukiTaKJ1MXdd8QK6E%2FQPpd2khkp2YAiBRopxNUm4xDzRd6cwnIb%2FdlHvtcJ5siOWGjSjkpRXKqyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMK%2FlOPxsT0i2iQ8UeKtwDOpqtEOY4TmpVYPpZXmlvLvTpdA%2F8pk6bIWjkjcGP7wOmgUIoqK7C9eEM2qZpd2sXHEj6nYyeCJKZfgYcinj0Y7pkPHHmzmTXNde1b4tVysjz5kBhmf6HbON6hGOgBLu%2FQzJ7DK0QAY9mv8uC0pHZkkF6DiSurfNhKfmt6zi7tW0nZlkZnVE6%2FwEkJXgG56UtZeXCBt5Jf7Rik0I%2B4fX%2BrKIFnxmsQBuWhSL1z76GuwCt24ucMml4g5QhrQsRQLbecoRsTtYF0I8kusbI5SbYcyeH0YRXWpeLqGVEr93DpquUY8oVquGfsYADSpwRIytXTEXVPgVMf4OUtF9zmnihdYaqQDTBTgM99tpnI96renMGCNGiSWi9x3ysk7bvt9GEX4a4h7FUsmKklr8UOqqGYb97Ia%2FhjFXgrzYQ9ZqNUv%2BONquV%2FPC%2BuvOW1r%2FCAQenTBlbVwildGSHKRjmQDRCUICLdRwzYasxWHDbK%2BBcr4HWE8%2FF1sE3JM6ZMEPuXJ%2FVAZ7SeDSQvesqL%2FR7iVEQgm3QPCmvUE1q35YjH291ezViKLjOXqbsT3MPTf42bBODGdwM5%2Fhv7O8ahrm6ziSfy1MOXJkP1hu15Nh8ZaxrzD1n1B9geX4TMaGEEH4wy4bszgY6pgHR9zuyV6fcMoFOpAijR8PSf%2BOT3KMAYZyP5XQ%2B3537PhirHrai61dVgO6CxXAgcUwFogxgQ1PLGRXWYiQfVzB6j%2FDBiZ3pxy9uygksf7x18ixAeIv7AcbQ7qOeXnrvhLVEjXI2LSv1RGKGDdUyd0s0AI901v8RUyHVhzGxat%2BArTvnf0eY%2B8GpVQFHQdNH2dUdrcJTdoMXGxckeKVe%2FhUZLJgG7v9H&X-Amz-Signature=548ad2208004c46624ae7b7e0dbc0bb41ff6df417299e4ec446a268eb3bc8fd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH33HYQ4%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHIgkNow6KXQ3cukiTaKJ1MXdd8QK6E%2FQPpd2khkp2YAiBRopxNUm4xDzRd6cwnIb%2FdlHvtcJ5siOWGjSjkpRXKqyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMK%2FlOPxsT0i2iQ8UeKtwDOpqtEOY4TmpVYPpZXmlvLvTpdA%2F8pk6bIWjkjcGP7wOmgUIoqK7C9eEM2qZpd2sXHEj6nYyeCJKZfgYcinj0Y7pkPHHmzmTXNde1b4tVysjz5kBhmf6HbON6hGOgBLu%2FQzJ7DK0QAY9mv8uC0pHZkkF6DiSurfNhKfmt6zi7tW0nZlkZnVE6%2FwEkJXgG56UtZeXCBt5Jf7Rik0I%2B4fX%2BrKIFnxmsQBuWhSL1z76GuwCt24ucMml4g5QhrQsRQLbecoRsTtYF0I8kusbI5SbYcyeH0YRXWpeLqGVEr93DpquUY8oVquGfsYADSpwRIytXTEXVPgVMf4OUtF9zmnihdYaqQDTBTgM99tpnI96renMGCNGiSWi9x3ysk7bvt9GEX4a4h7FUsmKklr8UOqqGYb97Ia%2FhjFXgrzYQ9ZqNUv%2BONquV%2FPC%2BuvOW1r%2FCAQenTBlbVwildGSHKRjmQDRCUICLdRwzYasxWHDbK%2BBcr4HWE8%2FF1sE3JM6ZMEPuXJ%2FVAZ7SeDSQvesqL%2FR7iVEQgm3QPCmvUE1q35YjH291ezViKLjOXqbsT3MPTf42bBODGdwM5%2Fhv7O8ahrm6ziSfy1MOXJkP1hu15Nh8ZaxrzD1n1B9geX4TMaGEEH4wy4bszgY6pgHR9zuyV6fcMoFOpAijR8PSf%2BOT3KMAYZyP5XQ%2B3537PhirHrai61dVgO6CxXAgcUwFogxgQ1PLGRXWYiQfVzB6j%2FDBiZ3pxy9uygksf7x18ixAeIv7AcbQ7qOeXnrvhLVEjXI2LSv1RGKGDdUyd0s0AI901v8RUyHVhzGxat%2BArTvnf0eY%2B8GpVQFHQdNH2dUdrcJTdoMXGxckeKVe%2FhUZLJgG7v9H&X-Amz-Signature=7b954cd7cf8cdb7208afc25a7403661f8752856f884017164cf20920b9c0c278&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



