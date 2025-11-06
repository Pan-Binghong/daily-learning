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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OIPQILU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2o3JpHh8yvruJcI7r8DorfguJE1S6aHJL4gYkDSVAYAIhAJLmo6pLE7URX2Gjd3Bp6H1dbRpHhf8RWrodq0zfUhk%2FKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzkIBjg3aNEpuDBAUsq3ANaAlBW9RsrqoBrGeiMLcM%2FWuQh92IWnc4RpQfp8x9aTIhNiWkwMWDEzqLkG2%2FsUI92OoOdVhf0HRiNfaqP50r%2FirNKHjDKZQMPe9R9kH%2FvyRoa0uQyluD1v9KIhxflsIaRSpD3JeT1QgMOKQ1swIAH0K7CQxm94joyi1kZIELggT38zZxj0N8nzfsqwdrT%2FFWXyPBhb3fZKOEj83LcJaa649nvH07xbckiAUFYCNqQ4z0YgQpHK26iaHNHpCkGMMBbXxk1jozUWK35rK37Zzw%2B0i0a2m6WDbHFL3ZlkI6RevcfOaUguuC9nQ%2F76zAPh%2BvWu2CaG6orPRW0TDiZFIn9D5aIQMC6yIHJZr4YJn2g%2Fyo1qkhykHEj2JEVJbWuhOXy28MwWivhFhLOD7HveKCRTRUS7Bg4YB%2BE%2Be6fx38ywkifmjp1xL3gUBfOOZh9%2F0u%2B12W9s4%2FHOsb6s893HDLUTGjxp05mDN690VPiFUEePN8xMsxZCUEFlQVv8Bd1BL39NSTGB%2Bk95e0khIk9dQagkL5SfBBpZPpnT4qzxToAYgWpJ0ot5gHv%2B8RRmQOqRDuGpbHRNKscfRUce4AUJMa5DW8CD3zGq7T7S4TUi7OWHH8lHgpQ0L78w3EEgzD78a%2FIBjqkARQ33m5F4B0zbNzlp9tMXEbAsj%2BBl3AQptOPwtrGxpJOnfW0kZplJT5upaIHg%2BZIQPvUcP255Em67Q%2BwC3BOcDigLy1iInKSg4ez3SAN9haU9mdt52PnYlPDo584xNaR3qPXXfuk0QP5wYPP8%2FvH%2F5HtHYHH902kfpYIzXmUlGfbTQV3iDBstljEmeiwIwzRRjsGeQHLzdBzFAhfzDcWvv5LD7eB&X-Amz-Signature=e6a7d471c51b6c093134244e6e9e0703b585d740e741ca044587366ef6b733c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OIPQILU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2o3JpHh8yvruJcI7r8DorfguJE1S6aHJL4gYkDSVAYAIhAJLmo6pLE7URX2Gjd3Bp6H1dbRpHhf8RWrodq0zfUhk%2FKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzkIBjg3aNEpuDBAUsq3ANaAlBW9RsrqoBrGeiMLcM%2FWuQh92IWnc4RpQfp8x9aTIhNiWkwMWDEzqLkG2%2FsUI92OoOdVhf0HRiNfaqP50r%2FirNKHjDKZQMPe9R9kH%2FvyRoa0uQyluD1v9KIhxflsIaRSpD3JeT1QgMOKQ1swIAH0K7CQxm94joyi1kZIELggT38zZxj0N8nzfsqwdrT%2FFWXyPBhb3fZKOEj83LcJaa649nvH07xbckiAUFYCNqQ4z0YgQpHK26iaHNHpCkGMMBbXxk1jozUWK35rK37Zzw%2B0i0a2m6WDbHFL3ZlkI6RevcfOaUguuC9nQ%2F76zAPh%2BvWu2CaG6orPRW0TDiZFIn9D5aIQMC6yIHJZr4YJn2g%2Fyo1qkhykHEj2JEVJbWuhOXy28MwWivhFhLOD7HveKCRTRUS7Bg4YB%2BE%2Be6fx38ywkifmjp1xL3gUBfOOZh9%2F0u%2B12W9s4%2FHOsb6s893HDLUTGjxp05mDN690VPiFUEePN8xMsxZCUEFlQVv8Bd1BL39NSTGB%2Bk95e0khIk9dQagkL5SfBBpZPpnT4qzxToAYgWpJ0ot5gHv%2B8RRmQOqRDuGpbHRNKscfRUce4AUJMa5DW8CD3zGq7T7S4TUi7OWHH8lHgpQ0L78w3EEgzD78a%2FIBjqkARQ33m5F4B0zbNzlp9tMXEbAsj%2BBl3AQptOPwtrGxpJOnfW0kZplJT5upaIHg%2BZIQPvUcP255Em67Q%2BwC3BOcDigLy1iInKSg4ez3SAN9haU9mdt52PnYlPDo584xNaR3qPXXfuk0QP5wYPP8%2FvH%2F5HtHYHH902kfpYIzXmUlGfbTQV3iDBstljEmeiwIwzRRjsGeQHLzdBzFAhfzDcWvv5LD7eB&X-Amz-Signature=cf53a2aaf175b5c0e2b7b8e19a9a6ef2553c7c1a64950bdec6a5c641cba85428&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OIPQILU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2o3JpHh8yvruJcI7r8DorfguJE1S6aHJL4gYkDSVAYAIhAJLmo6pLE7URX2Gjd3Bp6H1dbRpHhf8RWrodq0zfUhk%2FKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzkIBjg3aNEpuDBAUsq3ANaAlBW9RsrqoBrGeiMLcM%2FWuQh92IWnc4RpQfp8x9aTIhNiWkwMWDEzqLkG2%2FsUI92OoOdVhf0HRiNfaqP50r%2FirNKHjDKZQMPe9R9kH%2FvyRoa0uQyluD1v9KIhxflsIaRSpD3JeT1QgMOKQ1swIAH0K7CQxm94joyi1kZIELggT38zZxj0N8nzfsqwdrT%2FFWXyPBhb3fZKOEj83LcJaa649nvH07xbckiAUFYCNqQ4z0YgQpHK26iaHNHpCkGMMBbXxk1jozUWK35rK37Zzw%2B0i0a2m6WDbHFL3ZlkI6RevcfOaUguuC9nQ%2F76zAPh%2BvWu2CaG6orPRW0TDiZFIn9D5aIQMC6yIHJZr4YJn2g%2Fyo1qkhykHEj2JEVJbWuhOXy28MwWivhFhLOD7HveKCRTRUS7Bg4YB%2BE%2Be6fx38ywkifmjp1xL3gUBfOOZh9%2F0u%2B12W9s4%2FHOsb6s893HDLUTGjxp05mDN690VPiFUEePN8xMsxZCUEFlQVv8Bd1BL39NSTGB%2Bk95e0khIk9dQagkL5SfBBpZPpnT4qzxToAYgWpJ0ot5gHv%2B8RRmQOqRDuGpbHRNKscfRUce4AUJMa5DW8CD3zGq7T7S4TUi7OWHH8lHgpQ0L78w3EEgzD78a%2FIBjqkARQ33m5F4B0zbNzlp9tMXEbAsj%2BBl3AQptOPwtrGxpJOnfW0kZplJT5upaIHg%2BZIQPvUcP255Em67Q%2BwC3BOcDigLy1iInKSg4ez3SAN9haU9mdt52PnYlPDo584xNaR3qPXXfuk0QP5wYPP8%2FvH%2F5HtHYHH902kfpYIzXmUlGfbTQV3iDBstljEmeiwIwzRRjsGeQHLzdBzFAhfzDcWvv5LD7eB&X-Amz-Signature=bc65cc7e8af969c57e8e8079132b8b5d60d0ad7635226a2e7ccc021a04c5ec89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OIPQILU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2o3JpHh8yvruJcI7r8DorfguJE1S6aHJL4gYkDSVAYAIhAJLmo6pLE7URX2Gjd3Bp6H1dbRpHhf8RWrodq0zfUhk%2FKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzkIBjg3aNEpuDBAUsq3ANaAlBW9RsrqoBrGeiMLcM%2FWuQh92IWnc4RpQfp8x9aTIhNiWkwMWDEzqLkG2%2FsUI92OoOdVhf0HRiNfaqP50r%2FirNKHjDKZQMPe9R9kH%2FvyRoa0uQyluD1v9KIhxflsIaRSpD3JeT1QgMOKQ1swIAH0K7CQxm94joyi1kZIELggT38zZxj0N8nzfsqwdrT%2FFWXyPBhb3fZKOEj83LcJaa649nvH07xbckiAUFYCNqQ4z0YgQpHK26iaHNHpCkGMMBbXxk1jozUWK35rK37Zzw%2B0i0a2m6WDbHFL3ZlkI6RevcfOaUguuC9nQ%2F76zAPh%2BvWu2CaG6orPRW0TDiZFIn9D5aIQMC6yIHJZr4YJn2g%2Fyo1qkhykHEj2JEVJbWuhOXy28MwWivhFhLOD7HveKCRTRUS7Bg4YB%2BE%2Be6fx38ywkifmjp1xL3gUBfOOZh9%2F0u%2B12W9s4%2FHOsb6s893HDLUTGjxp05mDN690VPiFUEePN8xMsxZCUEFlQVv8Bd1BL39NSTGB%2Bk95e0khIk9dQagkL5SfBBpZPpnT4qzxToAYgWpJ0ot5gHv%2B8RRmQOqRDuGpbHRNKscfRUce4AUJMa5DW8CD3zGq7T7S4TUi7OWHH8lHgpQ0L78w3EEgzD78a%2FIBjqkARQ33m5F4B0zbNzlp9tMXEbAsj%2BBl3AQptOPwtrGxpJOnfW0kZplJT5upaIHg%2BZIQPvUcP255Em67Q%2BwC3BOcDigLy1iInKSg4ez3SAN9haU9mdt52PnYlPDo584xNaR3qPXXfuk0QP5wYPP8%2FvH%2F5HtHYHH902kfpYIzXmUlGfbTQV3iDBstljEmeiwIwzRRjsGeQHLzdBzFAhfzDcWvv5LD7eB&X-Amz-Signature=7fc4c34b30e9ad4a8bcb34f415bcf6b0e2dd82e9db4a27d31bee05075aa1132b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



