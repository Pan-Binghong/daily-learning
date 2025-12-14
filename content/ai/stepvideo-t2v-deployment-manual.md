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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3MQWEQ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHw9I0WAllTU6GPx%2Fxpg%2Bf6kKnsL3Nj0XVQiDF18IY1WAiEAqj2Qf1WvOco%2Fj1SEkQl3kXNsdSS3CFlmIvpqM7YYw2cq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNIZQQkLTpLGFqDsRircAyrEytIAqKK5v%2FKIaemg0OEFceJOSwRInzLr1LbUp8sFneuDiAKg%2BE%2F1myYpsFfAyEr8HPGeefNoaEIFP1IcqUzsJRgzCHJ87reYQ0bw3VskzNfjDY1ThfwqU44RL9XaA%2FgYL61%2FFTG4YAP6zFIx3YUWQpbKzTWAISIaeojVs%2F8OHDkauGQXQ%2BOe0S8rIp5HWqDOlgApKz5TZy5QORH0VgIGmlfPt4zBLN3hOynKNY4uootFRPP5Zfo0ACzHyfvApvlxpicDc%2BEcNFyFt%2F7FMUawwL%2FNJ8cQTh2Hu2AYHO62Ywg5VsHYsMBYSqptydI81TYBxUfVbO1IJBMz1jiZJ2aj3gZMj0joy50Eht0i3nNSMiluNRdwe%2Bmu6zhNzwQUlNbBsdSTueo0vbcW8kD2KraLFDBAu6UIyhgc6xKHaC91fZL7%2BI84%2FiFeU%2BWrSVUFhahk1CIU4Q6AE3hIY3NLdqS2aSu6jzKl3SJ8mukVctjUX8%2BcBpPw%2BUK60dINT2EOPOR54Z47Gj9V6VUlOnXKfNfHDhJCPrdatm6Tuj%2BetLEED0BUJgEGW9Z0MkdHuLDFI1mqxFVGdXEz7HHNdqPNgorRc4nMXRnxBXbRT9yiLySY7h1PWIK0uphuQiH7MJew%2BMkGOqUBc4XfIpokwpfrMM6%2BC1gBeOZcY9yS7%2FaklhTNvc6GY%2Br57Pm1P%2BOJMhocsCFWszYeNm%2B6l0BX84mqJg15JjpXdbP4ok6PaMI0p46Yk8f2Mw8vOY5SC8rHLMcIw8s2djznadf2BFBCEpx5lnbOl7lKpra6CAU8PEc8iX3B5bHULrtDPhpDnZnl1p%2FTzd%2BCx4YFdp13uiQQg8K11mrhA4i8mkM%2BdBGK&X-Amz-Signature=eb4d706f7603cc92fa53ebe70d9fc57c0ecaadb58ab04961909bf00d8028a60c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3MQWEQ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHw9I0WAllTU6GPx%2Fxpg%2Bf6kKnsL3Nj0XVQiDF18IY1WAiEAqj2Qf1WvOco%2Fj1SEkQl3kXNsdSS3CFlmIvpqM7YYw2cq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNIZQQkLTpLGFqDsRircAyrEytIAqKK5v%2FKIaemg0OEFceJOSwRInzLr1LbUp8sFneuDiAKg%2BE%2F1myYpsFfAyEr8HPGeefNoaEIFP1IcqUzsJRgzCHJ87reYQ0bw3VskzNfjDY1ThfwqU44RL9XaA%2FgYL61%2FFTG4YAP6zFIx3YUWQpbKzTWAISIaeojVs%2F8OHDkauGQXQ%2BOe0S8rIp5HWqDOlgApKz5TZy5QORH0VgIGmlfPt4zBLN3hOynKNY4uootFRPP5Zfo0ACzHyfvApvlxpicDc%2BEcNFyFt%2F7FMUawwL%2FNJ8cQTh2Hu2AYHO62Ywg5VsHYsMBYSqptydI81TYBxUfVbO1IJBMz1jiZJ2aj3gZMj0joy50Eht0i3nNSMiluNRdwe%2Bmu6zhNzwQUlNbBsdSTueo0vbcW8kD2KraLFDBAu6UIyhgc6xKHaC91fZL7%2BI84%2FiFeU%2BWrSVUFhahk1CIU4Q6AE3hIY3NLdqS2aSu6jzKl3SJ8mukVctjUX8%2BcBpPw%2BUK60dINT2EOPOR54Z47Gj9V6VUlOnXKfNfHDhJCPrdatm6Tuj%2BetLEED0BUJgEGW9Z0MkdHuLDFI1mqxFVGdXEz7HHNdqPNgorRc4nMXRnxBXbRT9yiLySY7h1PWIK0uphuQiH7MJew%2BMkGOqUBc4XfIpokwpfrMM6%2BC1gBeOZcY9yS7%2FaklhTNvc6GY%2Br57Pm1P%2BOJMhocsCFWszYeNm%2B6l0BX84mqJg15JjpXdbP4ok6PaMI0p46Yk8f2Mw8vOY5SC8rHLMcIw8s2djznadf2BFBCEpx5lnbOl7lKpra6CAU8PEc8iX3B5bHULrtDPhpDnZnl1p%2FTzd%2BCx4YFdp13uiQQg8K11mrhA4i8mkM%2BdBGK&X-Amz-Signature=4ef5ae083c68b610b98fb751dc834807c3cc283cbd75faf33cc84a2d248fdcb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3MQWEQ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHw9I0WAllTU6GPx%2Fxpg%2Bf6kKnsL3Nj0XVQiDF18IY1WAiEAqj2Qf1WvOco%2Fj1SEkQl3kXNsdSS3CFlmIvpqM7YYw2cq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNIZQQkLTpLGFqDsRircAyrEytIAqKK5v%2FKIaemg0OEFceJOSwRInzLr1LbUp8sFneuDiAKg%2BE%2F1myYpsFfAyEr8HPGeefNoaEIFP1IcqUzsJRgzCHJ87reYQ0bw3VskzNfjDY1ThfwqU44RL9XaA%2FgYL61%2FFTG4YAP6zFIx3YUWQpbKzTWAISIaeojVs%2F8OHDkauGQXQ%2BOe0S8rIp5HWqDOlgApKz5TZy5QORH0VgIGmlfPt4zBLN3hOynKNY4uootFRPP5Zfo0ACzHyfvApvlxpicDc%2BEcNFyFt%2F7FMUawwL%2FNJ8cQTh2Hu2AYHO62Ywg5VsHYsMBYSqptydI81TYBxUfVbO1IJBMz1jiZJ2aj3gZMj0joy50Eht0i3nNSMiluNRdwe%2Bmu6zhNzwQUlNbBsdSTueo0vbcW8kD2KraLFDBAu6UIyhgc6xKHaC91fZL7%2BI84%2FiFeU%2BWrSVUFhahk1CIU4Q6AE3hIY3NLdqS2aSu6jzKl3SJ8mukVctjUX8%2BcBpPw%2BUK60dINT2EOPOR54Z47Gj9V6VUlOnXKfNfHDhJCPrdatm6Tuj%2BetLEED0BUJgEGW9Z0MkdHuLDFI1mqxFVGdXEz7HHNdqPNgorRc4nMXRnxBXbRT9yiLySY7h1PWIK0uphuQiH7MJew%2BMkGOqUBc4XfIpokwpfrMM6%2BC1gBeOZcY9yS7%2FaklhTNvc6GY%2Br57Pm1P%2BOJMhocsCFWszYeNm%2B6l0BX84mqJg15JjpXdbP4ok6PaMI0p46Yk8f2Mw8vOY5SC8rHLMcIw8s2djznadf2BFBCEpx5lnbOl7lKpra6CAU8PEc8iX3B5bHULrtDPhpDnZnl1p%2FTzd%2BCx4YFdp13uiQQg8K11mrhA4i8mkM%2BdBGK&X-Amz-Signature=fb93bcd2669d0617bf6c93ce9f2566bed3fbf341f40db8599f030b021af05f0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3MQWEQ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHw9I0WAllTU6GPx%2Fxpg%2Bf6kKnsL3Nj0XVQiDF18IY1WAiEAqj2Qf1WvOco%2Fj1SEkQl3kXNsdSS3CFlmIvpqM7YYw2cq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDNIZQQkLTpLGFqDsRircAyrEytIAqKK5v%2FKIaemg0OEFceJOSwRInzLr1LbUp8sFneuDiAKg%2BE%2F1myYpsFfAyEr8HPGeefNoaEIFP1IcqUzsJRgzCHJ87reYQ0bw3VskzNfjDY1ThfwqU44RL9XaA%2FgYL61%2FFTG4YAP6zFIx3YUWQpbKzTWAISIaeojVs%2F8OHDkauGQXQ%2BOe0S8rIp5HWqDOlgApKz5TZy5QORH0VgIGmlfPt4zBLN3hOynKNY4uootFRPP5Zfo0ACzHyfvApvlxpicDc%2BEcNFyFt%2F7FMUawwL%2FNJ8cQTh2Hu2AYHO62Ywg5VsHYsMBYSqptydI81TYBxUfVbO1IJBMz1jiZJ2aj3gZMj0joy50Eht0i3nNSMiluNRdwe%2Bmu6zhNzwQUlNbBsdSTueo0vbcW8kD2KraLFDBAu6UIyhgc6xKHaC91fZL7%2BI84%2FiFeU%2BWrSVUFhahk1CIU4Q6AE3hIY3NLdqS2aSu6jzKl3SJ8mukVctjUX8%2BcBpPw%2BUK60dINT2EOPOR54Z47Gj9V6VUlOnXKfNfHDhJCPrdatm6Tuj%2BetLEED0BUJgEGW9Z0MkdHuLDFI1mqxFVGdXEz7HHNdqPNgorRc4nMXRnxBXbRT9yiLySY7h1PWIK0uphuQiH7MJew%2BMkGOqUBc4XfIpokwpfrMM6%2BC1gBeOZcY9yS7%2FaklhTNvc6GY%2Br57Pm1P%2BOJMhocsCFWszYeNm%2B6l0BX84mqJg15JjpXdbP4ok6PaMI0p46Yk8f2Mw8vOY5SC8rHLMcIw8s2djznadf2BFBCEpx5lnbOl7lKpra6CAU8PEc8iX3B5bHULrtDPhpDnZnl1p%2FTzd%2BCx4YFdp13uiQQg8K11mrhA4i8mkM%2BdBGK&X-Amz-Signature=723e9a85447798d667dd091db753f615c27caaee5a8f1ded358af3bbc9fa643a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



