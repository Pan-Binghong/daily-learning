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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H7JZYJD%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI84Bej2eUB7FZTvh7KxJrAmcW1V7hbYRpZStLVxqshAiAanEO7z25jpblIe%2BwzUwhMxUkMqqKtp8Qm3tJOyC3VzSr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIM3FAgDxicE9qh7NyYKtwDYtuf8yB88nJ6A9R6bZJ%2FXl8U4gJhaJMfFYplimGV%2B%2B%2BOa3yew%2BHngfm%2F%2FQBnggtrZ3tGFoIa67Ev7JOAXjG9%2FPku80vJoZWLX4w%2Bh14m6Ejz32KTbRThWojN4Q4qWJxOptAo7nKy9yirOl6h9fX3wsrXMh3uUOTHDrGPNYwD5XdPNs%2F5MMKDwA%2FrZLrkbQ%2F6NoX5I%2FRzPMQNucmLFaibPX%2F8rdFb0ZQDw4Qvv3xFxAJlZFs8oTEHC2%2F81OtYyTzcnT%2BnKNow%2FhSWXRF9gjPQGHs4VXcHriu0hqvH9hoJPvD1mtk%2BDKsCzlJemEIaHaGZd0B4mJkN15qsWg6iSPjZMkzQ3JHUJZ9QFOYtM9kJ8PzLJreZDrRUDPJ6flk3z%2B1Th0ZtZEZeppt7JVboN5f0mRAkHBmUpvKB397W33cQcK%2BhEesQMTNkNhdqn1iviHyJ03CY4ao7fXnE0ewLPRU%2FYUhyzp6dvnFgGOGU6X3anV1Rc4pXQihNvJUmzUmmcpqV%2Br%2BeCNYSXertBDcAkjK0MVOYVbEYVzJEPuGxVG4iGOjcatuwkusKD0baHW9Gbmx6WzWVHqqanLZD8KzZnWJ%2B10mNcQVU184U%2BoRWlMaoFRC1PLr55qhbGbePiIcw%2BIvIyQY6pgGgvcOA2PIw4prby0uKjZWXrPrltydVErUAiNhtACKS%2BYlDRCpQSl3z6gSv8lTF0cj5tu%2F%2FNcFfwe411Ui2L%2BfA9uLUUQh9Zh6s5JETqtzlU%2BRMOgMOQmxpYPhpxcMgIVvzO3oNw1u6h%2BKK3UXvLeabFno0XRKfZGSCWIl%2BtnTIzArgWOROdp0KWUITZa4N7X%2Bhe1q7GhHv2hXIV4ogpqMmUCpZI0P2&X-Amz-Signature=9ddc083e08c003f6580900fe772acafff5e2bda59fe90951e68625f6e8bf979b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H7JZYJD%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI84Bej2eUB7FZTvh7KxJrAmcW1V7hbYRpZStLVxqshAiAanEO7z25jpblIe%2BwzUwhMxUkMqqKtp8Qm3tJOyC3VzSr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIM3FAgDxicE9qh7NyYKtwDYtuf8yB88nJ6A9R6bZJ%2FXl8U4gJhaJMfFYplimGV%2B%2B%2BOa3yew%2BHngfm%2F%2FQBnggtrZ3tGFoIa67Ev7JOAXjG9%2FPku80vJoZWLX4w%2Bh14m6Ejz32KTbRThWojN4Q4qWJxOptAo7nKy9yirOl6h9fX3wsrXMh3uUOTHDrGPNYwD5XdPNs%2F5MMKDwA%2FrZLrkbQ%2F6NoX5I%2FRzPMQNucmLFaibPX%2F8rdFb0ZQDw4Qvv3xFxAJlZFs8oTEHC2%2F81OtYyTzcnT%2BnKNow%2FhSWXRF9gjPQGHs4VXcHriu0hqvH9hoJPvD1mtk%2BDKsCzlJemEIaHaGZd0B4mJkN15qsWg6iSPjZMkzQ3JHUJZ9QFOYtM9kJ8PzLJreZDrRUDPJ6flk3z%2B1Th0ZtZEZeppt7JVboN5f0mRAkHBmUpvKB397W33cQcK%2BhEesQMTNkNhdqn1iviHyJ03CY4ao7fXnE0ewLPRU%2FYUhyzp6dvnFgGOGU6X3anV1Rc4pXQihNvJUmzUmmcpqV%2Br%2BeCNYSXertBDcAkjK0MVOYVbEYVzJEPuGxVG4iGOjcatuwkusKD0baHW9Gbmx6WzWVHqqanLZD8KzZnWJ%2B10mNcQVU184U%2BoRWlMaoFRC1PLr55qhbGbePiIcw%2BIvIyQY6pgGgvcOA2PIw4prby0uKjZWXrPrltydVErUAiNhtACKS%2BYlDRCpQSl3z6gSv8lTF0cj5tu%2F%2FNcFfwe411Ui2L%2BfA9uLUUQh9Zh6s5JETqtzlU%2BRMOgMOQmxpYPhpxcMgIVvzO3oNw1u6h%2BKK3UXvLeabFno0XRKfZGSCWIl%2BtnTIzArgWOROdp0KWUITZa4N7X%2Bhe1q7GhHv2hXIV4ogpqMmUCpZI0P2&X-Amz-Signature=38bca13a82172a667a0ba21faaaec1c59b24c556f0c639f7ad0994c55d01f9eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H7JZYJD%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI84Bej2eUB7FZTvh7KxJrAmcW1V7hbYRpZStLVxqshAiAanEO7z25jpblIe%2BwzUwhMxUkMqqKtp8Qm3tJOyC3VzSr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIM3FAgDxicE9qh7NyYKtwDYtuf8yB88nJ6A9R6bZJ%2FXl8U4gJhaJMfFYplimGV%2B%2B%2BOa3yew%2BHngfm%2F%2FQBnggtrZ3tGFoIa67Ev7JOAXjG9%2FPku80vJoZWLX4w%2Bh14m6Ejz32KTbRThWojN4Q4qWJxOptAo7nKy9yirOl6h9fX3wsrXMh3uUOTHDrGPNYwD5XdPNs%2F5MMKDwA%2FrZLrkbQ%2F6NoX5I%2FRzPMQNucmLFaibPX%2F8rdFb0ZQDw4Qvv3xFxAJlZFs8oTEHC2%2F81OtYyTzcnT%2BnKNow%2FhSWXRF9gjPQGHs4VXcHriu0hqvH9hoJPvD1mtk%2BDKsCzlJemEIaHaGZd0B4mJkN15qsWg6iSPjZMkzQ3JHUJZ9QFOYtM9kJ8PzLJreZDrRUDPJ6flk3z%2B1Th0ZtZEZeppt7JVboN5f0mRAkHBmUpvKB397W33cQcK%2BhEesQMTNkNhdqn1iviHyJ03CY4ao7fXnE0ewLPRU%2FYUhyzp6dvnFgGOGU6X3anV1Rc4pXQihNvJUmzUmmcpqV%2Br%2BeCNYSXertBDcAkjK0MVOYVbEYVzJEPuGxVG4iGOjcatuwkusKD0baHW9Gbmx6WzWVHqqanLZD8KzZnWJ%2B10mNcQVU184U%2BoRWlMaoFRC1PLr55qhbGbePiIcw%2BIvIyQY6pgGgvcOA2PIw4prby0uKjZWXrPrltydVErUAiNhtACKS%2BYlDRCpQSl3z6gSv8lTF0cj5tu%2F%2FNcFfwe411Ui2L%2BfA9uLUUQh9Zh6s5JETqtzlU%2BRMOgMOQmxpYPhpxcMgIVvzO3oNw1u6h%2BKK3UXvLeabFno0XRKfZGSCWIl%2BtnTIzArgWOROdp0KWUITZa4N7X%2Bhe1q7GhHv2hXIV4ogpqMmUCpZI0P2&X-Amz-Signature=5b692f4e7217423619e55a33c90d13b3267f353127025918c00ebb400b2aae44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H7JZYJD%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDI84Bej2eUB7FZTvh7KxJrAmcW1V7hbYRpZStLVxqshAiAanEO7z25jpblIe%2BwzUwhMxUkMqqKtp8Qm3tJOyC3VzSr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIM3FAgDxicE9qh7NyYKtwDYtuf8yB88nJ6A9R6bZJ%2FXl8U4gJhaJMfFYplimGV%2B%2B%2BOa3yew%2BHngfm%2F%2FQBnggtrZ3tGFoIa67Ev7JOAXjG9%2FPku80vJoZWLX4w%2Bh14m6Ejz32KTbRThWojN4Q4qWJxOptAo7nKy9yirOl6h9fX3wsrXMh3uUOTHDrGPNYwD5XdPNs%2F5MMKDwA%2FrZLrkbQ%2F6NoX5I%2FRzPMQNucmLFaibPX%2F8rdFb0ZQDw4Qvv3xFxAJlZFs8oTEHC2%2F81OtYyTzcnT%2BnKNow%2FhSWXRF9gjPQGHs4VXcHriu0hqvH9hoJPvD1mtk%2BDKsCzlJemEIaHaGZd0B4mJkN15qsWg6iSPjZMkzQ3JHUJZ9QFOYtM9kJ8PzLJreZDrRUDPJ6flk3z%2B1Th0ZtZEZeppt7JVboN5f0mRAkHBmUpvKB397W33cQcK%2BhEesQMTNkNhdqn1iviHyJ03CY4ao7fXnE0ewLPRU%2FYUhyzp6dvnFgGOGU6X3anV1Rc4pXQihNvJUmzUmmcpqV%2Br%2BeCNYSXertBDcAkjK0MVOYVbEYVzJEPuGxVG4iGOjcatuwkusKD0baHW9Gbmx6WzWVHqqanLZD8KzZnWJ%2B10mNcQVU184U%2BoRWlMaoFRC1PLr55qhbGbePiIcw%2BIvIyQY6pgGgvcOA2PIw4prby0uKjZWXrPrltydVErUAiNhtACKS%2BYlDRCpQSl3z6gSv8lTF0cj5tu%2F%2FNcFfwe411Ui2L%2BfA9uLUUQh9Zh6s5JETqtzlU%2BRMOgMOQmxpYPhpxcMgIVvzO3oNw1u6h%2BKK3UXvLeabFno0XRKfZGSCWIl%2BtnTIzArgWOROdp0KWUITZa4N7X%2Bhe1q7GhHv2hXIV4ogpqMmUCpZI0P2&X-Amz-Signature=d5945c76dacac798a793ae01a8abeccb4c84f16500e1ce6244235c60034c656b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



