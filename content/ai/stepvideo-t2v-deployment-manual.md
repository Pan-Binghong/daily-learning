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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGC3B74C%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaAd2iL7RL%2BUEsi20Ws0g1UskowVJhhcRsrBAZokoSbAiEAxL06hEjiKCOQhxKkI%2BUzKpTJimA1lu8AQWYty27DnOgqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjbH2m5VKgj47FsHSrcA6w%2BwaLq%2FtUEPB%2BhA7CcEEeNeXig0bPqaFaJciispaMULQJv9ypkrr8MQblngKPB%2FiKpB%2B9zO6hh%2FhEYi4KY0ettm4%2BTUPO1ltMFMpKtYy0CsTL3aaNl8XG34HAJXZdjvd7JQ%2BsxKKFhwlccy6ap7OLBmzZN5Z4YaOk408DRUz1bN2w5Gm7WnLEAj6P4beFdLXpSQREP3PHus2%2BMIntsevVL9tI9GJpzqnychnTOxhT4yRUBheb15RLbR%2FqsuoasrfUbEcLr0VspbXtgUNGOwLgaFShObt4UV2Edwmt5hETuxY5gz8%2FtnvWOI21DCEZx89y2g2KUSVHdvfnCmEyPiCJvQe5JQckgstuzMG%2FaiGkYoofxHX8z6uX698FtdhB8WQVB7lHXwdaLF62IlZag2%2BDXGBUvfKURE1xmGKJZ%2BztG9M341x%2FoNTnHRytLT4HFGCAwbTn7NmVAaqYSAOnl54XO%2BOiDb0arewGFAqvkm6xK5MRV8RzvVNn9usFpgF1IM%2BVznsKtln0Ewgeebr4WU%2FwWJyQ0NKjaKnmaZLBm0wjiw2Y%2FCTUegTgNmotSX2DdaBcUZtULTFloQw3zVXF25UXuYwDn2hmJ69m2lPRvqFVEfp%2BASRyUMzUi%2B5L8MJXv2MkGOqUBhdCIEyhxBDSWyGXuFymGgyzyaG4Zatb1gfwoaI7gmmJAElqPUKpwjwKJ8F%2BPMjNg%2B5y8iUB6OY810dzqdioq1R6gMVwgsRpMgFYBTOKkyjn5uI6SukZy3biS90jNqrTZwucQslcyCZ3pX2JgVYSFdPPq8%2FU6Y7rVFFYKfT%2FZvpgGIhD5HACbg8Fc818tIAJKhvZfP22%2FfG0PT9velGkPDKFQXtJN&X-Amz-Signature=9313afdb1567444a8da016ede1cb4191100a0315409dcb7eba96430066580e38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGC3B74C%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaAd2iL7RL%2BUEsi20Ws0g1UskowVJhhcRsrBAZokoSbAiEAxL06hEjiKCOQhxKkI%2BUzKpTJimA1lu8AQWYty27DnOgqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjbH2m5VKgj47FsHSrcA6w%2BwaLq%2FtUEPB%2BhA7CcEEeNeXig0bPqaFaJciispaMULQJv9ypkrr8MQblngKPB%2FiKpB%2B9zO6hh%2FhEYi4KY0ettm4%2BTUPO1ltMFMpKtYy0CsTL3aaNl8XG34HAJXZdjvd7JQ%2BsxKKFhwlccy6ap7OLBmzZN5Z4YaOk408DRUz1bN2w5Gm7WnLEAj6P4beFdLXpSQREP3PHus2%2BMIntsevVL9tI9GJpzqnychnTOxhT4yRUBheb15RLbR%2FqsuoasrfUbEcLr0VspbXtgUNGOwLgaFShObt4UV2Edwmt5hETuxY5gz8%2FtnvWOI21DCEZx89y2g2KUSVHdvfnCmEyPiCJvQe5JQckgstuzMG%2FaiGkYoofxHX8z6uX698FtdhB8WQVB7lHXwdaLF62IlZag2%2BDXGBUvfKURE1xmGKJZ%2BztG9M341x%2FoNTnHRytLT4HFGCAwbTn7NmVAaqYSAOnl54XO%2BOiDb0arewGFAqvkm6xK5MRV8RzvVNn9usFpgF1IM%2BVznsKtln0Ewgeebr4WU%2FwWJyQ0NKjaKnmaZLBm0wjiw2Y%2FCTUegTgNmotSX2DdaBcUZtULTFloQw3zVXF25UXuYwDn2hmJ69m2lPRvqFVEfp%2BASRyUMzUi%2B5L8MJXv2MkGOqUBhdCIEyhxBDSWyGXuFymGgyzyaG4Zatb1gfwoaI7gmmJAElqPUKpwjwKJ8F%2BPMjNg%2B5y8iUB6OY810dzqdioq1R6gMVwgsRpMgFYBTOKkyjn5uI6SukZy3biS90jNqrTZwucQslcyCZ3pX2JgVYSFdPPq8%2FU6Y7rVFFYKfT%2FZvpgGIhD5HACbg8Fc818tIAJKhvZfP22%2FfG0PT9velGkPDKFQXtJN&X-Amz-Signature=1ab0195069931db779ec2cbf062bca4513b6719b1410aa99a03abb628b061539&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGC3B74C%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaAd2iL7RL%2BUEsi20Ws0g1UskowVJhhcRsrBAZokoSbAiEAxL06hEjiKCOQhxKkI%2BUzKpTJimA1lu8AQWYty27DnOgqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjbH2m5VKgj47FsHSrcA6w%2BwaLq%2FtUEPB%2BhA7CcEEeNeXig0bPqaFaJciispaMULQJv9ypkrr8MQblngKPB%2FiKpB%2B9zO6hh%2FhEYi4KY0ettm4%2BTUPO1ltMFMpKtYy0CsTL3aaNl8XG34HAJXZdjvd7JQ%2BsxKKFhwlccy6ap7OLBmzZN5Z4YaOk408DRUz1bN2w5Gm7WnLEAj6P4beFdLXpSQREP3PHus2%2BMIntsevVL9tI9GJpzqnychnTOxhT4yRUBheb15RLbR%2FqsuoasrfUbEcLr0VspbXtgUNGOwLgaFShObt4UV2Edwmt5hETuxY5gz8%2FtnvWOI21DCEZx89y2g2KUSVHdvfnCmEyPiCJvQe5JQckgstuzMG%2FaiGkYoofxHX8z6uX698FtdhB8WQVB7lHXwdaLF62IlZag2%2BDXGBUvfKURE1xmGKJZ%2BztG9M341x%2FoNTnHRytLT4HFGCAwbTn7NmVAaqYSAOnl54XO%2BOiDb0arewGFAqvkm6xK5MRV8RzvVNn9usFpgF1IM%2BVznsKtln0Ewgeebr4WU%2FwWJyQ0NKjaKnmaZLBm0wjiw2Y%2FCTUegTgNmotSX2DdaBcUZtULTFloQw3zVXF25UXuYwDn2hmJ69m2lPRvqFVEfp%2BASRyUMzUi%2B5L8MJXv2MkGOqUBhdCIEyhxBDSWyGXuFymGgyzyaG4Zatb1gfwoaI7gmmJAElqPUKpwjwKJ8F%2BPMjNg%2B5y8iUB6OY810dzqdioq1R6gMVwgsRpMgFYBTOKkyjn5uI6SukZy3biS90jNqrTZwucQslcyCZ3pX2JgVYSFdPPq8%2FU6Y7rVFFYKfT%2FZvpgGIhD5HACbg8Fc818tIAJKhvZfP22%2FfG0PT9velGkPDKFQXtJN&X-Amz-Signature=bcbdb1c07beb213986593692cd3b500929f69a837072e6ab2e2ba50ba699925b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGC3B74C%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaAd2iL7RL%2BUEsi20Ws0g1UskowVJhhcRsrBAZokoSbAiEAxL06hEjiKCOQhxKkI%2BUzKpTJimA1lu8AQWYty27DnOgqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjbH2m5VKgj47FsHSrcA6w%2BwaLq%2FtUEPB%2BhA7CcEEeNeXig0bPqaFaJciispaMULQJv9ypkrr8MQblngKPB%2FiKpB%2B9zO6hh%2FhEYi4KY0ettm4%2BTUPO1ltMFMpKtYy0CsTL3aaNl8XG34HAJXZdjvd7JQ%2BsxKKFhwlccy6ap7OLBmzZN5Z4YaOk408DRUz1bN2w5Gm7WnLEAj6P4beFdLXpSQREP3PHus2%2BMIntsevVL9tI9GJpzqnychnTOxhT4yRUBheb15RLbR%2FqsuoasrfUbEcLr0VspbXtgUNGOwLgaFShObt4UV2Edwmt5hETuxY5gz8%2FtnvWOI21DCEZx89y2g2KUSVHdvfnCmEyPiCJvQe5JQckgstuzMG%2FaiGkYoofxHX8z6uX698FtdhB8WQVB7lHXwdaLF62IlZag2%2BDXGBUvfKURE1xmGKJZ%2BztG9M341x%2FoNTnHRytLT4HFGCAwbTn7NmVAaqYSAOnl54XO%2BOiDb0arewGFAqvkm6xK5MRV8RzvVNn9usFpgF1IM%2BVznsKtln0Ewgeebr4WU%2FwWJyQ0NKjaKnmaZLBm0wjiw2Y%2FCTUegTgNmotSX2DdaBcUZtULTFloQw3zVXF25UXuYwDn2hmJ69m2lPRvqFVEfp%2BASRyUMzUi%2B5L8MJXv2MkGOqUBhdCIEyhxBDSWyGXuFymGgyzyaG4Zatb1gfwoaI7gmmJAElqPUKpwjwKJ8F%2BPMjNg%2B5y8iUB6OY810dzqdioq1R6gMVwgsRpMgFYBTOKkyjn5uI6SukZy3biS90jNqrTZwucQslcyCZ3pX2JgVYSFdPPq8%2FU6Y7rVFFYKfT%2FZvpgGIhD5HACbg8Fc818tIAJKhvZfP22%2FfG0PT9velGkPDKFQXtJN&X-Amz-Signature=2848c06be20c699be2d6b917ac5de37dcb371ba879ef6a7645b84420465a9fd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



