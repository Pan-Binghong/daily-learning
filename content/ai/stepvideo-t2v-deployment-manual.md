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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673K5MXAI%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIA2w5xuWymHOCRbiRvDpDuVZyonU5Jenu6ViFfd1ShhmAiEAjBHLWnpkuLVfALIntcuExBuQXi9eQiatf%2F5m19jznBYq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG0uhJ%2BsSfUog2lD%2BSrcA5nfWjDE9z1KRq2RRYUcHpS0nDAztaSz7agPKxrBVzTPqbE18zReLouqaQl5DLDjTa0HRYUdLhbR5CRVwZ3MbMxcULXQTQCHYznxyst1VEty4zGBEJD5ATuBnVr24fklQvkbQzJZPJPl7tVUEPYuqnkekSAuLxUCaTWNY5lKG8RJLf23GEvHiXHTAsSP3PLQvQ%2FofolaNyN0Y0zsKQ%2B94XU4rUAC0ejFFmGfgQOinqUXIqokHUrO8invWiTkovw%2BlLiY7wUrwART0qoPNbvdc0A7l6aVH2A5KaV5ALPZmI%2FZ0f0VRNbgEODmYMa2U3VT4x9QjGL7TBbj7unp%2BkGrRwlgqp6NVQRaHbEL1c%2FdOmS7Zepmk73ko9hOVLAlI5veGxlO6NVB%2FofyecOzaB4Crd8pu2K%2FMOvxwEJ%2FL0jf6bKMW9GxRZSg3pchFO4RlAEBmxeCuUDAB%2BFrkK4fuu3oHVvdCG2bwjLM5ZOlpYdbpui7etxMb2x3KsVskrQWkh2fmhWvwZIvtaTfLmIMZWXEgeR%2BV2gynOMh8tPQfksKKtuCsSgzI1EgHpjkzzPTE7RxoappvRfKwL7lrFO0wVTA8Rz2be1WX4MJOBCVDB%2Fg%2F0spYIngXqQHoKUP7i5hMKu9ysgGOqUBRYtyfDYQVlRsvmesfrAXzf%2B0A0G0lOFVuGboH9A6GWrevHbRrc5Pv8W%2F43Il%2Fwh%2FLtpNZDM1rTNmiixvzZ7y%2BGCAG%2F5zXa0JN0MXzRDINvK8y6FR9aEljUhUtHtlhXTQr2Xrhy6sVOcjpTbXDmEnUZI6XUI5PGuKqKN9M3gUHj5N31h8hw9bxZ0VeivmMPR8myNlC48ye1YjsmYwvtE335D%2BT6z%2F&X-Amz-Signature=ebebca4e32c2c5dc3cbe9921ad7e1c0f699efecb227aa24e766adf9e8a2c0c57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673K5MXAI%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIA2w5xuWymHOCRbiRvDpDuVZyonU5Jenu6ViFfd1ShhmAiEAjBHLWnpkuLVfALIntcuExBuQXi9eQiatf%2F5m19jznBYq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG0uhJ%2BsSfUog2lD%2BSrcA5nfWjDE9z1KRq2RRYUcHpS0nDAztaSz7agPKxrBVzTPqbE18zReLouqaQl5DLDjTa0HRYUdLhbR5CRVwZ3MbMxcULXQTQCHYznxyst1VEty4zGBEJD5ATuBnVr24fklQvkbQzJZPJPl7tVUEPYuqnkekSAuLxUCaTWNY5lKG8RJLf23GEvHiXHTAsSP3PLQvQ%2FofolaNyN0Y0zsKQ%2B94XU4rUAC0ejFFmGfgQOinqUXIqokHUrO8invWiTkovw%2BlLiY7wUrwART0qoPNbvdc0A7l6aVH2A5KaV5ALPZmI%2FZ0f0VRNbgEODmYMa2U3VT4x9QjGL7TBbj7unp%2BkGrRwlgqp6NVQRaHbEL1c%2FdOmS7Zepmk73ko9hOVLAlI5veGxlO6NVB%2FofyecOzaB4Crd8pu2K%2FMOvxwEJ%2FL0jf6bKMW9GxRZSg3pchFO4RlAEBmxeCuUDAB%2BFrkK4fuu3oHVvdCG2bwjLM5ZOlpYdbpui7etxMb2x3KsVskrQWkh2fmhWvwZIvtaTfLmIMZWXEgeR%2BV2gynOMh8tPQfksKKtuCsSgzI1EgHpjkzzPTE7RxoappvRfKwL7lrFO0wVTA8Rz2be1WX4MJOBCVDB%2Fg%2F0spYIngXqQHoKUP7i5hMKu9ysgGOqUBRYtyfDYQVlRsvmesfrAXzf%2B0A0G0lOFVuGboH9A6GWrevHbRrc5Pv8W%2F43Il%2Fwh%2FLtpNZDM1rTNmiixvzZ7y%2BGCAG%2F5zXa0JN0MXzRDINvK8y6FR9aEljUhUtHtlhXTQr2Xrhy6sVOcjpTbXDmEnUZI6XUI5PGuKqKN9M3gUHj5N31h8hw9bxZ0VeivmMPR8myNlC48ye1YjsmYwvtE335D%2BT6z%2F&X-Amz-Signature=f93c1a694667243462b12124df934b10aa1c70e995e0b58b8e5986502d182f11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673K5MXAI%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIA2w5xuWymHOCRbiRvDpDuVZyonU5Jenu6ViFfd1ShhmAiEAjBHLWnpkuLVfALIntcuExBuQXi9eQiatf%2F5m19jznBYq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG0uhJ%2BsSfUog2lD%2BSrcA5nfWjDE9z1KRq2RRYUcHpS0nDAztaSz7agPKxrBVzTPqbE18zReLouqaQl5DLDjTa0HRYUdLhbR5CRVwZ3MbMxcULXQTQCHYznxyst1VEty4zGBEJD5ATuBnVr24fklQvkbQzJZPJPl7tVUEPYuqnkekSAuLxUCaTWNY5lKG8RJLf23GEvHiXHTAsSP3PLQvQ%2FofolaNyN0Y0zsKQ%2B94XU4rUAC0ejFFmGfgQOinqUXIqokHUrO8invWiTkovw%2BlLiY7wUrwART0qoPNbvdc0A7l6aVH2A5KaV5ALPZmI%2FZ0f0VRNbgEODmYMa2U3VT4x9QjGL7TBbj7unp%2BkGrRwlgqp6NVQRaHbEL1c%2FdOmS7Zepmk73ko9hOVLAlI5veGxlO6NVB%2FofyecOzaB4Crd8pu2K%2FMOvxwEJ%2FL0jf6bKMW9GxRZSg3pchFO4RlAEBmxeCuUDAB%2BFrkK4fuu3oHVvdCG2bwjLM5ZOlpYdbpui7etxMb2x3KsVskrQWkh2fmhWvwZIvtaTfLmIMZWXEgeR%2BV2gynOMh8tPQfksKKtuCsSgzI1EgHpjkzzPTE7RxoappvRfKwL7lrFO0wVTA8Rz2be1WX4MJOBCVDB%2Fg%2F0spYIngXqQHoKUP7i5hMKu9ysgGOqUBRYtyfDYQVlRsvmesfrAXzf%2B0A0G0lOFVuGboH9A6GWrevHbRrc5Pv8W%2F43Il%2Fwh%2FLtpNZDM1rTNmiixvzZ7y%2BGCAG%2F5zXa0JN0MXzRDINvK8y6FR9aEljUhUtHtlhXTQr2Xrhy6sVOcjpTbXDmEnUZI6XUI5PGuKqKN9M3gUHj5N31h8hw9bxZ0VeivmMPR8myNlC48ye1YjsmYwvtE335D%2BT6z%2F&X-Amz-Signature=b6825f022759c17131ab233cd78cbcebfc5ed77b8782c964f091f092603e34b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673K5MXAI%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIA2w5xuWymHOCRbiRvDpDuVZyonU5Jenu6ViFfd1ShhmAiEAjBHLWnpkuLVfALIntcuExBuQXi9eQiatf%2F5m19jznBYq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG0uhJ%2BsSfUog2lD%2BSrcA5nfWjDE9z1KRq2RRYUcHpS0nDAztaSz7agPKxrBVzTPqbE18zReLouqaQl5DLDjTa0HRYUdLhbR5CRVwZ3MbMxcULXQTQCHYznxyst1VEty4zGBEJD5ATuBnVr24fklQvkbQzJZPJPl7tVUEPYuqnkekSAuLxUCaTWNY5lKG8RJLf23GEvHiXHTAsSP3PLQvQ%2FofolaNyN0Y0zsKQ%2B94XU4rUAC0ejFFmGfgQOinqUXIqokHUrO8invWiTkovw%2BlLiY7wUrwART0qoPNbvdc0A7l6aVH2A5KaV5ALPZmI%2FZ0f0VRNbgEODmYMa2U3VT4x9QjGL7TBbj7unp%2BkGrRwlgqp6NVQRaHbEL1c%2FdOmS7Zepmk73ko9hOVLAlI5veGxlO6NVB%2FofyecOzaB4Crd8pu2K%2FMOvxwEJ%2FL0jf6bKMW9GxRZSg3pchFO4RlAEBmxeCuUDAB%2BFrkK4fuu3oHVvdCG2bwjLM5ZOlpYdbpui7etxMb2x3KsVskrQWkh2fmhWvwZIvtaTfLmIMZWXEgeR%2BV2gynOMh8tPQfksKKtuCsSgzI1EgHpjkzzPTE7RxoappvRfKwL7lrFO0wVTA8Rz2be1WX4MJOBCVDB%2Fg%2F0spYIngXqQHoKUP7i5hMKu9ysgGOqUBRYtyfDYQVlRsvmesfrAXzf%2B0A0G0lOFVuGboH9A6GWrevHbRrc5Pv8W%2F43Il%2Fwh%2FLtpNZDM1rTNmiixvzZ7y%2BGCAG%2F5zXa0JN0MXzRDINvK8y6FR9aEljUhUtHtlhXTQr2Xrhy6sVOcjpTbXDmEnUZI6XUI5PGuKqKN9M3gUHj5N31h8hw9bxZ0VeivmMPR8myNlC48ye1YjsmYwvtE335D%2BT6z%2F&X-Amz-Signature=c5c1b94543a2157d4dc622f386b74ee7f36fc0b3ae44afa1558f1e933ecedcf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



