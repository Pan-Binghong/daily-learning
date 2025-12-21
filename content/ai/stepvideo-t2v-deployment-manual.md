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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUJM6VS%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIBmmf27QtlecevfkHoZ8hT3nZwDTqiJPfyhDp7mS%2FKQNAiB55NN3PSFyvAcK2s7q165KPpEgGT5IftGhlZUqpdMp7yqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa5m6nPtemt2RdnMpKtwDUQOaTlaA4cGooBZrM5spULUBCNvoEFf%2FgwIG4FcPoe%2BUxTFFE9kZul5xyvISq5uJr23AjqWx7dSy3HWUYmjCDBsGsKTe4%2BDyIk9CHIdJMI2By1ZsNMm6WqtDxge0ioZjuyBPICZ7SrPVp%2BxOBtvcOOLSEIpb6JbxHCoa9Izpu9r9%2FNI62rR2pIF2VUMf1f1Sb46vlnZ0KqoyyGNUMdvJdbftXJWM5eqVPW3FkpCyx3orK6RbSW4pFbLf5qCIfm%2BNNj3zNfkCWI0iqsMhH%2BM97QdUxowwyy6k2%2FVaumJ2PhteNDFUxSTTvR%2FQbs4wKpzxo%2Fk32nXQg1SOPvULtGZQzAfmrTOVKh0kpeMbjG9Rz8t6TjwDSlFjfywcVB780p0qKQMJgvLLEhoF3E3JVaVWormS3eqPGD%2BiT8pRn1qf%2BnSc3mS1UUmRos1oQ%2Fa8AuBFsHS%2BAKAyuqVv9jbswPO81jG06Xp8Mz1Uy3DF23BG6IZGfVYpDkuQaZwcKyMOq8xU6qhakm8OqimvafFBpFn95el22BpbyCZ5W%2FmWFA%2BEBZ0zhQ0UjzVo4dAEIQ8ZtgS0ml8sAH4%2BmzS24b6P%2BoDhKUBRdkbgrSVd4%2BrSqM6U2RmPXDkQpdozqaaBvaAwuficygY6pgE4CZFwNJV9683%2BZvl4EptcffXinC2PPG%2FiGz9Xqyn1sfixki6PXXToa1C7UF9GawOtad3jwblOR3R4hsYTauWlVtOc5Kh6tvKQk1XjsEnU5zaHhF%2BGxlbkPadNqoEZDH0Hdy4agM3POngt11egUIqnEC4NZFt5t6Dm1xvGxxIFsvXZwXiHiY4mGsD5pEn%2F65eX5G6OU1J1K41kQWr2ANzE%2Fs%2F3pkJ9&X-Amz-Signature=44f4db019e672d97e25476e4803325185a3cf3bc3a038341df70653936ff9121&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUJM6VS%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIBmmf27QtlecevfkHoZ8hT3nZwDTqiJPfyhDp7mS%2FKQNAiB55NN3PSFyvAcK2s7q165KPpEgGT5IftGhlZUqpdMp7yqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa5m6nPtemt2RdnMpKtwDUQOaTlaA4cGooBZrM5spULUBCNvoEFf%2FgwIG4FcPoe%2BUxTFFE9kZul5xyvISq5uJr23AjqWx7dSy3HWUYmjCDBsGsKTe4%2BDyIk9CHIdJMI2By1ZsNMm6WqtDxge0ioZjuyBPICZ7SrPVp%2BxOBtvcOOLSEIpb6JbxHCoa9Izpu9r9%2FNI62rR2pIF2VUMf1f1Sb46vlnZ0KqoyyGNUMdvJdbftXJWM5eqVPW3FkpCyx3orK6RbSW4pFbLf5qCIfm%2BNNj3zNfkCWI0iqsMhH%2BM97QdUxowwyy6k2%2FVaumJ2PhteNDFUxSTTvR%2FQbs4wKpzxo%2Fk32nXQg1SOPvULtGZQzAfmrTOVKh0kpeMbjG9Rz8t6TjwDSlFjfywcVB780p0qKQMJgvLLEhoF3E3JVaVWormS3eqPGD%2BiT8pRn1qf%2BnSc3mS1UUmRos1oQ%2Fa8AuBFsHS%2BAKAyuqVv9jbswPO81jG06Xp8Mz1Uy3DF23BG6IZGfVYpDkuQaZwcKyMOq8xU6qhakm8OqimvafFBpFn95el22BpbyCZ5W%2FmWFA%2BEBZ0zhQ0UjzVo4dAEIQ8ZtgS0ml8sAH4%2BmzS24b6P%2BoDhKUBRdkbgrSVd4%2BrSqM6U2RmPXDkQpdozqaaBvaAwuficygY6pgE4CZFwNJV9683%2BZvl4EptcffXinC2PPG%2FiGz9Xqyn1sfixki6PXXToa1C7UF9GawOtad3jwblOR3R4hsYTauWlVtOc5Kh6tvKQk1XjsEnU5zaHhF%2BGxlbkPadNqoEZDH0Hdy4agM3POngt11egUIqnEC4NZFt5t6Dm1xvGxxIFsvXZwXiHiY4mGsD5pEn%2F65eX5G6OU1J1K41kQWr2ANzE%2Fs%2F3pkJ9&X-Amz-Signature=a53d3d706554b89d32aff8d77e97ab9973896e0d2b2772c2233cb0241f3a7860&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUJM6VS%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIBmmf27QtlecevfkHoZ8hT3nZwDTqiJPfyhDp7mS%2FKQNAiB55NN3PSFyvAcK2s7q165KPpEgGT5IftGhlZUqpdMp7yqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa5m6nPtemt2RdnMpKtwDUQOaTlaA4cGooBZrM5spULUBCNvoEFf%2FgwIG4FcPoe%2BUxTFFE9kZul5xyvISq5uJr23AjqWx7dSy3HWUYmjCDBsGsKTe4%2BDyIk9CHIdJMI2By1ZsNMm6WqtDxge0ioZjuyBPICZ7SrPVp%2BxOBtvcOOLSEIpb6JbxHCoa9Izpu9r9%2FNI62rR2pIF2VUMf1f1Sb46vlnZ0KqoyyGNUMdvJdbftXJWM5eqVPW3FkpCyx3orK6RbSW4pFbLf5qCIfm%2BNNj3zNfkCWI0iqsMhH%2BM97QdUxowwyy6k2%2FVaumJ2PhteNDFUxSTTvR%2FQbs4wKpzxo%2Fk32nXQg1SOPvULtGZQzAfmrTOVKh0kpeMbjG9Rz8t6TjwDSlFjfywcVB780p0qKQMJgvLLEhoF3E3JVaVWormS3eqPGD%2BiT8pRn1qf%2BnSc3mS1UUmRos1oQ%2Fa8AuBFsHS%2BAKAyuqVv9jbswPO81jG06Xp8Mz1Uy3DF23BG6IZGfVYpDkuQaZwcKyMOq8xU6qhakm8OqimvafFBpFn95el22BpbyCZ5W%2FmWFA%2BEBZ0zhQ0UjzVo4dAEIQ8ZtgS0ml8sAH4%2BmzS24b6P%2BoDhKUBRdkbgrSVd4%2BrSqM6U2RmPXDkQpdozqaaBvaAwuficygY6pgE4CZFwNJV9683%2BZvl4EptcffXinC2PPG%2FiGz9Xqyn1sfixki6PXXToa1C7UF9GawOtad3jwblOR3R4hsYTauWlVtOc5Kh6tvKQk1XjsEnU5zaHhF%2BGxlbkPadNqoEZDH0Hdy4agM3POngt11egUIqnEC4NZFt5t6Dm1xvGxxIFsvXZwXiHiY4mGsD5pEn%2F65eX5G6OU1J1K41kQWr2ANzE%2Fs%2F3pkJ9&X-Amz-Signature=965f886da91051203b041bbd60dee8089d4a2dafca93738d0227775b4d16b34b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQUJM6VS%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIBmmf27QtlecevfkHoZ8hT3nZwDTqiJPfyhDp7mS%2FKQNAiB55NN3PSFyvAcK2s7q165KPpEgGT5IftGhlZUqpdMp7yqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMa5m6nPtemt2RdnMpKtwDUQOaTlaA4cGooBZrM5spULUBCNvoEFf%2FgwIG4FcPoe%2BUxTFFE9kZul5xyvISq5uJr23AjqWx7dSy3HWUYmjCDBsGsKTe4%2BDyIk9CHIdJMI2By1ZsNMm6WqtDxge0ioZjuyBPICZ7SrPVp%2BxOBtvcOOLSEIpb6JbxHCoa9Izpu9r9%2FNI62rR2pIF2VUMf1f1Sb46vlnZ0KqoyyGNUMdvJdbftXJWM5eqVPW3FkpCyx3orK6RbSW4pFbLf5qCIfm%2BNNj3zNfkCWI0iqsMhH%2BM97QdUxowwyy6k2%2FVaumJ2PhteNDFUxSTTvR%2FQbs4wKpzxo%2Fk32nXQg1SOPvULtGZQzAfmrTOVKh0kpeMbjG9Rz8t6TjwDSlFjfywcVB780p0qKQMJgvLLEhoF3E3JVaVWormS3eqPGD%2BiT8pRn1qf%2BnSc3mS1UUmRos1oQ%2Fa8AuBFsHS%2BAKAyuqVv9jbswPO81jG06Xp8Mz1Uy3DF23BG6IZGfVYpDkuQaZwcKyMOq8xU6qhakm8OqimvafFBpFn95el22BpbyCZ5W%2FmWFA%2BEBZ0zhQ0UjzVo4dAEIQ8ZtgS0ml8sAH4%2BmzS24b6P%2BoDhKUBRdkbgrSVd4%2BrSqM6U2RmPXDkQpdozqaaBvaAwuficygY6pgE4CZFwNJV9683%2BZvl4EptcffXinC2PPG%2FiGz9Xqyn1sfixki6PXXToa1C7UF9GawOtad3jwblOR3R4hsYTauWlVtOc5Kh6tvKQk1XjsEnU5zaHhF%2BGxlbkPadNqoEZDH0Hdy4agM3POngt11egUIqnEC4NZFt5t6Dm1xvGxxIFsvXZwXiHiY4mGsD5pEn%2F65eX5G6OU1J1K41kQWr2ANzE%2Fs%2F3pkJ9&X-Amz-Signature=d61524ea2366d1da7bddc831dce79f6e2b326c7fccd502973b23c4db9cae54ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



