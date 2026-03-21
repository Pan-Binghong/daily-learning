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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCD33OL%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIHV%2FBQ6mXAeiiR%2B8s2DBn%2FPVjlngs2JSq17AjpVpy%2BOMAiBBa2VPyJoDTjj9zIfaK999l6urldDp48OBrsgDQFtHeyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMVHrK5MMHLiPEF1A2KtwDAIJ9dB6cViVxp%2BdV81CMInZag2XEiVhPpCVnpDI91BIdR69A%2FNKHJVtBivx5%2BWqQq4OD4gwxJB05tbgQT41GIQKjAiKm4p8RXE1hZLT8x087DwxLWj1a%2Fb5I44iKPoui6U0xMG6teFq%2FfIs29nZLTb0kr635Lv%2BXTucYbktpMv3bmABksuUqPnFfs3I61Mdj%2FUt4fSMq%2BkcaiXnxsSqHHW8OP6%2BIbBSf1RW1EObMPoiK99DmJG1Gx43%2BC7M805aak8Y30LczW9DTdJTpzIKGGq6aiQrc33xntRPN2yJxvz5LPYczoYgjccfoEH8674WMURxnkcMaHa6djyULiGsv5Kw1%2F%2F%2Briq0xyG7hI4bE1F1c4aYV8t%2FCTKrhcUttck8LqAPa%2BUIL%2B2HGBadbvkocJ9qXj4%2BMJS%2Fzbpd9GD4SjDVZEDwcgjZ%2FBrTiLmI4RnOMYNOy%2BXBigOO2IJWkdPGReA5rsTrt6SB82irQ3PGpuOWqSe2pSk%2BTqfudmtyJ%2B5AFxUSPfOX%2BiY9eFk35Dd8pl3RB60mWezlTR7QEAH0c9jjX9kGKnaZ79PflDpde8PTFqPJK0%2F2vMdwjufWPzTV9Xfo%2BSNxNChm8W9L2oH%2FssOLsE%2FFoG162%2BxUUkGYw8474zQY6pgF%2B3J04ZCsjuCL5LwIswdMY9eAniQD1iwOzqNf3Hz%2BGdHLIkzpAZ%2Fs6QZcjpFH4B2PCHO5XfUDgQ%2Fy78U1GYkJk9jxkIIL%2F8OudTdN5N%2BN53QhwKKE%2BFaJ78622uA%2BPVRd9KCFHL5Nw7OLGV9Ve0vyHDx1OpSRYCgRIXEUN1CZgc1%2F5u7Hs3y0epkIqXWFtSwoykvKQmKKo1ffR%2FNpWQ4a3ybwCXXgk&X-Amz-Signature=dd086129c298c38c7391eae52e03d28b422bf7312ce90a0b374a229512b0a9d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCD33OL%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIHV%2FBQ6mXAeiiR%2B8s2DBn%2FPVjlngs2JSq17AjpVpy%2BOMAiBBa2VPyJoDTjj9zIfaK999l6urldDp48OBrsgDQFtHeyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMVHrK5MMHLiPEF1A2KtwDAIJ9dB6cViVxp%2BdV81CMInZag2XEiVhPpCVnpDI91BIdR69A%2FNKHJVtBivx5%2BWqQq4OD4gwxJB05tbgQT41GIQKjAiKm4p8RXE1hZLT8x087DwxLWj1a%2Fb5I44iKPoui6U0xMG6teFq%2FfIs29nZLTb0kr635Lv%2BXTucYbktpMv3bmABksuUqPnFfs3I61Mdj%2FUt4fSMq%2BkcaiXnxsSqHHW8OP6%2BIbBSf1RW1EObMPoiK99DmJG1Gx43%2BC7M805aak8Y30LczW9DTdJTpzIKGGq6aiQrc33xntRPN2yJxvz5LPYczoYgjccfoEH8674WMURxnkcMaHa6djyULiGsv5Kw1%2F%2F%2Briq0xyG7hI4bE1F1c4aYV8t%2FCTKrhcUttck8LqAPa%2BUIL%2B2HGBadbvkocJ9qXj4%2BMJS%2Fzbpd9GD4SjDVZEDwcgjZ%2FBrTiLmI4RnOMYNOy%2BXBigOO2IJWkdPGReA5rsTrt6SB82irQ3PGpuOWqSe2pSk%2BTqfudmtyJ%2B5AFxUSPfOX%2BiY9eFk35Dd8pl3RB60mWezlTR7QEAH0c9jjX9kGKnaZ79PflDpde8PTFqPJK0%2F2vMdwjufWPzTV9Xfo%2BSNxNChm8W9L2oH%2FssOLsE%2FFoG162%2BxUUkGYw8474zQY6pgF%2B3J04ZCsjuCL5LwIswdMY9eAniQD1iwOzqNf3Hz%2BGdHLIkzpAZ%2Fs6QZcjpFH4B2PCHO5XfUDgQ%2Fy78U1GYkJk9jxkIIL%2F8OudTdN5N%2BN53QhwKKE%2BFaJ78622uA%2BPVRd9KCFHL5Nw7OLGV9Ve0vyHDx1OpSRYCgRIXEUN1CZgc1%2F5u7Hs3y0epkIqXWFtSwoykvKQmKKo1ffR%2FNpWQ4a3ybwCXXgk&X-Amz-Signature=27e9e3687361ccd0ff6bd1d426ab0b958128b4002ab84bd53402214b038d413d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCD33OL%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIHV%2FBQ6mXAeiiR%2B8s2DBn%2FPVjlngs2JSq17AjpVpy%2BOMAiBBa2VPyJoDTjj9zIfaK999l6urldDp48OBrsgDQFtHeyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMVHrK5MMHLiPEF1A2KtwDAIJ9dB6cViVxp%2BdV81CMInZag2XEiVhPpCVnpDI91BIdR69A%2FNKHJVtBivx5%2BWqQq4OD4gwxJB05tbgQT41GIQKjAiKm4p8RXE1hZLT8x087DwxLWj1a%2Fb5I44iKPoui6U0xMG6teFq%2FfIs29nZLTb0kr635Lv%2BXTucYbktpMv3bmABksuUqPnFfs3I61Mdj%2FUt4fSMq%2BkcaiXnxsSqHHW8OP6%2BIbBSf1RW1EObMPoiK99DmJG1Gx43%2BC7M805aak8Y30LczW9DTdJTpzIKGGq6aiQrc33xntRPN2yJxvz5LPYczoYgjccfoEH8674WMURxnkcMaHa6djyULiGsv5Kw1%2F%2F%2Briq0xyG7hI4bE1F1c4aYV8t%2FCTKrhcUttck8LqAPa%2BUIL%2B2HGBadbvkocJ9qXj4%2BMJS%2Fzbpd9GD4SjDVZEDwcgjZ%2FBrTiLmI4RnOMYNOy%2BXBigOO2IJWkdPGReA5rsTrt6SB82irQ3PGpuOWqSe2pSk%2BTqfudmtyJ%2B5AFxUSPfOX%2BiY9eFk35Dd8pl3RB60mWezlTR7QEAH0c9jjX9kGKnaZ79PflDpde8PTFqPJK0%2F2vMdwjufWPzTV9Xfo%2BSNxNChm8W9L2oH%2FssOLsE%2FFoG162%2BxUUkGYw8474zQY6pgF%2B3J04ZCsjuCL5LwIswdMY9eAniQD1iwOzqNf3Hz%2BGdHLIkzpAZ%2Fs6QZcjpFH4B2PCHO5XfUDgQ%2Fy78U1GYkJk9jxkIIL%2F8OudTdN5N%2BN53QhwKKE%2BFaJ78622uA%2BPVRd9KCFHL5Nw7OLGV9Ve0vyHDx1OpSRYCgRIXEUN1CZgc1%2F5u7Hs3y0epkIqXWFtSwoykvKQmKKo1ffR%2FNpWQ4a3ybwCXXgk&X-Amz-Signature=e3fc47edeb518dc6cb6a5f45d56580eb5f39c7b5883a3af60672991a70af8e48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVCD33OL%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIHV%2FBQ6mXAeiiR%2B8s2DBn%2FPVjlngs2JSq17AjpVpy%2BOMAiBBa2VPyJoDTjj9zIfaK999l6urldDp48OBrsgDQFtHeyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMVHrK5MMHLiPEF1A2KtwDAIJ9dB6cViVxp%2BdV81CMInZag2XEiVhPpCVnpDI91BIdR69A%2FNKHJVtBivx5%2BWqQq4OD4gwxJB05tbgQT41GIQKjAiKm4p8RXE1hZLT8x087DwxLWj1a%2Fb5I44iKPoui6U0xMG6teFq%2FfIs29nZLTb0kr635Lv%2BXTucYbktpMv3bmABksuUqPnFfs3I61Mdj%2FUt4fSMq%2BkcaiXnxsSqHHW8OP6%2BIbBSf1RW1EObMPoiK99DmJG1Gx43%2BC7M805aak8Y30LczW9DTdJTpzIKGGq6aiQrc33xntRPN2yJxvz5LPYczoYgjccfoEH8674WMURxnkcMaHa6djyULiGsv5Kw1%2F%2F%2Briq0xyG7hI4bE1F1c4aYV8t%2FCTKrhcUttck8LqAPa%2BUIL%2B2HGBadbvkocJ9qXj4%2BMJS%2Fzbpd9GD4SjDVZEDwcgjZ%2FBrTiLmI4RnOMYNOy%2BXBigOO2IJWkdPGReA5rsTrt6SB82irQ3PGpuOWqSe2pSk%2BTqfudmtyJ%2B5AFxUSPfOX%2BiY9eFk35Dd8pl3RB60mWezlTR7QEAH0c9jjX9kGKnaZ79PflDpde8PTFqPJK0%2F2vMdwjufWPzTV9Xfo%2BSNxNChm8W9L2oH%2FssOLsE%2FFoG162%2BxUUkGYw8474zQY6pgF%2B3J04ZCsjuCL5LwIswdMY9eAniQD1iwOzqNf3Hz%2BGdHLIkzpAZ%2Fs6QZcjpFH4B2PCHO5XfUDgQ%2Fy78U1GYkJk9jxkIIL%2F8OudTdN5N%2BN53QhwKKE%2BFaJ78622uA%2BPVRd9KCFHL5Nw7OLGV9Ve0vyHDx1OpSRYCgRIXEUN1CZgc1%2F5u7Hs3y0epkIqXWFtSwoykvKQmKKo1ffR%2FNpWQ4a3ybwCXXgk&X-Amz-Signature=001c8138956b87c6a5b648f6494a23fef0f1ba9dbf3dd7f31dd7d1ccc367d5a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



