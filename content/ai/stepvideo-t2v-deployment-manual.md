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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LCV2D5%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIEHctyd2XlE88ayu36FRHkhCYe0mQAXX1kqjvgCgEiO2AiBE%2F9t9BUTb0SrANtFsUAK3kZZeV865Z1AYu0ghZT9wJyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0dQqfrjT3xm6Q263KtwDZOLsEZMiwtvtiaKMklH3dD5q6h1UMlrVsvgF6kaxza0PONPmRdc7j%2FJtvcKJD47tVngjtThntH47fOV1%2F6rW%2B%2FrSbHjtGQQUH1T7d9ykiNzJGbfXF4noNNWApJdAOhKN9%2BwWCqdYhhJt5qjQEWdjCGlvl4RvBrsiuPDRPJD2ZEewAMGMOQQ%2B0gSI4RThNvZG5rtcjeVjwK9iS2zR05ltbmbXqjd9NNAaN5VTplbaGFF7Y4lHHOZS7a7%2FyN%2B19N%2Fvt2yAfIfNY%2BLlokBlSuGEUh%2BvecZqyDa8tE1MZ%2FCekA8pq0IztL7LnPlWKEQzvgOd7GULFFHuHzL%2B3P9zE1NP49E1UTFm5QrKlgbHBcHh816p%2FMg36JUuFX7G%2FWZHKutcCfITX9FsCrGK1nvT9cg0sDUV7U%2BCeLxCxAWpVQoLf5Ft9U9q6g3lEajru%2FmVOUb686zmk50lk%2BXmvi1ZZzL72bBSZ49WSOwIg3g2DZDsaVEiKkvX3FIoqyKE1IoDgRvRXZPKkikhZ2loK%2BvjZsSllou2kZY%2Fx6RPB8bk%2FmIhHpe8bofqs6oPHP8kex83XUvbuU%2FHYOoaqbdefGU%2BeKGcuEZ4VEt%2BJArTkAs1xh2qDiWCWN8ytybesG2OtdEwxq7LywY6pgENbQcGjOsEhlWJ1Wk833JyLnmsZrBSPtCmpORT2JQ5tkoGFrkcbbM5dSzrHgeWtD4%2FcmmAD8OVONiFxscJ8FknlsAZB1I3mqEFRW2yovXkpHApfgWDTc7o2UDzUV64Wd85%2FxygcxPgUIwvz9sPGPsIUkyCcd2W6fGJJjJp%2BcYtIAIL2kdmf910%2FK5Aq1TlDlg%2BIFrjkCXj2yfsjCbbGSyTyEW7Fyse&X-Amz-Signature=526ba4156c1f87fbc0cbe64cc11e8abb817864ef8008cf0657ca987450bd8c22&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LCV2D5%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIEHctyd2XlE88ayu36FRHkhCYe0mQAXX1kqjvgCgEiO2AiBE%2F9t9BUTb0SrANtFsUAK3kZZeV865Z1AYu0ghZT9wJyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0dQqfrjT3xm6Q263KtwDZOLsEZMiwtvtiaKMklH3dD5q6h1UMlrVsvgF6kaxza0PONPmRdc7j%2FJtvcKJD47tVngjtThntH47fOV1%2F6rW%2B%2FrSbHjtGQQUH1T7d9ykiNzJGbfXF4noNNWApJdAOhKN9%2BwWCqdYhhJt5qjQEWdjCGlvl4RvBrsiuPDRPJD2ZEewAMGMOQQ%2B0gSI4RThNvZG5rtcjeVjwK9iS2zR05ltbmbXqjd9NNAaN5VTplbaGFF7Y4lHHOZS7a7%2FyN%2B19N%2Fvt2yAfIfNY%2BLlokBlSuGEUh%2BvecZqyDa8tE1MZ%2FCekA8pq0IztL7LnPlWKEQzvgOd7GULFFHuHzL%2B3P9zE1NP49E1UTFm5QrKlgbHBcHh816p%2FMg36JUuFX7G%2FWZHKutcCfITX9FsCrGK1nvT9cg0sDUV7U%2BCeLxCxAWpVQoLf5Ft9U9q6g3lEajru%2FmVOUb686zmk50lk%2BXmvi1ZZzL72bBSZ49WSOwIg3g2DZDsaVEiKkvX3FIoqyKE1IoDgRvRXZPKkikhZ2loK%2BvjZsSllou2kZY%2Fx6RPB8bk%2FmIhHpe8bofqs6oPHP8kex83XUvbuU%2FHYOoaqbdefGU%2BeKGcuEZ4VEt%2BJArTkAs1xh2qDiWCWN8ytybesG2OtdEwxq7LywY6pgENbQcGjOsEhlWJ1Wk833JyLnmsZrBSPtCmpORT2JQ5tkoGFrkcbbM5dSzrHgeWtD4%2FcmmAD8OVONiFxscJ8FknlsAZB1I3mqEFRW2yovXkpHApfgWDTc7o2UDzUV64Wd85%2FxygcxPgUIwvz9sPGPsIUkyCcd2W6fGJJjJp%2BcYtIAIL2kdmf910%2FK5Aq1TlDlg%2BIFrjkCXj2yfsjCbbGSyTyEW7Fyse&X-Amz-Signature=f4093dc3df5eb9079a614f3918c86c9dc9afcbfdcf93cf00e7983ed9ec59202e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LCV2D5%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIEHctyd2XlE88ayu36FRHkhCYe0mQAXX1kqjvgCgEiO2AiBE%2F9t9BUTb0SrANtFsUAK3kZZeV865Z1AYu0ghZT9wJyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0dQqfrjT3xm6Q263KtwDZOLsEZMiwtvtiaKMklH3dD5q6h1UMlrVsvgF6kaxza0PONPmRdc7j%2FJtvcKJD47tVngjtThntH47fOV1%2F6rW%2B%2FrSbHjtGQQUH1T7d9ykiNzJGbfXF4noNNWApJdAOhKN9%2BwWCqdYhhJt5qjQEWdjCGlvl4RvBrsiuPDRPJD2ZEewAMGMOQQ%2B0gSI4RThNvZG5rtcjeVjwK9iS2zR05ltbmbXqjd9NNAaN5VTplbaGFF7Y4lHHOZS7a7%2FyN%2B19N%2Fvt2yAfIfNY%2BLlokBlSuGEUh%2BvecZqyDa8tE1MZ%2FCekA8pq0IztL7LnPlWKEQzvgOd7GULFFHuHzL%2B3P9zE1NP49E1UTFm5QrKlgbHBcHh816p%2FMg36JUuFX7G%2FWZHKutcCfITX9FsCrGK1nvT9cg0sDUV7U%2BCeLxCxAWpVQoLf5Ft9U9q6g3lEajru%2FmVOUb686zmk50lk%2BXmvi1ZZzL72bBSZ49WSOwIg3g2DZDsaVEiKkvX3FIoqyKE1IoDgRvRXZPKkikhZ2loK%2BvjZsSllou2kZY%2Fx6RPB8bk%2FmIhHpe8bofqs6oPHP8kex83XUvbuU%2FHYOoaqbdefGU%2BeKGcuEZ4VEt%2BJArTkAs1xh2qDiWCWN8ytybesG2OtdEwxq7LywY6pgENbQcGjOsEhlWJ1Wk833JyLnmsZrBSPtCmpORT2JQ5tkoGFrkcbbM5dSzrHgeWtD4%2FcmmAD8OVONiFxscJ8FknlsAZB1I3mqEFRW2yovXkpHApfgWDTc7o2UDzUV64Wd85%2FxygcxPgUIwvz9sPGPsIUkyCcd2W6fGJJjJp%2BcYtIAIL2kdmf910%2FK5Aq1TlDlg%2BIFrjkCXj2yfsjCbbGSyTyEW7Fyse&X-Amz-Signature=15d43d3207dc70646f9f1346c2e998ab997a4abfd064e844f67adaefd1065aa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657LCV2D5%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIEHctyd2XlE88ayu36FRHkhCYe0mQAXX1kqjvgCgEiO2AiBE%2F9t9BUTb0SrANtFsUAK3kZZeV865Z1AYu0ghZT9wJyqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0dQqfrjT3xm6Q263KtwDZOLsEZMiwtvtiaKMklH3dD5q6h1UMlrVsvgF6kaxza0PONPmRdc7j%2FJtvcKJD47tVngjtThntH47fOV1%2F6rW%2B%2FrSbHjtGQQUH1T7d9ykiNzJGbfXF4noNNWApJdAOhKN9%2BwWCqdYhhJt5qjQEWdjCGlvl4RvBrsiuPDRPJD2ZEewAMGMOQQ%2B0gSI4RThNvZG5rtcjeVjwK9iS2zR05ltbmbXqjd9NNAaN5VTplbaGFF7Y4lHHOZS7a7%2FyN%2B19N%2Fvt2yAfIfNY%2BLlokBlSuGEUh%2BvecZqyDa8tE1MZ%2FCekA8pq0IztL7LnPlWKEQzvgOd7GULFFHuHzL%2B3P9zE1NP49E1UTFm5QrKlgbHBcHh816p%2FMg36JUuFX7G%2FWZHKutcCfITX9FsCrGK1nvT9cg0sDUV7U%2BCeLxCxAWpVQoLf5Ft9U9q6g3lEajru%2FmVOUb686zmk50lk%2BXmvi1ZZzL72bBSZ49WSOwIg3g2DZDsaVEiKkvX3FIoqyKE1IoDgRvRXZPKkikhZ2loK%2BvjZsSllou2kZY%2Fx6RPB8bk%2FmIhHpe8bofqs6oPHP8kex83XUvbuU%2FHYOoaqbdefGU%2BeKGcuEZ4VEt%2BJArTkAs1xh2qDiWCWN8ytybesG2OtdEwxq7LywY6pgENbQcGjOsEhlWJ1Wk833JyLnmsZrBSPtCmpORT2JQ5tkoGFrkcbbM5dSzrHgeWtD4%2FcmmAD8OVONiFxscJ8FknlsAZB1I3mqEFRW2yovXkpHApfgWDTc7o2UDzUV64Wd85%2FxygcxPgUIwvz9sPGPsIUkyCcd2W6fGJJjJp%2BcYtIAIL2kdmf910%2FK5Aq1TlDlg%2BIFrjkCXj2yfsjCbbGSyTyEW7Fyse&X-Amz-Signature=ac6907a99958d8f52938b5d9eb645a59dc2e542ebf3073bc1036d028927b76ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



