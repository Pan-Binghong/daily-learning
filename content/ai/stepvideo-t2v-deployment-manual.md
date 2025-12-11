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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWQ3UO46%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEGSmF5c0%2BOs2s72swLvlHsGkwDmI1rUOoBUX%2BMbmIy1AiEA6Rd9o63%2Fyp4GHP8FLsmfROwqCorM6HxfZfHjQvtBDMEqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9RdX5FmjPCxWXHACrcA2SSnnnq68H6uzkf1Q3kF6xOMPoo2urOYHO4kc0kE8xZ5IBpzsrryPqzaK0eYM4s5K7rANLOCUK3jbbTYU0WPk0894vXnveg7DbFKBWg%2FXW9LzGCukuVasNekHQV0SLLEvWbP4Ey81nGw1o7mdRoC1dMKCBIMGuFFuZWu%2F%2FDFFedFwpKL%2FkcTme426kc6ufs%2FdfeEIRb%2BdpFc%2B3bcfBvR1pnbvt1uO0Q%2BRd6K5FVOnIZ5p0UBb9Xoz9rGMaM69oQmkpkY9Y%2BKZg1qACaVO93vo7%2FLvc6x1XKBbFdDlV0tq0nLOcXwp9aRjZ8tj0mkd%2FC4ipTB1UYggjDys3Rw2Zi63V11JFoN4poEtPToYDEy0ZPm0r35QNY9zZ0i6fyI%2F4zz40994d7omCUHvnbNy7jQnM5YVSssEy65x%2FlnfZQqNJL6MlPIIugYKn%2BEmcQ7ohRW2RbKISBEjjMH%2B%2FkAUV0PzxsNMGwr6AviYZimAJKOFEYjIWAAcrr%2FpW%2FkS9xakTOtxw%2B2Inj%2FGKp4p%2BXUxlyWwMAgthg%2BfhDQLpPkNKjUSZBTxZhfcRLFOJRcEznRGQw107sh0VTvp7BJKga0kecPx%2F%2Fx4IbvviwKJX4G5t7vjbLMjcGsCP9RNZQtwv%2BMPu16MkGOqUBfqDUYZ6oJ0RD9vCeMNIJRquHuO4%2B1E%2FXiiLjWDlHdtp23fUqA1pdAz2m2xjFtg8U%2FUMM5XCLuKMCr9tkUhuhxEb1I1fhpKfnXDdIA%2FohX44jffOBQwEE2iJzCc9hdU3R4DGKcEXC%2BOpLWyhX2U4cIbHpHV8%2FqzTrZgY9pF9AlgTHXR1BJRNh1kbRSL6uv%2B0GGaHN%2Fvz%2Fp0X3i6XciKMYoKvd4abE&X-Amz-Signature=3b312287f6c06cd59abe40b340d5c204f25001096729cc72659a8c95221f0c4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWQ3UO46%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEGSmF5c0%2BOs2s72swLvlHsGkwDmI1rUOoBUX%2BMbmIy1AiEA6Rd9o63%2Fyp4GHP8FLsmfROwqCorM6HxfZfHjQvtBDMEqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9RdX5FmjPCxWXHACrcA2SSnnnq68H6uzkf1Q3kF6xOMPoo2urOYHO4kc0kE8xZ5IBpzsrryPqzaK0eYM4s5K7rANLOCUK3jbbTYU0WPk0894vXnveg7DbFKBWg%2FXW9LzGCukuVasNekHQV0SLLEvWbP4Ey81nGw1o7mdRoC1dMKCBIMGuFFuZWu%2F%2FDFFedFwpKL%2FkcTme426kc6ufs%2FdfeEIRb%2BdpFc%2B3bcfBvR1pnbvt1uO0Q%2BRd6K5FVOnIZ5p0UBb9Xoz9rGMaM69oQmkpkY9Y%2BKZg1qACaVO93vo7%2FLvc6x1XKBbFdDlV0tq0nLOcXwp9aRjZ8tj0mkd%2FC4ipTB1UYggjDys3Rw2Zi63V11JFoN4poEtPToYDEy0ZPm0r35QNY9zZ0i6fyI%2F4zz40994d7omCUHvnbNy7jQnM5YVSssEy65x%2FlnfZQqNJL6MlPIIugYKn%2BEmcQ7ohRW2RbKISBEjjMH%2B%2FkAUV0PzxsNMGwr6AviYZimAJKOFEYjIWAAcrr%2FpW%2FkS9xakTOtxw%2B2Inj%2FGKp4p%2BXUxlyWwMAgthg%2BfhDQLpPkNKjUSZBTxZhfcRLFOJRcEznRGQw107sh0VTvp7BJKga0kecPx%2F%2Fx4IbvviwKJX4G5t7vjbLMjcGsCP9RNZQtwv%2BMPu16MkGOqUBfqDUYZ6oJ0RD9vCeMNIJRquHuO4%2B1E%2FXiiLjWDlHdtp23fUqA1pdAz2m2xjFtg8U%2FUMM5XCLuKMCr9tkUhuhxEb1I1fhpKfnXDdIA%2FohX44jffOBQwEE2iJzCc9hdU3R4DGKcEXC%2BOpLWyhX2U4cIbHpHV8%2FqzTrZgY9pF9AlgTHXR1BJRNh1kbRSL6uv%2B0GGaHN%2Fvz%2Fp0X3i6XciKMYoKvd4abE&X-Amz-Signature=90a607f32637b5ac055dca7bd265a5f0ab3922bc6864c6b7f89038bf11769e2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWQ3UO46%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEGSmF5c0%2BOs2s72swLvlHsGkwDmI1rUOoBUX%2BMbmIy1AiEA6Rd9o63%2Fyp4GHP8FLsmfROwqCorM6HxfZfHjQvtBDMEqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9RdX5FmjPCxWXHACrcA2SSnnnq68H6uzkf1Q3kF6xOMPoo2urOYHO4kc0kE8xZ5IBpzsrryPqzaK0eYM4s5K7rANLOCUK3jbbTYU0WPk0894vXnveg7DbFKBWg%2FXW9LzGCukuVasNekHQV0SLLEvWbP4Ey81nGw1o7mdRoC1dMKCBIMGuFFuZWu%2F%2FDFFedFwpKL%2FkcTme426kc6ufs%2FdfeEIRb%2BdpFc%2B3bcfBvR1pnbvt1uO0Q%2BRd6K5FVOnIZ5p0UBb9Xoz9rGMaM69oQmkpkY9Y%2BKZg1qACaVO93vo7%2FLvc6x1XKBbFdDlV0tq0nLOcXwp9aRjZ8tj0mkd%2FC4ipTB1UYggjDys3Rw2Zi63V11JFoN4poEtPToYDEy0ZPm0r35QNY9zZ0i6fyI%2F4zz40994d7omCUHvnbNy7jQnM5YVSssEy65x%2FlnfZQqNJL6MlPIIugYKn%2BEmcQ7ohRW2RbKISBEjjMH%2B%2FkAUV0PzxsNMGwr6AviYZimAJKOFEYjIWAAcrr%2FpW%2FkS9xakTOtxw%2B2Inj%2FGKp4p%2BXUxlyWwMAgthg%2BfhDQLpPkNKjUSZBTxZhfcRLFOJRcEznRGQw107sh0VTvp7BJKga0kecPx%2F%2Fx4IbvviwKJX4G5t7vjbLMjcGsCP9RNZQtwv%2BMPu16MkGOqUBfqDUYZ6oJ0RD9vCeMNIJRquHuO4%2B1E%2FXiiLjWDlHdtp23fUqA1pdAz2m2xjFtg8U%2FUMM5XCLuKMCr9tkUhuhxEb1I1fhpKfnXDdIA%2FohX44jffOBQwEE2iJzCc9hdU3R4DGKcEXC%2BOpLWyhX2U4cIbHpHV8%2FqzTrZgY9pF9AlgTHXR1BJRNh1kbRSL6uv%2B0GGaHN%2Fvz%2Fp0X3i6XciKMYoKvd4abE&X-Amz-Signature=b5a7965a55403062473a30f208cbcfd98a7833fa87e99bb1b6740cf7218585bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWQ3UO46%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIEGSmF5c0%2BOs2s72swLvlHsGkwDmI1rUOoBUX%2BMbmIy1AiEA6Rd9o63%2Fyp4GHP8FLsmfROwqCorM6HxfZfHjQvtBDMEqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9RdX5FmjPCxWXHACrcA2SSnnnq68H6uzkf1Q3kF6xOMPoo2urOYHO4kc0kE8xZ5IBpzsrryPqzaK0eYM4s5K7rANLOCUK3jbbTYU0WPk0894vXnveg7DbFKBWg%2FXW9LzGCukuVasNekHQV0SLLEvWbP4Ey81nGw1o7mdRoC1dMKCBIMGuFFuZWu%2F%2FDFFedFwpKL%2FkcTme426kc6ufs%2FdfeEIRb%2BdpFc%2B3bcfBvR1pnbvt1uO0Q%2BRd6K5FVOnIZ5p0UBb9Xoz9rGMaM69oQmkpkY9Y%2BKZg1qACaVO93vo7%2FLvc6x1XKBbFdDlV0tq0nLOcXwp9aRjZ8tj0mkd%2FC4ipTB1UYggjDys3Rw2Zi63V11JFoN4poEtPToYDEy0ZPm0r35QNY9zZ0i6fyI%2F4zz40994d7omCUHvnbNy7jQnM5YVSssEy65x%2FlnfZQqNJL6MlPIIugYKn%2BEmcQ7ohRW2RbKISBEjjMH%2B%2FkAUV0PzxsNMGwr6AviYZimAJKOFEYjIWAAcrr%2FpW%2FkS9xakTOtxw%2B2Inj%2FGKp4p%2BXUxlyWwMAgthg%2BfhDQLpPkNKjUSZBTxZhfcRLFOJRcEznRGQw107sh0VTvp7BJKga0kecPx%2F%2Fx4IbvviwKJX4G5t7vjbLMjcGsCP9RNZQtwv%2BMPu16MkGOqUBfqDUYZ6oJ0RD9vCeMNIJRquHuO4%2B1E%2FXiiLjWDlHdtp23fUqA1pdAz2m2xjFtg8U%2FUMM5XCLuKMCr9tkUhuhxEb1I1fhpKfnXDdIA%2FohX44jffOBQwEE2iJzCc9hdU3R4DGKcEXC%2BOpLWyhX2U4cIbHpHV8%2FqzTrZgY9pF9AlgTHXR1BJRNh1kbRSL6uv%2B0GGaHN%2Fvz%2Fp0X3i6XciKMYoKvd4abE&X-Amz-Signature=7c0c547befff4b0a6171fbd6f50cd79cb0a2587d27d82ed50e977c47aa7039db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



