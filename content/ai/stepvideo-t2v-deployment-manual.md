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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGDW2OP2%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCdNfB5TY9HrYku9%2BfwyKRawBU6gfCknd%2BVeHA9emSTbwIhANhZahNQ3ezm2MTG79QBBQj3up7eI%2B9LB17WL1t2TIxWKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaU3uQP0DB6QXPcRUq3AM6Q0UL7VMalxjSdDuVIs9JtR%2B9BIecVUtggrTfZbbYhL%2BzACYqeXuhvqP6UlimpImrWEMvaItzgk0KbF8oYJD2gYxhIJHtIdWVk7KGn%2Bi7UkeaNJngzo2xSAmHWe8Wa27pLo5WRF2vLDxQMT4q4jCFEfweWHnU8k2YHQACfGMLq1gsy31Au7kmgP34rIv%2Bs1U%2F4xxNQim2Z%2Bz8eYQug1ui%2FMgsddmAO7in0KAj2iNK2QkwsRp6Bf8wPtp1oh6EDz7sskfb5uZBQNh5bWfgsFkrYCoT0s1eM3vss8chb3knRuo2CCy1JbxTw7JY4eEvO1bIbYI8RDFKbTCLfHJ1fjAoC2QI7uqmaV0WL%2BP2HWbcSqtxLRKL%2BUBm88DKmxRD3ajMehUr5dwHFDg5DUwPAUzBu9rBlNNQBvdVN4RQdKiwwQ16Wl7Hr8oHe3vH3K%2BErbzTHfnU0INOGeB61zcR60AO5UBvxGXJ2b0TxRHhAoKiA%2FCFo0UjkR7Yu2yvKSXbGsHK27YMdEZESvc9hr4kW9CIbmM%2FMvPd%2FqsfzitYrkDz9eEHnt6oovnu5W8oaXR0o%2FqElamPzqeAVpJnMZ1vcqk76W%2B%2Fs%2BVjPmXq2zlE4PJLKrkBkn22EykXOH3x6zDa5ZbLBjqkAdRazXZusCoJqCj0mCOCTosvPnJksX2U10D2baY0xahYA58cQFw%2Bu4MVIv96hkkqiyKvXe6sh%2F%2BGqIdp2AY65qrEai6Uu%2BBKQsij2BwjhAFa%2BPZsYYGYb9E96Kgq2n2ShnXb6lgCBETu894rwhy82O2jEr9vu4q65eeuySnfxzSKis%2BUGlH6%2F5mQ9inNEgUGNriTs8baw3Pn%2Fhbi8kXa4qDBY5hw&X-Amz-Signature=320c201050a8d8a5019efcd6e00f3aac448e8803968acbd17f09620958287e77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGDW2OP2%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCdNfB5TY9HrYku9%2BfwyKRawBU6gfCknd%2BVeHA9emSTbwIhANhZahNQ3ezm2MTG79QBBQj3up7eI%2B9LB17WL1t2TIxWKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaU3uQP0DB6QXPcRUq3AM6Q0UL7VMalxjSdDuVIs9JtR%2B9BIecVUtggrTfZbbYhL%2BzACYqeXuhvqP6UlimpImrWEMvaItzgk0KbF8oYJD2gYxhIJHtIdWVk7KGn%2Bi7UkeaNJngzo2xSAmHWe8Wa27pLo5WRF2vLDxQMT4q4jCFEfweWHnU8k2YHQACfGMLq1gsy31Au7kmgP34rIv%2Bs1U%2F4xxNQim2Z%2Bz8eYQug1ui%2FMgsddmAO7in0KAj2iNK2QkwsRp6Bf8wPtp1oh6EDz7sskfb5uZBQNh5bWfgsFkrYCoT0s1eM3vss8chb3knRuo2CCy1JbxTw7JY4eEvO1bIbYI8RDFKbTCLfHJ1fjAoC2QI7uqmaV0WL%2BP2HWbcSqtxLRKL%2BUBm88DKmxRD3ajMehUr5dwHFDg5DUwPAUzBu9rBlNNQBvdVN4RQdKiwwQ16Wl7Hr8oHe3vH3K%2BErbzTHfnU0INOGeB61zcR60AO5UBvxGXJ2b0TxRHhAoKiA%2FCFo0UjkR7Yu2yvKSXbGsHK27YMdEZESvc9hr4kW9CIbmM%2FMvPd%2FqsfzitYrkDz9eEHnt6oovnu5W8oaXR0o%2FqElamPzqeAVpJnMZ1vcqk76W%2B%2Fs%2BVjPmXq2zlE4PJLKrkBkn22EykXOH3x6zDa5ZbLBjqkAdRazXZusCoJqCj0mCOCTosvPnJksX2U10D2baY0xahYA58cQFw%2Bu4MVIv96hkkqiyKvXe6sh%2F%2BGqIdp2AY65qrEai6Uu%2BBKQsij2BwjhAFa%2BPZsYYGYb9E96Kgq2n2ShnXb6lgCBETu894rwhy82O2jEr9vu4q65eeuySnfxzSKis%2BUGlH6%2F5mQ9inNEgUGNriTs8baw3Pn%2Fhbi8kXa4qDBY5hw&X-Amz-Signature=03dc25c174dcbc0936918673da9f8fef33646fe2b665c12c0b71a2ea58cc6ffb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGDW2OP2%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCdNfB5TY9HrYku9%2BfwyKRawBU6gfCknd%2BVeHA9emSTbwIhANhZahNQ3ezm2MTG79QBBQj3up7eI%2B9LB17WL1t2TIxWKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaU3uQP0DB6QXPcRUq3AM6Q0UL7VMalxjSdDuVIs9JtR%2B9BIecVUtggrTfZbbYhL%2BzACYqeXuhvqP6UlimpImrWEMvaItzgk0KbF8oYJD2gYxhIJHtIdWVk7KGn%2Bi7UkeaNJngzo2xSAmHWe8Wa27pLo5WRF2vLDxQMT4q4jCFEfweWHnU8k2YHQACfGMLq1gsy31Au7kmgP34rIv%2Bs1U%2F4xxNQim2Z%2Bz8eYQug1ui%2FMgsddmAO7in0KAj2iNK2QkwsRp6Bf8wPtp1oh6EDz7sskfb5uZBQNh5bWfgsFkrYCoT0s1eM3vss8chb3knRuo2CCy1JbxTw7JY4eEvO1bIbYI8RDFKbTCLfHJ1fjAoC2QI7uqmaV0WL%2BP2HWbcSqtxLRKL%2BUBm88DKmxRD3ajMehUr5dwHFDg5DUwPAUzBu9rBlNNQBvdVN4RQdKiwwQ16Wl7Hr8oHe3vH3K%2BErbzTHfnU0INOGeB61zcR60AO5UBvxGXJ2b0TxRHhAoKiA%2FCFo0UjkR7Yu2yvKSXbGsHK27YMdEZESvc9hr4kW9CIbmM%2FMvPd%2FqsfzitYrkDz9eEHnt6oovnu5W8oaXR0o%2FqElamPzqeAVpJnMZ1vcqk76W%2B%2Fs%2BVjPmXq2zlE4PJLKrkBkn22EykXOH3x6zDa5ZbLBjqkAdRazXZusCoJqCj0mCOCTosvPnJksX2U10D2baY0xahYA58cQFw%2Bu4MVIv96hkkqiyKvXe6sh%2F%2BGqIdp2AY65qrEai6Uu%2BBKQsij2BwjhAFa%2BPZsYYGYb9E96Kgq2n2ShnXb6lgCBETu894rwhy82O2jEr9vu4q65eeuySnfxzSKis%2BUGlH6%2F5mQ9inNEgUGNriTs8baw3Pn%2Fhbi8kXa4qDBY5hw&X-Amz-Signature=1967783e19bc4653157048352d195b85dfbf7d5cc107a49fef95f7835933d18e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGDW2OP2%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCdNfB5TY9HrYku9%2BfwyKRawBU6gfCknd%2BVeHA9emSTbwIhANhZahNQ3ezm2MTG79QBBQj3up7eI%2B9LB17WL1t2TIxWKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaU3uQP0DB6QXPcRUq3AM6Q0UL7VMalxjSdDuVIs9JtR%2B9BIecVUtggrTfZbbYhL%2BzACYqeXuhvqP6UlimpImrWEMvaItzgk0KbF8oYJD2gYxhIJHtIdWVk7KGn%2Bi7UkeaNJngzo2xSAmHWe8Wa27pLo5WRF2vLDxQMT4q4jCFEfweWHnU8k2YHQACfGMLq1gsy31Au7kmgP34rIv%2Bs1U%2F4xxNQim2Z%2Bz8eYQug1ui%2FMgsddmAO7in0KAj2iNK2QkwsRp6Bf8wPtp1oh6EDz7sskfb5uZBQNh5bWfgsFkrYCoT0s1eM3vss8chb3knRuo2CCy1JbxTw7JY4eEvO1bIbYI8RDFKbTCLfHJ1fjAoC2QI7uqmaV0WL%2BP2HWbcSqtxLRKL%2BUBm88DKmxRD3ajMehUr5dwHFDg5DUwPAUzBu9rBlNNQBvdVN4RQdKiwwQ16Wl7Hr8oHe3vH3K%2BErbzTHfnU0INOGeB61zcR60AO5UBvxGXJ2b0TxRHhAoKiA%2FCFo0UjkR7Yu2yvKSXbGsHK27YMdEZESvc9hr4kW9CIbmM%2FMvPd%2FqsfzitYrkDz9eEHnt6oovnu5W8oaXR0o%2FqElamPzqeAVpJnMZ1vcqk76W%2B%2Fs%2BVjPmXq2zlE4PJLKrkBkn22EykXOH3x6zDa5ZbLBjqkAdRazXZusCoJqCj0mCOCTosvPnJksX2U10D2baY0xahYA58cQFw%2Bu4MVIv96hkkqiyKvXe6sh%2F%2BGqIdp2AY65qrEai6Uu%2BBKQsij2BwjhAFa%2BPZsYYGYb9E96Kgq2n2ShnXb6lgCBETu894rwhy82O2jEr9vu4q65eeuySnfxzSKis%2BUGlH6%2F5mQ9inNEgUGNriTs8baw3Pn%2Fhbi8kXa4qDBY5hw&X-Amz-Signature=ea6104a9627dfc98764e7235652c5288de0a95e7b17abbcb44e5e98ae61bd4aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



