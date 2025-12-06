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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYYQD7ZO%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICytjYtB0vcA5gb87fRrqt08wurJ9Jrimslc7NyQGGFoAiBOGOEJs7lPq27TpGi6cg1eypSFF9q0l3MMsqeWdP1UgCr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMDz7GLJhNF09EFfZQKtwDnrAElmzY6%2FCXziX7I984nIjoEYvJJLaum7BBWM7M9o%2BoHPr0gi%2FRurp1j6FT1eAivhPvqLmRxPRZCg4iegRLATWCQoYdSLOwkXxPx0mbPLej2adnxQRLqLZkpMAHMwnH5EfKyRM%2B3O52AKZk4Th6uvr%2BDH9DrT6DeqqgWzyRTKkM0SbuHDb9KDBrsphaD8%2FKrF2JExRgZTuNDajsfzFOluYda6n%2BO0A8EVdF9zkTEycwXX7rtgEjpGr%2FCd7IyuiU6s7uH3hEcO6PJkTyA0Da1YlIgJjA4bvu6IrjK4aTRjG0AtrysvGZNcD7Id1UrjBevrO4LeBz4Ir7wBbcSqfqsRzXR5GJrq9vaXhqwYFtcvw0GD38xSwSSaFEBVMwYC%2B4B%2F7EsXXN1cV7biuBSXkNiG5dPcLIhIF16L8WTDKdXFnuYwViCGDbeFIeO2JftI5vbNAvEjE0Oz4xu1fnkcOtNyCBSK%2BdseNc97cgVanGwfIPslX0XiHx5ie6MXP22Nd8LqzBS7tYMGMAGQwd%2Flst6IS%2BLaD9usoP3xqLLyrtYwRJweOxNviNNu%2Bp8ZXYJzx%2BDYkeshx25wI7ZF6KbMFIKHv%2Fm2qRJEgUeQnzNRQ3FJ3AJ1BwWHiAYa3V8QgwrKfOyQY6pgHJLxarbeWT5Mjv6mzuDXgme8tg%2B0AP4%2FY6qRDd2iEnA8m7wI%2BxWQdaV%2BgRD7T6EPEw7Z0PaI0UkIF35mHzS2zYQVoYFPAufSUZtK8M4bZ7wRYjxNEKeDHNyx2srUOKAtLri8bBCbiElFXQJWSdZXtUAdhOsTNSm3bkxWR9cmmmW6xrycudiP2dIQaYIobM4FLM4oKPtWYz9Cc72VAYRioO%2Fuc06I9q&X-Amz-Signature=baddc229db866fae07f23ef0b2f1ecb904cd4a85bae0f62cf8d3722059826f2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYYQD7ZO%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICytjYtB0vcA5gb87fRrqt08wurJ9Jrimslc7NyQGGFoAiBOGOEJs7lPq27TpGi6cg1eypSFF9q0l3MMsqeWdP1UgCr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMDz7GLJhNF09EFfZQKtwDnrAElmzY6%2FCXziX7I984nIjoEYvJJLaum7BBWM7M9o%2BoHPr0gi%2FRurp1j6FT1eAivhPvqLmRxPRZCg4iegRLATWCQoYdSLOwkXxPx0mbPLej2adnxQRLqLZkpMAHMwnH5EfKyRM%2B3O52AKZk4Th6uvr%2BDH9DrT6DeqqgWzyRTKkM0SbuHDb9KDBrsphaD8%2FKrF2JExRgZTuNDajsfzFOluYda6n%2BO0A8EVdF9zkTEycwXX7rtgEjpGr%2FCd7IyuiU6s7uH3hEcO6PJkTyA0Da1YlIgJjA4bvu6IrjK4aTRjG0AtrysvGZNcD7Id1UrjBevrO4LeBz4Ir7wBbcSqfqsRzXR5GJrq9vaXhqwYFtcvw0GD38xSwSSaFEBVMwYC%2B4B%2F7EsXXN1cV7biuBSXkNiG5dPcLIhIF16L8WTDKdXFnuYwViCGDbeFIeO2JftI5vbNAvEjE0Oz4xu1fnkcOtNyCBSK%2BdseNc97cgVanGwfIPslX0XiHx5ie6MXP22Nd8LqzBS7tYMGMAGQwd%2Flst6IS%2BLaD9usoP3xqLLyrtYwRJweOxNviNNu%2Bp8ZXYJzx%2BDYkeshx25wI7ZF6KbMFIKHv%2Fm2qRJEgUeQnzNRQ3FJ3AJ1BwWHiAYa3V8QgwrKfOyQY6pgHJLxarbeWT5Mjv6mzuDXgme8tg%2B0AP4%2FY6qRDd2iEnA8m7wI%2BxWQdaV%2BgRD7T6EPEw7Z0PaI0UkIF35mHzS2zYQVoYFPAufSUZtK8M4bZ7wRYjxNEKeDHNyx2srUOKAtLri8bBCbiElFXQJWSdZXtUAdhOsTNSm3bkxWR9cmmmW6xrycudiP2dIQaYIobM4FLM4oKPtWYz9Cc72VAYRioO%2Fuc06I9q&X-Amz-Signature=a77e5fbac714ef1728b9b67a27ae149d58140411fa2e6b70e5387b5502b20691&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYYQD7ZO%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICytjYtB0vcA5gb87fRrqt08wurJ9Jrimslc7NyQGGFoAiBOGOEJs7lPq27TpGi6cg1eypSFF9q0l3MMsqeWdP1UgCr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMDz7GLJhNF09EFfZQKtwDnrAElmzY6%2FCXziX7I984nIjoEYvJJLaum7BBWM7M9o%2BoHPr0gi%2FRurp1j6FT1eAivhPvqLmRxPRZCg4iegRLATWCQoYdSLOwkXxPx0mbPLej2adnxQRLqLZkpMAHMwnH5EfKyRM%2B3O52AKZk4Th6uvr%2BDH9DrT6DeqqgWzyRTKkM0SbuHDb9KDBrsphaD8%2FKrF2JExRgZTuNDajsfzFOluYda6n%2BO0A8EVdF9zkTEycwXX7rtgEjpGr%2FCd7IyuiU6s7uH3hEcO6PJkTyA0Da1YlIgJjA4bvu6IrjK4aTRjG0AtrysvGZNcD7Id1UrjBevrO4LeBz4Ir7wBbcSqfqsRzXR5GJrq9vaXhqwYFtcvw0GD38xSwSSaFEBVMwYC%2B4B%2F7EsXXN1cV7biuBSXkNiG5dPcLIhIF16L8WTDKdXFnuYwViCGDbeFIeO2JftI5vbNAvEjE0Oz4xu1fnkcOtNyCBSK%2BdseNc97cgVanGwfIPslX0XiHx5ie6MXP22Nd8LqzBS7tYMGMAGQwd%2Flst6IS%2BLaD9usoP3xqLLyrtYwRJweOxNviNNu%2Bp8ZXYJzx%2BDYkeshx25wI7ZF6KbMFIKHv%2Fm2qRJEgUeQnzNRQ3FJ3AJ1BwWHiAYa3V8QgwrKfOyQY6pgHJLxarbeWT5Mjv6mzuDXgme8tg%2B0AP4%2FY6qRDd2iEnA8m7wI%2BxWQdaV%2BgRD7T6EPEw7Z0PaI0UkIF35mHzS2zYQVoYFPAufSUZtK8M4bZ7wRYjxNEKeDHNyx2srUOKAtLri8bBCbiElFXQJWSdZXtUAdhOsTNSm3bkxWR9cmmmW6xrycudiP2dIQaYIobM4FLM4oKPtWYz9Cc72VAYRioO%2Fuc06I9q&X-Amz-Signature=90671efee674aebc4c3ce5fe14ac5c9015c8cfa746acf8bfb06db265a2dd8ccb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYYQD7ZO%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICytjYtB0vcA5gb87fRrqt08wurJ9Jrimslc7NyQGGFoAiBOGOEJs7lPq27TpGi6cg1eypSFF9q0l3MMsqeWdP1UgCr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMDz7GLJhNF09EFfZQKtwDnrAElmzY6%2FCXziX7I984nIjoEYvJJLaum7BBWM7M9o%2BoHPr0gi%2FRurp1j6FT1eAivhPvqLmRxPRZCg4iegRLATWCQoYdSLOwkXxPx0mbPLej2adnxQRLqLZkpMAHMwnH5EfKyRM%2B3O52AKZk4Th6uvr%2BDH9DrT6DeqqgWzyRTKkM0SbuHDb9KDBrsphaD8%2FKrF2JExRgZTuNDajsfzFOluYda6n%2BO0A8EVdF9zkTEycwXX7rtgEjpGr%2FCd7IyuiU6s7uH3hEcO6PJkTyA0Da1YlIgJjA4bvu6IrjK4aTRjG0AtrysvGZNcD7Id1UrjBevrO4LeBz4Ir7wBbcSqfqsRzXR5GJrq9vaXhqwYFtcvw0GD38xSwSSaFEBVMwYC%2B4B%2F7EsXXN1cV7biuBSXkNiG5dPcLIhIF16L8WTDKdXFnuYwViCGDbeFIeO2JftI5vbNAvEjE0Oz4xu1fnkcOtNyCBSK%2BdseNc97cgVanGwfIPslX0XiHx5ie6MXP22Nd8LqzBS7tYMGMAGQwd%2Flst6IS%2BLaD9usoP3xqLLyrtYwRJweOxNviNNu%2Bp8ZXYJzx%2BDYkeshx25wI7ZF6KbMFIKHv%2Fm2qRJEgUeQnzNRQ3FJ3AJ1BwWHiAYa3V8QgwrKfOyQY6pgHJLxarbeWT5Mjv6mzuDXgme8tg%2B0AP4%2FY6qRDd2iEnA8m7wI%2BxWQdaV%2BgRD7T6EPEw7Z0PaI0UkIF35mHzS2zYQVoYFPAufSUZtK8M4bZ7wRYjxNEKeDHNyx2srUOKAtLri8bBCbiElFXQJWSdZXtUAdhOsTNSm3bkxWR9cmmmW6xrycudiP2dIQaYIobM4FLM4oKPtWYz9Cc72VAYRioO%2Fuc06I9q&X-Amz-Signature=c391c04d21b4652cb723cfb2ef553331c84f774c7f7f68ab698d243725161458&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



