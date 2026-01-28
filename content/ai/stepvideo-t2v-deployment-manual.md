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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RE6PTD7%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuakkaDqxFHY6AaE5JQWEKh1gSuYsmo0mzZFuyhshdNgIhAIp4%2Ff%2Fk%2B7blC68iifwCCfGvm%2FAb%2BCdzDGRcSt%2B%2FqKCkKv8DCGEQABoMNjM3NDIzMTgzODA1IgwXiDW3HYXam3RTGfUq3ANKqNdyqNmJtN2czDCOfLUaMgUPR2gsbFWsaocbq6Qakcy8b3ajt4H%2FGlN7645yE6l4bGx9A5PJXgv%2F5cYBMqWx4BlUyi5be2uDN5VfOBjgEhvkeR5liK0nGmpq%2FumUFSTRGUcXn7U2rLjUwbYJIIFzN%2BplgmWjpbEovujNabBbk3JLR4kNLjpYqHDYQmeD5uUcru3t2CDQ7UnbECE%2BBykp%2B%2FGjZ7VXKbvnmOjBTnhQQOBEyKOWRnjCQK28Nhj51nLZlBqSDPoHu84ZsMsz5mHnfQE6twt6q%2Fvgwz622bgxFLM2S0rTfAsLecvd17bGwqziA3J9nYqFDV%2BfEporRz%2Fm%2B1bt3mYUDLH9J%2B%2BQjkp23j6L5FrA2yQuo7Ite9eprDP%2B7yqYY9NFwTl2D%2B4%2F06dMmdPjLPXrEVZMnDVc%2FwsUwVgEZGwl4j1tNTxsSssM%2BKbK4EkbcSTLXXD4EQFL9ZM6FcihbTm6hmZw%2BDUZpu5wJCGFilEFRDe5%2FAeIiN5fXHJYqMsuOkMfp6hc77sjY5PbzL%2Bfx0PCag59y04S9ShqAUwuZUPnOnP2RmtJvGm2VLAZCIaGw9IA1u%2BwPBhLE5NaxBIunfxnMs0aKXQf%2BEEFkYhkL9%2FJ1kwfN%2B2TXzCRluXLBjqkAaMPbJZ1ILOmKIY0eLI87zd3hnZpDsQjnlYFFhDXm5hAHdFPMsGSXMBR1XjWkdDyNZ%2B0xtJTIyEi870jSdZnvMHuzoRw7d7qkP1%2BOyvo73viXMEFUf8s5QlxP77Xhwz5ZEfrODl81%2FHZs98DMz7j2a9UpseUKuFjESpLM67ETdGjsm5GfoYD2bMgp2EUqwT8cpGTWov374UplMSTLRcluPXRL2CG&X-Amz-Signature=17d06c6b856d8a96240bf8f4f217bf5ca92aacfb6761dc38efdf3522452a13bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RE6PTD7%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuakkaDqxFHY6AaE5JQWEKh1gSuYsmo0mzZFuyhshdNgIhAIp4%2Ff%2Fk%2B7blC68iifwCCfGvm%2FAb%2BCdzDGRcSt%2B%2FqKCkKv8DCGEQABoMNjM3NDIzMTgzODA1IgwXiDW3HYXam3RTGfUq3ANKqNdyqNmJtN2czDCOfLUaMgUPR2gsbFWsaocbq6Qakcy8b3ajt4H%2FGlN7645yE6l4bGx9A5PJXgv%2F5cYBMqWx4BlUyi5be2uDN5VfOBjgEhvkeR5liK0nGmpq%2FumUFSTRGUcXn7U2rLjUwbYJIIFzN%2BplgmWjpbEovujNabBbk3JLR4kNLjpYqHDYQmeD5uUcru3t2CDQ7UnbECE%2BBykp%2B%2FGjZ7VXKbvnmOjBTnhQQOBEyKOWRnjCQK28Nhj51nLZlBqSDPoHu84ZsMsz5mHnfQE6twt6q%2Fvgwz622bgxFLM2S0rTfAsLecvd17bGwqziA3J9nYqFDV%2BfEporRz%2Fm%2B1bt3mYUDLH9J%2B%2BQjkp23j6L5FrA2yQuo7Ite9eprDP%2B7yqYY9NFwTl2D%2B4%2F06dMmdPjLPXrEVZMnDVc%2FwsUwVgEZGwl4j1tNTxsSssM%2BKbK4EkbcSTLXXD4EQFL9ZM6FcihbTm6hmZw%2BDUZpu5wJCGFilEFRDe5%2FAeIiN5fXHJYqMsuOkMfp6hc77sjY5PbzL%2Bfx0PCag59y04S9ShqAUwuZUPnOnP2RmtJvGm2VLAZCIaGw9IA1u%2BwPBhLE5NaxBIunfxnMs0aKXQf%2BEEFkYhkL9%2FJ1kwfN%2B2TXzCRluXLBjqkAaMPbJZ1ILOmKIY0eLI87zd3hnZpDsQjnlYFFhDXm5hAHdFPMsGSXMBR1XjWkdDyNZ%2B0xtJTIyEi870jSdZnvMHuzoRw7d7qkP1%2BOyvo73viXMEFUf8s5QlxP77Xhwz5ZEfrODl81%2FHZs98DMz7j2a9UpseUKuFjESpLM67ETdGjsm5GfoYD2bMgp2EUqwT8cpGTWov374UplMSTLRcluPXRL2CG&X-Amz-Signature=55ad20cd73b2723b07304e562b7368a33a79793d005e8d0699b78755172c522c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RE6PTD7%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuakkaDqxFHY6AaE5JQWEKh1gSuYsmo0mzZFuyhshdNgIhAIp4%2Ff%2Fk%2B7blC68iifwCCfGvm%2FAb%2BCdzDGRcSt%2B%2FqKCkKv8DCGEQABoMNjM3NDIzMTgzODA1IgwXiDW3HYXam3RTGfUq3ANKqNdyqNmJtN2czDCOfLUaMgUPR2gsbFWsaocbq6Qakcy8b3ajt4H%2FGlN7645yE6l4bGx9A5PJXgv%2F5cYBMqWx4BlUyi5be2uDN5VfOBjgEhvkeR5liK0nGmpq%2FumUFSTRGUcXn7U2rLjUwbYJIIFzN%2BplgmWjpbEovujNabBbk3JLR4kNLjpYqHDYQmeD5uUcru3t2CDQ7UnbECE%2BBykp%2B%2FGjZ7VXKbvnmOjBTnhQQOBEyKOWRnjCQK28Nhj51nLZlBqSDPoHu84ZsMsz5mHnfQE6twt6q%2Fvgwz622bgxFLM2S0rTfAsLecvd17bGwqziA3J9nYqFDV%2BfEporRz%2Fm%2B1bt3mYUDLH9J%2B%2BQjkp23j6L5FrA2yQuo7Ite9eprDP%2B7yqYY9NFwTl2D%2B4%2F06dMmdPjLPXrEVZMnDVc%2FwsUwVgEZGwl4j1tNTxsSssM%2BKbK4EkbcSTLXXD4EQFL9ZM6FcihbTm6hmZw%2BDUZpu5wJCGFilEFRDe5%2FAeIiN5fXHJYqMsuOkMfp6hc77sjY5PbzL%2Bfx0PCag59y04S9ShqAUwuZUPnOnP2RmtJvGm2VLAZCIaGw9IA1u%2BwPBhLE5NaxBIunfxnMs0aKXQf%2BEEFkYhkL9%2FJ1kwfN%2B2TXzCRluXLBjqkAaMPbJZ1ILOmKIY0eLI87zd3hnZpDsQjnlYFFhDXm5hAHdFPMsGSXMBR1XjWkdDyNZ%2B0xtJTIyEi870jSdZnvMHuzoRw7d7qkP1%2BOyvo73viXMEFUf8s5QlxP77Xhwz5ZEfrODl81%2FHZs98DMz7j2a9UpseUKuFjESpLM67ETdGjsm5GfoYD2bMgp2EUqwT8cpGTWov374UplMSTLRcluPXRL2CG&X-Amz-Signature=b72a7a3b9de4fcca96a7f7a289050afec8adcfd601be829a4739d5eae6dd5b03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RE6PTD7%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuakkaDqxFHY6AaE5JQWEKh1gSuYsmo0mzZFuyhshdNgIhAIp4%2Ff%2Fk%2B7blC68iifwCCfGvm%2FAb%2BCdzDGRcSt%2B%2FqKCkKv8DCGEQABoMNjM3NDIzMTgzODA1IgwXiDW3HYXam3RTGfUq3ANKqNdyqNmJtN2czDCOfLUaMgUPR2gsbFWsaocbq6Qakcy8b3ajt4H%2FGlN7645yE6l4bGx9A5PJXgv%2F5cYBMqWx4BlUyi5be2uDN5VfOBjgEhvkeR5liK0nGmpq%2FumUFSTRGUcXn7U2rLjUwbYJIIFzN%2BplgmWjpbEovujNabBbk3JLR4kNLjpYqHDYQmeD5uUcru3t2CDQ7UnbECE%2BBykp%2B%2FGjZ7VXKbvnmOjBTnhQQOBEyKOWRnjCQK28Nhj51nLZlBqSDPoHu84ZsMsz5mHnfQE6twt6q%2Fvgwz622bgxFLM2S0rTfAsLecvd17bGwqziA3J9nYqFDV%2BfEporRz%2Fm%2B1bt3mYUDLH9J%2B%2BQjkp23j6L5FrA2yQuo7Ite9eprDP%2B7yqYY9NFwTl2D%2B4%2F06dMmdPjLPXrEVZMnDVc%2FwsUwVgEZGwl4j1tNTxsSssM%2BKbK4EkbcSTLXXD4EQFL9ZM6FcihbTm6hmZw%2BDUZpu5wJCGFilEFRDe5%2FAeIiN5fXHJYqMsuOkMfp6hc77sjY5PbzL%2Bfx0PCag59y04S9ShqAUwuZUPnOnP2RmtJvGm2VLAZCIaGw9IA1u%2BwPBhLE5NaxBIunfxnMs0aKXQf%2BEEFkYhkL9%2FJ1kwfN%2B2TXzCRluXLBjqkAaMPbJZ1ILOmKIY0eLI87zd3hnZpDsQjnlYFFhDXm5hAHdFPMsGSXMBR1XjWkdDyNZ%2B0xtJTIyEi870jSdZnvMHuzoRw7d7qkP1%2BOyvo73viXMEFUf8s5QlxP77Xhwz5ZEfrODl81%2FHZs98DMz7j2a9UpseUKuFjESpLM67ETdGjsm5GfoYD2bMgp2EUqwT8cpGTWov374UplMSTLRcluPXRL2CG&X-Amz-Signature=6e3fa306bab332734b72354c52505bab1d2a5d6ec296802301f24da260bd9161&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



