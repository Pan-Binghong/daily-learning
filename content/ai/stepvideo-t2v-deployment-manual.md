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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVY5EIE%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCICgScfDAtIVTjUAIYC6hyesY5%2BO3yE3xCQKsF5HALBRPAiA87SVGUV%2FJl9HGumrSGTLvbL0NGwDjV2bGQM0iew%2BRlCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMWCDTW9Amfgt65RAOKtwDGJRb2VKNy9Vbx%2FGVGMA7cS%2BLY9oEXBazU8S0eFoV38NAxjm%2BpVEIIUG5vnRWqJNYHDrOhIxJ%2B3ALO4a9pT2DTjsjTyRFKz7ORYnMWWOCxlnEMFl569sOPY1Ch4StIcEtNRgjuT67YsS4XQeO3ZidA0PSK2hP37o6vaE5rlL8UIuxqf1Fc0FHkU1fZzqg8ROxA%2BQP0wcBXXYM9uDJf8cDOeetYAnpu7COCmakI42D6U4r9D5%2FHajqKF5Sq2QBNnXytzWhlz2Fr3YAgtJul6cYlSPqcDj2hMOALPiTxo%2FLMx7pGkqGBz%2FqF7KyMBcn%2F7OssQZF%2Bcqiz4omfmDtsbl3BN1VM51CTWci8%2BlI7tl6jN5%2F%2BK%2BCr%2F0Bsn5FZuPXR572PyXNwjVaP3OSbp9NMvFY2ftAGClluBBsRNBrDErLaDpaVV%2B0P1XBzTcMQCXYumj%2BeLR%2BJno0q4hwjtF2FAtbhGDtVxjLXkHIICK5%2BIZ400wDMEYDC7uOQVn%2Bd4DBdRb24xBqw0vwCdLnpFRuO0UNljkcNIs7bSQNNsbzLQZCOxEs8J0bLY4BzpYyT0syeCQ0N00zOv%2Fibuz3bzoZxBzbOibFc2fdErlaoMJz%2Fd6YKkqArQjOU0PXlSHoHfIwk%2FX%2BzAY6pgFL3knirXgIdZ5%2F5Ni51y28w2Lw2EtPDj%2FCQD7DLyuVS9sLEVFF8zuiy4f6clNVngAAI7dXNjauqB8yhMWDPivzH9m%2Bb0mMCd%2Fhmpzvd83pY6YeiFDQGXlEhcB2R4tsgZUxQ57h%2FtfjXAeDmVLce6s%2BAmSIKZJnABti4YU9BDR5DZSULdb6HbkC7%2BxEFQaqU7gWjxyMD2uA1Atp7cuAS5M3s5XmurIQ&X-Amz-Signature=2516b85edff6b9366bda0975245f0895b912fd86829e04916e1d5adffc4fd983&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVY5EIE%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCICgScfDAtIVTjUAIYC6hyesY5%2BO3yE3xCQKsF5HALBRPAiA87SVGUV%2FJl9HGumrSGTLvbL0NGwDjV2bGQM0iew%2BRlCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMWCDTW9Amfgt65RAOKtwDGJRb2VKNy9Vbx%2FGVGMA7cS%2BLY9oEXBazU8S0eFoV38NAxjm%2BpVEIIUG5vnRWqJNYHDrOhIxJ%2B3ALO4a9pT2DTjsjTyRFKz7ORYnMWWOCxlnEMFl569sOPY1Ch4StIcEtNRgjuT67YsS4XQeO3ZidA0PSK2hP37o6vaE5rlL8UIuxqf1Fc0FHkU1fZzqg8ROxA%2BQP0wcBXXYM9uDJf8cDOeetYAnpu7COCmakI42D6U4r9D5%2FHajqKF5Sq2QBNnXytzWhlz2Fr3YAgtJul6cYlSPqcDj2hMOALPiTxo%2FLMx7pGkqGBz%2FqF7KyMBcn%2F7OssQZF%2Bcqiz4omfmDtsbl3BN1VM51CTWci8%2BlI7tl6jN5%2F%2BK%2BCr%2F0Bsn5FZuPXR572PyXNwjVaP3OSbp9NMvFY2ftAGClluBBsRNBrDErLaDpaVV%2B0P1XBzTcMQCXYumj%2BeLR%2BJno0q4hwjtF2FAtbhGDtVxjLXkHIICK5%2BIZ400wDMEYDC7uOQVn%2Bd4DBdRb24xBqw0vwCdLnpFRuO0UNljkcNIs7bSQNNsbzLQZCOxEs8J0bLY4BzpYyT0syeCQ0N00zOv%2Fibuz3bzoZxBzbOibFc2fdErlaoMJz%2Fd6YKkqArQjOU0PXlSHoHfIwk%2FX%2BzAY6pgFL3knirXgIdZ5%2F5Ni51y28w2Lw2EtPDj%2FCQD7DLyuVS9sLEVFF8zuiy4f6clNVngAAI7dXNjauqB8yhMWDPivzH9m%2Bb0mMCd%2Fhmpzvd83pY6YeiFDQGXlEhcB2R4tsgZUxQ57h%2FtfjXAeDmVLce6s%2BAmSIKZJnABti4YU9BDR5DZSULdb6HbkC7%2BxEFQaqU7gWjxyMD2uA1Atp7cuAS5M3s5XmurIQ&X-Amz-Signature=d7803febb96ce46a984221dc26eef4a8aec144d85ff2be439cae676a1d4e76eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVY5EIE%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCICgScfDAtIVTjUAIYC6hyesY5%2BO3yE3xCQKsF5HALBRPAiA87SVGUV%2FJl9HGumrSGTLvbL0NGwDjV2bGQM0iew%2BRlCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMWCDTW9Amfgt65RAOKtwDGJRb2VKNy9Vbx%2FGVGMA7cS%2BLY9oEXBazU8S0eFoV38NAxjm%2BpVEIIUG5vnRWqJNYHDrOhIxJ%2B3ALO4a9pT2DTjsjTyRFKz7ORYnMWWOCxlnEMFl569sOPY1Ch4StIcEtNRgjuT67YsS4XQeO3ZidA0PSK2hP37o6vaE5rlL8UIuxqf1Fc0FHkU1fZzqg8ROxA%2BQP0wcBXXYM9uDJf8cDOeetYAnpu7COCmakI42D6U4r9D5%2FHajqKF5Sq2QBNnXytzWhlz2Fr3YAgtJul6cYlSPqcDj2hMOALPiTxo%2FLMx7pGkqGBz%2FqF7KyMBcn%2F7OssQZF%2Bcqiz4omfmDtsbl3BN1VM51CTWci8%2BlI7tl6jN5%2F%2BK%2BCr%2F0Bsn5FZuPXR572PyXNwjVaP3OSbp9NMvFY2ftAGClluBBsRNBrDErLaDpaVV%2B0P1XBzTcMQCXYumj%2BeLR%2BJno0q4hwjtF2FAtbhGDtVxjLXkHIICK5%2BIZ400wDMEYDC7uOQVn%2Bd4DBdRb24xBqw0vwCdLnpFRuO0UNljkcNIs7bSQNNsbzLQZCOxEs8J0bLY4BzpYyT0syeCQ0N00zOv%2Fibuz3bzoZxBzbOibFc2fdErlaoMJz%2Fd6YKkqArQjOU0PXlSHoHfIwk%2FX%2BzAY6pgFL3knirXgIdZ5%2F5Ni51y28w2Lw2EtPDj%2FCQD7DLyuVS9sLEVFF8zuiy4f6clNVngAAI7dXNjauqB8yhMWDPivzH9m%2Bb0mMCd%2Fhmpzvd83pY6YeiFDQGXlEhcB2R4tsgZUxQ57h%2FtfjXAeDmVLce6s%2BAmSIKZJnABti4YU9BDR5DZSULdb6HbkC7%2BxEFQaqU7gWjxyMD2uA1Atp7cuAS5M3s5XmurIQ&X-Amz-Signature=989eca331776d0526d0a879dc624f937f583f80d4fdfd821a618006534e8ab27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUVY5EIE%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCICgScfDAtIVTjUAIYC6hyesY5%2BO3yE3xCQKsF5HALBRPAiA87SVGUV%2FJl9HGumrSGTLvbL0NGwDjV2bGQM0iew%2BRlCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMWCDTW9Amfgt65RAOKtwDGJRb2VKNy9Vbx%2FGVGMA7cS%2BLY9oEXBazU8S0eFoV38NAxjm%2BpVEIIUG5vnRWqJNYHDrOhIxJ%2B3ALO4a9pT2DTjsjTyRFKz7ORYnMWWOCxlnEMFl569sOPY1Ch4StIcEtNRgjuT67YsS4XQeO3ZidA0PSK2hP37o6vaE5rlL8UIuxqf1Fc0FHkU1fZzqg8ROxA%2BQP0wcBXXYM9uDJf8cDOeetYAnpu7COCmakI42D6U4r9D5%2FHajqKF5Sq2QBNnXytzWhlz2Fr3YAgtJul6cYlSPqcDj2hMOALPiTxo%2FLMx7pGkqGBz%2FqF7KyMBcn%2F7OssQZF%2Bcqiz4omfmDtsbl3BN1VM51CTWci8%2BlI7tl6jN5%2F%2BK%2BCr%2F0Bsn5FZuPXR572PyXNwjVaP3OSbp9NMvFY2ftAGClluBBsRNBrDErLaDpaVV%2B0P1XBzTcMQCXYumj%2BeLR%2BJno0q4hwjtF2FAtbhGDtVxjLXkHIICK5%2BIZ400wDMEYDC7uOQVn%2Bd4DBdRb24xBqw0vwCdLnpFRuO0UNljkcNIs7bSQNNsbzLQZCOxEs8J0bLY4BzpYyT0syeCQ0N00zOv%2Fibuz3bzoZxBzbOibFc2fdErlaoMJz%2Fd6YKkqArQjOU0PXlSHoHfIwk%2FX%2BzAY6pgFL3knirXgIdZ5%2F5Ni51y28w2Lw2EtPDj%2FCQD7DLyuVS9sLEVFF8zuiy4f6clNVngAAI7dXNjauqB8yhMWDPivzH9m%2Bb0mMCd%2Fhmpzvd83pY6YeiFDQGXlEhcB2R4tsgZUxQ57h%2FtfjXAeDmVLce6s%2BAmSIKZJnABti4YU9BDR5DZSULdb6HbkC7%2BxEFQaqU7gWjxyMD2uA1Atp7cuAS5M3s5XmurIQ&X-Amz-Signature=6135714777364b04b781dd23db291d175c9da63bd6bc3f03d40b6cffb8c8c77b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



