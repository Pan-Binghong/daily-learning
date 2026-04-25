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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WQOAM74%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWVbYDFSS9TigthDL6xopI3hk1ErAfHwjYn92paZxuJwIgLNYL6UZ5WlG0R9A0OglW9lBDTwYrE%2BsIo5PW5n9atTkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIqQGcUohtngv%2FpGeyrcA%2BlTd9x0gzIAIAvLjc74EL8a%2FmeVN4axxxQ91esCAyVHMyPZ6PajAV%2Fi7xmnkfHWCh6UJu%2BIQUxJSe4IqNz7TBRlzAle1QeFqv6mHqmwufK3yaCBXZeKCGK9jHIXQwqfxa07Q%2BdUGbHDj7wHU7TKuQ%2BiI0kmtG2yId%2FHPeci6Ohm0aW%2Bo9mgfJWFjECXtye19aAq49%2FkgfRS3CBi%2Bl0BmAcjks5epo3bxB14CExbayHiuphy%2FxASZdZKfHWcnVXn9ZnpAIigCjmRInnaGRz%2FHkt%2BFECVXzVCIuyTbT4W2fYSF2NAhS%2BQKXevBwv9ee2Sruj1o4zYpDyudgWqhuCTlnTR5kBBkYWwslIuyasYM3WiJnG3da6qvW1zojhspbXJA8jJyEewr8R0G0u7d3%2FjgRe5HzVm8BuXHLzNlCSbrJj0ppWuwWyaFnyi0uFsHQ314CuE6MxyHtIGsSiouUIIw1eVegKs3Ao6N1HZyRIMz22jPYmUdSF%2FGhnQlc688weWy6mWvhiF4mDlcMJE3YMSL%2FJOKnCFSSw95gtcrvIKzJUnCsgedBi8iO3Hi8f%2B2Rq8UGxOoZ2YaCIDQJcxLx%2Bd%2F0TgUs%2FLDhw7Js9HzEwaAVxuE67kz9Cj0552kH4WMIXxsM8GOqUBlC4XXDR6k6vRJeDfTi748WFFZQsiB8a4eRUCl1SCme84fNQd02hmVl2CDO%2FUAfQTZgca9HTcwi%2Bz0%2Fyg8OOQqgl9m7%2F097QR6V%2FnaA0rnROIwimT8WRi%2FSTmYM70cNuo%2Be%2FQzRKxjDhJ%2BG3GKJuX65Iqj09RVSnTP79gPDplQacaPo7bO693Pi6XXMN3poof58tg9OvBSa5neqxMuI25V6mHjfwM&X-Amz-Signature=51a35674f745b1ad0407917dce122e3072f0c1d4b33b9992f07490eb9a716fa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WQOAM74%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWVbYDFSS9TigthDL6xopI3hk1ErAfHwjYn92paZxuJwIgLNYL6UZ5WlG0R9A0OglW9lBDTwYrE%2BsIo5PW5n9atTkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIqQGcUohtngv%2FpGeyrcA%2BlTd9x0gzIAIAvLjc74EL8a%2FmeVN4axxxQ91esCAyVHMyPZ6PajAV%2Fi7xmnkfHWCh6UJu%2BIQUxJSe4IqNz7TBRlzAle1QeFqv6mHqmwufK3yaCBXZeKCGK9jHIXQwqfxa07Q%2BdUGbHDj7wHU7TKuQ%2BiI0kmtG2yId%2FHPeci6Ohm0aW%2Bo9mgfJWFjECXtye19aAq49%2FkgfRS3CBi%2Bl0BmAcjks5epo3bxB14CExbayHiuphy%2FxASZdZKfHWcnVXn9ZnpAIigCjmRInnaGRz%2FHkt%2BFECVXzVCIuyTbT4W2fYSF2NAhS%2BQKXevBwv9ee2Sruj1o4zYpDyudgWqhuCTlnTR5kBBkYWwslIuyasYM3WiJnG3da6qvW1zojhspbXJA8jJyEewr8R0G0u7d3%2FjgRe5HzVm8BuXHLzNlCSbrJj0ppWuwWyaFnyi0uFsHQ314CuE6MxyHtIGsSiouUIIw1eVegKs3Ao6N1HZyRIMz22jPYmUdSF%2FGhnQlc688weWy6mWvhiF4mDlcMJE3YMSL%2FJOKnCFSSw95gtcrvIKzJUnCsgedBi8iO3Hi8f%2B2Rq8UGxOoZ2YaCIDQJcxLx%2Bd%2F0TgUs%2FLDhw7Js9HzEwaAVxuE67kz9Cj0552kH4WMIXxsM8GOqUBlC4XXDR6k6vRJeDfTi748WFFZQsiB8a4eRUCl1SCme84fNQd02hmVl2CDO%2FUAfQTZgca9HTcwi%2Bz0%2Fyg8OOQqgl9m7%2F097QR6V%2FnaA0rnROIwimT8WRi%2FSTmYM70cNuo%2Be%2FQzRKxjDhJ%2BG3GKJuX65Iqj09RVSnTP79gPDplQacaPo7bO693Pi6XXMN3poof58tg9OvBSa5neqxMuI25V6mHjfwM&X-Amz-Signature=a2091a20ff8f189320fa7cc3f7aff1ff5ad770d0f6b4615983cdbc94bd40b09a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WQOAM74%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWVbYDFSS9TigthDL6xopI3hk1ErAfHwjYn92paZxuJwIgLNYL6UZ5WlG0R9A0OglW9lBDTwYrE%2BsIo5PW5n9atTkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIqQGcUohtngv%2FpGeyrcA%2BlTd9x0gzIAIAvLjc74EL8a%2FmeVN4axxxQ91esCAyVHMyPZ6PajAV%2Fi7xmnkfHWCh6UJu%2BIQUxJSe4IqNz7TBRlzAle1QeFqv6mHqmwufK3yaCBXZeKCGK9jHIXQwqfxa07Q%2BdUGbHDj7wHU7TKuQ%2BiI0kmtG2yId%2FHPeci6Ohm0aW%2Bo9mgfJWFjECXtye19aAq49%2FkgfRS3CBi%2Bl0BmAcjks5epo3bxB14CExbayHiuphy%2FxASZdZKfHWcnVXn9ZnpAIigCjmRInnaGRz%2FHkt%2BFECVXzVCIuyTbT4W2fYSF2NAhS%2BQKXevBwv9ee2Sruj1o4zYpDyudgWqhuCTlnTR5kBBkYWwslIuyasYM3WiJnG3da6qvW1zojhspbXJA8jJyEewr8R0G0u7d3%2FjgRe5HzVm8BuXHLzNlCSbrJj0ppWuwWyaFnyi0uFsHQ314CuE6MxyHtIGsSiouUIIw1eVegKs3Ao6N1HZyRIMz22jPYmUdSF%2FGhnQlc688weWy6mWvhiF4mDlcMJE3YMSL%2FJOKnCFSSw95gtcrvIKzJUnCsgedBi8iO3Hi8f%2B2Rq8UGxOoZ2YaCIDQJcxLx%2Bd%2F0TgUs%2FLDhw7Js9HzEwaAVxuE67kz9Cj0552kH4WMIXxsM8GOqUBlC4XXDR6k6vRJeDfTi748WFFZQsiB8a4eRUCl1SCme84fNQd02hmVl2CDO%2FUAfQTZgca9HTcwi%2Bz0%2Fyg8OOQqgl9m7%2F097QR6V%2FnaA0rnROIwimT8WRi%2FSTmYM70cNuo%2Be%2FQzRKxjDhJ%2BG3GKJuX65Iqj09RVSnTP79gPDplQacaPo7bO693Pi6XXMN3poof58tg9OvBSa5neqxMuI25V6mHjfwM&X-Amz-Signature=e814bee048e63da87f515cc898f14a28f5c68c118ef9bcae7fdf49de62d7fddc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WQOAM74%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWVbYDFSS9TigthDL6xopI3hk1ErAfHwjYn92paZxuJwIgLNYL6UZ5WlG0R9A0OglW9lBDTwYrE%2BsIo5PW5n9atTkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIqQGcUohtngv%2FpGeyrcA%2BlTd9x0gzIAIAvLjc74EL8a%2FmeVN4axxxQ91esCAyVHMyPZ6PajAV%2Fi7xmnkfHWCh6UJu%2BIQUxJSe4IqNz7TBRlzAle1QeFqv6mHqmwufK3yaCBXZeKCGK9jHIXQwqfxa07Q%2BdUGbHDj7wHU7TKuQ%2BiI0kmtG2yId%2FHPeci6Ohm0aW%2Bo9mgfJWFjECXtye19aAq49%2FkgfRS3CBi%2Bl0BmAcjks5epo3bxB14CExbayHiuphy%2FxASZdZKfHWcnVXn9ZnpAIigCjmRInnaGRz%2FHkt%2BFECVXzVCIuyTbT4W2fYSF2NAhS%2BQKXevBwv9ee2Sruj1o4zYpDyudgWqhuCTlnTR5kBBkYWwslIuyasYM3WiJnG3da6qvW1zojhspbXJA8jJyEewr8R0G0u7d3%2FjgRe5HzVm8BuXHLzNlCSbrJj0ppWuwWyaFnyi0uFsHQ314CuE6MxyHtIGsSiouUIIw1eVegKs3Ao6N1HZyRIMz22jPYmUdSF%2FGhnQlc688weWy6mWvhiF4mDlcMJE3YMSL%2FJOKnCFSSw95gtcrvIKzJUnCsgedBi8iO3Hi8f%2B2Rq8UGxOoZ2YaCIDQJcxLx%2Bd%2F0TgUs%2FLDhw7Js9HzEwaAVxuE67kz9Cj0552kH4WMIXxsM8GOqUBlC4XXDR6k6vRJeDfTi748WFFZQsiB8a4eRUCl1SCme84fNQd02hmVl2CDO%2FUAfQTZgca9HTcwi%2Bz0%2Fyg8OOQqgl9m7%2F097QR6V%2FnaA0rnROIwimT8WRi%2FSTmYM70cNuo%2Be%2FQzRKxjDhJ%2BG3GKJuX65Iqj09RVSnTP79gPDplQacaPo7bO693Pi6XXMN3poof58tg9OvBSa5neqxMuI25V6mHjfwM&X-Amz-Signature=e46b7bdc60f0a8cd0763c49d9873ddff20da932dc3ad907781b836761bda5dd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



