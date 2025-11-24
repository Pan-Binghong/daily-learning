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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SIKMVFE%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5P4EJVC58mN6A%2F1spOS9d%2FoxORWj0GZD06nRfT5sCWAiEAvb%2FCEU6oU7NDYw7Phak0jr%2BXjKXQ0u0wpXxVgXds%2BZEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOGjF3ELjA%2FVFcsp%2FircAyJrYGAcC%2BntpxhZRlK66fXGOpwTyoVCvhrEkqlHpX6WZ3jaDsZnbwAe4j9hGd9bXmbnYyb7fVsRh90wndc3GUM2Wq7i7mu98ZtZCW7ekeQZ3Rpa4cOss9Dl0NskKDaUTXMxev0drmYA5NXR%2FvGF9dH6BB887s8Z9%2Fk9HiVEc6SqvXne5%2BcWvufNUL8daCXNEXtqijPcjFamkfkrVRL2h2gHySwRG30paJGNShMfui%2Bm%2FtBEXpR%2BjGpI7QudpZ5sB1bJY5y2szde00F1ZE6HZdEtJ31gC5NBprhoJ4Xje9locfjJkn7RlPhUnR8u3BEqgY45xBpPWMQuFy1oxzMVUvYACKl1K0scefd121NWueO9VFe1E0vmidTBPhpUKR4pqGwbHZu4zJiMKsdsJXvCo2eczkrrxzGGyTGXWITbjYuVvBuaG1p12fyOO3Ebwq4iref2ySm%2FaCbK%2F6JVsLG8ofNmyEeeGO0RwhIccc9atIFZe0u%2FrTp42kqnGfuXEwHg%2BnaW2%2BpeY6FKJsHGxvTDmOh%2BXovGA0K2yPfC13dfDMc%2BYPlCuPXPVxwjMZdeTt8Txq0ySQx%2FPXpNNb1jKxS4%2F5kMNNr%2BU0O4Mb9n6tXpm7wf4SQI8PhnXVMxxouHMPrbjskGOqUBO%2BxqBLrVJULiPmAWDJuUMYLV7wtLyV0TiKFUZM8hlv1ilrFv58ef8mVY8TP%2Boc1n33us8usi0HbNjS2clAd8%2FwfN51mYyu180akHJMbKJvYd5AT9XTwxqQV1J41iULajhcS37B%2FBDFALYTea%2B7zAkTPBeTQ3RLWdZB9MmT0O28cnKg0jC23LknZKkpoxYdGbUHlb1p6LJeSjAKy3dV%2FB8rnKiSDc&X-Amz-Signature=e536c01b7065433a9405ea4cc8dfade4b51c59a5e46f744ec1a8200bc62da121&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SIKMVFE%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5P4EJVC58mN6A%2F1spOS9d%2FoxORWj0GZD06nRfT5sCWAiEAvb%2FCEU6oU7NDYw7Phak0jr%2BXjKXQ0u0wpXxVgXds%2BZEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOGjF3ELjA%2FVFcsp%2FircAyJrYGAcC%2BntpxhZRlK66fXGOpwTyoVCvhrEkqlHpX6WZ3jaDsZnbwAe4j9hGd9bXmbnYyb7fVsRh90wndc3GUM2Wq7i7mu98ZtZCW7ekeQZ3Rpa4cOss9Dl0NskKDaUTXMxev0drmYA5NXR%2FvGF9dH6BB887s8Z9%2Fk9HiVEc6SqvXne5%2BcWvufNUL8daCXNEXtqijPcjFamkfkrVRL2h2gHySwRG30paJGNShMfui%2Bm%2FtBEXpR%2BjGpI7QudpZ5sB1bJY5y2szde00F1ZE6HZdEtJ31gC5NBprhoJ4Xje9locfjJkn7RlPhUnR8u3BEqgY45xBpPWMQuFy1oxzMVUvYACKl1K0scefd121NWueO9VFe1E0vmidTBPhpUKR4pqGwbHZu4zJiMKsdsJXvCo2eczkrrxzGGyTGXWITbjYuVvBuaG1p12fyOO3Ebwq4iref2ySm%2FaCbK%2F6JVsLG8ofNmyEeeGO0RwhIccc9atIFZe0u%2FrTp42kqnGfuXEwHg%2BnaW2%2BpeY6FKJsHGxvTDmOh%2BXovGA0K2yPfC13dfDMc%2BYPlCuPXPVxwjMZdeTt8Txq0ySQx%2FPXpNNb1jKxS4%2F5kMNNr%2BU0O4Mb9n6tXpm7wf4SQI8PhnXVMxxouHMPrbjskGOqUBO%2BxqBLrVJULiPmAWDJuUMYLV7wtLyV0TiKFUZM8hlv1ilrFv58ef8mVY8TP%2Boc1n33us8usi0HbNjS2clAd8%2FwfN51mYyu180akHJMbKJvYd5AT9XTwxqQV1J41iULajhcS37B%2FBDFALYTea%2B7zAkTPBeTQ3RLWdZB9MmT0O28cnKg0jC23LknZKkpoxYdGbUHlb1p6LJeSjAKy3dV%2FB8rnKiSDc&X-Amz-Signature=bb42d86bda76cf93efb1af34e5616c74185caceacea60ec8d9667e0f8275c859&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SIKMVFE%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5P4EJVC58mN6A%2F1spOS9d%2FoxORWj0GZD06nRfT5sCWAiEAvb%2FCEU6oU7NDYw7Phak0jr%2BXjKXQ0u0wpXxVgXds%2BZEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOGjF3ELjA%2FVFcsp%2FircAyJrYGAcC%2BntpxhZRlK66fXGOpwTyoVCvhrEkqlHpX6WZ3jaDsZnbwAe4j9hGd9bXmbnYyb7fVsRh90wndc3GUM2Wq7i7mu98ZtZCW7ekeQZ3Rpa4cOss9Dl0NskKDaUTXMxev0drmYA5NXR%2FvGF9dH6BB887s8Z9%2Fk9HiVEc6SqvXne5%2BcWvufNUL8daCXNEXtqijPcjFamkfkrVRL2h2gHySwRG30paJGNShMfui%2Bm%2FtBEXpR%2BjGpI7QudpZ5sB1bJY5y2szde00F1ZE6HZdEtJ31gC5NBprhoJ4Xje9locfjJkn7RlPhUnR8u3BEqgY45xBpPWMQuFy1oxzMVUvYACKl1K0scefd121NWueO9VFe1E0vmidTBPhpUKR4pqGwbHZu4zJiMKsdsJXvCo2eczkrrxzGGyTGXWITbjYuVvBuaG1p12fyOO3Ebwq4iref2ySm%2FaCbK%2F6JVsLG8ofNmyEeeGO0RwhIccc9atIFZe0u%2FrTp42kqnGfuXEwHg%2BnaW2%2BpeY6FKJsHGxvTDmOh%2BXovGA0K2yPfC13dfDMc%2BYPlCuPXPVxwjMZdeTt8Txq0ySQx%2FPXpNNb1jKxS4%2F5kMNNr%2BU0O4Mb9n6tXpm7wf4SQI8PhnXVMxxouHMPrbjskGOqUBO%2BxqBLrVJULiPmAWDJuUMYLV7wtLyV0TiKFUZM8hlv1ilrFv58ef8mVY8TP%2Boc1n33us8usi0HbNjS2clAd8%2FwfN51mYyu180akHJMbKJvYd5AT9XTwxqQV1J41iULajhcS37B%2FBDFALYTea%2B7zAkTPBeTQ3RLWdZB9MmT0O28cnKg0jC23LknZKkpoxYdGbUHlb1p6LJeSjAKy3dV%2FB8rnKiSDc&X-Amz-Signature=a34f8e20e562fbc30f69491cc0c5ad26ecd37422d9a1edfdfac76eaa7d52697b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SIKMVFE%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5P4EJVC58mN6A%2F1spOS9d%2FoxORWj0GZD06nRfT5sCWAiEAvb%2FCEU6oU7NDYw7Phak0jr%2BXjKXQ0u0wpXxVgXds%2BZEq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDOGjF3ELjA%2FVFcsp%2FircAyJrYGAcC%2BntpxhZRlK66fXGOpwTyoVCvhrEkqlHpX6WZ3jaDsZnbwAe4j9hGd9bXmbnYyb7fVsRh90wndc3GUM2Wq7i7mu98ZtZCW7ekeQZ3Rpa4cOss9Dl0NskKDaUTXMxev0drmYA5NXR%2FvGF9dH6BB887s8Z9%2Fk9HiVEc6SqvXne5%2BcWvufNUL8daCXNEXtqijPcjFamkfkrVRL2h2gHySwRG30paJGNShMfui%2Bm%2FtBEXpR%2BjGpI7QudpZ5sB1bJY5y2szde00F1ZE6HZdEtJ31gC5NBprhoJ4Xje9locfjJkn7RlPhUnR8u3BEqgY45xBpPWMQuFy1oxzMVUvYACKl1K0scefd121NWueO9VFe1E0vmidTBPhpUKR4pqGwbHZu4zJiMKsdsJXvCo2eczkrrxzGGyTGXWITbjYuVvBuaG1p12fyOO3Ebwq4iref2ySm%2FaCbK%2F6JVsLG8ofNmyEeeGO0RwhIccc9atIFZe0u%2FrTp42kqnGfuXEwHg%2BnaW2%2BpeY6FKJsHGxvTDmOh%2BXovGA0K2yPfC13dfDMc%2BYPlCuPXPVxwjMZdeTt8Txq0ySQx%2FPXpNNb1jKxS4%2F5kMNNr%2BU0O4Mb9n6tXpm7wf4SQI8PhnXVMxxouHMPrbjskGOqUBO%2BxqBLrVJULiPmAWDJuUMYLV7wtLyV0TiKFUZM8hlv1ilrFv58ef8mVY8TP%2Boc1n33us8usi0HbNjS2clAd8%2FwfN51mYyu180akHJMbKJvYd5AT9XTwxqQV1J41iULajhcS37B%2FBDFALYTea%2B7zAkTPBeTQ3RLWdZB9MmT0O28cnKg0jC23LknZKkpoxYdGbUHlb1p6LJeSjAKy3dV%2FB8rnKiSDc&X-Amz-Signature=c835166e70098daa18ce6ee378875a1cbcf2307f78c476470548325fdcacc9f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



