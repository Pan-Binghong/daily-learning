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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPFR7IXV%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE9EQPM48S04uAGnA%2FFJnSaHfHvb5BIbLnx088dYl03AIhAOGichWbV63Hlh%2BgQljXfOnoOsAQTdz%2B%2BTWOUY1B3hDEKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxbl7GHTYrTVCY1Yxcq3APuKes7YmhKAAS8%2F7anAz1%2FqHPz7TI8wXO6w1iAeSJZFIPFNfebnul23SSicRIWpsGTSd7dK4rhfrBEZJhMZKo2%2B4SumgS%2FxUUBsR5ZyaSNW2KrOsSKjgSQxQmzUFZD%2BzvIQo7jrWN3%2F63fcAfEKFEBASnjTLobhE%2BKMtxVtLkXsjKzScf9bwZt0O2lqjNpSIKriY1MGif2d7uXw2N%2FIm6LcBNN51iA2Me5b%2F1Tmgi62IB5KJ1mRxa%2Bb9fvQTin9Lm7FnhjXnbBVHDdp%2Fsq6s10nkpzmU91we%2Fd9ipwGCc%2BoeABfaIwVQakcqaNcw%2FuVvr8MSHSD8ntdLcipDszOHp5Jk%2F0BpTBLaD6SAKqV69Y3yQXtcA5pRjwLOrneoa3rmOGKaxC70%2FFShsXVgnGDrkGutGjAb1lmplNj9dQurSGPzgHoXvXUR%2FbUeokpDomw0iarllY6Sbw7NZUvJd%2FjKkFIhkiyhsqZzONNnzoGxfBqrGmtQ6cOXgiV4SMunC6mQzP%2B2iHBuDXy1L9DAThTjT8AjK4nuOtk0sbTrpIq9h3SdjTVCno9%2FydPz%2FxaCbZNYR7tcg2Ocmu5QU90gD%2Fd0Ql0s8wpEhMPNHBPji8HXCH2Kdt6JEWA2Qze7KPsTCTxYHLBjqkAVMGfZVOi8Bb%2FnhvZGq7FPMmXCAz6W7o7m9iqXNDyBmIS4e8IDCd0qM7A0%2BKbOHDl7iIt3XFzXW1TDhCe8jMIctPOdVoycMc67jRTW9SvSQbzYc5SVsnHHMFWqOg1%2BXNXjbFIrEZO8O1PcZz%2FQQKEaMhHFxIhm%2F29Zj9IWa6EveDIVBs4rRdZ85AqkFnfCG%2FQzHr8sH1%2FUNYTUBGc5Z3x0K3o0e%2B&X-Amz-Signature=b385c842d182e91199b020a829e1e513b2c2bcb1a2bfc9183a443d66b777f4b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPFR7IXV%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE9EQPM48S04uAGnA%2FFJnSaHfHvb5BIbLnx088dYl03AIhAOGichWbV63Hlh%2BgQljXfOnoOsAQTdz%2B%2BTWOUY1B3hDEKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxbl7GHTYrTVCY1Yxcq3APuKes7YmhKAAS8%2F7anAz1%2FqHPz7TI8wXO6w1iAeSJZFIPFNfebnul23SSicRIWpsGTSd7dK4rhfrBEZJhMZKo2%2B4SumgS%2FxUUBsR5ZyaSNW2KrOsSKjgSQxQmzUFZD%2BzvIQo7jrWN3%2F63fcAfEKFEBASnjTLobhE%2BKMtxVtLkXsjKzScf9bwZt0O2lqjNpSIKriY1MGif2d7uXw2N%2FIm6LcBNN51iA2Me5b%2F1Tmgi62IB5KJ1mRxa%2Bb9fvQTin9Lm7FnhjXnbBVHDdp%2Fsq6s10nkpzmU91we%2Fd9ipwGCc%2BoeABfaIwVQakcqaNcw%2FuVvr8MSHSD8ntdLcipDszOHp5Jk%2F0BpTBLaD6SAKqV69Y3yQXtcA5pRjwLOrneoa3rmOGKaxC70%2FFShsXVgnGDrkGutGjAb1lmplNj9dQurSGPzgHoXvXUR%2FbUeokpDomw0iarllY6Sbw7NZUvJd%2FjKkFIhkiyhsqZzONNnzoGxfBqrGmtQ6cOXgiV4SMunC6mQzP%2B2iHBuDXy1L9DAThTjT8AjK4nuOtk0sbTrpIq9h3SdjTVCno9%2FydPz%2FxaCbZNYR7tcg2Ocmu5QU90gD%2Fd0Ql0s8wpEhMPNHBPji8HXCH2Kdt6JEWA2Qze7KPsTCTxYHLBjqkAVMGfZVOi8Bb%2FnhvZGq7FPMmXCAz6W7o7m9iqXNDyBmIS4e8IDCd0qM7A0%2BKbOHDl7iIt3XFzXW1TDhCe8jMIctPOdVoycMc67jRTW9SvSQbzYc5SVsnHHMFWqOg1%2BXNXjbFIrEZO8O1PcZz%2FQQKEaMhHFxIhm%2F29Zj9IWa6EveDIVBs4rRdZ85AqkFnfCG%2FQzHr8sH1%2FUNYTUBGc5Z3x0K3o0e%2B&X-Amz-Signature=059b2bc79981ff382d13205781dadfdb9f1ec40e0ee9904b8020ae01efb3a14d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPFR7IXV%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE9EQPM48S04uAGnA%2FFJnSaHfHvb5BIbLnx088dYl03AIhAOGichWbV63Hlh%2BgQljXfOnoOsAQTdz%2B%2BTWOUY1B3hDEKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxbl7GHTYrTVCY1Yxcq3APuKes7YmhKAAS8%2F7anAz1%2FqHPz7TI8wXO6w1iAeSJZFIPFNfebnul23SSicRIWpsGTSd7dK4rhfrBEZJhMZKo2%2B4SumgS%2FxUUBsR5ZyaSNW2KrOsSKjgSQxQmzUFZD%2BzvIQo7jrWN3%2F63fcAfEKFEBASnjTLobhE%2BKMtxVtLkXsjKzScf9bwZt0O2lqjNpSIKriY1MGif2d7uXw2N%2FIm6LcBNN51iA2Me5b%2F1Tmgi62IB5KJ1mRxa%2Bb9fvQTin9Lm7FnhjXnbBVHDdp%2Fsq6s10nkpzmU91we%2Fd9ipwGCc%2BoeABfaIwVQakcqaNcw%2FuVvr8MSHSD8ntdLcipDszOHp5Jk%2F0BpTBLaD6SAKqV69Y3yQXtcA5pRjwLOrneoa3rmOGKaxC70%2FFShsXVgnGDrkGutGjAb1lmplNj9dQurSGPzgHoXvXUR%2FbUeokpDomw0iarllY6Sbw7NZUvJd%2FjKkFIhkiyhsqZzONNnzoGxfBqrGmtQ6cOXgiV4SMunC6mQzP%2B2iHBuDXy1L9DAThTjT8AjK4nuOtk0sbTrpIq9h3SdjTVCno9%2FydPz%2FxaCbZNYR7tcg2Ocmu5QU90gD%2Fd0Ql0s8wpEhMPNHBPji8HXCH2Kdt6JEWA2Qze7KPsTCTxYHLBjqkAVMGfZVOi8Bb%2FnhvZGq7FPMmXCAz6W7o7m9iqXNDyBmIS4e8IDCd0qM7A0%2BKbOHDl7iIt3XFzXW1TDhCe8jMIctPOdVoycMc67jRTW9SvSQbzYc5SVsnHHMFWqOg1%2BXNXjbFIrEZO8O1PcZz%2FQQKEaMhHFxIhm%2F29Zj9IWa6EveDIVBs4rRdZ85AqkFnfCG%2FQzHr8sH1%2FUNYTUBGc5Z3x0K3o0e%2B&X-Amz-Signature=b4586ed6b9cc3fc902eb6896bd73f44ebcd0e56a0b3fa30708a8bfae8db05c5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPFR7IXV%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE9EQPM48S04uAGnA%2FFJnSaHfHvb5BIbLnx088dYl03AIhAOGichWbV63Hlh%2BgQljXfOnoOsAQTdz%2B%2BTWOUY1B3hDEKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxbl7GHTYrTVCY1Yxcq3APuKes7YmhKAAS8%2F7anAz1%2FqHPz7TI8wXO6w1iAeSJZFIPFNfebnul23SSicRIWpsGTSd7dK4rhfrBEZJhMZKo2%2B4SumgS%2FxUUBsR5ZyaSNW2KrOsSKjgSQxQmzUFZD%2BzvIQo7jrWN3%2F63fcAfEKFEBASnjTLobhE%2BKMtxVtLkXsjKzScf9bwZt0O2lqjNpSIKriY1MGif2d7uXw2N%2FIm6LcBNN51iA2Me5b%2F1Tmgi62IB5KJ1mRxa%2Bb9fvQTin9Lm7FnhjXnbBVHDdp%2Fsq6s10nkpzmU91we%2Fd9ipwGCc%2BoeABfaIwVQakcqaNcw%2FuVvr8MSHSD8ntdLcipDszOHp5Jk%2F0BpTBLaD6SAKqV69Y3yQXtcA5pRjwLOrneoa3rmOGKaxC70%2FFShsXVgnGDrkGutGjAb1lmplNj9dQurSGPzgHoXvXUR%2FbUeokpDomw0iarllY6Sbw7NZUvJd%2FjKkFIhkiyhsqZzONNnzoGxfBqrGmtQ6cOXgiV4SMunC6mQzP%2B2iHBuDXy1L9DAThTjT8AjK4nuOtk0sbTrpIq9h3SdjTVCno9%2FydPz%2FxaCbZNYR7tcg2Ocmu5QU90gD%2Fd0Ql0s8wpEhMPNHBPji8HXCH2Kdt6JEWA2Qze7KPsTCTxYHLBjqkAVMGfZVOi8Bb%2FnhvZGq7FPMmXCAz6W7o7m9iqXNDyBmIS4e8IDCd0qM7A0%2BKbOHDl7iIt3XFzXW1TDhCe8jMIctPOdVoycMc67jRTW9SvSQbzYc5SVsnHHMFWqOg1%2BXNXjbFIrEZO8O1PcZz%2FQQKEaMhHFxIhm%2F29Zj9IWa6EveDIVBs4rRdZ85AqkFnfCG%2FQzHr8sH1%2FUNYTUBGc5Z3x0K3o0e%2B&X-Amz-Signature=385b976559571f1f477ef9d222c9148c1136b1c1a929ddf717b506f4fc0c3d9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



