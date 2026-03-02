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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW2UCSUP%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkHVv%2BwfV46cNsDrtUH9f8eROvbTqxV6TN99h%2Bbq8v1QIgPyMeeO49zVm8kSKi4mKe1BIo5hRsJA3KyhdjtWGK7a4q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDKaDa7i0aHJPxXuPiSrcA3gzrII6r6CXpKaz3S8s1DSjdrpY5Ix7XWGZBegKEmjwvJ%2FmkkAZIyAjC2fHHsuROWS2771pAiBMydI%2BZLrHc5245R195kHR7w1l9NSYmXNHDEeI%2F%2BwuCf4WmcgV4Uy%2FrGbNXuRZ%2FjuHjRqc2zRNKzQCgW4fFEqCQickYr2QOgwQPT1VG0Z7k58HBzOnn0UupJ7PahGLkaPP3QWTZZ4SaoGki6mhylRE%2BdhSH%2FwzmEeSQrEidqE7Fzr94WTX0uHRhl7fG6IIs2TWKubf%2FT6hIx8R%2BJZw9wBP7faEReI6xx%2Fv6XdGCc9SIWo8MplGtQ611JXKqoZbpasFV60c94P11MPvBxtz1iNgwMg6Bv%2F1cfoq%2BrRJIMWf0pAxdzrFRVPwe6S1PG7UDYD7FL4PnEmchzG7qBQ7TWtFKu7ab%2BMw%2FW5I1t97CgXFBiNHCIOQ6HeHgIkXXp8EetuvLpTvyFEBw0seHi1U1kYhNUOhvN61Rg0ok4KWFg%2BpDnIViqeOnPmamVPCdnF5GcXqYo%2BIKZVk76Gg5p5ItI8lLmeXrNKViMpS4uy7kKogb8NqTH4QofSTS8C8Yl5pdFj0LuVtPq3CjoS7jhuCPKQs820JQnOcI%2BoflRhS5dr0s%2BH4fKtYMK%2F9k80GOqUBEeRZrYrPdPasQur01nOhnes06j1ape6zzL7iYiB4NR%2FXfuOpe6v%2B%2B%2Bx5tOoYCXha10Oq2kFYUfzz%2BQjOr5i5pgSscdc50Tv1Bsj631YBzmALf9CmnpmjuAXfgfV5BBgFK8v3SSclFtzohdnwDl0oCkgsKs%2Bkgzs0VFI6cjSEz%2FQu0Kl4nzsr6xzbTm3r7WsTS43L99xLRohnp30c5hpqrTQ%2F84VC&X-Amz-Signature=f9c332b4dc6f654a4d3e692211d3bc7a559518839e4fd57e13e75634e6c1ce0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW2UCSUP%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkHVv%2BwfV46cNsDrtUH9f8eROvbTqxV6TN99h%2Bbq8v1QIgPyMeeO49zVm8kSKi4mKe1BIo5hRsJA3KyhdjtWGK7a4q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDKaDa7i0aHJPxXuPiSrcA3gzrII6r6CXpKaz3S8s1DSjdrpY5Ix7XWGZBegKEmjwvJ%2FmkkAZIyAjC2fHHsuROWS2771pAiBMydI%2BZLrHc5245R195kHR7w1l9NSYmXNHDEeI%2F%2BwuCf4WmcgV4Uy%2FrGbNXuRZ%2FjuHjRqc2zRNKzQCgW4fFEqCQickYr2QOgwQPT1VG0Z7k58HBzOnn0UupJ7PahGLkaPP3QWTZZ4SaoGki6mhylRE%2BdhSH%2FwzmEeSQrEidqE7Fzr94WTX0uHRhl7fG6IIs2TWKubf%2FT6hIx8R%2BJZw9wBP7faEReI6xx%2Fv6XdGCc9SIWo8MplGtQ611JXKqoZbpasFV60c94P11MPvBxtz1iNgwMg6Bv%2F1cfoq%2BrRJIMWf0pAxdzrFRVPwe6S1PG7UDYD7FL4PnEmchzG7qBQ7TWtFKu7ab%2BMw%2FW5I1t97CgXFBiNHCIOQ6HeHgIkXXp8EetuvLpTvyFEBw0seHi1U1kYhNUOhvN61Rg0ok4KWFg%2BpDnIViqeOnPmamVPCdnF5GcXqYo%2BIKZVk76Gg5p5ItI8lLmeXrNKViMpS4uy7kKogb8NqTH4QofSTS8C8Yl5pdFj0LuVtPq3CjoS7jhuCPKQs820JQnOcI%2BoflRhS5dr0s%2BH4fKtYMK%2F9k80GOqUBEeRZrYrPdPasQur01nOhnes06j1ape6zzL7iYiB4NR%2FXfuOpe6v%2B%2B%2Bx5tOoYCXha10Oq2kFYUfzz%2BQjOr5i5pgSscdc50Tv1Bsj631YBzmALf9CmnpmjuAXfgfV5BBgFK8v3SSclFtzohdnwDl0oCkgsKs%2Bkgzs0VFI6cjSEz%2FQu0Kl4nzsr6xzbTm3r7WsTS43L99xLRohnp30c5hpqrTQ%2F84VC&X-Amz-Signature=cfc80f34058daa9d8ea1313eaa4050ab2e6120951a8ddc295e50a00ff875b628&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW2UCSUP%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkHVv%2BwfV46cNsDrtUH9f8eROvbTqxV6TN99h%2Bbq8v1QIgPyMeeO49zVm8kSKi4mKe1BIo5hRsJA3KyhdjtWGK7a4q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDKaDa7i0aHJPxXuPiSrcA3gzrII6r6CXpKaz3S8s1DSjdrpY5Ix7XWGZBegKEmjwvJ%2FmkkAZIyAjC2fHHsuROWS2771pAiBMydI%2BZLrHc5245R195kHR7w1l9NSYmXNHDEeI%2F%2BwuCf4WmcgV4Uy%2FrGbNXuRZ%2FjuHjRqc2zRNKzQCgW4fFEqCQickYr2QOgwQPT1VG0Z7k58HBzOnn0UupJ7PahGLkaPP3QWTZZ4SaoGki6mhylRE%2BdhSH%2FwzmEeSQrEidqE7Fzr94WTX0uHRhl7fG6IIs2TWKubf%2FT6hIx8R%2BJZw9wBP7faEReI6xx%2Fv6XdGCc9SIWo8MplGtQ611JXKqoZbpasFV60c94P11MPvBxtz1iNgwMg6Bv%2F1cfoq%2BrRJIMWf0pAxdzrFRVPwe6S1PG7UDYD7FL4PnEmchzG7qBQ7TWtFKu7ab%2BMw%2FW5I1t97CgXFBiNHCIOQ6HeHgIkXXp8EetuvLpTvyFEBw0seHi1U1kYhNUOhvN61Rg0ok4KWFg%2BpDnIViqeOnPmamVPCdnF5GcXqYo%2BIKZVk76Gg5p5ItI8lLmeXrNKViMpS4uy7kKogb8NqTH4QofSTS8C8Yl5pdFj0LuVtPq3CjoS7jhuCPKQs820JQnOcI%2BoflRhS5dr0s%2BH4fKtYMK%2F9k80GOqUBEeRZrYrPdPasQur01nOhnes06j1ape6zzL7iYiB4NR%2FXfuOpe6v%2B%2B%2Bx5tOoYCXha10Oq2kFYUfzz%2BQjOr5i5pgSscdc50Tv1Bsj631YBzmALf9CmnpmjuAXfgfV5BBgFK8v3SSclFtzohdnwDl0oCkgsKs%2Bkgzs0VFI6cjSEz%2FQu0Kl4nzsr6xzbTm3r7WsTS43L99xLRohnp30c5hpqrTQ%2F84VC&X-Amz-Signature=74e0c775affe112c4fee3c23dc5b0e6c76bd3db3f71c5776a9980688e85311fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW2UCSUP%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkHVv%2BwfV46cNsDrtUH9f8eROvbTqxV6TN99h%2Bbq8v1QIgPyMeeO49zVm8kSKi4mKe1BIo5hRsJA3KyhdjtWGK7a4q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDKaDa7i0aHJPxXuPiSrcA3gzrII6r6CXpKaz3S8s1DSjdrpY5Ix7XWGZBegKEmjwvJ%2FmkkAZIyAjC2fHHsuROWS2771pAiBMydI%2BZLrHc5245R195kHR7w1l9NSYmXNHDEeI%2F%2BwuCf4WmcgV4Uy%2FrGbNXuRZ%2FjuHjRqc2zRNKzQCgW4fFEqCQickYr2QOgwQPT1VG0Z7k58HBzOnn0UupJ7PahGLkaPP3QWTZZ4SaoGki6mhylRE%2BdhSH%2FwzmEeSQrEidqE7Fzr94WTX0uHRhl7fG6IIs2TWKubf%2FT6hIx8R%2BJZw9wBP7faEReI6xx%2Fv6XdGCc9SIWo8MplGtQ611JXKqoZbpasFV60c94P11MPvBxtz1iNgwMg6Bv%2F1cfoq%2BrRJIMWf0pAxdzrFRVPwe6S1PG7UDYD7FL4PnEmchzG7qBQ7TWtFKu7ab%2BMw%2FW5I1t97CgXFBiNHCIOQ6HeHgIkXXp8EetuvLpTvyFEBw0seHi1U1kYhNUOhvN61Rg0ok4KWFg%2BpDnIViqeOnPmamVPCdnF5GcXqYo%2BIKZVk76Gg5p5ItI8lLmeXrNKViMpS4uy7kKogb8NqTH4QofSTS8C8Yl5pdFj0LuVtPq3CjoS7jhuCPKQs820JQnOcI%2BoflRhS5dr0s%2BH4fKtYMK%2F9k80GOqUBEeRZrYrPdPasQur01nOhnes06j1ape6zzL7iYiB4NR%2FXfuOpe6v%2B%2B%2Bx5tOoYCXha10Oq2kFYUfzz%2BQjOr5i5pgSscdc50Tv1Bsj631YBzmALf9CmnpmjuAXfgfV5BBgFK8v3SSclFtzohdnwDl0oCkgsKs%2Bkgzs0VFI6cjSEz%2FQu0Kl4nzsr6xzbTm3r7WsTS43L99xLRohnp30c5hpqrTQ%2F84VC&X-Amz-Signature=93ca14265b5ae470e55defcd5c4b0f5000b2a301f1a2bc187fd04cceacb6e509&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



