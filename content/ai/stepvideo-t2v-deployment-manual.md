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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKPWOPNE%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5vQfNcRqGKPMgouTG9so8MFjZTqDa8LcRrUesHISt9wIgeN%2FTJVvvyydy0baHdZq3blccKWL6pvSHipP0YJ%2BFmJUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDAcu5aWTyk8h2LYMjircA2KAI8T5TEeo%2BHJK%2BlxCbD%2F30vRteRSro%2B%2FBG4bIwzSlRZUKryALmSEwzTO5iCPnpyyScO1J9JDaGqd2BxE5LFNhFLeE5VQDc9CvpE%2FeLO1gR7wywXHCMGppoa3RMIML4ZknDUfM4aUK8szWga6CWwlATwwL9BLExyKbFT%2BmWHhNdrWktX9LLTCBdo7EJa1Ibflx%2F2XvgnuweYKIhfCrg9RtGHFpSv%2Bg8uVBa1PMommxoqkQK7R6Rl6uouHw5s6u60eQUkaOE0FuMjDJEIz9ssLGKCAPY8IVhFIK57CeXSVZtn7nGJFSB44EeXZhEF6SFxvnmJVSBNzr2sk778csYB3YyPZP2O%2Ftr%2FW6raEi4vsBy2KqC65vWZDUtszmwvGUrRrFLIoU9fgyISgIZx%2FbkpqwERbdjCUMitC1A0o55RvmUs3wQEZNX6aUOOjkGH7ktwVc0YdQmXJarfeR61TNj0EyFD%2FwJ%2BKT9tYmY5yFzUnFx8FpI3%2Bhzx3Pi5UeEC7ejHivnpzdBjEEHCH2s9xlKxEKIFRdEPrPyGRYAhkRmBMU%2B10lRGR2uK2OlEf7OV2ztoHTNI%2FKAlVZ4XjKui%2F9dtCBuRleK8Kb0qtTsYalSDeEYRYGO1%2BppbXgL50vMKHhwcoGOqUBeoSJjhKXu%2F698mix2sd%2BeIuRIMacvhT%2BdVnFhzcFolnDSV5Z%2B7IdVOsnLwhVUNTvftgkcjK%2Baeu5sBE0SSJLnfqDqkWYp0UJKWupmvZRxxdJEz%2BYa9BfeiPSs0TgrtENTD6n1Ty0OwNccuwBgzFObjhTacNMwTajtgVEbu2UKNX3wKJaYvaFDI%2BbSxc84dJKJnJFj9eRFWjuWLQP8UT3V2Bv2Qgj&X-Amz-Signature=dd1da30608d722d781a8c3d807769d618bff7a12c7186493ac8d7beeb69f9eef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKPWOPNE%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5vQfNcRqGKPMgouTG9so8MFjZTqDa8LcRrUesHISt9wIgeN%2FTJVvvyydy0baHdZq3blccKWL6pvSHipP0YJ%2BFmJUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDAcu5aWTyk8h2LYMjircA2KAI8T5TEeo%2BHJK%2BlxCbD%2F30vRteRSro%2B%2FBG4bIwzSlRZUKryALmSEwzTO5iCPnpyyScO1J9JDaGqd2BxE5LFNhFLeE5VQDc9CvpE%2FeLO1gR7wywXHCMGppoa3RMIML4ZknDUfM4aUK8szWga6CWwlATwwL9BLExyKbFT%2BmWHhNdrWktX9LLTCBdo7EJa1Ibflx%2F2XvgnuweYKIhfCrg9RtGHFpSv%2Bg8uVBa1PMommxoqkQK7R6Rl6uouHw5s6u60eQUkaOE0FuMjDJEIz9ssLGKCAPY8IVhFIK57CeXSVZtn7nGJFSB44EeXZhEF6SFxvnmJVSBNzr2sk778csYB3YyPZP2O%2Ftr%2FW6raEi4vsBy2KqC65vWZDUtszmwvGUrRrFLIoU9fgyISgIZx%2FbkpqwERbdjCUMitC1A0o55RvmUs3wQEZNX6aUOOjkGH7ktwVc0YdQmXJarfeR61TNj0EyFD%2FwJ%2BKT9tYmY5yFzUnFx8FpI3%2Bhzx3Pi5UeEC7ejHivnpzdBjEEHCH2s9xlKxEKIFRdEPrPyGRYAhkRmBMU%2B10lRGR2uK2OlEf7OV2ztoHTNI%2FKAlVZ4XjKui%2F9dtCBuRleK8Kb0qtTsYalSDeEYRYGO1%2BppbXgL50vMKHhwcoGOqUBeoSJjhKXu%2F698mix2sd%2BeIuRIMacvhT%2BdVnFhzcFolnDSV5Z%2B7IdVOsnLwhVUNTvftgkcjK%2Baeu5sBE0SSJLnfqDqkWYp0UJKWupmvZRxxdJEz%2BYa9BfeiPSs0TgrtENTD6n1Ty0OwNccuwBgzFObjhTacNMwTajtgVEbu2UKNX3wKJaYvaFDI%2BbSxc84dJKJnJFj9eRFWjuWLQP8UT3V2Bv2Qgj&X-Amz-Signature=1db4564345ffe7145236eabaf21be71785c2f47fd50c71a756e37b8c4ef4b010&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKPWOPNE%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5vQfNcRqGKPMgouTG9so8MFjZTqDa8LcRrUesHISt9wIgeN%2FTJVvvyydy0baHdZq3blccKWL6pvSHipP0YJ%2BFmJUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDAcu5aWTyk8h2LYMjircA2KAI8T5TEeo%2BHJK%2BlxCbD%2F30vRteRSro%2B%2FBG4bIwzSlRZUKryALmSEwzTO5iCPnpyyScO1J9JDaGqd2BxE5LFNhFLeE5VQDc9CvpE%2FeLO1gR7wywXHCMGppoa3RMIML4ZknDUfM4aUK8szWga6CWwlATwwL9BLExyKbFT%2BmWHhNdrWktX9LLTCBdo7EJa1Ibflx%2F2XvgnuweYKIhfCrg9RtGHFpSv%2Bg8uVBa1PMommxoqkQK7R6Rl6uouHw5s6u60eQUkaOE0FuMjDJEIz9ssLGKCAPY8IVhFIK57CeXSVZtn7nGJFSB44EeXZhEF6SFxvnmJVSBNzr2sk778csYB3YyPZP2O%2Ftr%2FW6raEi4vsBy2KqC65vWZDUtszmwvGUrRrFLIoU9fgyISgIZx%2FbkpqwERbdjCUMitC1A0o55RvmUs3wQEZNX6aUOOjkGH7ktwVc0YdQmXJarfeR61TNj0EyFD%2FwJ%2BKT9tYmY5yFzUnFx8FpI3%2Bhzx3Pi5UeEC7ejHivnpzdBjEEHCH2s9xlKxEKIFRdEPrPyGRYAhkRmBMU%2B10lRGR2uK2OlEf7OV2ztoHTNI%2FKAlVZ4XjKui%2F9dtCBuRleK8Kb0qtTsYalSDeEYRYGO1%2BppbXgL50vMKHhwcoGOqUBeoSJjhKXu%2F698mix2sd%2BeIuRIMacvhT%2BdVnFhzcFolnDSV5Z%2B7IdVOsnLwhVUNTvftgkcjK%2Baeu5sBE0SSJLnfqDqkWYp0UJKWupmvZRxxdJEz%2BYa9BfeiPSs0TgrtENTD6n1Ty0OwNccuwBgzFObjhTacNMwTajtgVEbu2UKNX3wKJaYvaFDI%2BbSxc84dJKJnJFj9eRFWjuWLQP8UT3V2Bv2Qgj&X-Amz-Signature=6bea11356d0379802b7efbcd36aeb58daad4d46d6ca4d4cea88dcc80d0400284&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKPWOPNE%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5vQfNcRqGKPMgouTG9so8MFjZTqDa8LcRrUesHISt9wIgeN%2FTJVvvyydy0baHdZq3blccKWL6pvSHipP0YJ%2BFmJUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDAcu5aWTyk8h2LYMjircA2KAI8T5TEeo%2BHJK%2BlxCbD%2F30vRteRSro%2B%2FBG4bIwzSlRZUKryALmSEwzTO5iCPnpyyScO1J9JDaGqd2BxE5LFNhFLeE5VQDc9CvpE%2FeLO1gR7wywXHCMGppoa3RMIML4ZknDUfM4aUK8szWga6CWwlATwwL9BLExyKbFT%2BmWHhNdrWktX9LLTCBdo7EJa1Ibflx%2F2XvgnuweYKIhfCrg9RtGHFpSv%2Bg8uVBa1PMommxoqkQK7R6Rl6uouHw5s6u60eQUkaOE0FuMjDJEIz9ssLGKCAPY8IVhFIK57CeXSVZtn7nGJFSB44EeXZhEF6SFxvnmJVSBNzr2sk778csYB3YyPZP2O%2Ftr%2FW6raEi4vsBy2KqC65vWZDUtszmwvGUrRrFLIoU9fgyISgIZx%2FbkpqwERbdjCUMitC1A0o55RvmUs3wQEZNX6aUOOjkGH7ktwVc0YdQmXJarfeR61TNj0EyFD%2FwJ%2BKT9tYmY5yFzUnFx8FpI3%2Bhzx3Pi5UeEC7ejHivnpzdBjEEHCH2s9xlKxEKIFRdEPrPyGRYAhkRmBMU%2B10lRGR2uK2OlEf7OV2ztoHTNI%2FKAlVZ4XjKui%2F9dtCBuRleK8Kb0qtTsYalSDeEYRYGO1%2BppbXgL50vMKHhwcoGOqUBeoSJjhKXu%2F698mix2sd%2BeIuRIMacvhT%2BdVnFhzcFolnDSV5Z%2B7IdVOsnLwhVUNTvftgkcjK%2Baeu5sBE0SSJLnfqDqkWYp0UJKWupmvZRxxdJEz%2BYa9BfeiPSs0TgrtENTD6n1Ty0OwNccuwBgzFObjhTacNMwTajtgVEbu2UKNX3wKJaYvaFDI%2BbSxc84dJKJnJFj9eRFWjuWLQP8UT3V2Bv2Qgj&X-Amz-Signature=6a078e8c4d024e8f71b095ac2137706f75ec292c9d3d26534d6338e3ab2a0282&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



