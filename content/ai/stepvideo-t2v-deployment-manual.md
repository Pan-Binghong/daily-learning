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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DU2TD5L%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBTGU7ho6lyCrK2YCGoQDySTVxnXysx4zLYqPlJ7VNEQAiBW7fod5QIPP0BlId%2Fj2kYiko6ojnZKkD7%2BRJL0d2IuCSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0C2k0YLI2E3glvCvKtwDhv87svexXVOxnNNyqKy5C1806zdzTp0I1f32rBPqFktkWZJ3ij7M%2B9qmTv963sjbF3Z1AbzkNZoF6p2aI4FCclPCLneR4XzZ6AHRZI%2BTRFfxlgMYBdpc67rZcNN0QHszhR%2BBgA166SnbQDoevp6Jj5WmwNaHGV58Uvwt3hvPxM8VUJrH0S%2B5y%2BjjQ3NDnSajUiW2UkpfgOVDdaidrNpbTedsyTpzkwftUy4FbXOZyttIJCb4ay6YMpBWY2JYZ5cvJ8e5hH4naJlvNPyPPgSq9njN%2FTsk6qXxZANib1xMUPHSrEcgksdMKFxxKDpgFHWEZBRhS1dUMVQE9iqRzpsapiA7BdXomeFzqIraC7VMLxPhQM5zKZ1xbEq8lrhGgmQeJcHWWEIkc3iPsJTEHPQ%2BAV1xIg1WGHS4pV%2B1v7%2Bjh76bnpsr%2BLegyReu7PSIQHVGu4fPkECPR6Cdn%2BJPkbcyodWXWoib8IykTz3t4Tsn4JFjEueQz4WWemeHLEWuEnUooXeZ37kY7018is%2FjEYD9vIKAaJ2z8PD%2FingNLGnxXkmkETQV2DPMtCVDiFzi3ibfls9YeVwF93RJ%2FIt%2Fwb2o1c4vPhPWES58%2FtOn3Bo0cVae0L0PbKJOjmwpBcowkri%2FyAY6pgHIwu%2FieIRnZ%2B%2FS7OiuKuscPBz%2BPsCsMzCBl5O8lTeGpRVlyXRvGvDS5XkNrDVWGOz6L%2Bk722MI3U5acrOpIKg28eO3KoLPvs0B%2BHbqtwqVWpEoVsJm4skT4H6qHXb%2FKO%2FTRTHMaoQXzKfbl2X1%2FY6vMHq8RDZWwPP%2FSaoAahePeqU1TZ%2FWeeAQkksVuk7pRfDxcbXaHA4fGi9%2FPoQiDkOpswdbknep&X-Amz-Signature=eafddd3b7faf4f6601ef86ed99924c9a6cdf8ff8e6bddd8004a0f212d9a052ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DU2TD5L%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBTGU7ho6lyCrK2YCGoQDySTVxnXysx4zLYqPlJ7VNEQAiBW7fod5QIPP0BlId%2Fj2kYiko6ojnZKkD7%2BRJL0d2IuCSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0C2k0YLI2E3glvCvKtwDhv87svexXVOxnNNyqKy5C1806zdzTp0I1f32rBPqFktkWZJ3ij7M%2B9qmTv963sjbF3Z1AbzkNZoF6p2aI4FCclPCLneR4XzZ6AHRZI%2BTRFfxlgMYBdpc67rZcNN0QHszhR%2BBgA166SnbQDoevp6Jj5WmwNaHGV58Uvwt3hvPxM8VUJrH0S%2B5y%2BjjQ3NDnSajUiW2UkpfgOVDdaidrNpbTedsyTpzkwftUy4FbXOZyttIJCb4ay6YMpBWY2JYZ5cvJ8e5hH4naJlvNPyPPgSq9njN%2FTsk6qXxZANib1xMUPHSrEcgksdMKFxxKDpgFHWEZBRhS1dUMVQE9iqRzpsapiA7BdXomeFzqIraC7VMLxPhQM5zKZ1xbEq8lrhGgmQeJcHWWEIkc3iPsJTEHPQ%2BAV1xIg1WGHS4pV%2B1v7%2Bjh76bnpsr%2BLegyReu7PSIQHVGu4fPkECPR6Cdn%2BJPkbcyodWXWoib8IykTz3t4Tsn4JFjEueQz4WWemeHLEWuEnUooXeZ37kY7018is%2FjEYD9vIKAaJ2z8PD%2FingNLGnxXkmkETQV2DPMtCVDiFzi3ibfls9YeVwF93RJ%2FIt%2Fwb2o1c4vPhPWES58%2FtOn3Bo0cVae0L0PbKJOjmwpBcowkri%2FyAY6pgHIwu%2FieIRnZ%2B%2FS7OiuKuscPBz%2BPsCsMzCBl5O8lTeGpRVlyXRvGvDS5XkNrDVWGOz6L%2Bk722MI3U5acrOpIKg28eO3KoLPvs0B%2BHbqtwqVWpEoVsJm4skT4H6qHXb%2FKO%2FTRTHMaoQXzKfbl2X1%2FY6vMHq8RDZWwPP%2FSaoAahePeqU1TZ%2FWeeAQkksVuk7pRfDxcbXaHA4fGi9%2FPoQiDkOpswdbknep&X-Amz-Signature=7d5a0d3905d74e419f64bb0028382bd4e026b19444cbcbd43f51fe93f7a7a5d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DU2TD5L%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBTGU7ho6lyCrK2YCGoQDySTVxnXysx4zLYqPlJ7VNEQAiBW7fod5QIPP0BlId%2Fj2kYiko6ojnZKkD7%2BRJL0d2IuCSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0C2k0YLI2E3glvCvKtwDhv87svexXVOxnNNyqKy5C1806zdzTp0I1f32rBPqFktkWZJ3ij7M%2B9qmTv963sjbF3Z1AbzkNZoF6p2aI4FCclPCLneR4XzZ6AHRZI%2BTRFfxlgMYBdpc67rZcNN0QHszhR%2BBgA166SnbQDoevp6Jj5WmwNaHGV58Uvwt3hvPxM8VUJrH0S%2B5y%2BjjQ3NDnSajUiW2UkpfgOVDdaidrNpbTedsyTpzkwftUy4FbXOZyttIJCb4ay6YMpBWY2JYZ5cvJ8e5hH4naJlvNPyPPgSq9njN%2FTsk6qXxZANib1xMUPHSrEcgksdMKFxxKDpgFHWEZBRhS1dUMVQE9iqRzpsapiA7BdXomeFzqIraC7VMLxPhQM5zKZ1xbEq8lrhGgmQeJcHWWEIkc3iPsJTEHPQ%2BAV1xIg1WGHS4pV%2B1v7%2Bjh76bnpsr%2BLegyReu7PSIQHVGu4fPkECPR6Cdn%2BJPkbcyodWXWoib8IykTz3t4Tsn4JFjEueQz4WWemeHLEWuEnUooXeZ37kY7018is%2FjEYD9vIKAaJ2z8PD%2FingNLGnxXkmkETQV2DPMtCVDiFzi3ibfls9YeVwF93RJ%2FIt%2Fwb2o1c4vPhPWES58%2FtOn3Bo0cVae0L0PbKJOjmwpBcowkri%2FyAY6pgHIwu%2FieIRnZ%2B%2FS7OiuKuscPBz%2BPsCsMzCBl5O8lTeGpRVlyXRvGvDS5XkNrDVWGOz6L%2Bk722MI3U5acrOpIKg28eO3KoLPvs0B%2BHbqtwqVWpEoVsJm4skT4H6qHXb%2FKO%2FTRTHMaoQXzKfbl2X1%2FY6vMHq8RDZWwPP%2FSaoAahePeqU1TZ%2FWeeAQkksVuk7pRfDxcbXaHA4fGi9%2FPoQiDkOpswdbknep&X-Amz-Signature=83693b0cd84819db25cdb648b5fa5b485f3f14ab279ed574f7a6de65a34f4a92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DU2TD5L%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBTGU7ho6lyCrK2YCGoQDySTVxnXysx4zLYqPlJ7VNEQAiBW7fod5QIPP0BlId%2Fj2kYiko6ojnZKkD7%2BRJL0d2IuCSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0C2k0YLI2E3glvCvKtwDhv87svexXVOxnNNyqKy5C1806zdzTp0I1f32rBPqFktkWZJ3ij7M%2B9qmTv963sjbF3Z1AbzkNZoF6p2aI4FCclPCLneR4XzZ6AHRZI%2BTRFfxlgMYBdpc67rZcNN0QHszhR%2BBgA166SnbQDoevp6Jj5WmwNaHGV58Uvwt3hvPxM8VUJrH0S%2B5y%2BjjQ3NDnSajUiW2UkpfgOVDdaidrNpbTedsyTpzkwftUy4FbXOZyttIJCb4ay6YMpBWY2JYZ5cvJ8e5hH4naJlvNPyPPgSq9njN%2FTsk6qXxZANib1xMUPHSrEcgksdMKFxxKDpgFHWEZBRhS1dUMVQE9iqRzpsapiA7BdXomeFzqIraC7VMLxPhQM5zKZ1xbEq8lrhGgmQeJcHWWEIkc3iPsJTEHPQ%2BAV1xIg1WGHS4pV%2B1v7%2Bjh76bnpsr%2BLegyReu7PSIQHVGu4fPkECPR6Cdn%2BJPkbcyodWXWoib8IykTz3t4Tsn4JFjEueQz4WWemeHLEWuEnUooXeZ37kY7018is%2FjEYD9vIKAaJ2z8PD%2FingNLGnxXkmkETQV2DPMtCVDiFzi3ibfls9YeVwF93RJ%2FIt%2Fwb2o1c4vPhPWES58%2FtOn3Bo0cVae0L0PbKJOjmwpBcowkri%2FyAY6pgHIwu%2FieIRnZ%2B%2FS7OiuKuscPBz%2BPsCsMzCBl5O8lTeGpRVlyXRvGvDS5XkNrDVWGOz6L%2Bk722MI3U5acrOpIKg28eO3KoLPvs0B%2BHbqtwqVWpEoVsJm4skT4H6qHXb%2FKO%2FTRTHMaoQXzKfbl2X1%2FY6vMHq8RDZWwPP%2FSaoAahePeqU1TZ%2FWeeAQkksVuk7pRfDxcbXaHA4fGi9%2FPoQiDkOpswdbknep&X-Amz-Signature=c8b056472f6901663c2d9258f0afcf350a2d30da5cd7b41cd30780564802ec10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



