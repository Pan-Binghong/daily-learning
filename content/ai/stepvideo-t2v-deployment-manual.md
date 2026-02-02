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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKJFI6L%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHhj%2FBHj4E4NxfjUCTHdvB9NKbyDsa4wInA8fWvgcgz7AiAgjgfviFs1t4JMKUVnQ0Lx2cNgfVnA0sf3WBUq0wFIBSqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmwfnHHaFf5yC9tkJKtwDVxy%2BLUbYTxLkbWquyktlgamY5aBX7dlr8HgGa%2F%2Bx8KQ1Hy40lx%2BOi6PYD1FFfXVHh55DnjQnsHZuf0Tf%2FZvvZe2GAiGRUVImQniQvwNzg2J%2BPfTZgJTo0sLKJ1LFxm4nSDvk4bnBxyE8ur6wHtt2gV%2FwvaTWxWl8JmgVRorZ6kc1OBaUDNB8A%2FGWnXtoKB1Tqk5RTpgyebkhoRa%2F2NJUfe8dEBSPfgNCB4OOec4tr5PGRgQBN%2BKB597xgfpyd5STrFaXplBIeLpVb6zap0peOIHMNkBmFfSuvbiFo9yE%2F3rpWraCxFmo9mcH0CKEgPAsL02CJD6Wz%2BzOTseB7KPs36NrOmIWKIKUupJziaEjcFiqSzIVUmOjuMlk%2BsSDpQp9SsGZJ%2BmkVBOXmEv6BnYGy3D%2FBZ1UVKIPv1cSXH8vkbR5jXMj93mVGs%2BQtPxtt%2FHLraSiv42YKabB0vX12QFtvX5D3ImHNFq1hgWQBDCJnuzW4l7vb2me5IBnsHIVIg8Tw7MlUf0kePVgTtzx8%2BanDdogfEVI%2BVla1trBiLTmL%2FX%2BQtBbUDMAZ6rcl%2FTcYBUVi7eO1aldO%2FnFs2KD5foK8Z96LdpN4rgwKW36tt00u4D2PlKmika4NGEXJlQwxIaAzAY6pgG9s%2FQ4OaHbGfb%2ByS2YNMk76YxT5AheScVmikevkbytb37OvxXuNPZSQcZbAlYCM8ChQ4gvaK32fPc7LbkqqCjWyFS5hyO2bRmizH3YXLhwdRZ91ls%2BSHYCJmdJot506RNIQeNVSCUT5Chssh5DLi%2B51Zgepqfjki3CV5m7CSUVf3nj2U7wVkeiyqLA%2FR5G6vTnpLpJzNV2a7KLMgK%2B5cGqrr7PELdE&X-Amz-Signature=826c1b270e09f840c00bf61d3d64ddf7a7a3737821075891d1c9a071e48a917a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKJFI6L%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHhj%2FBHj4E4NxfjUCTHdvB9NKbyDsa4wInA8fWvgcgz7AiAgjgfviFs1t4JMKUVnQ0Lx2cNgfVnA0sf3WBUq0wFIBSqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmwfnHHaFf5yC9tkJKtwDVxy%2BLUbYTxLkbWquyktlgamY5aBX7dlr8HgGa%2F%2Bx8KQ1Hy40lx%2BOi6PYD1FFfXVHh55DnjQnsHZuf0Tf%2FZvvZe2GAiGRUVImQniQvwNzg2J%2BPfTZgJTo0sLKJ1LFxm4nSDvk4bnBxyE8ur6wHtt2gV%2FwvaTWxWl8JmgVRorZ6kc1OBaUDNB8A%2FGWnXtoKB1Tqk5RTpgyebkhoRa%2F2NJUfe8dEBSPfgNCB4OOec4tr5PGRgQBN%2BKB597xgfpyd5STrFaXplBIeLpVb6zap0peOIHMNkBmFfSuvbiFo9yE%2F3rpWraCxFmo9mcH0CKEgPAsL02CJD6Wz%2BzOTseB7KPs36NrOmIWKIKUupJziaEjcFiqSzIVUmOjuMlk%2BsSDpQp9SsGZJ%2BmkVBOXmEv6BnYGy3D%2FBZ1UVKIPv1cSXH8vkbR5jXMj93mVGs%2BQtPxtt%2FHLraSiv42YKabB0vX12QFtvX5D3ImHNFq1hgWQBDCJnuzW4l7vb2me5IBnsHIVIg8Tw7MlUf0kePVgTtzx8%2BanDdogfEVI%2BVla1trBiLTmL%2FX%2BQtBbUDMAZ6rcl%2FTcYBUVi7eO1aldO%2FnFs2KD5foK8Z96LdpN4rgwKW36tt00u4D2PlKmika4NGEXJlQwxIaAzAY6pgG9s%2FQ4OaHbGfb%2ByS2YNMk76YxT5AheScVmikevkbytb37OvxXuNPZSQcZbAlYCM8ChQ4gvaK32fPc7LbkqqCjWyFS5hyO2bRmizH3YXLhwdRZ91ls%2BSHYCJmdJot506RNIQeNVSCUT5Chssh5DLi%2B51Zgepqfjki3CV5m7CSUVf3nj2U7wVkeiyqLA%2FR5G6vTnpLpJzNV2a7KLMgK%2B5cGqrr7PELdE&X-Amz-Signature=24c635c5d588c503268d90d00417d0bf83f6a283e53bac44d2d5d033101563e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKJFI6L%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHhj%2FBHj4E4NxfjUCTHdvB9NKbyDsa4wInA8fWvgcgz7AiAgjgfviFs1t4JMKUVnQ0Lx2cNgfVnA0sf3WBUq0wFIBSqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmwfnHHaFf5yC9tkJKtwDVxy%2BLUbYTxLkbWquyktlgamY5aBX7dlr8HgGa%2F%2Bx8KQ1Hy40lx%2BOi6PYD1FFfXVHh55DnjQnsHZuf0Tf%2FZvvZe2GAiGRUVImQniQvwNzg2J%2BPfTZgJTo0sLKJ1LFxm4nSDvk4bnBxyE8ur6wHtt2gV%2FwvaTWxWl8JmgVRorZ6kc1OBaUDNB8A%2FGWnXtoKB1Tqk5RTpgyebkhoRa%2F2NJUfe8dEBSPfgNCB4OOec4tr5PGRgQBN%2BKB597xgfpyd5STrFaXplBIeLpVb6zap0peOIHMNkBmFfSuvbiFo9yE%2F3rpWraCxFmo9mcH0CKEgPAsL02CJD6Wz%2BzOTseB7KPs36NrOmIWKIKUupJziaEjcFiqSzIVUmOjuMlk%2BsSDpQp9SsGZJ%2BmkVBOXmEv6BnYGy3D%2FBZ1UVKIPv1cSXH8vkbR5jXMj93mVGs%2BQtPxtt%2FHLraSiv42YKabB0vX12QFtvX5D3ImHNFq1hgWQBDCJnuzW4l7vb2me5IBnsHIVIg8Tw7MlUf0kePVgTtzx8%2BanDdogfEVI%2BVla1trBiLTmL%2FX%2BQtBbUDMAZ6rcl%2FTcYBUVi7eO1aldO%2FnFs2KD5foK8Z96LdpN4rgwKW36tt00u4D2PlKmika4NGEXJlQwxIaAzAY6pgG9s%2FQ4OaHbGfb%2ByS2YNMk76YxT5AheScVmikevkbytb37OvxXuNPZSQcZbAlYCM8ChQ4gvaK32fPc7LbkqqCjWyFS5hyO2bRmizH3YXLhwdRZ91ls%2BSHYCJmdJot506RNIQeNVSCUT5Chssh5DLi%2B51Zgepqfjki3CV5m7CSUVf3nj2U7wVkeiyqLA%2FR5G6vTnpLpJzNV2a7KLMgK%2B5cGqrr7PELdE&X-Amz-Signature=5f60c6c2e25e011cc2884b0332f5e2b1a43cdae7b8ece359d7b60263193d5742&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LKJFI6L%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHhj%2FBHj4E4NxfjUCTHdvB9NKbyDsa4wInA8fWvgcgz7AiAgjgfviFs1t4JMKUVnQ0Lx2cNgfVnA0sf3WBUq0wFIBSqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmwfnHHaFf5yC9tkJKtwDVxy%2BLUbYTxLkbWquyktlgamY5aBX7dlr8HgGa%2F%2Bx8KQ1Hy40lx%2BOi6PYD1FFfXVHh55DnjQnsHZuf0Tf%2FZvvZe2GAiGRUVImQniQvwNzg2J%2BPfTZgJTo0sLKJ1LFxm4nSDvk4bnBxyE8ur6wHtt2gV%2FwvaTWxWl8JmgVRorZ6kc1OBaUDNB8A%2FGWnXtoKB1Tqk5RTpgyebkhoRa%2F2NJUfe8dEBSPfgNCB4OOec4tr5PGRgQBN%2BKB597xgfpyd5STrFaXplBIeLpVb6zap0peOIHMNkBmFfSuvbiFo9yE%2F3rpWraCxFmo9mcH0CKEgPAsL02CJD6Wz%2BzOTseB7KPs36NrOmIWKIKUupJziaEjcFiqSzIVUmOjuMlk%2BsSDpQp9SsGZJ%2BmkVBOXmEv6BnYGy3D%2FBZ1UVKIPv1cSXH8vkbR5jXMj93mVGs%2BQtPxtt%2FHLraSiv42YKabB0vX12QFtvX5D3ImHNFq1hgWQBDCJnuzW4l7vb2me5IBnsHIVIg8Tw7MlUf0kePVgTtzx8%2BanDdogfEVI%2BVla1trBiLTmL%2FX%2BQtBbUDMAZ6rcl%2FTcYBUVi7eO1aldO%2FnFs2KD5foK8Z96LdpN4rgwKW36tt00u4D2PlKmika4NGEXJlQwxIaAzAY6pgG9s%2FQ4OaHbGfb%2ByS2YNMk76YxT5AheScVmikevkbytb37OvxXuNPZSQcZbAlYCM8ChQ4gvaK32fPc7LbkqqCjWyFS5hyO2bRmizH3YXLhwdRZ91ls%2BSHYCJmdJot506RNIQeNVSCUT5Chssh5DLi%2B51Zgepqfjki3CV5m7CSUVf3nj2U7wVkeiyqLA%2FR5G6vTnpLpJzNV2a7KLMgK%2B5cGqrr7PELdE&X-Amz-Signature=2813bf4cf4e49e5b967e4b8a057ca69dd694d45368fbf13cd730b97366f81633&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



