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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXQVNT3Y%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIAI%2BN%2F7FUo8dVZEGJDM%2B512Liroa8kDIGUJJ%2B7LT0GaCAiBkAYkUAxgyn9tkWMoLkUmZmuO%2BI6lVkIikmOh%2FQTNpiCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnNoUaUhvuCWeCfqtKtwDuy8t0gA0qTwvsYCpLVTbkqwTkts9lVNx%2BKBuO3nFSb9c%2F45y%2BXkJUIqrd4PxSIN%2Bw8LauHJiuN9MDY1MJd51BG1GflgX%2BnvaEDDnrE7kY%2BelzObXB%2FyIZG4%2BFH14qNwRnWLCl2beorVhRDVvcWEw2e%2FK9KGCys2IB0b%2ByEJbQ9Ejon9aPWL%2FXzGLJbmm3ZnBXI9fvSBJzerbToLv%2FzwnYDFUjVey4suoGuqTtVE8HzrkcdBmJCrOA2%2BkBJ8KuC9iRUm4iT%2F8yLFuCKus6zLHoiLAdGAA%2F3824IW7JoZ77xnP9jahFSstBOtuqmXTjUBHPVoMToiAjQDq4x9GNVOOjihanNmECXmP7yiPTFTOR7YS1BvQ8ni1p7HSY7cm1%2FigaBa3LU83yC2cXnXKZ1GezAjYv43iaKxesN4qOTHSFptu8tgBuf49lKekmiXww1LsLErIigKjDqgYLFS5WeKLl9VRToW%2F8kt%2BGBGlQ4D5DxWPt0Hl6TuETgWp1bLzRcVRKdSeLl51fv6iud6CuHP0jOQ82VcjB7%2Fm1tsV25YE2vNBDM8PPXloOhD5jV37ChGspf3ynM5VHidqPbxs0wh2Xh88vSkiidu6TdUMxQKcKf74BQFj3mE45J%2Bot4cwmdmtyQY6pgEiIp6%2F0EiOmqZJE9LUavi16YRy%2BEs2ItLHwEy563QnC0dt67YgcS%2Ba%2Byl%2Fc1w1wQB%2FEl8D2Tam%2B7mnVAumbgl6Nyt3gmeBibQfziYyG5YFkJsXGps785Rofl5%2FXEvEtnPq6GYIGXfjxJJOqUhV1GJYAmQP7FcPKiNypQSfNAxy81yZ4GbgUG9d4mTvzsUgm%2BQlIdCRSispRf0K3FT4o28Ifupxyc4G&X-Amz-Signature=0fadc00e5db2ffe3d25a36312ead86527b57ebca976c5e656515a95a195d495c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXQVNT3Y%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIAI%2BN%2F7FUo8dVZEGJDM%2B512Liroa8kDIGUJJ%2B7LT0GaCAiBkAYkUAxgyn9tkWMoLkUmZmuO%2BI6lVkIikmOh%2FQTNpiCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnNoUaUhvuCWeCfqtKtwDuy8t0gA0qTwvsYCpLVTbkqwTkts9lVNx%2BKBuO3nFSb9c%2F45y%2BXkJUIqrd4PxSIN%2Bw8LauHJiuN9MDY1MJd51BG1GflgX%2BnvaEDDnrE7kY%2BelzObXB%2FyIZG4%2BFH14qNwRnWLCl2beorVhRDVvcWEw2e%2FK9KGCys2IB0b%2ByEJbQ9Ejon9aPWL%2FXzGLJbmm3ZnBXI9fvSBJzerbToLv%2FzwnYDFUjVey4suoGuqTtVE8HzrkcdBmJCrOA2%2BkBJ8KuC9iRUm4iT%2F8yLFuCKus6zLHoiLAdGAA%2F3824IW7JoZ77xnP9jahFSstBOtuqmXTjUBHPVoMToiAjQDq4x9GNVOOjihanNmECXmP7yiPTFTOR7YS1BvQ8ni1p7HSY7cm1%2FigaBa3LU83yC2cXnXKZ1GezAjYv43iaKxesN4qOTHSFptu8tgBuf49lKekmiXww1LsLErIigKjDqgYLFS5WeKLl9VRToW%2F8kt%2BGBGlQ4D5DxWPt0Hl6TuETgWp1bLzRcVRKdSeLl51fv6iud6CuHP0jOQ82VcjB7%2Fm1tsV25YE2vNBDM8PPXloOhD5jV37ChGspf3ynM5VHidqPbxs0wh2Xh88vSkiidu6TdUMxQKcKf74BQFj3mE45J%2Bot4cwmdmtyQY6pgEiIp6%2F0EiOmqZJE9LUavi16YRy%2BEs2ItLHwEy563QnC0dt67YgcS%2Ba%2Byl%2Fc1w1wQB%2FEl8D2Tam%2B7mnVAumbgl6Nyt3gmeBibQfziYyG5YFkJsXGps785Rofl5%2FXEvEtnPq6GYIGXfjxJJOqUhV1GJYAmQP7FcPKiNypQSfNAxy81yZ4GbgUG9d4mTvzsUgm%2BQlIdCRSispRf0K3FT4o28Ifupxyc4G&X-Amz-Signature=a7798c9d26d868365a48c0102d11f3df2606dd87cec30499fe2c1ceac557c8af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXQVNT3Y%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIAI%2BN%2F7FUo8dVZEGJDM%2B512Liroa8kDIGUJJ%2B7LT0GaCAiBkAYkUAxgyn9tkWMoLkUmZmuO%2BI6lVkIikmOh%2FQTNpiCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnNoUaUhvuCWeCfqtKtwDuy8t0gA0qTwvsYCpLVTbkqwTkts9lVNx%2BKBuO3nFSb9c%2F45y%2BXkJUIqrd4PxSIN%2Bw8LauHJiuN9MDY1MJd51BG1GflgX%2BnvaEDDnrE7kY%2BelzObXB%2FyIZG4%2BFH14qNwRnWLCl2beorVhRDVvcWEw2e%2FK9KGCys2IB0b%2ByEJbQ9Ejon9aPWL%2FXzGLJbmm3ZnBXI9fvSBJzerbToLv%2FzwnYDFUjVey4suoGuqTtVE8HzrkcdBmJCrOA2%2BkBJ8KuC9iRUm4iT%2F8yLFuCKus6zLHoiLAdGAA%2F3824IW7JoZ77xnP9jahFSstBOtuqmXTjUBHPVoMToiAjQDq4x9GNVOOjihanNmECXmP7yiPTFTOR7YS1BvQ8ni1p7HSY7cm1%2FigaBa3LU83yC2cXnXKZ1GezAjYv43iaKxesN4qOTHSFptu8tgBuf49lKekmiXww1LsLErIigKjDqgYLFS5WeKLl9VRToW%2F8kt%2BGBGlQ4D5DxWPt0Hl6TuETgWp1bLzRcVRKdSeLl51fv6iud6CuHP0jOQ82VcjB7%2Fm1tsV25YE2vNBDM8PPXloOhD5jV37ChGspf3ynM5VHidqPbxs0wh2Xh88vSkiidu6TdUMxQKcKf74BQFj3mE45J%2Bot4cwmdmtyQY6pgEiIp6%2F0EiOmqZJE9LUavi16YRy%2BEs2ItLHwEy563QnC0dt67YgcS%2Ba%2Byl%2Fc1w1wQB%2FEl8D2Tam%2B7mnVAumbgl6Nyt3gmeBibQfziYyG5YFkJsXGps785Rofl5%2FXEvEtnPq6GYIGXfjxJJOqUhV1GJYAmQP7FcPKiNypQSfNAxy81yZ4GbgUG9d4mTvzsUgm%2BQlIdCRSispRf0K3FT4o28Ifupxyc4G&X-Amz-Signature=b80ebca7520449c57e4ca631f7a87b50d5f44e9e958fb5492c283778d44df07d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXQVNT3Y%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIAI%2BN%2F7FUo8dVZEGJDM%2B512Liroa8kDIGUJJ%2B7LT0GaCAiBkAYkUAxgyn9tkWMoLkUmZmuO%2BI6lVkIikmOh%2FQTNpiCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnNoUaUhvuCWeCfqtKtwDuy8t0gA0qTwvsYCpLVTbkqwTkts9lVNx%2BKBuO3nFSb9c%2F45y%2BXkJUIqrd4PxSIN%2Bw8LauHJiuN9MDY1MJd51BG1GflgX%2BnvaEDDnrE7kY%2BelzObXB%2FyIZG4%2BFH14qNwRnWLCl2beorVhRDVvcWEw2e%2FK9KGCys2IB0b%2ByEJbQ9Ejon9aPWL%2FXzGLJbmm3ZnBXI9fvSBJzerbToLv%2FzwnYDFUjVey4suoGuqTtVE8HzrkcdBmJCrOA2%2BkBJ8KuC9iRUm4iT%2F8yLFuCKus6zLHoiLAdGAA%2F3824IW7JoZ77xnP9jahFSstBOtuqmXTjUBHPVoMToiAjQDq4x9GNVOOjihanNmECXmP7yiPTFTOR7YS1BvQ8ni1p7HSY7cm1%2FigaBa3LU83yC2cXnXKZ1GezAjYv43iaKxesN4qOTHSFptu8tgBuf49lKekmiXww1LsLErIigKjDqgYLFS5WeKLl9VRToW%2F8kt%2BGBGlQ4D5DxWPt0Hl6TuETgWp1bLzRcVRKdSeLl51fv6iud6CuHP0jOQ82VcjB7%2Fm1tsV25YE2vNBDM8PPXloOhD5jV37ChGspf3ynM5VHidqPbxs0wh2Xh88vSkiidu6TdUMxQKcKf74BQFj3mE45J%2Bot4cwmdmtyQY6pgEiIp6%2F0EiOmqZJE9LUavi16YRy%2BEs2ItLHwEy563QnC0dt67YgcS%2Ba%2Byl%2Fc1w1wQB%2FEl8D2Tam%2B7mnVAumbgl6Nyt3gmeBibQfziYyG5YFkJsXGps785Rofl5%2FXEvEtnPq6GYIGXfjxJJOqUhV1GJYAmQP7FcPKiNypQSfNAxy81yZ4GbgUG9d4mTvzsUgm%2BQlIdCRSispRf0K3FT4o28Ifupxyc4G&X-Amz-Signature=570da2ee1493b3ef4100805b04d2ade760723c5a913c60e58e22cefa8f151e7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



