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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2B6J3W%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQCDHZLlN3AAwzC1xyBQsGrhd5ZPlpSzFV05ozuxdnmINgIgIz7o97yfOLgcj85qBgKXRuw2qgE07EAW4dqrlSittqUqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFVxyN6vlxKxwmAFyrcAwHFkVRJPXU0nmpuQRxUMDWRX4r62E194cN1qvf79FkOEgd9PmhUunJwrUlU4eTsqdR%2F2%2F1UpJVnRGecKhmOaaifYaEPaAMLihQW7RBt4i2eWYJF9VGuPxLcSq65PEcOe%2FZvBRF2x%2B6%2F3XB2L3P7MyDR8%2F8ySbgY%2BlA3JSbhY9q0MrLp1iIS5SILOjmL3rorZikCSQMag7Cc4Rbhzp7C9TTEur8YYsJv%2FhV6JS%2FTwLVpI0RM30i9k%2FNqyOtomIAVvkY70XYnF3W1o1fkQ9FzvOGAXfdQzf0WfP8WIokUHViG5CYHdUg%2FgHLBKmNRZuMVUs4ggac2108R9scgtMSigq27FLiR41hVzK5Vqg0zUy7KXlwJlim2DsbK09M2Egje6NqyKIJzULrYTue%2FEysvpCrzEZ1HHxZH9kI9EPLidM%2BPeUXJj3XvbJP2gO4vYlGIyqomb5N%2F%2Fkm9ZKH6uxHz0TZJnhqVPMfLUdcCYWziXUcDF3Cenakslnjs2ii3fkRPnBpk8okSyYnLLEAdZTB89xXvttE2k3k99McahutxuvIQAc%2FdJ2VqZFVoXmYd5lMTPHov%2FI3IHjXjs8SPUikY%2BCcd%2BH3heGYJ8y5Udjc%2BMMr67ncni242n3oukqWYMIHZhcwGOqUBFGTbcNbMzsMkvQU92lqqzWQj4pJpelOL1bmJdVdPMDq%2FIw1PGIBSekQZ3P5kECGGlSKcRt0VTMPJ%2BN6pmNqgGBkrkSMJ2atkGOeBSq2BY8JE05cSHsC87dAfH3jHN3YgvcCyUUKwZD3XK6tBelO6RxQiKQvHA33sTxz%2BmJ51s0OeClTrjWpR7OPsSFEnmb2EEjSQFRp9q0iRH69vzmX2kXtY%2F%2B14&X-Amz-Signature=27f4c35f4bc78fba30917f58d3f9208a2a10431b50f7ec18d5d08ecc64b97e5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2B6J3W%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQCDHZLlN3AAwzC1xyBQsGrhd5ZPlpSzFV05ozuxdnmINgIgIz7o97yfOLgcj85qBgKXRuw2qgE07EAW4dqrlSittqUqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFVxyN6vlxKxwmAFyrcAwHFkVRJPXU0nmpuQRxUMDWRX4r62E194cN1qvf79FkOEgd9PmhUunJwrUlU4eTsqdR%2F2%2F1UpJVnRGecKhmOaaifYaEPaAMLihQW7RBt4i2eWYJF9VGuPxLcSq65PEcOe%2FZvBRF2x%2B6%2F3XB2L3P7MyDR8%2F8ySbgY%2BlA3JSbhY9q0MrLp1iIS5SILOjmL3rorZikCSQMag7Cc4Rbhzp7C9TTEur8YYsJv%2FhV6JS%2FTwLVpI0RM30i9k%2FNqyOtomIAVvkY70XYnF3W1o1fkQ9FzvOGAXfdQzf0WfP8WIokUHViG5CYHdUg%2FgHLBKmNRZuMVUs4ggac2108R9scgtMSigq27FLiR41hVzK5Vqg0zUy7KXlwJlim2DsbK09M2Egje6NqyKIJzULrYTue%2FEysvpCrzEZ1HHxZH9kI9EPLidM%2BPeUXJj3XvbJP2gO4vYlGIyqomb5N%2F%2Fkm9ZKH6uxHz0TZJnhqVPMfLUdcCYWziXUcDF3Cenakslnjs2ii3fkRPnBpk8okSyYnLLEAdZTB89xXvttE2k3k99McahutxuvIQAc%2FdJ2VqZFVoXmYd5lMTPHov%2FI3IHjXjs8SPUikY%2BCcd%2BH3heGYJ8y5Udjc%2BMMr67ncni242n3oukqWYMIHZhcwGOqUBFGTbcNbMzsMkvQU92lqqzWQj4pJpelOL1bmJdVdPMDq%2FIw1PGIBSekQZ3P5kECGGlSKcRt0VTMPJ%2BN6pmNqgGBkrkSMJ2atkGOeBSq2BY8JE05cSHsC87dAfH3jHN3YgvcCyUUKwZD3XK6tBelO6RxQiKQvHA33sTxz%2BmJ51s0OeClTrjWpR7OPsSFEnmb2EEjSQFRp9q0iRH69vzmX2kXtY%2F%2B14&X-Amz-Signature=c50297255db1c634da8ab1517cd1e44794c08c54df0c23fbbd4ffcb02e73af05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2B6J3W%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQCDHZLlN3AAwzC1xyBQsGrhd5ZPlpSzFV05ozuxdnmINgIgIz7o97yfOLgcj85qBgKXRuw2qgE07EAW4dqrlSittqUqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFVxyN6vlxKxwmAFyrcAwHFkVRJPXU0nmpuQRxUMDWRX4r62E194cN1qvf79FkOEgd9PmhUunJwrUlU4eTsqdR%2F2%2F1UpJVnRGecKhmOaaifYaEPaAMLihQW7RBt4i2eWYJF9VGuPxLcSq65PEcOe%2FZvBRF2x%2B6%2F3XB2L3P7MyDR8%2F8ySbgY%2BlA3JSbhY9q0MrLp1iIS5SILOjmL3rorZikCSQMag7Cc4Rbhzp7C9TTEur8YYsJv%2FhV6JS%2FTwLVpI0RM30i9k%2FNqyOtomIAVvkY70XYnF3W1o1fkQ9FzvOGAXfdQzf0WfP8WIokUHViG5CYHdUg%2FgHLBKmNRZuMVUs4ggac2108R9scgtMSigq27FLiR41hVzK5Vqg0zUy7KXlwJlim2DsbK09M2Egje6NqyKIJzULrYTue%2FEysvpCrzEZ1HHxZH9kI9EPLidM%2BPeUXJj3XvbJP2gO4vYlGIyqomb5N%2F%2Fkm9ZKH6uxHz0TZJnhqVPMfLUdcCYWziXUcDF3Cenakslnjs2ii3fkRPnBpk8okSyYnLLEAdZTB89xXvttE2k3k99McahutxuvIQAc%2FdJ2VqZFVoXmYd5lMTPHov%2FI3IHjXjs8SPUikY%2BCcd%2BH3heGYJ8y5Udjc%2BMMr67ncni242n3oukqWYMIHZhcwGOqUBFGTbcNbMzsMkvQU92lqqzWQj4pJpelOL1bmJdVdPMDq%2FIw1PGIBSekQZ3P5kECGGlSKcRt0VTMPJ%2BN6pmNqgGBkrkSMJ2atkGOeBSq2BY8JE05cSHsC87dAfH3jHN3YgvcCyUUKwZD3XK6tBelO6RxQiKQvHA33sTxz%2BmJ51s0OeClTrjWpR7OPsSFEnmb2EEjSQFRp9q0iRH69vzmX2kXtY%2F%2B14&X-Amz-Signature=b2cebbb546998f6ae928f658a46f49eff05a93003bfcd6e295c1a7520e8338dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2B6J3W%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQCDHZLlN3AAwzC1xyBQsGrhd5ZPlpSzFV05ozuxdnmINgIgIz7o97yfOLgcj85qBgKXRuw2qgE07EAW4dqrlSittqUqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFVxyN6vlxKxwmAFyrcAwHFkVRJPXU0nmpuQRxUMDWRX4r62E194cN1qvf79FkOEgd9PmhUunJwrUlU4eTsqdR%2F2%2F1UpJVnRGecKhmOaaifYaEPaAMLihQW7RBt4i2eWYJF9VGuPxLcSq65PEcOe%2FZvBRF2x%2B6%2F3XB2L3P7MyDR8%2F8ySbgY%2BlA3JSbhY9q0MrLp1iIS5SILOjmL3rorZikCSQMag7Cc4Rbhzp7C9TTEur8YYsJv%2FhV6JS%2FTwLVpI0RM30i9k%2FNqyOtomIAVvkY70XYnF3W1o1fkQ9FzvOGAXfdQzf0WfP8WIokUHViG5CYHdUg%2FgHLBKmNRZuMVUs4ggac2108R9scgtMSigq27FLiR41hVzK5Vqg0zUy7KXlwJlim2DsbK09M2Egje6NqyKIJzULrYTue%2FEysvpCrzEZ1HHxZH9kI9EPLidM%2BPeUXJj3XvbJP2gO4vYlGIyqomb5N%2F%2Fkm9ZKH6uxHz0TZJnhqVPMfLUdcCYWziXUcDF3Cenakslnjs2ii3fkRPnBpk8okSyYnLLEAdZTB89xXvttE2k3k99McahutxuvIQAc%2FdJ2VqZFVoXmYd5lMTPHov%2FI3IHjXjs8SPUikY%2BCcd%2BH3heGYJ8y5Udjc%2BMMr67ncni242n3oukqWYMIHZhcwGOqUBFGTbcNbMzsMkvQU92lqqzWQj4pJpelOL1bmJdVdPMDq%2FIw1PGIBSekQZ3P5kECGGlSKcRt0VTMPJ%2BN6pmNqgGBkrkSMJ2atkGOeBSq2BY8JE05cSHsC87dAfH3jHN3YgvcCyUUKwZD3XK6tBelO6RxQiKQvHA33sTxz%2BmJ51s0OeClTrjWpR7OPsSFEnmb2EEjSQFRp9q0iRH69vzmX2kXtY%2F%2B14&X-Amz-Signature=068dfac941125a683b9bef226209e993e44231a43af787dcafca3cc2e254d031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



