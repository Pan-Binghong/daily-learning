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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GDL34IE%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhasgzh7%2FyrqmW2H%2BtS22D9NAIJ59CUeDvjh4eQat3dAiAEmKjwtsaCcPv%2FiNpz2994m5hbzK59Xi4abVd6iPIwbyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvn0wPy51lFXCnlJBKtwDglvDVBXW0dIN47A0fZaROaxSP66NopuqWFDDr50tmAXDn2qPbPSc3am8Niqyxph4xnztQBoBxTELC4CeZEYR964WBGfqO%2FC1yxydFfQ9KTayNQBVqhj51hMjrbSJhmknBVwM7OmsmmgtazYBJ8V%2FDKuDtiRSaPfDkZRGWpMyrkMbxDz0dOqqqCjQFPRsh5CP6ihk%2F4dzrcjk5d6S3JBY51q1dJ15TazEGGPZjotl%2BNcJhB%2F7IR4wZiT4yYQZJ5f851xqwcdI7M5No6nA66k9zRNdRYzuf1w1R7hVCos7%2Fe33e4MJdT1iukNJcTEMzpaAoa0cSXzqluhUbQ5vT7n8v14Q6y6or6%2BXCIqko8B3X5%2Bl%2Fgu6V3gaCtEbjYDwPC7mgyq50rYoqNwSmzAkZyCSzI%2BFFSKh0uO8QzKxlNLIpbkn8RBUGyoLU2Q0G77zV%2BmlsionPlKQ1%2FfVG%2B%2F8Ggm6ygjJLsiGm49h50TJ%2BR0CKp41vDrvtfl6%2Fj42lyUYq8a9Jt96CmXxsNIJps0m2%2Bx%2Bq%2FrkcSN39L4x9%2Fmz%2F6vE2RlD%2FH9Rv%2FiMTCd91cBsbiHYenyUDFzLpXBVgtqthgXbr2MeCrVWeV%2BX%2FmjFtwVIllNEqboGDnPFCjBWAgUw6Zb7ywY6pgG6%2Fx8CN74KYCl8r%2FD7TGzUnYHhJlXYezwUPL7tDLNS%2Fm6o%2BwD8OnfdpWNd6j0QImmAyfMCHIifetxiMbBEYIJ%2FAt%2Bmfx6zSf033txn1XGYFLyTTbfUtwLlMVBCAcfa4VPqR%2BMqC4ug1pMYYLMOa5aKhXTCHcgJMX5QVdCK898W6s6J0o1RA9qi%2FrmVEQ%2Bn2y1WAoD%2Fl4ZmVbC79AqH9%2BJL%2FBzuw2VL&X-Amz-Signature=224c25c357d8a36f6083f7d7e0d3911367675f0da2bc784fb235cda83d0fce09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GDL34IE%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhasgzh7%2FyrqmW2H%2BtS22D9NAIJ59CUeDvjh4eQat3dAiAEmKjwtsaCcPv%2FiNpz2994m5hbzK59Xi4abVd6iPIwbyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvn0wPy51lFXCnlJBKtwDglvDVBXW0dIN47A0fZaROaxSP66NopuqWFDDr50tmAXDn2qPbPSc3am8Niqyxph4xnztQBoBxTELC4CeZEYR964WBGfqO%2FC1yxydFfQ9KTayNQBVqhj51hMjrbSJhmknBVwM7OmsmmgtazYBJ8V%2FDKuDtiRSaPfDkZRGWpMyrkMbxDz0dOqqqCjQFPRsh5CP6ihk%2F4dzrcjk5d6S3JBY51q1dJ15TazEGGPZjotl%2BNcJhB%2F7IR4wZiT4yYQZJ5f851xqwcdI7M5No6nA66k9zRNdRYzuf1w1R7hVCos7%2Fe33e4MJdT1iukNJcTEMzpaAoa0cSXzqluhUbQ5vT7n8v14Q6y6or6%2BXCIqko8B3X5%2Bl%2Fgu6V3gaCtEbjYDwPC7mgyq50rYoqNwSmzAkZyCSzI%2BFFSKh0uO8QzKxlNLIpbkn8RBUGyoLU2Q0G77zV%2BmlsionPlKQ1%2FfVG%2B%2F8Ggm6ygjJLsiGm49h50TJ%2BR0CKp41vDrvtfl6%2Fj42lyUYq8a9Jt96CmXxsNIJps0m2%2Bx%2Bq%2FrkcSN39L4x9%2Fmz%2F6vE2RlD%2FH9Rv%2FiMTCd91cBsbiHYenyUDFzLpXBVgtqthgXbr2MeCrVWeV%2BX%2FmjFtwVIllNEqboGDnPFCjBWAgUw6Zb7ywY6pgG6%2Fx8CN74KYCl8r%2FD7TGzUnYHhJlXYezwUPL7tDLNS%2Fm6o%2BwD8OnfdpWNd6j0QImmAyfMCHIifetxiMbBEYIJ%2FAt%2Bmfx6zSf033txn1XGYFLyTTbfUtwLlMVBCAcfa4VPqR%2BMqC4ug1pMYYLMOa5aKhXTCHcgJMX5QVdCK898W6s6J0o1RA9qi%2FrmVEQ%2Bn2y1WAoD%2Fl4ZmVbC79AqH9%2BJL%2FBzuw2VL&X-Amz-Signature=014d5651e2aa332b0184178c29ba1ba8cd97922076dfe6f4854531a448497595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GDL34IE%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhasgzh7%2FyrqmW2H%2BtS22D9NAIJ59CUeDvjh4eQat3dAiAEmKjwtsaCcPv%2FiNpz2994m5hbzK59Xi4abVd6iPIwbyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvn0wPy51lFXCnlJBKtwDglvDVBXW0dIN47A0fZaROaxSP66NopuqWFDDr50tmAXDn2qPbPSc3am8Niqyxph4xnztQBoBxTELC4CeZEYR964WBGfqO%2FC1yxydFfQ9KTayNQBVqhj51hMjrbSJhmknBVwM7OmsmmgtazYBJ8V%2FDKuDtiRSaPfDkZRGWpMyrkMbxDz0dOqqqCjQFPRsh5CP6ihk%2F4dzrcjk5d6S3JBY51q1dJ15TazEGGPZjotl%2BNcJhB%2F7IR4wZiT4yYQZJ5f851xqwcdI7M5No6nA66k9zRNdRYzuf1w1R7hVCos7%2Fe33e4MJdT1iukNJcTEMzpaAoa0cSXzqluhUbQ5vT7n8v14Q6y6or6%2BXCIqko8B3X5%2Bl%2Fgu6V3gaCtEbjYDwPC7mgyq50rYoqNwSmzAkZyCSzI%2BFFSKh0uO8QzKxlNLIpbkn8RBUGyoLU2Q0G77zV%2BmlsionPlKQ1%2FfVG%2B%2F8Ggm6ygjJLsiGm49h50TJ%2BR0CKp41vDrvtfl6%2Fj42lyUYq8a9Jt96CmXxsNIJps0m2%2Bx%2Bq%2FrkcSN39L4x9%2Fmz%2F6vE2RlD%2FH9Rv%2FiMTCd91cBsbiHYenyUDFzLpXBVgtqthgXbr2MeCrVWeV%2BX%2FmjFtwVIllNEqboGDnPFCjBWAgUw6Zb7ywY6pgG6%2Fx8CN74KYCl8r%2FD7TGzUnYHhJlXYezwUPL7tDLNS%2Fm6o%2BwD8OnfdpWNd6j0QImmAyfMCHIifetxiMbBEYIJ%2FAt%2Bmfx6zSf033txn1XGYFLyTTbfUtwLlMVBCAcfa4VPqR%2BMqC4ug1pMYYLMOa5aKhXTCHcgJMX5QVdCK898W6s6J0o1RA9qi%2FrmVEQ%2Bn2y1WAoD%2Fl4ZmVbC79AqH9%2BJL%2FBzuw2VL&X-Amz-Signature=321305affcd147e5b9224d3c21bdb84b6ce66d8b7dacd9816b08ac6b83566b9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GDL34IE%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhasgzh7%2FyrqmW2H%2BtS22D9NAIJ59CUeDvjh4eQat3dAiAEmKjwtsaCcPv%2FiNpz2994m5hbzK59Xi4abVd6iPIwbyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvn0wPy51lFXCnlJBKtwDglvDVBXW0dIN47A0fZaROaxSP66NopuqWFDDr50tmAXDn2qPbPSc3am8Niqyxph4xnztQBoBxTELC4CeZEYR964WBGfqO%2FC1yxydFfQ9KTayNQBVqhj51hMjrbSJhmknBVwM7OmsmmgtazYBJ8V%2FDKuDtiRSaPfDkZRGWpMyrkMbxDz0dOqqqCjQFPRsh5CP6ihk%2F4dzrcjk5d6S3JBY51q1dJ15TazEGGPZjotl%2BNcJhB%2F7IR4wZiT4yYQZJ5f851xqwcdI7M5No6nA66k9zRNdRYzuf1w1R7hVCos7%2Fe33e4MJdT1iukNJcTEMzpaAoa0cSXzqluhUbQ5vT7n8v14Q6y6or6%2BXCIqko8B3X5%2Bl%2Fgu6V3gaCtEbjYDwPC7mgyq50rYoqNwSmzAkZyCSzI%2BFFSKh0uO8QzKxlNLIpbkn8RBUGyoLU2Q0G77zV%2BmlsionPlKQ1%2FfVG%2B%2F8Ggm6ygjJLsiGm49h50TJ%2BR0CKp41vDrvtfl6%2Fj42lyUYq8a9Jt96CmXxsNIJps0m2%2Bx%2Bq%2FrkcSN39L4x9%2Fmz%2F6vE2RlD%2FH9Rv%2FiMTCd91cBsbiHYenyUDFzLpXBVgtqthgXbr2MeCrVWeV%2BX%2FmjFtwVIllNEqboGDnPFCjBWAgUw6Zb7ywY6pgG6%2Fx8CN74KYCl8r%2FD7TGzUnYHhJlXYezwUPL7tDLNS%2Fm6o%2BwD8OnfdpWNd6j0QImmAyfMCHIifetxiMbBEYIJ%2FAt%2Bmfx6zSf033txn1XGYFLyTTbfUtwLlMVBCAcfa4VPqR%2BMqC4ug1pMYYLMOa5aKhXTCHcgJMX5QVdCK898W6s6J0o1RA9qi%2FrmVEQ%2Bn2y1WAoD%2Fl4ZmVbC79AqH9%2BJL%2FBzuw2VL&X-Amz-Signature=ee256da73c58b8dc6b7c92a38521361be1cba04f637ce261bf6f024f21dc5921&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



