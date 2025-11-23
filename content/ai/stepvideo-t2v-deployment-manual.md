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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXUPGS7M%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCO9szqM7PaYMW98P07UWsdmxzpr%2F8d2XcuDwLv0oOztgIgbZaPcJOh9gppRSPAA6Xc1OD5e8YmxShJEuvgcsxuSnoq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDOheXCutzsrgh5V5BCrcA5iBtp0oh0A6uAfkabdffBHV4aM7zh6V88PhGRSSbTP%2B%2FLx9fB8whx7ghWVI6jqEtAYyJ27SB60Dzd1pV%2FzpW0cZoTMgtugtBzU9Iq1pREZD4mT0Fy%2Bs5%2BnbRm18B%2FMaVdCNVMQsEDiXsVUXHtALmCWp9jmuWR4udT5b9bi9g56Iw5XijgKYrOEHDcJL70p2HDzi8qWsCWofxlW0zxXjPNU3Ff1N%2FYJHugT1cQBPhtpNEIIoN2wgqcx%2FR6UnL4KlqcI%2BdS5ta1ATiUvfd%2BK%2F0FPtG%2BdG3m40T6uxy4PyxJhDpkddwZeZEgC2Ca%2FnXMsWFTqsguqJzxqQnoFhk7wl4LkPviquOlot8tyDZr%2BYr%2B8VZtZuM%2Fw1uzHOO7cHRvXL%2BQ5yTjuuvLfQH5HPyZHa8ipjybbkR23N2iF1Sxo%2BEvSNo65toUSyLJfKsIhWBIyJvODfLfyvbvZ9MZe%2FdobIw1Fu5NOo5pd%2BI4qDnnuxlwnbF0bgO0OQXjqJBgCfyOxbluq2C4yWcJmsNR%2BKBHppHTyKj7hlUqad1SYW7AbMH2HtZGN9WUTf%2BMOMqAu1KZ9y8E80teHrNH1kNo%2BGWmMQBODiYkrWZt7XSs9%2BYpNLrRhUwZqiz35y9yAVgbl8MLywickGOqUBFYdSML5ax%2FGspAVrt%2BiHigEfAOuIXOwraj%2BgEWQxbciN9GcksQ7uXxY6aitn%2F0RX7vpHCwM15tfYn2g%2BkSj8wbgc%2BOetc3YYBd63eS%2Fi%2FDYbEX8Gzj7AkcKqp79KfQjzihqFZB88UscVI5C5TvaB11QayQp0fBxEI2EMFGXE2T0BpAClH12n0L%2B9lIqltXoXswli9uEz%2BIz28vNhrt%2B3qRkPNNPR&X-Amz-Signature=e46a447725fc56bd66084adf6baa05c9139ec401c2593c17000b69277b51b6b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXUPGS7M%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCO9szqM7PaYMW98P07UWsdmxzpr%2F8d2XcuDwLv0oOztgIgbZaPcJOh9gppRSPAA6Xc1OD5e8YmxShJEuvgcsxuSnoq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDOheXCutzsrgh5V5BCrcA5iBtp0oh0A6uAfkabdffBHV4aM7zh6V88PhGRSSbTP%2B%2FLx9fB8whx7ghWVI6jqEtAYyJ27SB60Dzd1pV%2FzpW0cZoTMgtugtBzU9Iq1pREZD4mT0Fy%2Bs5%2BnbRm18B%2FMaVdCNVMQsEDiXsVUXHtALmCWp9jmuWR4udT5b9bi9g56Iw5XijgKYrOEHDcJL70p2HDzi8qWsCWofxlW0zxXjPNU3Ff1N%2FYJHugT1cQBPhtpNEIIoN2wgqcx%2FR6UnL4KlqcI%2BdS5ta1ATiUvfd%2BK%2F0FPtG%2BdG3m40T6uxy4PyxJhDpkddwZeZEgC2Ca%2FnXMsWFTqsguqJzxqQnoFhk7wl4LkPviquOlot8tyDZr%2BYr%2B8VZtZuM%2Fw1uzHOO7cHRvXL%2BQ5yTjuuvLfQH5HPyZHa8ipjybbkR23N2iF1Sxo%2BEvSNo65toUSyLJfKsIhWBIyJvODfLfyvbvZ9MZe%2FdobIw1Fu5NOo5pd%2BI4qDnnuxlwnbF0bgO0OQXjqJBgCfyOxbluq2C4yWcJmsNR%2BKBHppHTyKj7hlUqad1SYW7AbMH2HtZGN9WUTf%2BMOMqAu1KZ9y8E80teHrNH1kNo%2BGWmMQBODiYkrWZt7XSs9%2BYpNLrRhUwZqiz35y9yAVgbl8MLywickGOqUBFYdSML5ax%2FGspAVrt%2BiHigEfAOuIXOwraj%2BgEWQxbciN9GcksQ7uXxY6aitn%2F0RX7vpHCwM15tfYn2g%2BkSj8wbgc%2BOetc3YYBd63eS%2Fi%2FDYbEX8Gzj7AkcKqp79KfQjzihqFZB88UscVI5C5TvaB11QayQp0fBxEI2EMFGXE2T0BpAClH12n0L%2B9lIqltXoXswli9uEz%2BIz28vNhrt%2B3qRkPNNPR&X-Amz-Signature=97ec8857ec0e4644946d66aee03411ba690aad68715d2dd42f06ad6a6854d244&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXUPGS7M%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCO9szqM7PaYMW98P07UWsdmxzpr%2F8d2XcuDwLv0oOztgIgbZaPcJOh9gppRSPAA6Xc1OD5e8YmxShJEuvgcsxuSnoq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDOheXCutzsrgh5V5BCrcA5iBtp0oh0A6uAfkabdffBHV4aM7zh6V88PhGRSSbTP%2B%2FLx9fB8whx7ghWVI6jqEtAYyJ27SB60Dzd1pV%2FzpW0cZoTMgtugtBzU9Iq1pREZD4mT0Fy%2Bs5%2BnbRm18B%2FMaVdCNVMQsEDiXsVUXHtALmCWp9jmuWR4udT5b9bi9g56Iw5XijgKYrOEHDcJL70p2HDzi8qWsCWofxlW0zxXjPNU3Ff1N%2FYJHugT1cQBPhtpNEIIoN2wgqcx%2FR6UnL4KlqcI%2BdS5ta1ATiUvfd%2BK%2F0FPtG%2BdG3m40T6uxy4PyxJhDpkddwZeZEgC2Ca%2FnXMsWFTqsguqJzxqQnoFhk7wl4LkPviquOlot8tyDZr%2BYr%2B8VZtZuM%2Fw1uzHOO7cHRvXL%2BQ5yTjuuvLfQH5HPyZHa8ipjybbkR23N2iF1Sxo%2BEvSNo65toUSyLJfKsIhWBIyJvODfLfyvbvZ9MZe%2FdobIw1Fu5NOo5pd%2BI4qDnnuxlwnbF0bgO0OQXjqJBgCfyOxbluq2C4yWcJmsNR%2BKBHppHTyKj7hlUqad1SYW7AbMH2HtZGN9WUTf%2BMOMqAu1KZ9y8E80teHrNH1kNo%2BGWmMQBODiYkrWZt7XSs9%2BYpNLrRhUwZqiz35y9yAVgbl8MLywickGOqUBFYdSML5ax%2FGspAVrt%2BiHigEfAOuIXOwraj%2BgEWQxbciN9GcksQ7uXxY6aitn%2F0RX7vpHCwM15tfYn2g%2BkSj8wbgc%2BOetc3YYBd63eS%2Fi%2FDYbEX8Gzj7AkcKqp79KfQjzihqFZB88UscVI5C5TvaB11QayQp0fBxEI2EMFGXE2T0BpAClH12n0L%2B9lIqltXoXswli9uEz%2BIz28vNhrt%2B3qRkPNNPR&X-Amz-Signature=3b64cbb3fe526175775152950bdeab9625b4352214febc80a3f883254155adbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXUPGS7M%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCO9szqM7PaYMW98P07UWsdmxzpr%2F8d2XcuDwLv0oOztgIgbZaPcJOh9gppRSPAA6Xc1OD5e8YmxShJEuvgcsxuSnoq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDOheXCutzsrgh5V5BCrcA5iBtp0oh0A6uAfkabdffBHV4aM7zh6V88PhGRSSbTP%2B%2FLx9fB8whx7ghWVI6jqEtAYyJ27SB60Dzd1pV%2FzpW0cZoTMgtugtBzU9Iq1pREZD4mT0Fy%2Bs5%2BnbRm18B%2FMaVdCNVMQsEDiXsVUXHtALmCWp9jmuWR4udT5b9bi9g56Iw5XijgKYrOEHDcJL70p2HDzi8qWsCWofxlW0zxXjPNU3Ff1N%2FYJHugT1cQBPhtpNEIIoN2wgqcx%2FR6UnL4KlqcI%2BdS5ta1ATiUvfd%2BK%2F0FPtG%2BdG3m40T6uxy4PyxJhDpkddwZeZEgC2Ca%2FnXMsWFTqsguqJzxqQnoFhk7wl4LkPviquOlot8tyDZr%2BYr%2B8VZtZuM%2Fw1uzHOO7cHRvXL%2BQ5yTjuuvLfQH5HPyZHa8ipjybbkR23N2iF1Sxo%2BEvSNo65toUSyLJfKsIhWBIyJvODfLfyvbvZ9MZe%2FdobIw1Fu5NOo5pd%2BI4qDnnuxlwnbF0bgO0OQXjqJBgCfyOxbluq2C4yWcJmsNR%2BKBHppHTyKj7hlUqad1SYW7AbMH2HtZGN9WUTf%2BMOMqAu1KZ9y8E80teHrNH1kNo%2BGWmMQBODiYkrWZt7XSs9%2BYpNLrRhUwZqiz35y9yAVgbl8MLywickGOqUBFYdSML5ax%2FGspAVrt%2BiHigEfAOuIXOwraj%2BgEWQxbciN9GcksQ7uXxY6aitn%2F0RX7vpHCwM15tfYn2g%2BkSj8wbgc%2BOetc3YYBd63eS%2Fi%2FDYbEX8Gzj7AkcKqp79KfQjzihqFZB88UscVI5C5TvaB11QayQp0fBxEI2EMFGXE2T0BpAClH12n0L%2B9lIqltXoXswli9uEz%2BIz28vNhrt%2B3qRkPNNPR&X-Amz-Signature=1e918fb5c288a25714ab80e97649233fe5a18984c2b3e1880853770a76b4ee72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



