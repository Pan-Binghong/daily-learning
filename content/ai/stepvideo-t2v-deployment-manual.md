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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMR4NVVA%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBbUSxx0WkH6xfNq1wve6W%2F0V%2BpeB2DRiTiX9HIzCmZsAiAO8S4BD2YI87VXIzgt5aSZoupMUDQ16UMod1bAaRrO6yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMJIRzedIfEwY2bFmuKtwDpe0uHvr06cNqrBhf4geIvypUMeWBqF5gz2iu9wXQ1JJ99RTsJQ6FUjl6fSfA01dz6PP0gwhcEWyZI08G%2FUBMYBQWty10xIyQDwodoBoieS8xBek9uUvB9va0U3upyJmoK2aFI0QO1sHRbdKqyElhJm7mhKV3g5Kc%2FWSZBFg8lg9pjaQF14SWaYr6wwSIecVI8hkc4uJouc%2FijNWp86KIm%2FNjly9PX3uFZ1N8HkyPCEVgC2R2KjWpBRFlUFf0NWykqvYLaXM5Uhx7OlKoumaCvgPT6Jo%2FkdwBR%2BxnDw2IEW0iDDo%2FirjmFhL2QNkhepXfhkeP1Yb4wdFdenx8KJO11ynLXKfPJQoNhj14s9mNOFHWFdnLX8hUuc8K%2BOeDvjnjQ9Y%2BizGHP28HCBZSYr37LzDBHGwewDgDtJKhDxxA0EgXYESSCF%2BEtLHTQeKZWuoRhlE0Ki6TYRu7LHjjrA6p43oFdCW8EL88R8qJcTy%2BRwZz6SALGWTY154hveWPJHDFdNam0cAYHo2o1KwrSuihUetw8gtJw7DU6t5Invm0shs1FrMhEyXnztp%2B3wfCQDXVGD1dgb4vszgrgDdzlPlalmPfPVTA9xSXdc1eYfvCy%2BSYOMdjp4I1U7Vh9qMw4OCsygY6pgEvAATr9E%2BfEOEuJHfP5mdbvzy5zO%2F3xY91cGYtqSHbR3UDdM9XCLGhN4gYfzOTqEB9oWsJmd6E01Mwss8T84VYzxoGZDTl5PsPqa6aUhSdf2tq6zpLXJ0c8cECNEBbgkD9kViMCwZY6td%2Fxu5e3AIf5Z2%2Fj8hk4YDA%2FtVSVW3pNtcz7XeOyj0SAkRTbzlxqfX7ax4D5etA4PDucpnqJqM7LmaElszB&X-Amz-Signature=a2bf3c7b40421d80724e7bf3183ecdc89f32dd258eee3939607aa78821e70376&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMR4NVVA%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBbUSxx0WkH6xfNq1wve6W%2F0V%2BpeB2DRiTiX9HIzCmZsAiAO8S4BD2YI87VXIzgt5aSZoupMUDQ16UMod1bAaRrO6yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMJIRzedIfEwY2bFmuKtwDpe0uHvr06cNqrBhf4geIvypUMeWBqF5gz2iu9wXQ1JJ99RTsJQ6FUjl6fSfA01dz6PP0gwhcEWyZI08G%2FUBMYBQWty10xIyQDwodoBoieS8xBek9uUvB9va0U3upyJmoK2aFI0QO1sHRbdKqyElhJm7mhKV3g5Kc%2FWSZBFg8lg9pjaQF14SWaYr6wwSIecVI8hkc4uJouc%2FijNWp86KIm%2FNjly9PX3uFZ1N8HkyPCEVgC2R2KjWpBRFlUFf0NWykqvYLaXM5Uhx7OlKoumaCvgPT6Jo%2FkdwBR%2BxnDw2IEW0iDDo%2FirjmFhL2QNkhepXfhkeP1Yb4wdFdenx8KJO11ynLXKfPJQoNhj14s9mNOFHWFdnLX8hUuc8K%2BOeDvjnjQ9Y%2BizGHP28HCBZSYr37LzDBHGwewDgDtJKhDxxA0EgXYESSCF%2BEtLHTQeKZWuoRhlE0Ki6TYRu7LHjjrA6p43oFdCW8EL88R8qJcTy%2BRwZz6SALGWTY154hveWPJHDFdNam0cAYHo2o1KwrSuihUetw8gtJw7DU6t5Invm0shs1FrMhEyXnztp%2B3wfCQDXVGD1dgb4vszgrgDdzlPlalmPfPVTA9xSXdc1eYfvCy%2BSYOMdjp4I1U7Vh9qMw4OCsygY6pgEvAATr9E%2BfEOEuJHfP5mdbvzy5zO%2F3xY91cGYtqSHbR3UDdM9XCLGhN4gYfzOTqEB9oWsJmd6E01Mwss8T84VYzxoGZDTl5PsPqa6aUhSdf2tq6zpLXJ0c8cECNEBbgkD9kViMCwZY6td%2Fxu5e3AIf5Z2%2Fj8hk4YDA%2FtVSVW3pNtcz7XeOyj0SAkRTbzlxqfX7ax4D5etA4PDucpnqJqM7LmaElszB&X-Amz-Signature=90ca373f7d6642ded6e79d5aada37edfe04a316ebaad766e02e200c18aa55f7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMR4NVVA%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBbUSxx0WkH6xfNq1wve6W%2F0V%2BpeB2DRiTiX9HIzCmZsAiAO8S4BD2YI87VXIzgt5aSZoupMUDQ16UMod1bAaRrO6yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMJIRzedIfEwY2bFmuKtwDpe0uHvr06cNqrBhf4geIvypUMeWBqF5gz2iu9wXQ1JJ99RTsJQ6FUjl6fSfA01dz6PP0gwhcEWyZI08G%2FUBMYBQWty10xIyQDwodoBoieS8xBek9uUvB9va0U3upyJmoK2aFI0QO1sHRbdKqyElhJm7mhKV3g5Kc%2FWSZBFg8lg9pjaQF14SWaYr6wwSIecVI8hkc4uJouc%2FijNWp86KIm%2FNjly9PX3uFZ1N8HkyPCEVgC2R2KjWpBRFlUFf0NWykqvYLaXM5Uhx7OlKoumaCvgPT6Jo%2FkdwBR%2BxnDw2IEW0iDDo%2FirjmFhL2QNkhepXfhkeP1Yb4wdFdenx8KJO11ynLXKfPJQoNhj14s9mNOFHWFdnLX8hUuc8K%2BOeDvjnjQ9Y%2BizGHP28HCBZSYr37LzDBHGwewDgDtJKhDxxA0EgXYESSCF%2BEtLHTQeKZWuoRhlE0Ki6TYRu7LHjjrA6p43oFdCW8EL88R8qJcTy%2BRwZz6SALGWTY154hveWPJHDFdNam0cAYHo2o1KwrSuihUetw8gtJw7DU6t5Invm0shs1FrMhEyXnztp%2B3wfCQDXVGD1dgb4vszgrgDdzlPlalmPfPVTA9xSXdc1eYfvCy%2BSYOMdjp4I1U7Vh9qMw4OCsygY6pgEvAATr9E%2BfEOEuJHfP5mdbvzy5zO%2F3xY91cGYtqSHbR3UDdM9XCLGhN4gYfzOTqEB9oWsJmd6E01Mwss8T84VYzxoGZDTl5PsPqa6aUhSdf2tq6zpLXJ0c8cECNEBbgkD9kViMCwZY6td%2Fxu5e3AIf5Z2%2Fj8hk4YDA%2FtVSVW3pNtcz7XeOyj0SAkRTbzlxqfX7ax4D5etA4PDucpnqJqM7LmaElszB&X-Amz-Signature=98ae40fff80263ad36fc1e2d24b30ca2bcd9836bdc287186265e70e70ffdacdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMR4NVVA%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBbUSxx0WkH6xfNq1wve6W%2F0V%2BpeB2DRiTiX9HIzCmZsAiAO8S4BD2YI87VXIzgt5aSZoupMUDQ16UMod1bAaRrO6yr%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMJIRzedIfEwY2bFmuKtwDpe0uHvr06cNqrBhf4geIvypUMeWBqF5gz2iu9wXQ1JJ99RTsJQ6FUjl6fSfA01dz6PP0gwhcEWyZI08G%2FUBMYBQWty10xIyQDwodoBoieS8xBek9uUvB9va0U3upyJmoK2aFI0QO1sHRbdKqyElhJm7mhKV3g5Kc%2FWSZBFg8lg9pjaQF14SWaYr6wwSIecVI8hkc4uJouc%2FijNWp86KIm%2FNjly9PX3uFZ1N8HkyPCEVgC2R2KjWpBRFlUFf0NWykqvYLaXM5Uhx7OlKoumaCvgPT6Jo%2FkdwBR%2BxnDw2IEW0iDDo%2FirjmFhL2QNkhepXfhkeP1Yb4wdFdenx8KJO11ynLXKfPJQoNhj14s9mNOFHWFdnLX8hUuc8K%2BOeDvjnjQ9Y%2BizGHP28HCBZSYr37LzDBHGwewDgDtJKhDxxA0EgXYESSCF%2BEtLHTQeKZWuoRhlE0Ki6TYRu7LHjjrA6p43oFdCW8EL88R8qJcTy%2BRwZz6SALGWTY154hveWPJHDFdNam0cAYHo2o1KwrSuihUetw8gtJw7DU6t5Invm0shs1FrMhEyXnztp%2B3wfCQDXVGD1dgb4vszgrgDdzlPlalmPfPVTA9xSXdc1eYfvCy%2BSYOMdjp4I1U7Vh9qMw4OCsygY6pgEvAATr9E%2BfEOEuJHfP5mdbvzy5zO%2F3xY91cGYtqSHbR3UDdM9XCLGhN4gYfzOTqEB9oWsJmd6E01Mwss8T84VYzxoGZDTl5PsPqa6aUhSdf2tq6zpLXJ0c8cECNEBbgkD9kViMCwZY6td%2Fxu5e3AIf5Z2%2Fj8hk4YDA%2FtVSVW3pNtcz7XeOyj0SAkRTbzlxqfX7ax4D5etA4PDucpnqJqM7LmaElszB&X-Amz-Signature=947d61ab81fc9f6aa7e0dcd875cafe2a51937decfb9a40a2048fd605f0bf9163&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



