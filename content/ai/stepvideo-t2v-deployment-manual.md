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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BEXPUKM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsJWq5%2B9%2B%2BsJwnCo8qwuHZB7fKojTDRo49QQX4MTMLIAiBYOrWTESOsIg1zkOmIqoExm0JK60QoramahhHudakofyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMKH8J6%2BqytLbtFr%2BUKtwDJtDEHaSLt7TO4ws0OwQFFzBhHNA%2Bd5sd%2F6u4lPqau2fYI4G14kwFKG9XfkLUz%2B00uS8Lrwrd2GGQfiNMRp13Ngg4m5mo4wqfq5f2T2YezvI%2FObAmcwxG1WdVCFLp9Ycsi4pkW2BRkSrzBsqaA5%2Bflh1%2FiwM2SBa6AQv%2FtkFu4npMY0F948Ar3E9n3RSzedVbvsy8SuUgJnmcvHOJ9HSfQBEo88nEQ0qZmXT6%2BX%2FPMLWLYcqO4YtBSk8w1WoQkEEu1WurGMn5uV3hQK0FpAKda72zWK5UCmsU5ZHvHEcJVwqDBU7uNFZ2CL6CpxMrR%2FM1HW8IYq5hfVeSRytHZyjIltLMw34FnY5p5v57gytf0iGga5i5BGf8Mrm9UY84aiuKdgWADpQXRJwfelaPf%2Fpcms72q1V1iGYzygJAxx3%2B9vwiYgtCZ1xRAxi1Kpt2QalBrXhL2Gc9ZBPBctDe%2BUFJHXmC9JazrYn5T6uThu2ouNe14Alg8k7FdwrflMNgjfkC7e2TP3djwu0sIX1lZkcQgGAa%2BotlYC%2Ba0wuukeSGQL5TvV12rtvJ1ghora0rDtDpvqtlGaQ%2B6jNOkQN0KvOkWPJQ1WBqjxD8jSFOLp7d96q9McoMnWJpibVWr7Iw5um8zgY6pgEWRGpVO2MOZXlRvoc%2FbKemRfZsQw8DhD1MRiYZhW0sDgJCwmpUA2DEAUxhGwc0Qn5wQP1b6Klm1m9B3vguEW0JEn5MHLB6AKdQMlMw8HvHna%2F6UbF%2B7T9XE6z7cF0aDqG87ik2zGuNpfP502EjF%2BYnoJd2D74XolaAXiAYc5WE9eT6bWSCCRoNmcbdvsU0v3Xo8w4VqHOusZjNUrjditcrZoIPl1iS&X-Amz-Signature=71646caad53ec783dbe3c3a72593604ea7bca5c01577a5562b587f0bf138c2af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BEXPUKM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsJWq5%2B9%2B%2BsJwnCo8qwuHZB7fKojTDRo49QQX4MTMLIAiBYOrWTESOsIg1zkOmIqoExm0JK60QoramahhHudakofyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMKH8J6%2BqytLbtFr%2BUKtwDJtDEHaSLt7TO4ws0OwQFFzBhHNA%2Bd5sd%2F6u4lPqau2fYI4G14kwFKG9XfkLUz%2B00uS8Lrwrd2GGQfiNMRp13Ngg4m5mo4wqfq5f2T2YezvI%2FObAmcwxG1WdVCFLp9Ycsi4pkW2BRkSrzBsqaA5%2Bflh1%2FiwM2SBa6AQv%2FtkFu4npMY0F948Ar3E9n3RSzedVbvsy8SuUgJnmcvHOJ9HSfQBEo88nEQ0qZmXT6%2BX%2FPMLWLYcqO4YtBSk8w1WoQkEEu1WurGMn5uV3hQK0FpAKda72zWK5UCmsU5ZHvHEcJVwqDBU7uNFZ2CL6CpxMrR%2FM1HW8IYq5hfVeSRytHZyjIltLMw34FnY5p5v57gytf0iGga5i5BGf8Mrm9UY84aiuKdgWADpQXRJwfelaPf%2Fpcms72q1V1iGYzygJAxx3%2B9vwiYgtCZ1xRAxi1Kpt2QalBrXhL2Gc9ZBPBctDe%2BUFJHXmC9JazrYn5T6uThu2ouNe14Alg8k7FdwrflMNgjfkC7e2TP3djwu0sIX1lZkcQgGAa%2BotlYC%2Ba0wuukeSGQL5TvV12rtvJ1ghora0rDtDpvqtlGaQ%2B6jNOkQN0KvOkWPJQ1WBqjxD8jSFOLp7d96q9McoMnWJpibVWr7Iw5um8zgY6pgEWRGpVO2MOZXlRvoc%2FbKemRfZsQw8DhD1MRiYZhW0sDgJCwmpUA2DEAUxhGwc0Qn5wQP1b6Klm1m9B3vguEW0JEn5MHLB6AKdQMlMw8HvHna%2F6UbF%2B7T9XE6z7cF0aDqG87ik2zGuNpfP502EjF%2BYnoJd2D74XolaAXiAYc5WE9eT6bWSCCRoNmcbdvsU0v3Xo8w4VqHOusZjNUrjditcrZoIPl1iS&X-Amz-Signature=85dc7d8e55d080bf78f88f754ba554043c27be10f7aa3cd3bbb624589651919b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BEXPUKM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsJWq5%2B9%2B%2BsJwnCo8qwuHZB7fKojTDRo49QQX4MTMLIAiBYOrWTESOsIg1zkOmIqoExm0JK60QoramahhHudakofyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMKH8J6%2BqytLbtFr%2BUKtwDJtDEHaSLt7TO4ws0OwQFFzBhHNA%2Bd5sd%2F6u4lPqau2fYI4G14kwFKG9XfkLUz%2B00uS8Lrwrd2GGQfiNMRp13Ngg4m5mo4wqfq5f2T2YezvI%2FObAmcwxG1WdVCFLp9Ycsi4pkW2BRkSrzBsqaA5%2Bflh1%2FiwM2SBa6AQv%2FtkFu4npMY0F948Ar3E9n3RSzedVbvsy8SuUgJnmcvHOJ9HSfQBEo88nEQ0qZmXT6%2BX%2FPMLWLYcqO4YtBSk8w1WoQkEEu1WurGMn5uV3hQK0FpAKda72zWK5UCmsU5ZHvHEcJVwqDBU7uNFZ2CL6CpxMrR%2FM1HW8IYq5hfVeSRytHZyjIltLMw34FnY5p5v57gytf0iGga5i5BGf8Mrm9UY84aiuKdgWADpQXRJwfelaPf%2Fpcms72q1V1iGYzygJAxx3%2B9vwiYgtCZ1xRAxi1Kpt2QalBrXhL2Gc9ZBPBctDe%2BUFJHXmC9JazrYn5T6uThu2ouNe14Alg8k7FdwrflMNgjfkC7e2TP3djwu0sIX1lZkcQgGAa%2BotlYC%2Ba0wuukeSGQL5TvV12rtvJ1ghora0rDtDpvqtlGaQ%2B6jNOkQN0KvOkWPJQ1WBqjxD8jSFOLp7d96q9McoMnWJpibVWr7Iw5um8zgY6pgEWRGpVO2MOZXlRvoc%2FbKemRfZsQw8DhD1MRiYZhW0sDgJCwmpUA2DEAUxhGwc0Qn5wQP1b6Klm1m9B3vguEW0JEn5MHLB6AKdQMlMw8HvHna%2F6UbF%2B7T9XE6z7cF0aDqG87ik2zGuNpfP502EjF%2BYnoJd2D74XolaAXiAYc5WE9eT6bWSCCRoNmcbdvsU0v3Xo8w4VqHOusZjNUrjditcrZoIPl1iS&X-Amz-Signature=2a998b20e44ad6e1df9d71f53c539d927fd6a04779d4ff54cc3b6d7d1f2b32e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BEXPUKM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsJWq5%2B9%2B%2BsJwnCo8qwuHZB7fKojTDRo49QQX4MTMLIAiBYOrWTESOsIg1zkOmIqoExm0JK60QoramahhHudakofyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMKH8J6%2BqytLbtFr%2BUKtwDJtDEHaSLt7TO4ws0OwQFFzBhHNA%2Bd5sd%2F6u4lPqau2fYI4G14kwFKG9XfkLUz%2B00uS8Lrwrd2GGQfiNMRp13Ngg4m5mo4wqfq5f2T2YezvI%2FObAmcwxG1WdVCFLp9Ycsi4pkW2BRkSrzBsqaA5%2Bflh1%2FiwM2SBa6AQv%2FtkFu4npMY0F948Ar3E9n3RSzedVbvsy8SuUgJnmcvHOJ9HSfQBEo88nEQ0qZmXT6%2BX%2FPMLWLYcqO4YtBSk8w1WoQkEEu1WurGMn5uV3hQK0FpAKda72zWK5UCmsU5ZHvHEcJVwqDBU7uNFZ2CL6CpxMrR%2FM1HW8IYq5hfVeSRytHZyjIltLMw34FnY5p5v57gytf0iGga5i5BGf8Mrm9UY84aiuKdgWADpQXRJwfelaPf%2Fpcms72q1V1iGYzygJAxx3%2B9vwiYgtCZ1xRAxi1Kpt2QalBrXhL2Gc9ZBPBctDe%2BUFJHXmC9JazrYn5T6uThu2ouNe14Alg8k7FdwrflMNgjfkC7e2TP3djwu0sIX1lZkcQgGAa%2BotlYC%2Ba0wuukeSGQL5TvV12rtvJ1ghora0rDtDpvqtlGaQ%2B6jNOkQN0KvOkWPJQ1WBqjxD8jSFOLp7d96q9McoMnWJpibVWr7Iw5um8zgY6pgEWRGpVO2MOZXlRvoc%2FbKemRfZsQw8DhD1MRiYZhW0sDgJCwmpUA2DEAUxhGwc0Qn5wQP1b6Klm1m9B3vguEW0JEn5MHLB6AKdQMlMw8HvHna%2F6UbF%2B7T9XE6z7cF0aDqG87ik2zGuNpfP502EjF%2BYnoJd2D74XolaAXiAYc5WE9eT6bWSCCRoNmcbdvsU0v3Xo8w4VqHOusZjNUrjditcrZoIPl1iS&X-Amz-Signature=02067541b9c5da53bbba8e61cdcdb22753cdcb7acb67c947408c8303864f2a56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



