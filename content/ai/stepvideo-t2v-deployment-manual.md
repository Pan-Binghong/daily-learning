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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VKFC3VD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDTbWTp36iE60UxOlLWW7wupkRSsIWno%2F6x2nGCxw9ULAiA0QaoSRh0rbMlG5IwrKdBPoTlV3kaXap2vDzc%2BvZkc3yqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMPwQx00yduIFB2FRKtwDo1Ghn7glo1TjLHiEUxLY2GCwa3yJa5Ozx20Y94%2Be%2BTkJ6ARYeJ4%2BSCVDOYjFn6POg%2FhNtIbcqKYTQR7bVHwkDQhcSyvV9O%2F7DWolbbbvsAWTj09fyB7Jvl8FWdAuINyT37W5klkFU1H2FUXm5p1YUVVxguOm0l4Nv5Iuirh2AlC9%2F5hRTundnHhzhbBzH%2FMAv0Tt%2B9kI4jgqY%2B5%2FO1cK3TCsDFatVDuc8zes5Duzm2q4mhtAefMEVPkunL8uRjNhafN%2FRzB3DsUP1OpCw%2BEDIPS4MGvncDloFsKJYZz5VbhvJ0ATPkWtdcWMz3Vw4NeAfiSUDKIq8jen5oElCwzjy4fkpZVs79rbXh5YIvkfoDumsS8Rokb0BwRUvDuaZn6Df3E2nW6wVbAgLJx22OXPf4puJ%2FNNdm7dBjI8BG9g63U0Wbls1%2FrF2R%2B%2FrjzKVanijzZKpJN4SrAJJJ8Jo30F1XdcafxZa0h6okD4jy0QPGpy4YHQX0wWqc0K4v5ebV0UCbS2tRw3i2pPRHkguSpVUOWIsrHrGUWfP4Dkhkf6rI0BmhtFeI%2FjvLzZvKSELmZ5ydFh4VLvoslQOlh7x73jvA86RvK9sqMycDBBZ2XbWQw%2F%2BNN9sWPTQyiuJt8wr8nwywY6pgE2r8Gf9%2Bq9ePy%2F8Nm3ekyWFVhsEuWQZibR5sd4p%2FiKl1veLyzBfs5QO62RXGE8NsFBW7CM0OBkR5hPIOYCbRTHOXO4s8J4kRltQVTG%2F21ngpGAHqWw2pIcBpFuoAoL08zFcugxj0KwRXyl%2FgvH87N4P5Qi%2F7bnQiWu8CYOC2TPcIHJmRDul9a3RCeKSHM3a7gBvI5vvop6N9BKbiT6xdoEVauk%2FJBe&X-Amz-Signature=ae15e6e346680ef63480a7a3a064faee2619552203ea6605ef6fba1e92b9fb4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VKFC3VD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDTbWTp36iE60UxOlLWW7wupkRSsIWno%2F6x2nGCxw9ULAiA0QaoSRh0rbMlG5IwrKdBPoTlV3kaXap2vDzc%2BvZkc3yqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMPwQx00yduIFB2FRKtwDo1Ghn7glo1TjLHiEUxLY2GCwa3yJa5Ozx20Y94%2Be%2BTkJ6ARYeJ4%2BSCVDOYjFn6POg%2FhNtIbcqKYTQR7bVHwkDQhcSyvV9O%2F7DWolbbbvsAWTj09fyB7Jvl8FWdAuINyT37W5klkFU1H2FUXm5p1YUVVxguOm0l4Nv5Iuirh2AlC9%2F5hRTundnHhzhbBzH%2FMAv0Tt%2B9kI4jgqY%2B5%2FO1cK3TCsDFatVDuc8zes5Duzm2q4mhtAefMEVPkunL8uRjNhafN%2FRzB3DsUP1OpCw%2BEDIPS4MGvncDloFsKJYZz5VbhvJ0ATPkWtdcWMz3Vw4NeAfiSUDKIq8jen5oElCwzjy4fkpZVs79rbXh5YIvkfoDumsS8Rokb0BwRUvDuaZn6Df3E2nW6wVbAgLJx22OXPf4puJ%2FNNdm7dBjI8BG9g63U0Wbls1%2FrF2R%2B%2FrjzKVanijzZKpJN4SrAJJJ8Jo30F1XdcafxZa0h6okD4jy0QPGpy4YHQX0wWqc0K4v5ebV0UCbS2tRw3i2pPRHkguSpVUOWIsrHrGUWfP4Dkhkf6rI0BmhtFeI%2FjvLzZvKSELmZ5ydFh4VLvoslQOlh7x73jvA86RvK9sqMycDBBZ2XbWQw%2F%2BNN9sWPTQyiuJt8wr8nwywY6pgE2r8Gf9%2Bq9ePy%2F8Nm3ekyWFVhsEuWQZibR5sd4p%2FiKl1veLyzBfs5QO62RXGE8NsFBW7CM0OBkR5hPIOYCbRTHOXO4s8J4kRltQVTG%2F21ngpGAHqWw2pIcBpFuoAoL08zFcugxj0KwRXyl%2FgvH87N4P5Qi%2F7bnQiWu8CYOC2TPcIHJmRDul9a3RCeKSHM3a7gBvI5vvop6N9BKbiT6xdoEVauk%2FJBe&X-Amz-Signature=381b1af816e1e1b4a6d9d74af24e7ec2986816fc86ff597b24dd114a3e88de99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VKFC3VD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDTbWTp36iE60UxOlLWW7wupkRSsIWno%2F6x2nGCxw9ULAiA0QaoSRh0rbMlG5IwrKdBPoTlV3kaXap2vDzc%2BvZkc3yqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMPwQx00yduIFB2FRKtwDo1Ghn7glo1TjLHiEUxLY2GCwa3yJa5Ozx20Y94%2Be%2BTkJ6ARYeJ4%2BSCVDOYjFn6POg%2FhNtIbcqKYTQR7bVHwkDQhcSyvV9O%2F7DWolbbbvsAWTj09fyB7Jvl8FWdAuINyT37W5klkFU1H2FUXm5p1YUVVxguOm0l4Nv5Iuirh2AlC9%2F5hRTundnHhzhbBzH%2FMAv0Tt%2B9kI4jgqY%2B5%2FO1cK3TCsDFatVDuc8zes5Duzm2q4mhtAefMEVPkunL8uRjNhafN%2FRzB3DsUP1OpCw%2BEDIPS4MGvncDloFsKJYZz5VbhvJ0ATPkWtdcWMz3Vw4NeAfiSUDKIq8jen5oElCwzjy4fkpZVs79rbXh5YIvkfoDumsS8Rokb0BwRUvDuaZn6Df3E2nW6wVbAgLJx22OXPf4puJ%2FNNdm7dBjI8BG9g63U0Wbls1%2FrF2R%2B%2FrjzKVanijzZKpJN4SrAJJJ8Jo30F1XdcafxZa0h6okD4jy0QPGpy4YHQX0wWqc0K4v5ebV0UCbS2tRw3i2pPRHkguSpVUOWIsrHrGUWfP4Dkhkf6rI0BmhtFeI%2FjvLzZvKSELmZ5ydFh4VLvoslQOlh7x73jvA86RvK9sqMycDBBZ2XbWQw%2F%2BNN9sWPTQyiuJt8wr8nwywY6pgE2r8Gf9%2Bq9ePy%2F8Nm3ekyWFVhsEuWQZibR5sd4p%2FiKl1veLyzBfs5QO62RXGE8NsFBW7CM0OBkR5hPIOYCbRTHOXO4s8J4kRltQVTG%2F21ngpGAHqWw2pIcBpFuoAoL08zFcugxj0KwRXyl%2FgvH87N4P5Qi%2F7bnQiWu8CYOC2TPcIHJmRDul9a3RCeKSHM3a7gBvI5vvop6N9BKbiT6xdoEVauk%2FJBe&X-Amz-Signature=e7bc83501d75e346d00e6e7607ffbc9a0f8c4e20790be08b3e2dac7e6cb64525&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VKFC3VD%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDTbWTp36iE60UxOlLWW7wupkRSsIWno%2F6x2nGCxw9ULAiA0QaoSRh0rbMlG5IwrKdBPoTlV3kaXap2vDzc%2BvZkc3yqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMPwQx00yduIFB2FRKtwDo1Ghn7glo1TjLHiEUxLY2GCwa3yJa5Ozx20Y94%2Be%2BTkJ6ARYeJ4%2BSCVDOYjFn6POg%2FhNtIbcqKYTQR7bVHwkDQhcSyvV9O%2F7DWolbbbvsAWTj09fyB7Jvl8FWdAuINyT37W5klkFU1H2FUXm5p1YUVVxguOm0l4Nv5Iuirh2AlC9%2F5hRTundnHhzhbBzH%2FMAv0Tt%2B9kI4jgqY%2B5%2FO1cK3TCsDFatVDuc8zes5Duzm2q4mhtAefMEVPkunL8uRjNhafN%2FRzB3DsUP1OpCw%2BEDIPS4MGvncDloFsKJYZz5VbhvJ0ATPkWtdcWMz3Vw4NeAfiSUDKIq8jen5oElCwzjy4fkpZVs79rbXh5YIvkfoDumsS8Rokb0BwRUvDuaZn6Df3E2nW6wVbAgLJx22OXPf4puJ%2FNNdm7dBjI8BG9g63U0Wbls1%2FrF2R%2B%2FrjzKVanijzZKpJN4SrAJJJ8Jo30F1XdcafxZa0h6okD4jy0QPGpy4YHQX0wWqc0K4v5ebV0UCbS2tRw3i2pPRHkguSpVUOWIsrHrGUWfP4Dkhkf6rI0BmhtFeI%2FjvLzZvKSELmZ5ydFh4VLvoslQOlh7x73jvA86RvK9sqMycDBBZ2XbWQw%2F%2BNN9sWPTQyiuJt8wr8nwywY6pgE2r8Gf9%2Bq9ePy%2F8Nm3ekyWFVhsEuWQZibR5sd4p%2FiKl1veLyzBfs5QO62RXGE8NsFBW7CM0OBkR5hPIOYCbRTHOXO4s8J4kRltQVTG%2F21ngpGAHqWw2pIcBpFuoAoL08zFcugxj0KwRXyl%2FgvH87N4P5Qi%2F7bnQiWu8CYOC2TPcIHJmRDul9a3RCeKSHM3a7gBvI5vvop6N9BKbiT6xdoEVauk%2FJBe&X-Amz-Signature=a3b7d9e33ade56162f58a9d93bbf366f2db25098350b2e627788a7816df68395&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



