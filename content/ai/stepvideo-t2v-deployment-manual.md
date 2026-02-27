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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIQGZ4LY%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC5omgmV4tuJI0OvYPkvxOHtK24ofoiULaRA6FvL%2BHIEQIhAJwK%2FYnCHCjatW96lyCT3rAtBC4l28t%2BNIk0%2FQ4LKMrsKv8DCDQQABoMNjM3NDIzMTgzODA1IgwRCzshbdBhsC1JS0Iq3AOICHbCtuLQ3BI86rG3EfJOQWUQS5EtV6yYetOZTeatzG97n8ajb4VTUU%2Fmmw%2BkOURWSMjK8moqlBQj31KWDZOATyuZ95A4K%2BSpwMBAev50lK8%2BRg%2Bn3300IM5jQugTm9RQaE%2FWezhOxGT9BgZ9CsezT0U7MQQByqT9pqi9I6sASgIYKcu05U%2BtkscMHp2q6iFT%2FApXjeCPTfQPWHAk2gA92KnnBGLNKM3JuUxV1HrxjcCnnajt7oIb2c1iE6J0ZJghqj95oyDryQSbMbrZD%2BizkOynKabn2kVoHc4ZXz%2FgwK6Y7kqutckiaUlZ65pM41ArcHUY9k7wmZjcVNiN%2BMDjd1S9sygvWtJKSyINfSDWGBipRd1Z5lzJvCnHynfSHxx7urvoq0Y67GKnhlaZUJVMO762YA0iYMblEV1Vk0opJeHOBanyau0vGDAdevFyqmzNR6qPFJmKMnOE%2BFAQ%2BwXZXROQQ0cSgPWaudIhhQ0%2F%2FkmaDX1XslF0sXmcyE6UldB32hmB1wwpKnUEPMh0Y0QTjunbE3ofONl9p7qRhX%2BHjisHSB6elKMnp46m37elW7C9CYwmG1o%2Ff2jOWDFsUs%2BzlludEhxogVlXUpbzGQoaQmoB5qFw9D2rkDNOrTDuhYTNBjqkAamVcM6b2RdikLhs9wr0qamuF%2Bn8or2JAzFXWMFqJCHVSpUA9jDiXU1h6l3TQ7xZ6BCnTFJch3hsSJ6UAQRxVBslxhA9OKvLtaZA0J%2Fc6V1V3FuBWivkT8cHp815Jn7oflguQNKf2NghxlbtkbTXTqAxrHE4GoNWdnpXSOErSohwK2x5StZbJzaKfDXBhvh7LXbX352O%2B2Tntn16qdZlAZ4ioPmW&X-Amz-Signature=31fd9fca2d2faf7077875b53301a925d3b37b3d9e9894cb8d4a46fdd00746380&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIQGZ4LY%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC5omgmV4tuJI0OvYPkvxOHtK24ofoiULaRA6FvL%2BHIEQIhAJwK%2FYnCHCjatW96lyCT3rAtBC4l28t%2BNIk0%2FQ4LKMrsKv8DCDQQABoMNjM3NDIzMTgzODA1IgwRCzshbdBhsC1JS0Iq3AOICHbCtuLQ3BI86rG3EfJOQWUQS5EtV6yYetOZTeatzG97n8ajb4VTUU%2Fmmw%2BkOURWSMjK8moqlBQj31KWDZOATyuZ95A4K%2BSpwMBAev50lK8%2BRg%2Bn3300IM5jQugTm9RQaE%2FWezhOxGT9BgZ9CsezT0U7MQQByqT9pqi9I6sASgIYKcu05U%2BtkscMHp2q6iFT%2FApXjeCPTfQPWHAk2gA92KnnBGLNKM3JuUxV1HrxjcCnnajt7oIb2c1iE6J0ZJghqj95oyDryQSbMbrZD%2BizkOynKabn2kVoHc4ZXz%2FgwK6Y7kqutckiaUlZ65pM41ArcHUY9k7wmZjcVNiN%2BMDjd1S9sygvWtJKSyINfSDWGBipRd1Z5lzJvCnHynfSHxx7urvoq0Y67GKnhlaZUJVMO762YA0iYMblEV1Vk0opJeHOBanyau0vGDAdevFyqmzNR6qPFJmKMnOE%2BFAQ%2BwXZXROQQ0cSgPWaudIhhQ0%2F%2FkmaDX1XslF0sXmcyE6UldB32hmB1wwpKnUEPMh0Y0QTjunbE3ofONl9p7qRhX%2BHjisHSB6elKMnp46m37elW7C9CYwmG1o%2Ff2jOWDFsUs%2BzlludEhxogVlXUpbzGQoaQmoB5qFw9D2rkDNOrTDuhYTNBjqkAamVcM6b2RdikLhs9wr0qamuF%2Bn8or2JAzFXWMFqJCHVSpUA9jDiXU1h6l3TQ7xZ6BCnTFJch3hsSJ6UAQRxVBslxhA9OKvLtaZA0J%2Fc6V1V3FuBWivkT8cHp815Jn7oflguQNKf2NghxlbtkbTXTqAxrHE4GoNWdnpXSOErSohwK2x5StZbJzaKfDXBhvh7LXbX352O%2B2Tntn16qdZlAZ4ioPmW&X-Amz-Signature=2b902badaf832a40ae4394d4ee63d84c1bbd64a5757451b36cf229f3c14f42df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIQGZ4LY%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC5omgmV4tuJI0OvYPkvxOHtK24ofoiULaRA6FvL%2BHIEQIhAJwK%2FYnCHCjatW96lyCT3rAtBC4l28t%2BNIk0%2FQ4LKMrsKv8DCDQQABoMNjM3NDIzMTgzODA1IgwRCzshbdBhsC1JS0Iq3AOICHbCtuLQ3BI86rG3EfJOQWUQS5EtV6yYetOZTeatzG97n8ajb4VTUU%2Fmmw%2BkOURWSMjK8moqlBQj31KWDZOATyuZ95A4K%2BSpwMBAev50lK8%2BRg%2Bn3300IM5jQugTm9RQaE%2FWezhOxGT9BgZ9CsezT0U7MQQByqT9pqi9I6sASgIYKcu05U%2BtkscMHp2q6iFT%2FApXjeCPTfQPWHAk2gA92KnnBGLNKM3JuUxV1HrxjcCnnajt7oIb2c1iE6J0ZJghqj95oyDryQSbMbrZD%2BizkOynKabn2kVoHc4ZXz%2FgwK6Y7kqutckiaUlZ65pM41ArcHUY9k7wmZjcVNiN%2BMDjd1S9sygvWtJKSyINfSDWGBipRd1Z5lzJvCnHynfSHxx7urvoq0Y67GKnhlaZUJVMO762YA0iYMblEV1Vk0opJeHOBanyau0vGDAdevFyqmzNR6qPFJmKMnOE%2BFAQ%2BwXZXROQQ0cSgPWaudIhhQ0%2F%2FkmaDX1XslF0sXmcyE6UldB32hmB1wwpKnUEPMh0Y0QTjunbE3ofONl9p7qRhX%2BHjisHSB6elKMnp46m37elW7C9CYwmG1o%2Ff2jOWDFsUs%2BzlludEhxogVlXUpbzGQoaQmoB5qFw9D2rkDNOrTDuhYTNBjqkAamVcM6b2RdikLhs9wr0qamuF%2Bn8or2JAzFXWMFqJCHVSpUA9jDiXU1h6l3TQ7xZ6BCnTFJch3hsSJ6UAQRxVBslxhA9OKvLtaZA0J%2Fc6V1V3FuBWivkT8cHp815Jn7oflguQNKf2NghxlbtkbTXTqAxrHE4GoNWdnpXSOErSohwK2x5StZbJzaKfDXBhvh7LXbX352O%2B2Tntn16qdZlAZ4ioPmW&X-Amz-Signature=e321306d5e9074da4709e3e24dc1ad5bf8115d230b62b1b5dd3b11af9ff83384&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIQGZ4LY%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC5omgmV4tuJI0OvYPkvxOHtK24ofoiULaRA6FvL%2BHIEQIhAJwK%2FYnCHCjatW96lyCT3rAtBC4l28t%2BNIk0%2FQ4LKMrsKv8DCDQQABoMNjM3NDIzMTgzODA1IgwRCzshbdBhsC1JS0Iq3AOICHbCtuLQ3BI86rG3EfJOQWUQS5EtV6yYetOZTeatzG97n8ajb4VTUU%2Fmmw%2BkOURWSMjK8moqlBQj31KWDZOATyuZ95A4K%2BSpwMBAev50lK8%2BRg%2Bn3300IM5jQugTm9RQaE%2FWezhOxGT9BgZ9CsezT0U7MQQByqT9pqi9I6sASgIYKcu05U%2BtkscMHp2q6iFT%2FApXjeCPTfQPWHAk2gA92KnnBGLNKM3JuUxV1HrxjcCnnajt7oIb2c1iE6J0ZJghqj95oyDryQSbMbrZD%2BizkOynKabn2kVoHc4ZXz%2FgwK6Y7kqutckiaUlZ65pM41ArcHUY9k7wmZjcVNiN%2BMDjd1S9sygvWtJKSyINfSDWGBipRd1Z5lzJvCnHynfSHxx7urvoq0Y67GKnhlaZUJVMO762YA0iYMblEV1Vk0opJeHOBanyau0vGDAdevFyqmzNR6qPFJmKMnOE%2BFAQ%2BwXZXROQQ0cSgPWaudIhhQ0%2F%2FkmaDX1XslF0sXmcyE6UldB32hmB1wwpKnUEPMh0Y0QTjunbE3ofONl9p7qRhX%2BHjisHSB6elKMnp46m37elW7C9CYwmG1o%2Ff2jOWDFsUs%2BzlludEhxogVlXUpbzGQoaQmoB5qFw9D2rkDNOrTDuhYTNBjqkAamVcM6b2RdikLhs9wr0qamuF%2Bn8or2JAzFXWMFqJCHVSpUA9jDiXU1h6l3TQ7xZ6BCnTFJch3hsSJ6UAQRxVBslxhA9OKvLtaZA0J%2Fc6V1V3FuBWivkT8cHp815Jn7oflguQNKf2NghxlbtkbTXTqAxrHE4GoNWdnpXSOErSohwK2x5StZbJzaKfDXBhvh7LXbX352O%2B2Tntn16qdZlAZ4ioPmW&X-Amz-Signature=51133e32e152a096764a2177431d1e745726ea1a1e0d644868ad7766cb75a8ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



