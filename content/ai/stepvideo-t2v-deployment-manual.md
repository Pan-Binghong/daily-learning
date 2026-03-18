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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XI64BEC%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIFwgX%2B%2F8BHa50c2gWvygCkCfkONK%2FmpCfhm%2FVsBOLybWAiA8HpvjkQKSBNTD2s27AEQaTmCutO8ybvyWOOWzM7%2FT5SqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU4hiO%2F2urAsIFWl9KtwDbAE4nRS%2FS7wWgRxPJO%2FfBlXOuiLImDpVIfF0YYQe5s1z6pbSauzVB00E6hyCfsoxS16V1qXIiguvZy8V76jPa7HoqkmnFYInSMFlrt7fSVz%2Bffz1BZCBHzT1cKjeMM6BNqCZApjPUOCp9T4v5iVBPYD91Zua3CAUnyHP3R2mW4O7j0dOmVYEUpKHGHqV7oeWBBc56fhcretNU9%2BNeTBlB30Q8tOUJa8p5YdEltdGddUZ8hP7OBIP7kcqQrueez4NrvZZVhoVakNnXB%2BeBxKVRzu%2Bc4aj6RYGqLuTgAoHTF77ceLsfW4oKacZJWJoOciL%2FC1mAjMRr6n8ECeg0n%2BGuVzgh1cjj0jULe1zVi1wR1cR0mU7Cmbvkp9lJ9PYLPAuus96noPthVyXYZn3OiXRGnJzTFhdZpzIWFqLPR52hBVqUy5xSlIllPS8yo9lvwuv2bLuwJBtA1E16ejuzNChuipgvmSdYTjXvog1zeM%2FahYyRw1LAbg6ZG%2FwU7YYX1FCz9MCgsPrOe6lzl9BkH47zT%2FM%2B4UWW%2BCSm8Iq8c%2BtyRhCbp5eGi8LxptzZAEvvIkrQ3NiEDfY2PuCMhhEHyW5%2FpH5BcQPPW5uyieLZfDm54McKM7SFAU4xISdlfQwxaXozQY6pgHZPp8I%2FgGz0Za7ORase1z0prqS63E172TmebER9gO5qN%2BNj2DBSSFAOAB%2F1Oko%2FB39YI%2BEhK0POBM9jHZ%2BadmbFXtCbVWWHTkfHIvOL3FHPDbNqxSICJ8oGuk9BOHtrWKNYp%2B9r7tUteL3EwQVxnL%2F2PhCzKNaO2hP5T3%2BEkbjd6q50rpeSZ7aIiGD%2BDPGvEkcSAIr%2Fd2vc2Dhg3xJlRFuaETGuite&X-Amz-Signature=1afd774858fa44f4e44b8f480b34ab6b85f932129df2204f37e97f7e7dba1acd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XI64BEC%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIFwgX%2B%2F8BHa50c2gWvygCkCfkONK%2FmpCfhm%2FVsBOLybWAiA8HpvjkQKSBNTD2s27AEQaTmCutO8ybvyWOOWzM7%2FT5SqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU4hiO%2F2urAsIFWl9KtwDbAE4nRS%2FS7wWgRxPJO%2FfBlXOuiLImDpVIfF0YYQe5s1z6pbSauzVB00E6hyCfsoxS16V1qXIiguvZy8V76jPa7HoqkmnFYInSMFlrt7fSVz%2Bffz1BZCBHzT1cKjeMM6BNqCZApjPUOCp9T4v5iVBPYD91Zua3CAUnyHP3R2mW4O7j0dOmVYEUpKHGHqV7oeWBBc56fhcretNU9%2BNeTBlB30Q8tOUJa8p5YdEltdGddUZ8hP7OBIP7kcqQrueez4NrvZZVhoVakNnXB%2BeBxKVRzu%2Bc4aj6RYGqLuTgAoHTF77ceLsfW4oKacZJWJoOciL%2FC1mAjMRr6n8ECeg0n%2BGuVzgh1cjj0jULe1zVi1wR1cR0mU7Cmbvkp9lJ9PYLPAuus96noPthVyXYZn3OiXRGnJzTFhdZpzIWFqLPR52hBVqUy5xSlIllPS8yo9lvwuv2bLuwJBtA1E16ejuzNChuipgvmSdYTjXvog1zeM%2FahYyRw1LAbg6ZG%2FwU7YYX1FCz9MCgsPrOe6lzl9BkH47zT%2FM%2B4UWW%2BCSm8Iq8c%2BtyRhCbp5eGi8LxptzZAEvvIkrQ3NiEDfY2PuCMhhEHyW5%2FpH5BcQPPW5uyieLZfDm54McKM7SFAU4xISdlfQwxaXozQY6pgHZPp8I%2FgGz0Za7ORase1z0prqS63E172TmebER9gO5qN%2BNj2DBSSFAOAB%2F1Oko%2FB39YI%2BEhK0POBM9jHZ%2BadmbFXtCbVWWHTkfHIvOL3FHPDbNqxSICJ8oGuk9BOHtrWKNYp%2B9r7tUteL3EwQVxnL%2F2PhCzKNaO2hP5T3%2BEkbjd6q50rpeSZ7aIiGD%2BDPGvEkcSAIr%2Fd2vc2Dhg3xJlRFuaETGuite&X-Amz-Signature=3fb18f73cf111b5b3eb649397019ae67932d8e5d27b275577d32675aa28d6bfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XI64BEC%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIFwgX%2B%2F8BHa50c2gWvygCkCfkONK%2FmpCfhm%2FVsBOLybWAiA8HpvjkQKSBNTD2s27AEQaTmCutO8ybvyWOOWzM7%2FT5SqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU4hiO%2F2urAsIFWl9KtwDbAE4nRS%2FS7wWgRxPJO%2FfBlXOuiLImDpVIfF0YYQe5s1z6pbSauzVB00E6hyCfsoxS16V1qXIiguvZy8V76jPa7HoqkmnFYInSMFlrt7fSVz%2Bffz1BZCBHzT1cKjeMM6BNqCZApjPUOCp9T4v5iVBPYD91Zua3CAUnyHP3R2mW4O7j0dOmVYEUpKHGHqV7oeWBBc56fhcretNU9%2BNeTBlB30Q8tOUJa8p5YdEltdGddUZ8hP7OBIP7kcqQrueez4NrvZZVhoVakNnXB%2BeBxKVRzu%2Bc4aj6RYGqLuTgAoHTF77ceLsfW4oKacZJWJoOciL%2FC1mAjMRr6n8ECeg0n%2BGuVzgh1cjj0jULe1zVi1wR1cR0mU7Cmbvkp9lJ9PYLPAuus96noPthVyXYZn3OiXRGnJzTFhdZpzIWFqLPR52hBVqUy5xSlIllPS8yo9lvwuv2bLuwJBtA1E16ejuzNChuipgvmSdYTjXvog1zeM%2FahYyRw1LAbg6ZG%2FwU7YYX1FCz9MCgsPrOe6lzl9BkH47zT%2FM%2B4UWW%2BCSm8Iq8c%2BtyRhCbp5eGi8LxptzZAEvvIkrQ3NiEDfY2PuCMhhEHyW5%2FpH5BcQPPW5uyieLZfDm54McKM7SFAU4xISdlfQwxaXozQY6pgHZPp8I%2FgGz0Za7ORase1z0prqS63E172TmebER9gO5qN%2BNj2DBSSFAOAB%2F1Oko%2FB39YI%2BEhK0POBM9jHZ%2BadmbFXtCbVWWHTkfHIvOL3FHPDbNqxSICJ8oGuk9BOHtrWKNYp%2B9r7tUteL3EwQVxnL%2F2PhCzKNaO2hP5T3%2BEkbjd6q50rpeSZ7aIiGD%2BDPGvEkcSAIr%2Fd2vc2Dhg3xJlRFuaETGuite&X-Amz-Signature=1ebea873fb7b2bce341944e0ef74718e5280014225bd416dee61913831c91097&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XI64BEC%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIFwgX%2B%2F8BHa50c2gWvygCkCfkONK%2FmpCfhm%2FVsBOLybWAiA8HpvjkQKSBNTD2s27AEQaTmCutO8ybvyWOOWzM7%2FT5SqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMU4hiO%2F2urAsIFWl9KtwDbAE4nRS%2FS7wWgRxPJO%2FfBlXOuiLImDpVIfF0YYQe5s1z6pbSauzVB00E6hyCfsoxS16V1qXIiguvZy8V76jPa7HoqkmnFYInSMFlrt7fSVz%2Bffz1BZCBHzT1cKjeMM6BNqCZApjPUOCp9T4v5iVBPYD91Zua3CAUnyHP3R2mW4O7j0dOmVYEUpKHGHqV7oeWBBc56fhcretNU9%2BNeTBlB30Q8tOUJa8p5YdEltdGddUZ8hP7OBIP7kcqQrueez4NrvZZVhoVakNnXB%2BeBxKVRzu%2Bc4aj6RYGqLuTgAoHTF77ceLsfW4oKacZJWJoOciL%2FC1mAjMRr6n8ECeg0n%2BGuVzgh1cjj0jULe1zVi1wR1cR0mU7Cmbvkp9lJ9PYLPAuus96noPthVyXYZn3OiXRGnJzTFhdZpzIWFqLPR52hBVqUy5xSlIllPS8yo9lvwuv2bLuwJBtA1E16ejuzNChuipgvmSdYTjXvog1zeM%2FahYyRw1LAbg6ZG%2FwU7YYX1FCz9MCgsPrOe6lzl9BkH47zT%2FM%2B4UWW%2BCSm8Iq8c%2BtyRhCbp5eGi8LxptzZAEvvIkrQ3NiEDfY2PuCMhhEHyW5%2FpH5BcQPPW5uyieLZfDm54McKM7SFAU4xISdlfQwxaXozQY6pgHZPp8I%2FgGz0Za7ORase1z0prqS63E172TmebER9gO5qN%2BNj2DBSSFAOAB%2F1Oko%2FB39YI%2BEhK0POBM9jHZ%2BadmbFXtCbVWWHTkfHIvOL3FHPDbNqxSICJ8oGuk9BOHtrWKNYp%2B9r7tUteL3EwQVxnL%2F2PhCzKNaO2hP5T3%2BEkbjd6q50rpeSZ7aIiGD%2BDPGvEkcSAIr%2Fd2vc2Dhg3xJlRFuaETGuite&X-Amz-Signature=528a8b66de42efcd8450eefee48403dbebefa7696b39a2130e5b4344ee4a4dbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



