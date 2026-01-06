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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X756ZR3G%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FH5ZUR%2BfCksaJ1JI1WkJIXQkwnN6FJ%2FPfDr7Lxsxp8AiAr%2BuDrzzeEH47EMXNYVu%2Bsp5cCUlASrnJ1hqLWFG3%2BTCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMq2Az6967LuFyxLutKtwDkuKUaRu5oLXop3QVSyM3e38lAVfcyJx7aMM%2FI4yko7TkWVjjhZ3MU0Cdqd5G%2FThpcOCbmORiuXYOP9LNkeHLP80umXQj8N%2FNQi1o0S1l6PxyKasDmFWrmx0jq56ZhofZt1bRASywFDVMSdk8fmjFmi%2FqEM6rzAjzG7z%2Fkys4ntF8Ou7b5IjBcFCs1JyhYa4DpG%2FWMbE%2Bszi1msjvH7ErXJcdLA3WXgwG%2B1N2kwA2adTDRtrpI5GGlE7VBAC5YzQase2cyAABmc1HCilqctk360CAMOONQjz7UlreZ%2F8npF3QC5hVlEUoHFbNPCjbR1URPEOr8EuDW41MuQS5z2bIdPwAx7h%2BnAzcctCEiSkHQsc3eSoXgCmZM6YDj8uMYy1bn08fHfqT%2FJUCmRYLsTJk3vqsud6pN6iZJdGmkxKsXnATQN4cjMROh0ImyEOIRV%2BXjFnBFu0BgDnbWIj%2F%2BacFoMB9r45CFT7JNa%2B8SIiuxHpPWa0Lk10WiDZUttQgs679Mr%2BSPSwD%2BRKPcux%2Fo73FzNvzyvsGKDQiBSlrT%2B89w0N7CUMKjFD6%2BE18Z6lEV7vWIFMjdmUpW25a4yN0JNq%2BSXw%2BEjxd7qB%2FXj88u7BrN1K9AUaLMESKaeabJXkw7%2BXxygY6pgHxQnhoxtPJ7JA8%2F9aTE6Hp%2BWCaxRMbxDRrvPkJLmNX9eojd3x0nbtBTNYgU8bT%2FA1IvI6HmYmz5xgipvedxx3tsYecn1m7bsJ%2F45cjCSBTVmuh5yzUquKQ4yee122bH8Qa9e478jASDaVVroyeYWhvw8HdZibKOLnnddrgf7BMtgyYAtWJ%2FPngnLckOiQML2YIAK9CMKLLFT%2BiVmRpKyrwBT9NFNuD&X-Amz-Signature=0d39d393d543d7519c1afac02641652ec67ac315b65c9b8c4ef3eb6b5bf5060d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X756ZR3G%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FH5ZUR%2BfCksaJ1JI1WkJIXQkwnN6FJ%2FPfDr7Lxsxp8AiAr%2BuDrzzeEH47EMXNYVu%2Bsp5cCUlASrnJ1hqLWFG3%2BTCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMq2Az6967LuFyxLutKtwDkuKUaRu5oLXop3QVSyM3e38lAVfcyJx7aMM%2FI4yko7TkWVjjhZ3MU0Cdqd5G%2FThpcOCbmORiuXYOP9LNkeHLP80umXQj8N%2FNQi1o0S1l6PxyKasDmFWrmx0jq56ZhofZt1bRASywFDVMSdk8fmjFmi%2FqEM6rzAjzG7z%2Fkys4ntF8Ou7b5IjBcFCs1JyhYa4DpG%2FWMbE%2Bszi1msjvH7ErXJcdLA3WXgwG%2B1N2kwA2adTDRtrpI5GGlE7VBAC5YzQase2cyAABmc1HCilqctk360CAMOONQjz7UlreZ%2F8npF3QC5hVlEUoHFbNPCjbR1URPEOr8EuDW41MuQS5z2bIdPwAx7h%2BnAzcctCEiSkHQsc3eSoXgCmZM6YDj8uMYy1bn08fHfqT%2FJUCmRYLsTJk3vqsud6pN6iZJdGmkxKsXnATQN4cjMROh0ImyEOIRV%2BXjFnBFu0BgDnbWIj%2F%2BacFoMB9r45CFT7JNa%2B8SIiuxHpPWa0Lk10WiDZUttQgs679Mr%2BSPSwD%2BRKPcux%2Fo73FzNvzyvsGKDQiBSlrT%2B89w0N7CUMKjFD6%2BE18Z6lEV7vWIFMjdmUpW25a4yN0JNq%2BSXw%2BEjxd7qB%2FXj88u7BrN1K9AUaLMESKaeabJXkw7%2BXxygY6pgHxQnhoxtPJ7JA8%2F9aTE6Hp%2BWCaxRMbxDRrvPkJLmNX9eojd3x0nbtBTNYgU8bT%2FA1IvI6HmYmz5xgipvedxx3tsYecn1m7bsJ%2F45cjCSBTVmuh5yzUquKQ4yee122bH8Qa9e478jASDaVVroyeYWhvw8HdZibKOLnnddrgf7BMtgyYAtWJ%2FPngnLckOiQML2YIAK9CMKLLFT%2BiVmRpKyrwBT9NFNuD&X-Amz-Signature=a913b632a5d7be7c61cf67575a1696538841bc84640f5df1e7e12bc3660e8609&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X756ZR3G%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FH5ZUR%2BfCksaJ1JI1WkJIXQkwnN6FJ%2FPfDr7Lxsxp8AiAr%2BuDrzzeEH47EMXNYVu%2Bsp5cCUlASrnJ1hqLWFG3%2BTCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMq2Az6967LuFyxLutKtwDkuKUaRu5oLXop3QVSyM3e38lAVfcyJx7aMM%2FI4yko7TkWVjjhZ3MU0Cdqd5G%2FThpcOCbmORiuXYOP9LNkeHLP80umXQj8N%2FNQi1o0S1l6PxyKasDmFWrmx0jq56ZhofZt1bRASywFDVMSdk8fmjFmi%2FqEM6rzAjzG7z%2Fkys4ntF8Ou7b5IjBcFCs1JyhYa4DpG%2FWMbE%2Bszi1msjvH7ErXJcdLA3WXgwG%2B1N2kwA2adTDRtrpI5GGlE7VBAC5YzQase2cyAABmc1HCilqctk360CAMOONQjz7UlreZ%2F8npF3QC5hVlEUoHFbNPCjbR1URPEOr8EuDW41MuQS5z2bIdPwAx7h%2BnAzcctCEiSkHQsc3eSoXgCmZM6YDj8uMYy1bn08fHfqT%2FJUCmRYLsTJk3vqsud6pN6iZJdGmkxKsXnATQN4cjMROh0ImyEOIRV%2BXjFnBFu0BgDnbWIj%2F%2BacFoMB9r45CFT7JNa%2B8SIiuxHpPWa0Lk10WiDZUttQgs679Mr%2BSPSwD%2BRKPcux%2Fo73FzNvzyvsGKDQiBSlrT%2B89w0N7CUMKjFD6%2BE18Z6lEV7vWIFMjdmUpW25a4yN0JNq%2BSXw%2BEjxd7qB%2FXj88u7BrN1K9AUaLMESKaeabJXkw7%2BXxygY6pgHxQnhoxtPJ7JA8%2F9aTE6Hp%2BWCaxRMbxDRrvPkJLmNX9eojd3x0nbtBTNYgU8bT%2FA1IvI6HmYmz5xgipvedxx3tsYecn1m7bsJ%2F45cjCSBTVmuh5yzUquKQ4yee122bH8Qa9e478jASDaVVroyeYWhvw8HdZibKOLnnddrgf7BMtgyYAtWJ%2FPngnLckOiQML2YIAK9CMKLLFT%2BiVmRpKyrwBT9NFNuD&X-Amz-Signature=9cb90bf33ab5c3ed565987b32997e029b0c5e3ef72bed1cda3d3367e969f3706&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X756ZR3G%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH%2FH5ZUR%2BfCksaJ1JI1WkJIXQkwnN6FJ%2FPfDr7Lxsxp8AiAr%2BuDrzzeEH47EMXNYVu%2Bsp5cCUlASrnJ1hqLWFG3%2BTCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMq2Az6967LuFyxLutKtwDkuKUaRu5oLXop3QVSyM3e38lAVfcyJx7aMM%2FI4yko7TkWVjjhZ3MU0Cdqd5G%2FThpcOCbmORiuXYOP9LNkeHLP80umXQj8N%2FNQi1o0S1l6PxyKasDmFWrmx0jq56ZhofZt1bRASywFDVMSdk8fmjFmi%2FqEM6rzAjzG7z%2Fkys4ntF8Ou7b5IjBcFCs1JyhYa4DpG%2FWMbE%2Bszi1msjvH7ErXJcdLA3WXgwG%2B1N2kwA2adTDRtrpI5GGlE7VBAC5YzQase2cyAABmc1HCilqctk360CAMOONQjz7UlreZ%2F8npF3QC5hVlEUoHFbNPCjbR1URPEOr8EuDW41MuQS5z2bIdPwAx7h%2BnAzcctCEiSkHQsc3eSoXgCmZM6YDj8uMYy1bn08fHfqT%2FJUCmRYLsTJk3vqsud6pN6iZJdGmkxKsXnATQN4cjMROh0ImyEOIRV%2BXjFnBFu0BgDnbWIj%2F%2BacFoMB9r45CFT7JNa%2B8SIiuxHpPWa0Lk10WiDZUttQgs679Mr%2BSPSwD%2BRKPcux%2Fo73FzNvzyvsGKDQiBSlrT%2B89w0N7CUMKjFD6%2BE18Z6lEV7vWIFMjdmUpW25a4yN0JNq%2BSXw%2BEjxd7qB%2FXj88u7BrN1K9AUaLMESKaeabJXkw7%2BXxygY6pgHxQnhoxtPJ7JA8%2F9aTE6Hp%2BWCaxRMbxDRrvPkJLmNX9eojd3x0nbtBTNYgU8bT%2FA1IvI6HmYmz5xgipvedxx3tsYecn1m7bsJ%2F45cjCSBTVmuh5yzUquKQ4yee122bH8Qa9e478jASDaVVroyeYWhvw8HdZibKOLnnddrgf7BMtgyYAtWJ%2FPngnLckOiQML2YIAK9CMKLLFT%2BiVmRpKyrwBT9NFNuD&X-Amz-Signature=a8cc0ee09b3d8b6e1bcc6c2058d31db0006e7cf789d9984e573ee7d5296e7dbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



