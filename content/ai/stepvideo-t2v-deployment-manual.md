---
title: Stepvideo-t2v Deployment Manual
date: '2025-04-22T00:43:00.000Z'
lastmod: '2025-04-23T02:58:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 记录部署阶跃星辰发布的stepvideo-ti2v (图片生成视频)模型，全流程。含踩坑记录，以及webui展示代码。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW6FAGR6%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjndzvqtxlqvu35SL8hAhz2RtMc3FcTf3KOFNFG2sFZAiEA1LN6AXWm9vGYZlDYkeNU6dZi%2FJCCB0rSMAY0LhOfvRsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvGjAPVdD8juN7KrSrcA9NxaX5EqUVBRQTzl%2FTZ58iJ7gd8A6yMo0f0V%2Fj0I8SK8zVXNW7asGnDY5pOW97L5ZVmaBvh2vdcJelBIX0x7I8BiLkx5Bmf6IT26XX0My2H5QBgcl9luFtql72Xd2e%2FwvXRHDs%2FYxLHIWRaz3nuAhzBgp1TBSA7OVw1mTuWKiNsxmd9IUO1HqUd3VHw7jfHpnTS1GIihnwOLDd2LTHXMk9vdIpraIc97LejL8r7nfyJPqLSiQLxbHGLkc%2FdyNGiPti%2FZKrVu5Qew%2BgR9Zids0vSg4vlkB787zJbJOisjTlBp907V0wBTBq1Sb4FeqT1S60cxKS7m65GCTHmMHh%2BWJXCL6h3UOE6tEYzVGRkkK%2FtH5u6B1KzHWfr%2BGsc8OIWhAFaHT1CLuHQ6YiKirb8xzyS%2BmPYVgEdpG7vM5%2FOL%2Fm6%2FWVEhlIfCm19KcwhZpOSTk3RaEko59ew7PzLtMyIz7Rr9WVgN%2F%2FwsK7aAXDxYJFC4lRUtnxpMaBl4WhKdwNIOfq94br1YSM3mUaE5JJZ0eKaOYrN2aNMwi1xq%2FuesDr4sNedJkUfG1pfA4G0yz6VWbKOtvK%2BOSfjw6eqCyKQXdPFl%2F96H4N%2BiDrjIn5%2FiTd2Kzm2BedhzhhyD%2FI0MOCirMgGOqUBQDTS7uASDcS1LjkKUeBmpJ1GkR7SO6wodUwes03K2Kjtoar%2BppiorvPcHrUYusKHm8aShrFSwUIP4Ps%2FkYQET5PmobR3ccuaNU%2B4nQZymY79%2B8eKNQFkOO2wNAQt7Tm6Lh8kERXPTKAx4JGqNfDf%2Ft5hdRMfC2BGNn5drkQFzxiE0cXoPEOVWGC8l8mSkK8c9%2FfKb3mlVJafNmsyEejGPbtvz6PK&X-Amz-Signature=5f2c35cbbf2c41e563297c75e6c5c5f1cc51c317a052bf7081de2d6d8e0ab7e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW6FAGR6%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjndzvqtxlqvu35SL8hAhz2RtMc3FcTf3KOFNFG2sFZAiEA1LN6AXWm9vGYZlDYkeNU6dZi%2FJCCB0rSMAY0LhOfvRsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvGjAPVdD8juN7KrSrcA9NxaX5EqUVBRQTzl%2FTZ58iJ7gd8A6yMo0f0V%2Fj0I8SK8zVXNW7asGnDY5pOW97L5ZVmaBvh2vdcJelBIX0x7I8BiLkx5Bmf6IT26XX0My2H5QBgcl9luFtql72Xd2e%2FwvXRHDs%2FYxLHIWRaz3nuAhzBgp1TBSA7OVw1mTuWKiNsxmd9IUO1HqUd3VHw7jfHpnTS1GIihnwOLDd2LTHXMk9vdIpraIc97LejL8r7nfyJPqLSiQLxbHGLkc%2FdyNGiPti%2FZKrVu5Qew%2BgR9Zids0vSg4vlkB787zJbJOisjTlBp907V0wBTBq1Sb4FeqT1S60cxKS7m65GCTHmMHh%2BWJXCL6h3UOE6tEYzVGRkkK%2FtH5u6B1KzHWfr%2BGsc8OIWhAFaHT1CLuHQ6YiKirb8xzyS%2BmPYVgEdpG7vM5%2FOL%2Fm6%2FWVEhlIfCm19KcwhZpOSTk3RaEko59ew7PzLtMyIz7Rr9WVgN%2F%2FwsK7aAXDxYJFC4lRUtnxpMaBl4WhKdwNIOfq94br1YSM3mUaE5JJZ0eKaOYrN2aNMwi1xq%2FuesDr4sNedJkUfG1pfA4G0yz6VWbKOtvK%2BOSfjw6eqCyKQXdPFl%2F96H4N%2BiDrjIn5%2FiTd2Kzm2BedhzhhyD%2FI0MOCirMgGOqUBQDTS7uASDcS1LjkKUeBmpJ1GkR7SO6wodUwes03K2Kjtoar%2BppiorvPcHrUYusKHm8aShrFSwUIP4Ps%2FkYQET5PmobR3ccuaNU%2B4nQZymY79%2B8eKNQFkOO2wNAQt7Tm6Lh8kERXPTKAx4JGqNfDf%2Ft5hdRMfC2BGNn5drkQFzxiE0cXoPEOVWGC8l8mSkK8c9%2FfKb3mlVJafNmsyEejGPbtvz6PK&X-Amz-Signature=f33ffe3c2c18fddc45f44ef2a95d44b7845fa151d5e4b88e67ac3ece1ae6ada7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW6FAGR6%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjndzvqtxlqvu35SL8hAhz2RtMc3FcTf3KOFNFG2sFZAiEA1LN6AXWm9vGYZlDYkeNU6dZi%2FJCCB0rSMAY0LhOfvRsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvGjAPVdD8juN7KrSrcA9NxaX5EqUVBRQTzl%2FTZ58iJ7gd8A6yMo0f0V%2Fj0I8SK8zVXNW7asGnDY5pOW97L5ZVmaBvh2vdcJelBIX0x7I8BiLkx5Bmf6IT26XX0My2H5QBgcl9luFtql72Xd2e%2FwvXRHDs%2FYxLHIWRaz3nuAhzBgp1TBSA7OVw1mTuWKiNsxmd9IUO1HqUd3VHw7jfHpnTS1GIihnwOLDd2LTHXMk9vdIpraIc97LejL8r7nfyJPqLSiQLxbHGLkc%2FdyNGiPti%2FZKrVu5Qew%2BgR9Zids0vSg4vlkB787zJbJOisjTlBp907V0wBTBq1Sb4FeqT1S60cxKS7m65GCTHmMHh%2BWJXCL6h3UOE6tEYzVGRkkK%2FtH5u6B1KzHWfr%2BGsc8OIWhAFaHT1CLuHQ6YiKirb8xzyS%2BmPYVgEdpG7vM5%2FOL%2Fm6%2FWVEhlIfCm19KcwhZpOSTk3RaEko59ew7PzLtMyIz7Rr9WVgN%2F%2FwsK7aAXDxYJFC4lRUtnxpMaBl4WhKdwNIOfq94br1YSM3mUaE5JJZ0eKaOYrN2aNMwi1xq%2FuesDr4sNedJkUfG1pfA4G0yz6VWbKOtvK%2BOSfjw6eqCyKQXdPFl%2F96H4N%2BiDrjIn5%2FiTd2Kzm2BedhzhhyD%2FI0MOCirMgGOqUBQDTS7uASDcS1LjkKUeBmpJ1GkR7SO6wodUwes03K2Kjtoar%2BppiorvPcHrUYusKHm8aShrFSwUIP4Ps%2FkYQET5PmobR3ccuaNU%2B4nQZymY79%2B8eKNQFkOO2wNAQt7Tm6Lh8kERXPTKAx4JGqNfDf%2Ft5hdRMfC2BGNn5drkQFzxiE0cXoPEOVWGC8l8mSkK8c9%2FfKb3mlVJafNmsyEejGPbtvz6PK&X-Amz-Signature=ba148415381490348928d5e717bba10878f5db43f436e821ae28b94cd79793a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW6FAGR6%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDjndzvqtxlqvu35SL8hAhz2RtMc3FcTf3KOFNFG2sFZAiEA1LN6AXWm9vGYZlDYkeNU6dZi%2FJCCB0rSMAY0LhOfvRsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMvGjAPVdD8juN7KrSrcA9NxaX5EqUVBRQTzl%2FTZ58iJ7gd8A6yMo0f0V%2Fj0I8SK8zVXNW7asGnDY5pOW97L5ZVmaBvh2vdcJelBIX0x7I8BiLkx5Bmf6IT26XX0My2H5QBgcl9luFtql72Xd2e%2FwvXRHDs%2FYxLHIWRaz3nuAhzBgp1TBSA7OVw1mTuWKiNsxmd9IUO1HqUd3VHw7jfHpnTS1GIihnwOLDd2LTHXMk9vdIpraIc97LejL8r7nfyJPqLSiQLxbHGLkc%2FdyNGiPti%2FZKrVu5Qew%2BgR9Zids0vSg4vlkB787zJbJOisjTlBp907V0wBTBq1Sb4FeqT1S60cxKS7m65GCTHmMHh%2BWJXCL6h3UOE6tEYzVGRkkK%2FtH5u6B1KzHWfr%2BGsc8OIWhAFaHT1CLuHQ6YiKirb8xzyS%2BmPYVgEdpG7vM5%2FOL%2Fm6%2FWVEhlIfCm19KcwhZpOSTk3RaEko59ew7PzLtMyIz7Rr9WVgN%2F%2FwsK7aAXDxYJFC4lRUtnxpMaBl4WhKdwNIOfq94br1YSM3mUaE5JJZ0eKaOYrN2aNMwi1xq%2FuesDr4sNedJkUfG1pfA4G0yz6VWbKOtvK%2BOSfjw6eqCyKQXdPFl%2F96H4N%2BiDrjIn5%2FiTd2Kzm2BedhzhhyD%2FI0MOCirMgGOqUBQDTS7uASDcS1LjkKUeBmpJ1GkR7SO6wodUwes03K2Kjtoar%2BppiorvPcHrUYusKHm8aShrFSwUIP4Ps%2FkYQET5PmobR3ccuaNU%2B4nQZymY79%2B8eKNQFkOO2wNAQt7Tm6Lh8kERXPTKAx4JGqNfDf%2Ft5hdRMfC2BGNn5drkQFzxiE0cXoPEOVWGC8l8mSkK8c9%2FfKb3mlVJafNmsyEejGPbtvz6PK&X-Amz-Signature=98718b8865a4f6a6304abadea9be435017c78b3820f0adde439b4922ccc7a32a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



