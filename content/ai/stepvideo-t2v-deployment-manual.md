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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAI3BSK7%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDKCUBjTNARPhUNf2RBdzSKpUEGuDEfKIi3UcpFK6aiAAIgaWNs9cSokOqpYOsv2rjyK7qIfHLugxzuEd8sRZnEyBAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDG3NevY1qJuFzgXbCrcA%2Fz1aflEuIloiM4OWoFpUZszI1ADZZopHNm%2FuyI4agku3npax6nRVPmfq7ZMpliaExt7sC5jACdHyDlmz4s6Nmd4Qgq%2FoFER19GKaGvXz6ay38nlKe4PelcYT5%2Fp%2FSldQlkKO11PHMMPhGUU5nVbdtfNszJ3KijanYPoE9Ym2RuAAKSbFwKreZsKtoYJPJI8p%2FCFyWHDqmo3kEJlU2ymhsEMIgRC32IYVXd8YjXCpy5BYrwbwYqgh73rFHZE04TjgvrL%2FCf9vQLL4qpRaHrGFt%2BiBql8dDPMYWb44%2BGyUYHC6hRQhDpoYW%2FKw9cBdAtd6Ebc6HQ6D6o1nJCZ4os4CwbwPirsobN7haMlVJymybtd5gnV523eNhy8SDQRo8g0SvuFkyM1A%2FqwnYKvaLKTE1r0fQKmJQlSOm2Zc%2FidRzssQack%2FQS5kKbVPO4nzgYVHZk38dBwZIaGHKOvIOLrJejZTEnO6mA8x8dcR%2Bp6iHV0KAkT3F5T7%2FmAf4IkcuIbJ05VGu%2FHX1cRWEm5r7QwwIHasxkxDbV6eNAhVt5W%2FIj%2Fm5mfy9ELy6yrHGyoh%2BQWQrw2PKp2YfNxozgBCmMeYbh3aliarNbbtGR2bbVnuvuXF64e9xEHp%2F2XQ6%2FDMNnMp84GOqUBBQ54wFf2o6aD%2F%2FLFALtg3B7SVtrlmYPD%2Foj%2FaZKnzepyyAwbpbsGRXSJdYSaS4SWw44dV3cWJYoFG%2FT3ZzgYAEUR4Ycarl%2BnWs8Gx9HMigiIY1orIIGWx9Pr50ZF4h1WZ80V9nt9AxoiX%2BdxVgxx%2BlZBmDmDUoXE%2BAYxA4t1WkW2LJC2u3EV5bHYbrnrvAyMiq%2BgJNrubboHJACQGDJABu5afe3s&X-Amz-Signature=1373612f46167660cff02d4760d3b87f77ccd3f7b1c0e34c114def6e2a176496&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAI3BSK7%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDKCUBjTNARPhUNf2RBdzSKpUEGuDEfKIi3UcpFK6aiAAIgaWNs9cSokOqpYOsv2rjyK7qIfHLugxzuEd8sRZnEyBAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDG3NevY1qJuFzgXbCrcA%2Fz1aflEuIloiM4OWoFpUZszI1ADZZopHNm%2FuyI4agku3npax6nRVPmfq7ZMpliaExt7sC5jACdHyDlmz4s6Nmd4Qgq%2FoFER19GKaGvXz6ay38nlKe4PelcYT5%2Fp%2FSldQlkKO11PHMMPhGUU5nVbdtfNszJ3KijanYPoE9Ym2RuAAKSbFwKreZsKtoYJPJI8p%2FCFyWHDqmo3kEJlU2ymhsEMIgRC32IYVXd8YjXCpy5BYrwbwYqgh73rFHZE04TjgvrL%2FCf9vQLL4qpRaHrGFt%2BiBql8dDPMYWb44%2BGyUYHC6hRQhDpoYW%2FKw9cBdAtd6Ebc6HQ6D6o1nJCZ4os4CwbwPirsobN7haMlVJymybtd5gnV523eNhy8SDQRo8g0SvuFkyM1A%2FqwnYKvaLKTE1r0fQKmJQlSOm2Zc%2FidRzssQack%2FQS5kKbVPO4nzgYVHZk38dBwZIaGHKOvIOLrJejZTEnO6mA8x8dcR%2Bp6iHV0KAkT3F5T7%2FmAf4IkcuIbJ05VGu%2FHX1cRWEm5r7QwwIHasxkxDbV6eNAhVt5W%2FIj%2Fm5mfy9ELy6yrHGyoh%2BQWQrw2PKp2YfNxozgBCmMeYbh3aliarNbbtGR2bbVnuvuXF64e9xEHp%2F2XQ6%2FDMNnMp84GOqUBBQ54wFf2o6aD%2F%2FLFALtg3B7SVtrlmYPD%2Foj%2FaZKnzepyyAwbpbsGRXSJdYSaS4SWw44dV3cWJYoFG%2FT3ZzgYAEUR4Ycarl%2BnWs8Gx9HMigiIY1orIIGWx9Pr50ZF4h1WZ80V9nt9AxoiX%2BdxVgxx%2BlZBmDmDUoXE%2BAYxA4t1WkW2LJC2u3EV5bHYbrnrvAyMiq%2BgJNrubboHJACQGDJABu5afe3s&X-Amz-Signature=1628f7e073f616f42350254c5dacdfbef15fdb1dad0494ebe6201faf5d4396c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAI3BSK7%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDKCUBjTNARPhUNf2RBdzSKpUEGuDEfKIi3UcpFK6aiAAIgaWNs9cSokOqpYOsv2rjyK7qIfHLugxzuEd8sRZnEyBAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDG3NevY1qJuFzgXbCrcA%2Fz1aflEuIloiM4OWoFpUZszI1ADZZopHNm%2FuyI4agku3npax6nRVPmfq7ZMpliaExt7sC5jACdHyDlmz4s6Nmd4Qgq%2FoFER19GKaGvXz6ay38nlKe4PelcYT5%2Fp%2FSldQlkKO11PHMMPhGUU5nVbdtfNszJ3KijanYPoE9Ym2RuAAKSbFwKreZsKtoYJPJI8p%2FCFyWHDqmo3kEJlU2ymhsEMIgRC32IYVXd8YjXCpy5BYrwbwYqgh73rFHZE04TjgvrL%2FCf9vQLL4qpRaHrGFt%2BiBql8dDPMYWb44%2BGyUYHC6hRQhDpoYW%2FKw9cBdAtd6Ebc6HQ6D6o1nJCZ4os4CwbwPirsobN7haMlVJymybtd5gnV523eNhy8SDQRo8g0SvuFkyM1A%2FqwnYKvaLKTE1r0fQKmJQlSOm2Zc%2FidRzssQack%2FQS5kKbVPO4nzgYVHZk38dBwZIaGHKOvIOLrJejZTEnO6mA8x8dcR%2Bp6iHV0KAkT3F5T7%2FmAf4IkcuIbJ05VGu%2FHX1cRWEm5r7QwwIHasxkxDbV6eNAhVt5W%2FIj%2Fm5mfy9ELy6yrHGyoh%2BQWQrw2PKp2YfNxozgBCmMeYbh3aliarNbbtGR2bbVnuvuXF64e9xEHp%2F2XQ6%2FDMNnMp84GOqUBBQ54wFf2o6aD%2F%2FLFALtg3B7SVtrlmYPD%2Foj%2FaZKnzepyyAwbpbsGRXSJdYSaS4SWw44dV3cWJYoFG%2FT3ZzgYAEUR4Ycarl%2BnWs8Gx9HMigiIY1orIIGWx9Pr50ZF4h1WZ80V9nt9AxoiX%2BdxVgxx%2BlZBmDmDUoXE%2BAYxA4t1WkW2LJC2u3EV5bHYbrnrvAyMiq%2BgJNrubboHJACQGDJABu5afe3s&X-Amz-Signature=32d47709f22cc1373a0d2df800046450caea4a1c9f71eacc22ac4e7fb6cbe33e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAI3BSK7%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQDKCUBjTNARPhUNf2RBdzSKpUEGuDEfKIi3UcpFK6aiAAIgaWNs9cSokOqpYOsv2rjyK7qIfHLugxzuEd8sRZnEyBAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDG3NevY1qJuFzgXbCrcA%2Fz1aflEuIloiM4OWoFpUZszI1ADZZopHNm%2FuyI4agku3npax6nRVPmfq7ZMpliaExt7sC5jACdHyDlmz4s6Nmd4Qgq%2FoFER19GKaGvXz6ay38nlKe4PelcYT5%2Fp%2FSldQlkKO11PHMMPhGUU5nVbdtfNszJ3KijanYPoE9Ym2RuAAKSbFwKreZsKtoYJPJI8p%2FCFyWHDqmo3kEJlU2ymhsEMIgRC32IYVXd8YjXCpy5BYrwbwYqgh73rFHZE04TjgvrL%2FCf9vQLL4qpRaHrGFt%2BiBql8dDPMYWb44%2BGyUYHC6hRQhDpoYW%2FKw9cBdAtd6Ebc6HQ6D6o1nJCZ4os4CwbwPirsobN7haMlVJymybtd5gnV523eNhy8SDQRo8g0SvuFkyM1A%2FqwnYKvaLKTE1r0fQKmJQlSOm2Zc%2FidRzssQack%2FQS5kKbVPO4nzgYVHZk38dBwZIaGHKOvIOLrJejZTEnO6mA8x8dcR%2Bp6iHV0KAkT3F5T7%2FmAf4IkcuIbJ05VGu%2FHX1cRWEm5r7QwwIHasxkxDbV6eNAhVt5W%2FIj%2Fm5mfy9ELy6yrHGyoh%2BQWQrw2PKp2YfNxozgBCmMeYbh3aliarNbbtGR2bbVnuvuXF64e9xEHp%2F2XQ6%2FDMNnMp84GOqUBBQ54wFf2o6aD%2F%2FLFALtg3B7SVtrlmYPD%2Foj%2FaZKnzepyyAwbpbsGRXSJdYSaS4SWw44dV3cWJYoFG%2FT3ZzgYAEUR4Ycarl%2BnWs8Gx9HMigiIY1orIIGWx9Pr50ZF4h1WZ80V9nt9AxoiX%2BdxVgxx%2BlZBmDmDUoXE%2BAYxA4t1WkW2LJC2u3EV5bHYbrnrvAyMiq%2BgJNrubboHJACQGDJABu5afe3s&X-Amz-Signature=85c28f2bc289b99868f1dca37111c0897253d4955b764f0ce0fbc90945335a75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



