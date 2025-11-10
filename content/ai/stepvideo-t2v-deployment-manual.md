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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R2MPKBZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC7jLq7R17JaXSZY5dLDXve%2FIJcFKRW3gSoLTWGMqCXfAIgDrUpju8j3IfzBVguGoZodqqwbNg6DEOcVSccW0F587oqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJ7Y7k%2FerA%2FlAzOSSrcA2aOY%2FEBo6H%2BzUxeFlEhlC53sRc6xJCBFBOUbhsoU1SLVDzLZiIln57XIWTgi8nNBVn8IwzXYbIFwk5Uo0LUX0TDdrjjTL9f1pAJa85tDXfSK7FwzSAFoS3X1kq%2FyWM4NnDLnK62U6R45elBRzh2lUfPgVQCldwMaQOfLtdVeGQyVMO81W6NFGwz2a%2FnGEIWDtlGMpM9Bs1iiHHeFJ6f%2BMll7PRXKWFDXDf9zNM%2BIYpW8E6DR22%2FwLIFNJAXLtkvT%2FwBmUJupbjss4uOU4eiAW6Gvn7IS%2BCSLCIl9jYa8OCT8SxTT%2BuDht8ZRZ13OKtpGRqQ52ityTOwz8ZiyidNzcnvxU%2FQHZpdCxkQkoTtgStmgLh3%2B0tCTvCFvO5v699zs2H2sgvXCTRfx0jVkpnxMRQjxILwedoqIm9Yob3BtaEOCqoThN71rtsNagrukZrlHjVeJyjnDkQXDcvaCIQm8eE4HOgZ0ppP88E8YephhyYNPbWdVJ9CwCJbM%2Bz7yUfHDiYEnSJcrt99x0oWF8r4jCJPaK2Xz9icZJSEKc1D1fGaa2Z0pohUA7n1X6VNYNU7tn7xg1Rcr94kujnDRVjjuhgKJQOFY4XARcYrHShORCjLrjACWTysPPvw0jy7MJ64xMgGOqUBiKtfQbMenDztNgFax0fJM69yDGJEFk4AOH6DFA1lcQdUk8CKjA7jMzeXoAgg4OZj46GI38uipBY5%2F8BTpC2dyO9wZwyP7U%2BLM2AoJ7LyVyFkAZE1OOiwimBrNFNg2EzsObP3SHIKoERrMs%2B6uZ5hYnOVgDnW%2FH9wL1oq0mj6rFDFdgXb6jvxjDcJ5pOk8fTuljK4nD%2FbSD31P7z2Ad25e5u8Xpv0&X-Amz-Signature=be11bc85e2480807d8a8e840b63636f0fb6fc8a144da730db21c0dd29631faa4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R2MPKBZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC7jLq7R17JaXSZY5dLDXve%2FIJcFKRW3gSoLTWGMqCXfAIgDrUpju8j3IfzBVguGoZodqqwbNg6DEOcVSccW0F587oqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJ7Y7k%2FerA%2FlAzOSSrcA2aOY%2FEBo6H%2BzUxeFlEhlC53sRc6xJCBFBOUbhsoU1SLVDzLZiIln57XIWTgi8nNBVn8IwzXYbIFwk5Uo0LUX0TDdrjjTL9f1pAJa85tDXfSK7FwzSAFoS3X1kq%2FyWM4NnDLnK62U6R45elBRzh2lUfPgVQCldwMaQOfLtdVeGQyVMO81W6NFGwz2a%2FnGEIWDtlGMpM9Bs1iiHHeFJ6f%2BMll7PRXKWFDXDf9zNM%2BIYpW8E6DR22%2FwLIFNJAXLtkvT%2FwBmUJupbjss4uOU4eiAW6Gvn7IS%2BCSLCIl9jYa8OCT8SxTT%2BuDht8ZRZ13OKtpGRqQ52ityTOwz8ZiyidNzcnvxU%2FQHZpdCxkQkoTtgStmgLh3%2B0tCTvCFvO5v699zs2H2sgvXCTRfx0jVkpnxMRQjxILwedoqIm9Yob3BtaEOCqoThN71rtsNagrukZrlHjVeJyjnDkQXDcvaCIQm8eE4HOgZ0ppP88E8YephhyYNPbWdVJ9CwCJbM%2Bz7yUfHDiYEnSJcrt99x0oWF8r4jCJPaK2Xz9icZJSEKc1D1fGaa2Z0pohUA7n1X6VNYNU7tn7xg1Rcr94kujnDRVjjuhgKJQOFY4XARcYrHShORCjLrjACWTysPPvw0jy7MJ64xMgGOqUBiKtfQbMenDztNgFax0fJM69yDGJEFk4AOH6DFA1lcQdUk8CKjA7jMzeXoAgg4OZj46GI38uipBY5%2F8BTpC2dyO9wZwyP7U%2BLM2AoJ7LyVyFkAZE1OOiwimBrNFNg2EzsObP3SHIKoERrMs%2B6uZ5hYnOVgDnW%2FH9wL1oq0mj6rFDFdgXb6jvxjDcJ5pOk8fTuljK4nD%2FbSD31P7z2Ad25e5u8Xpv0&X-Amz-Signature=88fe5cf2ad728aead49ae8cf9e64935a55f412ff35bcd106d6bd704167f691fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R2MPKBZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC7jLq7R17JaXSZY5dLDXve%2FIJcFKRW3gSoLTWGMqCXfAIgDrUpju8j3IfzBVguGoZodqqwbNg6DEOcVSccW0F587oqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJ7Y7k%2FerA%2FlAzOSSrcA2aOY%2FEBo6H%2BzUxeFlEhlC53sRc6xJCBFBOUbhsoU1SLVDzLZiIln57XIWTgi8nNBVn8IwzXYbIFwk5Uo0LUX0TDdrjjTL9f1pAJa85tDXfSK7FwzSAFoS3X1kq%2FyWM4NnDLnK62U6R45elBRzh2lUfPgVQCldwMaQOfLtdVeGQyVMO81W6NFGwz2a%2FnGEIWDtlGMpM9Bs1iiHHeFJ6f%2BMll7PRXKWFDXDf9zNM%2BIYpW8E6DR22%2FwLIFNJAXLtkvT%2FwBmUJupbjss4uOU4eiAW6Gvn7IS%2BCSLCIl9jYa8OCT8SxTT%2BuDht8ZRZ13OKtpGRqQ52ityTOwz8ZiyidNzcnvxU%2FQHZpdCxkQkoTtgStmgLh3%2B0tCTvCFvO5v699zs2H2sgvXCTRfx0jVkpnxMRQjxILwedoqIm9Yob3BtaEOCqoThN71rtsNagrukZrlHjVeJyjnDkQXDcvaCIQm8eE4HOgZ0ppP88E8YephhyYNPbWdVJ9CwCJbM%2Bz7yUfHDiYEnSJcrt99x0oWF8r4jCJPaK2Xz9icZJSEKc1D1fGaa2Z0pohUA7n1X6VNYNU7tn7xg1Rcr94kujnDRVjjuhgKJQOFY4XARcYrHShORCjLrjACWTysPPvw0jy7MJ64xMgGOqUBiKtfQbMenDztNgFax0fJM69yDGJEFk4AOH6DFA1lcQdUk8CKjA7jMzeXoAgg4OZj46GI38uipBY5%2F8BTpC2dyO9wZwyP7U%2BLM2AoJ7LyVyFkAZE1OOiwimBrNFNg2EzsObP3SHIKoERrMs%2B6uZ5hYnOVgDnW%2FH9wL1oq0mj6rFDFdgXb6jvxjDcJ5pOk8fTuljK4nD%2FbSD31P7z2Ad25e5u8Xpv0&X-Amz-Signature=283136f23ab0103d21c2652dcca90f0b9c3810fb16a2529908aef8165572b966&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R2MPKBZ%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC7jLq7R17JaXSZY5dLDXve%2FIJcFKRW3gSoLTWGMqCXfAIgDrUpju8j3IfzBVguGoZodqqwbNg6DEOcVSccW0F587oqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJ7Y7k%2FerA%2FlAzOSSrcA2aOY%2FEBo6H%2BzUxeFlEhlC53sRc6xJCBFBOUbhsoU1SLVDzLZiIln57XIWTgi8nNBVn8IwzXYbIFwk5Uo0LUX0TDdrjjTL9f1pAJa85tDXfSK7FwzSAFoS3X1kq%2FyWM4NnDLnK62U6R45elBRzh2lUfPgVQCldwMaQOfLtdVeGQyVMO81W6NFGwz2a%2FnGEIWDtlGMpM9Bs1iiHHeFJ6f%2BMll7PRXKWFDXDf9zNM%2BIYpW8E6DR22%2FwLIFNJAXLtkvT%2FwBmUJupbjss4uOU4eiAW6Gvn7IS%2BCSLCIl9jYa8OCT8SxTT%2BuDht8ZRZ13OKtpGRqQ52ityTOwz8ZiyidNzcnvxU%2FQHZpdCxkQkoTtgStmgLh3%2B0tCTvCFvO5v699zs2H2sgvXCTRfx0jVkpnxMRQjxILwedoqIm9Yob3BtaEOCqoThN71rtsNagrukZrlHjVeJyjnDkQXDcvaCIQm8eE4HOgZ0ppP88E8YephhyYNPbWdVJ9CwCJbM%2Bz7yUfHDiYEnSJcrt99x0oWF8r4jCJPaK2Xz9icZJSEKc1D1fGaa2Z0pohUA7n1X6VNYNU7tn7xg1Rcr94kujnDRVjjuhgKJQOFY4XARcYrHShORCjLrjACWTysPPvw0jy7MJ64xMgGOqUBiKtfQbMenDztNgFax0fJM69yDGJEFk4AOH6DFA1lcQdUk8CKjA7jMzeXoAgg4OZj46GI38uipBY5%2F8BTpC2dyO9wZwyP7U%2BLM2AoJ7LyVyFkAZE1OOiwimBrNFNg2EzsObP3SHIKoERrMs%2B6uZ5hYnOVgDnW%2FH9wL1oq0mj6rFDFdgXb6jvxjDcJ5pOk8fTuljK4nD%2FbSD31P7z2Ad25e5u8Xpv0&X-Amz-Signature=39bbce832a5d56c8003f8357a4c97220e89469e14e4f94646450c2aff86b5c0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



