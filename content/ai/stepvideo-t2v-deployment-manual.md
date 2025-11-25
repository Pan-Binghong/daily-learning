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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O57CZ3X%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPbaIw3tMyzuZhhYrIaUf2KNyMT20SxKSpgaTsYpXRoAiAtF88zc4LIcu%2BX7Ns4oYTdLbZt7m13jQdaJUGT%2BwunrSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMNxWCysr3SucIosbKKtwDh1SzC2X8T0s4ZH19okNLil%2BwpC5eXtGwCQV%2F3xrql9SfERUPTQqFFIt6n6V7P1vaWNGYXcCOpkKYHhOfdmala3llbDJ1ZvkC%2BO69a%2BzFcgVhim%2BkrCZUAojYmexyDq%2Bb5nxoQaaLHs8wF5hxavoJCZ5WF79M4ifA1IyxV76i0nfykQC5L817upzDfeNwV91dK4Bou1wzbIxZTVr3qIaQKta3z1N2I8KmyWOA3%2FQOxCArZeAVwKoiuLuzG2rWOVINYi882hglZnpIIp6BK1z%2BlCxk8QRXVDzRmvzpg43XSiR28cmFwqnlzNhcfc%2Fqtux1IQZA5d%2Fnngu2TzTTyrjO02U%2FET9SaxnzlnSdxb8oocU6ynJkFSto%2F2y%2BNRYfn2EE2ZtoXiThAXnxUHQY68Sbux2SM8SAvCNa2igyl0TE2zFsZnWQblqFRVCPiJjBhxNsAeb%2FM7CBb93E8ap9Z4pGjxrppDUpJQL1yphLg7%2FbGcVDQ48u11s7Ce7Wf68if2Csguc80w01Mkew9uuasTct82nfI7yP1FkhkXGt3NaM%2B2PggDapyghVRpC1DXrcgRZN%2B2c0IiCZ4%2FvZ1wyMBs4cRNm6Q3VoezN3N0HqmVNwDNR8KDVFy3sj8pkwclIwi6yUyQY6pgHsziI8sSpjRYkF9%2B%2BLMPdbc01KiI5OII2TzhMKDt7mFvBm6bN0Y17oUyOb%2BYytPSGQU8FjuTVG2wYMyW1UdMTBz%2BuFkhw8jA2KOFgDV8H5gfL9G4rWvrYf2Q%2FOP6qdUaOq3gBo6hx9d529yWkZV%2ByrbtbPLriDy2AlpXHoESjNyL7nLlPA%2BoMLRijgO8%2FiHxv4SSePA1hNL3HMotzn9jt8dd%2Fmzq3O&X-Amz-Signature=6b7034e2f92324d6cab2020d3f091a838a3fdf9c0a4ddd86a091b980b934fede&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O57CZ3X%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPbaIw3tMyzuZhhYrIaUf2KNyMT20SxKSpgaTsYpXRoAiAtF88zc4LIcu%2BX7Ns4oYTdLbZt7m13jQdaJUGT%2BwunrSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMNxWCysr3SucIosbKKtwDh1SzC2X8T0s4ZH19okNLil%2BwpC5eXtGwCQV%2F3xrql9SfERUPTQqFFIt6n6V7P1vaWNGYXcCOpkKYHhOfdmala3llbDJ1ZvkC%2BO69a%2BzFcgVhim%2BkrCZUAojYmexyDq%2Bb5nxoQaaLHs8wF5hxavoJCZ5WF79M4ifA1IyxV76i0nfykQC5L817upzDfeNwV91dK4Bou1wzbIxZTVr3qIaQKta3z1N2I8KmyWOA3%2FQOxCArZeAVwKoiuLuzG2rWOVINYi882hglZnpIIp6BK1z%2BlCxk8QRXVDzRmvzpg43XSiR28cmFwqnlzNhcfc%2Fqtux1IQZA5d%2Fnngu2TzTTyrjO02U%2FET9SaxnzlnSdxb8oocU6ynJkFSto%2F2y%2BNRYfn2EE2ZtoXiThAXnxUHQY68Sbux2SM8SAvCNa2igyl0TE2zFsZnWQblqFRVCPiJjBhxNsAeb%2FM7CBb93E8ap9Z4pGjxrppDUpJQL1yphLg7%2FbGcVDQ48u11s7Ce7Wf68if2Csguc80w01Mkew9uuasTct82nfI7yP1FkhkXGt3NaM%2B2PggDapyghVRpC1DXrcgRZN%2B2c0IiCZ4%2FvZ1wyMBs4cRNm6Q3VoezN3N0HqmVNwDNR8KDVFy3sj8pkwclIwi6yUyQY6pgHsziI8sSpjRYkF9%2B%2BLMPdbc01KiI5OII2TzhMKDt7mFvBm6bN0Y17oUyOb%2BYytPSGQU8FjuTVG2wYMyW1UdMTBz%2BuFkhw8jA2KOFgDV8H5gfL9G4rWvrYf2Q%2FOP6qdUaOq3gBo6hx9d529yWkZV%2ByrbtbPLriDy2AlpXHoESjNyL7nLlPA%2BoMLRijgO8%2FiHxv4SSePA1hNL3HMotzn9jt8dd%2Fmzq3O&X-Amz-Signature=8a20dafe16a1d0229b8580ccab857146a50f68136cc6b5eb5dc449e2aeacc7a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O57CZ3X%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPbaIw3tMyzuZhhYrIaUf2KNyMT20SxKSpgaTsYpXRoAiAtF88zc4LIcu%2BX7Ns4oYTdLbZt7m13jQdaJUGT%2BwunrSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMNxWCysr3SucIosbKKtwDh1SzC2X8T0s4ZH19okNLil%2BwpC5eXtGwCQV%2F3xrql9SfERUPTQqFFIt6n6V7P1vaWNGYXcCOpkKYHhOfdmala3llbDJ1ZvkC%2BO69a%2BzFcgVhim%2BkrCZUAojYmexyDq%2Bb5nxoQaaLHs8wF5hxavoJCZ5WF79M4ifA1IyxV76i0nfykQC5L817upzDfeNwV91dK4Bou1wzbIxZTVr3qIaQKta3z1N2I8KmyWOA3%2FQOxCArZeAVwKoiuLuzG2rWOVINYi882hglZnpIIp6BK1z%2BlCxk8QRXVDzRmvzpg43XSiR28cmFwqnlzNhcfc%2Fqtux1IQZA5d%2Fnngu2TzTTyrjO02U%2FET9SaxnzlnSdxb8oocU6ynJkFSto%2F2y%2BNRYfn2EE2ZtoXiThAXnxUHQY68Sbux2SM8SAvCNa2igyl0TE2zFsZnWQblqFRVCPiJjBhxNsAeb%2FM7CBb93E8ap9Z4pGjxrppDUpJQL1yphLg7%2FbGcVDQ48u11s7Ce7Wf68if2Csguc80w01Mkew9uuasTct82nfI7yP1FkhkXGt3NaM%2B2PggDapyghVRpC1DXrcgRZN%2B2c0IiCZ4%2FvZ1wyMBs4cRNm6Q3VoezN3N0HqmVNwDNR8KDVFy3sj8pkwclIwi6yUyQY6pgHsziI8sSpjRYkF9%2B%2BLMPdbc01KiI5OII2TzhMKDt7mFvBm6bN0Y17oUyOb%2BYytPSGQU8FjuTVG2wYMyW1UdMTBz%2BuFkhw8jA2KOFgDV8H5gfL9G4rWvrYf2Q%2FOP6qdUaOq3gBo6hx9d529yWkZV%2ByrbtbPLriDy2AlpXHoESjNyL7nLlPA%2BoMLRijgO8%2FiHxv4SSePA1hNL3HMotzn9jt8dd%2Fmzq3O&X-Amz-Signature=afc22ebe9d93b819b557f91fcb110dc75c379b234bd7e7652e5f4d013d79bd9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O57CZ3X%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPbaIw3tMyzuZhhYrIaUf2KNyMT20SxKSpgaTsYpXRoAiAtF88zc4LIcu%2BX7Ns4oYTdLbZt7m13jQdaJUGT%2BwunrSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMNxWCysr3SucIosbKKtwDh1SzC2X8T0s4ZH19okNLil%2BwpC5eXtGwCQV%2F3xrql9SfERUPTQqFFIt6n6V7P1vaWNGYXcCOpkKYHhOfdmala3llbDJ1ZvkC%2BO69a%2BzFcgVhim%2BkrCZUAojYmexyDq%2Bb5nxoQaaLHs8wF5hxavoJCZ5WF79M4ifA1IyxV76i0nfykQC5L817upzDfeNwV91dK4Bou1wzbIxZTVr3qIaQKta3z1N2I8KmyWOA3%2FQOxCArZeAVwKoiuLuzG2rWOVINYi882hglZnpIIp6BK1z%2BlCxk8QRXVDzRmvzpg43XSiR28cmFwqnlzNhcfc%2Fqtux1IQZA5d%2Fnngu2TzTTyrjO02U%2FET9SaxnzlnSdxb8oocU6ynJkFSto%2F2y%2BNRYfn2EE2ZtoXiThAXnxUHQY68Sbux2SM8SAvCNa2igyl0TE2zFsZnWQblqFRVCPiJjBhxNsAeb%2FM7CBb93E8ap9Z4pGjxrppDUpJQL1yphLg7%2FbGcVDQ48u11s7Ce7Wf68if2Csguc80w01Mkew9uuasTct82nfI7yP1FkhkXGt3NaM%2B2PggDapyghVRpC1DXrcgRZN%2B2c0IiCZ4%2FvZ1wyMBs4cRNm6Q3VoezN3N0HqmVNwDNR8KDVFy3sj8pkwclIwi6yUyQY6pgHsziI8sSpjRYkF9%2B%2BLMPdbc01KiI5OII2TzhMKDt7mFvBm6bN0Y17oUyOb%2BYytPSGQU8FjuTVG2wYMyW1UdMTBz%2BuFkhw8jA2KOFgDV8H5gfL9G4rWvrYf2Q%2FOP6qdUaOq3gBo6hx9d529yWkZV%2ByrbtbPLriDy2AlpXHoESjNyL7nLlPA%2BoMLRijgO8%2FiHxv4SSePA1hNL3HMotzn9jt8dd%2Fmzq3O&X-Amz-Signature=690cbb515f8749385b7723d87d320c8ef31e71bef5be90ab65a726a27c946bb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



