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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ME2MECE%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQCVRhZvTqLdX%2F5fmaHY3kH35p4lPfevuk4G6sOKEZkHYAIhAKCtZZE8KP2PGhAO4575XCodrkBR4Rskrp%2FaFBiq0Z76Kv8DCDoQABoMNjM3NDIzMTgzODA1IgxpNkqZwRr5BwXDJ0sq3ANVrRorNbziWUg5xPcC%2B1%2FlkCnP5TQieD%2F%2Fe91nC5Xz8mbNIIx8WO1YgUECY1QPnxjd1foIwQJQ%2Fl3S06U0Am7aHa3WxsNvJulEN9WXhtTlOgw%2B11tJkJUx%2FuWgToE0Iy2ozK1U7OMQao4vSr5MQfjGVvpLSep0Q26eGKYWNYPoF45FINxqhmk8ET9lWV3WrgcVak3iVPD8UEMtQ9ub0SpqH%2FT98Q0qfrYeCTG8eqh%2BPBfq8417tZdkHFGBI%2BqjnQMP4xOZpUT2xhsrySsdOCG6jTSk4MvA9hD6gJAot8I2HaWxqUy0I5FYHwfPVl%2F%2FfW1Bxna0aOT9h%2BKPbq%2B45z80We4Izn7d9RP1Fp2mpOsOZ7hXAXWFhebAapnVQ9WqEaquc4p1okxWXfucGHKag3LJ2O%2Bz5EkdcHVBTPg4FA33kNfWWKVD8UbDg2nEMWGA7x1NWIfxjd6IgOtnVwQomR%2BFHBtSS%2FaneE2etDHE7Dv6MNcew%2FUh%2FJdTipcxapr6Nk3lbo9nNjdUAwyCVP2kOV3YFF%2FQJoZpjAz5pJJcRhMO7UlvK53QIG%2FdaEBX73U1JUTdhWRYWFtz%2B1D%2BSiJ7tPx7vI32lKRtP2NLVUEscttDH1cWQwU1SnubTYyWCzDbjuzKBjqkAQJp%2B455u6apmy9GwF3YHNtapSA6ehwBTq7pgnRV9JBfaJsS%2BP5Nh00ULzdXRqG5tBrRvnrJwEfMNcszB1SS3%2FRVCGxfOdg4qZqYjW%2FAffNAhcHxu725ZBAr1HDbhA3N8O5yLcrpNwHnqoX6ludj%2FSgGTuFxOJnPJsjF%2Bgjk6DpPVCEfdqNPiroh7YxtdMmEqe9E5MOBRZdZtrnYHh56Ck%2B01X5%2F&X-Amz-Signature=e76a3427ff391b35e3291af4adb413d6e9a2028b36133327ad073fb4e4f3ebf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ME2MECE%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQCVRhZvTqLdX%2F5fmaHY3kH35p4lPfevuk4G6sOKEZkHYAIhAKCtZZE8KP2PGhAO4575XCodrkBR4Rskrp%2FaFBiq0Z76Kv8DCDoQABoMNjM3NDIzMTgzODA1IgxpNkqZwRr5BwXDJ0sq3ANVrRorNbziWUg5xPcC%2B1%2FlkCnP5TQieD%2F%2Fe91nC5Xz8mbNIIx8WO1YgUECY1QPnxjd1foIwQJQ%2Fl3S06U0Am7aHa3WxsNvJulEN9WXhtTlOgw%2B11tJkJUx%2FuWgToE0Iy2ozK1U7OMQao4vSr5MQfjGVvpLSep0Q26eGKYWNYPoF45FINxqhmk8ET9lWV3WrgcVak3iVPD8UEMtQ9ub0SpqH%2FT98Q0qfrYeCTG8eqh%2BPBfq8417tZdkHFGBI%2BqjnQMP4xOZpUT2xhsrySsdOCG6jTSk4MvA9hD6gJAot8I2HaWxqUy0I5FYHwfPVl%2F%2FfW1Bxna0aOT9h%2BKPbq%2B45z80We4Izn7d9RP1Fp2mpOsOZ7hXAXWFhebAapnVQ9WqEaquc4p1okxWXfucGHKag3LJ2O%2Bz5EkdcHVBTPg4FA33kNfWWKVD8UbDg2nEMWGA7x1NWIfxjd6IgOtnVwQomR%2BFHBtSS%2FaneE2etDHE7Dv6MNcew%2FUh%2FJdTipcxapr6Nk3lbo9nNjdUAwyCVP2kOV3YFF%2FQJoZpjAz5pJJcRhMO7UlvK53QIG%2FdaEBX73U1JUTdhWRYWFtz%2B1D%2BSiJ7tPx7vI32lKRtP2NLVUEscttDH1cWQwU1SnubTYyWCzDbjuzKBjqkAQJp%2B455u6apmy9GwF3YHNtapSA6ehwBTq7pgnRV9JBfaJsS%2BP5Nh00ULzdXRqG5tBrRvnrJwEfMNcszB1SS3%2FRVCGxfOdg4qZqYjW%2FAffNAhcHxu725ZBAr1HDbhA3N8O5yLcrpNwHnqoX6ludj%2FSgGTuFxOJnPJsjF%2Bgjk6DpPVCEfdqNPiroh7YxtdMmEqe9E5MOBRZdZtrnYHh56Ck%2B01X5%2F&X-Amz-Signature=e2cf61e7b3acd892881ee597db361eb688c89a22a22c1fc039bca5a589e0b97c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ME2MECE%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQCVRhZvTqLdX%2F5fmaHY3kH35p4lPfevuk4G6sOKEZkHYAIhAKCtZZE8KP2PGhAO4575XCodrkBR4Rskrp%2FaFBiq0Z76Kv8DCDoQABoMNjM3NDIzMTgzODA1IgxpNkqZwRr5BwXDJ0sq3ANVrRorNbziWUg5xPcC%2B1%2FlkCnP5TQieD%2F%2Fe91nC5Xz8mbNIIx8WO1YgUECY1QPnxjd1foIwQJQ%2Fl3S06U0Am7aHa3WxsNvJulEN9WXhtTlOgw%2B11tJkJUx%2FuWgToE0Iy2ozK1U7OMQao4vSr5MQfjGVvpLSep0Q26eGKYWNYPoF45FINxqhmk8ET9lWV3WrgcVak3iVPD8UEMtQ9ub0SpqH%2FT98Q0qfrYeCTG8eqh%2BPBfq8417tZdkHFGBI%2BqjnQMP4xOZpUT2xhsrySsdOCG6jTSk4MvA9hD6gJAot8I2HaWxqUy0I5FYHwfPVl%2F%2FfW1Bxna0aOT9h%2BKPbq%2B45z80We4Izn7d9RP1Fp2mpOsOZ7hXAXWFhebAapnVQ9WqEaquc4p1okxWXfucGHKag3LJ2O%2Bz5EkdcHVBTPg4FA33kNfWWKVD8UbDg2nEMWGA7x1NWIfxjd6IgOtnVwQomR%2BFHBtSS%2FaneE2etDHE7Dv6MNcew%2FUh%2FJdTipcxapr6Nk3lbo9nNjdUAwyCVP2kOV3YFF%2FQJoZpjAz5pJJcRhMO7UlvK53QIG%2FdaEBX73U1JUTdhWRYWFtz%2B1D%2BSiJ7tPx7vI32lKRtP2NLVUEscttDH1cWQwU1SnubTYyWCzDbjuzKBjqkAQJp%2B455u6apmy9GwF3YHNtapSA6ehwBTq7pgnRV9JBfaJsS%2BP5Nh00ULzdXRqG5tBrRvnrJwEfMNcszB1SS3%2FRVCGxfOdg4qZqYjW%2FAffNAhcHxu725ZBAr1HDbhA3N8O5yLcrpNwHnqoX6ludj%2FSgGTuFxOJnPJsjF%2Bgjk6DpPVCEfdqNPiroh7YxtdMmEqe9E5MOBRZdZtrnYHh56Ck%2B01X5%2F&X-Amz-Signature=4ae89435a68312308b8f1c5ae0ca197758cb8f59605fc29d7bc84494e0b69cbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ME2MECE%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQCVRhZvTqLdX%2F5fmaHY3kH35p4lPfevuk4G6sOKEZkHYAIhAKCtZZE8KP2PGhAO4575XCodrkBR4Rskrp%2FaFBiq0Z76Kv8DCDoQABoMNjM3NDIzMTgzODA1IgxpNkqZwRr5BwXDJ0sq3ANVrRorNbziWUg5xPcC%2B1%2FlkCnP5TQieD%2F%2Fe91nC5Xz8mbNIIx8WO1YgUECY1QPnxjd1foIwQJQ%2Fl3S06U0Am7aHa3WxsNvJulEN9WXhtTlOgw%2B11tJkJUx%2FuWgToE0Iy2ozK1U7OMQao4vSr5MQfjGVvpLSep0Q26eGKYWNYPoF45FINxqhmk8ET9lWV3WrgcVak3iVPD8UEMtQ9ub0SpqH%2FT98Q0qfrYeCTG8eqh%2BPBfq8417tZdkHFGBI%2BqjnQMP4xOZpUT2xhsrySsdOCG6jTSk4MvA9hD6gJAot8I2HaWxqUy0I5FYHwfPVl%2F%2FfW1Bxna0aOT9h%2BKPbq%2B45z80We4Izn7d9RP1Fp2mpOsOZ7hXAXWFhebAapnVQ9WqEaquc4p1okxWXfucGHKag3LJ2O%2Bz5EkdcHVBTPg4FA33kNfWWKVD8UbDg2nEMWGA7x1NWIfxjd6IgOtnVwQomR%2BFHBtSS%2FaneE2etDHE7Dv6MNcew%2FUh%2FJdTipcxapr6Nk3lbo9nNjdUAwyCVP2kOV3YFF%2FQJoZpjAz5pJJcRhMO7UlvK53QIG%2FdaEBX73U1JUTdhWRYWFtz%2B1D%2BSiJ7tPx7vI32lKRtP2NLVUEscttDH1cWQwU1SnubTYyWCzDbjuzKBjqkAQJp%2B455u6apmy9GwF3YHNtapSA6ehwBTq7pgnRV9JBfaJsS%2BP5Nh00ULzdXRqG5tBrRvnrJwEfMNcszB1SS3%2FRVCGxfOdg4qZqYjW%2FAffNAhcHxu725ZBAr1HDbhA3N8O5yLcrpNwHnqoX6ludj%2FSgGTuFxOJnPJsjF%2Bgjk6DpPVCEfdqNPiroh7YxtdMmEqe9E5MOBRZdZtrnYHh56Ck%2B01X5%2F&X-Amz-Signature=91dee64e556778547ec050a2330a1eb924a679f4d68f4d6f0ed04927b4e6da28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



