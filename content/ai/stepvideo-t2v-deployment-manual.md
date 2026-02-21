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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMJRES2O%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBZwCIR2L4ay1NVIpP8%2BQUqOzH2DW4Q31yTIgB6%2Fsp3AIhAK%2BLyT%2BQtVNlvfnHM1zGmdU9qw%2B0wSG6RTLnwWoHfY7wKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRakthnpUEM0LuYj0q3APyFpmUm16Y%2F2vG9ENhbQT5emt%2FmenVohBDxlgXw%2Byu3S%2BAv0lclQ4nSLFbfemSAXoDap0z8%2F9yMRXakqmT9bgc2VbVa6fLVEtW009UVuOQw17lNd6nX1LYL6BQZJGP%2FEW7SCRB%2FSnLCbRiNgWFiEykhsM5uLxd45EAAGURQ%2BNKn9RnxkzLMLkcT%2FIJD7EvIvWHREJO%2BfUhF2p421o%2BzuCdKXKVO%2Fc5X4KmUG8qwzQFQXbk7bsXf%2BxemomHzmXL0gH3Nb4Pk9emaJbNaQNFvSMIvRm4xdG75mnZbQFuQYsT5P7rEuJn7uwLNC2K6CoHdrJbcQSFgnnHZUu7oDdsEm%2BC6MC%2F1lNeTE5mCw4VIzCF2Kmwkqd7ZqoSO%2Bd7JFjQ%2BrpbZVurBVtHsT%2FUgqWBSnKY4TRF%2B9IXzk02ClMSKM%2B66Vc%2FZI1MARFrDJ7WymlLZjjnFluyuWFqrBqMuz2KN3YDUzUmfzN7Zs5DiAtcQhuAW2bqT3rF0Di66qS%2B45YnlWF95l4F2IHtQ%2FvafyPhcX4M4L5n6hkKI%2Fyda0CqGXvKq0qff9mF%2FUSFjDCasEHsQwqxnMTWnxnB2AK0y%2F5sO0l7OqGGogAr3bMFKLvhfdSvll%2B1h60%2B9%2FqSJVPXVTCxveTMBjqkAVd3FVRpLJtosBRuqWhwTbrxEFqnXIzy%2Bw3DYxtxxNsFHZq1Lp0EkptIkg1d%2FeuMkP3JIpSNpmxAmf%2BIXscOkrhj6eb5LwHdcPuGdKPXHrWDFoaBZPzTK2pM7VGeq%2BWfoV7d9s9rWuu2qjwqEOrdCHZ72Qc7X1aeXoL5zXOY%2FOW8%2FVWb%2B%2FiPl1id1%2FGU1wPIpCrqlV%2BKIMWx0En6%2BXYUgyOrNzKv&X-Amz-Signature=9f37d596806d4beddf9fa89e44e4e2a32d63026fab6cbcbc655bc82d7d2bd278&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMJRES2O%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBZwCIR2L4ay1NVIpP8%2BQUqOzH2DW4Q31yTIgB6%2Fsp3AIhAK%2BLyT%2BQtVNlvfnHM1zGmdU9qw%2B0wSG6RTLnwWoHfY7wKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRakthnpUEM0LuYj0q3APyFpmUm16Y%2F2vG9ENhbQT5emt%2FmenVohBDxlgXw%2Byu3S%2BAv0lclQ4nSLFbfemSAXoDap0z8%2F9yMRXakqmT9bgc2VbVa6fLVEtW009UVuOQw17lNd6nX1LYL6BQZJGP%2FEW7SCRB%2FSnLCbRiNgWFiEykhsM5uLxd45EAAGURQ%2BNKn9RnxkzLMLkcT%2FIJD7EvIvWHREJO%2BfUhF2p421o%2BzuCdKXKVO%2Fc5X4KmUG8qwzQFQXbk7bsXf%2BxemomHzmXL0gH3Nb4Pk9emaJbNaQNFvSMIvRm4xdG75mnZbQFuQYsT5P7rEuJn7uwLNC2K6CoHdrJbcQSFgnnHZUu7oDdsEm%2BC6MC%2F1lNeTE5mCw4VIzCF2Kmwkqd7ZqoSO%2Bd7JFjQ%2BrpbZVurBVtHsT%2FUgqWBSnKY4TRF%2B9IXzk02ClMSKM%2B66Vc%2FZI1MARFrDJ7WymlLZjjnFluyuWFqrBqMuz2KN3YDUzUmfzN7Zs5DiAtcQhuAW2bqT3rF0Di66qS%2B45YnlWF95l4F2IHtQ%2FvafyPhcX4M4L5n6hkKI%2Fyda0CqGXvKq0qff9mF%2FUSFjDCasEHsQwqxnMTWnxnB2AK0y%2F5sO0l7OqGGogAr3bMFKLvhfdSvll%2B1h60%2B9%2FqSJVPXVTCxveTMBjqkAVd3FVRpLJtosBRuqWhwTbrxEFqnXIzy%2Bw3DYxtxxNsFHZq1Lp0EkptIkg1d%2FeuMkP3JIpSNpmxAmf%2BIXscOkrhj6eb5LwHdcPuGdKPXHrWDFoaBZPzTK2pM7VGeq%2BWfoV7d9s9rWuu2qjwqEOrdCHZ72Qc7X1aeXoL5zXOY%2FOW8%2FVWb%2B%2FiPl1id1%2FGU1wPIpCrqlV%2BKIMWx0En6%2BXYUgyOrNzKv&X-Amz-Signature=83ac1c8747813cc39375ec3c9c3327741521864e4073aae20804b7ad536d72c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMJRES2O%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBZwCIR2L4ay1NVIpP8%2BQUqOzH2DW4Q31yTIgB6%2Fsp3AIhAK%2BLyT%2BQtVNlvfnHM1zGmdU9qw%2B0wSG6RTLnwWoHfY7wKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRakthnpUEM0LuYj0q3APyFpmUm16Y%2F2vG9ENhbQT5emt%2FmenVohBDxlgXw%2Byu3S%2BAv0lclQ4nSLFbfemSAXoDap0z8%2F9yMRXakqmT9bgc2VbVa6fLVEtW009UVuOQw17lNd6nX1LYL6BQZJGP%2FEW7SCRB%2FSnLCbRiNgWFiEykhsM5uLxd45EAAGURQ%2BNKn9RnxkzLMLkcT%2FIJD7EvIvWHREJO%2BfUhF2p421o%2BzuCdKXKVO%2Fc5X4KmUG8qwzQFQXbk7bsXf%2BxemomHzmXL0gH3Nb4Pk9emaJbNaQNFvSMIvRm4xdG75mnZbQFuQYsT5P7rEuJn7uwLNC2K6CoHdrJbcQSFgnnHZUu7oDdsEm%2BC6MC%2F1lNeTE5mCw4VIzCF2Kmwkqd7ZqoSO%2Bd7JFjQ%2BrpbZVurBVtHsT%2FUgqWBSnKY4TRF%2B9IXzk02ClMSKM%2B66Vc%2FZI1MARFrDJ7WymlLZjjnFluyuWFqrBqMuz2KN3YDUzUmfzN7Zs5DiAtcQhuAW2bqT3rF0Di66qS%2B45YnlWF95l4F2IHtQ%2FvafyPhcX4M4L5n6hkKI%2Fyda0CqGXvKq0qff9mF%2FUSFjDCasEHsQwqxnMTWnxnB2AK0y%2F5sO0l7OqGGogAr3bMFKLvhfdSvll%2B1h60%2B9%2FqSJVPXVTCxveTMBjqkAVd3FVRpLJtosBRuqWhwTbrxEFqnXIzy%2Bw3DYxtxxNsFHZq1Lp0EkptIkg1d%2FeuMkP3JIpSNpmxAmf%2BIXscOkrhj6eb5LwHdcPuGdKPXHrWDFoaBZPzTK2pM7VGeq%2BWfoV7d9s9rWuu2qjwqEOrdCHZ72Qc7X1aeXoL5zXOY%2FOW8%2FVWb%2B%2FiPl1id1%2FGU1wPIpCrqlV%2BKIMWx0En6%2BXYUgyOrNzKv&X-Amz-Signature=0a9a7b64019221ba953d59c11cb21c8c932aaa98bd770a85faeb736772e13c37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMJRES2O%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBZwCIR2L4ay1NVIpP8%2BQUqOzH2DW4Q31yTIgB6%2Fsp3AIhAK%2BLyT%2BQtVNlvfnHM1zGmdU9qw%2B0wSG6RTLnwWoHfY7wKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRakthnpUEM0LuYj0q3APyFpmUm16Y%2F2vG9ENhbQT5emt%2FmenVohBDxlgXw%2Byu3S%2BAv0lclQ4nSLFbfemSAXoDap0z8%2F9yMRXakqmT9bgc2VbVa6fLVEtW009UVuOQw17lNd6nX1LYL6BQZJGP%2FEW7SCRB%2FSnLCbRiNgWFiEykhsM5uLxd45EAAGURQ%2BNKn9RnxkzLMLkcT%2FIJD7EvIvWHREJO%2BfUhF2p421o%2BzuCdKXKVO%2Fc5X4KmUG8qwzQFQXbk7bsXf%2BxemomHzmXL0gH3Nb4Pk9emaJbNaQNFvSMIvRm4xdG75mnZbQFuQYsT5P7rEuJn7uwLNC2K6CoHdrJbcQSFgnnHZUu7oDdsEm%2BC6MC%2F1lNeTE5mCw4VIzCF2Kmwkqd7ZqoSO%2Bd7JFjQ%2BrpbZVurBVtHsT%2FUgqWBSnKY4TRF%2B9IXzk02ClMSKM%2B66Vc%2FZI1MARFrDJ7WymlLZjjnFluyuWFqrBqMuz2KN3YDUzUmfzN7Zs5DiAtcQhuAW2bqT3rF0Di66qS%2B45YnlWF95l4F2IHtQ%2FvafyPhcX4M4L5n6hkKI%2Fyda0CqGXvKq0qff9mF%2FUSFjDCasEHsQwqxnMTWnxnB2AK0y%2F5sO0l7OqGGogAr3bMFKLvhfdSvll%2B1h60%2B9%2FqSJVPXVTCxveTMBjqkAVd3FVRpLJtosBRuqWhwTbrxEFqnXIzy%2Bw3DYxtxxNsFHZq1Lp0EkptIkg1d%2FeuMkP3JIpSNpmxAmf%2BIXscOkrhj6eb5LwHdcPuGdKPXHrWDFoaBZPzTK2pM7VGeq%2BWfoV7d9s9rWuu2qjwqEOrdCHZ72Qc7X1aeXoL5zXOY%2FOW8%2FVWb%2B%2FiPl1id1%2FGU1wPIpCrqlV%2BKIMWx0En6%2BXYUgyOrNzKv&X-Amz-Signature=2c475130984d5c32bf3467adc835fd30e1a9fc5d69044364066f8165941e93c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



