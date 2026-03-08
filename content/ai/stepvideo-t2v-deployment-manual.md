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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R7GF4JM%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIF6IkX5L%2BAZTmx%2FS1RxeVTf7yNQXTNLf%2Bj8rcNP%2ByNGRAiBi49YUUGf0MudgfrPpVWsbVmOFCfUT5D3a5VSKYZ%2B49yr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMiRAZ%2FDTx3Gb3lzklKtwD6%2Fe526Ot4o7W2PcK7SnGbCSaoxt0uQpXgc0gYP9oQrqnhXNDPXRNvSpGZpz4H7M3d4Gq1MNghasjD3OnCz6hM%2BLi1zOEu5HE2te4KKXytxmjitbYFesRzNkxtsbT8UOICdxrzN43BNOQ6aEjCV9iEIknHd%2Bz7ls5TsypYEGIub4zRHtvKdKtg6iVGA23n1r2KJIyUnshurJ0zm%2BGUd%2Bev%2BLDec7fuR%2BKkcfbEv85rwfenPx3G01CNwP8v79%2Fa8i2A48hHxrcdVo56WDxAD1CDzmq1afqKRCePlORBfRV%2BjD64dlJ%2BMFRMHpLf3ZktXiAcYsWVXtXXImgwOmn6ht8v0KwB5Kjc054t8cn1wJuoZA1fQv9JmkuJq4sBuMvzfg4anZjJzaCb4K0bd9ecE4loEEYdXEfWyuJEzJ%2FNSaCIt6GKjwsqP6d5No1B%2Fx7dWbMgm3Qvz0mO6%2BCawayCYRDtl8vSW2ZWm1KXb9zQEWdy4vPfx44whWzaAQYM8Jb8%2BGR0%2BPQGHVlFaIhQd5%2BhnEPhcGK6KlPjm2ddgV1bYgwUvrc6Ejd9yOt%2F6yhVoAmsdLFityKwTdgqSAFzmeJ90CnMr0kxrwVLP5Hkb1YKZcoGlbwqQ6tW%2BapzdBUVDwwqcKzzQY6pgHtdRSNM%2Fs%2FAgwliZ4gfpBpk46uLmdO7FX10lyJ5IeMqdzzygcHBQS3fgptaZmotzq4RnxeNE3PLzIg6mAz1YSTqWwz5MZ6k47xrAtztkgMUveHI0RIVHbmSUWkDpw%2BaQTE4XPF9iMqC9jZvrsKGrWlZSci7MyS4LeTWcQLQmmnrlO%2BA%2BBI25Kb6ta9vblUHw%2FkfzKLwQSGRhCuqcYzN6iBy3dRKm5q&X-Amz-Signature=9285bdc4d32249a75ec90461fc5b8da21a2c8140f06f286d49b2487d087fd17d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R7GF4JM%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIF6IkX5L%2BAZTmx%2FS1RxeVTf7yNQXTNLf%2Bj8rcNP%2ByNGRAiBi49YUUGf0MudgfrPpVWsbVmOFCfUT5D3a5VSKYZ%2B49yr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMiRAZ%2FDTx3Gb3lzklKtwD6%2Fe526Ot4o7W2PcK7SnGbCSaoxt0uQpXgc0gYP9oQrqnhXNDPXRNvSpGZpz4H7M3d4Gq1MNghasjD3OnCz6hM%2BLi1zOEu5HE2te4KKXytxmjitbYFesRzNkxtsbT8UOICdxrzN43BNOQ6aEjCV9iEIknHd%2Bz7ls5TsypYEGIub4zRHtvKdKtg6iVGA23n1r2KJIyUnshurJ0zm%2BGUd%2Bev%2BLDec7fuR%2BKkcfbEv85rwfenPx3G01CNwP8v79%2Fa8i2A48hHxrcdVo56WDxAD1CDzmq1afqKRCePlORBfRV%2BjD64dlJ%2BMFRMHpLf3ZktXiAcYsWVXtXXImgwOmn6ht8v0KwB5Kjc054t8cn1wJuoZA1fQv9JmkuJq4sBuMvzfg4anZjJzaCb4K0bd9ecE4loEEYdXEfWyuJEzJ%2FNSaCIt6GKjwsqP6d5No1B%2Fx7dWbMgm3Qvz0mO6%2BCawayCYRDtl8vSW2ZWm1KXb9zQEWdy4vPfx44whWzaAQYM8Jb8%2BGR0%2BPQGHVlFaIhQd5%2BhnEPhcGK6KlPjm2ddgV1bYgwUvrc6Ejd9yOt%2F6yhVoAmsdLFityKwTdgqSAFzmeJ90CnMr0kxrwVLP5Hkb1YKZcoGlbwqQ6tW%2BapzdBUVDwwqcKzzQY6pgHtdRSNM%2Fs%2FAgwliZ4gfpBpk46uLmdO7FX10lyJ5IeMqdzzygcHBQS3fgptaZmotzq4RnxeNE3PLzIg6mAz1YSTqWwz5MZ6k47xrAtztkgMUveHI0RIVHbmSUWkDpw%2BaQTE4XPF9iMqC9jZvrsKGrWlZSci7MyS4LeTWcQLQmmnrlO%2BA%2BBI25Kb6ta9vblUHw%2FkfzKLwQSGRhCuqcYzN6iBy3dRKm5q&X-Amz-Signature=dd5e10cdc73f450eca183f73214f4894ba1458a89729f6a306cd3d3a59955fb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R7GF4JM%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIF6IkX5L%2BAZTmx%2FS1RxeVTf7yNQXTNLf%2Bj8rcNP%2ByNGRAiBi49YUUGf0MudgfrPpVWsbVmOFCfUT5D3a5VSKYZ%2B49yr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMiRAZ%2FDTx3Gb3lzklKtwD6%2Fe526Ot4o7W2PcK7SnGbCSaoxt0uQpXgc0gYP9oQrqnhXNDPXRNvSpGZpz4H7M3d4Gq1MNghasjD3OnCz6hM%2BLi1zOEu5HE2te4KKXytxmjitbYFesRzNkxtsbT8UOICdxrzN43BNOQ6aEjCV9iEIknHd%2Bz7ls5TsypYEGIub4zRHtvKdKtg6iVGA23n1r2KJIyUnshurJ0zm%2BGUd%2Bev%2BLDec7fuR%2BKkcfbEv85rwfenPx3G01CNwP8v79%2Fa8i2A48hHxrcdVo56WDxAD1CDzmq1afqKRCePlORBfRV%2BjD64dlJ%2BMFRMHpLf3ZktXiAcYsWVXtXXImgwOmn6ht8v0KwB5Kjc054t8cn1wJuoZA1fQv9JmkuJq4sBuMvzfg4anZjJzaCb4K0bd9ecE4loEEYdXEfWyuJEzJ%2FNSaCIt6GKjwsqP6d5No1B%2Fx7dWbMgm3Qvz0mO6%2BCawayCYRDtl8vSW2ZWm1KXb9zQEWdy4vPfx44whWzaAQYM8Jb8%2BGR0%2BPQGHVlFaIhQd5%2BhnEPhcGK6KlPjm2ddgV1bYgwUvrc6Ejd9yOt%2F6yhVoAmsdLFityKwTdgqSAFzmeJ90CnMr0kxrwVLP5Hkb1YKZcoGlbwqQ6tW%2BapzdBUVDwwqcKzzQY6pgHtdRSNM%2Fs%2FAgwliZ4gfpBpk46uLmdO7FX10lyJ5IeMqdzzygcHBQS3fgptaZmotzq4RnxeNE3PLzIg6mAz1YSTqWwz5MZ6k47xrAtztkgMUveHI0RIVHbmSUWkDpw%2BaQTE4XPF9iMqC9jZvrsKGrWlZSci7MyS4LeTWcQLQmmnrlO%2BA%2BBI25Kb6ta9vblUHw%2FkfzKLwQSGRhCuqcYzN6iBy3dRKm5q&X-Amz-Signature=ee8db490086f8d639c5d11f56ffa7ff0b5ccef507788a85ed8de7d10fd7dfcb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R7GF4JM%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIF6IkX5L%2BAZTmx%2FS1RxeVTf7yNQXTNLf%2Bj8rcNP%2ByNGRAiBi49YUUGf0MudgfrPpVWsbVmOFCfUT5D3a5VSKYZ%2B49yr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMiRAZ%2FDTx3Gb3lzklKtwD6%2Fe526Ot4o7W2PcK7SnGbCSaoxt0uQpXgc0gYP9oQrqnhXNDPXRNvSpGZpz4H7M3d4Gq1MNghasjD3OnCz6hM%2BLi1zOEu5HE2te4KKXytxmjitbYFesRzNkxtsbT8UOICdxrzN43BNOQ6aEjCV9iEIknHd%2Bz7ls5TsypYEGIub4zRHtvKdKtg6iVGA23n1r2KJIyUnshurJ0zm%2BGUd%2Bev%2BLDec7fuR%2BKkcfbEv85rwfenPx3G01CNwP8v79%2Fa8i2A48hHxrcdVo56WDxAD1CDzmq1afqKRCePlORBfRV%2BjD64dlJ%2BMFRMHpLf3ZktXiAcYsWVXtXXImgwOmn6ht8v0KwB5Kjc054t8cn1wJuoZA1fQv9JmkuJq4sBuMvzfg4anZjJzaCb4K0bd9ecE4loEEYdXEfWyuJEzJ%2FNSaCIt6GKjwsqP6d5No1B%2Fx7dWbMgm3Qvz0mO6%2BCawayCYRDtl8vSW2ZWm1KXb9zQEWdy4vPfx44whWzaAQYM8Jb8%2BGR0%2BPQGHVlFaIhQd5%2BhnEPhcGK6KlPjm2ddgV1bYgwUvrc6Ejd9yOt%2F6yhVoAmsdLFityKwTdgqSAFzmeJ90CnMr0kxrwVLP5Hkb1YKZcoGlbwqQ6tW%2BapzdBUVDwwqcKzzQY6pgHtdRSNM%2Fs%2FAgwliZ4gfpBpk46uLmdO7FX10lyJ5IeMqdzzygcHBQS3fgptaZmotzq4RnxeNE3PLzIg6mAz1YSTqWwz5MZ6k47xrAtztkgMUveHI0RIVHbmSUWkDpw%2BaQTE4XPF9iMqC9jZvrsKGrWlZSci7MyS4LeTWcQLQmmnrlO%2BA%2BBI25Kb6ta9vblUHw%2FkfzKLwQSGRhCuqcYzN6iBy3dRKm5q&X-Amz-Signature=d826337804727437f460968f8c35b3d1b35e6a1c0f982fe17c26da594bbd2c5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



