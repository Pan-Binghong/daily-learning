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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6HZFNJP%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgR0bPzuwyR1rjnGIoVhjwsMAjr%2BvRMVPFMm94L%2BAFzgIhAKdxj%2F2UAqudt77n2UllFSj8F15oFKtNXCVch5nad4VSKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7GlHIf0b03bHPQLcq3AP6ihLIbsj6wz01ziz91RQhKMSDvgFckYXUsksbglMAyH%2Bj9ztONklu1p7IzWmtDSDcXl76OR1NT%2FaORg9FJk3cDPOinm19GEa%2BZHowQn0JanRNu0u9UpPxb3AR%2BTABtpoIwZ0ezX48tcSVA7oXihezylFep560AFA9Bt0DezJv1F7cPmZHsiPryWOizR1opspAIusS2lx9g5pyicuKjaCJ%2BEjunT0X20LGfNrSZeg889srhpZNc%2FDpNV2f3nRiZSDc8rhhpanPBZ14h83%2B5BogsCuDaSOwR039C%2FRUT%2BPuiM7YO9gCgjJmL3%2BliFUI0An758uNew4O4fgqp4EyW%2Ba%2F%2BibxGe%2BiEsrIu%2B3hvYM2DZXitYqyIA9PZyDl6LftNoAqZ1Lxs9T2sWDokE9Z2oK69i9izI%2BmRKPs2LnOfRarTcyGzzKZ5FVVSJRMVbsXvj5Tr7n%2FYvGIOsRQLoiTSryit99NGierK7GswjLAgrjU9%2FNNJ47s0sO3zxC8mPOuMuDwSbHwu83E1sMnV6CDP9cFH8uAYlW2lpRdSv2iCBq4u5I6YsjAIZ6JB8yz4if4psJN8A5j2dVOJMZIZNv2Vo2ROH%2BwA5HYl%2Fi%2FFoib9MNIfbtj%2BCHOnudEJdhkUTDAhurIBjqkAeZUGfox2tUkaTJUBE916JLxmzhJwsbyONtGp31b9CLb3sT5pgEKQboQIAwZCLZvbptbAypzxep%2FOYKo4ljdkEqIOqeGQWmBmP0y98BDIvN9qvjcxeeZT2Nq9YM4hn6Jto3DV9KVRFk13ol%2FnH851h0UfsIxOI%2BhaZh20aoWF0Juo8wj7zM%2B4fkWRO7ATG6YAi7P%2BoBJPyVYovdcugmCutmom82f&X-Amz-Signature=232adadf6ad53b063d4d4a77a148a3353d080c0a42647768c99a0f75fbea1567&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6HZFNJP%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgR0bPzuwyR1rjnGIoVhjwsMAjr%2BvRMVPFMm94L%2BAFzgIhAKdxj%2F2UAqudt77n2UllFSj8F15oFKtNXCVch5nad4VSKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7GlHIf0b03bHPQLcq3AP6ihLIbsj6wz01ziz91RQhKMSDvgFckYXUsksbglMAyH%2Bj9ztONklu1p7IzWmtDSDcXl76OR1NT%2FaORg9FJk3cDPOinm19GEa%2BZHowQn0JanRNu0u9UpPxb3AR%2BTABtpoIwZ0ezX48tcSVA7oXihezylFep560AFA9Bt0DezJv1F7cPmZHsiPryWOizR1opspAIusS2lx9g5pyicuKjaCJ%2BEjunT0X20LGfNrSZeg889srhpZNc%2FDpNV2f3nRiZSDc8rhhpanPBZ14h83%2B5BogsCuDaSOwR039C%2FRUT%2BPuiM7YO9gCgjJmL3%2BliFUI0An758uNew4O4fgqp4EyW%2Ba%2F%2BibxGe%2BiEsrIu%2B3hvYM2DZXitYqyIA9PZyDl6LftNoAqZ1Lxs9T2sWDokE9Z2oK69i9izI%2BmRKPs2LnOfRarTcyGzzKZ5FVVSJRMVbsXvj5Tr7n%2FYvGIOsRQLoiTSryit99NGierK7GswjLAgrjU9%2FNNJ47s0sO3zxC8mPOuMuDwSbHwu83E1sMnV6CDP9cFH8uAYlW2lpRdSv2iCBq4u5I6YsjAIZ6JB8yz4if4psJN8A5j2dVOJMZIZNv2Vo2ROH%2BwA5HYl%2Fi%2FFoib9MNIfbtj%2BCHOnudEJdhkUTDAhurIBjqkAeZUGfox2tUkaTJUBE916JLxmzhJwsbyONtGp31b9CLb3sT5pgEKQboQIAwZCLZvbptbAypzxep%2FOYKo4ljdkEqIOqeGQWmBmP0y98BDIvN9qvjcxeeZT2Nq9YM4hn6Jto3DV9KVRFk13ol%2FnH851h0UfsIxOI%2BhaZh20aoWF0Juo8wj7zM%2B4fkWRO7ATG6YAi7P%2BoBJPyVYovdcugmCutmom82f&X-Amz-Signature=3c0fbc93c9955940769be38978a5b8a6f73553236b4b63f4c7694415725843db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6HZFNJP%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgR0bPzuwyR1rjnGIoVhjwsMAjr%2BvRMVPFMm94L%2BAFzgIhAKdxj%2F2UAqudt77n2UllFSj8F15oFKtNXCVch5nad4VSKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7GlHIf0b03bHPQLcq3AP6ihLIbsj6wz01ziz91RQhKMSDvgFckYXUsksbglMAyH%2Bj9ztONklu1p7IzWmtDSDcXl76OR1NT%2FaORg9FJk3cDPOinm19GEa%2BZHowQn0JanRNu0u9UpPxb3AR%2BTABtpoIwZ0ezX48tcSVA7oXihezylFep560AFA9Bt0DezJv1F7cPmZHsiPryWOizR1opspAIusS2lx9g5pyicuKjaCJ%2BEjunT0X20LGfNrSZeg889srhpZNc%2FDpNV2f3nRiZSDc8rhhpanPBZ14h83%2B5BogsCuDaSOwR039C%2FRUT%2BPuiM7YO9gCgjJmL3%2BliFUI0An758uNew4O4fgqp4EyW%2Ba%2F%2BibxGe%2BiEsrIu%2B3hvYM2DZXitYqyIA9PZyDl6LftNoAqZ1Lxs9T2sWDokE9Z2oK69i9izI%2BmRKPs2LnOfRarTcyGzzKZ5FVVSJRMVbsXvj5Tr7n%2FYvGIOsRQLoiTSryit99NGierK7GswjLAgrjU9%2FNNJ47s0sO3zxC8mPOuMuDwSbHwu83E1sMnV6CDP9cFH8uAYlW2lpRdSv2iCBq4u5I6YsjAIZ6JB8yz4if4psJN8A5j2dVOJMZIZNv2Vo2ROH%2BwA5HYl%2Fi%2FFoib9MNIfbtj%2BCHOnudEJdhkUTDAhurIBjqkAeZUGfox2tUkaTJUBE916JLxmzhJwsbyONtGp31b9CLb3sT5pgEKQboQIAwZCLZvbptbAypzxep%2FOYKo4ljdkEqIOqeGQWmBmP0y98BDIvN9qvjcxeeZT2Nq9YM4hn6Jto3DV9KVRFk13ol%2FnH851h0UfsIxOI%2BhaZh20aoWF0Juo8wj7zM%2B4fkWRO7ATG6YAi7P%2BoBJPyVYovdcugmCutmom82f&X-Amz-Signature=6f2114d00829cbb0b168f3408a0d8f330e831c52f5ae72a4beaff39e8008b69f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6HZFNJP%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgR0bPzuwyR1rjnGIoVhjwsMAjr%2BvRMVPFMm94L%2BAFzgIhAKdxj%2F2UAqudt77n2UllFSj8F15oFKtNXCVch5nad4VSKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7GlHIf0b03bHPQLcq3AP6ihLIbsj6wz01ziz91RQhKMSDvgFckYXUsksbglMAyH%2Bj9ztONklu1p7IzWmtDSDcXl76OR1NT%2FaORg9FJk3cDPOinm19GEa%2BZHowQn0JanRNu0u9UpPxb3AR%2BTABtpoIwZ0ezX48tcSVA7oXihezylFep560AFA9Bt0DezJv1F7cPmZHsiPryWOizR1opspAIusS2lx9g5pyicuKjaCJ%2BEjunT0X20LGfNrSZeg889srhpZNc%2FDpNV2f3nRiZSDc8rhhpanPBZ14h83%2B5BogsCuDaSOwR039C%2FRUT%2BPuiM7YO9gCgjJmL3%2BliFUI0An758uNew4O4fgqp4EyW%2Ba%2F%2BibxGe%2BiEsrIu%2B3hvYM2DZXitYqyIA9PZyDl6LftNoAqZ1Lxs9T2sWDokE9Z2oK69i9izI%2BmRKPs2LnOfRarTcyGzzKZ5FVVSJRMVbsXvj5Tr7n%2FYvGIOsRQLoiTSryit99NGierK7GswjLAgrjU9%2FNNJ47s0sO3zxC8mPOuMuDwSbHwu83E1sMnV6CDP9cFH8uAYlW2lpRdSv2iCBq4u5I6YsjAIZ6JB8yz4if4psJN8A5j2dVOJMZIZNv2Vo2ROH%2BwA5HYl%2Fi%2FFoib9MNIfbtj%2BCHOnudEJdhkUTDAhurIBjqkAeZUGfox2tUkaTJUBE916JLxmzhJwsbyONtGp31b9CLb3sT5pgEKQboQIAwZCLZvbptbAypzxep%2FOYKo4ljdkEqIOqeGQWmBmP0y98BDIvN9qvjcxeeZT2Nq9YM4hn6Jto3DV9KVRFk13ol%2FnH851h0UfsIxOI%2BhaZh20aoWF0Juo8wj7zM%2B4fkWRO7ATG6YAi7P%2BoBJPyVYovdcugmCutmom82f&X-Amz-Signature=5bdf67b4a990d986f5c95c8aba4a670e03e78413629418dca426d81735d05527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



