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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVB7KQC3%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFVDLncWO84vTDhKsFnnyMXPDki5rFx5yookv2hssMgeAiEA8%2BN%2FC5qyLAjuPwRZGr3jcWlXCD4TSFP20KRj6EkSyNEq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDKAmZExHLQZiu4yRsircA%2BMLqbdc%2BWWwSs%2BGpKUWp0jLakZo8AsMtuhJEDsMVO2yDaoM1lxnTGSxhIL8c7HkWUdurb6b%2B%2FST9Opsxsd8Qnek2KSo2W5eEhAA7LPBlt20T8rri4%2BrvG7%2B8MCnZs8Uhqt7RwGQgh678CTBmuZ34JOjJlR3iZMFvfTrknjoQLN3tUAd%2BTJYNVX%2BO3pvK0Zsy3V47PqoAs9a9Lp4NEoME37L4lQLC0mkDJGn4AwXlK9SU%2FXiFm4eUlv44sQ14fGVkkMBBu63g%2F16nR4H7yazpf7hdkSi6yO6L8Blg%2Fu3z4kK2%2F3%2FTf0bXqv95RQy%2Fyxlz3OcE%2B7i3bZxCaVUVvus6XSmKsHCZxIKSxrsjL3WSJAdCPBHnJmHiG1hkgIQ8CdrR4DUkBpGAy1NLtlr7CS2a%2FRwWrMKcQSQkfWB%2BYQfZdLMun7RTC%2FXQi7gqZ%2BuYDHdt19ZNC6EJujWcuQJS3AEFbKrLlGDCCKbTw8GuXnvk5RFJGblA4t9RnGB6uDZWCqDgz9TgAejsmNzMLQtN6dNUW9VHFGqNPk%2FMbwcQdi4k1a7wCyal%2BMBQz3oho%2FMLIXUJvdIDfXbAmaMtBPRnf0kTK6QVGXncn3OM6o2l%2F2USrbFOBeB6RDphqtQIT6DMNnA38gGOqUBBt9RjbaHDuUkWSkxL4hOBNqNhuR0oS0hQUYk5VHyTYh1oZfiv%2FL4LmbMSrAGZoISUr%2Bu7VJP%2B3SnoY7hVFElUUw6SPDUxoF6r6qgBB9rZj9i%2FfoYMvKfg9edIlEPEIojRglQN56ZGsvidKx9YcvG998qDyAtFEdaUSd%2Fi91A8Jk%2BSKBf3yM47N106EVR1Upwh7lCjbwToeznz9PKn3TWI4Wz3ppi&X-Amz-Signature=2782f383eb067d600259a0dfcb199e536df56f77847527419a057cd8c00c3aae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVB7KQC3%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFVDLncWO84vTDhKsFnnyMXPDki5rFx5yookv2hssMgeAiEA8%2BN%2FC5qyLAjuPwRZGr3jcWlXCD4TSFP20KRj6EkSyNEq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDKAmZExHLQZiu4yRsircA%2BMLqbdc%2BWWwSs%2BGpKUWp0jLakZo8AsMtuhJEDsMVO2yDaoM1lxnTGSxhIL8c7HkWUdurb6b%2B%2FST9Opsxsd8Qnek2KSo2W5eEhAA7LPBlt20T8rri4%2BrvG7%2B8MCnZs8Uhqt7RwGQgh678CTBmuZ34JOjJlR3iZMFvfTrknjoQLN3tUAd%2BTJYNVX%2BO3pvK0Zsy3V47PqoAs9a9Lp4NEoME37L4lQLC0mkDJGn4AwXlK9SU%2FXiFm4eUlv44sQ14fGVkkMBBu63g%2F16nR4H7yazpf7hdkSi6yO6L8Blg%2Fu3z4kK2%2F3%2FTf0bXqv95RQy%2Fyxlz3OcE%2B7i3bZxCaVUVvus6XSmKsHCZxIKSxrsjL3WSJAdCPBHnJmHiG1hkgIQ8CdrR4DUkBpGAy1NLtlr7CS2a%2FRwWrMKcQSQkfWB%2BYQfZdLMun7RTC%2FXQi7gqZ%2BuYDHdt19ZNC6EJujWcuQJS3AEFbKrLlGDCCKbTw8GuXnvk5RFJGblA4t9RnGB6uDZWCqDgz9TgAejsmNzMLQtN6dNUW9VHFGqNPk%2FMbwcQdi4k1a7wCyal%2BMBQz3oho%2FMLIXUJvdIDfXbAmaMtBPRnf0kTK6QVGXncn3OM6o2l%2F2USrbFOBeB6RDphqtQIT6DMNnA38gGOqUBBt9RjbaHDuUkWSkxL4hOBNqNhuR0oS0hQUYk5VHyTYh1oZfiv%2FL4LmbMSrAGZoISUr%2Bu7VJP%2B3SnoY7hVFElUUw6SPDUxoF6r6qgBB9rZj9i%2FfoYMvKfg9edIlEPEIojRglQN56ZGsvidKx9YcvG998qDyAtFEdaUSd%2Fi91A8Jk%2BSKBf3yM47N106EVR1Upwh7lCjbwToeznz9PKn3TWI4Wz3ppi&X-Amz-Signature=ac4921bdcc8b1dc5c2cd9e518bf40bd9aac91b751a7f770085a75fd8f5ef714a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVB7KQC3%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFVDLncWO84vTDhKsFnnyMXPDki5rFx5yookv2hssMgeAiEA8%2BN%2FC5qyLAjuPwRZGr3jcWlXCD4TSFP20KRj6EkSyNEq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDKAmZExHLQZiu4yRsircA%2BMLqbdc%2BWWwSs%2BGpKUWp0jLakZo8AsMtuhJEDsMVO2yDaoM1lxnTGSxhIL8c7HkWUdurb6b%2B%2FST9Opsxsd8Qnek2KSo2W5eEhAA7LPBlt20T8rri4%2BrvG7%2B8MCnZs8Uhqt7RwGQgh678CTBmuZ34JOjJlR3iZMFvfTrknjoQLN3tUAd%2BTJYNVX%2BO3pvK0Zsy3V47PqoAs9a9Lp4NEoME37L4lQLC0mkDJGn4AwXlK9SU%2FXiFm4eUlv44sQ14fGVkkMBBu63g%2F16nR4H7yazpf7hdkSi6yO6L8Blg%2Fu3z4kK2%2F3%2FTf0bXqv95RQy%2Fyxlz3OcE%2B7i3bZxCaVUVvus6XSmKsHCZxIKSxrsjL3WSJAdCPBHnJmHiG1hkgIQ8CdrR4DUkBpGAy1NLtlr7CS2a%2FRwWrMKcQSQkfWB%2BYQfZdLMun7RTC%2FXQi7gqZ%2BuYDHdt19ZNC6EJujWcuQJS3AEFbKrLlGDCCKbTw8GuXnvk5RFJGblA4t9RnGB6uDZWCqDgz9TgAejsmNzMLQtN6dNUW9VHFGqNPk%2FMbwcQdi4k1a7wCyal%2BMBQz3oho%2FMLIXUJvdIDfXbAmaMtBPRnf0kTK6QVGXncn3OM6o2l%2F2USrbFOBeB6RDphqtQIT6DMNnA38gGOqUBBt9RjbaHDuUkWSkxL4hOBNqNhuR0oS0hQUYk5VHyTYh1oZfiv%2FL4LmbMSrAGZoISUr%2Bu7VJP%2B3SnoY7hVFElUUw6SPDUxoF6r6qgBB9rZj9i%2FfoYMvKfg9edIlEPEIojRglQN56ZGsvidKx9YcvG998qDyAtFEdaUSd%2Fi91A8Jk%2BSKBf3yM47N106EVR1Upwh7lCjbwToeznz9PKn3TWI4Wz3ppi&X-Amz-Signature=30b0d6639488f549ad32e2a99a5bfc2f2b402a2c9f30af3108b29b6ade96048d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVB7KQC3%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFVDLncWO84vTDhKsFnnyMXPDki5rFx5yookv2hssMgeAiEA8%2BN%2FC5qyLAjuPwRZGr3jcWlXCD4TSFP20KRj6EkSyNEq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDKAmZExHLQZiu4yRsircA%2BMLqbdc%2BWWwSs%2BGpKUWp0jLakZo8AsMtuhJEDsMVO2yDaoM1lxnTGSxhIL8c7HkWUdurb6b%2B%2FST9Opsxsd8Qnek2KSo2W5eEhAA7LPBlt20T8rri4%2BrvG7%2B8MCnZs8Uhqt7RwGQgh678CTBmuZ34JOjJlR3iZMFvfTrknjoQLN3tUAd%2BTJYNVX%2BO3pvK0Zsy3V47PqoAs9a9Lp4NEoME37L4lQLC0mkDJGn4AwXlK9SU%2FXiFm4eUlv44sQ14fGVkkMBBu63g%2F16nR4H7yazpf7hdkSi6yO6L8Blg%2Fu3z4kK2%2F3%2FTf0bXqv95RQy%2Fyxlz3OcE%2B7i3bZxCaVUVvus6XSmKsHCZxIKSxrsjL3WSJAdCPBHnJmHiG1hkgIQ8CdrR4DUkBpGAy1NLtlr7CS2a%2FRwWrMKcQSQkfWB%2BYQfZdLMun7RTC%2FXQi7gqZ%2BuYDHdt19ZNC6EJujWcuQJS3AEFbKrLlGDCCKbTw8GuXnvk5RFJGblA4t9RnGB6uDZWCqDgz9TgAejsmNzMLQtN6dNUW9VHFGqNPk%2FMbwcQdi4k1a7wCyal%2BMBQz3oho%2FMLIXUJvdIDfXbAmaMtBPRnf0kTK6QVGXncn3OM6o2l%2F2USrbFOBeB6RDphqtQIT6DMNnA38gGOqUBBt9RjbaHDuUkWSkxL4hOBNqNhuR0oS0hQUYk5VHyTYh1oZfiv%2FL4LmbMSrAGZoISUr%2Bu7VJP%2B3SnoY7hVFElUUw6SPDUxoF6r6qgBB9rZj9i%2FfoYMvKfg9edIlEPEIojRglQN56ZGsvidKx9YcvG998qDyAtFEdaUSd%2Fi91A8Jk%2BSKBf3yM47N106EVR1Upwh7lCjbwToeznz9PKn3TWI4Wz3ppi&X-Amz-Signature=fb090a121a5f6ccd900de8583b7fd57edcc8e898a663b2c93731cb8c08fb7581&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



