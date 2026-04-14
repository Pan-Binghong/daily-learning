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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIFI7JB%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHO1G4EfSvXUh2qOJaEHHfkLHp3sVPIsLU5%2FAivBxpT4AiAMZ1%2BMTXxVrJbEBJBaPKxd5DCFFVxvBoPVK6offOPUxyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYI5nmCuO0orXVOzMKtwDCjDmJekUKxTjPYCKufKmvRetv9kea4GBIXwA8tzPAQeUP32%2B0Ugz9w6Tt%2BQGm1X8spkzz8moZnLAJV0r6wFcYAFEp6MIui2%2BHv8CevZ0RAoGBxGmfYI3xvEaI6WJKh3hU%2FxO1wBeEUZmCWutjJqmKt7tD%2Fi6v2%2BbbkUNaTRA%2BdQjwYbuHKBdpZA7G5XsqYXh714Xs%2FM%2F6BU4hiwJDAKEnax8w6eF0eioPbe84klj5bPcgwWDnA5xleblJwDCUc6lmQOzxxTNxGQ7VGnoPmiBQoKVlQLDFd6QHqi0HTRqpHdSzv4Ua8l45NcTXjaTkYto58x1lZkNRZA0sNSopmJhqJzkGAgfnFMu9HGFlyRFO1cQ7ynRy16VC%2BLW64Wa4NLfmkqg0MYn82VCauia82xGR1gDMBGN2pAiRxXdAFo9tLBln%2BdIX9mFlyZYbPHHD46II%2BKAFUvPZG%2FD97z%2Fv%2FGHeiSjjokWJxBn0Anc529qlMVHnNDaMdBj5vUX8HU41LZgtb2DurZ%2FrIFLmT50fEBTbqY7MEZNpbZLdHabEPvydNPQkklo5heUTZA0qhuTdkQz9H1oPIYjqRKtYG7EmWyP7c%2BowcXswMa2PS3E%2BezSA6jbKuPuKNmn4%2F50mQEwi%2BH2zgY6pgFx3fhZpqvXvBJM9xP8BTo9X%2Bz4xKZWz1vRWeaXd2qXDQxpn%2BvO9DBnMcFHMmhskEfyUF2ArD9lWYcdOj7iZ6uHX4VScT9eCbfUJBNrKZoizLmc22%2BtNVEvs7DVn6q7N3XXFEvtpiMr19NnnFShlYD%2BOmahYqxAz9OKpuBAYYMQar1GgZUlFa30V1mW3JkT2urjfH3Byrb6FW8yT5BUNgflZSqRjcwz&X-Amz-Signature=9471701b9b9d6a3c540e01d5cb6f9760848add4d0c191a42b30e6440b5cd1658&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIFI7JB%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHO1G4EfSvXUh2qOJaEHHfkLHp3sVPIsLU5%2FAivBxpT4AiAMZ1%2BMTXxVrJbEBJBaPKxd5DCFFVxvBoPVK6offOPUxyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYI5nmCuO0orXVOzMKtwDCjDmJekUKxTjPYCKufKmvRetv9kea4GBIXwA8tzPAQeUP32%2B0Ugz9w6Tt%2BQGm1X8spkzz8moZnLAJV0r6wFcYAFEp6MIui2%2BHv8CevZ0RAoGBxGmfYI3xvEaI6WJKh3hU%2FxO1wBeEUZmCWutjJqmKt7tD%2Fi6v2%2BbbkUNaTRA%2BdQjwYbuHKBdpZA7G5XsqYXh714Xs%2FM%2F6BU4hiwJDAKEnax8w6eF0eioPbe84klj5bPcgwWDnA5xleblJwDCUc6lmQOzxxTNxGQ7VGnoPmiBQoKVlQLDFd6QHqi0HTRqpHdSzv4Ua8l45NcTXjaTkYto58x1lZkNRZA0sNSopmJhqJzkGAgfnFMu9HGFlyRFO1cQ7ynRy16VC%2BLW64Wa4NLfmkqg0MYn82VCauia82xGR1gDMBGN2pAiRxXdAFo9tLBln%2BdIX9mFlyZYbPHHD46II%2BKAFUvPZG%2FD97z%2Fv%2FGHeiSjjokWJxBn0Anc529qlMVHnNDaMdBj5vUX8HU41LZgtb2DurZ%2FrIFLmT50fEBTbqY7MEZNpbZLdHabEPvydNPQkklo5heUTZA0qhuTdkQz9H1oPIYjqRKtYG7EmWyP7c%2BowcXswMa2PS3E%2BezSA6jbKuPuKNmn4%2F50mQEwi%2BH2zgY6pgFx3fhZpqvXvBJM9xP8BTo9X%2Bz4xKZWz1vRWeaXd2qXDQxpn%2BvO9DBnMcFHMmhskEfyUF2ArD9lWYcdOj7iZ6uHX4VScT9eCbfUJBNrKZoizLmc22%2BtNVEvs7DVn6q7N3XXFEvtpiMr19NnnFShlYD%2BOmahYqxAz9OKpuBAYYMQar1GgZUlFa30V1mW3JkT2urjfH3Byrb6FW8yT5BUNgflZSqRjcwz&X-Amz-Signature=339a616deda82e63fb81e5d44ec93d679372ac997975da1d1f6eba29388d87ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIFI7JB%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHO1G4EfSvXUh2qOJaEHHfkLHp3sVPIsLU5%2FAivBxpT4AiAMZ1%2BMTXxVrJbEBJBaPKxd5DCFFVxvBoPVK6offOPUxyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYI5nmCuO0orXVOzMKtwDCjDmJekUKxTjPYCKufKmvRetv9kea4GBIXwA8tzPAQeUP32%2B0Ugz9w6Tt%2BQGm1X8spkzz8moZnLAJV0r6wFcYAFEp6MIui2%2BHv8CevZ0RAoGBxGmfYI3xvEaI6WJKh3hU%2FxO1wBeEUZmCWutjJqmKt7tD%2Fi6v2%2BbbkUNaTRA%2BdQjwYbuHKBdpZA7G5XsqYXh714Xs%2FM%2F6BU4hiwJDAKEnax8w6eF0eioPbe84klj5bPcgwWDnA5xleblJwDCUc6lmQOzxxTNxGQ7VGnoPmiBQoKVlQLDFd6QHqi0HTRqpHdSzv4Ua8l45NcTXjaTkYto58x1lZkNRZA0sNSopmJhqJzkGAgfnFMu9HGFlyRFO1cQ7ynRy16VC%2BLW64Wa4NLfmkqg0MYn82VCauia82xGR1gDMBGN2pAiRxXdAFo9tLBln%2BdIX9mFlyZYbPHHD46II%2BKAFUvPZG%2FD97z%2Fv%2FGHeiSjjokWJxBn0Anc529qlMVHnNDaMdBj5vUX8HU41LZgtb2DurZ%2FrIFLmT50fEBTbqY7MEZNpbZLdHabEPvydNPQkklo5heUTZA0qhuTdkQz9H1oPIYjqRKtYG7EmWyP7c%2BowcXswMa2PS3E%2BezSA6jbKuPuKNmn4%2F50mQEwi%2BH2zgY6pgFx3fhZpqvXvBJM9xP8BTo9X%2Bz4xKZWz1vRWeaXd2qXDQxpn%2BvO9DBnMcFHMmhskEfyUF2ArD9lWYcdOj7iZ6uHX4VScT9eCbfUJBNrKZoizLmc22%2BtNVEvs7DVn6q7N3XXFEvtpiMr19NnnFShlYD%2BOmahYqxAz9OKpuBAYYMQar1GgZUlFa30V1mW3JkT2urjfH3Byrb6FW8yT5BUNgflZSqRjcwz&X-Amz-Signature=31d4b6e33ff509759883ffd34b7dcb36020d0949ba9fc81d9d80bcf9de812637&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRIFI7JB%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHO1G4EfSvXUh2qOJaEHHfkLHp3sVPIsLU5%2FAivBxpT4AiAMZ1%2BMTXxVrJbEBJBaPKxd5DCFFVxvBoPVK6offOPUxyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYI5nmCuO0orXVOzMKtwDCjDmJekUKxTjPYCKufKmvRetv9kea4GBIXwA8tzPAQeUP32%2B0Ugz9w6Tt%2BQGm1X8spkzz8moZnLAJV0r6wFcYAFEp6MIui2%2BHv8CevZ0RAoGBxGmfYI3xvEaI6WJKh3hU%2FxO1wBeEUZmCWutjJqmKt7tD%2Fi6v2%2BbbkUNaTRA%2BdQjwYbuHKBdpZA7G5XsqYXh714Xs%2FM%2F6BU4hiwJDAKEnax8w6eF0eioPbe84klj5bPcgwWDnA5xleblJwDCUc6lmQOzxxTNxGQ7VGnoPmiBQoKVlQLDFd6QHqi0HTRqpHdSzv4Ua8l45NcTXjaTkYto58x1lZkNRZA0sNSopmJhqJzkGAgfnFMu9HGFlyRFO1cQ7ynRy16VC%2BLW64Wa4NLfmkqg0MYn82VCauia82xGR1gDMBGN2pAiRxXdAFo9tLBln%2BdIX9mFlyZYbPHHD46II%2BKAFUvPZG%2FD97z%2Fv%2FGHeiSjjokWJxBn0Anc529qlMVHnNDaMdBj5vUX8HU41LZgtb2DurZ%2FrIFLmT50fEBTbqY7MEZNpbZLdHabEPvydNPQkklo5heUTZA0qhuTdkQz9H1oPIYjqRKtYG7EmWyP7c%2BowcXswMa2PS3E%2BezSA6jbKuPuKNmn4%2F50mQEwi%2BH2zgY6pgFx3fhZpqvXvBJM9xP8BTo9X%2Bz4xKZWz1vRWeaXd2qXDQxpn%2BvO9DBnMcFHMmhskEfyUF2ArD9lWYcdOj7iZ6uHX4VScT9eCbfUJBNrKZoizLmc22%2BtNVEvs7DVn6q7N3XXFEvtpiMr19NnnFShlYD%2BOmahYqxAz9OKpuBAYYMQar1GgZUlFa30V1mW3JkT2urjfH3Byrb6FW8yT5BUNgflZSqRjcwz&X-Amz-Signature=5a0bbe609aa400df0dd49910f4676251cf3f7ade1b4a83d4e8b9de074f5bab25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



