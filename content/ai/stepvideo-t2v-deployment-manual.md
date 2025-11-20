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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKNTYAPX%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIDs3vIYHmYBB8maZulakWawtpalEG8v3rukbHAr9IEdrAiBZFX90ZJ4W%2FXMhPFGoYh0AX%2FL8F4miJGoZI%2BzQQNm8bSqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT289RTQQBmWCxb7jKtwDOUAR03cD%2BDcbid2KzGIiN%2FgkFSHCkCFL%2FVgUUD72Agy%2FvY6tgI8FSddyIt0pcQb%2BNigazs%2BAsvBFpu589nc6aNHZPwMWeMV7RjujcMRbljpX9iagzzm%2B41lnHi%2B7TSmQYlU2QZPqI9vmTYh2Db6Pl8uiqcR%2F4Mu8m7weN9cNtiOUhqahQk5WiYU1fvnkTdyA06nJbaaxS1POYSk7mdZcPQMPQg8q1oIYxKAEZKgp86QcKJ%2BRhTiUNG2OZicopCfLgG2bPzeZiY0YrJZhJ7e6ewoJ4HTlw6miy2YNHiqPQxEzyZjaS0gkSJ4UB%2BmQdOLXZFEO9vGYbtJrQ7l80RVn7gjkUAdN%2F%2BQZdUAeh8lRi%2FsEINI05gI4M7dsOf2B2OaMSoO1U4lHeN9%2FQsOCHsQ46DyLAUzyXIOQo8P8cLqZIGa%2F7uxDwhXbamoMFrAU5Zingwg6%2F8TcFU2rz%2B0umTr6af2h4qVPC%2Fi2LBZVAS8CFX2u3AWEJ7LVw5liP53XYDWq%2Bl%2FUZJuV4PTCQhVci54A4HiUNd66xnnTsyQtCBASsK%2FzsC131OEvF006m3clCx5DI3goe%2F6TFXSBaobZWUmQeaenwNcT7a58pqVAcWwmpN07FBCsoYOR%2FCL0qxMwnuv5yAY6pgEkigqi3u7qNBh%2Bt7gpM7H25kDJk6hc5rJv31E5viuKc%2Byw5m6kv0v9l5PCbaqsu%2F32ZQrpNqw9qAWaB45ONaUI6rTIHTJdavl4Fy4NvimFJe7WQcAuOjFnkNebpDf1pSjQtMvtS%2FlIh7pretEpCG2CXyn%2BxqPKgNVFbEgbict3p0%2BROnogA5CWfH2T%2BlCsPHHSh8qpsgM9p6%2FGFJLHEofJnDHfm44p&X-Amz-Signature=fcc4fc90cd1cca0aaba038f03849960bf8c7378c76e5dd9b3f5560b75e79c29f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKNTYAPX%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIDs3vIYHmYBB8maZulakWawtpalEG8v3rukbHAr9IEdrAiBZFX90ZJ4W%2FXMhPFGoYh0AX%2FL8F4miJGoZI%2BzQQNm8bSqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT289RTQQBmWCxb7jKtwDOUAR03cD%2BDcbid2KzGIiN%2FgkFSHCkCFL%2FVgUUD72Agy%2FvY6tgI8FSddyIt0pcQb%2BNigazs%2BAsvBFpu589nc6aNHZPwMWeMV7RjujcMRbljpX9iagzzm%2B41lnHi%2B7TSmQYlU2QZPqI9vmTYh2Db6Pl8uiqcR%2F4Mu8m7weN9cNtiOUhqahQk5WiYU1fvnkTdyA06nJbaaxS1POYSk7mdZcPQMPQg8q1oIYxKAEZKgp86QcKJ%2BRhTiUNG2OZicopCfLgG2bPzeZiY0YrJZhJ7e6ewoJ4HTlw6miy2YNHiqPQxEzyZjaS0gkSJ4UB%2BmQdOLXZFEO9vGYbtJrQ7l80RVn7gjkUAdN%2F%2BQZdUAeh8lRi%2FsEINI05gI4M7dsOf2B2OaMSoO1U4lHeN9%2FQsOCHsQ46DyLAUzyXIOQo8P8cLqZIGa%2F7uxDwhXbamoMFrAU5Zingwg6%2F8TcFU2rz%2B0umTr6af2h4qVPC%2Fi2LBZVAS8CFX2u3AWEJ7LVw5liP53XYDWq%2Bl%2FUZJuV4PTCQhVci54A4HiUNd66xnnTsyQtCBASsK%2FzsC131OEvF006m3clCx5DI3goe%2F6TFXSBaobZWUmQeaenwNcT7a58pqVAcWwmpN07FBCsoYOR%2FCL0qxMwnuv5yAY6pgEkigqi3u7qNBh%2Bt7gpM7H25kDJk6hc5rJv31E5viuKc%2Byw5m6kv0v9l5PCbaqsu%2F32ZQrpNqw9qAWaB45ONaUI6rTIHTJdavl4Fy4NvimFJe7WQcAuOjFnkNebpDf1pSjQtMvtS%2FlIh7pretEpCG2CXyn%2BxqPKgNVFbEgbict3p0%2BROnogA5CWfH2T%2BlCsPHHSh8qpsgM9p6%2FGFJLHEofJnDHfm44p&X-Amz-Signature=5af248c652619ced29c2579e6a7784327a7668020dd644ce6ebb85c1e9ae4711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKNTYAPX%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIDs3vIYHmYBB8maZulakWawtpalEG8v3rukbHAr9IEdrAiBZFX90ZJ4W%2FXMhPFGoYh0AX%2FL8F4miJGoZI%2BzQQNm8bSqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT289RTQQBmWCxb7jKtwDOUAR03cD%2BDcbid2KzGIiN%2FgkFSHCkCFL%2FVgUUD72Agy%2FvY6tgI8FSddyIt0pcQb%2BNigazs%2BAsvBFpu589nc6aNHZPwMWeMV7RjujcMRbljpX9iagzzm%2B41lnHi%2B7TSmQYlU2QZPqI9vmTYh2Db6Pl8uiqcR%2F4Mu8m7weN9cNtiOUhqahQk5WiYU1fvnkTdyA06nJbaaxS1POYSk7mdZcPQMPQg8q1oIYxKAEZKgp86QcKJ%2BRhTiUNG2OZicopCfLgG2bPzeZiY0YrJZhJ7e6ewoJ4HTlw6miy2YNHiqPQxEzyZjaS0gkSJ4UB%2BmQdOLXZFEO9vGYbtJrQ7l80RVn7gjkUAdN%2F%2BQZdUAeh8lRi%2FsEINI05gI4M7dsOf2B2OaMSoO1U4lHeN9%2FQsOCHsQ46DyLAUzyXIOQo8P8cLqZIGa%2F7uxDwhXbamoMFrAU5Zingwg6%2F8TcFU2rz%2B0umTr6af2h4qVPC%2Fi2LBZVAS8CFX2u3AWEJ7LVw5liP53XYDWq%2Bl%2FUZJuV4PTCQhVci54A4HiUNd66xnnTsyQtCBASsK%2FzsC131OEvF006m3clCx5DI3goe%2F6TFXSBaobZWUmQeaenwNcT7a58pqVAcWwmpN07FBCsoYOR%2FCL0qxMwnuv5yAY6pgEkigqi3u7qNBh%2Bt7gpM7H25kDJk6hc5rJv31E5viuKc%2Byw5m6kv0v9l5PCbaqsu%2F32ZQrpNqw9qAWaB45ONaUI6rTIHTJdavl4Fy4NvimFJe7WQcAuOjFnkNebpDf1pSjQtMvtS%2FlIh7pretEpCG2CXyn%2BxqPKgNVFbEgbict3p0%2BROnogA5CWfH2T%2BlCsPHHSh8qpsgM9p6%2FGFJLHEofJnDHfm44p&X-Amz-Signature=0d302a764f335e2183f940f989c2e9cdb58ff8678b0ba4264e1fe5c3e3b4b9f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKNTYAPX%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIDs3vIYHmYBB8maZulakWawtpalEG8v3rukbHAr9IEdrAiBZFX90ZJ4W%2FXMhPFGoYh0AX%2FL8F4miJGoZI%2BzQQNm8bSqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMT289RTQQBmWCxb7jKtwDOUAR03cD%2BDcbid2KzGIiN%2FgkFSHCkCFL%2FVgUUD72Agy%2FvY6tgI8FSddyIt0pcQb%2BNigazs%2BAsvBFpu589nc6aNHZPwMWeMV7RjujcMRbljpX9iagzzm%2B41lnHi%2B7TSmQYlU2QZPqI9vmTYh2Db6Pl8uiqcR%2F4Mu8m7weN9cNtiOUhqahQk5WiYU1fvnkTdyA06nJbaaxS1POYSk7mdZcPQMPQg8q1oIYxKAEZKgp86QcKJ%2BRhTiUNG2OZicopCfLgG2bPzeZiY0YrJZhJ7e6ewoJ4HTlw6miy2YNHiqPQxEzyZjaS0gkSJ4UB%2BmQdOLXZFEO9vGYbtJrQ7l80RVn7gjkUAdN%2F%2BQZdUAeh8lRi%2FsEINI05gI4M7dsOf2B2OaMSoO1U4lHeN9%2FQsOCHsQ46DyLAUzyXIOQo8P8cLqZIGa%2F7uxDwhXbamoMFrAU5Zingwg6%2F8TcFU2rz%2B0umTr6af2h4qVPC%2Fi2LBZVAS8CFX2u3AWEJ7LVw5liP53XYDWq%2Bl%2FUZJuV4PTCQhVci54A4HiUNd66xnnTsyQtCBASsK%2FzsC131OEvF006m3clCx5DI3goe%2F6TFXSBaobZWUmQeaenwNcT7a58pqVAcWwmpN07FBCsoYOR%2FCL0qxMwnuv5yAY6pgEkigqi3u7qNBh%2Bt7gpM7H25kDJk6hc5rJv31E5viuKc%2Byw5m6kv0v9l5PCbaqsu%2F32ZQrpNqw9qAWaB45ONaUI6rTIHTJdavl4Fy4NvimFJe7WQcAuOjFnkNebpDf1pSjQtMvtS%2FlIh7pretEpCG2CXyn%2BxqPKgNVFbEgbict3p0%2BROnogA5CWfH2T%2BlCsPHHSh8qpsgM9p6%2FGFJLHEofJnDHfm44p&X-Amz-Signature=93bae4f862a668dab72ec1f343cc54588a8b4d73696884f97ca0e5a46b865fc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



