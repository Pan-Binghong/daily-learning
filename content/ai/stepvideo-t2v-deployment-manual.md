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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBKLIBFG%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC0PUH1v87LZmdjGwfmr4Sm2%2B1%2BRjWOpDmCzGTLM5bBxQIgFpJ6Znu2TwqPVrtLPtiG6S8vUJJBg1%2BFzuPcx0Uyuj0q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNHReMlIF1AW65Xk2yrcA4CYRsyl0Ohw9pYme9TrJZv%2FS6BvSjpM11Yug%2BujZX7pHqdIsaSa20nyqCl%2BNFzRckkEP6bydmMZ3s8y7ZD3sNSkyrskks8pL9yf640pDD2QxHFWYRW7ccGRflDhrscWB6L0mhWkDuB7ad1wM%2F5UI%2F4f19Ook7xHyM5w3kyCvktDKu%2FVXjScNtBBrSac%2Fs2aV6m8jbbLuSrawVXxjQCW8P1rza2TiU6HYoO7XCu1KmkDWAYNgN42AO6TiUL5%2Btt%2BWfItdWPBKgcSlo6GCvLzL6CjOxdBmBLOiODnq0qPQdhcza%2FH8srtxG0bPgmpi1LCV461u2BZsOPr3oFS5j4jFhPe59ADCReP5ncxEzPXGWgku5%2FGo8VEgDiy%2FqNPt2%2FFQUvgxIWCeyzpuUT1GZlEO0RK%2BOj5PRVeMhkKGkpfI1CbZK1q5WKriCZ9NB%2FlXcNvhM7SlkHeZspi6%2BKS8D2cFMnEhS3nt%2BzByityx1DvD7D%2Fw0UFLRnBXX3FYiWF8bFQXtKgOUCU9vvf9vlQuXTloQv9kZTVrfhFFIxe4BWGB1KBAU46Sy7yoDzwpvFHqPJHQvwZszaPz6YETpHdtfrVQl3hu6DQxjEyizKqTYShOcOrvDRMktLjtTmv%2FaTcMKmf%2F8gGOqUBkFreRQ3XC4b3cmItVWHYzbz8QRaKIWrstcyIuntO%2FvLdASK0cTtf%2FKIGIg9rlCPnXSy2WwqcvaSLmOS2AbaAxmmdorvqOlW5ZT7rEjMHjwV4Ffbw5vkWnDAHoYuHmtXmaqMunrb20x3mGPM7JtpzZCUjejdCk9F2y%2Fn3zV%2FTK3AcO73R0hFHgy3JHiZmmPINSbNE7Ut%2Bt5LZ%2FgAHGQ4RVdu0tUjy&X-Amz-Signature=323bef4778741c95f40232048307fdd767620b78da7c928d152f48e4a25aec60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBKLIBFG%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC0PUH1v87LZmdjGwfmr4Sm2%2B1%2BRjWOpDmCzGTLM5bBxQIgFpJ6Znu2TwqPVrtLPtiG6S8vUJJBg1%2BFzuPcx0Uyuj0q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNHReMlIF1AW65Xk2yrcA4CYRsyl0Ohw9pYme9TrJZv%2FS6BvSjpM11Yug%2BujZX7pHqdIsaSa20nyqCl%2BNFzRckkEP6bydmMZ3s8y7ZD3sNSkyrskks8pL9yf640pDD2QxHFWYRW7ccGRflDhrscWB6L0mhWkDuB7ad1wM%2F5UI%2F4f19Ook7xHyM5w3kyCvktDKu%2FVXjScNtBBrSac%2Fs2aV6m8jbbLuSrawVXxjQCW8P1rza2TiU6HYoO7XCu1KmkDWAYNgN42AO6TiUL5%2Btt%2BWfItdWPBKgcSlo6GCvLzL6CjOxdBmBLOiODnq0qPQdhcza%2FH8srtxG0bPgmpi1LCV461u2BZsOPr3oFS5j4jFhPe59ADCReP5ncxEzPXGWgku5%2FGo8VEgDiy%2FqNPt2%2FFQUvgxIWCeyzpuUT1GZlEO0RK%2BOj5PRVeMhkKGkpfI1CbZK1q5WKriCZ9NB%2FlXcNvhM7SlkHeZspi6%2BKS8D2cFMnEhS3nt%2BzByityx1DvD7D%2Fw0UFLRnBXX3FYiWF8bFQXtKgOUCU9vvf9vlQuXTloQv9kZTVrfhFFIxe4BWGB1KBAU46Sy7yoDzwpvFHqPJHQvwZszaPz6YETpHdtfrVQl3hu6DQxjEyizKqTYShOcOrvDRMktLjtTmv%2FaTcMKmf%2F8gGOqUBkFreRQ3XC4b3cmItVWHYzbz8QRaKIWrstcyIuntO%2FvLdASK0cTtf%2FKIGIg9rlCPnXSy2WwqcvaSLmOS2AbaAxmmdorvqOlW5ZT7rEjMHjwV4Ffbw5vkWnDAHoYuHmtXmaqMunrb20x3mGPM7JtpzZCUjejdCk9F2y%2Fn3zV%2FTK3AcO73R0hFHgy3JHiZmmPINSbNE7Ut%2Bt5LZ%2FgAHGQ4RVdu0tUjy&X-Amz-Signature=7df0a855f731f2cc2449df14e60933d4468983d8f2a93477c0e9b7377c9907f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBKLIBFG%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC0PUH1v87LZmdjGwfmr4Sm2%2B1%2BRjWOpDmCzGTLM5bBxQIgFpJ6Znu2TwqPVrtLPtiG6S8vUJJBg1%2BFzuPcx0Uyuj0q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNHReMlIF1AW65Xk2yrcA4CYRsyl0Ohw9pYme9TrJZv%2FS6BvSjpM11Yug%2BujZX7pHqdIsaSa20nyqCl%2BNFzRckkEP6bydmMZ3s8y7ZD3sNSkyrskks8pL9yf640pDD2QxHFWYRW7ccGRflDhrscWB6L0mhWkDuB7ad1wM%2F5UI%2F4f19Ook7xHyM5w3kyCvktDKu%2FVXjScNtBBrSac%2Fs2aV6m8jbbLuSrawVXxjQCW8P1rza2TiU6HYoO7XCu1KmkDWAYNgN42AO6TiUL5%2Btt%2BWfItdWPBKgcSlo6GCvLzL6CjOxdBmBLOiODnq0qPQdhcza%2FH8srtxG0bPgmpi1LCV461u2BZsOPr3oFS5j4jFhPe59ADCReP5ncxEzPXGWgku5%2FGo8VEgDiy%2FqNPt2%2FFQUvgxIWCeyzpuUT1GZlEO0RK%2BOj5PRVeMhkKGkpfI1CbZK1q5WKriCZ9NB%2FlXcNvhM7SlkHeZspi6%2BKS8D2cFMnEhS3nt%2BzByityx1DvD7D%2Fw0UFLRnBXX3FYiWF8bFQXtKgOUCU9vvf9vlQuXTloQv9kZTVrfhFFIxe4BWGB1KBAU46Sy7yoDzwpvFHqPJHQvwZszaPz6YETpHdtfrVQl3hu6DQxjEyizKqTYShOcOrvDRMktLjtTmv%2FaTcMKmf%2F8gGOqUBkFreRQ3XC4b3cmItVWHYzbz8QRaKIWrstcyIuntO%2FvLdASK0cTtf%2FKIGIg9rlCPnXSy2WwqcvaSLmOS2AbaAxmmdorvqOlW5ZT7rEjMHjwV4Ffbw5vkWnDAHoYuHmtXmaqMunrb20x3mGPM7JtpzZCUjejdCk9F2y%2Fn3zV%2FTK3AcO73R0hFHgy3JHiZmmPINSbNE7Ut%2Bt5LZ%2FgAHGQ4RVdu0tUjy&X-Amz-Signature=e4bda687c0e33ef4d6bcb330ab50d25bcd5557ad0d8a1c212e817986e221e409&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBKLIBFG%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC0PUH1v87LZmdjGwfmr4Sm2%2B1%2BRjWOpDmCzGTLM5bBxQIgFpJ6Znu2TwqPVrtLPtiG6S8vUJJBg1%2BFzuPcx0Uyuj0q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNHReMlIF1AW65Xk2yrcA4CYRsyl0Ohw9pYme9TrJZv%2FS6BvSjpM11Yug%2BujZX7pHqdIsaSa20nyqCl%2BNFzRckkEP6bydmMZ3s8y7ZD3sNSkyrskks8pL9yf640pDD2QxHFWYRW7ccGRflDhrscWB6L0mhWkDuB7ad1wM%2F5UI%2F4f19Ook7xHyM5w3kyCvktDKu%2FVXjScNtBBrSac%2Fs2aV6m8jbbLuSrawVXxjQCW8P1rza2TiU6HYoO7XCu1KmkDWAYNgN42AO6TiUL5%2Btt%2BWfItdWPBKgcSlo6GCvLzL6CjOxdBmBLOiODnq0qPQdhcza%2FH8srtxG0bPgmpi1LCV461u2BZsOPr3oFS5j4jFhPe59ADCReP5ncxEzPXGWgku5%2FGo8VEgDiy%2FqNPt2%2FFQUvgxIWCeyzpuUT1GZlEO0RK%2BOj5PRVeMhkKGkpfI1CbZK1q5WKriCZ9NB%2FlXcNvhM7SlkHeZspi6%2BKS8D2cFMnEhS3nt%2BzByityx1DvD7D%2Fw0UFLRnBXX3FYiWF8bFQXtKgOUCU9vvf9vlQuXTloQv9kZTVrfhFFIxe4BWGB1KBAU46Sy7yoDzwpvFHqPJHQvwZszaPz6YETpHdtfrVQl3hu6DQxjEyizKqTYShOcOrvDRMktLjtTmv%2FaTcMKmf%2F8gGOqUBkFreRQ3XC4b3cmItVWHYzbz8QRaKIWrstcyIuntO%2FvLdASK0cTtf%2FKIGIg9rlCPnXSy2WwqcvaSLmOS2AbaAxmmdorvqOlW5ZT7rEjMHjwV4Ffbw5vkWnDAHoYuHmtXmaqMunrb20x3mGPM7JtpzZCUjejdCk9F2y%2Fn3zV%2FTK3AcO73R0hFHgy3JHiZmmPINSbNE7Ut%2Bt5LZ%2FgAHGQ4RVdu0tUjy&X-Amz-Signature=aa73be12784f00808e87e8661cc170180aae6cc43f9e55fea8280a8167f05e67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



