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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P7CWB25%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIA%2Bow4xIw4NIC6%2Fytn5RSjk4H5hGY%2BBdo8%2BkTcjBCEZUAiBtiCYyQdpNMCqGzlPxAOuodB4kTU%2BDOlFSjaZr48fh%2FiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl8%2F%2FnMiekVptjgzpKtwDB0bgw%2BW3%2FlCoNgAYQ9BFMjp7kfCF7dbkYVYr%2Bp9P%2B9Qb06s1FBXjo101B%2Bs0A%2B91fWIpVmFCF%2FJyiyjtylRUrbRXRGELR22OcgTUP6tJcbZcC8Lbjp95QQnVUnzdI2PDj6uWCRrDfAkcWsquNo5YHadGSCS3z27j7dLHHnzl9oxOn%2FO7PboEWdEaUQoiJFzgf3MAIf%2BMMblXkiuelGYnf%2B8TdZ9Ll1rsA5flzyVxHYT0zBQovIWWqWIihg5ftNU3zjHwNV2DJlG5HbhxNPTVqmNWy8RFHlEs5y7%2FevNEkUqkOwovw5KLNpaj37OE03fxuqF1UcMkSg2CYMct6nuCDLicSwJCMRXRFqyxVPpiX9W%2FEQpX45tuT7J%2Fx7k%2BmZX4H8C50bolDDmstHmorVXAsntbczesLCA0T8Z3PBFCUS4gbxzHQlkaTaRSYdvdGIFf0CMaMLMmgb6pho5G7mz4crJmr29lvWIjBBFDh5i2isQxf%2FQ2khijCdXACj7vglrw9FO%2FaargMknc3%2B8Pjm6iqLpSLLFoDjYWFz49CDgHh4QTb0Ylmxy3dCITy%2FvIUy9qhA0wh8w1S%2FkwTgIA1OI7UYIoLByY%2F9x%2B98pPmd5I1VXxV29c%2BKqtIDRqFBYwtNjFywY6pgEbrV%2Bp0uvrjgfB6yRYjdmRG1H44Go3b6o%2FlDIuOGjIzyeKiRF0QHqB2OEwqFIRkr1oHR%2BO%2F%2FKCh4fEyqY2Uz9%2FL7FnKvOMFluRYPATiGnBwP2F3SU4EDlK0RBkJOkLFc4Rm%2BCEFeJrmkhA8tDQrkdytwz4uUjrmt1flK3GQ8GeEQHbVM5zU9bv5iF%2B%2BWx0gA7kTvaTIOqDT1vDVqYHIO5DBlQmxnPG&X-Amz-Signature=2042e67a47324097a90e3a7a50c6fea0c0d3a4685f244509f21783b085ff518b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P7CWB25%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIA%2Bow4xIw4NIC6%2Fytn5RSjk4H5hGY%2BBdo8%2BkTcjBCEZUAiBtiCYyQdpNMCqGzlPxAOuodB4kTU%2BDOlFSjaZr48fh%2FiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl8%2F%2FnMiekVptjgzpKtwDB0bgw%2BW3%2FlCoNgAYQ9BFMjp7kfCF7dbkYVYr%2Bp9P%2B9Qb06s1FBXjo101B%2Bs0A%2B91fWIpVmFCF%2FJyiyjtylRUrbRXRGELR22OcgTUP6tJcbZcC8Lbjp95QQnVUnzdI2PDj6uWCRrDfAkcWsquNo5YHadGSCS3z27j7dLHHnzl9oxOn%2FO7PboEWdEaUQoiJFzgf3MAIf%2BMMblXkiuelGYnf%2B8TdZ9Ll1rsA5flzyVxHYT0zBQovIWWqWIihg5ftNU3zjHwNV2DJlG5HbhxNPTVqmNWy8RFHlEs5y7%2FevNEkUqkOwovw5KLNpaj37OE03fxuqF1UcMkSg2CYMct6nuCDLicSwJCMRXRFqyxVPpiX9W%2FEQpX45tuT7J%2Fx7k%2BmZX4H8C50bolDDmstHmorVXAsntbczesLCA0T8Z3PBFCUS4gbxzHQlkaTaRSYdvdGIFf0CMaMLMmgb6pho5G7mz4crJmr29lvWIjBBFDh5i2isQxf%2FQ2khijCdXACj7vglrw9FO%2FaargMknc3%2B8Pjm6iqLpSLLFoDjYWFz49CDgHh4QTb0Ylmxy3dCITy%2FvIUy9qhA0wh8w1S%2FkwTgIA1OI7UYIoLByY%2F9x%2B98pPmd5I1VXxV29c%2BKqtIDRqFBYwtNjFywY6pgEbrV%2Bp0uvrjgfB6yRYjdmRG1H44Go3b6o%2FlDIuOGjIzyeKiRF0QHqB2OEwqFIRkr1oHR%2BO%2F%2FKCh4fEyqY2Uz9%2FL7FnKvOMFluRYPATiGnBwP2F3SU4EDlK0RBkJOkLFc4Rm%2BCEFeJrmkhA8tDQrkdytwz4uUjrmt1flK3GQ8GeEQHbVM5zU9bv5iF%2B%2BWx0gA7kTvaTIOqDT1vDVqYHIO5DBlQmxnPG&X-Amz-Signature=7e7f31e3134aeaa800be921ab7fa3d8ed28eb7d93f990272ded5fb08bab495d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P7CWB25%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIA%2Bow4xIw4NIC6%2Fytn5RSjk4H5hGY%2BBdo8%2BkTcjBCEZUAiBtiCYyQdpNMCqGzlPxAOuodB4kTU%2BDOlFSjaZr48fh%2FiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl8%2F%2FnMiekVptjgzpKtwDB0bgw%2BW3%2FlCoNgAYQ9BFMjp7kfCF7dbkYVYr%2Bp9P%2B9Qb06s1FBXjo101B%2Bs0A%2B91fWIpVmFCF%2FJyiyjtylRUrbRXRGELR22OcgTUP6tJcbZcC8Lbjp95QQnVUnzdI2PDj6uWCRrDfAkcWsquNo5YHadGSCS3z27j7dLHHnzl9oxOn%2FO7PboEWdEaUQoiJFzgf3MAIf%2BMMblXkiuelGYnf%2B8TdZ9Ll1rsA5flzyVxHYT0zBQovIWWqWIihg5ftNU3zjHwNV2DJlG5HbhxNPTVqmNWy8RFHlEs5y7%2FevNEkUqkOwovw5KLNpaj37OE03fxuqF1UcMkSg2CYMct6nuCDLicSwJCMRXRFqyxVPpiX9W%2FEQpX45tuT7J%2Fx7k%2BmZX4H8C50bolDDmstHmorVXAsntbczesLCA0T8Z3PBFCUS4gbxzHQlkaTaRSYdvdGIFf0CMaMLMmgb6pho5G7mz4crJmr29lvWIjBBFDh5i2isQxf%2FQ2khijCdXACj7vglrw9FO%2FaargMknc3%2B8Pjm6iqLpSLLFoDjYWFz49CDgHh4QTb0Ylmxy3dCITy%2FvIUy9qhA0wh8w1S%2FkwTgIA1OI7UYIoLByY%2F9x%2B98pPmd5I1VXxV29c%2BKqtIDRqFBYwtNjFywY6pgEbrV%2Bp0uvrjgfB6yRYjdmRG1H44Go3b6o%2FlDIuOGjIzyeKiRF0QHqB2OEwqFIRkr1oHR%2BO%2F%2FKCh4fEyqY2Uz9%2FL7FnKvOMFluRYPATiGnBwP2F3SU4EDlK0RBkJOkLFc4Rm%2BCEFeJrmkhA8tDQrkdytwz4uUjrmt1flK3GQ8GeEQHbVM5zU9bv5iF%2B%2BWx0gA7kTvaTIOqDT1vDVqYHIO5DBlQmxnPG&X-Amz-Signature=9bc211fc8de29028c0ff90c3b85260c9eba914c0abf0299cf35423bcba7854ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663P7CWB25%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIA%2Bow4xIw4NIC6%2Fytn5RSjk4H5hGY%2BBdo8%2BkTcjBCEZUAiBtiCYyQdpNMCqGzlPxAOuodB4kTU%2BDOlFSjaZr48fh%2FiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl8%2F%2FnMiekVptjgzpKtwDB0bgw%2BW3%2FlCoNgAYQ9BFMjp7kfCF7dbkYVYr%2Bp9P%2B9Qb06s1FBXjo101B%2Bs0A%2B91fWIpVmFCF%2FJyiyjtylRUrbRXRGELR22OcgTUP6tJcbZcC8Lbjp95QQnVUnzdI2PDj6uWCRrDfAkcWsquNo5YHadGSCS3z27j7dLHHnzl9oxOn%2FO7PboEWdEaUQoiJFzgf3MAIf%2BMMblXkiuelGYnf%2B8TdZ9Ll1rsA5flzyVxHYT0zBQovIWWqWIihg5ftNU3zjHwNV2DJlG5HbhxNPTVqmNWy8RFHlEs5y7%2FevNEkUqkOwovw5KLNpaj37OE03fxuqF1UcMkSg2CYMct6nuCDLicSwJCMRXRFqyxVPpiX9W%2FEQpX45tuT7J%2Fx7k%2BmZX4H8C50bolDDmstHmorVXAsntbczesLCA0T8Z3PBFCUS4gbxzHQlkaTaRSYdvdGIFf0CMaMLMmgb6pho5G7mz4crJmr29lvWIjBBFDh5i2isQxf%2FQ2khijCdXACj7vglrw9FO%2FaargMknc3%2B8Pjm6iqLpSLLFoDjYWFz49CDgHh4QTb0Ylmxy3dCITy%2FvIUy9qhA0wh8w1S%2FkwTgIA1OI7UYIoLByY%2F9x%2B98pPmd5I1VXxV29c%2BKqtIDRqFBYwtNjFywY6pgEbrV%2Bp0uvrjgfB6yRYjdmRG1H44Go3b6o%2FlDIuOGjIzyeKiRF0QHqB2OEwqFIRkr1oHR%2BO%2F%2FKCh4fEyqY2Uz9%2FL7FnKvOMFluRYPATiGnBwP2F3SU4EDlK0RBkJOkLFc4Rm%2BCEFeJrmkhA8tDQrkdytwz4uUjrmt1flK3GQ8GeEQHbVM5zU9bv5iF%2B%2BWx0gA7kTvaTIOqDT1vDVqYHIO5DBlQmxnPG&X-Amz-Signature=29e942b76e75da23229057686db10da59a520719e69db2ab86932ac4db4fbafa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



