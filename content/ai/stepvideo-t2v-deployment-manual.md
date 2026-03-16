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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHDTUTLC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIE7WxT4h2JONczaxgGiri1J03ZZz9JSxQmHNTp0oektfAiAjbkeLw%2Fut0dVGgts%2FwSlMMtOacJ6FhBYAZL0FrRAxkSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyfkmCziOOrHOBaP0KtwDebnLjVhACjTYSs3sCmb6Oa4wkiyJHpYSw8WOfblpSYgXXIJHP6zAjG7M3LknOoe8MXawmnj8REBBkOufj%2F%2BTFEMJcYxAleHQI5KIkpv%2F6XWjeLRkEzGgp1bpoXnV%2BQXA2WmlZo4sdJRA5vxwo3qEYsSB4hdobYvKT6%2Bfjq5Y9Me8%2BwZHgOIyjIbXUyU5jBPmkuqXILbZxj%2FODStXy8uvcrVUUwasPTJOGcWKsF4riVEqrTijBR4kPqvGA7UlQ2%2BW82IOxDeBFhZvvVdAxUt54DcFMpMQSvpc13y%2F220Dex1M%2BlAPzM4wLbLZIgZ4WHXgSD45Kys7bw7dJaCrNQo0Xe3RgCZIXbGhSx0nKkkWA837%2FkQUHn%2FMcL0DOXVYnq6yCBCwLOIkfMF8Emc%2FD3zKymsh7iDdTbjwQ4zcS0Hzd1oIJy2LaQ0p18TZJhlx%2Fc9KxCYnFmdOcf5e1FRMvKlATiXR5d7f1%2Be%2F46PDmsdlHoCRhcL9AGBcUgKrIk7c6nmHfTxoJ9Pa61tkK99qq%2FgV9FcUUZzw3f9FrZVntwsJm3nv4d5e%2Fk5C0SbzkFp%2FoVObqASvgmRF70sb8S5e5%2Fz2Qw8GbvvuN6TSZV5mNMwihu9QwwHUtTpe7QaieFYwtL7dzQY6pgGTyk8Vt2IVP%2FYjCkIfbkTgT0dif7xVKS%2BCG0aX5qRb4TJPgd4aCs7RX1KpNBr2Fi7QkI5o2XcUjmvqUxpHQ%2BaQxcqnd6QYlFw8Rg8a4hQbBh7asYJngOSPqcvBe%2Fm8CxShZQ502AuMtZ3o1DGWO5%2FjfuF69MQrgk1SaKDV0em57SFtEpqTaTWFhJYcqcAE4MywuqU%2F4xlNe5BxtHSGeBdEYTyBtssv&X-Amz-Signature=2958d3ed73dbc47f513a75079cb3fb40ef78586f1ce7b6d409c4e1660bdee6bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHDTUTLC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIE7WxT4h2JONczaxgGiri1J03ZZz9JSxQmHNTp0oektfAiAjbkeLw%2Fut0dVGgts%2FwSlMMtOacJ6FhBYAZL0FrRAxkSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyfkmCziOOrHOBaP0KtwDebnLjVhACjTYSs3sCmb6Oa4wkiyJHpYSw8WOfblpSYgXXIJHP6zAjG7M3LknOoe8MXawmnj8REBBkOufj%2F%2BTFEMJcYxAleHQI5KIkpv%2F6XWjeLRkEzGgp1bpoXnV%2BQXA2WmlZo4sdJRA5vxwo3qEYsSB4hdobYvKT6%2Bfjq5Y9Me8%2BwZHgOIyjIbXUyU5jBPmkuqXILbZxj%2FODStXy8uvcrVUUwasPTJOGcWKsF4riVEqrTijBR4kPqvGA7UlQ2%2BW82IOxDeBFhZvvVdAxUt54DcFMpMQSvpc13y%2F220Dex1M%2BlAPzM4wLbLZIgZ4WHXgSD45Kys7bw7dJaCrNQo0Xe3RgCZIXbGhSx0nKkkWA837%2FkQUHn%2FMcL0DOXVYnq6yCBCwLOIkfMF8Emc%2FD3zKymsh7iDdTbjwQ4zcS0Hzd1oIJy2LaQ0p18TZJhlx%2Fc9KxCYnFmdOcf5e1FRMvKlATiXR5d7f1%2Be%2F46PDmsdlHoCRhcL9AGBcUgKrIk7c6nmHfTxoJ9Pa61tkK99qq%2FgV9FcUUZzw3f9FrZVntwsJm3nv4d5e%2Fk5C0SbzkFp%2FoVObqASvgmRF70sb8S5e5%2Fz2Qw8GbvvuN6TSZV5mNMwihu9QwwHUtTpe7QaieFYwtL7dzQY6pgGTyk8Vt2IVP%2FYjCkIfbkTgT0dif7xVKS%2BCG0aX5qRb4TJPgd4aCs7RX1KpNBr2Fi7QkI5o2XcUjmvqUxpHQ%2BaQxcqnd6QYlFw8Rg8a4hQbBh7asYJngOSPqcvBe%2Fm8CxShZQ502AuMtZ3o1DGWO5%2FjfuF69MQrgk1SaKDV0em57SFtEpqTaTWFhJYcqcAE4MywuqU%2F4xlNe5BxtHSGeBdEYTyBtssv&X-Amz-Signature=66d656a6c403f47efa1dfe10efa1c6966729202e049202a3eeb79b25f517efd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHDTUTLC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIE7WxT4h2JONczaxgGiri1J03ZZz9JSxQmHNTp0oektfAiAjbkeLw%2Fut0dVGgts%2FwSlMMtOacJ6FhBYAZL0FrRAxkSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyfkmCziOOrHOBaP0KtwDebnLjVhACjTYSs3sCmb6Oa4wkiyJHpYSw8WOfblpSYgXXIJHP6zAjG7M3LknOoe8MXawmnj8REBBkOufj%2F%2BTFEMJcYxAleHQI5KIkpv%2F6XWjeLRkEzGgp1bpoXnV%2BQXA2WmlZo4sdJRA5vxwo3qEYsSB4hdobYvKT6%2Bfjq5Y9Me8%2BwZHgOIyjIbXUyU5jBPmkuqXILbZxj%2FODStXy8uvcrVUUwasPTJOGcWKsF4riVEqrTijBR4kPqvGA7UlQ2%2BW82IOxDeBFhZvvVdAxUt54DcFMpMQSvpc13y%2F220Dex1M%2BlAPzM4wLbLZIgZ4WHXgSD45Kys7bw7dJaCrNQo0Xe3RgCZIXbGhSx0nKkkWA837%2FkQUHn%2FMcL0DOXVYnq6yCBCwLOIkfMF8Emc%2FD3zKymsh7iDdTbjwQ4zcS0Hzd1oIJy2LaQ0p18TZJhlx%2Fc9KxCYnFmdOcf5e1FRMvKlATiXR5d7f1%2Be%2F46PDmsdlHoCRhcL9AGBcUgKrIk7c6nmHfTxoJ9Pa61tkK99qq%2FgV9FcUUZzw3f9FrZVntwsJm3nv4d5e%2Fk5C0SbzkFp%2FoVObqASvgmRF70sb8S5e5%2Fz2Qw8GbvvuN6TSZV5mNMwihu9QwwHUtTpe7QaieFYwtL7dzQY6pgGTyk8Vt2IVP%2FYjCkIfbkTgT0dif7xVKS%2BCG0aX5qRb4TJPgd4aCs7RX1KpNBr2Fi7QkI5o2XcUjmvqUxpHQ%2BaQxcqnd6QYlFw8Rg8a4hQbBh7asYJngOSPqcvBe%2Fm8CxShZQ502AuMtZ3o1DGWO5%2FjfuF69MQrgk1SaKDV0em57SFtEpqTaTWFhJYcqcAE4MywuqU%2F4xlNe5BxtHSGeBdEYTyBtssv&X-Amz-Signature=04b8d7ab4556ff73f85509e846f9a31fa46acbc5fd047c27a8281da051dddd06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHDTUTLC%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIE7WxT4h2JONczaxgGiri1J03ZZz9JSxQmHNTp0oektfAiAjbkeLw%2Fut0dVGgts%2FwSlMMtOacJ6FhBYAZL0FrRAxkSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyfkmCziOOrHOBaP0KtwDebnLjVhACjTYSs3sCmb6Oa4wkiyJHpYSw8WOfblpSYgXXIJHP6zAjG7M3LknOoe8MXawmnj8REBBkOufj%2F%2BTFEMJcYxAleHQI5KIkpv%2F6XWjeLRkEzGgp1bpoXnV%2BQXA2WmlZo4sdJRA5vxwo3qEYsSB4hdobYvKT6%2Bfjq5Y9Me8%2BwZHgOIyjIbXUyU5jBPmkuqXILbZxj%2FODStXy8uvcrVUUwasPTJOGcWKsF4riVEqrTijBR4kPqvGA7UlQ2%2BW82IOxDeBFhZvvVdAxUt54DcFMpMQSvpc13y%2F220Dex1M%2BlAPzM4wLbLZIgZ4WHXgSD45Kys7bw7dJaCrNQo0Xe3RgCZIXbGhSx0nKkkWA837%2FkQUHn%2FMcL0DOXVYnq6yCBCwLOIkfMF8Emc%2FD3zKymsh7iDdTbjwQ4zcS0Hzd1oIJy2LaQ0p18TZJhlx%2Fc9KxCYnFmdOcf5e1FRMvKlATiXR5d7f1%2Be%2F46PDmsdlHoCRhcL9AGBcUgKrIk7c6nmHfTxoJ9Pa61tkK99qq%2FgV9FcUUZzw3f9FrZVntwsJm3nv4d5e%2Fk5C0SbzkFp%2FoVObqASvgmRF70sb8S5e5%2Fz2Qw8GbvvuN6TSZV5mNMwihu9QwwHUtTpe7QaieFYwtL7dzQY6pgGTyk8Vt2IVP%2FYjCkIfbkTgT0dif7xVKS%2BCG0aX5qRb4TJPgd4aCs7RX1KpNBr2Fi7QkI5o2XcUjmvqUxpHQ%2BaQxcqnd6QYlFw8Rg8a4hQbBh7asYJngOSPqcvBe%2Fm8CxShZQ502AuMtZ3o1DGWO5%2FjfuF69MQrgk1SaKDV0em57SFtEpqTaTWFhJYcqcAE4MywuqU%2F4xlNe5BxtHSGeBdEYTyBtssv&X-Amz-Signature=1bddc5275c335672db055f319aa24c11304e86a51b9b8cad28b9e4fa7c1f7790&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



