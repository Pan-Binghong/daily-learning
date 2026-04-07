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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHOWH6K%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQC%2BM7LTHjlzrkEWxIhoCLH26k%2BfByr7YFxDWfpbl2JqqgIgVSbBvnorFnCwglNMNCdvB2ie%2BEgFw%2Bp6%2FoQAe1W9KRYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6Cf552pciunuzEQircA2zSwJZABztvBuqk1qY%2FK2eSR7wOx%2BE%2FGJxPlWlA8OWjnhCV9abUpxju07%2FMkhEYeJ8NYGs0un1liWlD2%2Bp5lX5HGjUyAP06zZepRwtVUeiEAPYgoSXPQdpnu01KakjZ%2ByVUfBGSBTr8ZbAMqxSnrwSXRLcd0r0jD2jhC5oo6aVvhey3z3chgVjTF9dWF5r8einqX9z2Szc1vCbrfGbotmgy4fdw6aw7sJgAlVVdflU8Gjf9ASE40CLwVI7Va2GwacD45oYNgSJs70q4k5q93A68sOyhx1ttwMrM9LxDt56MQ%2F0%2FNswP4yj5ju5ZIiXah898bbmxJL8AK%2BqyQjgs3pNV90B12I3RlTSXgQds1v040xv%2FEea4CGoloB4tR4LKWwpcnlK64oN60g1I%2BtAF2jCJ%2FtMYm8mfvRLZSkAW6kbvCoIXHXpTgd3KwBqzEBkz7HnhDh0mhgFZPB0gvsH5JdN1V0pTjSw7x0kHQeiw%2BsHUNXxZodmqpVjPvZ65ptHH7CpcuYGCWIKaY64loMZP1y70bTcK4qw1jCJnNK5TtLzcGtxm8wEep1E4Qwt87phfr9pQeuvbKfeU0TboENOvPszdny0iAvsybhQ%2B%2BP6KrAzVLUVeY%2BK43jOmJYcLMJP20c4GOqUB1xp7kg3X8IcW6%2BsUtPvZz5xx4krIaD%2B8Vuz3fF69HSDmEFoNaWOq6CO%2B3IRaoK81SgTB7vhgmP%2Fyq9dtBib6rlkMAN0tvA%2FqwSNdDhU8PfqCBcwyAam%2BA9ZqLq%2BD9%2BZFo8um%2FeHHGxTf6bp%2BeC0srajARhfZj7v2zvKtQWt4pKZ3kBd%2B2B3AY2jiLR0VcAn6MfbzvszskOv8WaI2aUJt4x1a1xS9&X-Amz-Signature=d901f89b71b191eebe98ef88ff5e96d55508fd848644bf1e3e0817d5879863e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHOWH6K%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQC%2BM7LTHjlzrkEWxIhoCLH26k%2BfByr7YFxDWfpbl2JqqgIgVSbBvnorFnCwglNMNCdvB2ie%2BEgFw%2Bp6%2FoQAe1W9KRYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6Cf552pciunuzEQircA2zSwJZABztvBuqk1qY%2FK2eSR7wOx%2BE%2FGJxPlWlA8OWjnhCV9abUpxju07%2FMkhEYeJ8NYGs0un1liWlD2%2Bp5lX5HGjUyAP06zZepRwtVUeiEAPYgoSXPQdpnu01KakjZ%2ByVUfBGSBTr8ZbAMqxSnrwSXRLcd0r0jD2jhC5oo6aVvhey3z3chgVjTF9dWF5r8einqX9z2Szc1vCbrfGbotmgy4fdw6aw7sJgAlVVdflU8Gjf9ASE40CLwVI7Va2GwacD45oYNgSJs70q4k5q93A68sOyhx1ttwMrM9LxDt56MQ%2F0%2FNswP4yj5ju5ZIiXah898bbmxJL8AK%2BqyQjgs3pNV90B12I3RlTSXgQds1v040xv%2FEea4CGoloB4tR4LKWwpcnlK64oN60g1I%2BtAF2jCJ%2FtMYm8mfvRLZSkAW6kbvCoIXHXpTgd3KwBqzEBkz7HnhDh0mhgFZPB0gvsH5JdN1V0pTjSw7x0kHQeiw%2BsHUNXxZodmqpVjPvZ65ptHH7CpcuYGCWIKaY64loMZP1y70bTcK4qw1jCJnNK5TtLzcGtxm8wEep1E4Qwt87phfr9pQeuvbKfeU0TboENOvPszdny0iAvsybhQ%2B%2BP6KrAzVLUVeY%2BK43jOmJYcLMJP20c4GOqUB1xp7kg3X8IcW6%2BsUtPvZz5xx4krIaD%2B8Vuz3fF69HSDmEFoNaWOq6CO%2B3IRaoK81SgTB7vhgmP%2Fyq9dtBib6rlkMAN0tvA%2FqwSNdDhU8PfqCBcwyAam%2BA9ZqLq%2BD9%2BZFo8um%2FeHHGxTf6bp%2BeC0srajARhfZj7v2zvKtQWt4pKZ3kBd%2B2B3AY2jiLR0VcAn6MfbzvszskOv8WaI2aUJt4x1a1xS9&X-Amz-Signature=759f379dd92abf03ae3d7501e892fc50fe0473d8c96254fc669e87e14695717a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHOWH6K%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQC%2BM7LTHjlzrkEWxIhoCLH26k%2BfByr7YFxDWfpbl2JqqgIgVSbBvnorFnCwglNMNCdvB2ie%2BEgFw%2Bp6%2FoQAe1W9KRYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6Cf552pciunuzEQircA2zSwJZABztvBuqk1qY%2FK2eSR7wOx%2BE%2FGJxPlWlA8OWjnhCV9abUpxju07%2FMkhEYeJ8NYGs0un1liWlD2%2Bp5lX5HGjUyAP06zZepRwtVUeiEAPYgoSXPQdpnu01KakjZ%2ByVUfBGSBTr8ZbAMqxSnrwSXRLcd0r0jD2jhC5oo6aVvhey3z3chgVjTF9dWF5r8einqX9z2Szc1vCbrfGbotmgy4fdw6aw7sJgAlVVdflU8Gjf9ASE40CLwVI7Va2GwacD45oYNgSJs70q4k5q93A68sOyhx1ttwMrM9LxDt56MQ%2F0%2FNswP4yj5ju5ZIiXah898bbmxJL8AK%2BqyQjgs3pNV90B12I3RlTSXgQds1v040xv%2FEea4CGoloB4tR4LKWwpcnlK64oN60g1I%2BtAF2jCJ%2FtMYm8mfvRLZSkAW6kbvCoIXHXpTgd3KwBqzEBkz7HnhDh0mhgFZPB0gvsH5JdN1V0pTjSw7x0kHQeiw%2BsHUNXxZodmqpVjPvZ65ptHH7CpcuYGCWIKaY64loMZP1y70bTcK4qw1jCJnNK5TtLzcGtxm8wEep1E4Qwt87phfr9pQeuvbKfeU0TboENOvPszdny0iAvsybhQ%2B%2BP6KrAzVLUVeY%2BK43jOmJYcLMJP20c4GOqUB1xp7kg3X8IcW6%2BsUtPvZz5xx4krIaD%2B8Vuz3fF69HSDmEFoNaWOq6CO%2B3IRaoK81SgTB7vhgmP%2Fyq9dtBib6rlkMAN0tvA%2FqwSNdDhU8PfqCBcwyAam%2BA9ZqLq%2BD9%2BZFo8um%2FeHHGxTf6bp%2BeC0srajARhfZj7v2zvKtQWt4pKZ3kBd%2B2B3AY2jiLR0VcAn6MfbzvszskOv8WaI2aUJt4x1a1xS9&X-Amz-Signature=a7924662a03a5ffad08245f2e86b9be02ea23a320528fabcd74deb70f9cbb949&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHOWH6K%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQC%2BM7LTHjlzrkEWxIhoCLH26k%2BfByr7YFxDWfpbl2JqqgIgVSbBvnorFnCwglNMNCdvB2ie%2BEgFw%2Bp6%2FoQAe1W9KRYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK6Cf552pciunuzEQircA2zSwJZABztvBuqk1qY%2FK2eSR7wOx%2BE%2FGJxPlWlA8OWjnhCV9abUpxju07%2FMkhEYeJ8NYGs0un1liWlD2%2Bp5lX5HGjUyAP06zZepRwtVUeiEAPYgoSXPQdpnu01KakjZ%2ByVUfBGSBTr8ZbAMqxSnrwSXRLcd0r0jD2jhC5oo6aVvhey3z3chgVjTF9dWF5r8einqX9z2Szc1vCbrfGbotmgy4fdw6aw7sJgAlVVdflU8Gjf9ASE40CLwVI7Va2GwacD45oYNgSJs70q4k5q93A68sOyhx1ttwMrM9LxDt56MQ%2F0%2FNswP4yj5ju5ZIiXah898bbmxJL8AK%2BqyQjgs3pNV90B12I3RlTSXgQds1v040xv%2FEea4CGoloB4tR4LKWwpcnlK64oN60g1I%2BtAF2jCJ%2FtMYm8mfvRLZSkAW6kbvCoIXHXpTgd3KwBqzEBkz7HnhDh0mhgFZPB0gvsH5JdN1V0pTjSw7x0kHQeiw%2BsHUNXxZodmqpVjPvZ65ptHH7CpcuYGCWIKaY64loMZP1y70bTcK4qw1jCJnNK5TtLzcGtxm8wEep1E4Qwt87phfr9pQeuvbKfeU0TboENOvPszdny0iAvsybhQ%2B%2BP6KrAzVLUVeY%2BK43jOmJYcLMJP20c4GOqUB1xp7kg3X8IcW6%2BsUtPvZz5xx4krIaD%2B8Vuz3fF69HSDmEFoNaWOq6CO%2B3IRaoK81SgTB7vhgmP%2Fyq9dtBib6rlkMAN0tvA%2FqwSNdDhU8PfqCBcwyAam%2BA9ZqLq%2BD9%2BZFo8um%2FeHHGxTf6bp%2BeC0srajARhfZj7v2zvKtQWt4pKZ3kBd%2B2B3AY2jiLR0VcAn6MfbzvszskOv8WaI2aUJt4x1a1xS9&X-Amz-Signature=902d8490df7792c31df1fbd34dbaa5738ade36789b52ebcd935a57c764ffacfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



