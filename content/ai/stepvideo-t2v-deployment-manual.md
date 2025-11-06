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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XEF3YR7%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPTKnzV0pxLmjM%2FGcX05Nm0YL2dHDNpHSCw8coO5sJtQIgRGNHiEj9qaJDVtHD9HXXji%2FkCTjEA3Iibo7p%2FBoxvy0qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIybX2zFOznocmNuTSrcA00JJrfz6snXkri%2F2Ol8sU%2FqwAs6OZGkTmWCOYnIdy1VT2NjhZ6tD5IWnMCaclnc49Qm06FrpFKqClTLJ1fa9sQX8QA6Bg0egsDQ4s%2FFoGnOZ5UHPuL9HHessAnxZ2ocjcoQWkGnfGypPH19vHDeb3fco24S71cOkYrVYvemJRxN2ox9sL1MrX7AyNWAhT6oPQgux%2BqLor8k9Wso1Yz590t05u0yHzrpY3xWMZ0QRzuD2m1Gw1krqLSeXdh91rp3sc5cqk1YKJmA9XBb8XCglJixw6OdxbmuZR0D0yAeDqM6Ym8UTNU8hXJWxbfFJKtRCuaUpLd%2FoKyP1DLPNQUDmOUwkKwk84P7%2FRSomcD1svYY1ZHyWhuX7Lw1eH%2FVHo%2FwQ2RqbtfZt8ePqsjRdaDJIubiunx4DXMb2ecpcuFB65DYnszLWPNhRQFmT3vrX%2F5f7BF5WJoGgHGLW0DhP3kRGDNkW1sl3NDeU4qTatfaRFqgyiFV3Abct%2B9BVPrNn2o0PL3GoZ2yJvopBF1mIoFP16ljC%2B2JDm1yZg%2FDWqDD%2BTmRn3kJP4THaZBSvDkFP4KuKimnDx6zgoyaGPaZsIp4VX8cXQM58Hsl2jfpcoFlUc1qVST%2BRqMu5roNRXqAMNjwr8gGOqUBVAvCX0nVU2ckd6GMSc1W63HJnGKpJODcANp5Ect%2FPii5ZfLhiaytoeoPRvE4MTZP0LW38G82C6QaOzz6h%2Be9GnjqiY4cQI0cKx4M7tFek87vP3iSOth3CTgiyyhHFSUioSPty3x6RIaSxwghA9y4E4OiX2EkKTwVVF5s1rbUSTWtVSCY6PwSV9mH7uVUvE1IGGAspx3ruuLCrgqus11OlSGClLnE&X-Amz-Signature=012fe3a328b0322538b610069ef934bd6f852dc9a386fa3c4f5b543eaa068c9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XEF3YR7%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPTKnzV0pxLmjM%2FGcX05Nm0YL2dHDNpHSCw8coO5sJtQIgRGNHiEj9qaJDVtHD9HXXji%2FkCTjEA3Iibo7p%2FBoxvy0qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIybX2zFOznocmNuTSrcA00JJrfz6snXkri%2F2Ol8sU%2FqwAs6OZGkTmWCOYnIdy1VT2NjhZ6tD5IWnMCaclnc49Qm06FrpFKqClTLJ1fa9sQX8QA6Bg0egsDQ4s%2FFoGnOZ5UHPuL9HHessAnxZ2ocjcoQWkGnfGypPH19vHDeb3fco24S71cOkYrVYvemJRxN2ox9sL1MrX7AyNWAhT6oPQgux%2BqLor8k9Wso1Yz590t05u0yHzrpY3xWMZ0QRzuD2m1Gw1krqLSeXdh91rp3sc5cqk1YKJmA9XBb8XCglJixw6OdxbmuZR0D0yAeDqM6Ym8UTNU8hXJWxbfFJKtRCuaUpLd%2FoKyP1DLPNQUDmOUwkKwk84P7%2FRSomcD1svYY1ZHyWhuX7Lw1eH%2FVHo%2FwQ2RqbtfZt8ePqsjRdaDJIubiunx4DXMb2ecpcuFB65DYnszLWPNhRQFmT3vrX%2F5f7BF5WJoGgHGLW0DhP3kRGDNkW1sl3NDeU4qTatfaRFqgyiFV3Abct%2B9BVPrNn2o0PL3GoZ2yJvopBF1mIoFP16ljC%2B2JDm1yZg%2FDWqDD%2BTmRn3kJP4THaZBSvDkFP4KuKimnDx6zgoyaGPaZsIp4VX8cXQM58Hsl2jfpcoFlUc1qVST%2BRqMu5roNRXqAMNjwr8gGOqUBVAvCX0nVU2ckd6GMSc1W63HJnGKpJODcANp5Ect%2FPii5ZfLhiaytoeoPRvE4MTZP0LW38G82C6QaOzz6h%2Be9GnjqiY4cQI0cKx4M7tFek87vP3iSOth3CTgiyyhHFSUioSPty3x6RIaSxwghA9y4E4OiX2EkKTwVVF5s1rbUSTWtVSCY6PwSV9mH7uVUvE1IGGAspx3ruuLCrgqus11OlSGClLnE&X-Amz-Signature=f09262df5c3a5d38c9dae7fbc646859433ffc25d467f3d45e8e9a668451dfa1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XEF3YR7%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPTKnzV0pxLmjM%2FGcX05Nm0YL2dHDNpHSCw8coO5sJtQIgRGNHiEj9qaJDVtHD9HXXji%2FkCTjEA3Iibo7p%2FBoxvy0qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIybX2zFOznocmNuTSrcA00JJrfz6snXkri%2F2Ol8sU%2FqwAs6OZGkTmWCOYnIdy1VT2NjhZ6tD5IWnMCaclnc49Qm06FrpFKqClTLJ1fa9sQX8QA6Bg0egsDQ4s%2FFoGnOZ5UHPuL9HHessAnxZ2ocjcoQWkGnfGypPH19vHDeb3fco24S71cOkYrVYvemJRxN2ox9sL1MrX7AyNWAhT6oPQgux%2BqLor8k9Wso1Yz590t05u0yHzrpY3xWMZ0QRzuD2m1Gw1krqLSeXdh91rp3sc5cqk1YKJmA9XBb8XCglJixw6OdxbmuZR0D0yAeDqM6Ym8UTNU8hXJWxbfFJKtRCuaUpLd%2FoKyP1DLPNQUDmOUwkKwk84P7%2FRSomcD1svYY1ZHyWhuX7Lw1eH%2FVHo%2FwQ2RqbtfZt8ePqsjRdaDJIubiunx4DXMb2ecpcuFB65DYnszLWPNhRQFmT3vrX%2F5f7BF5WJoGgHGLW0DhP3kRGDNkW1sl3NDeU4qTatfaRFqgyiFV3Abct%2B9BVPrNn2o0PL3GoZ2yJvopBF1mIoFP16ljC%2B2JDm1yZg%2FDWqDD%2BTmRn3kJP4THaZBSvDkFP4KuKimnDx6zgoyaGPaZsIp4VX8cXQM58Hsl2jfpcoFlUc1qVST%2BRqMu5roNRXqAMNjwr8gGOqUBVAvCX0nVU2ckd6GMSc1W63HJnGKpJODcANp5Ect%2FPii5ZfLhiaytoeoPRvE4MTZP0LW38G82C6QaOzz6h%2Be9GnjqiY4cQI0cKx4M7tFek87vP3iSOth3CTgiyyhHFSUioSPty3x6RIaSxwghA9y4E4OiX2EkKTwVVF5s1rbUSTWtVSCY6PwSV9mH7uVUvE1IGGAspx3ruuLCrgqus11OlSGClLnE&X-Amz-Signature=e15c34c07cc88d8b317a7db83cf251345792d26286d24472b95155480d1f56cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XEF3YR7%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPTKnzV0pxLmjM%2FGcX05Nm0YL2dHDNpHSCw8coO5sJtQIgRGNHiEj9qaJDVtHD9HXXji%2FkCTjEA3Iibo7p%2FBoxvy0qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIybX2zFOznocmNuTSrcA00JJrfz6snXkri%2F2Ol8sU%2FqwAs6OZGkTmWCOYnIdy1VT2NjhZ6tD5IWnMCaclnc49Qm06FrpFKqClTLJ1fa9sQX8QA6Bg0egsDQ4s%2FFoGnOZ5UHPuL9HHessAnxZ2ocjcoQWkGnfGypPH19vHDeb3fco24S71cOkYrVYvemJRxN2ox9sL1MrX7AyNWAhT6oPQgux%2BqLor8k9Wso1Yz590t05u0yHzrpY3xWMZ0QRzuD2m1Gw1krqLSeXdh91rp3sc5cqk1YKJmA9XBb8XCglJixw6OdxbmuZR0D0yAeDqM6Ym8UTNU8hXJWxbfFJKtRCuaUpLd%2FoKyP1DLPNQUDmOUwkKwk84P7%2FRSomcD1svYY1ZHyWhuX7Lw1eH%2FVHo%2FwQ2RqbtfZt8ePqsjRdaDJIubiunx4DXMb2ecpcuFB65DYnszLWPNhRQFmT3vrX%2F5f7BF5WJoGgHGLW0DhP3kRGDNkW1sl3NDeU4qTatfaRFqgyiFV3Abct%2B9BVPrNn2o0PL3GoZ2yJvopBF1mIoFP16ljC%2B2JDm1yZg%2FDWqDD%2BTmRn3kJP4THaZBSvDkFP4KuKimnDx6zgoyaGPaZsIp4VX8cXQM58Hsl2jfpcoFlUc1qVST%2BRqMu5roNRXqAMNjwr8gGOqUBVAvCX0nVU2ckd6GMSc1W63HJnGKpJODcANp5Ect%2FPii5ZfLhiaytoeoPRvE4MTZP0LW38G82C6QaOzz6h%2Be9GnjqiY4cQI0cKx4M7tFek87vP3iSOth3CTgiyyhHFSUioSPty3x6RIaSxwghA9y4E4OiX2EkKTwVVF5s1rbUSTWtVSCY6PwSV9mH7uVUvE1IGGAspx3ruuLCrgqus11OlSGClLnE&X-Amz-Signature=f7493d5a57ac7ca91a9ba24eb35947c4914406bc5055ab9ccb2f4e23ffb269d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



