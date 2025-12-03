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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRWM5JNH%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHubpatpwa8EVmihJ8pz%2BahWRS0p9bCY2EZM91Nax8SOAiAcFdr%2BWMzS1%2FODRgLKaEvC1BVoSC0W%2FuHcOe9dn1%2BLhCr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMf3BLZinSIITrXvk6KtwDqjPThFgvHHLOYIBwJMBn%2B%2F3l%2FOS3FxT50nuflCfLFrqJAfDWBcuDuA5F%2FXB4qs1cTnIdR%2ByH%2BINevDA0nvfYLDUu0W1PCCTiH574FoKsiWE6hDMs5c8nXlo0b0CQc0g1%2FLmLdDjuTNqMYjOdRACcmWltdo66cL7nNgyqjGReFBQpb42IMGSsbjUH3CrXPFbvEFdLkFD4Me7dD9gG%2Bip4yUz6FKraqcFaSmarnYqwrj5FS9yNCXIrkOY9j7Vs42hUNhZD%2BhVX2%2FV1tHURT3kk%2B%2FZbu1EfVQ%2BcsE%2F9m5vJIc8r0WcM12CZuhQ9kPDwmvSh7%2BzZHgM0Ir3yFRY5Q5PmE1igQiROrwCiAXFzyxnDhyemLWeMOUwBJhtPEpTlgjY0EpE4wLg4PWccBhxa6msRTXnI3GKanPP9H5Hvi36GnNyc4VgR%2F%2FYPyATGEHKh1P2wPCfgo590%2BoqCQa1k6y6uzWQ1DC8FLxgSZ2OoXbbKeFYqGAmpIN3Wl2JPJfEmleaBBjjEnuiT54ZlZ1zCHw1Il%2BFil1mW%2F1XI0ZhoRYbcTSyS4e3atVKmPf5hBZ50wGxs%2F%2BXDHL5jJ4NK%2FmjVG3WzR65RFV7NLLFJm0wZbdXHVqS55QCdHkn6yxnIfEwwl5a%2ByQY6pgGtNZ%2Frs5oXGsVH%2BWQgZXdVFubwctGd357qazCAld8NACchiKsC%2FBjoSP%2FIf2gNJH0496D72zGFcy1DBvjPnDn2qV5f0QvSrB%2B92UUm9xbgNmZlDw47WR3iWkJtEWeZLWcHBkBIJahSUaClyVv8Ti3LKZCF10GwFNQW6YUPHkXK1sFCIpfaj5PzZZf%2Fzy8C1idJIYqsecjgIlCh8gQ4rkl0t%2FzWe2wq&X-Amz-Signature=afe51edb0e660f3fc4fb0956d9e23588a23eb83f5a0be23a2189cf05a76f9139&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRWM5JNH%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHubpatpwa8EVmihJ8pz%2BahWRS0p9bCY2EZM91Nax8SOAiAcFdr%2BWMzS1%2FODRgLKaEvC1BVoSC0W%2FuHcOe9dn1%2BLhCr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMf3BLZinSIITrXvk6KtwDqjPThFgvHHLOYIBwJMBn%2B%2F3l%2FOS3FxT50nuflCfLFrqJAfDWBcuDuA5F%2FXB4qs1cTnIdR%2ByH%2BINevDA0nvfYLDUu0W1PCCTiH574FoKsiWE6hDMs5c8nXlo0b0CQc0g1%2FLmLdDjuTNqMYjOdRACcmWltdo66cL7nNgyqjGReFBQpb42IMGSsbjUH3CrXPFbvEFdLkFD4Me7dD9gG%2Bip4yUz6FKraqcFaSmarnYqwrj5FS9yNCXIrkOY9j7Vs42hUNhZD%2BhVX2%2FV1tHURT3kk%2B%2FZbu1EfVQ%2BcsE%2F9m5vJIc8r0WcM12CZuhQ9kPDwmvSh7%2BzZHgM0Ir3yFRY5Q5PmE1igQiROrwCiAXFzyxnDhyemLWeMOUwBJhtPEpTlgjY0EpE4wLg4PWccBhxa6msRTXnI3GKanPP9H5Hvi36GnNyc4VgR%2F%2FYPyATGEHKh1P2wPCfgo590%2BoqCQa1k6y6uzWQ1DC8FLxgSZ2OoXbbKeFYqGAmpIN3Wl2JPJfEmleaBBjjEnuiT54ZlZ1zCHw1Il%2BFil1mW%2F1XI0ZhoRYbcTSyS4e3atVKmPf5hBZ50wGxs%2F%2BXDHL5jJ4NK%2FmjVG3WzR65RFV7NLLFJm0wZbdXHVqS55QCdHkn6yxnIfEwwl5a%2ByQY6pgGtNZ%2Frs5oXGsVH%2BWQgZXdVFubwctGd357qazCAld8NACchiKsC%2FBjoSP%2FIf2gNJH0496D72zGFcy1DBvjPnDn2qV5f0QvSrB%2B92UUm9xbgNmZlDw47WR3iWkJtEWeZLWcHBkBIJahSUaClyVv8Ti3LKZCF10GwFNQW6YUPHkXK1sFCIpfaj5PzZZf%2Fzy8C1idJIYqsecjgIlCh8gQ4rkl0t%2FzWe2wq&X-Amz-Signature=801c326ee2a0a60fce29219075278f3d723a1a3d5a66bf3dce470fac58d296a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRWM5JNH%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHubpatpwa8EVmihJ8pz%2BahWRS0p9bCY2EZM91Nax8SOAiAcFdr%2BWMzS1%2FODRgLKaEvC1BVoSC0W%2FuHcOe9dn1%2BLhCr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMf3BLZinSIITrXvk6KtwDqjPThFgvHHLOYIBwJMBn%2B%2F3l%2FOS3FxT50nuflCfLFrqJAfDWBcuDuA5F%2FXB4qs1cTnIdR%2ByH%2BINevDA0nvfYLDUu0W1PCCTiH574FoKsiWE6hDMs5c8nXlo0b0CQc0g1%2FLmLdDjuTNqMYjOdRACcmWltdo66cL7nNgyqjGReFBQpb42IMGSsbjUH3CrXPFbvEFdLkFD4Me7dD9gG%2Bip4yUz6FKraqcFaSmarnYqwrj5FS9yNCXIrkOY9j7Vs42hUNhZD%2BhVX2%2FV1tHURT3kk%2B%2FZbu1EfVQ%2BcsE%2F9m5vJIc8r0WcM12CZuhQ9kPDwmvSh7%2BzZHgM0Ir3yFRY5Q5PmE1igQiROrwCiAXFzyxnDhyemLWeMOUwBJhtPEpTlgjY0EpE4wLg4PWccBhxa6msRTXnI3GKanPP9H5Hvi36GnNyc4VgR%2F%2FYPyATGEHKh1P2wPCfgo590%2BoqCQa1k6y6uzWQ1DC8FLxgSZ2OoXbbKeFYqGAmpIN3Wl2JPJfEmleaBBjjEnuiT54ZlZ1zCHw1Il%2BFil1mW%2F1XI0ZhoRYbcTSyS4e3atVKmPf5hBZ50wGxs%2F%2BXDHL5jJ4NK%2FmjVG3WzR65RFV7NLLFJm0wZbdXHVqS55QCdHkn6yxnIfEwwl5a%2ByQY6pgGtNZ%2Frs5oXGsVH%2BWQgZXdVFubwctGd357qazCAld8NACchiKsC%2FBjoSP%2FIf2gNJH0496D72zGFcy1DBvjPnDn2qV5f0QvSrB%2B92UUm9xbgNmZlDw47WR3iWkJtEWeZLWcHBkBIJahSUaClyVv8Ti3LKZCF10GwFNQW6YUPHkXK1sFCIpfaj5PzZZf%2Fzy8C1idJIYqsecjgIlCh8gQ4rkl0t%2FzWe2wq&X-Amz-Signature=fa644772b4a54e505a33afea48d15c2f299e53efca0d38611dd7a7d05827ee5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRWM5JNH%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHubpatpwa8EVmihJ8pz%2BahWRS0p9bCY2EZM91Nax8SOAiAcFdr%2BWMzS1%2FODRgLKaEvC1BVoSC0W%2FuHcOe9dn1%2BLhCr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMf3BLZinSIITrXvk6KtwDqjPThFgvHHLOYIBwJMBn%2B%2F3l%2FOS3FxT50nuflCfLFrqJAfDWBcuDuA5F%2FXB4qs1cTnIdR%2ByH%2BINevDA0nvfYLDUu0W1PCCTiH574FoKsiWE6hDMs5c8nXlo0b0CQc0g1%2FLmLdDjuTNqMYjOdRACcmWltdo66cL7nNgyqjGReFBQpb42IMGSsbjUH3CrXPFbvEFdLkFD4Me7dD9gG%2Bip4yUz6FKraqcFaSmarnYqwrj5FS9yNCXIrkOY9j7Vs42hUNhZD%2BhVX2%2FV1tHURT3kk%2B%2FZbu1EfVQ%2BcsE%2F9m5vJIc8r0WcM12CZuhQ9kPDwmvSh7%2BzZHgM0Ir3yFRY5Q5PmE1igQiROrwCiAXFzyxnDhyemLWeMOUwBJhtPEpTlgjY0EpE4wLg4PWccBhxa6msRTXnI3GKanPP9H5Hvi36GnNyc4VgR%2F%2FYPyATGEHKh1P2wPCfgo590%2BoqCQa1k6y6uzWQ1DC8FLxgSZ2OoXbbKeFYqGAmpIN3Wl2JPJfEmleaBBjjEnuiT54ZlZ1zCHw1Il%2BFil1mW%2F1XI0ZhoRYbcTSyS4e3atVKmPf5hBZ50wGxs%2F%2BXDHL5jJ4NK%2FmjVG3WzR65RFV7NLLFJm0wZbdXHVqS55QCdHkn6yxnIfEwwl5a%2ByQY6pgGtNZ%2Frs5oXGsVH%2BWQgZXdVFubwctGd357qazCAld8NACchiKsC%2FBjoSP%2FIf2gNJH0496D72zGFcy1DBvjPnDn2qV5f0QvSrB%2B92UUm9xbgNmZlDw47WR3iWkJtEWeZLWcHBkBIJahSUaClyVv8Ti3LKZCF10GwFNQW6YUPHkXK1sFCIpfaj5PzZZf%2Fzy8C1idJIYqsecjgIlCh8gQ4rkl0t%2FzWe2wq&X-Amz-Signature=591ea2ed8b671567c19c8607cee1a52ca45a5562ec058b3bab79b13e8b8950e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



