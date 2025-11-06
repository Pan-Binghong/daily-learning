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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3FC3XT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrX4ecVCDmllwTnsAvhdrryLxbGaxdhxyYeQselrLOPAiEAuRaws2LCk6blzzVJLOu2mzevYkCRS6OJweitzVFAo0YqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiLEsGhiemmkGtujyrcA%2F1sUr43XeGQonPDEM7rjybEKUN%2BAMJw%2F6Et57z5pxsJ%2B3q6IWHV4AIdlgFCmg27OYwkrGDVSyCtMXCpvV2OKqYLla8l%2FwBte6t8BeYaEzM%2FO913hEh1X5WlcFOmbrpx7QkuDeKIgWhRC0ICcaIoIgCDPU6RNJ7X7ecs8LT8W6P2j24EHRGGRA32EwkhmDGzZWzLGVrKnXM4SGCH4zSPARg24q0pAGYdG4MlBOgpxrUW9zyRDnECX33JaPxre0At%2Fm3o17od1rJ7Ome8wZsHRrqbs4hRe%2Fcd%2Bz77ypFTInR%2F6iGYTieiNVC86e8SUOH%2Fy4UzkVv9DMM4n%2B4%2FM%2BWDoqQEEo8eGwuBmeYxqthsb27LdiHUQ%2BYsXFP8wb2rcX4RXOuY9fBlXbE21ly8GOCTtTAmgXBF3m7MGI56Ezh3Lc05qITDjLglifAeM86XsRVJJuigGLpn3ggqOuU4nQ22zf4NvrVzONPpWujH%2Bk9%2FdkV%2B8zoVynIzegmjjYZdFaeJuluCcdxDB2VnsgKFwkAPUlJ%2Fvz8%2BnaWVTn%2Bor7F3p33SsLyORH85o%2FJF3Q%2BdccVBdrqOfUVa%2F2TtBQUIZd8bg0uzsd3DU6fCUJQXpv5ihYT7yB%2Bsn%2BVO%2BCkKgS4vMITxr8gGOqUBhIQWIQxsqV2K2IK1789lyUFhlItJY1uNfjLwa3%2F3ZxUPNycIeYIAkpi1F5PL3Lb%2BRjfBh0oABQBXLcYkTpCOspiIkjDRx9wOBMIH%2BuVPkOZMEKz%2FUQ6OhUylfh33d4qq7wZgnSDDiFfCmZLjcm7%2FgduCftVVdtcUidSLspN2VFJL3f4iGMFskHZUPS65cV7NOY%2Fbs%2BRpnGaYp6OwY3qdQ5cr8EAl&X-Amz-Signature=58af9679b83371072056a70912d6efc8e7a56881d4cbcc0f9726d0c46e698e64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3FC3XT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrX4ecVCDmllwTnsAvhdrryLxbGaxdhxyYeQselrLOPAiEAuRaws2LCk6blzzVJLOu2mzevYkCRS6OJweitzVFAo0YqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiLEsGhiemmkGtujyrcA%2F1sUr43XeGQonPDEM7rjybEKUN%2BAMJw%2F6Et57z5pxsJ%2B3q6IWHV4AIdlgFCmg27OYwkrGDVSyCtMXCpvV2OKqYLla8l%2FwBte6t8BeYaEzM%2FO913hEh1X5WlcFOmbrpx7QkuDeKIgWhRC0ICcaIoIgCDPU6RNJ7X7ecs8LT8W6P2j24EHRGGRA32EwkhmDGzZWzLGVrKnXM4SGCH4zSPARg24q0pAGYdG4MlBOgpxrUW9zyRDnECX33JaPxre0At%2Fm3o17od1rJ7Ome8wZsHRrqbs4hRe%2Fcd%2Bz77ypFTInR%2F6iGYTieiNVC86e8SUOH%2Fy4UzkVv9DMM4n%2B4%2FM%2BWDoqQEEo8eGwuBmeYxqthsb27LdiHUQ%2BYsXFP8wb2rcX4RXOuY9fBlXbE21ly8GOCTtTAmgXBF3m7MGI56Ezh3Lc05qITDjLglifAeM86XsRVJJuigGLpn3ggqOuU4nQ22zf4NvrVzONPpWujH%2Bk9%2FdkV%2B8zoVynIzegmjjYZdFaeJuluCcdxDB2VnsgKFwkAPUlJ%2Fvz8%2BnaWVTn%2Bor7F3p33SsLyORH85o%2FJF3Q%2BdccVBdrqOfUVa%2F2TtBQUIZd8bg0uzsd3DU6fCUJQXpv5ihYT7yB%2Bsn%2BVO%2BCkKgS4vMITxr8gGOqUBhIQWIQxsqV2K2IK1789lyUFhlItJY1uNfjLwa3%2F3ZxUPNycIeYIAkpi1F5PL3Lb%2BRjfBh0oABQBXLcYkTpCOspiIkjDRx9wOBMIH%2BuVPkOZMEKz%2FUQ6OhUylfh33d4qq7wZgnSDDiFfCmZLjcm7%2FgduCftVVdtcUidSLspN2VFJL3f4iGMFskHZUPS65cV7NOY%2Fbs%2BRpnGaYp6OwY3qdQ5cr8EAl&X-Amz-Signature=e5ee7e00ca11b7d92451da53035660d3958d74f7fa13e68504202f950eab9b47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3FC3XT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrX4ecVCDmllwTnsAvhdrryLxbGaxdhxyYeQselrLOPAiEAuRaws2LCk6blzzVJLOu2mzevYkCRS6OJweitzVFAo0YqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiLEsGhiemmkGtujyrcA%2F1sUr43XeGQonPDEM7rjybEKUN%2BAMJw%2F6Et57z5pxsJ%2B3q6IWHV4AIdlgFCmg27OYwkrGDVSyCtMXCpvV2OKqYLla8l%2FwBte6t8BeYaEzM%2FO913hEh1X5WlcFOmbrpx7QkuDeKIgWhRC0ICcaIoIgCDPU6RNJ7X7ecs8LT8W6P2j24EHRGGRA32EwkhmDGzZWzLGVrKnXM4SGCH4zSPARg24q0pAGYdG4MlBOgpxrUW9zyRDnECX33JaPxre0At%2Fm3o17od1rJ7Ome8wZsHRrqbs4hRe%2Fcd%2Bz77ypFTInR%2F6iGYTieiNVC86e8SUOH%2Fy4UzkVv9DMM4n%2B4%2FM%2BWDoqQEEo8eGwuBmeYxqthsb27LdiHUQ%2BYsXFP8wb2rcX4RXOuY9fBlXbE21ly8GOCTtTAmgXBF3m7MGI56Ezh3Lc05qITDjLglifAeM86XsRVJJuigGLpn3ggqOuU4nQ22zf4NvrVzONPpWujH%2Bk9%2FdkV%2B8zoVynIzegmjjYZdFaeJuluCcdxDB2VnsgKFwkAPUlJ%2Fvz8%2BnaWVTn%2Bor7F3p33SsLyORH85o%2FJF3Q%2BdccVBdrqOfUVa%2F2TtBQUIZd8bg0uzsd3DU6fCUJQXpv5ihYT7yB%2Bsn%2BVO%2BCkKgS4vMITxr8gGOqUBhIQWIQxsqV2K2IK1789lyUFhlItJY1uNfjLwa3%2F3ZxUPNycIeYIAkpi1F5PL3Lb%2BRjfBh0oABQBXLcYkTpCOspiIkjDRx9wOBMIH%2BuVPkOZMEKz%2FUQ6OhUylfh33d4qq7wZgnSDDiFfCmZLjcm7%2FgduCftVVdtcUidSLspN2VFJL3f4iGMFskHZUPS65cV7NOY%2Fbs%2BRpnGaYp6OwY3qdQ5cr8EAl&X-Amz-Signature=82314d94ec215fe4d12993c375dd8048f26ed1e5879050bb36dcab11276a5d91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3FC3XT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrX4ecVCDmllwTnsAvhdrryLxbGaxdhxyYeQselrLOPAiEAuRaws2LCk6blzzVJLOu2mzevYkCRS6OJweitzVFAo0YqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKiLEsGhiemmkGtujyrcA%2F1sUr43XeGQonPDEM7rjybEKUN%2BAMJw%2F6Et57z5pxsJ%2B3q6IWHV4AIdlgFCmg27OYwkrGDVSyCtMXCpvV2OKqYLla8l%2FwBte6t8BeYaEzM%2FO913hEh1X5WlcFOmbrpx7QkuDeKIgWhRC0ICcaIoIgCDPU6RNJ7X7ecs8LT8W6P2j24EHRGGRA32EwkhmDGzZWzLGVrKnXM4SGCH4zSPARg24q0pAGYdG4MlBOgpxrUW9zyRDnECX33JaPxre0At%2Fm3o17od1rJ7Ome8wZsHRrqbs4hRe%2Fcd%2Bz77ypFTInR%2F6iGYTieiNVC86e8SUOH%2Fy4UzkVv9DMM4n%2B4%2FM%2BWDoqQEEo8eGwuBmeYxqthsb27LdiHUQ%2BYsXFP8wb2rcX4RXOuY9fBlXbE21ly8GOCTtTAmgXBF3m7MGI56Ezh3Lc05qITDjLglifAeM86XsRVJJuigGLpn3ggqOuU4nQ22zf4NvrVzONPpWujH%2Bk9%2FdkV%2B8zoVynIzegmjjYZdFaeJuluCcdxDB2VnsgKFwkAPUlJ%2Fvz8%2BnaWVTn%2Bor7F3p33SsLyORH85o%2FJF3Q%2BdccVBdrqOfUVa%2F2TtBQUIZd8bg0uzsd3DU6fCUJQXpv5ihYT7yB%2Bsn%2BVO%2BCkKgS4vMITxr8gGOqUBhIQWIQxsqV2K2IK1789lyUFhlItJY1uNfjLwa3%2F3ZxUPNycIeYIAkpi1F5PL3Lb%2BRjfBh0oABQBXLcYkTpCOspiIkjDRx9wOBMIH%2BuVPkOZMEKz%2FUQ6OhUylfh33d4qq7wZgnSDDiFfCmZLjcm7%2FgduCftVVdtcUidSLspN2VFJL3f4iGMFskHZUPS65cV7NOY%2Fbs%2BRpnGaYp6OwY3qdQ5cr8EAl&X-Amz-Signature=c532df3455ef5e6a65de4602aa6ccd0030c2b004c02221ae708db22d1efb6a9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



