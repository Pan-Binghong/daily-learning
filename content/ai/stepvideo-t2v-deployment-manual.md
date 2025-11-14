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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRJIDGK7%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAZJTzHsxbFJw84TiLX1qsQKOvHUSk054zzBHoqKXauAiB6ssv6v%2F2rDSgq%2FIli2zQ1m73uBd1eSoY5bpORuR3vkyr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMRjEkm3P65PpU3xckKtwDVQiotsfpeIn%2F9w76vuTJlGJwAq29N6b7nQeUaBoYa%2B0nn2xplNQ7RKnS%2FGghH3jMhg0oxGrMsVa5JQGuxq%2FqERyrW%2FZRNOUHbcCzTjUAs1RrC9CrNV%2Fa7M%2FflyjMEeqoidZS7xNwB9RZsyJK3jeqBD1esNBUHIgiSnCA4rp1WN%2BGLf53wodcMXYApMZ9k%2FwH4T%2BaUmQ%2FF9PxmnJr%2B%2FPZ%2BxMG%2BgV453S4KKst5IGuRIyE5a4qChB801fdfPBc9Cc%2F15zhrv4uK2sWP27Rj%2FkTBNPffbWnv3QTCjaOhlTllqdAu9JYvs3%2F%2F5jMlcG%2BE7m9B0iUkZJjqmPfXuYF9kanOS9jHFUsWuKQM11XBjNEZN9Aore7xCF%2F4t61Tk88o1Sdsdk9UZmLwBazqtLTpKUPiX3ix%2B%2BZfAnpONVhMQ1%2Fumol7rFMut1SvjjD5gNnfTn2sWEvH%2F420iWzTn5t1ymh%2BYvPOIQlSve60I%2B%2B7HBTxOPJB4rFZ6w1GXHyfSTbNDzWf0PAYGAaGbiE5BrnpjOUG%2BnPd%2F5zztIGfDKBnO4ncIz4SYi0LlEUFFwKYAyOvohOSMp9K%2BDb%2BHzyeof6CuNb7t3mgTZUAqeEif2lS4Sg%2BDi51UqQQvipIV8g%2B1Uw8InayAY6pgFKkUJIWjty5B4R%2BgoFPEgpjy5sb9ZeOS%2BhfoF0j84m4jE%2B8H9qJodZifEYHS8xmne27Ak3ZBr5GgAl38u%2Bpfusv4yzlyetrzS%2FhQ03NcXFs4YQiEGYBAamAn%2FqzZkVEr12qr6riFYIjcKUOSioT0%2FnIH%2FEc3NYxsVTgGkbrdj%2BdlnTokBO9DDf2pzpk%2Fy%2BBkceVNDBEuYrl7Jz4ujINxf1Uzkz8REz&X-Amz-Signature=68d41e65a9b8f0e65c330e06f6946374bbf74cec75b23f2eacf370adb73eef39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRJIDGK7%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAZJTzHsxbFJw84TiLX1qsQKOvHUSk054zzBHoqKXauAiB6ssv6v%2F2rDSgq%2FIli2zQ1m73uBd1eSoY5bpORuR3vkyr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMRjEkm3P65PpU3xckKtwDVQiotsfpeIn%2F9w76vuTJlGJwAq29N6b7nQeUaBoYa%2B0nn2xplNQ7RKnS%2FGghH3jMhg0oxGrMsVa5JQGuxq%2FqERyrW%2FZRNOUHbcCzTjUAs1RrC9CrNV%2Fa7M%2FflyjMEeqoidZS7xNwB9RZsyJK3jeqBD1esNBUHIgiSnCA4rp1WN%2BGLf53wodcMXYApMZ9k%2FwH4T%2BaUmQ%2FF9PxmnJr%2B%2FPZ%2BxMG%2BgV453S4KKst5IGuRIyE5a4qChB801fdfPBc9Cc%2F15zhrv4uK2sWP27Rj%2FkTBNPffbWnv3QTCjaOhlTllqdAu9JYvs3%2F%2F5jMlcG%2BE7m9B0iUkZJjqmPfXuYF9kanOS9jHFUsWuKQM11XBjNEZN9Aore7xCF%2F4t61Tk88o1Sdsdk9UZmLwBazqtLTpKUPiX3ix%2B%2BZfAnpONVhMQ1%2Fumol7rFMut1SvjjD5gNnfTn2sWEvH%2F420iWzTn5t1ymh%2BYvPOIQlSve60I%2B%2B7HBTxOPJB4rFZ6w1GXHyfSTbNDzWf0PAYGAaGbiE5BrnpjOUG%2BnPd%2F5zztIGfDKBnO4ncIz4SYi0LlEUFFwKYAyOvohOSMp9K%2BDb%2BHzyeof6CuNb7t3mgTZUAqeEif2lS4Sg%2BDi51UqQQvipIV8g%2B1Uw8InayAY6pgFKkUJIWjty5B4R%2BgoFPEgpjy5sb9ZeOS%2BhfoF0j84m4jE%2B8H9qJodZifEYHS8xmne27Ak3ZBr5GgAl38u%2Bpfusv4yzlyetrzS%2FhQ03NcXFs4YQiEGYBAamAn%2FqzZkVEr12qr6riFYIjcKUOSioT0%2FnIH%2FEc3NYxsVTgGkbrdj%2BdlnTokBO9DDf2pzpk%2Fy%2BBkceVNDBEuYrl7Jz4ujINxf1Uzkz8REz&X-Amz-Signature=dcc8c6d66dd62c64bb7dbe72288522a876d0f879124d4df7d9f8c3a4031e987c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRJIDGK7%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAZJTzHsxbFJw84TiLX1qsQKOvHUSk054zzBHoqKXauAiB6ssv6v%2F2rDSgq%2FIli2zQ1m73uBd1eSoY5bpORuR3vkyr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMRjEkm3P65PpU3xckKtwDVQiotsfpeIn%2F9w76vuTJlGJwAq29N6b7nQeUaBoYa%2B0nn2xplNQ7RKnS%2FGghH3jMhg0oxGrMsVa5JQGuxq%2FqERyrW%2FZRNOUHbcCzTjUAs1RrC9CrNV%2Fa7M%2FflyjMEeqoidZS7xNwB9RZsyJK3jeqBD1esNBUHIgiSnCA4rp1WN%2BGLf53wodcMXYApMZ9k%2FwH4T%2BaUmQ%2FF9PxmnJr%2B%2FPZ%2BxMG%2BgV453S4KKst5IGuRIyE5a4qChB801fdfPBc9Cc%2F15zhrv4uK2sWP27Rj%2FkTBNPffbWnv3QTCjaOhlTllqdAu9JYvs3%2F%2F5jMlcG%2BE7m9B0iUkZJjqmPfXuYF9kanOS9jHFUsWuKQM11XBjNEZN9Aore7xCF%2F4t61Tk88o1Sdsdk9UZmLwBazqtLTpKUPiX3ix%2B%2BZfAnpONVhMQ1%2Fumol7rFMut1SvjjD5gNnfTn2sWEvH%2F420iWzTn5t1ymh%2BYvPOIQlSve60I%2B%2B7HBTxOPJB4rFZ6w1GXHyfSTbNDzWf0PAYGAaGbiE5BrnpjOUG%2BnPd%2F5zztIGfDKBnO4ncIz4SYi0LlEUFFwKYAyOvohOSMp9K%2BDb%2BHzyeof6CuNb7t3mgTZUAqeEif2lS4Sg%2BDi51UqQQvipIV8g%2B1Uw8InayAY6pgFKkUJIWjty5B4R%2BgoFPEgpjy5sb9ZeOS%2BhfoF0j84m4jE%2B8H9qJodZifEYHS8xmne27Ak3ZBr5GgAl38u%2Bpfusv4yzlyetrzS%2FhQ03NcXFs4YQiEGYBAamAn%2FqzZkVEr12qr6riFYIjcKUOSioT0%2FnIH%2FEc3NYxsVTgGkbrdj%2BdlnTokBO9DDf2pzpk%2Fy%2BBkceVNDBEuYrl7Jz4ujINxf1Uzkz8REz&X-Amz-Signature=171ff207c7203fe516a4286e39d27f7ca36bb21422a6b32b7eb5a332e3aa86cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRJIDGK7%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAZJTzHsxbFJw84TiLX1qsQKOvHUSk054zzBHoqKXauAiB6ssv6v%2F2rDSgq%2FIli2zQ1m73uBd1eSoY5bpORuR3vkyr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMRjEkm3P65PpU3xckKtwDVQiotsfpeIn%2F9w76vuTJlGJwAq29N6b7nQeUaBoYa%2B0nn2xplNQ7RKnS%2FGghH3jMhg0oxGrMsVa5JQGuxq%2FqERyrW%2FZRNOUHbcCzTjUAs1RrC9CrNV%2Fa7M%2FflyjMEeqoidZS7xNwB9RZsyJK3jeqBD1esNBUHIgiSnCA4rp1WN%2BGLf53wodcMXYApMZ9k%2FwH4T%2BaUmQ%2FF9PxmnJr%2B%2FPZ%2BxMG%2BgV453S4KKst5IGuRIyE5a4qChB801fdfPBc9Cc%2F15zhrv4uK2sWP27Rj%2FkTBNPffbWnv3QTCjaOhlTllqdAu9JYvs3%2F%2F5jMlcG%2BE7m9B0iUkZJjqmPfXuYF9kanOS9jHFUsWuKQM11XBjNEZN9Aore7xCF%2F4t61Tk88o1Sdsdk9UZmLwBazqtLTpKUPiX3ix%2B%2BZfAnpONVhMQ1%2Fumol7rFMut1SvjjD5gNnfTn2sWEvH%2F420iWzTn5t1ymh%2BYvPOIQlSve60I%2B%2B7HBTxOPJB4rFZ6w1GXHyfSTbNDzWf0PAYGAaGbiE5BrnpjOUG%2BnPd%2F5zztIGfDKBnO4ncIz4SYi0LlEUFFwKYAyOvohOSMp9K%2BDb%2BHzyeof6CuNb7t3mgTZUAqeEif2lS4Sg%2BDi51UqQQvipIV8g%2B1Uw8InayAY6pgFKkUJIWjty5B4R%2BgoFPEgpjy5sb9ZeOS%2BhfoF0j84m4jE%2B8H9qJodZifEYHS8xmne27Ak3ZBr5GgAl38u%2Bpfusv4yzlyetrzS%2FhQ03NcXFs4YQiEGYBAamAn%2FqzZkVEr12qr6riFYIjcKUOSioT0%2FnIH%2FEc3NYxsVTgGkbrdj%2BdlnTokBO9DDf2pzpk%2Fy%2BBkceVNDBEuYrl7Jz4ujINxf1Uzkz8REz&X-Amz-Signature=d2f7cce1dcceb9d6dae21436e8806401dd9b252ec98e41053c5e74b804e46b94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



