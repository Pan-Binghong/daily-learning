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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJZ3ZJPO%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF9ZYD174r%2FrbJkkNClTy07mKzk2WScezGWcD5tBQ5%2FgIgfmzogPRoxp%2BGExIm32FTUF2WTpZiAwfGNidEuO3XLa4qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZXUohoMdeZzbQaLircAxAZVFtUthRQI0vYTXP0PW8Z3C1uh7Laaq80EVjdvgKaXpF2%2BhmXXOxNnfalgRB0Df9KS5poal4hOeuHqHxuujy0tGewSZ2SMKqHkGAtgO1fB0IhUmvV0KzrYC%2F80ZWA%2F41JS%2B1IiKDmt%2BMPmlKXKQdeX%2BQiLSqr93b2%2BDL%2F2V0t5zCwptIqILMK71CmQ8PZdNRKwz%2BQTsbL6Y3LNCkaYcYjQ79maP1EBXaeK3aQiYVYKNB95CfgpvgxEVJQd521EGAvj9o7po%2Bmn53wmYptbgx9uUweE1rNgb%2FfeAQYVmP5UcvZKXMY3Xzp7M7VkbMOkVfZ828w2pPDK7cDog2PCdcRmfNCfsd465FeEiKjNzlqaV0%2F0PmIjCRRGnuWza27zPJDrim%2B4aOTDb%2FHgKc%2BAsaT68ySdFjUpg3EMM0CWlu02K%2BsoG%2F9FEoaaaab2Q1ZunLYGRnDixTdwBPIANxbZz%2FEsDHLADJwsVSRFWawX6sezRUrCQ6vWXMWbTiAJVPYn8RXj02%2BX1sqeean1L7HXK3GgTLPEZyO6x2XqVN1kQ3EN3xPFqpZhaPVSzoohRXEcpf6zsp%2FFmogrt0S0XbAUBDX%2BkxNweXlpB%2BAfePSQijaeVPgo6kP66hE46FPMMWPqckGOqUBFjK6uDkI7316ND5AKtx8XjEGA0dF6HfSgKZaztFjkvgfSDBjjatgVSrGezscCLekH%2BuC%2F2P8Cg3tUo%2FfXTWfy1VdUBQBQR8qNhHCKbzUAQAKrB4D61Q0qja4E5CrqWNBer70SMCJubr6MAfFP8dB1L3Tuz72UP2JMTk%2Flkl9I9t1UCXR3xydivqP1yinavn1Eo5Pj%2Fe396p3d26jDXrFhD459UoL&X-Amz-Signature=8ff368ea1e6f27f0cd873c4c9bd9b4829cbc6ce17ce6c9e703df2a820c8ed23a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJZ3ZJPO%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF9ZYD174r%2FrbJkkNClTy07mKzk2WScezGWcD5tBQ5%2FgIgfmzogPRoxp%2BGExIm32FTUF2WTpZiAwfGNidEuO3XLa4qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZXUohoMdeZzbQaLircAxAZVFtUthRQI0vYTXP0PW8Z3C1uh7Laaq80EVjdvgKaXpF2%2BhmXXOxNnfalgRB0Df9KS5poal4hOeuHqHxuujy0tGewSZ2SMKqHkGAtgO1fB0IhUmvV0KzrYC%2F80ZWA%2F41JS%2B1IiKDmt%2BMPmlKXKQdeX%2BQiLSqr93b2%2BDL%2F2V0t5zCwptIqILMK71CmQ8PZdNRKwz%2BQTsbL6Y3LNCkaYcYjQ79maP1EBXaeK3aQiYVYKNB95CfgpvgxEVJQd521EGAvj9o7po%2Bmn53wmYptbgx9uUweE1rNgb%2FfeAQYVmP5UcvZKXMY3Xzp7M7VkbMOkVfZ828w2pPDK7cDog2PCdcRmfNCfsd465FeEiKjNzlqaV0%2F0PmIjCRRGnuWza27zPJDrim%2B4aOTDb%2FHgKc%2BAsaT68ySdFjUpg3EMM0CWlu02K%2BsoG%2F9FEoaaaab2Q1ZunLYGRnDixTdwBPIANxbZz%2FEsDHLADJwsVSRFWawX6sezRUrCQ6vWXMWbTiAJVPYn8RXj02%2BX1sqeean1L7HXK3GgTLPEZyO6x2XqVN1kQ3EN3xPFqpZhaPVSzoohRXEcpf6zsp%2FFmogrt0S0XbAUBDX%2BkxNweXlpB%2BAfePSQijaeVPgo6kP66hE46FPMMWPqckGOqUBFjK6uDkI7316ND5AKtx8XjEGA0dF6HfSgKZaztFjkvgfSDBjjatgVSrGezscCLekH%2BuC%2F2P8Cg3tUo%2FfXTWfy1VdUBQBQR8qNhHCKbzUAQAKrB4D61Q0qja4E5CrqWNBer70SMCJubr6MAfFP8dB1L3Tuz72UP2JMTk%2Flkl9I9t1UCXR3xydivqP1yinavn1Eo5Pj%2Fe396p3d26jDXrFhD459UoL&X-Amz-Signature=97a482ea7958cc51845fae9ddfeb8d75801339a397d1c492c9a8899dcea49d8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJZ3ZJPO%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF9ZYD174r%2FrbJkkNClTy07mKzk2WScezGWcD5tBQ5%2FgIgfmzogPRoxp%2BGExIm32FTUF2WTpZiAwfGNidEuO3XLa4qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZXUohoMdeZzbQaLircAxAZVFtUthRQI0vYTXP0PW8Z3C1uh7Laaq80EVjdvgKaXpF2%2BhmXXOxNnfalgRB0Df9KS5poal4hOeuHqHxuujy0tGewSZ2SMKqHkGAtgO1fB0IhUmvV0KzrYC%2F80ZWA%2F41JS%2B1IiKDmt%2BMPmlKXKQdeX%2BQiLSqr93b2%2BDL%2F2V0t5zCwptIqILMK71CmQ8PZdNRKwz%2BQTsbL6Y3LNCkaYcYjQ79maP1EBXaeK3aQiYVYKNB95CfgpvgxEVJQd521EGAvj9o7po%2Bmn53wmYptbgx9uUweE1rNgb%2FfeAQYVmP5UcvZKXMY3Xzp7M7VkbMOkVfZ828w2pPDK7cDog2PCdcRmfNCfsd465FeEiKjNzlqaV0%2F0PmIjCRRGnuWza27zPJDrim%2B4aOTDb%2FHgKc%2BAsaT68ySdFjUpg3EMM0CWlu02K%2BsoG%2F9FEoaaaab2Q1ZunLYGRnDixTdwBPIANxbZz%2FEsDHLADJwsVSRFWawX6sezRUrCQ6vWXMWbTiAJVPYn8RXj02%2BX1sqeean1L7HXK3GgTLPEZyO6x2XqVN1kQ3EN3xPFqpZhaPVSzoohRXEcpf6zsp%2FFmogrt0S0XbAUBDX%2BkxNweXlpB%2BAfePSQijaeVPgo6kP66hE46FPMMWPqckGOqUBFjK6uDkI7316ND5AKtx8XjEGA0dF6HfSgKZaztFjkvgfSDBjjatgVSrGezscCLekH%2BuC%2F2P8Cg3tUo%2FfXTWfy1VdUBQBQR8qNhHCKbzUAQAKrB4D61Q0qja4E5CrqWNBer70SMCJubr6MAfFP8dB1L3Tuz72UP2JMTk%2Flkl9I9t1UCXR3xydivqP1yinavn1Eo5Pj%2Fe396p3d26jDXrFhD459UoL&X-Amz-Signature=e14005fab5af251f788912f233cb589433e0aad9dc44994a07ec12dcec2cdefc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJZ3ZJPO%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF9ZYD174r%2FrbJkkNClTy07mKzk2WScezGWcD5tBQ5%2FgIgfmzogPRoxp%2BGExIm32FTUF2WTpZiAwfGNidEuO3XLa4qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZXUohoMdeZzbQaLircAxAZVFtUthRQI0vYTXP0PW8Z3C1uh7Laaq80EVjdvgKaXpF2%2BhmXXOxNnfalgRB0Df9KS5poal4hOeuHqHxuujy0tGewSZ2SMKqHkGAtgO1fB0IhUmvV0KzrYC%2F80ZWA%2F41JS%2B1IiKDmt%2BMPmlKXKQdeX%2BQiLSqr93b2%2BDL%2F2V0t5zCwptIqILMK71CmQ8PZdNRKwz%2BQTsbL6Y3LNCkaYcYjQ79maP1EBXaeK3aQiYVYKNB95CfgpvgxEVJQd521EGAvj9o7po%2Bmn53wmYptbgx9uUweE1rNgb%2FfeAQYVmP5UcvZKXMY3Xzp7M7VkbMOkVfZ828w2pPDK7cDog2PCdcRmfNCfsd465FeEiKjNzlqaV0%2F0PmIjCRRGnuWza27zPJDrim%2B4aOTDb%2FHgKc%2BAsaT68ySdFjUpg3EMM0CWlu02K%2BsoG%2F9FEoaaaab2Q1ZunLYGRnDixTdwBPIANxbZz%2FEsDHLADJwsVSRFWawX6sezRUrCQ6vWXMWbTiAJVPYn8RXj02%2BX1sqeean1L7HXK3GgTLPEZyO6x2XqVN1kQ3EN3xPFqpZhaPVSzoohRXEcpf6zsp%2FFmogrt0S0XbAUBDX%2BkxNweXlpB%2BAfePSQijaeVPgo6kP66hE46FPMMWPqckGOqUBFjK6uDkI7316ND5AKtx8XjEGA0dF6HfSgKZaztFjkvgfSDBjjatgVSrGezscCLekH%2BuC%2F2P8Cg3tUo%2FfXTWfy1VdUBQBQR8qNhHCKbzUAQAKrB4D61Q0qja4E5CrqWNBer70SMCJubr6MAfFP8dB1L3Tuz72UP2JMTk%2Flkl9I9t1UCXR3xydivqP1yinavn1Eo5Pj%2Fe396p3d26jDXrFhD459UoL&X-Amz-Signature=e9b559284655dee2e2f822e7a81c03aba1615cda67ee66a11735d6ecf1cd0884&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



