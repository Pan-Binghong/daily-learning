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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZINICM%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQzZ%2BsLe5TccF9eArdqg9E3I41vUxFpWmPjIou8p5LhAiBJp%2F4vybpMMOvccTuf4osyvLhtRn9etA8vzCw1HBnYrCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8FF%2FeDZ6iH1kRVbcKtwD2OEx09Xq63C%2BuV4ZqG%2BwNMhIDsb%2F%2BJ%2FMCR1BMIDB%2BhDOPpUp%2F9zJY6Cq24n%2BkCuyByz2PMXR1P%2BCTpvLxZ81OLG0b0qR5kS2QEcM077KMAKkWVOqPf4myaHf3I%2BCT7ngNxhegiOc4FW6DiR9KJEuoB0LpGdUK8amVOaxYHFQZTyCCFC1UFSneV615S96fozSt1esRkH2nromv%2Fc5bw4mMbYkkwjhSxCAcsFNk100LSDiYN9lkUhYM%2FN0%2B4Mn1UpqTna%2F0ycT6vJFFoMW0hp1Vd0oaRD3dzvXlmq8t%2B1p259sORZuQMED7MReeJ90tG3sVyeWHUwyujFCYW9aZGhKNdTQy%2Bqstch2HtTHM%2BeHPYd8YLtHS8kOrqREXy%2FaU3KhxB%2F80c6Wvkm75Z1nMMWzP25IEZeiB1T1wi1ww6Df7D9rSo9%2F1dlqgsVsuz47K12UsqzWIj1ISkNIvyzolSGKBYzuHfvR0ee20ZrSXCpagcMM%2BAhFfUoB%2BhwxeHWI%2BdQBEY7KN0EqkOcEly%2FqwTclb9sA%2FR%2F3WOW%2FfyPokS1uSXcsSlYNYuCBhWiOHcso9pxPb5ZSkk%2BbwzU%2BJIB3NTyeqjM3TSjrn84hb53Z07sbsNEzqztl0abiI2ifRIcwgbaYzQY6pgE240QNkt4M%2Bzpk3IUZOpiH2DwEHMgCdH%2FhTzx4LDUWoNr9%2F2l%2Fx49TtwuC9DBCTZ7v7AsNyF3RTGniPFfwAbAEzSMkUJKvIOk%2F6mAnMbkUwQayVN2HEU%2BgFLlYPzMiPOxBpJKRybyn4R3MS%2F6%2F5MSVitycMt0ABrN1sVq7ycDCFHB9esVPCg6qROzfpem6FDyXLVUtar%2FASo6cjnpzm18IVp5CxaJT&X-Amz-Signature=4f93c10656a9d5c86dc7e8613001e0187f93e9068e3e8186b0893e3bb893c207&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZINICM%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQzZ%2BsLe5TccF9eArdqg9E3I41vUxFpWmPjIou8p5LhAiBJp%2F4vybpMMOvccTuf4osyvLhtRn9etA8vzCw1HBnYrCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8FF%2FeDZ6iH1kRVbcKtwD2OEx09Xq63C%2BuV4ZqG%2BwNMhIDsb%2F%2BJ%2FMCR1BMIDB%2BhDOPpUp%2F9zJY6Cq24n%2BkCuyByz2PMXR1P%2BCTpvLxZ81OLG0b0qR5kS2QEcM077KMAKkWVOqPf4myaHf3I%2BCT7ngNxhegiOc4FW6DiR9KJEuoB0LpGdUK8amVOaxYHFQZTyCCFC1UFSneV615S96fozSt1esRkH2nromv%2Fc5bw4mMbYkkwjhSxCAcsFNk100LSDiYN9lkUhYM%2FN0%2B4Mn1UpqTna%2F0ycT6vJFFoMW0hp1Vd0oaRD3dzvXlmq8t%2B1p259sORZuQMED7MReeJ90tG3sVyeWHUwyujFCYW9aZGhKNdTQy%2Bqstch2HtTHM%2BeHPYd8YLtHS8kOrqREXy%2FaU3KhxB%2F80c6Wvkm75Z1nMMWzP25IEZeiB1T1wi1ww6Df7D9rSo9%2F1dlqgsVsuz47K12UsqzWIj1ISkNIvyzolSGKBYzuHfvR0ee20ZrSXCpagcMM%2BAhFfUoB%2BhwxeHWI%2BdQBEY7KN0EqkOcEly%2FqwTclb9sA%2FR%2F3WOW%2FfyPokS1uSXcsSlYNYuCBhWiOHcso9pxPb5ZSkk%2BbwzU%2BJIB3NTyeqjM3TSjrn84hb53Z07sbsNEzqztl0abiI2ifRIcwgbaYzQY6pgE240QNkt4M%2Bzpk3IUZOpiH2DwEHMgCdH%2FhTzx4LDUWoNr9%2F2l%2Fx49TtwuC9DBCTZ7v7AsNyF3RTGniPFfwAbAEzSMkUJKvIOk%2F6mAnMbkUwQayVN2HEU%2BgFLlYPzMiPOxBpJKRybyn4R3MS%2F6%2F5MSVitycMt0ABrN1sVq7ycDCFHB9esVPCg6qROzfpem6FDyXLVUtar%2FASo6cjnpzm18IVp5CxaJT&X-Amz-Signature=dd532ad0186c6ca6f340aad9c94a2f4e57599716aa68d2c26eb5790cd2729749&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZINICM%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQzZ%2BsLe5TccF9eArdqg9E3I41vUxFpWmPjIou8p5LhAiBJp%2F4vybpMMOvccTuf4osyvLhtRn9etA8vzCw1HBnYrCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8FF%2FeDZ6iH1kRVbcKtwD2OEx09Xq63C%2BuV4ZqG%2BwNMhIDsb%2F%2BJ%2FMCR1BMIDB%2BhDOPpUp%2F9zJY6Cq24n%2BkCuyByz2PMXR1P%2BCTpvLxZ81OLG0b0qR5kS2QEcM077KMAKkWVOqPf4myaHf3I%2BCT7ngNxhegiOc4FW6DiR9KJEuoB0LpGdUK8amVOaxYHFQZTyCCFC1UFSneV615S96fozSt1esRkH2nromv%2Fc5bw4mMbYkkwjhSxCAcsFNk100LSDiYN9lkUhYM%2FN0%2B4Mn1UpqTna%2F0ycT6vJFFoMW0hp1Vd0oaRD3dzvXlmq8t%2B1p259sORZuQMED7MReeJ90tG3sVyeWHUwyujFCYW9aZGhKNdTQy%2Bqstch2HtTHM%2BeHPYd8YLtHS8kOrqREXy%2FaU3KhxB%2F80c6Wvkm75Z1nMMWzP25IEZeiB1T1wi1ww6Df7D9rSo9%2F1dlqgsVsuz47K12UsqzWIj1ISkNIvyzolSGKBYzuHfvR0ee20ZrSXCpagcMM%2BAhFfUoB%2BhwxeHWI%2BdQBEY7KN0EqkOcEly%2FqwTclb9sA%2FR%2F3WOW%2FfyPokS1uSXcsSlYNYuCBhWiOHcso9pxPb5ZSkk%2BbwzU%2BJIB3NTyeqjM3TSjrn84hb53Z07sbsNEzqztl0abiI2ifRIcwgbaYzQY6pgE240QNkt4M%2Bzpk3IUZOpiH2DwEHMgCdH%2FhTzx4LDUWoNr9%2F2l%2Fx49TtwuC9DBCTZ7v7AsNyF3RTGniPFfwAbAEzSMkUJKvIOk%2F6mAnMbkUwQayVN2HEU%2BgFLlYPzMiPOxBpJKRybyn4R3MS%2F6%2F5MSVitycMt0ABrN1sVq7ycDCFHB9esVPCg6qROzfpem6FDyXLVUtar%2FASo6cjnpzm18IVp5CxaJT&X-Amz-Signature=974f2e180b3cc81ddd97668e323bf8830230dab878a02c970060ea32a60e3981&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JZINICM%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQzZ%2BsLe5TccF9eArdqg9E3I41vUxFpWmPjIou8p5LhAiBJp%2F4vybpMMOvccTuf4osyvLhtRn9etA8vzCw1HBnYrCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8FF%2FeDZ6iH1kRVbcKtwD2OEx09Xq63C%2BuV4ZqG%2BwNMhIDsb%2F%2BJ%2FMCR1BMIDB%2BhDOPpUp%2F9zJY6Cq24n%2BkCuyByz2PMXR1P%2BCTpvLxZ81OLG0b0qR5kS2QEcM077KMAKkWVOqPf4myaHf3I%2BCT7ngNxhegiOc4FW6DiR9KJEuoB0LpGdUK8amVOaxYHFQZTyCCFC1UFSneV615S96fozSt1esRkH2nromv%2Fc5bw4mMbYkkwjhSxCAcsFNk100LSDiYN9lkUhYM%2FN0%2B4Mn1UpqTna%2F0ycT6vJFFoMW0hp1Vd0oaRD3dzvXlmq8t%2B1p259sORZuQMED7MReeJ90tG3sVyeWHUwyujFCYW9aZGhKNdTQy%2Bqstch2HtTHM%2BeHPYd8YLtHS8kOrqREXy%2FaU3KhxB%2F80c6Wvkm75Z1nMMWzP25IEZeiB1T1wi1ww6Df7D9rSo9%2F1dlqgsVsuz47K12UsqzWIj1ISkNIvyzolSGKBYzuHfvR0ee20ZrSXCpagcMM%2BAhFfUoB%2BhwxeHWI%2BdQBEY7KN0EqkOcEly%2FqwTclb9sA%2FR%2F3WOW%2FfyPokS1uSXcsSlYNYuCBhWiOHcso9pxPb5ZSkk%2BbwzU%2BJIB3NTyeqjM3TSjrn84hb53Z07sbsNEzqztl0abiI2ifRIcwgbaYzQY6pgE240QNkt4M%2Bzpk3IUZOpiH2DwEHMgCdH%2FhTzx4LDUWoNr9%2F2l%2Fx49TtwuC9DBCTZ7v7AsNyF3RTGniPFfwAbAEzSMkUJKvIOk%2F6mAnMbkUwQayVN2HEU%2BgFLlYPzMiPOxBpJKRybyn4R3MS%2F6%2F5MSVitycMt0ABrN1sVq7ycDCFHB9esVPCg6qROzfpem6FDyXLVUtar%2FASo6cjnpzm18IVp5CxaJT&X-Amz-Signature=0f5bd58e979ff263cd8bd738d1d4f97dd9c03921dc3282c89f43ac2e39d99b31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



