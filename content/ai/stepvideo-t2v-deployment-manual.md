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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCZA2F4B%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDp1HGEi3IaKqfgMc5twsdaTbfQXq%2BrTHUPqDPNvAetYAIgMvx4TW0Z1QKamlb1j2GLtyEF4YZXjYLAOILYjtJebToqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQ5CisLL0hUDY4zrSrcAx04P4URnlgDact%2BCByfqpkCUq%2B%2B31zU3B5JmJ5CbwQt%2FNUcUzcI%2Bchaph3QraRY%2BYPZXHiJvgHLYcB4sEKk3jQKoMdCl5sqMehOJ%2BvOME%2BSO063a2qzwndWuE1jXKBJd2WAYswNRGKss0jBFwlcCP5jk1MAr8%2Bu5tAn%2BV%2FBrgQF6NR%2FKVIXM6wyHoik%2FCSd1GBB8zYMaeE1xHq9D8Al3jhpXu162gYkXdkSVcImp87sJQLHtYpW8EvVAprHPqJRTE4P3znCfQw0wkY6L8%2FCkvWV6aaEZzUxftHIKUcJE8SqPRt8CraH6zuwMoD187XRtwp6xfdkQlZLC2eNH7yQ1%2BwJyHjqwOF9wwcPevGJrDPJEGFt1nuFI2OvvsoidapWQ2ra3zOf2%2FAhR5pcsn35HRvJWLfXoqCmtk3NfNatLzJyqpmMF7a3tuNQVX85YHgk%2BO1t%2BZULPvYSDYgk4pallTpt54XK5Ls4MwZDs8r5%2BAdR3RmHejItz4lHB4yyivK8F%2FBzwyRSnjUe87qWO6gApxu%2B9%2Bbge3Zodu4EmF9NYtmuMaKdE%2FUyq2rEhT3HcgDFPpuNVENfDomEUjcFxL%2B0cKlp%2FJiXgYBqmLJJ6PJAYdTnqmS0UHPqeMtY6wpbMMDpls4GOqUB8ZNM%2B6%2B6c2WPVyXm3WSwdNjni4ByuLWpfFtvZ%2BgY1Br1D5dYTp0D0wOmob7d7LMivRveQeq7LSUh7eHNn5PoMnUwpEBvq7L9C7MisoJTPARweMVoYwP80ERXmA68zNlaaPAEI2A0dP%2B4ZoIuK%2Bx4m64sfl0w6P7vU3w20nxs6%2Bw4Q0b2R7TtDkb%2FxlIfXR3Kvo0cAmfuxCN68vcisaLZ%2FcoQoIDf&X-Amz-Signature=392353d6908ffff41eca6943d55227148423877d4f4c9e69876da502a77e08eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCZA2F4B%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDp1HGEi3IaKqfgMc5twsdaTbfQXq%2BrTHUPqDPNvAetYAIgMvx4TW0Z1QKamlb1j2GLtyEF4YZXjYLAOILYjtJebToqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQ5CisLL0hUDY4zrSrcAx04P4URnlgDact%2BCByfqpkCUq%2B%2B31zU3B5JmJ5CbwQt%2FNUcUzcI%2Bchaph3QraRY%2BYPZXHiJvgHLYcB4sEKk3jQKoMdCl5sqMehOJ%2BvOME%2BSO063a2qzwndWuE1jXKBJd2WAYswNRGKss0jBFwlcCP5jk1MAr8%2Bu5tAn%2BV%2FBrgQF6NR%2FKVIXM6wyHoik%2FCSd1GBB8zYMaeE1xHq9D8Al3jhpXu162gYkXdkSVcImp87sJQLHtYpW8EvVAprHPqJRTE4P3znCfQw0wkY6L8%2FCkvWV6aaEZzUxftHIKUcJE8SqPRt8CraH6zuwMoD187XRtwp6xfdkQlZLC2eNH7yQ1%2BwJyHjqwOF9wwcPevGJrDPJEGFt1nuFI2OvvsoidapWQ2ra3zOf2%2FAhR5pcsn35HRvJWLfXoqCmtk3NfNatLzJyqpmMF7a3tuNQVX85YHgk%2BO1t%2BZULPvYSDYgk4pallTpt54XK5Ls4MwZDs8r5%2BAdR3RmHejItz4lHB4yyivK8F%2FBzwyRSnjUe87qWO6gApxu%2B9%2Bbge3Zodu4EmF9NYtmuMaKdE%2FUyq2rEhT3HcgDFPpuNVENfDomEUjcFxL%2B0cKlp%2FJiXgYBqmLJJ6PJAYdTnqmS0UHPqeMtY6wpbMMDpls4GOqUB8ZNM%2B6%2B6c2WPVyXm3WSwdNjni4ByuLWpfFtvZ%2BgY1Br1D5dYTp0D0wOmob7d7LMivRveQeq7LSUh7eHNn5PoMnUwpEBvq7L9C7MisoJTPARweMVoYwP80ERXmA68zNlaaPAEI2A0dP%2B4ZoIuK%2Bx4m64sfl0w6P7vU3w20nxs6%2Bw4Q0b2R7TtDkb%2FxlIfXR3Kvo0cAmfuxCN68vcisaLZ%2FcoQoIDf&X-Amz-Signature=077e0254afd866933d4243a59dab0920cbfe947f8df3219bdc5ff27dfc478088&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCZA2F4B%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDp1HGEi3IaKqfgMc5twsdaTbfQXq%2BrTHUPqDPNvAetYAIgMvx4TW0Z1QKamlb1j2GLtyEF4YZXjYLAOILYjtJebToqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQ5CisLL0hUDY4zrSrcAx04P4URnlgDact%2BCByfqpkCUq%2B%2B31zU3B5JmJ5CbwQt%2FNUcUzcI%2Bchaph3QraRY%2BYPZXHiJvgHLYcB4sEKk3jQKoMdCl5sqMehOJ%2BvOME%2BSO063a2qzwndWuE1jXKBJd2WAYswNRGKss0jBFwlcCP5jk1MAr8%2Bu5tAn%2BV%2FBrgQF6NR%2FKVIXM6wyHoik%2FCSd1GBB8zYMaeE1xHq9D8Al3jhpXu162gYkXdkSVcImp87sJQLHtYpW8EvVAprHPqJRTE4P3znCfQw0wkY6L8%2FCkvWV6aaEZzUxftHIKUcJE8SqPRt8CraH6zuwMoD187XRtwp6xfdkQlZLC2eNH7yQ1%2BwJyHjqwOF9wwcPevGJrDPJEGFt1nuFI2OvvsoidapWQ2ra3zOf2%2FAhR5pcsn35HRvJWLfXoqCmtk3NfNatLzJyqpmMF7a3tuNQVX85YHgk%2BO1t%2BZULPvYSDYgk4pallTpt54XK5Ls4MwZDs8r5%2BAdR3RmHejItz4lHB4yyivK8F%2FBzwyRSnjUe87qWO6gApxu%2B9%2Bbge3Zodu4EmF9NYtmuMaKdE%2FUyq2rEhT3HcgDFPpuNVENfDomEUjcFxL%2B0cKlp%2FJiXgYBqmLJJ6PJAYdTnqmS0UHPqeMtY6wpbMMDpls4GOqUB8ZNM%2B6%2B6c2WPVyXm3WSwdNjni4ByuLWpfFtvZ%2BgY1Br1D5dYTp0D0wOmob7d7LMivRveQeq7LSUh7eHNn5PoMnUwpEBvq7L9C7MisoJTPARweMVoYwP80ERXmA68zNlaaPAEI2A0dP%2B4ZoIuK%2Bx4m64sfl0w6P7vU3w20nxs6%2Bw4Q0b2R7TtDkb%2FxlIfXR3Kvo0cAmfuxCN68vcisaLZ%2FcoQoIDf&X-Amz-Signature=b4e6a2a7df4c22be6c0f78a0d1d42e465b1141a138f87ecddda56fb9936557c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCZA2F4B%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDp1HGEi3IaKqfgMc5twsdaTbfQXq%2BrTHUPqDPNvAetYAIgMvx4TW0Z1QKamlb1j2GLtyEF4YZXjYLAOILYjtJebToqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQ5CisLL0hUDY4zrSrcAx04P4URnlgDact%2BCByfqpkCUq%2B%2B31zU3B5JmJ5CbwQt%2FNUcUzcI%2Bchaph3QraRY%2BYPZXHiJvgHLYcB4sEKk3jQKoMdCl5sqMehOJ%2BvOME%2BSO063a2qzwndWuE1jXKBJd2WAYswNRGKss0jBFwlcCP5jk1MAr8%2Bu5tAn%2BV%2FBrgQF6NR%2FKVIXM6wyHoik%2FCSd1GBB8zYMaeE1xHq9D8Al3jhpXu162gYkXdkSVcImp87sJQLHtYpW8EvVAprHPqJRTE4P3znCfQw0wkY6L8%2FCkvWV6aaEZzUxftHIKUcJE8SqPRt8CraH6zuwMoD187XRtwp6xfdkQlZLC2eNH7yQ1%2BwJyHjqwOF9wwcPevGJrDPJEGFt1nuFI2OvvsoidapWQ2ra3zOf2%2FAhR5pcsn35HRvJWLfXoqCmtk3NfNatLzJyqpmMF7a3tuNQVX85YHgk%2BO1t%2BZULPvYSDYgk4pallTpt54XK5Ls4MwZDs8r5%2BAdR3RmHejItz4lHB4yyivK8F%2FBzwyRSnjUe87qWO6gApxu%2B9%2Bbge3Zodu4EmF9NYtmuMaKdE%2FUyq2rEhT3HcgDFPpuNVENfDomEUjcFxL%2B0cKlp%2FJiXgYBqmLJJ6PJAYdTnqmS0UHPqeMtY6wpbMMDpls4GOqUB8ZNM%2B6%2B6c2WPVyXm3WSwdNjni4ByuLWpfFtvZ%2BgY1Br1D5dYTp0D0wOmob7d7LMivRveQeq7LSUh7eHNn5PoMnUwpEBvq7L9C7MisoJTPARweMVoYwP80ERXmA68zNlaaPAEI2A0dP%2B4ZoIuK%2Bx4m64sfl0w6P7vU3w20nxs6%2Bw4Q0b2R7TtDkb%2FxlIfXR3Kvo0cAmfuxCN68vcisaLZ%2FcoQoIDf&X-Amz-Signature=3f05f1919e5136f1286cfad19ec6940fa5455a372c2c303564fd3eb4cd0788dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



