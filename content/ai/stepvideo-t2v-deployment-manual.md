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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYFRXL4P%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICExYWqL8m9bMLEI7XUhUDR9j7M5flwE6gHSahu5A69fAiEA%2FhR%2F15SVxhB7ONx8O9z3E8s8PwzOO9uBL0l5uP0Pifwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL7pwJAeU%2FsF55cIvCrcA1FmY9KOV5AhUtiFDXR5pSUQrLCdlN1Yb71cVM0BySUl1n8EVZQlPTF6Ruav1g0HnNhhH3v4OEwiMEBcEIADNCod9aMQ0CnVM%2FEXxdHesZBvlvS12iMqLPE8WiJhYGuVBbTnFjRmixgoICWf7VoIK%2BluDZYUPP6jNEpU6wRXCBGS1goKzg5lAx8YVveI%2FrcuW8nYWJabzfTo9tgtAp0ChKYNKKLH%2Fo%2FxxSzNhDTPGb%2BgTgcj9YLqGalsTYw2pl4H5ccmpeVXqRf73xDOGlVkz%2B4ZPAMvWpkbM0B2RCMTa48bK01QfkpFQjJvh4xb463JJCWf615bPzISBvLePRiB6U4Yy%2F0IE3FyizBKGVxG0chFJ%2B5kgsigoEGmJODMfRyzFqw2VMeLF4PB%2BxinyC57vUCa9hRLf%2BG0jPNqiwxF6FIcJdO9VIteGaWV6ZMFmhiuP%2Fa55H1jZWsvE15xRRNbNmA4fhJZ5EXXEBWFzrcPHuuJZ%2FMn%2BPz7m39xtCSYiY96Z97HRvjLOK8LudbUi6vVJmCcQ9cY795hEcii6hFQlcGZoHb%2FrObLhsZ2IbSDaiRDOC3dkSDR9PXNUH2qPWBGXhbERnC%2BDnFOVmHVrxn9mohvQIQCGOnhGh%2FRwa1LMM3zws0GOqUBuy%2Bc6S4eSkAwq1OmtddylhzNq8liSKvK8r0IxyoU7%2BZ%2B5KSnyA%2BF3YBE0FU7P7aDOSAuZw1O6lXCKa07fAdwWKJdzQ4VyEcPRfjtCpl4E%2F1r7w%2F%2FcR3fLRrUcxzUilIlcaAFm1EnmOQXGx8OaS%2BN7H26aSkB6Wnt9YTBNWo%2FxEES1fZxMFJhxe8A76XlD28J%2FjLU5038BVA%2FbbNX8%2FGjlSDEYUmy&X-Amz-Signature=049661018e9f3ec935b12555f667839f4c1601a7b10efc4781db767cfd9d8617&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYFRXL4P%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICExYWqL8m9bMLEI7XUhUDR9j7M5flwE6gHSahu5A69fAiEA%2FhR%2F15SVxhB7ONx8O9z3E8s8PwzOO9uBL0l5uP0Pifwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL7pwJAeU%2FsF55cIvCrcA1FmY9KOV5AhUtiFDXR5pSUQrLCdlN1Yb71cVM0BySUl1n8EVZQlPTF6Ruav1g0HnNhhH3v4OEwiMEBcEIADNCod9aMQ0CnVM%2FEXxdHesZBvlvS12iMqLPE8WiJhYGuVBbTnFjRmixgoICWf7VoIK%2BluDZYUPP6jNEpU6wRXCBGS1goKzg5lAx8YVveI%2FrcuW8nYWJabzfTo9tgtAp0ChKYNKKLH%2Fo%2FxxSzNhDTPGb%2BgTgcj9YLqGalsTYw2pl4H5ccmpeVXqRf73xDOGlVkz%2B4ZPAMvWpkbM0B2RCMTa48bK01QfkpFQjJvh4xb463JJCWf615bPzISBvLePRiB6U4Yy%2F0IE3FyizBKGVxG0chFJ%2B5kgsigoEGmJODMfRyzFqw2VMeLF4PB%2BxinyC57vUCa9hRLf%2BG0jPNqiwxF6FIcJdO9VIteGaWV6ZMFmhiuP%2Fa55H1jZWsvE15xRRNbNmA4fhJZ5EXXEBWFzrcPHuuJZ%2FMn%2BPz7m39xtCSYiY96Z97HRvjLOK8LudbUi6vVJmCcQ9cY795hEcii6hFQlcGZoHb%2FrObLhsZ2IbSDaiRDOC3dkSDR9PXNUH2qPWBGXhbERnC%2BDnFOVmHVrxn9mohvQIQCGOnhGh%2FRwa1LMM3zws0GOqUBuy%2Bc6S4eSkAwq1OmtddylhzNq8liSKvK8r0IxyoU7%2BZ%2B5KSnyA%2BF3YBE0FU7P7aDOSAuZw1O6lXCKa07fAdwWKJdzQ4VyEcPRfjtCpl4E%2F1r7w%2F%2FcR3fLRrUcxzUilIlcaAFm1EnmOQXGx8OaS%2BN7H26aSkB6Wnt9YTBNWo%2FxEES1fZxMFJhxe8A76XlD28J%2FjLU5038BVA%2FbbNX8%2FGjlSDEYUmy&X-Amz-Signature=b474503f617272bef246e4ccbad2bd2536dc9971451e14365fb2a7ca36d2afd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYFRXL4P%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICExYWqL8m9bMLEI7XUhUDR9j7M5flwE6gHSahu5A69fAiEA%2FhR%2F15SVxhB7ONx8O9z3E8s8PwzOO9uBL0l5uP0Pifwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL7pwJAeU%2FsF55cIvCrcA1FmY9KOV5AhUtiFDXR5pSUQrLCdlN1Yb71cVM0BySUl1n8EVZQlPTF6Ruav1g0HnNhhH3v4OEwiMEBcEIADNCod9aMQ0CnVM%2FEXxdHesZBvlvS12iMqLPE8WiJhYGuVBbTnFjRmixgoICWf7VoIK%2BluDZYUPP6jNEpU6wRXCBGS1goKzg5lAx8YVveI%2FrcuW8nYWJabzfTo9tgtAp0ChKYNKKLH%2Fo%2FxxSzNhDTPGb%2BgTgcj9YLqGalsTYw2pl4H5ccmpeVXqRf73xDOGlVkz%2B4ZPAMvWpkbM0B2RCMTa48bK01QfkpFQjJvh4xb463JJCWf615bPzISBvLePRiB6U4Yy%2F0IE3FyizBKGVxG0chFJ%2B5kgsigoEGmJODMfRyzFqw2VMeLF4PB%2BxinyC57vUCa9hRLf%2BG0jPNqiwxF6FIcJdO9VIteGaWV6ZMFmhiuP%2Fa55H1jZWsvE15xRRNbNmA4fhJZ5EXXEBWFzrcPHuuJZ%2FMn%2BPz7m39xtCSYiY96Z97HRvjLOK8LudbUi6vVJmCcQ9cY795hEcii6hFQlcGZoHb%2FrObLhsZ2IbSDaiRDOC3dkSDR9PXNUH2qPWBGXhbERnC%2BDnFOVmHVrxn9mohvQIQCGOnhGh%2FRwa1LMM3zws0GOqUBuy%2Bc6S4eSkAwq1OmtddylhzNq8liSKvK8r0IxyoU7%2BZ%2B5KSnyA%2BF3YBE0FU7P7aDOSAuZw1O6lXCKa07fAdwWKJdzQ4VyEcPRfjtCpl4E%2F1r7w%2F%2FcR3fLRrUcxzUilIlcaAFm1EnmOQXGx8OaS%2BN7H26aSkB6Wnt9YTBNWo%2FxEES1fZxMFJhxe8A76XlD28J%2FjLU5038BVA%2FbbNX8%2FGjlSDEYUmy&X-Amz-Signature=0c28969b95768e738efb29ce3ac33b1b012adacc4fbba1eff68387f807d89cdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYFRXL4P%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICExYWqL8m9bMLEI7XUhUDR9j7M5flwE6gHSahu5A69fAiEA%2FhR%2F15SVxhB7ONx8O9z3E8s8PwzOO9uBL0l5uP0Pifwq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDL7pwJAeU%2FsF55cIvCrcA1FmY9KOV5AhUtiFDXR5pSUQrLCdlN1Yb71cVM0BySUl1n8EVZQlPTF6Ruav1g0HnNhhH3v4OEwiMEBcEIADNCod9aMQ0CnVM%2FEXxdHesZBvlvS12iMqLPE8WiJhYGuVBbTnFjRmixgoICWf7VoIK%2BluDZYUPP6jNEpU6wRXCBGS1goKzg5lAx8YVveI%2FrcuW8nYWJabzfTo9tgtAp0ChKYNKKLH%2Fo%2FxxSzNhDTPGb%2BgTgcj9YLqGalsTYw2pl4H5ccmpeVXqRf73xDOGlVkz%2B4ZPAMvWpkbM0B2RCMTa48bK01QfkpFQjJvh4xb463JJCWf615bPzISBvLePRiB6U4Yy%2F0IE3FyizBKGVxG0chFJ%2B5kgsigoEGmJODMfRyzFqw2VMeLF4PB%2BxinyC57vUCa9hRLf%2BG0jPNqiwxF6FIcJdO9VIteGaWV6ZMFmhiuP%2Fa55H1jZWsvE15xRRNbNmA4fhJZ5EXXEBWFzrcPHuuJZ%2FMn%2BPz7m39xtCSYiY96Z97HRvjLOK8LudbUi6vVJmCcQ9cY795hEcii6hFQlcGZoHb%2FrObLhsZ2IbSDaiRDOC3dkSDR9PXNUH2qPWBGXhbERnC%2BDnFOVmHVrxn9mohvQIQCGOnhGh%2FRwa1LMM3zws0GOqUBuy%2Bc6S4eSkAwq1OmtddylhzNq8liSKvK8r0IxyoU7%2BZ%2B5KSnyA%2BF3YBE0FU7P7aDOSAuZw1O6lXCKa07fAdwWKJdzQ4VyEcPRfjtCpl4E%2F1r7w%2F%2FcR3fLRrUcxzUilIlcaAFm1EnmOQXGx8OaS%2BN7H26aSkB6Wnt9YTBNWo%2FxEES1fZxMFJhxe8A76XlD28J%2FjLU5038BVA%2FbbNX8%2FGjlSDEYUmy&X-Amz-Signature=de1283e8e4f9369e2a49576740fe7d1a56eebd53a3edcc1e4abb458f1b453843&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



