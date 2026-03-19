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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P2GQR6J%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB1LKlkecSXGTG%2F0FZ1H12I5tY2GYbMO6huLcHus4HbpAiAUtUTDaAxGvMTDIaJGzKsuTT8XuvETnfAK%2FeOqaucuoyr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMGYU9A7pFSlM1JUNYKtwD1akK2HNJRNyzJWAmAdeL05%2BHaWeXwTScj%2BEJgGLg2ZlU6jZbxWzGBE32EScJwccLA8IWbXezQVX0o1PlDbpRM3vqqEu%2FZFzspoZnbDBWAp7%2FJxD5KBVt3hsqAL0JO%2FqjPFot%2FdYAzigM2NAcu5SV3R2Ak9k9D3VLXiwCpiptFhEb0CZhnc5PV2bVqWZYsQx1gFLpaBofKWSsgE%2B4IF%2Fnh1qXTS4zAjejlNZR6%2BZv6bTVr26Lw2r%2Bc88bzVM0bVgILFxnWoUrM63WdRq2J2CXzWdD%2B%2BHlgeZMDOucuSvxSbthuTl1bysPybuoQulA1J5YjpHY%2F5b1oBs9bNBX3ovH%2BAXuWRuGSh4%2BnIlp825MNN3A2EEF00Rs6E02soeK5aqkmWdev4mbTOLOFurOOJzx6sSYdwaR3WsFgG4ZbSFSBiL8YDJK6VOxupTj0Fu7hRnWBebPGpGEjNVsU0%2BGdmEyfoLu8YIaUq1pRvjM2kVZrYQTbR0QfepK05doBP4KQBaycXcbehDN%2FZB30QH6OCmNijhWzzdG%2BbQX%2BgYFD7h8KRmcNN88MDRs4lxH8LTBBRCbJY4USbwe1G37EkDBOXSvI4BEfwqhGtCIsdpyj%2FbjCSRPbkOeRE848aAdTEAwv8btzQY6pgGgbt7xvBwqDa%2Ft1Sa7VcRmxqIaoEwDJxQqhObnwFtap26v%2FsuP4rxtWY6A9zyO3G5V1R2W3LIkf6Nds%2Bj4Zu7I16ECWhCObSEsZCEGi2iBQARpWY2e9G1oG8ueMgVHXjIaj%2BSuF7%2B2gQ%2Fma%2FPqA%2BSBVnA4OVgVCJnV1EZj584OxiFnT%2Fv78OvV43r8IV9Jd7a0jTZuZIy5kbQZcy7pxVjy81wMu7iP&X-Amz-Signature=48221999f9cd3bacc8eb5b3941c5538198cb424ed5593e27a325d522cdb01a38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P2GQR6J%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB1LKlkecSXGTG%2F0FZ1H12I5tY2GYbMO6huLcHus4HbpAiAUtUTDaAxGvMTDIaJGzKsuTT8XuvETnfAK%2FeOqaucuoyr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMGYU9A7pFSlM1JUNYKtwD1akK2HNJRNyzJWAmAdeL05%2BHaWeXwTScj%2BEJgGLg2ZlU6jZbxWzGBE32EScJwccLA8IWbXezQVX0o1PlDbpRM3vqqEu%2FZFzspoZnbDBWAp7%2FJxD5KBVt3hsqAL0JO%2FqjPFot%2FdYAzigM2NAcu5SV3R2Ak9k9D3VLXiwCpiptFhEb0CZhnc5PV2bVqWZYsQx1gFLpaBofKWSsgE%2B4IF%2Fnh1qXTS4zAjejlNZR6%2BZv6bTVr26Lw2r%2Bc88bzVM0bVgILFxnWoUrM63WdRq2J2CXzWdD%2B%2BHlgeZMDOucuSvxSbthuTl1bysPybuoQulA1J5YjpHY%2F5b1oBs9bNBX3ovH%2BAXuWRuGSh4%2BnIlp825MNN3A2EEF00Rs6E02soeK5aqkmWdev4mbTOLOFurOOJzx6sSYdwaR3WsFgG4ZbSFSBiL8YDJK6VOxupTj0Fu7hRnWBebPGpGEjNVsU0%2BGdmEyfoLu8YIaUq1pRvjM2kVZrYQTbR0QfepK05doBP4KQBaycXcbehDN%2FZB30QH6OCmNijhWzzdG%2BbQX%2BgYFD7h8KRmcNN88MDRs4lxH8LTBBRCbJY4USbwe1G37EkDBOXSvI4BEfwqhGtCIsdpyj%2FbjCSRPbkOeRE848aAdTEAwv8btzQY6pgGgbt7xvBwqDa%2Ft1Sa7VcRmxqIaoEwDJxQqhObnwFtap26v%2FsuP4rxtWY6A9zyO3G5V1R2W3LIkf6Nds%2Bj4Zu7I16ECWhCObSEsZCEGi2iBQARpWY2e9G1oG8ueMgVHXjIaj%2BSuF7%2B2gQ%2Fma%2FPqA%2BSBVnA4OVgVCJnV1EZj584OxiFnT%2Fv78OvV43r8IV9Jd7a0jTZuZIy5kbQZcy7pxVjy81wMu7iP&X-Amz-Signature=971d3580eed9e1186b64e60e9603cd3d4209ece19b1cfadd19b8968ba2c77bcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P2GQR6J%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB1LKlkecSXGTG%2F0FZ1H12I5tY2GYbMO6huLcHus4HbpAiAUtUTDaAxGvMTDIaJGzKsuTT8XuvETnfAK%2FeOqaucuoyr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMGYU9A7pFSlM1JUNYKtwD1akK2HNJRNyzJWAmAdeL05%2BHaWeXwTScj%2BEJgGLg2ZlU6jZbxWzGBE32EScJwccLA8IWbXezQVX0o1PlDbpRM3vqqEu%2FZFzspoZnbDBWAp7%2FJxD5KBVt3hsqAL0JO%2FqjPFot%2FdYAzigM2NAcu5SV3R2Ak9k9D3VLXiwCpiptFhEb0CZhnc5PV2bVqWZYsQx1gFLpaBofKWSsgE%2B4IF%2Fnh1qXTS4zAjejlNZR6%2BZv6bTVr26Lw2r%2Bc88bzVM0bVgILFxnWoUrM63WdRq2J2CXzWdD%2B%2BHlgeZMDOucuSvxSbthuTl1bysPybuoQulA1J5YjpHY%2F5b1oBs9bNBX3ovH%2BAXuWRuGSh4%2BnIlp825MNN3A2EEF00Rs6E02soeK5aqkmWdev4mbTOLOFurOOJzx6sSYdwaR3WsFgG4ZbSFSBiL8YDJK6VOxupTj0Fu7hRnWBebPGpGEjNVsU0%2BGdmEyfoLu8YIaUq1pRvjM2kVZrYQTbR0QfepK05doBP4KQBaycXcbehDN%2FZB30QH6OCmNijhWzzdG%2BbQX%2BgYFD7h8KRmcNN88MDRs4lxH8LTBBRCbJY4USbwe1G37EkDBOXSvI4BEfwqhGtCIsdpyj%2FbjCSRPbkOeRE848aAdTEAwv8btzQY6pgGgbt7xvBwqDa%2Ft1Sa7VcRmxqIaoEwDJxQqhObnwFtap26v%2FsuP4rxtWY6A9zyO3G5V1R2W3LIkf6Nds%2Bj4Zu7I16ECWhCObSEsZCEGi2iBQARpWY2e9G1oG8ueMgVHXjIaj%2BSuF7%2B2gQ%2Fma%2FPqA%2BSBVnA4OVgVCJnV1EZj584OxiFnT%2Fv78OvV43r8IV9Jd7a0jTZuZIy5kbQZcy7pxVjy81wMu7iP&X-Amz-Signature=d7ab43a474b6bec0bdfceb4d706877692c648709188656c63e8e7af44b241fe0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P2GQR6J%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIB1LKlkecSXGTG%2F0FZ1H12I5tY2GYbMO6huLcHus4HbpAiAUtUTDaAxGvMTDIaJGzKsuTT8XuvETnfAK%2FeOqaucuoyr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMGYU9A7pFSlM1JUNYKtwD1akK2HNJRNyzJWAmAdeL05%2BHaWeXwTScj%2BEJgGLg2ZlU6jZbxWzGBE32EScJwccLA8IWbXezQVX0o1PlDbpRM3vqqEu%2FZFzspoZnbDBWAp7%2FJxD5KBVt3hsqAL0JO%2FqjPFot%2FdYAzigM2NAcu5SV3R2Ak9k9D3VLXiwCpiptFhEb0CZhnc5PV2bVqWZYsQx1gFLpaBofKWSsgE%2B4IF%2Fnh1qXTS4zAjejlNZR6%2BZv6bTVr26Lw2r%2Bc88bzVM0bVgILFxnWoUrM63WdRq2J2CXzWdD%2B%2BHlgeZMDOucuSvxSbthuTl1bysPybuoQulA1J5YjpHY%2F5b1oBs9bNBX3ovH%2BAXuWRuGSh4%2BnIlp825MNN3A2EEF00Rs6E02soeK5aqkmWdev4mbTOLOFurOOJzx6sSYdwaR3WsFgG4ZbSFSBiL8YDJK6VOxupTj0Fu7hRnWBebPGpGEjNVsU0%2BGdmEyfoLu8YIaUq1pRvjM2kVZrYQTbR0QfepK05doBP4KQBaycXcbehDN%2FZB30QH6OCmNijhWzzdG%2BbQX%2BgYFD7h8KRmcNN88MDRs4lxH8LTBBRCbJY4USbwe1G37EkDBOXSvI4BEfwqhGtCIsdpyj%2FbjCSRPbkOeRE848aAdTEAwv8btzQY6pgGgbt7xvBwqDa%2Ft1Sa7VcRmxqIaoEwDJxQqhObnwFtap26v%2FsuP4rxtWY6A9zyO3G5V1R2W3LIkf6Nds%2Bj4Zu7I16ECWhCObSEsZCEGi2iBQARpWY2e9G1oG8ueMgVHXjIaj%2BSuF7%2B2gQ%2Fma%2FPqA%2BSBVnA4OVgVCJnV1EZj584OxiFnT%2Fv78OvV43r8IV9Jd7a0jTZuZIy5kbQZcy7pxVjy81wMu7iP&X-Amz-Signature=6c4bb8c12f884ec1efb2f770df5d041ad2c70281a1914bba7da48977c8d4a4bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



