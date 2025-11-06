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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DWRIPSA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPj%2BK3K6Ea4q0vSoffO1F5AaKB2MZS6calXgozErLxtwIgbd5Ap7y2h1Wv3EjMiUYTOaJBbeFHRHzdqGTLHuwSKZMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVHuMIAeybfq0ktNSrcA8Vf3M%2FaGu4s1XTG%2BJwQbAgjrt3JS25gcZ1t9HHA09KW5P5jBFJdKE%2BSKIGXUQ2UfILkZLmJ9FX%2BtdC2QZiG6MSHRB4PzoyGBoWwemtTO6RdZD0gJVgGC98hU1k1WZaoJ4smfEIxOdWuEf0BqKqpaXQKPdOlRnyaid%2BmzB18YMpNLvR8TQYBMwfgy0p2%2BUjfLyReM1zy47x%2FEcV0EyraE3QNQo0mvAqBbWQCEGfsDr6FE8Yhk2rGwOPtrLqyrngNoxn37JFk7HBO5esXSXtwpsLz%2FC3CTjZfOlFLVldrTaYedJRVjmvQKu%2BjEGVprtXpk%2BuqxX4dwpbjWx4X3xSOo1tUkmqvU6BOJLnbs9uNtgBdYcCnw%2FCNCxU9ZsFlieBjpBvCm6DSMtXb5%2BIl5RcylVYJ19sCEwQRa7a50KoNfh9AQSPdCtqYar8chCBglX1UJKmPkXz2D6ibcbPjCQ534D5kURK3r%2B2RsBzK7MOkk%2FbWNPNFBrvW6o3%2BETKWdJR%2F4FVh14DEwhbhcmN9D9KBDPGwaedVy%2B9HvUCDylCfi0qLE%2FO8L7ITklbXlDnQN6NrYK6pwZBg2QeqrndxpKzZHfOB7AETAIOyg2fM6rB1WQwEB4ARJZu4BSHZrvVuML3yr8gGOqUBIEFB3aRGYg2aMC2szdmVAMFwolzxYBrVwr9rtfaU9kkdF9SrCvFbzHg4SJg%2FD3Tsf1WPRu8k%2BxwJL%2B28WhQFz38fUfOL9JKx7xikMIIoff3GXd3HdcMa1WGScB7JOscEoThzN%2F0kQZjojDyOZceQwz6uT%2BEEL5g2%2Fy8jxnrlG%2BLDTHuKHP0cIdT%2BmDSNh5WG%2BlgoK5Kf%2BQCZ%2Bgmq24mQCuE6zwTC&X-Amz-Signature=4adc7700b1e44ac2026dd098a895c8914f625013884d10351eeb3f42587e5e7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DWRIPSA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPj%2BK3K6Ea4q0vSoffO1F5AaKB2MZS6calXgozErLxtwIgbd5Ap7y2h1Wv3EjMiUYTOaJBbeFHRHzdqGTLHuwSKZMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVHuMIAeybfq0ktNSrcA8Vf3M%2FaGu4s1XTG%2BJwQbAgjrt3JS25gcZ1t9HHA09KW5P5jBFJdKE%2BSKIGXUQ2UfILkZLmJ9FX%2BtdC2QZiG6MSHRB4PzoyGBoWwemtTO6RdZD0gJVgGC98hU1k1WZaoJ4smfEIxOdWuEf0BqKqpaXQKPdOlRnyaid%2BmzB18YMpNLvR8TQYBMwfgy0p2%2BUjfLyReM1zy47x%2FEcV0EyraE3QNQo0mvAqBbWQCEGfsDr6FE8Yhk2rGwOPtrLqyrngNoxn37JFk7HBO5esXSXtwpsLz%2FC3CTjZfOlFLVldrTaYedJRVjmvQKu%2BjEGVprtXpk%2BuqxX4dwpbjWx4X3xSOo1tUkmqvU6BOJLnbs9uNtgBdYcCnw%2FCNCxU9ZsFlieBjpBvCm6DSMtXb5%2BIl5RcylVYJ19sCEwQRa7a50KoNfh9AQSPdCtqYar8chCBglX1UJKmPkXz2D6ibcbPjCQ534D5kURK3r%2B2RsBzK7MOkk%2FbWNPNFBrvW6o3%2BETKWdJR%2F4FVh14DEwhbhcmN9D9KBDPGwaedVy%2B9HvUCDylCfi0qLE%2FO8L7ITklbXlDnQN6NrYK6pwZBg2QeqrndxpKzZHfOB7AETAIOyg2fM6rB1WQwEB4ARJZu4BSHZrvVuML3yr8gGOqUBIEFB3aRGYg2aMC2szdmVAMFwolzxYBrVwr9rtfaU9kkdF9SrCvFbzHg4SJg%2FD3Tsf1WPRu8k%2BxwJL%2B28WhQFz38fUfOL9JKx7xikMIIoff3GXd3HdcMa1WGScB7JOscEoThzN%2F0kQZjojDyOZceQwz6uT%2BEEL5g2%2Fy8jxnrlG%2BLDTHuKHP0cIdT%2BmDSNh5WG%2BlgoK5Kf%2BQCZ%2Bgmq24mQCuE6zwTC&X-Amz-Signature=02ac9c38e31c9b9d84647296e997d3c91e13e666989a5c2ade2a4e913a423f62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DWRIPSA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPj%2BK3K6Ea4q0vSoffO1F5AaKB2MZS6calXgozErLxtwIgbd5Ap7y2h1Wv3EjMiUYTOaJBbeFHRHzdqGTLHuwSKZMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVHuMIAeybfq0ktNSrcA8Vf3M%2FaGu4s1XTG%2BJwQbAgjrt3JS25gcZ1t9HHA09KW5P5jBFJdKE%2BSKIGXUQ2UfILkZLmJ9FX%2BtdC2QZiG6MSHRB4PzoyGBoWwemtTO6RdZD0gJVgGC98hU1k1WZaoJ4smfEIxOdWuEf0BqKqpaXQKPdOlRnyaid%2BmzB18YMpNLvR8TQYBMwfgy0p2%2BUjfLyReM1zy47x%2FEcV0EyraE3QNQo0mvAqBbWQCEGfsDr6FE8Yhk2rGwOPtrLqyrngNoxn37JFk7HBO5esXSXtwpsLz%2FC3CTjZfOlFLVldrTaYedJRVjmvQKu%2BjEGVprtXpk%2BuqxX4dwpbjWx4X3xSOo1tUkmqvU6BOJLnbs9uNtgBdYcCnw%2FCNCxU9ZsFlieBjpBvCm6DSMtXb5%2BIl5RcylVYJ19sCEwQRa7a50KoNfh9AQSPdCtqYar8chCBglX1UJKmPkXz2D6ibcbPjCQ534D5kURK3r%2B2RsBzK7MOkk%2FbWNPNFBrvW6o3%2BETKWdJR%2F4FVh14DEwhbhcmN9D9KBDPGwaedVy%2B9HvUCDylCfi0qLE%2FO8L7ITklbXlDnQN6NrYK6pwZBg2QeqrndxpKzZHfOB7AETAIOyg2fM6rB1WQwEB4ARJZu4BSHZrvVuML3yr8gGOqUBIEFB3aRGYg2aMC2szdmVAMFwolzxYBrVwr9rtfaU9kkdF9SrCvFbzHg4SJg%2FD3Tsf1WPRu8k%2BxwJL%2B28WhQFz38fUfOL9JKx7xikMIIoff3GXd3HdcMa1WGScB7JOscEoThzN%2F0kQZjojDyOZceQwz6uT%2BEEL5g2%2Fy8jxnrlG%2BLDTHuKHP0cIdT%2BmDSNh5WG%2BlgoK5Kf%2BQCZ%2Bgmq24mQCuE6zwTC&X-Amz-Signature=bb1c8e7ed2f3fb718a802fad33a488adb01610b6fefb69c263bc521b7ec69655&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DWRIPSA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPj%2BK3K6Ea4q0vSoffO1F5AaKB2MZS6calXgozErLxtwIgbd5Ap7y2h1Wv3EjMiUYTOaJBbeFHRHzdqGTLHuwSKZMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPVHuMIAeybfq0ktNSrcA8Vf3M%2FaGu4s1XTG%2BJwQbAgjrt3JS25gcZ1t9HHA09KW5P5jBFJdKE%2BSKIGXUQ2UfILkZLmJ9FX%2BtdC2QZiG6MSHRB4PzoyGBoWwemtTO6RdZD0gJVgGC98hU1k1WZaoJ4smfEIxOdWuEf0BqKqpaXQKPdOlRnyaid%2BmzB18YMpNLvR8TQYBMwfgy0p2%2BUjfLyReM1zy47x%2FEcV0EyraE3QNQo0mvAqBbWQCEGfsDr6FE8Yhk2rGwOPtrLqyrngNoxn37JFk7HBO5esXSXtwpsLz%2FC3CTjZfOlFLVldrTaYedJRVjmvQKu%2BjEGVprtXpk%2BuqxX4dwpbjWx4X3xSOo1tUkmqvU6BOJLnbs9uNtgBdYcCnw%2FCNCxU9ZsFlieBjpBvCm6DSMtXb5%2BIl5RcylVYJ19sCEwQRa7a50KoNfh9AQSPdCtqYar8chCBglX1UJKmPkXz2D6ibcbPjCQ534D5kURK3r%2B2RsBzK7MOkk%2FbWNPNFBrvW6o3%2BETKWdJR%2F4FVh14DEwhbhcmN9D9KBDPGwaedVy%2B9HvUCDylCfi0qLE%2FO8L7ITklbXlDnQN6NrYK6pwZBg2QeqrndxpKzZHfOB7AETAIOyg2fM6rB1WQwEB4ARJZu4BSHZrvVuML3yr8gGOqUBIEFB3aRGYg2aMC2szdmVAMFwolzxYBrVwr9rtfaU9kkdF9SrCvFbzHg4SJg%2FD3Tsf1WPRu8k%2BxwJL%2B28WhQFz38fUfOL9JKx7xikMIIoff3GXd3HdcMa1WGScB7JOscEoThzN%2F0kQZjojDyOZceQwz6uT%2BEEL5g2%2Fy8jxnrlG%2BLDTHuKHP0cIdT%2BmDSNh5WG%2BlgoK5Kf%2BQCZ%2Bgmq24mQCuE6zwTC&X-Amz-Signature=2ed5f17fcf98682af5791e1cc0c68062c17b05fcbd2d0a1b674d9ac45d24f8fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



