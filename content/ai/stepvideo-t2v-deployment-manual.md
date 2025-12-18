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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX6JEFBG%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEApxW7o7PGDUCWbNx87jnLOuQ3BLelkaZoqtA7M34r0AiBR6VNBbQJTksn8P%2Byt6svtj3Uu%2BuWrq%2B8GrC9M2EYZQSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLWtsO15RLfExyzhyKtwDLWXuI45oA%2B5hfimPGccPimYjkfMBcUfV%2BUh6%2BKCF2qL3t80%2BRlFQU73grvQLqwmfj31NTbjhrkp%2Br7%2BhIYwqnDFvpqlT6WdhQm1zvUD7zjBhslDmbuevDYu2TqFknqZkFXnvkozAyvJInUxVTIjeDV6MEMX%2Fe%2F41pZleIYlHRbrPSuSNVevti%2Bx2NZIcx99SvH2tXkMXaognVlYRz8YCIufdanm0J1y4KrLLxyvm2B2TCydtkraHRJZaBJijTgZyI2zsBCN7XFpsv0QT5qTGeBqBp0eiIv3soqLJTqkXIe4wlJ7cj3kryemukp2UrMPu3sJ7WcbGQ%2FCN2Wqyxry7LabU0IANMjJaF53TFr4rp69sHZjqPvRdaoriElP2ad4LU8ccsGUDktR4J8FT6HiZRPuss94Wd72AypT7978jcoaX8Ho%2Fp%2BPwEFBhUSOBs6cb9zVx4guyVgLpEm9vZiC2sDi31EidqjR7%2FVj4j4YvFnBm4FIzFt59VgYlvTPwVyTIh6jyCqoRGYMIXUsBP7s2AmOKc9CVS1fIiuIxDxEub%2FAbP%2BrOSl7CsK%2B8nOCVIrvqeOZ0Fc1t5DZVBQ3%2BseOvUuLuuK%2Buhh98Ti716jJCYNQ3suHqzM7MKjZYAyYw9MmNygY6pgF9o8hfLAjuS%2BIkYdZuxweqePsF7WqcPAR%2Bxyoqkkz2suDg8YJRI%2FDR3R9EgbxMkYSYXArExTnDcAMH4sPHlz83b%2FEIZM9Jqvodiesq2KOeBpKkr%2FTZ9OuVWVP10XRKt20Fte0%2F3%2FwOXnYMIsbksXLXl0Z9PwCTCHtiEFGXKaY7a174JwyVLZkIB9gEp2oviALiO23GsFPf2E%2FPmYcjvoE91lAliT%2F3&X-Amz-Signature=4627316ca47f54c1c66ddd7ae91951b6bb04f286bd2a085f5a01c4f0160ad07b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX6JEFBG%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEApxW7o7PGDUCWbNx87jnLOuQ3BLelkaZoqtA7M34r0AiBR6VNBbQJTksn8P%2Byt6svtj3Uu%2BuWrq%2B8GrC9M2EYZQSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLWtsO15RLfExyzhyKtwDLWXuI45oA%2B5hfimPGccPimYjkfMBcUfV%2BUh6%2BKCF2qL3t80%2BRlFQU73grvQLqwmfj31NTbjhrkp%2Br7%2BhIYwqnDFvpqlT6WdhQm1zvUD7zjBhslDmbuevDYu2TqFknqZkFXnvkozAyvJInUxVTIjeDV6MEMX%2Fe%2F41pZleIYlHRbrPSuSNVevti%2Bx2NZIcx99SvH2tXkMXaognVlYRz8YCIufdanm0J1y4KrLLxyvm2B2TCydtkraHRJZaBJijTgZyI2zsBCN7XFpsv0QT5qTGeBqBp0eiIv3soqLJTqkXIe4wlJ7cj3kryemukp2UrMPu3sJ7WcbGQ%2FCN2Wqyxry7LabU0IANMjJaF53TFr4rp69sHZjqPvRdaoriElP2ad4LU8ccsGUDktR4J8FT6HiZRPuss94Wd72AypT7978jcoaX8Ho%2Fp%2BPwEFBhUSOBs6cb9zVx4guyVgLpEm9vZiC2sDi31EidqjR7%2FVj4j4YvFnBm4FIzFt59VgYlvTPwVyTIh6jyCqoRGYMIXUsBP7s2AmOKc9CVS1fIiuIxDxEub%2FAbP%2BrOSl7CsK%2B8nOCVIrvqeOZ0Fc1t5DZVBQ3%2BseOvUuLuuK%2Buhh98Ti716jJCYNQ3suHqzM7MKjZYAyYw9MmNygY6pgF9o8hfLAjuS%2BIkYdZuxweqePsF7WqcPAR%2Bxyoqkkz2suDg8YJRI%2FDR3R9EgbxMkYSYXArExTnDcAMH4sPHlz83b%2FEIZM9Jqvodiesq2KOeBpKkr%2FTZ9OuVWVP10XRKt20Fte0%2F3%2FwOXnYMIsbksXLXl0Z9PwCTCHtiEFGXKaY7a174JwyVLZkIB9gEp2oviALiO23GsFPf2E%2FPmYcjvoE91lAliT%2F3&X-Amz-Signature=d2478910eda6843fbcc6731b4c639f82f0e53ad984c92b05e159a60648bee452&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX6JEFBG%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEApxW7o7PGDUCWbNx87jnLOuQ3BLelkaZoqtA7M34r0AiBR6VNBbQJTksn8P%2Byt6svtj3Uu%2BuWrq%2B8GrC9M2EYZQSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLWtsO15RLfExyzhyKtwDLWXuI45oA%2B5hfimPGccPimYjkfMBcUfV%2BUh6%2BKCF2qL3t80%2BRlFQU73grvQLqwmfj31NTbjhrkp%2Br7%2BhIYwqnDFvpqlT6WdhQm1zvUD7zjBhslDmbuevDYu2TqFknqZkFXnvkozAyvJInUxVTIjeDV6MEMX%2Fe%2F41pZleIYlHRbrPSuSNVevti%2Bx2NZIcx99SvH2tXkMXaognVlYRz8YCIufdanm0J1y4KrLLxyvm2B2TCydtkraHRJZaBJijTgZyI2zsBCN7XFpsv0QT5qTGeBqBp0eiIv3soqLJTqkXIe4wlJ7cj3kryemukp2UrMPu3sJ7WcbGQ%2FCN2Wqyxry7LabU0IANMjJaF53TFr4rp69sHZjqPvRdaoriElP2ad4LU8ccsGUDktR4J8FT6HiZRPuss94Wd72AypT7978jcoaX8Ho%2Fp%2BPwEFBhUSOBs6cb9zVx4guyVgLpEm9vZiC2sDi31EidqjR7%2FVj4j4YvFnBm4FIzFt59VgYlvTPwVyTIh6jyCqoRGYMIXUsBP7s2AmOKc9CVS1fIiuIxDxEub%2FAbP%2BrOSl7CsK%2B8nOCVIrvqeOZ0Fc1t5DZVBQ3%2BseOvUuLuuK%2Buhh98Ti716jJCYNQ3suHqzM7MKjZYAyYw9MmNygY6pgF9o8hfLAjuS%2BIkYdZuxweqePsF7WqcPAR%2Bxyoqkkz2suDg8YJRI%2FDR3R9EgbxMkYSYXArExTnDcAMH4sPHlz83b%2FEIZM9Jqvodiesq2KOeBpKkr%2FTZ9OuVWVP10XRKt20Fte0%2F3%2FwOXnYMIsbksXLXl0Z9PwCTCHtiEFGXKaY7a174JwyVLZkIB9gEp2oviALiO23GsFPf2E%2FPmYcjvoE91lAliT%2F3&X-Amz-Signature=20e73b636976452d63323ff8ff63e6a78294bbd3177344b7102e0b45bc2dc4cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX6JEFBG%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEApxW7o7PGDUCWbNx87jnLOuQ3BLelkaZoqtA7M34r0AiBR6VNBbQJTksn8P%2Byt6svtj3Uu%2BuWrq%2B8GrC9M2EYZQSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLWtsO15RLfExyzhyKtwDLWXuI45oA%2B5hfimPGccPimYjkfMBcUfV%2BUh6%2BKCF2qL3t80%2BRlFQU73grvQLqwmfj31NTbjhrkp%2Br7%2BhIYwqnDFvpqlT6WdhQm1zvUD7zjBhslDmbuevDYu2TqFknqZkFXnvkozAyvJInUxVTIjeDV6MEMX%2Fe%2F41pZleIYlHRbrPSuSNVevti%2Bx2NZIcx99SvH2tXkMXaognVlYRz8YCIufdanm0J1y4KrLLxyvm2B2TCydtkraHRJZaBJijTgZyI2zsBCN7XFpsv0QT5qTGeBqBp0eiIv3soqLJTqkXIe4wlJ7cj3kryemukp2UrMPu3sJ7WcbGQ%2FCN2Wqyxry7LabU0IANMjJaF53TFr4rp69sHZjqPvRdaoriElP2ad4LU8ccsGUDktR4J8FT6HiZRPuss94Wd72AypT7978jcoaX8Ho%2Fp%2BPwEFBhUSOBs6cb9zVx4guyVgLpEm9vZiC2sDi31EidqjR7%2FVj4j4YvFnBm4FIzFt59VgYlvTPwVyTIh6jyCqoRGYMIXUsBP7s2AmOKc9CVS1fIiuIxDxEub%2FAbP%2BrOSl7CsK%2B8nOCVIrvqeOZ0Fc1t5DZVBQ3%2BseOvUuLuuK%2Buhh98Ti716jJCYNQ3suHqzM7MKjZYAyYw9MmNygY6pgF9o8hfLAjuS%2BIkYdZuxweqePsF7WqcPAR%2Bxyoqkkz2suDg8YJRI%2FDR3R9EgbxMkYSYXArExTnDcAMH4sPHlz83b%2FEIZM9Jqvodiesq2KOeBpKkr%2FTZ9OuVWVP10XRKt20Fte0%2F3%2FwOXnYMIsbksXLXl0Z9PwCTCHtiEFGXKaY7a174JwyVLZkIB9gEp2oviALiO23GsFPf2E%2FPmYcjvoE91lAliT%2F3&X-Amz-Signature=4df1d94ce3bbcf904534bafe5594724b76f1fe2b14bddc27ff1115e3bf2617e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



