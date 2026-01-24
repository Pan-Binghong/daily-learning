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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOUFGBY%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIEN9i1ZAMYFLua64jp%2BoVBkpkcQs7nzjCKoKo1qBhwQsAiEA3MHHwIwAaJ8xjcr1Zn6RC%2Bkw%2FCdkdWimlmiW9c7PTMUq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDClBdaA3iZNNlVNJ3CrcA9LxvJA3lzVbzp5IjTw6HjQF5rOTtT5mWvj7%2Fu1DdWatAwNmgQ67KGmasETrxfb6RBWT5Ufu2FCN7yOVFVsU2rIHbt76mIVcMNMSoh7WLq%2FgoEyVl%2B6gAN3TlVR%2B%2BRpIKY0NtAPOWEEWuCBrYJS5yALnRVwPEnxs4DH4vTbLb0xrU8XfA8pC31YCkhKVSrzdqnMpmzKRg0VNChTK33EA5%2FTJqfEI9jD%2FSbK8JJZ7kArAxDcReOGVCM8kdCZqJ2iW92nsFdS4MhzMGzsR2dHUcl8iRPsjUj4Egdr1oq0jdVArRvM4g770aO5N3qjfb%2FrXcmMdTJd6sNer%2FlS5JqDO%2FU3oa1zHYE5vcslQdJxZFmAxymc7MpqIOflwh6clT0PjqnZHTzL77DzV4qB1ZPm%2FRl60GP2QagE4mkKQHYkGm9eZZkUn0l9WmeBDqC5krIqcjUkNi5s2tPDTJNbBcT6uNYcyFa4MfISzEYZVml2vDc35bXkoCQqnvjgCT%2BHhbtMmEj3cEWMEfirb7ghb46Nfd8e0uPfDChIP3Fnob%2BSWOi%2Bmr3QLXfYkYID5Tt2Lize7KDnE%2B4zlwR9cihBCb1lIDqzGbfQq%2B%2FT6vS4leKkp8pFjwY21LPjwh2aPbTOKMLjO0MsGOqUBwh7dY4k6RHlN21I%2B1CUyrWXoUcWz7lp4kYjdwXserKXRm7LsClFDfVb42ADQ8vNo8IHRN64Xy9v2oH91oW5LIQeDI7YfNEyO%2FwQSM6KX1JBNDjIyaxJumJzZWFghTWe4yE3L4dNhSuSVcNIG8lJmQ%2BiZg7bWgcxJqmfxSaAi1SoL48GtaaofP2Hm3FlTX7DDP80h8LaGfnXVv98ZURfFX9%2BkWv9u&X-Amz-Signature=bf4d42ab6e3839905d4bfe9c48675196bc4bfd992fc94aa53299e2b13a3f5fae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOUFGBY%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIEN9i1ZAMYFLua64jp%2BoVBkpkcQs7nzjCKoKo1qBhwQsAiEA3MHHwIwAaJ8xjcr1Zn6RC%2Bkw%2FCdkdWimlmiW9c7PTMUq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDClBdaA3iZNNlVNJ3CrcA9LxvJA3lzVbzp5IjTw6HjQF5rOTtT5mWvj7%2Fu1DdWatAwNmgQ67KGmasETrxfb6RBWT5Ufu2FCN7yOVFVsU2rIHbt76mIVcMNMSoh7WLq%2FgoEyVl%2B6gAN3TlVR%2B%2BRpIKY0NtAPOWEEWuCBrYJS5yALnRVwPEnxs4DH4vTbLb0xrU8XfA8pC31YCkhKVSrzdqnMpmzKRg0VNChTK33EA5%2FTJqfEI9jD%2FSbK8JJZ7kArAxDcReOGVCM8kdCZqJ2iW92nsFdS4MhzMGzsR2dHUcl8iRPsjUj4Egdr1oq0jdVArRvM4g770aO5N3qjfb%2FrXcmMdTJd6sNer%2FlS5JqDO%2FU3oa1zHYE5vcslQdJxZFmAxymc7MpqIOflwh6clT0PjqnZHTzL77DzV4qB1ZPm%2FRl60GP2QagE4mkKQHYkGm9eZZkUn0l9WmeBDqC5krIqcjUkNi5s2tPDTJNbBcT6uNYcyFa4MfISzEYZVml2vDc35bXkoCQqnvjgCT%2BHhbtMmEj3cEWMEfirb7ghb46Nfd8e0uPfDChIP3Fnob%2BSWOi%2Bmr3QLXfYkYID5Tt2Lize7KDnE%2B4zlwR9cihBCb1lIDqzGbfQq%2B%2FT6vS4leKkp8pFjwY21LPjwh2aPbTOKMLjO0MsGOqUBwh7dY4k6RHlN21I%2B1CUyrWXoUcWz7lp4kYjdwXserKXRm7LsClFDfVb42ADQ8vNo8IHRN64Xy9v2oH91oW5LIQeDI7YfNEyO%2FwQSM6KX1JBNDjIyaxJumJzZWFghTWe4yE3L4dNhSuSVcNIG8lJmQ%2BiZg7bWgcxJqmfxSaAi1SoL48GtaaofP2Hm3FlTX7DDP80h8LaGfnXVv98ZURfFX9%2BkWv9u&X-Amz-Signature=ed05dd335dbd3f69912ee42a6844a1b2fa6826377698a617c4ef1cdfaa617a42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOUFGBY%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIEN9i1ZAMYFLua64jp%2BoVBkpkcQs7nzjCKoKo1qBhwQsAiEA3MHHwIwAaJ8xjcr1Zn6RC%2Bkw%2FCdkdWimlmiW9c7PTMUq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDClBdaA3iZNNlVNJ3CrcA9LxvJA3lzVbzp5IjTw6HjQF5rOTtT5mWvj7%2Fu1DdWatAwNmgQ67KGmasETrxfb6RBWT5Ufu2FCN7yOVFVsU2rIHbt76mIVcMNMSoh7WLq%2FgoEyVl%2B6gAN3TlVR%2B%2BRpIKY0NtAPOWEEWuCBrYJS5yALnRVwPEnxs4DH4vTbLb0xrU8XfA8pC31YCkhKVSrzdqnMpmzKRg0VNChTK33EA5%2FTJqfEI9jD%2FSbK8JJZ7kArAxDcReOGVCM8kdCZqJ2iW92nsFdS4MhzMGzsR2dHUcl8iRPsjUj4Egdr1oq0jdVArRvM4g770aO5N3qjfb%2FrXcmMdTJd6sNer%2FlS5JqDO%2FU3oa1zHYE5vcslQdJxZFmAxymc7MpqIOflwh6clT0PjqnZHTzL77DzV4qB1ZPm%2FRl60GP2QagE4mkKQHYkGm9eZZkUn0l9WmeBDqC5krIqcjUkNi5s2tPDTJNbBcT6uNYcyFa4MfISzEYZVml2vDc35bXkoCQqnvjgCT%2BHhbtMmEj3cEWMEfirb7ghb46Nfd8e0uPfDChIP3Fnob%2BSWOi%2Bmr3QLXfYkYID5Tt2Lize7KDnE%2B4zlwR9cihBCb1lIDqzGbfQq%2B%2FT6vS4leKkp8pFjwY21LPjwh2aPbTOKMLjO0MsGOqUBwh7dY4k6RHlN21I%2B1CUyrWXoUcWz7lp4kYjdwXserKXRm7LsClFDfVb42ADQ8vNo8IHRN64Xy9v2oH91oW5LIQeDI7YfNEyO%2FwQSM6KX1JBNDjIyaxJumJzZWFghTWe4yE3L4dNhSuSVcNIG8lJmQ%2BiZg7bWgcxJqmfxSaAi1SoL48GtaaofP2Hm3FlTX7DDP80h8LaGfnXVv98ZURfFX9%2BkWv9u&X-Amz-Signature=6b5fcf8f6d55d86bf88d24ad9f92e2aaf81f0849c6c2cc48f0dc125e1261c6cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QOUFGBY%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIEN9i1ZAMYFLua64jp%2BoVBkpkcQs7nzjCKoKo1qBhwQsAiEA3MHHwIwAaJ8xjcr1Zn6RC%2Bkw%2FCdkdWimlmiW9c7PTMUq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDClBdaA3iZNNlVNJ3CrcA9LxvJA3lzVbzp5IjTw6HjQF5rOTtT5mWvj7%2Fu1DdWatAwNmgQ67KGmasETrxfb6RBWT5Ufu2FCN7yOVFVsU2rIHbt76mIVcMNMSoh7WLq%2FgoEyVl%2B6gAN3TlVR%2B%2BRpIKY0NtAPOWEEWuCBrYJS5yALnRVwPEnxs4DH4vTbLb0xrU8XfA8pC31YCkhKVSrzdqnMpmzKRg0VNChTK33EA5%2FTJqfEI9jD%2FSbK8JJZ7kArAxDcReOGVCM8kdCZqJ2iW92nsFdS4MhzMGzsR2dHUcl8iRPsjUj4Egdr1oq0jdVArRvM4g770aO5N3qjfb%2FrXcmMdTJd6sNer%2FlS5JqDO%2FU3oa1zHYE5vcslQdJxZFmAxymc7MpqIOflwh6clT0PjqnZHTzL77DzV4qB1ZPm%2FRl60GP2QagE4mkKQHYkGm9eZZkUn0l9WmeBDqC5krIqcjUkNi5s2tPDTJNbBcT6uNYcyFa4MfISzEYZVml2vDc35bXkoCQqnvjgCT%2BHhbtMmEj3cEWMEfirb7ghb46Nfd8e0uPfDChIP3Fnob%2BSWOi%2Bmr3QLXfYkYID5Tt2Lize7KDnE%2B4zlwR9cihBCb1lIDqzGbfQq%2B%2FT6vS4leKkp8pFjwY21LPjwh2aPbTOKMLjO0MsGOqUBwh7dY4k6RHlN21I%2B1CUyrWXoUcWz7lp4kYjdwXserKXRm7LsClFDfVb42ADQ8vNo8IHRN64Xy9v2oH91oW5LIQeDI7YfNEyO%2FwQSM6KX1JBNDjIyaxJumJzZWFghTWe4yE3L4dNhSuSVcNIG8lJmQ%2BiZg7bWgcxJqmfxSaAi1SoL48GtaaofP2Hm3FlTX7DDP80h8LaGfnXVv98ZURfFX9%2BkWv9u&X-Amz-Signature=054fabe55cbfbf1b092fbf5453189aee22702acca39373f3d018b011600b848b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



