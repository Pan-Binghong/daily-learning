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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWWXBRMN%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAkatMYF2o6RqoIM9VoJSx0kEgcnAt2R7qHkJoNwNlpbAiANxbRSESLwTZVHFap1Rodqer0k93b8rwREXkDe4k9PpSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgdLH%2BtPYrfO2HnpCKtwDopaWAhKOYXvmAB1TIuebwaMJsGfCm04JtzmEw3BAFVkSP2xhl7nWPW3wns1bQvZPAAkSgVoo2PQJzcpYIeae2xjtqD1c6uzJbvWuquhvqZAL7RNnqYfVq5wJvwE9M7iy1LqSR%2BdCE%2B%2F9Mdj1BRUAXD%2B228F45zjA732cSQZJc8at%2BdGv4wnwFB3A15L8b%2BkfIK0Q1w4DBk24MeSLZBDXsS%2BxL2ueESs5NZ%2Fo%2FbOas%2BzZFxNyXixYXm1iVr6Dn%2FVZEr3r1vopNVNYYNO1u1uZ6UPbdUPbp4GDHwpcdPJ%2B4Pa2C%2BBWn7iujNKyZe56BR4WrdEYc5%2Fzp9KgJovLGlUbVahztFsmCDb8%2FH5XPFp%2BbatV5rATjPri9RPcOl9i62%2FqN1VqjKEyM8I23oxbIOxWZ22OsSQAZ6NhacyEPfM1G%2FF5flUGmFYO2qapVptS1SVmoytrt2v4Yxelw9PgERNnF1GQEUF9zfjo%2BRATTVBA2qkPe1WT3jXlkgxqtcoFcY7teybwHF5sYd9uVkidUxZFYiVND1CMT4OY%2BA7tvzdihWscP78%2BfaFWi7nQab44oVhImohDaks%2FXOph5mBezf3KiDxGpQo2l%2BIdHeLy%2FmnXKF0Prd1NC73qjUxFEl8wup7EzAY6pgFzG%2B59A6FImvVq49sboNGs7jrPsfaINTdTV7nmJsryHCDe1t4ZYhpvnnqAnQ3DTbk323MyYM6ICsyXPevMQJWzNiGXuF%2Bw7dZuf5rH7sLu2oCqJPkL7yx8t5Pg5VDGZzzqJwyBsU1pi9gtZUwESZ0%2BA52yvcIKKOFHn4vFkFv9JnpeV8psN71JS9PijN5UB%2BQEZslabpNjuwuLwdHYK6o3hMfCJJ4j&X-Amz-Signature=5ddf60ef88865a45f1ea8e8ea0197c9d3b955679fa033343671a6ba18e19bd03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWWXBRMN%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAkatMYF2o6RqoIM9VoJSx0kEgcnAt2R7qHkJoNwNlpbAiANxbRSESLwTZVHFap1Rodqer0k93b8rwREXkDe4k9PpSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgdLH%2BtPYrfO2HnpCKtwDopaWAhKOYXvmAB1TIuebwaMJsGfCm04JtzmEw3BAFVkSP2xhl7nWPW3wns1bQvZPAAkSgVoo2PQJzcpYIeae2xjtqD1c6uzJbvWuquhvqZAL7RNnqYfVq5wJvwE9M7iy1LqSR%2BdCE%2B%2F9Mdj1BRUAXD%2B228F45zjA732cSQZJc8at%2BdGv4wnwFB3A15L8b%2BkfIK0Q1w4DBk24MeSLZBDXsS%2BxL2ueESs5NZ%2Fo%2FbOas%2BzZFxNyXixYXm1iVr6Dn%2FVZEr3r1vopNVNYYNO1u1uZ6UPbdUPbp4GDHwpcdPJ%2B4Pa2C%2BBWn7iujNKyZe56BR4WrdEYc5%2Fzp9KgJovLGlUbVahztFsmCDb8%2FH5XPFp%2BbatV5rATjPri9RPcOl9i62%2FqN1VqjKEyM8I23oxbIOxWZ22OsSQAZ6NhacyEPfM1G%2FF5flUGmFYO2qapVptS1SVmoytrt2v4Yxelw9PgERNnF1GQEUF9zfjo%2BRATTVBA2qkPe1WT3jXlkgxqtcoFcY7teybwHF5sYd9uVkidUxZFYiVND1CMT4OY%2BA7tvzdihWscP78%2BfaFWi7nQab44oVhImohDaks%2FXOph5mBezf3KiDxGpQo2l%2BIdHeLy%2FmnXKF0Prd1NC73qjUxFEl8wup7EzAY6pgFzG%2B59A6FImvVq49sboNGs7jrPsfaINTdTV7nmJsryHCDe1t4ZYhpvnnqAnQ3DTbk323MyYM6ICsyXPevMQJWzNiGXuF%2Bw7dZuf5rH7sLu2oCqJPkL7yx8t5Pg5VDGZzzqJwyBsU1pi9gtZUwESZ0%2BA52yvcIKKOFHn4vFkFv9JnpeV8psN71JS9PijN5UB%2BQEZslabpNjuwuLwdHYK6o3hMfCJJ4j&X-Amz-Signature=0493e6f7d0bb4e6d0fec66d73f88a23ee4456b812482c51411a74a7b3ed98c65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWWXBRMN%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAkatMYF2o6RqoIM9VoJSx0kEgcnAt2R7qHkJoNwNlpbAiANxbRSESLwTZVHFap1Rodqer0k93b8rwREXkDe4k9PpSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgdLH%2BtPYrfO2HnpCKtwDopaWAhKOYXvmAB1TIuebwaMJsGfCm04JtzmEw3BAFVkSP2xhl7nWPW3wns1bQvZPAAkSgVoo2PQJzcpYIeae2xjtqD1c6uzJbvWuquhvqZAL7RNnqYfVq5wJvwE9M7iy1LqSR%2BdCE%2B%2F9Mdj1BRUAXD%2B228F45zjA732cSQZJc8at%2BdGv4wnwFB3A15L8b%2BkfIK0Q1w4DBk24MeSLZBDXsS%2BxL2ueESs5NZ%2Fo%2FbOas%2BzZFxNyXixYXm1iVr6Dn%2FVZEr3r1vopNVNYYNO1u1uZ6UPbdUPbp4GDHwpcdPJ%2B4Pa2C%2BBWn7iujNKyZe56BR4WrdEYc5%2Fzp9KgJovLGlUbVahztFsmCDb8%2FH5XPFp%2BbatV5rATjPri9RPcOl9i62%2FqN1VqjKEyM8I23oxbIOxWZ22OsSQAZ6NhacyEPfM1G%2FF5flUGmFYO2qapVptS1SVmoytrt2v4Yxelw9PgERNnF1GQEUF9zfjo%2BRATTVBA2qkPe1WT3jXlkgxqtcoFcY7teybwHF5sYd9uVkidUxZFYiVND1CMT4OY%2BA7tvzdihWscP78%2BfaFWi7nQab44oVhImohDaks%2FXOph5mBezf3KiDxGpQo2l%2BIdHeLy%2FmnXKF0Prd1NC73qjUxFEl8wup7EzAY6pgFzG%2B59A6FImvVq49sboNGs7jrPsfaINTdTV7nmJsryHCDe1t4ZYhpvnnqAnQ3DTbk323MyYM6ICsyXPevMQJWzNiGXuF%2Bw7dZuf5rH7sLu2oCqJPkL7yx8t5Pg5VDGZzzqJwyBsU1pi9gtZUwESZ0%2BA52yvcIKKOFHn4vFkFv9JnpeV8psN71JS9PijN5UB%2BQEZslabpNjuwuLwdHYK6o3hMfCJJ4j&X-Amz-Signature=33d4a732a5338e5650614002693c54d716a354c48eb66b7f0028d37c7761c15e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWWXBRMN%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAkatMYF2o6RqoIM9VoJSx0kEgcnAt2R7qHkJoNwNlpbAiANxbRSESLwTZVHFap1Rodqer0k93b8rwREXkDe4k9PpSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMgdLH%2BtPYrfO2HnpCKtwDopaWAhKOYXvmAB1TIuebwaMJsGfCm04JtzmEw3BAFVkSP2xhl7nWPW3wns1bQvZPAAkSgVoo2PQJzcpYIeae2xjtqD1c6uzJbvWuquhvqZAL7RNnqYfVq5wJvwE9M7iy1LqSR%2BdCE%2B%2F9Mdj1BRUAXD%2B228F45zjA732cSQZJc8at%2BdGv4wnwFB3A15L8b%2BkfIK0Q1w4DBk24MeSLZBDXsS%2BxL2ueESs5NZ%2Fo%2FbOas%2BzZFxNyXixYXm1iVr6Dn%2FVZEr3r1vopNVNYYNO1u1uZ6UPbdUPbp4GDHwpcdPJ%2B4Pa2C%2BBWn7iujNKyZe56BR4WrdEYc5%2Fzp9KgJovLGlUbVahztFsmCDb8%2FH5XPFp%2BbatV5rATjPri9RPcOl9i62%2FqN1VqjKEyM8I23oxbIOxWZ22OsSQAZ6NhacyEPfM1G%2FF5flUGmFYO2qapVptS1SVmoytrt2v4Yxelw9PgERNnF1GQEUF9zfjo%2BRATTVBA2qkPe1WT3jXlkgxqtcoFcY7teybwHF5sYd9uVkidUxZFYiVND1CMT4OY%2BA7tvzdihWscP78%2BfaFWi7nQab44oVhImohDaks%2FXOph5mBezf3KiDxGpQo2l%2BIdHeLy%2FmnXKF0Prd1NC73qjUxFEl8wup7EzAY6pgFzG%2B59A6FImvVq49sboNGs7jrPsfaINTdTV7nmJsryHCDe1t4ZYhpvnnqAnQ3DTbk323MyYM6ICsyXPevMQJWzNiGXuF%2Bw7dZuf5rH7sLu2oCqJPkL7yx8t5Pg5VDGZzzqJwyBsU1pi9gtZUwESZ0%2BA52yvcIKKOFHn4vFkFv9JnpeV8psN71JS9PijN5UB%2BQEZslabpNjuwuLwdHYK6o3hMfCJJ4j&X-Amz-Signature=156a5c72b6724262d427c87c3c75af2ee3dc280d92fee3705be6bec621c11906&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



