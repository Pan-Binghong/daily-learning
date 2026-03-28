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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZHGEUB%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIBjOfceWsF1%2Fg3k42dYzmzNW%2FUxDbbN9YN130y4M8%2FwYAiBjGO4yvrZ7dTo72uZVGpvHNecQ8I9KqNXmLkPicrjFlyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpNfnAdy%2FaDop8X3CKtwDqnVTw%2FUvk0VlzmMbAk%2FjTDGZS3BnQ7oYEyDUoGncekc%2FzzZYHF4zEkzJbnlfv1MTHtUCEybLa27krdEcpkJU3AcCpgEOB9J%2FGVWi5Snzbb9AHf2lA81PN9dET2scCOFK2IjI%2FfCkSC8%2FKMsILw8nCxF5l4pZzO%2BjnPw99%2FBf92Y%2BUZhGP0%2FtNt%2BRoQiD2Sk4yjOzmjkSph1ss8l1bVPMYhp0zW5R%2BXckq2qrZklzZupB4SFVtUSYuZFXKVbVZBSRV7pner3x1XKWoHGkO%2Fpny4gzuhlfslhx2EZc7k2947Owa8jSFehQQ4BUq1R0VixHug%2FIRZWyruOUDN0QMVHVzPyrpe6rLS7n3twcOKn2AzVKWyzu1IUkWsS4fItVdJlTB40xfll9eKNf%2BaiGHIMdixUqddks9rTueusKA1idx4Y2BU1vtVLAoD4f5wv0aWbJ91UordNblyacWYLP8tl%2BdBZZCSdkE9ofJg4oe%2FF9bX1Aq5SfB84yu%2FcnH42vh7Hreqp8YuZwoqakWFYOs5vJe5uSLXviuB2wHE0zIeCMgFqlR9vJC2DPvf6bK33Ayxw%2BTpW9RzyatbJq%2F2ubS4rqk5NahdKIpk3XfQUAYITkRlJ85WNmX21pTXZaeXIwkO2czgY6pgGseZuzGbLlOpFYLSkMBza1YwV6beARtse%2FJAY%2B3hABc1le%2BkxK2GHPmLnf6%2BzYmXBtwfmmRlb46SVAvgBRvPQbBX4dDuj540B7kw31sx4E8ySWMzOOUU682bPQddIE%2Bwc1wN0JJgzVDvZ53WX%2F0t6q4n%2Bpoii7nzvRdP8poioMGSANXEr86wMYv41HYWRWkXzgFOu9wNkxmDv1LSHjNY0Um37sey8u&X-Amz-Signature=d82187a53c21b5ae4657348ef2b98b9b0b1d8995474eee368e6c356a55bafb9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZHGEUB%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIBjOfceWsF1%2Fg3k42dYzmzNW%2FUxDbbN9YN130y4M8%2FwYAiBjGO4yvrZ7dTo72uZVGpvHNecQ8I9KqNXmLkPicrjFlyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpNfnAdy%2FaDop8X3CKtwDqnVTw%2FUvk0VlzmMbAk%2FjTDGZS3BnQ7oYEyDUoGncekc%2FzzZYHF4zEkzJbnlfv1MTHtUCEybLa27krdEcpkJU3AcCpgEOB9J%2FGVWi5Snzbb9AHf2lA81PN9dET2scCOFK2IjI%2FfCkSC8%2FKMsILw8nCxF5l4pZzO%2BjnPw99%2FBf92Y%2BUZhGP0%2FtNt%2BRoQiD2Sk4yjOzmjkSph1ss8l1bVPMYhp0zW5R%2BXckq2qrZklzZupB4SFVtUSYuZFXKVbVZBSRV7pner3x1XKWoHGkO%2Fpny4gzuhlfslhx2EZc7k2947Owa8jSFehQQ4BUq1R0VixHug%2FIRZWyruOUDN0QMVHVzPyrpe6rLS7n3twcOKn2AzVKWyzu1IUkWsS4fItVdJlTB40xfll9eKNf%2BaiGHIMdixUqddks9rTueusKA1idx4Y2BU1vtVLAoD4f5wv0aWbJ91UordNblyacWYLP8tl%2BdBZZCSdkE9ofJg4oe%2FF9bX1Aq5SfB84yu%2FcnH42vh7Hreqp8YuZwoqakWFYOs5vJe5uSLXviuB2wHE0zIeCMgFqlR9vJC2DPvf6bK33Ayxw%2BTpW9RzyatbJq%2F2ubS4rqk5NahdKIpk3XfQUAYITkRlJ85WNmX21pTXZaeXIwkO2czgY6pgGseZuzGbLlOpFYLSkMBza1YwV6beARtse%2FJAY%2B3hABc1le%2BkxK2GHPmLnf6%2BzYmXBtwfmmRlb46SVAvgBRvPQbBX4dDuj540B7kw31sx4E8ySWMzOOUU682bPQddIE%2Bwc1wN0JJgzVDvZ53WX%2F0t6q4n%2Bpoii7nzvRdP8poioMGSANXEr86wMYv41HYWRWkXzgFOu9wNkxmDv1LSHjNY0Um37sey8u&X-Amz-Signature=aeb0a8f32f4ee7f4ef279bf8825e76b1b0ae0b57d7da4c017056749d9a98e90b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZHGEUB%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIBjOfceWsF1%2Fg3k42dYzmzNW%2FUxDbbN9YN130y4M8%2FwYAiBjGO4yvrZ7dTo72uZVGpvHNecQ8I9KqNXmLkPicrjFlyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpNfnAdy%2FaDop8X3CKtwDqnVTw%2FUvk0VlzmMbAk%2FjTDGZS3BnQ7oYEyDUoGncekc%2FzzZYHF4zEkzJbnlfv1MTHtUCEybLa27krdEcpkJU3AcCpgEOB9J%2FGVWi5Snzbb9AHf2lA81PN9dET2scCOFK2IjI%2FfCkSC8%2FKMsILw8nCxF5l4pZzO%2BjnPw99%2FBf92Y%2BUZhGP0%2FtNt%2BRoQiD2Sk4yjOzmjkSph1ss8l1bVPMYhp0zW5R%2BXckq2qrZklzZupB4SFVtUSYuZFXKVbVZBSRV7pner3x1XKWoHGkO%2Fpny4gzuhlfslhx2EZc7k2947Owa8jSFehQQ4BUq1R0VixHug%2FIRZWyruOUDN0QMVHVzPyrpe6rLS7n3twcOKn2AzVKWyzu1IUkWsS4fItVdJlTB40xfll9eKNf%2BaiGHIMdixUqddks9rTueusKA1idx4Y2BU1vtVLAoD4f5wv0aWbJ91UordNblyacWYLP8tl%2BdBZZCSdkE9ofJg4oe%2FF9bX1Aq5SfB84yu%2FcnH42vh7Hreqp8YuZwoqakWFYOs5vJe5uSLXviuB2wHE0zIeCMgFqlR9vJC2DPvf6bK33Ayxw%2BTpW9RzyatbJq%2F2ubS4rqk5NahdKIpk3XfQUAYITkRlJ85WNmX21pTXZaeXIwkO2czgY6pgGseZuzGbLlOpFYLSkMBza1YwV6beARtse%2FJAY%2B3hABc1le%2BkxK2GHPmLnf6%2BzYmXBtwfmmRlb46SVAvgBRvPQbBX4dDuj540B7kw31sx4E8ySWMzOOUU682bPQddIE%2Bwc1wN0JJgzVDvZ53WX%2F0t6q4n%2Bpoii7nzvRdP8poioMGSANXEr86wMYv41HYWRWkXzgFOu9wNkxmDv1LSHjNY0Um37sey8u&X-Amz-Signature=d157a8e472f3781bbc5e610c9436f562f6b6a98a3ea96954f20099a6bc4c9b7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZHGEUB%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIBjOfceWsF1%2Fg3k42dYzmzNW%2FUxDbbN9YN130y4M8%2FwYAiBjGO4yvrZ7dTo72uZVGpvHNecQ8I9KqNXmLkPicrjFlyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpNfnAdy%2FaDop8X3CKtwDqnVTw%2FUvk0VlzmMbAk%2FjTDGZS3BnQ7oYEyDUoGncekc%2FzzZYHF4zEkzJbnlfv1MTHtUCEybLa27krdEcpkJU3AcCpgEOB9J%2FGVWi5Snzbb9AHf2lA81PN9dET2scCOFK2IjI%2FfCkSC8%2FKMsILw8nCxF5l4pZzO%2BjnPw99%2FBf92Y%2BUZhGP0%2FtNt%2BRoQiD2Sk4yjOzmjkSph1ss8l1bVPMYhp0zW5R%2BXckq2qrZklzZupB4SFVtUSYuZFXKVbVZBSRV7pner3x1XKWoHGkO%2Fpny4gzuhlfslhx2EZc7k2947Owa8jSFehQQ4BUq1R0VixHug%2FIRZWyruOUDN0QMVHVzPyrpe6rLS7n3twcOKn2AzVKWyzu1IUkWsS4fItVdJlTB40xfll9eKNf%2BaiGHIMdixUqddks9rTueusKA1idx4Y2BU1vtVLAoD4f5wv0aWbJ91UordNblyacWYLP8tl%2BdBZZCSdkE9ofJg4oe%2FF9bX1Aq5SfB84yu%2FcnH42vh7Hreqp8YuZwoqakWFYOs5vJe5uSLXviuB2wHE0zIeCMgFqlR9vJC2DPvf6bK33Ayxw%2BTpW9RzyatbJq%2F2ubS4rqk5NahdKIpk3XfQUAYITkRlJ85WNmX21pTXZaeXIwkO2czgY6pgGseZuzGbLlOpFYLSkMBza1YwV6beARtse%2FJAY%2B3hABc1le%2BkxK2GHPmLnf6%2BzYmXBtwfmmRlb46SVAvgBRvPQbBX4dDuj540B7kw31sx4E8ySWMzOOUU682bPQddIE%2Bwc1wN0JJgzVDvZ53WX%2F0t6q4n%2Bpoii7nzvRdP8poioMGSANXEr86wMYv41HYWRWkXzgFOu9wNkxmDv1LSHjNY0Um37sey8u&X-Amz-Signature=dc0c10605b2b133e12c3f326cfbd9d0b014736db7bf314289a0ed263691a4736&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



