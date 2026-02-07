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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDV7CHOX%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAZRev9YPgsfu9eipcxTpiXo7nvC%2Fx0rYx6g4dQsJNXQIhAKR%2BEjICAcyRr9PU10jLuvbHClz5bLab1Xi9XKJmgKHpKv8DCFQQABoMNjM3NDIzMTgzODA1IgyW7Ez3Hu64jZZNAEsq3APl9%2FIa72w5bRsIdfAUhdeka9lOCZVDEGD%2FxYDEOn6LDR39svh7i0seY31qv6G1fqeTUwslx3nnjwU6c4kWjfbnMbfssQ5EffCVDEFS0ltb9cWP5qIE%2BUb%2FFYw9rTbHmbMueBsRzN81C6MvXjghiPRAoeLSk0rrAVRn9BB8fBrKTXSiNNKZcgv%2FZrygIpo7mbfyttbRkSQp56UGLO3iBkTTqoGU28VG7NrvHJ3IYfzdy7odWFLcnOl5R0CtENoM%2FZhQoPvzyPu1sTogA68%2FAu%2F%2BqCLjcnhtGlL9MgK95%2FuD22cxyotGfd3%2BzpALXwHJQvuY0IuoAQAy%2BxUrJqaBIV4%2Fj%2Bz%2FcxlVQz%2F6R%2Br8Shuj4upMRTypGB07xNDBs2ywr%2BozpGGdi%2BvLklHMfqcQDS0uv4VyKtuRTxTfG8XhueXwTdDF8FFmM71ud7wLkBPsM0IZFo2W%2FMTXTX8qxqcYBbxdySxwQEYObE8jUV0b%2BorKAZWEJOjpCYGalpmPn0lU8ZUQAXEohQZ9mJUqmcMJ9LKHqpx%2FAo7l2kI2g5GD0WC66th3pKog0%2BDnxmUXzgXS4XKAU7O49Ay3Lrz9A7uUoacZm7vDGHFVvDOl29yKs6gz3%2FT2KxluW96fOU9H7TCNxZrMBjqkAX3VRzRfIggJHPL9Q4CxED3VsR1lVg8aJdxeOIAjKlztMzaBGPHXGZyWnOkyhTTTGpC821VEqhBF1rIaeTZ6K05kZaAzSvMIlpaiNb1DWv0kLCVlLmHl%2Bs2StCR9RYnJ0J1Y3NFaRjXmfc8u2VoELqWTfgfR%2FXbpW9D59VgOzIirl5gbz2f8m2S5AWwUAiAkmCDnhRvGJ0stkS4VLOP2H5GDk8SX&X-Amz-Signature=a37afcaceffd0bec61483918cdd8dcef5fd4798f79054ee09b9669f4891d9a43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDV7CHOX%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAZRev9YPgsfu9eipcxTpiXo7nvC%2Fx0rYx6g4dQsJNXQIhAKR%2BEjICAcyRr9PU10jLuvbHClz5bLab1Xi9XKJmgKHpKv8DCFQQABoMNjM3NDIzMTgzODA1IgyW7Ez3Hu64jZZNAEsq3APl9%2FIa72w5bRsIdfAUhdeka9lOCZVDEGD%2FxYDEOn6LDR39svh7i0seY31qv6G1fqeTUwslx3nnjwU6c4kWjfbnMbfssQ5EffCVDEFS0ltb9cWP5qIE%2BUb%2FFYw9rTbHmbMueBsRzN81C6MvXjghiPRAoeLSk0rrAVRn9BB8fBrKTXSiNNKZcgv%2FZrygIpo7mbfyttbRkSQp56UGLO3iBkTTqoGU28VG7NrvHJ3IYfzdy7odWFLcnOl5R0CtENoM%2FZhQoPvzyPu1sTogA68%2FAu%2F%2BqCLjcnhtGlL9MgK95%2FuD22cxyotGfd3%2BzpALXwHJQvuY0IuoAQAy%2BxUrJqaBIV4%2Fj%2Bz%2FcxlVQz%2F6R%2Br8Shuj4upMRTypGB07xNDBs2ywr%2BozpGGdi%2BvLklHMfqcQDS0uv4VyKtuRTxTfG8XhueXwTdDF8FFmM71ud7wLkBPsM0IZFo2W%2FMTXTX8qxqcYBbxdySxwQEYObE8jUV0b%2BorKAZWEJOjpCYGalpmPn0lU8ZUQAXEohQZ9mJUqmcMJ9LKHqpx%2FAo7l2kI2g5GD0WC66th3pKog0%2BDnxmUXzgXS4XKAU7O49Ay3Lrz9A7uUoacZm7vDGHFVvDOl29yKs6gz3%2FT2KxluW96fOU9H7TCNxZrMBjqkAX3VRzRfIggJHPL9Q4CxED3VsR1lVg8aJdxeOIAjKlztMzaBGPHXGZyWnOkyhTTTGpC821VEqhBF1rIaeTZ6K05kZaAzSvMIlpaiNb1DWv0kLCVlLmHl%2Bs2StCR9RYnJ0J1Y3NFaRjXmfc8u2VoELqWTfgfR%2FXbpW9D59VgOzIirl5gbz2f8m2S5AWwUAiAkmCDnhRvGJ0stkS4VLOP2H5GDk8SX&X-Amz-Signature=1b50729d616a66098ea4307087a54be55ea8e0dce1bbecdc3790c7528e1ac0b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDV7CHOX%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAZRev9YPgsfu9eipcxTpiXo7nvC%2Fx0rYx6g4dQsJNXQIhAKR%2BEjICAcyRr9PU10jLuvbHClz5bLab1Xi9XKJmgKHpKv8DCFQQABoMNjM3NDIzMTgzODA1IgyW7Ez3Hu64jZZNAEsq3APl9%2FIa72w5bRsIdfAUhdeka9lOCZVDEGD%2FxYDEOn6LDR39svh7i0seY31qv6G1fqeTUwslx3nnjwU6c4kWjfbnMbfssQ5EffCVDEFS0ltb9cWP5qIE%2BUb%2FFYw9rTbHmbMueBsRzN81C6MvXjghiPRAoeLSk0rrAVRn9BB8fBrKTXSiNNKZcgv%2FZrygIpo7mbfyttbRkSQp56UGLO3iBkTTqoGU28VG7NrvHJ3IYfzdy7odWFLcnOl5R0CtENoM%2FZhQoPvzyPu1sTogA68%2FAu%2F%2BqCLjcnhtGlL9MgK95%2FuD22cxyotGfd3%2BzpALXwHJQvuY0IuoAQAy%2BxUrJqaBIV4%2Fj%2Bz%2FcxlVQz%2F6R%2Br8Shuj4upMRTypGB07xNDBs2ywr%2BozpGGdi%2BvLklHMfqcQDS0uv4VyKtuRTxTfG8XhueXwTdDF8FFmM71ud7wLkBPsM0IZFo2W%2FMTXTX8qxqcYBbxdySxwQEYObE8jUV0b%2BorKAZWEJOjpCYGalpmPn0lU8ZUQAXEohQZ9mJUqmcMJ9LKHqpx%2FAo7l2kI2g5GD0WC66th3pKog0%2BDnxmUXzgXS4XKAU7O49Ay3Lrz9A7uUoacZm7vDGHFVvDOl29yKs6gz3%2FT2KxluW96fOU9H7TCNxZrMBjqkAX3VRzRfIggJHPL9Q4CxED3VsR1lVg8aJdxeOIAjKlztMzaBGPHXGZyWnOkyhTTTGpC821VEqhBF1rIaeTZ6K05kZaAzSvMIlpaiNb1DWv0kLCVlLmHl%2Bs2StCR9RYnJ0J1Y3NFaRjXmfc8u2VoELqWTfgfR%2FXbpW9D59VgOzIirl5gbz2f8m2S5AWwUAiAkmCDnhRvGJ0stkS4VLOP2H5GDk8SX&X-Amz-Signature=ad751e9485b5ea58d742e1c5decbe62b7d315fba3bc6ddd7e955e4d55c7b20b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDV7CHOX%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCAZRev9YPgsfu9eipcxTpiXo7nvC%2Fx0rYx6g4dQsJNXQIhAKR%2BEjICAcyRr9PU10jLuvbHClz5bLab1Xi9XKJmgKHpKv8DCFQQABoMNjM3NDIzMTgzODA1IgyW7Ez3Hu64jZZNAEsq3APl9%2FIa72w5bRsIdfAUhdeka9lOCZVDEGD%2FxYDEOn6LDR39svh7i0seY31qv6G1fqeTUwslx3nnjwU6c4kWjfbnMbfssQ5EffCVDEFS0ltb9cWP5qIE%2BUb%2FFYw9rTbHmbMueBsRzN81C6MvXjghiPRAoeLSk0rrAVRn9BB8fBrKTXSiNNKZcgv%2FZrygIpo7mbfyttbRkSQp56UGLO3iBkTTqoGU28VG7NrvHJ3IYfzdy7odWFLcnOl5R0CtENoM%2FZhQoPvzyPu1sTogA68%2FAu%2F%2BqCLjcnhtGlL9MgK95%2FuD22cxyotGfd3%2BzpALXwHJQvuY0IuoAQAy%2BxUrJqaBIV4%2Fj%2Bz%2FcxlVQz%2F6R%2Br8Shuj4upMRTypGB07xNDBs2ywr%2BozpGGdi%2BvLklHMfqcQDS0uv4VyKtuRTxTfG8XhueXwTdDF8FFmM71ud7wLkBPsM0IZFo2W%2FMTXTX8qxqcYBbxdySxwQEYObE8jUV0b%2BorKAZWEJOjpCYGalpmPn0lU8ZUQAXEohQZ9mJUqmcMJ9LKHqpx%2FAo7l2kI2g5GD0WC66th3pKog0%2BDnxmUXzgXS4XKAU7O49Ay3Lrz9A7uUoacZm7vDGHFVvDOl29yKs6gz3%2FT2KxluW96fOU9H7TCNxZrMBjqkAX3VRzRfIggJHPL9Q4CxED3VsR1lVg8aJdxeOIAjKlztMzaBGPHXGZyWnOkyhTTTGpC821VEqhBF1rIaeTZ6K05kZaAzSvMIlpaiNb1DWv0kLCVlLmHl%2Bs2StCR9RYnJ0J1Y3NFaRjXmfc8u2VoELqWTfgfR%2FXbpW9D59VgOzIirl5gbz2f8m2S5AWwUAiAkmCDnhRvGJ0stkS4VLOP2H5GDk8SX&X-Amz-Signature=fde3a8e8d7dce49a51887fc7f6d8125e69b33e8c3e1f426acce8da76a81651a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



