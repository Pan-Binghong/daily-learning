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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBCZKJ5S%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDTuADC4Dzbrmdl%2BM3y%2FHtKts45NLu3HLYh2yX7Fy4b5wIgY7DLQavxbpuzlhdqwW%2F6SrkbTGovjhB6Fikhhm%2Bog70qiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7wwRe4E25ZfoRpMircA%2F45jevDUKRok1P3KPFrBpmRdqfA8OQ9Et%2FLg7fRo6rCq6ebWHbBwfjsrBBth5YYbFWworaD7F%2BWqNZ3Ygqi7TRjrQa5r5Q25np8STz5oFhyaQuqE8T1aL8Q3i274KUUWW91G0s%2Fw3l8XzI%2BWquklRJNrWPakAgehA9Sb6eM9nKQ2WoOVLvxITwobYevhadrdOq2G67TE2nCHmn9c39EXM0oPcOY%2FxLdFTbmTAxr6PTjz56OYHsYcWJfpnsuIxtsJGpjV%2Fqv5S5o4pMElEKfbmLCHz87eFt5UAz5zkpiv%2F855Jo8d7ZlpoDm0JMi9MDY1%2BRLvQgHbqkAABK75DZ1%2F%2BY4DzItRcCCrWPQS12Po6fqjvD62QNMRn6WaZKmJxiyhNBt8BCbgr1HzON0p3DVJmOj0ETXyx2PgQdSnxBYdxfhWuxYLiAF7R5x1HfM1Y3mDYvblEw4FtM2UFVFiNDUgGfqS0sJ9xj9qHiQtHBd%2BeD6NioaSX%2BnglsCqoFnlCwWRV7BluXxxBzGuf0AIUWSxt4fKfsAM2v5%2BQGKrvtK5PYuB60da3swv5HY1%2BcKX03r7fLCSLxxjNf9NssaZ%2B9YzUHOOr63%2BdACoqg7snvBcaQyjbrYKDK2Y%2FJhUyh5MLKT78wGOqUBAVMf3SpPdahYf7U9Rx13giSLiAGC93%2FKS1sRg%2Bkuh%2BV%2FWiHy3LvqSccHfULzpm%2FwPP6ivBncTtj%2FqyMnfRa8%2BQGIfQk6b5Ie5n4mQn1SNWfw0O2DukMLBFMZlzec4eefZ7hQr1ae3b6wUPGK3qH6X0khiOWAmDh%2BIMV%2BC%2BdgdBUOtj5IKqyiwn0VxoXghpuYRaUW44Burjt0lmY9sZgGyhAb560Q&X-Amz-Signature=fd859c7e8823d40e224db6b4edcf04eb059065f7e500fe164317bcc4a09cbda3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBCZKJ5S%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDTuADC4Dzbrmdl%2BM3y%2FHtKts45NLu3HLYh2yX7Fy4b5wIgY7DLQavxbpuzlhdqwW%2F6SrkbTGovjhB6Fikhhm%2Bog70qiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7wwRe4E25ZfoRpMircA%2F45jevDUKRok1P3KPFrBpmRdqfA8OQ9Et%2FLg7fRo6rCq6ebWHbBwfjsrBBth5YYbFWworaD7F%2BWqNZ3Ygqi7TRjrQa5r5Q25np8STz5oFhyaQuqE8T1aL8Q3i274KUUWW91G0s%2Fw3l8XzI%2BWquklRJNrWPakAgehA9Sb6eM9nKQ2WoOVLvxITwobYevhadrdOq2G67TE2nCHmn9c39EXM0oPcOY%2FxLdFTbmTAxr6PTjz56OYHsYcWJfpnsuIxtsJGpjV%2Fqv5S5o4pMElEKfbmLCHz87eFt5UAz5zkpiv%2F855Jo8d7ZlpoDm0JMi9MDY1%2BRLvQgHbqkAABK75DZ1%2F%2BY4DzItRcCCrWPQS12Po6fqjvD62QNMRn6WaZKmJxiyhNBt8BCbgr1HzON0p3DVJmOj0ETXyx2PgQdSnxBYdxfhWuxYLiAF7R5x1HfM1Y3mDYvblEw4FtM2UFVFiNDUgGfqS0sJ9xj9qHiQtHBd%2BeD6NioaSX%2BnglsCqoFnlCwWRV7BluXxxBzGuf0AIUWSxt4fKfsAM2v5%2BQGKrvtK5PYuB60da3swv5HY1%2BcKX03r7fLCSLxxjNf9NssaZ%2B9YzUHOOr63%2BdACoqg7snvBcaQyjbrYKDK2Y%2FJhUyh5MLKT78wGOqUBAVMf3SpPdahYf7U9Rx13giSLiAGC93%2FKS1sRg%2Bkuh%2BV%2FWiHy3LvqSccHfULzpm%2FwPP6ivBncTtj%2FqyMnfRa8%2BQGIfQk6b5Ie5n4mQn1SNWfw0O2DukMLBFMZlzec4eefZ7hQr1ae3b6wUPGK3qH6X0khiOWAmDh%2BIMV%2BC%2BdgdBUOtj5IKqyiwn0VxoXghpuYRaUW44Burjt0lmY9sZgGyhAb560Q&X-Amz-Signature=4be69cd62e8b297224a783707422e663bf0a6575d837d6d4ad680d48bfd2d06e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBCZKJ5S%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDTuADC4Dzbrmdl%2BM3y%2FHtKts45NLu3HLYh2yX7Fy4b5wIgY7DLQavxbpuzlhdqwW%2F6SrkbTGovjhB6Fikhhm%2Bog70qiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7wwRe4E25ZfoRpMircA%2F45jevDUKRok1P3KPFrBpmRdqfA8OQ9Et%2FLg7fRo6rCq6ebWHbBwfjsrBBth5YYbFWworaD7F%2BWqNZ3Ygqi7TRjrQa5r5Q25np8STz5oFhyaQuqE8T1aL8Q3i274KUUWW91G0s%2Fw3l8XzI%2BWquklRJNrWPakAgehA9Sb6eM9nKQ2WoOVLvxITwobYevhadrdOq2G67TE2nCHmn9c39EXM0oPcOY%2FxLdFTbmTAxr6PTjz56OYHsYcWJfpnsuIxtsJGpjV%2Fqv5S5o4pMElEKfbmLCHz87eFt5UAz5zkpiv%2F855Jo8d7ZlpoDm0JMi9MDY1%2BRLvQgHbqkAABK75DZ1%2F%2BY4DzItRcCCrWPQS12Po6fqjvD62QNMRn6WaZKmJxiyhNBt8BCbgr1HzON0p3DVJmOj0ETXyx2PgQdSnxBYdxfhWuxYLiAF7R5x1HfM1Y3mDYvblEw4FtM2UFVFiNDUgGfqS0sJ9xj9qHiQtHBd%2BeD6NioaSX%2BnglsCqoFnlCwWRV7BluXxxBzGuf0AIUWSxt4fKfsAM2v5%2BQGKrvtK5PYuB60da3swv5HY1%2BcKX03r7fLCSLxxjNf9NssaZ%2B9YzUHOOr63%2BdACoqg7snvBcaQyjbrYKDK2Y%2FJhUyh5MLKT78wGOqUBAVMf3SpPdahYf7U9Rx13giSLiAGC93%2FKS1sRg%2Bkuh%2BV%2FWiHy3LvqSccHfULzpm%2FwPP6ivBncTtj%2FqyMnfRa8%2BQGIfQk6b5Ie5n4mQn1SNWfw0O2DukMLBFMZlzec4eefZ7hQr1ae3b6wUPGK3qH6X0khiOWAmDh%2BIMV%2BC%2BdgdBUOtj5IKqyiwn0VxoXghpuYRaUW44Burjt0lmY9sZgGyhAb560Q&X-Amz-Signature=7658c30b79f343e21abda066695cb2215af86082addabccd5bf85b937735f14f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBCZKJ5S%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDTuADC4Dzbrmdl%2BM3y%2FHtKts45NLu3HLYh2yX7Fy4b5wIgY7DLQavxbpuzlhdqwW%2F6SrkbTGovjhB6Fikhhm%2Bog70qiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7wwRe4E25ZfoRpMircA%2F45jevDUKRok1P3KPFrBpmRdqfA8OQ9Et%2FLg7fRo6rCq6ebWHbBwfjsrBBth5YYbFWworaD7F%2BWqNZ3Ygqi7TRjrQa5r5Q25np8STz5oFhyaQuqE8T1aL8Q3i274KUUWW91G0s%2Fw3l8XzI%2BWquklRJNrWPakAgehA9Sb6eM9nKQ2WoOVLvxITwobYevhadrdOq2G67TE2nCHmn9c39EXM0oPcOY%2FxLdFTbmTAxr6PTjz56OYHsYcWJfpnsuIxtsJGpjV%2Fqv5S5o4pMElEKfbmLCHz87eFt5UAz5zkpiv%2F855Jo8d7ZlpoDm0JMi9MDY1%2BRLvQgHbqkAABK75DZ1%2F%2BY4DzItRcCCrWPQS12Po6fqjvD62QNMRn6WaZKmJxiyhNBt8BCbgr1HzON0p3DVJmOj0ETXyx2PgQdSnxBYdxfhWuxYLiAF7R5x1HfM1Y3mDYvblEw4FtM2UFVFiNDUgGfqS0sJ9xj9qHiQtHBd%2BeD6NioaSX%2BnglsCqoFnlCwWRV7BluXxxBzGuf0AIUWSxt4fKfsAM2v5%2BQGKrvtK5PYuB60da3swv5HY1%2BcKX03r7fLCSLxxjNf9NssaZ%2B9YzUHOOr63%2BdACoqg7snvBcaQyjbrYKDK2Y%2FJhUyh5MLKT78wGOqUBAVMf3SpPdahYf7U9Rx13giSLiAGC93%2FKS1sRg%2Bkuh%2BV%2FWiHy3LvqSccHfULzpm%2FwPP6ivBncTtj%2FqyMnfRa8%2BQGIfQk6b5Ie5n4mQn1SNWfw0O2DukMLBFMZlzec4eefZ7hQr1ae3b6wUPGK3qH6X0khiOWAmDh%2BIMV%2BC%2BdgdBUOtj5IKqyiwn0VxoXghpuYRaUW44Burjt0lmY9sZgGyhAb560Q&X-Amz-Signature=c2a51189dc9af91428678d94c5f7203eee1a598ceff90c8f037aaa811888d2a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



