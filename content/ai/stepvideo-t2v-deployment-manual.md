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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3TNCDQ3%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD6be4Nwo%2BZFMci1nYruxDTSn7qJZAgef2fpVD5Ms5SSQIhAJUsM3Nsmm6CPfa8w7ZvSiATIuqRarXhs4iWdDrLRTS0Kv8DCCoQABoMNjM3NDIzMTgzODA1IgylKu6wLUzUHAK%2FWQEq3APdJf3EeRo2ZGtDDs93vEd4p2V3xc7j3vWYrpdKxYGknop8JGleqKd294Qchw%2BKGVyjQxUdTsTP4Veek7Fr0ks%2FOG2JeafjC%2BHCkOwt2TbUARRfAOeaI%2F5pfpOB9WVJHP2snR12kIPcRSvRvj4KoG6psx05a1EvQXpCbjV01XFEBv1wmEYI8%2Fgxqw0XiUEuvZvgWsmUXUoSQB%2BYT2559ajpibYKn7%2F4mvVqMJeWw1TKGswP993D5zC38kJXdz96abg9x8ISMPd3DAIsv7gwucUpdXUCfpbLsfAVU9jcYfC2iLqp5UlzxFNk96ac2CVjRP%2BEAgn5KvKpbbtLX5WYT1WJc8DOpc5KdwNqafsX8HG1hBKER8c2TuinhRVqM4W4b7Sqab4mXW4FeJE9rNoTpOdxzs0NBdYZD2TNcAsPLkq3COU9PMnfbttZOphZF7JszlH1PwgXsk8KpsjlwCuvh8JnopF3zhzb4Ix60hgbrgh7iGrNpNZR%2Bze9kQH5ZPyq03ZG08tAxXcB0L8yH8ZceMQZPwefxdRH87UMrZrAvOgsPUUQM52VhUucQVIsbQ%2Fh4MyciBuIFbKs6b1j6uS6tBTDssUQgpv09u4oIsLWO3FLGrlXNgQxCX1ONW0xODDit%2FLNBjqkAa0RzB0fdmbDgcUNECnG6VBa91Dceqke6Z4gIrp0bO4BpRYp%2BTd6QpObxm7%2BxZdVg9U81XukahEPUohs%2BoamKwaMXnZM%2BdqrlV74KY06n3xpim3I6YrRJ0fQza0u6qYMryJmfZ%2F96u%2FHj69YOc%2BC5E2AYWYBrvR77vmE7kAbhT35OPdPYg%2BDay8qGahSznv%2BEGLpdE3t6jdCJC%2BqVi3CVQXnr4Ig&X-Amz-Signature=74f4358aa10cb68a7789f7dfb8aaffc579d55a70af6d79c5da015004c0eee51c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3TNCDQ3%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD6be4Nwo%2BZFMci1nYruxDTSn7qJZAgef2fpVD5Ms5SSQIhAJUsM3Nsmm6CPfa8w7ZvSiATIuqRarXhs4iWdDrLRTS0Kv8DCCoQABoMNjM3NDIzMTgzODA1IgylKu6wLUzUHAK%2FWQEq3APdJf3EeRo2ZGtDDs93vEd4p2V3xc7j3vWYrpdKxYGknop8JGleqKd294Qchw%2BKGVyjQxUdTsTP4Veek7Fr0ks%2FOG2JeafjC%2BHCkOwt2TbUARRfAOeaI%2F5pfpOB9WVJHP2snR12kIPcRSvRvj4KoG6psx05a1EvQXpCbjV01XFEBv1wmEYI8%2Fgxqw0XiUEuvZvgWsmUXUoSQB%2BYT2559ajpibYKn7%2F4mvVqMJeWw1TKGswP993D5zC38kJXdz96abg9x8ISMPd3DAIsv7gwucUpdXUCfpbLsfAVU9jcYfC2iLqp5UlzxFNk96ac2CVjRP%2BEAgn5KvKpbbtLX5WYT1WJc8DOpc5KdwNqafsX8HG1hBKER8c2TuinhRVqM4W4b7Sqab4mXW4FeJE9rNoTpOdxzs0NBdYZD2TNcAsPLkq3COU9PMnfbttZOphZF7JszlH1PwgXsk8KpsjlwCuvh8JnopF3zhzb4Ix60hgbrgh7iGrNpNZR%2Bze9kQH5ZPyq03ZG08tAxXcB0L8yH8ZceMQZPwefxdRH87UMrZrAvOgsPUUQM52VhUucQVIsbQ%2Fh4MyciBuIFbKs6b1j6uS6tBTDssUQgpv09u4oIsLWO3FLGrlXNgQxCX1ONW0xODDit%2FLNBjqkAa0RzB0fdmbDgcUNECnG6VBa91Dceqke6Z4gIrp0bO4BpRYp%2BTd6QpObxm7%2BxZdVg9U81XukahEPUohs%2BoamKwaMXnZM%2BdqrlV74KY06n3xpim3I6YrRJ0fQza0u6qYMryJmfZ%2F96u%2FHj69YOc%2BC5E2AYWYBrvR77vmE7kAbhT35OPdPYg%2BDay8qGahSznv%2BEGLpdE3t6jdCJC%2BqVi3CVQXnr4Ig&X-Amz-Signature=cf72e9cf21afe2a54fcc5a2d9a88aef04138a73dc9b5f1cdace61d1a3bf1fe90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3TNCDQ3%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD6be4Nwo%2BZFMci1nYruxDTSn7qJZAgef2fpVD5Ms5SSQIhAJUsM3Nsmm6CPfa8w7ZvSiATIuqRarXhs4iWdDrLRTS0Kv8DCCoQABoMNjM3NDIzMTgzODA1IgylKu6wLUzUHAK%2FWQEq3APdJf3EeRo2ZGtDDs93vEd4p2V3xc7j3vWYrpdKxYGknop8JGleqKd294Qchw%2BKGVyjQxUdTsTP4Veek7Fr0ks%2FOG2JeafjC%2BHCkOwt2TbUARRfAOeaI%2F5pfpOB9WVJHP2snR12kIPcRSvRvj4KoG6psx05a1EvQXpCbjV01XFEBv1wmEYI8%2Fgxqw0XiUEuvZvgWsmUXUoSQB%2BYT2559ajpibYKn7%2F4mvVqMJeWw1TKGswP993D5zC38kJXdz96abg9x8ISMPd3DAIsv7gwucUpdXUCfpbLsfAVU9jcYfC2iLqp5UlzxFNk96ac2CVjRP%2BEAgn5KvKpbbtLX5WYT1WJc8DOpc5KdwNqafsX8HG1hBKER8c2TuinhRVqM4W4b7Sqab4mXW4FeJE9rNoTpOdxzs0NBdYZD2TNcAsPLkq3COU9PMnfbttZOphZF7JszlH1PwgXsk8KpsjlwCuvh8JnopF3zhzb4Ix60hgbrgh7iGrNpNZR%2Bze9kQH5ZPyq03ZG08tAxXcB0L8yH8ZceMQZPwefxdRH87UMrZrAvOgsPUUQM52VhUucQVIsbQ%2Fh4MyciBuIFbKs6b1j6uS6tBTDssUQgpv09u4oIsLWO3FLGrlXNgQxCX1ONW0xODDit%2FLNBjqkAa0RzB0fdmbDgcUNECnG6VBa91Dceqke6Z4gIrp0bO4BpRYp%2BTd6QpObxm7%2BxZdVg9U81XukahEPUohs%2BoamKwaMXnZM%2BdqrlV74KY06n3xpim3I6YrRJ0fQza0u6qYMryJmfZ%2F96u%2FHj69YOc%2BC5E2AYWYBrvR77vmE7kAbhT35OPdPYg%2BDay8qGahSznv%2BEGLpdE3t6jdCJC%2BqVi3CVQXnr4Ig&X-Amz-Signature=7e81cca3aade812106c4f7652bc20739346f640a0f5e467386e8408b95a074ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3TNCDQ3%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD6be4Nwo%2BZFMci1nYruxDTSn7qJZAgef2fpVD5Ms5SSQIhAJUsM3Nsmm6CPfa8w7ZvSiATIuqRarXhs4iWdDrLRTS0Kv8DCCoQABoMNjM3NDIzMTgzODA1IgylKu6wLUzUHAK%2FWQEq3APdJf3EeRo2ZGtDDs93vEd4p2V3xc7j3vWYrpdKxYGknop8JGleqKd294Qchw%2BKGVyjQxUdTsTP4Veek7Fr0ks%2FOG2JeafjC%2BHCkOwt2TbUARRfAOeaI%2F5pfpOB9WVJHP2snR12kIPcRSvRvj4KoG6psx05a1EvQXpCbjV01XFEBv1wmEYI8%2Fgxqw0XiUEuvZvgWsmUXUoSQB%2BYT2559ajpibYKn7%2F4mvVqMJeWw1TKGswP993D5zC38kJXdz96abg9x8ISMPd3DAIsv7gwucUpdXUCfpbLsfAVU9jcYfC2iLqp5UlzxFNk96ac2CVjRP%2BEAgn5KvKpbbtLX5WYT1WJc8DOpc5KdwNqafsX8HG1hBKER8c2TuinhRVqM4W4b7Sqab4mXW4FeJE9rNoTpOdxzs0NBdYZD2TNcAsPLkq3COU9PMnfbttZOphZF7JszlH1PwgXsk8KpsjlwCuvh8JnopF3zhzb4Ix60hgbrgh7iGrNpNZR%2Bze9kQH5ZPyq03ZG08tAxXcB0L8yH8ZceMQZPwefxdRH87UMrZrAvOgsPUUQM52VhUucQVIsbQ%2Fh4MyciBuIFbKs6b1j6uS6tBTDssUQgpv09u4oIsLWO3FLGrlXNgQxCX1ONW0xODDit%2FLNBjqkAa0RzB0fdmbDgcUNECnG6VBa91Dceqke6Z4gIrp0bO4BpRYp%2BTd6QpObxm7%2BxZdVg9U81XukahEPUohs%2BoamKwaMXnZM%2BdqrlV74KY06n3xpim3I6YrRJ0fQza0u6qYMryJmfZ%2F96u%2FHj69YOc%2BC5E2AYWYBrvR77vmE7kAbhT35OPdPYg%2BDay8qGahSznv%2BEGLpdE3t6jdCJC%2BqVi3CVQXnr4Ig&X-Amz-Signature=3d785854eef54966aea34ecb2d666547f52ae4a4a7030101a90fe73efc31109b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



