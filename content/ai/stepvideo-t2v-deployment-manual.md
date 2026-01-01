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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHFLOAM%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIG49Z%2BcpY%2FAguQWf4FLsrekP6owKm9JCeRq%2Fl9CjuklkAiEAqyk%2FNmgU%2F%2BNeIufFZ3bj5O3om7RQABSrRO8HaCgKR2sqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB39Jd9Rt%2BcnOGEMircAySrqsRiZoRIkju56qexOZWydbEsBS0opL4sziZFlPsr7ln1vvs8EquIiHo3RwIvhzk5hlqQ7Ip6v0KDoyB%2BA4xwMl4mRh78903zk3CjXpCW27%2F7EEsizCapE%2Flil6ZodzGC%2BEMpxsJ8HpNwNej0aKikwx7s9E3Gh6bDjjLb%2BNpuPZpxidOzpbckKeRdzLW2N5xCFf563IV0NhkuHGgfF4sKifsuvAwnj5Y6O1vAa1BXXoS2AQ8ZPM1mTR8cFT3Vz6lc4mEeSvO70Yn9eZdeHP8MuT%2FlaPPXjlK64aKeRCvctw7kM3bBhcAtAbh%2FjoizHHW9FK0%2F%2FKmPGG7IzjfW%2BpLzYPoRixNgPaEvCXQXfcNlz4XCLFw5Ai7FJQVbQrWGl3PzxTCPU5l53%2BH%2Fxh18KwG%2BJDkb0Z3LFpfbNyHDRD9HEryVuweSJ6OYxtZXC2X14E6J42e1g3jT8zmJDrXhbvqkxqhz3%2FFl2lzK2KgxPwfceWuuDZz4NHkrp8h%2FZFFp1HX5oJGzmZMmDBbPOpy4oaWnJeDeHSOiOOEl3XkxXHArbjakZAh%2Fj%2Bx776DwDzFSJdpqd8SMcH7FgRTvWHrqUUbAT9QEqAYnhxAwYx7h0JJcIx8uxmaG3vyOTTGRMIWa18oGOqUBQkcW9SccS9KYwxoAf0rDWRY2eF0Dxzm5%2BHN19%2BVtQYgfcZtK887mAbikue3AdR9sdGq%2FpE1D9XBu%2FGCLDZK3tR4pMcXsXGJrxB1SvTAFCbC7IjqoAeCAgwx6UG4XlSvxvoc4Gar4yqONcmOiR56XNgPdYpfpWxx7eH3fLSdeItJMD8Hgs7v3AEdkE7pNmGGPv6%2Bhy54OP9BM0%2FC6mqeKd0VWrTaL&X-Amz-Signature=d53e2fc21f9b846262b405552cd33e9ac9df437541645055d107d848bbb7abce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHFLOAM%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIG49Z%2BcpY%2FAguQWf4FLsrekP6owKm9JCeRq%2Fl9CjuklkAiEAqyk%2FNmgU%2F%2BNeIufFZ3bj5O3om7RQABSrRO8HaCgKR2sqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB39Jd9Rt%2BcnOGEMircAySrqsRiZoRIkju56qexOZWydbEsBS0opL4sziZFlPsr7ln1vvs8EquIiHo3RwIvhzk5hlqQ7Ip6v0KDoyB%2BA4xwMl4mRh78903zk3CjXpCW27%2F7EEsizCapE%2Flil6ZodzGC%2BEMpxsJ8HpNwNej0aKikwx7s9E3Gh6bDjjLb%2BNpuPZpxidOzpbckKeRdzLW2N5xCFf563IV0NhkuHGgfF4sKifsuvAwnj5Y6O1vAa1BXXoS2AQ8ZPM1mTR8cFT3Vz6lc4mEeSvO70Yn9eZdeHP8MuT%2FlaPPXjlK64aKeRCvctw7kM3bBhcAtAbh%2FjoizHHW9FK0%2F%2FKmPGG7IzjfW%2BpLzYPoRixNgPaEvCXQXfcNlz4XCLFw5Ai7FJQVbQrWGl3PzxTCPU5l53%2BH%2Fxh18KwG%2BJDkb0Z3LFpfbNyHDRD9HEryVuweSJ6OYxtZXC2X14E6J42e1g3jT8zmJDrXhbvqkxqhz3%2FFl2lzK2KgxPwfceWuuDZz4NHkrp8h%2FZFFp1HX5oJGzmZMmDBbPOpy4oaWnJeDeHSOiOOEl3XkxXHArbjakZAh%2Fj%2Bx776DwDzFSJdpqd8SMcH7FgRTvWHrqUUbAT9QEqAYnhxAwYx7h0JJcIx8uxmaG3vyOTTGRMIWa18oGOqUBQkcW9SccS9KYwxoAf0rDWRY2eF0Dxzm5%2BHN19%2BVtQYgfcZtK887mAbikue3AdR9sdGq%2FpE1D9XBu%2FGCLDZK3tR4pMcXsXGJrxB1SvTAFCbC7IjqoAeCAgwx6UG4XlSvxvoc4Gar4yqONcmOiR56XNgPdYpfpWxx7eH3fLSdeItJMD8Hgs7v3AEdkE7pNmGGPv6%2Bhy54OP9BM0%2FC6mqeKd0VWrTaL&X-Amz-Signature=612df979527f3c66c0fcfb3efe4a39d7215915a85493088c2bfa951dfa3f6a68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHFLOAM%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIG49Z%2BcpY%2FAguQWf4FLsrekP6owKm9JCeRq%2Fl9CjuklkAiEAqyk%2FNmgU%2F%2BNeIufFZ3bj5O3om7RQABSrRO8HaCgKR2sqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB39Jd9Rt%2BcnOGEMircAySrqsRiZoRIkju56qexOZWydbEsBS0opL4sziZFlPsr7ln1vvs8EquIiHo3RwIvhzk5hlqQ7Ip6v0KDoyB%2BA4xwMl4mRh78903zk3CjXpCW27%2F7EEsizCapE%2Flil6ZodzGC%2BEMpxsJ8HpNwNej0aKikwx7s9E3Gh6bDjjLb%2BNpuPZpxidOzpbckKeRdzLW2N5xCFf563IV0NhkuHGgfF4sKifsuvAwnj5Y6O1vAa1BXXoS2AQ8ZPM1mTR8cFT3Vz6lc4mEeSvO70Yn9eZdeHP8MuT%2FlaPPXjlK64aKeRCvctw7kM3bBhcAtAbh%2FjoizHHW9FK0%2F%2FKmPGG7IzjfW%2BpLzYPoRixNgPaEvCXQXfcNlz4XCLFw5Ai7FJQVbQrWGl3PzxTCPU5l53%2BH%2Fxh18KwG%2BJDkb0Z3LFpfbNyHDRD9HEryVuweSJ6OYxtZXC2X14E6J42e1g3jT8zmJDrXhbvqkxqhz3%2FFl2lzK2KgxPwfceWuuDZz4NHkrp8h%2FZFFp1HX5oJGzmZMmDBbPOpy4oaWnJeDeHSOiOOEl3XkxXHArbjakZAh%2Fj%2Bx776DwDzFSJdpqd8SMcH7FgRTvWHrqUUbAT9QEqAYnhxAwYx7h0JJcIx8uxmaG3vyOTTGRMIWa18oGOqUBQkcW9SccS9KYwxoAf0rDWRY2eF0Dxzm5%2BHN19%2BVtQYgfcZtK887mAbikue3AdR9sdGq%2FpE1D9XBu%2FGCLDZK3tR4pMcXsXGJrxB1SvTAFCbC7IjqoAeCAgwx6UG4XlSvxvoc4Gar4yqONcmOiR56XNgPdYpfpWxx7eH3fLSdeItJMD8Hgs7v3AEdkE7pNmGGPv6%2Bhy54OP9BM0%2FC6mqeKd0VWrTaL&X-Amz-Signature=87e63ed8cc113719be65609388a8c6d6eadc4344da4b40866552f92975829ab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYHFLOAM%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIG49Z%2BcpY%2FAguQWf4FLsrekP6owKm9JCeRq%2Fl9CjuklkAiEAqyk%2FNmgU%2F%2BNeIufFZ3bj5O3om7RQABSrRO8HaCgKR2sqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB39Jd9Rt%2BcnOGEMircAySrqsRiZoRIkju56qexOZWydbEsBS0opL4sziZFlPsr7ln1vvs8EquIiHo3RwIvhzk5hlqQ7Ip6v0KDoyB%2BA4xwMl4mRh78903zk3CjXpCW27%2F7EEsizCapE%2Flil6ZodzGC%2BEMpxsJ8HpNwNej0aKikwx7s9E3Gh6bDjjLb%2BNpuPZpxidOzpbckKeRdzLW2N5xCFf563IV0NhkuHGgfF4sKifsuvAwnj5Y6O1vAa1BXXoS2AQ8ZPM1mTR8cFT3Vz6lc4mEeSvO70Yn9eZdeHP8MuT%2FlaPPXjlK64aKeRCvctw7kM3bBhcAtAbh%2FjoizHHW9FK0%2F%2FKmPGG7IzjfW%2BpLzYPoRixNgPaEvCXQXfcNlz4XCLFw5Ai7FJQVbQrWGl3PzxTCPU5l53%2BH%2Fxh18KwG%2BJDkb0Z3LFpfbNyHDRD9HEryVuweSJ6OYxtZXC2X14E6J42e1g3jT8zmJDrXhbvqkxqhz3%2FFl2lzK2KgxPwfceWuuDZz4NHkrp8h%2FZFFp1HX5oJGzmZMmDBbPOpy4oaWnJeDeHSOiOOEl3XkxXHArbjakZAh%2Fj%2Bx776DwDzFSJdpqd8SMcH7FgRTvWHrqUUbAT9QEqAYnhxAwYx7h0JJcIx8uxmaG3vyOTTGRMIWa18oGOqUBQkcW9SccS9KYwxoAf0rDWRY2eF0Dxzm5%2BHN19%2BVtQYgfcZtK887mAbikue3AdR9sdGq%2FpE1D9XBu%2FGCLDZK3tR4pMcXsXGJrxB1SvTAFCbC7IjqoAeCAgwx6UG4XlSvxvoc4Gar4yqONcmOiR56XNgPdYpfpWxx7eH3fLSdeItJMD8Hgs7v3AEdkE7pNmGGPv6%2Bhy54OP9BM0%2FC6mqeKd0VWrTaL&X-Amz-Signature=72fcd75f4e4b9deb9dc8c7813d21272215efbb200846fde81b4bfd621f52d0eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



