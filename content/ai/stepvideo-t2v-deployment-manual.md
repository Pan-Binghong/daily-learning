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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMMYTPJI%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICm52nGlGW6RtjdDoov8G1JusG%2FTyHMB9R4KohATe%2F3yAiEAz%2FVWQNpbxUgchet12Ws3Q%2BCh3O9uhalOMH0OjqcO6IUq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDL0YOaAOaoAjQA5MkircA6tbxKq49BuzNoE%2FHex4RTeUpn13zQJGHLMrl%2BXe5%2B9Wit8SGv1sdNcz3HYX2XMnMPK%2F1kI7bL5Q4TFHRmca99cUYV8df4%2FMnIwbI2Xk9%2FgsbAnZcgma7dU9K5avviHNVnbrHcHPdonOkYh4JZkIue4HvzxVFtwSSmdyNiBkHChoKTUrs8a1DAfzsSlmBxeQ1m2r94rEmR8ZWDnlk%2Bl1hMyPhD5L%2BEamTDbdZklgiaIttSBRTBPMRaSyL8wMHp0ka6w6UTcM7uSckudDYGldAX97Znq6lNYhuaTwExzHYrXUkUOS9TM3XsLuIqotK3wdcLiNTFeHat9MP%2FA7UG98YbsC%2BVw%2FuFHADVO2kzXKLBlgleEcXLuK%2F7WMJAQr1uHsDQiAP8f%2BaV8UGUwa6AigAh1VKHGYdVoRnu%2BSjKk55Muckd8lPtbw9ItfAeOo2HBuXq0593vo7RDMU45KSLM9WAwJZr318K4%2Fr3R9w7bTlABbY5To3jF2LflRjl%2Fmfqg8%2Fc%2F%2FsHbhxv4oclEKbzkF1%2FGG7eelCPRjaLgpr3YxOFbHw75pFbZRmWLoAptpZJVDXohhXjXLJRAOwGNUuwjSpVHtgdbEt7T%2B%2FYa1GGWwgU1OuxVpMqCMjiZgqPHIMOiPvs0GOqUBG7WZYdRGMEiH4D%2FHrPqFOE8OvhAFvipItEyxCWU8Q8SdlpYN8l0oLBXcJpUie%2FRu3CTajsOuHC%2FJWSsv7332ay0alCw2ZnIMvCfCpOtzz4HZlANLd1RA6fctKS5kANftr1hxjvUChZMEZGI%2BIbRz2Dfbe1%2BJ%2Fo%2BOhMipICUT5aiO%2FpRx5HCKlQ3SjEYKn8u21yjpx2vmKc9XnPxFpO4zTQeqszYd&X-Amz-Signature=1233554e4e7b04ab7dd992518c91c10db24bdd906aafc0bd53d9290d7b9f9c96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMMYTPJI%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICm52nGlGW6RtjdDoov8G1JusG%2FTyHMB9R4KohATe%2F3yAiEAz%2FVWQNpbxUgchet12Ws3Q%2BCh3O9uhalOMH0OjqcO6IUq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDL0YOaAOaoAjQA5MkircA6tbxKq49BuzNoE%2FHex4RTeUpn13zQJGHLMrl%2BXe5%2B9Wit8SGv1sdNcz3HYX2XMnMPK%2F1kI7bL5Q4TFHRmca99cUYV8df4%2FMnIwbI2Xk9%2FgsbAnZcgma7dU9K5avviHNVnbrHcHPdonOkYh4JZkIue4HvzxVFtwSSmdyNiBkHChoKTUrs8a1DAfzsSlmBxeQ1m2r94rEmR8ZWDnlk%2Bl1hMyPhD5L%2BEamTDbdZklgiaIttSBRTBPMRaSyL8wMHp0ka6w6UTcM7uSckudDYGldAX97Znq6lNYhuaTwExzHYrXUkUOS9TM3XsLuIqotK3wdcLiNTFeHat9MP%2FA7UG98YbsC%2BVw%2FuFHADVO2kzXKLBlgleEcXLuK%2F7WMJAQr1uHsDQiAP8f%2BaV8UGUwa6AigAh1VKHGYdVoRnu%2BSjKk55Muckd8lPtbw9ItfAeOo2HBuXq0593vo7RDMU45KSLM9WAwJZr318K4%2Fr3R9w7bTlABbY5To3jF2LflRjl%2Fmfqg8%2Fc%2F%2FsHbhxv4oclEKbzkF1%2FGG7eelCPRjaLgpr3YxOFbHw75pFbZRmWLoAptpZJVDXohhXjXLJRAOwGNUuwjSpVHtgdbEt7T%2B%2FYa1GGWwgU1OuxVpMqCMjiZgqPHIMOiPvs0GOqUBG7WZYdRGMEiH4D%2FHrPqFOE8OvhAFvipItEyxCWU8Q8SdlpYN8l0oLBXcJpUie%2FRu3CTajsOuHC%2FJWSsv7332ay0alCw2ZnIMvCfCpOtzz4HZlANLd1RA6fctKS5kANftr1hxjvUChZMEZGI%2BIbRz2Dfbe1%2BJ%2Fo%2BOhMipICUT5aiO%2FpRx5HCKlQ3SjEYKn8u21yjpx2vmKc9XnPxFpO4zTQeqszYd&X-Amz-Signature=68441e2303bfabf7571ebc35e0bff70e4012cbbb17500f21d207df6bd21d573b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMMYTPJI%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICm52nGlGW6RtjdDoov8G1JusG%2FTyHMB9R4KohATe%2F3yAiEAz%2FVWQNpbxUgchet12Ws3Q%2BCh3O9uhalOMH0OjqcO6IUq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDL0YOaAOaoAjQA5MkircA6tbxKq49BuzNoE%2FHex4RTeUpn13zQJGHLMrl%2BXe5%2B9Wit8SGv1sdNcz3HYX2XMnMPK%2F1kI7bL5Q4TFHRmca99cUYV8df4%2FMnIwbI2Xk9%2FgsbAnZcgma7dU9K5avviHNVnbrHcHPdonOkYh4JZkIue4HvzxVFtwSSmdyNiBkHChoKTUrs8a1DAfzsSlmBxeQ1m2r94rEmR8ZWDnlk%2Bl1hMyPhD5L%2BEamTDbdZklgiaIttSBRTBPMRaSyL8wMHp0ka6w6UTcM7uSckudDYGldAX97Znq6lNYhuaTwExzHYrXUkUOS9TM3XsLuIqotK3wdcLiNTFeHat9MP%2FA7UG98YbsC%2BVw%2FuFHADVO2kzXKLBlgleEcXLuK%2F7WMJAQr1uHsDQiAP8f%2BaV8UGUwa6AigAh1VKHGYdVoRnu%2BSjKk55Muckd8lPtbw9ItfAeOo2HBuXq0593vo7RDMU45KSLM9WAwJZr318K4%2Fr3R9w7bTlABbY5To3jF2LflRjl%2Fmfqg8%2Fc%2F%2FsHbhxv4oclEKbzkF1%2FGG7eelCPRjaLgpr3YxOFbHw75pFbZRmWLoAptpZJVDXohhXjXLJRAOwGNUuwjSpVHtgdbEt7T%2B%2FYa1GGWwgU1OuxVpMqCMjiZgqPHIMOiPvs0GOqUBG7WZYdRGMEiH4D%2FHrPqFOE8OvhAFvipItEyxCWU8Q8SdlpYN8l0oLBXcJpUie%2FRu3CTajsOuHC%2FJWSsv7332ay0alCw2ZnIMvCfCpOtzz4HZlANLd1RA6fctKS5kANftr1hxjvUChZMEZGI%2BIbRz2Dfbe1%2BJ%2Fo%2BOhMipICUT5aiO%2FpRx5HCKlQ3SjEYKn8u21yjpx2vmKc9XnPxFpO4zTQeqszYd&X-Amz-Signature=684890c36c95bc93f0ff8eec683d36d71c3d28b814ac6f58cca2a61c52a8c453&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMMYTPJI%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICm52nGlGW6RtjdDoov8G1JusG%2FTyHMB9R4KohATe%2F3yAiEAz%2FVWQNpbxUgchet12Ws3Q%2BCh3O9uhalOMH0OjqcO6IUq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDL0YOaAOaoAjQA5MkircA6tbxKq49BuzNoE%2FHex4RTeUpn13zQJGHLMrl%2BXe5%2B9Wit8SGv1sdNcz3HYX2XMnMPK%2F1kI7bL5Q4TFHRmca99cUYV8df4%2FMnIwbI2Xk9%2FgsbAnZcgma7dU9K5avviHNVnbrHcHPdonOkYh4JZkIue4HvzxVFtwSSmdyNiBkHChoKTUrs8a1DAfzsSlmBxeQ1m2r94rEmR8ZWDnlk%2Bl1hMyPhD5L%2BEamTDbdZklgiaIttSBRTBPMRaSyL8wMHp0ka6w6UTcM7uSckudDYGldAX97Znq6lNYhuaTwExzHYrXUkUOS9TM3XsLuIqotK3wdcLiNTFeHat9MP%2FA7UG98YbsC%2BVw%2FuFHADVO2kzXKLBlgleEcXLuK%2F7WMJAQr1uHsDQiAP8f%2BaV8UGUwa6AigAh1VKHGYdVoRnu%2BSjKk55Muckd8lPtbw9ItfAeOo2HBuXq0593vo7RDMU45KSLM9WAwJZr318K4%2Fr3R9w7bTlABbY5To3jF2LflRjl%2Fmfqg8%2Fc%2F%2FsHbhxv4oclEKbzkF1%2FGG7eelCPRjaLgpr3YxOFbHw75pFbZRmWLoAptpZJVDXohhXjXLJRAOwGNUuwjSpVHtgdbEt7T%2B%2FYa1GGWwgU1OuxVpMqCMjiZgqPHIMOiPvs0GOqUBG7WZYdRGMEiH4D%2FHrPqFOE8OvhAFvipItEyxCWU8Q8SdlpYN8l0oLBXcJpUie%2FRu3CTajsOuHC%2FJWSsv7332ay0alCw2ZnIMvCfCpOtzz4HZlANLd1RA6fctKS5kANftr1hxjvUChZMEZGI%2BIbRz2Dfbe1%2BJ%2Fo%2BOhMipICUT5aiO%2FpRx5HCKlQ3SjEYKn8u21yjpx2vmKc9XnPxFpO4zTQeqszYd&X-Amz-Signature=d20b0156307b727d95c313e455b493f6c82055fbc752904293b717488066f225&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



