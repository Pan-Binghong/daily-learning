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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652WZSN26%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCM8ZuzFIxJs3T30gPfwavjh8V4e7SO2lC%2BYDSxNjzuwQIhAOpEQuMFl4FejpNlOGJlnmdFqTYD3Gxhcw47G3lAQA98KogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzF5ddDdrhJZOJ90Soq3APpPPpYi2XcGA%2FlLTZiM83ril8QbGEkjHboKVJI8wiG3%2Bfb4%2BpAZGeq24io3T631J6XRVqb416yS2FhDjjzMjKwEW7KktCbJO67s1GwCsirw754pMGK9LMEbBSCRZc6jCkl01pgdDVhcljZ7ni6Ga6bnLICPbpmDtHNzUEGyKiCaqJG9yB65S%2FIq6XXRqzdoSMSXVBslkJDnmKVI9Mo8SLZvgfF9gpEIiGIerYyqzhh46Rz%2BUVvgDPNXPX%2BIuxYADMuIb4thK9YT0dqLm9xBWcb0ORb5aLLn3L%2Bmvs1nOhPR%2Blb%2BK3%2Fn5psKEAAApdLkr604iO2NmSgmqeRy4IbzhWrgEwPLhkdIPPpuLAiGDp7EMNwpcmKHwobKOK%2B1omlhy8p2EbLwKbgzYT0cZAh9b8NccwxRwgDVhbtQajSlHlf4%2B%2FMECxpkc6wdJJC%2BPfkJKe%2FPnrx5o%2BYAvxpENMGfQV2%2F16%2ByBPDv%2FwCDxH68Evw7fGaPHrRoC%2FQlFPu2vg4DEa9hBwOhNEBRyD0F1XKpIq4ZamcJ8PJlHHlSo2HEmTCVBDE5jk002zYMzXfdxOGWiuJp%2Bx%2F3UVUU34y38wcnojMaHHsy86R3D8K%2Fosc3FEwsftcL7JS3mi7Sl7CWDDx28zKBjqkAfGNeYIJ1nxoyOA37jKevgYODZ5aSWB%2FM8baV9BpmkplPFGi3C7Uvod762uCaAxJMfhLhEw0CnsqZ10%2F2xJeb09s0uCyoMLpLdC5xO0MGKmrtcpz%2FMOEtWt%2BlXIApRiyD%2BXVp0pQjPh%2BWw3sd7RQw2fut%2Bof60Whuleudi%2FMr5Y6leU6ELGufCdGIiKHIcuAFNJJoydN9hlN%2FcH6Zy42DkDCjhpU&X-Amz-Signature=32ecfac17f2661eac499d4b97c2074bf42502ac8f32c1142923a550648f44de5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652WZSN26%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCM8ZuzFIxJs3T30gPfwavjh8V4e7SO2lC%2BYDSxNjzuwQIhAOpEQuMFl4FejpNlOGJlnmdFqTYD3Gxhcw47G3lAQA98KogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzF5ddDdrhJZOJ90Soq3APpPPpYi2XcGA%2FlLTZiM83ril8QbGEkjHboKVJI8wiG3%2Bfb4%2BpAZGeq24io3T631J6XRVqb416yS2FhDjjzMjKwEW7KktCbJO67s1GwCsirw754pMGK9LMEbBSCRZc6jCkl01pgdDVhcljZ7ni6Ga6bnLICPbpmDtHNzUEGyKiCaqJG9yB65S%2FIq6XXRqzdoSMSXVBslkJDnmKVI9Mo8SLZvgfF9gpEIiGIerYyqzhh46Rz%2BUVvgDPNXPX%2BIuxYADMuIb4thK9YT0dqLm9xBWcb0ORb5aLLn3L%2Bmvs1nOhPR%2Blb%2BK3%2Fn5psKEAAApdLkr604iO2NmSgmqeRy4IbzhWrgEwPLhkdIPPpuLAiGDp7EMNwpcmKHwobKOK%2B1omlhy8p2EbLwKbgzYT0cZAh9b8NccwxRwgDVhbtQajSlHlf4%2B%2FMECxpkc6wdJJC%2BPfkJKe%2FPnrx5o%2BYAvxpENMGfQV2%2F16%2ByBPDv%2FwCDxH68Evw7fGaPHrRoC%2FQlFPu2vg4DEa9hBwOhNEBRyD0F1XKpIq4ZamcJ8PJlHHlSo2HEmTCVBDE5jk002zYMzXfdxOGWiuJp%2Bx%2F3UVUU34y38wcnojMaHHsy86R3D8K%2Fosc3FEwsftcL7JS3mi7Sl7CWDDx28zKBjqkAfGNeYIJ1nxoyOA37jKevgYODZ5aSWB%2FM8baV9BpmkplPFGi3C7Uvod762uCaAxJMfhLhEw0CnsqZ10%2F2xJeb09s0uCyoMLpLdC5xO0MGKmrtcpz%2FMOEtWt%2BlXIApRiyD%2BXVp0pQjPh%2BWw3sd7RQw2fut%2Bof60Whuleudi%2FMr5Y6leU6ELGufCdGIiKHIcuAFNJJoydN9hlN%2FcH6Zy42DkDCjhpU&X-Amz-Signature=4d0ea1277741a10f2cdd8129090a8174af5a5f353422a1996dd69cb947e909fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652WZSN26%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCM8ZuzFIxJs3T30gPfwavjh8V4e7SO2lC%2BYDSxNjzuwQIhAOpEQuMFl4FejpNlOGJlnmdFqTYD3Gxhcw47G3lAQA98KogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzF5ddDdrhJZOJ90Soq3APpPPpYi2XcGA%2FlLTZiM83ril8QbGEkjHboKVJI8wiG3%2Bfb4%2BpAZGeq24io3T631J6XRVqb416yS2FhDjjzMjKwEW7KktCbJO67s1GwCsirw754pMGK9LMEbBSCRZc6jCkl01pgdDVhcljZ7ni6Ga6bnLICPbpmDtHNzUEGyKiCaqJG9yB65S%2FIq6XXRqzdoSMSXVBslkJDnmKVI9Mo8SLZvgfF9gpEIiGIerYyqzhh46Rz%2BUVvgDPNXPX%2BIuxYADMuIb4thK9YT0dqLm9xBWcb0ORb5aLLn3L%2Bmvs1nOhPR%2Blb%2BK3%2Fn5psKEAAApdLkr604iO2NmSgmqeRy4IbzhWrgEwPLhkdIPPpuLAiGDp7EMNwpcmKHwobKOK%2B1omlhy8p2EbLwKbgzYT0cZAh9b8NccwxRwgDVhbtQajSlHlf4%2B%2FMECxpkc6wdJJC%2BPfkJKe%2FPnrx5o%2BYAvxpENMGfQV2%2F16%2ByBPDv%2FwCDxH68Evw7fGaPHrRoC%2FQlFPu2vg4DEa9hBwOhNEBRyD0F1XKpIq4ZamcJ8PJlHHlSo2HEmTCVBDE5jk002zYMzXfdxOGWiuJp%2Bx%2F3UVUU34y38wcnojMaHHsy86R3D8K%2Fosc3FEwsftcL7JS3mi7Sl7CWDDx28zKBjqkAfGNeYIJ1nxoyOA37jKevgYODZ5aSWB%2FM8baV9BpmkplPFGi3C7Uvod762uCaAxJMfhLhEw0CnsqZ10%2F2xJeb09s0uCyoMLpLdC5xO0MGKmrtcpz%2FMOEtWt%2BlXIApRiyD%2BXVp0pQjPh%2BWw3sd7RQw2fut%2Bof60Whuleudi%2FMr5Y6leU6ELGufCdGIiKHIcuAFNJJoydN9hlN%2FcH6Zy42DkDCjhpU&X-Amz-Signature=dde2950d18014cb7af3ba234af61960f2693b504abbf83e37043996b8598ad52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652WZSN26%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCM8ZuzFIxJs3T30gPfwavjh8V4e7SO2lC%2BYDSxNjzuwQIhAOpEQuMFl4FejpNlOGJlnmdFqTYD3Gxhcw47G3lAQA98KogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzF5ddDdrhJZOJ90Soq3APpPPpYi2XcGA%2FlLTZiM83ril8QbGEkjHboKVJI8wiG3%2Bfb4%2BpAZGeq24io3T631J6XRVqb416yS2FhDjjzMjKwEW7KktCbJO67s1GwCsirw754pMGK9LMEbBSCRZc6jCkl01pgdDVhcljZ7ni6Ga6bnLICPbpmDtHNzUEGyKiCaqJG9yB65S%2FIq6XXRqzdoSMSXVBslkJDnmKVI9Mo8SLZvgfF9gpEIiGIerYyqzhh46Rz%2BUVvgDPNXPX%2BIuxYADMuIb4thK9YT0dqLm9xBWcb0ORb5aLLn3L%2Bmvs1nOhPR%2Blb%2BK3%2Fn5psKEAAApdLkr604iO2NmSgmqeRy4IbzhWrgEwPLhkdIPPpuLAiGDp7EMNwpcmKHwobKOK%2B1omlhy8p2EbLwKbgzYT0cZAh9b8NccwxRwgDVhbtQajSlHlf4%2B%2FMECxpkc6wdJJC%2BPfkJKe%2FPnrx5o%2BYAvxpENMGfQV2%2F16%2ByBPDv%2FwCDxH68Evw7fGaPHrRoC%2FQlFPu2vg4DEa9hBwOhNEBRyD0F1XKpIq4ZamcJ8PJlHHlSo2HEmTCVBDE5jk002zYMzXfdxOGWiuJp%2Bx%2F3UVUU34y38wcnojMaHHsy86R3D8K%2Fosc3FEwsftcL7JS3mi7Sl7CWDDx28zKBjqkAfGNeYIJ1nxoyOA37jKevgYODZ5aSWB%2FM8baV9BpmkplPFGi3C7Uvod762uCaAxJMfhLhEw0CnsqZ10%2F2xJeb09s0uCyoMLpLdC5xO0MGKmrtcpz%2FMOEtWt%2BlXIApRiyD%2BXVp0pQjPh%2BWw3sd7RQw2fut%2Bof60Whuleudi%2FMr5Y6leU6ELGufCdGIiKHIcuAFNJJoydN9hlN%2FcH6Zy42DkDCjhpU&X-Amz-Signature=3013f4bd56e5d2a38256047761a654fe7d3c546394f52c2b33b4b96b2c6a60f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



