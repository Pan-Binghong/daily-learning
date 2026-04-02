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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBNVVUXM%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDQqwFtgRvUI7stHtquzsRYD2zbZUoEDZ8Z7TS8NKPDwIgfErBdnIfHynRWep%2FcVTdZOVOT%2FJZsOlALESqGMOOF3Aq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFdx9exnhIKsZnJZeyrcA1w%2B5LzovUJEZRRw0OW7L9cHwROmAvez73mca66g0OQCyMcEFvKouOiS%2FfXivO67QNo7S4eS7rZq9EpSa74t6gd0PIJKheqqqSh%2FBouB8KBOfTGiV9aPXwKe5hJg0fc2hhZT3zNEomcPGjrib2iUOSo0Ryeuh%2B7s70wXEw6f%2BS2tpvm1zYaMNdlIJjKWmERWgQW06MTrmX3nnldTUQfoxFQ5QlKGNpxRnmDMBxL3bHS%2FK%2BZBsnhQqZ6ECu%2FpRM8yo0Y1Wfb0ZWX7utWswvFCy9oWNOoaSHrMzHYP4w4VOpQBwTch3%2FTDffET09lEoKptRFxEqmUiPiNwMkgJMap3Ib1itDAeM7IVFSLn%2BZV6HS5aP3CBbYf8ESjNUbNWcV4wxc%2F1QZTg1kurcTSEVBxdTfTj9ko1NPr1jEGthtAOBlfH7wuAbWqCE2FlScFq0TyGtJXj1fPc0Jv5o0x5ArUroQP9fEPVFQWfnD5Zh27aq5%2FSDCp6iSA%2FGe7b%2F5e9HO%2BVgQXqDj12kUn0Bp9hzoEdlm6zdLbM%2F%2Fwc0WinZ86H0y8v1ljpasGgjXI2Z6oiyD2B%2FZ7bve8Chm5lGa%2BK3Ye6Q44MmXu%2ByFd90FtR0SPtxcnuHH1N3UsC91FTQ8%2BnMLaut84GOqUBay1AGup0bPyFXpaHd%2FjxU0z%2FZC%2FS8Q0j7jTE4Z1z641RhvTYim7aEt%2BebpTOZRuY1WjkCK6RYgVHyvp8OLr1AauNMLEQI5zR7pF7aQXIKcun%2Bh08bcid6rQxb0RTsjFeQ9%2FISOU4EA0SuQudnC0f3LIoH6fDF%2FIABiqvxCSCyvUqkEVBmM39LIDmlrMoQP1NtZVNk586rHBzpB6aU7nsZqhau07N&X-Amz-Signature=a68602d859bf282b96aa8e8804b091e0df64d1134c1b81494f1bc972e862d140&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBNVVUXM%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDQqwFtgRvUI7stHtquzsRYD2zbZUoEDZ8Z7TS8NKPDwIgfErBdnIfHynRWep%2FcVTdZOVOT%2FJZsOlALESqGMOOF3Aq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFdx9exnhIKsZnJZeyrcA1w%2B5LzovUJEZRRw0OW7L9cHwROmAvez73mca66g0OQCyMcEFvKouOiS%2FfXivO67QNo7S4eS7rZq9EpSa74t6gd0PIJKheqqqSh%2FBouB8KBOfTGiV9aPXwKe5hJg0fc2hhZT3zNEomcPGjrib2iUOSo0Ryeuh%2B7s70wXEw6f%2BS2tpvm1zYaMNdlIJjKWmERWgQW06MTrmX3nnldTUQfoxFQ5QlKGNpxRnmDMBxL3bHS%2FK%2BZBsnhQqZ6ECu%2FpRM8yo0Y1Wfb0ZWX7utWswvFCy9oWNOoaSHrMzHYP4w4VOpQBwTch3%2FTDffET09lEoKptRFxEqmUiPiNwMkgJMap3Ib1itDAeM7IVFSLn%2BZV6HS5aP3CBbYf8ESjNUbNWcV4wxc%2F1QZTg1kurcTSEVBxdTfTj9ko1NPr1jEGthtAOBlfH7wuAbWqCE2FlScFq0TyGtJXj1fPc0Jv5o0x5ArUroQP9fEPVFQWfnD5Zh27aq5%2FSDCp6iSA%2FGe7b%2F5e9HO%2BVgQXqDj12kUn0Bp9hzoEdlm6zdLbM%2F%2Fwc0WinZ86H0y8v1ljpasGgjXI2Z6oiyD2B%2FZ7bve8Chm5lGa%2BK3Ye6Q44MmXu%2ByFd90FtR0SPtxcnuHH1N3UsC91FTQ8%2BnMLaut84GOqUBay1AGup0bPyFXpaHd%2FjxU0z%2FZC%2FS8Q0j7jTE4Z1z641RhvTYim7aEt%2BebpTOZRuY1WjkCK6RYgVHyvp8OLr1AauNMLEQI5zR7pF7aQXIKcun%2Bh08bcid6rQxb0RTsjFeQ9%2FISOU4EA0SuQudnC0f3LIoH6fDF%2FIABiqvxCSCyvUqkEVBmM39LIDmlrMoQP1NtZVNk586rHBzpB6aU7nsZqhau07N&X-Amz-Signature=5ecc84a62d29c0c756edb1386088467b244bad97237de0d62370ae3c395fbbdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBNVVUXM%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDQqwFtgRvUI7stHtquzsRYD2zbZUoEDZ8Z7TS8NKPDwIgfErBdnIfHynRWep%2FcVTdZOVOT%2FJZsOlALESqGMOOF3Aq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFdx9exnhIKsZnJZeyrcA1w%2B5LzovUJEZRRw0OW7L9cHwROmAvez73mca66g0OQCyMcEFvKouOiS%2FfXivO67QNo7S4eS7rZq9EpSa74t6gd0PIJKheqqqSh%2FBouB8KBOfTGiV9aPXwKe5hJg0fc2hhZT3zNEomcPGjrib2iUOSo0Ryeuh%2B7s70wXEw6f%2BS2tpvm1zYaMNdlIJjKWmERWgQW06MTrmX3nnldTUQfoxFQ5QlKGNpxRnmDMBxL3bHS%2FK%2BZBsnhQqZ6ECu%2FpRM8yo0Y1Wfb0ZWX7utWswvFCy9oWNOoaSHrMzHYP4w4VOpQBwTch3%2FTDffET09lEoKptRFxEqmUiPiNwMkgJMap3Ib1itDAeM7IVFSLn%2BZV6HS5aP3CBbYf8ESjNUbNWcV4wxc%2F1QZTg1kurcTSEVBxdTfTj9ko1NPr1jEGthtAOBlfH7wuAbWqCE2FlScFq0TyGtJXj1fPc0Jv5o0x5ArUroQP9fEPVFQWfnD5Zh27aq5%2FSDCp6iSA%2FGe7b%2F5e9HO%2BVgQXqDj12kUn0Bp9hzoEdlm6zdLbM%2F%2Fwc0WinZ86H0y8v1ljpasGgjXI2Z6oiyD2B%2FZ7bve8Chm5lGa%2BK3Ye6Q44MmXu%2ByFd90FtR0SPtxcnuHH1N3UsC91FTQ8%2BnMLaut84GOqUBay1AGup0bPyFXpaHd%2FjxU0z%2FZC%2FS8Q0j7jTE4Z1z641RhvTYim7aEt%2BebpTOZRuY1WjkCK6RYgVHyvp8OLr1AauNMLEQI5zR7pF7aQXIKcun%2Bh08bcid6rQxb0RTsjFeQ9%2FISOU4EA0SuQudnC0f3LIoH6fDF%2FIABiqvxCSCyvUqkEVBmM39LIDmlrMoQP1NtZVNk586rHBzpB6aU7nsZqhau07N&X-Amz-Signature=54ad6ed74d2ce18ea0034326552b829a28969fee216b285a7ce1a99c2cbb6f6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBNVVUXM%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDQqwFtgRvUI7stHtquzsRYD2zbZUoEDZ8Z7TS8NKPDwIgfErBdnIfHynRWep%2FcVTdZOVOT%2FJZsOlALESqGMOOF3Aq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDFdx9exnhIKsZnJZeyrcA1w%2B5LzovUJEZRRw0OW7L9cHwROmAvez73mca66g0OQCyMcEFvKouOiS%2FfXivO67QNo7S4eS7rZq9EpSa74t6gd0PIJKheqqqSh%2FBouB8KBOfTGiV9aPXwKe5hJg0fc2hhZT3zNEomcPGjrib2iUOSo0Ryeuh%2B7s70wXEw6f%2BS2tpvm1zYaMNdlIJjKWmERWgQW06MTrmX3nnldTUQfoxFQ5QlKGNpxRnmDMBxL3bHS%2FK%2BZBsnhQqZ6ECu%2FpRM8yo0Y1Wfb0ZWX7utWswvFCy9oWNOoaSHrMzHYP4w4VOpQBwTch3%2FTDffET09lEoKptRFxEqmUiPiNwMkgJMap3Ib1itDAeM7IVFSLn%2BZV6HS5aP3CBbYf8ESjNUbNWcV4wxc%2F1QZTg1kurcTSEVBxdTfTj9ko1NPr1jEGthtAOBlfH7wuAbWqCE2FlScFq0TyGtJXj1fPc0Jv5o0x5ArUroQP9fEPVFQWfnD5Zh27aq5%2FSDCp6iSA%2FGe7b%2F5e9HO%2BVgQXqDj12kUn0Bp9hzoEdlm6zdLbM%2F%2Fwc0WinZ86H0y8v1ljpasGgjXI2Z6oiyD2B%2FZ7bve8Chm5lGa%2BK3Ye6Q44MmXu%2ByFd90FtR0SPtxcnuHH1N3UsC91FTQ8%2BnMLaut84GOqUBay1AGup0bPyFXpaHd%2FjxU0z%2FZC%2FS8Q0j7jTE4Z1z641RhvTYim7aEt%2BebpTOZRuY1WjkCK6RYgVHyvp8OLr1AauNMLEQI5zR7pF7aQXIKcun%2Bh08bcid6rQxb0RTsjFeQ9%2FISOU4EA0SuQudnC0f3LIoH6fDF%2FIABiqvxCSCyvUqkEVBmM39LIDmlrMoQP1NtZVNk586rHBzpB6aU7nsZqhau07N&X-Amz-Signature=67571adeaa6c24b5ffb6ba776f5ad9b1c6de2f133e31739c0ed0f5ff8e5db55c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



