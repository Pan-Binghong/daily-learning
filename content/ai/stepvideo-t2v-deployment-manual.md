---
title: Stepvideo-t2v Deployment Manual
date: '2025-04-22T00:43:00.000Z'
lastmod: '2025-04-23T02:58:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 记录部署阶跃星辰发布的stepvideo-ti2v (图片生成视频)模型，全流程。含踩坑记录，以及webui展示代码。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB7WH3HR%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA7GDMs5bPLmP3Ltiz%2BxH9KxcPfAmNhC0zhB%2F7aQV1RpAiBCVhuOpeBJYKIzTXrvaF%2FjkvgLkSIvTAuTWxdzplt%2FtyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe4rYyeZZAYjQX8MNKtwD4CJ2a6fh2uH%2Bb2cKiC%2F%2F0QuKj2SoQ0n6qVQjS186jdWvFAl6hOm9%2BWZxQedpTI0QLrQCsYAJSLPRcV%2FsaK6lgVRBsKyKDishq3SCQHRoVhlhpwxSfvwRqrEzzM%2FWmcAFftXsvQtIh17DRwH4gaWT64%2FQgc%2B9gUmyX6q8tULam9U%2BNhKAHrllEfqgMoyyiGh8hoiFNjdNCrkVxQ9FFIMOmzjtwFRwYOg3YtOJcYh7acbP9ci6dFRcVmulvUZwDif9Nst8P2lcgYWvv7reiMGdFif%2FcgtTcsrB1QN%2F49iKK7Oj6lSMCCGp0G0N%2FrCTtiNGYgLoej7fPi2FucIqtUxEpjTEzC3GdSQnRbAWfP2xUFisky2Q%2BaHqhnq7eHaSVjRSifC%2BYSGLXsAe5cgQzMth1lFJRWc7z3skHkqY8YtRQt%2BB6tIAelhh%2BACnyfdGQNBjW5wyrhdnnGrJh7r9mJug%2FEUPss9hq7xlzE%2F7DVN5XyFNEBLTG93uckZkACT03LNizwNoOP4kB34V1X6PpjsBJp5uiby8fmy6Df6GEx5t0TpPVqD6nHwkr336zZ%2BYtbOA0%2FBDO2ALKpVSjpqyo3pMUQ%2FxUV0UOgVb9OVc23GOEwUbH39TxcxBu2hDDsQwvKOsyAY6pgHV3xdv%2FvftxxJ4zRNKHejEjqHUNblLJslKPjegYFGMOFlqTx6Y8PZ1IpwIFRUL6d0%2FNDwxeh%2F2JwRzFslG9H8f%2BUa5PVxR1hDLvNx%2Bvv%2FQ%2FNPA4dMsUEzfMo%2B6B0G5TfVKBJUfP%2FwUL1F7P2FjW7%2FR5thihmXXGDg6TxCCWJNOxhI6eCCFjaI3OYGK4koyxV76bTRVmT8hBSWRi%2BQxkUhj5vsXC%2Buw&X-Amz-Signature=46213d071d944dfa577ff1225056af69fb0bacb160aa77b9077880fab963a87f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB7WH3HR%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA7GDMs5bPLmP3Ltiz%2BxH9KxcPfAmNhC0zhB%2F7aQV1RpAiBCVhuOpeBJYKIzTXrvaF%2FjkvgLkSIvTAuTWxdzplt%2FtyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe4rYyeZZAYjQX8MNKtwD4CJ2a6fh2uH%2Bb2cKiC%2F%2F0QuKj2SoQ0n6qVQjS186jdWvFAl6hOm9%2BWZxQedpTI0QLrQCsYAJSLPRcV%2FsaK6lgVRBsKyKDishq3SCQHRoVhlhpwxSfvwRqrEzzM%2FWmcAFftXsvQtIh17DRwH4gaWT64%2FQgc%2B9gUmyX6q8tULam9U%2BNhKAHrllEfqgMoyyiGh8hoiFNjdNCrkVxQ9FFIMOmzjtwFRwYOg3YtOJcYh7acbP9ci6dFRcVmulvUZwDif9Nst8P2lcgYWvv7reiMGdFif%2FcgtTcsrB1QN%2F49iKK7Oj6lSMCCGp0G0N%2FrCTtiNGYgLoej7fPi2FucIqtUxEpjTEzC3GdSQnRbAWfP2xUFisky2Q%2BaHqhnq7eHaSVjRSifC%2BYSGLXsAe5cgQzMth1lFJRWc7z3skHkqY8YtRQt%2BB6tIAelhh%2BACnyfdGQNBjW5wyrhdnnGrJh7r9mJug%2FEUPss9hq7xlzE%2F7DVN5XyFNEBLTG93uckZkACT03LNizwNoOP4kB34V1X6PpjsBJp5uiby8fmy6Df6GEx5t0TpPVqD6nHwkr336zZ%2BYtbOA0%2FBDO2ALKpVSjpqyo3pMUQ%2FxUV0UOgVb9OVc23GOEwUbH39TxcxBu2hDDsQwvKOsyAY6pgHV3xdv%2FvftxxJ4zRNKHejEjqHUNblLJslKPjegYFGMOFlqTx6Y8PZ1IpwIFRUL6d0%2FNDwxeh%2F2JwRzFslG9H8f%2BUa5PVxR1hDLvNx%2Bvv%2FQ%2FNPA4dMsUEzfMo%2B6B0G5TfVKBJUfP%2FwUL1F7P2FjW7%2FR5thihmXXGDg6TxCCWJNOxhI6eCCFjaI3OYGK4koyxV76bTRVmT8hBSWRi%2BQxkUhj5vsXC%2Buw&X-Amz-Signature=a4d8426433cc4f91a64496cb9dba1381699325355ac035e29fae954f85ce9694&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB7WH3HR%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA7GDMs5bPLmP3Ltiz%2BxH9KxcPfAmNhC0zhB%2F7aQV1RpAiBCVhuOpeBJYKIzTXrvaF%2FjkvgLkSIvTAuTWxdzplt%2FtyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe4rYyeZZAYjQX8MNKtwD4CJ2a6fh2uH%2Bb2cKiC%2F%2F0QuKj2SoQ0n6qVQjS186jdWvFAl6hOm9%2BWZxQedpTI0QLrQCsYAJSLPRcV%2FsaK6lgVRBsKyKDishq3SCQHRoVhlhpwxSfvwRqrEzzM%2FWmcAFftXsvQtIh17DRwH4gaWT64%2FQgc%2B9gUmyX6q8tULam9U%2BNhKAHrllEfqgMoyyiGh8hoiFNjdNCrkVxQ9FFIMOmzjtwFRwYOg3YtOJcYh7acbP9ci6dFRcVmulvUZwDif9Nst8P2lcgYWvv7reiMGdFif%2FcgtTcsrB1QN%2F49iKK7Oj6lSMCCGp0G0N%2FrCTtiNGYgLoej7fPi2FucIqtUxEpjTEzC3GdSQnRbAWfP2xUFisky2Q%2BaHqhnq7eHaSVjRSifC%2BYSGLXsAe5cgQzMth1lFJRWc7z3skHkqY8YtRQt%2BB6tIAelhh%2BACnyfdGQNBjW5wyrhdnnGrJh7r9mJug%2FEUPss9hq7xlzE%2F7DVN5XyFNEBLTG93uckZkACT03LNizwNoOP4kB34V1X6PpjsBJp5uiby8fmy6Df6GEx5t0TpPVqD6nHwkr336zZ%2BYtbOA0%2FBDO2ALKpVSjpqyo3pMUQ%2FxUV0UOgVb9OVc23GOEwUbH39TxcxBu2hDDsQwvKOsyAY6pgHV3xdv%2FvftxxJ4zRNKHejEjqHUNblLJslKPjegYFGMOFlqTx6Y8PZ1IpwIFRUL6d0%2FNDwxeh%2F2JwRzFslG9H8f%2BUa5PVxR1hDLvNx%2Bvv%2FQ%2FNPA4dMsUEzfMo%2B6B0G5TfVKBJUfP%2FwUL1F7P2FjW7%2FR5thihmXXGDg6TxCCWJNOxhI6eCCFjaI3OYGK4koyxV76bTRVmT8hBSWRi%2BQxkUhj5vsXC%2Buw&X-Amz-Signature=c7f40ab6f24ef1ec566a139da55fd4a5dc8e560c07cdb61a36e0be37b88383cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB7WH3HR%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA7GDMs5bPLmP3Ltiz%2BxH9KxcPfAmNhC0zhB%2F7aQV1RpAiBCVhuOpeBJYKIzTXrvaF%2FjkvgLkSIvTAuTWxdzplt%2FtyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe4rYyeZZAYjQX8MNKtwD4CJ2a6fh2uH%2Bb2cKiC%2F%2F0QuKj2SoQ0n6qVQjS186jdWvFAl6hOm9%2BWZxQedpTI0QLrQCsYAJSLPRcV%2FsaK6lgVRBsKyKDishq3SCQHRoVhlhpwxSfvwRqrEzzM%2FWmcAFftXsvQtIh17DRwH4gaWT64%2FQgc%2B9gUmyX6q8tULam9U%2BNhKAHrllEfqgMoyyiGh8hoiFNjdNCrkVxQ9FFIMOmzjtwFRwYOg3YtOJcYh7acbP9ci6dFRcVmulvUZwDif9Nst8P2lcgYWvv7reiMGdFif%2FcgtTcsrB1QN%2F49iKK7Oj6lSMCCGp0G0N%2FrCTtiNGYgLoej7fPi2FucIqtUxEpjTEzC3GdSQnRbAWfP2xUFisky2Q%2BaHqhnq7eHaSVjRSifC%2BYSGLXsAe5cgQzMth1lFJRWc7z3skHkqY8YtRQt%2BB6tIAelhh%2BACnyfdGQNBjW5wyrhdnnGrJh7r9mJug%2FEUPss9hq7xlzE%2F7DVN5XyFNEBLTG93uckZkACT03LNizwNoOP4kB34V1X6PpjsBJp5uiby8fmy6Df6GEx5t0TpPVqD6nHwkr336zZ%2BYtbOA0%2FBDO2ALKpVSjpqyo3pMUQ%2FxUV0UOgVb9OVc23GOEwUbH39TxcxBu2hDDsQwvKOsyAY6pgHV3xdv%2FvftxxJ4zRNKHejEjqHUNblLJslKPjegYFGMOFlqTx6Y8PZ1IpwIFRUL6d0%2FNDwxeh%2F2JwRzFslG9H8f%2BUa5PVxR1hDLvNx%2Bvv%2FQ%2FNPA4dMsUEzfMo%2B6B0G5TfVKBJUfP%2FwUL1F7P2FjW7%2FR5thihmXXGDg6TxCCWJNOxhI6eCCFjaI3OYGK4koyxV76bTRVmT8hBSWRi%2BQxkUhj5vsXC%2Buw&X-Amz-Signature=2d8c9e6cbc33d8c0a9f937f39f50fda1c1989bfe995f657f54ea4104921c2484&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



