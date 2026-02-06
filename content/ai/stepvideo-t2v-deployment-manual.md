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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRZMEXRH%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FuBdu2vcaLJeY%2B0IKsQlTizc0n9GMlPWAinLaZD8CgIhAKQxCcQalc2n1Rlt%2BTDSgpolTnFrWS4pmUYekzxjCsJfKv8DCDwQABoMNjM3NDIzMTgzODA1IgwerFSud%2B6m6Dsns1sq3APm05vHlcjQ0rnN42GkSRJkm%2BCFv3aYPnVszKMteD9OjYHGG6cS%2FJ%2F2r3bSLSKOYETXTWhzAD1J6zmgd0sIS7UipVDGtvmnCyfNrf2p7M8aTyhrRTCcCa6otip07%2BJXsJmU2MdZ86I%2FXrFblGIF5kSpZOsdm943wJi%2FqimJZ1hwEWToCyXFzKovFJ%2BYOfDIZ%2F3Sc%2Bt2%2BrSfZhqioMy4hlkcVtCvUdzaWkCGIZnI3WAhKZLZSNGiL5DBNYjLdeMUidMZiPXh%2BqF9uCNBko0q9wnZxxlbmP0xt7utXy1B3m%2FiLQvaDTgSuQY6rcIboIJE4eOF70EIHNpsyMSsFCKYKbYMiluavjgBqakx%2BwQ%2BuwQ0HFgE%2BefkktRd2veSpaF5T5tG4lp%2BbMbQHZ5V%2F2Iy%2F6o%2FBNNtIoz3kGVNItpZ5TGRzokmFDDx0yMlIe2EleAVJfdi59aUE7LWrnVM20yFEDHGYL6QQQ9ymH3yxhuc5RAIeFVbTWe9pPfJltI5%2BbZ1AztQpctFmSRic3yVsd%2F6X3Njlf1AfqYednHxEqyx0AV8e5GQWH9TdYKkGUmIczxU%2B9wd2D4Eq%2BsevaJBXNevy%2FxOG9fuTwmVT%2FnEzo5XkF3SPH6Cdet%2BICkQEKHYujDKu5XMBjqkAWoGMdk7NZ1598a9Dfjl2Oo3o%2FomaWv8zD65btpu9eGO1y4NGcCptGk2MyZdB0VHKDVaMKAPZvtrmdtWSLEbTfOmJLs3LjOq4xQM81sq9dUE2m5IJKlyHH0R2N%2FYWiUkKmt47s23rTMvvXBsbif20xIzYR5FAte28nmVGky8Ew%2BrzfHWtcvPrUthQzec4iOtZonjtPy3QpBDEuCibN2I4tJZSAd1&X-Amz-Signature=1c863f0e423c0770ff03e993512f421873ab15ebd1996dfc271040e6f050b797&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRZMEXRH%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FuBdu2vcaLJeY%2B0IKsQlTizc0n9GMlPWAinLaZD8CgIhAKQxCcQalc2n1Rlt%2BTDSgpolTnFrWS4pmUYekzxjCsJfKv8DCDwQABoMNjM3NDIzMTgzODA1IgwerFSud%2B6m6Dsns1sq3APm05vHlcjQ0rnN42GkSRJkm%2BCFv3aYPnVszKMteD9OjYHGG6cS%2FJ%2F2r3bSLSKOYETXTWhzAD1J6zmgd0sIS7UipVDGtvmnCyfNrf2p7M8aTyhrRTCcCa6otip07%2BJXsJmU2MdZ86I%2FXrFblGIF5kSpZOsdm943wJi%2FqimJZ1hwEWToCyXFzKovFJ%2BYOfDIZ%2F3Sc%2Bt2%2BrSfZhqioMy4hlkcVtCvUdzaWkCGIZnI3WAhKZLZSNGiL5DBNYjLdeMUidMZiPXh%2BqF9uCNBko0q9wnZxxlbmP0xt7utXy1B3m%2FiLQvaDTgSuQY6rcIboIJE4eOF70EIHNpsyMSsFCKYKbYMiluavjgBqakx%2BwQ%2BuwQ0HFgE%2BefkktRd2veSpaF5T5tG4lp%2BbMbQHZ5V%2F2Iy%2F6o%2FBNNtIoz3kGVNItpZ5TGRzokmFDDx0yMlIe2EleAVJfdi59aUE7LWrnVM20yFEDHGYL6QQQ9ymH3yxhuc5RAIeFVbTWe9pPfJltI5%2BbZ1AztQpctFmSRic3yVsd%2F6X3Njlf1AfqYednHxEqyx0AV8e5GQWH9TdYKkGUmIczxU%2B9wd2D4Eq%2BsevaJBXNevy%2FxOG9fuTwmVT%2FnEzo5XkF3SPH6Cdet%2BICkQEKHYujDKu5XMBjqkAWoGMdk7NZ1598a9Dfjl2Oo3o%2FomaWv8zD65btpu9eGO1y4NGcCptGk2MyZdB0VHKDVaMKAPZvtrmdtWSLEbTfOmJLs3LjOq4xQM81sq9dUE2m5IJKlyHH0R2N%2FYWiUkKmt47s23rTMvvXBsbif20xIzYR5FAte28nmVGky8Ew%2BrzfHWtcvPrUthQzec4iOtZonjtPy3QpBDEuCibN2I4tJZSAd1&X-Amz-Signature=a6418545e26ccb2495558b356600cc7d965903db9f84c0851420e78b84315c20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRZMEXRH%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FuBdu2vcaLJeY%2B0IKsQlTizc0n9GMlPWAinLaZD8CgIhAKQxCcQalc2n1Rlt%2BTDSgpolTnFrWS4pmUYekzxjCsJfKv8DCDwQABoMNjM3NDIzMTgzODA1IgwerFSud%2B6m6Dsns1sq3APm05vHlcjQ0rnN42GkSRJkm%2BCFv3aYPnVszKMteD9OjYHGG6cS%2FJ%2F2r3bSLSKOYETXTWhzAD1J6zmgd0sIS7UipVDGtvmnCyfNrf2p7M8aTyhrRTCcCa6otip07%2BJXsJmU2MdZ86I%2FXrFblGIF5kSpZOsdm943wJi%2FqimJZ1hwEWToCyXFzKovFJ%2BYOfDIZ%2F3Sc%2Bt2%2BrSfZhqioMy4hlkcVtCvUdzaWkCGIZnI3WAhKZLZSNGiL5DBNYjLdeMUidMZiPXh%2BqF9uCNBko0q9wnZxxlbmP0xt7utXy1B3m%2FiLQvaDTgSuQY6rcIboIJE4eOF70EIHNpsyMSsFCKYKbYMiluavjgBqakx%2BwQ%2BuwQ0HFgE%2BefkktRd2veSpaF5T5tG4lp%2BbMbQHZ5V%2F2Iy%2F6o%2FBNNtIoz3kGVNItpZ5TGRzokmFDDx0yMlIe2EleAVJfdi59aUE7LWrnVM20yFEDHGYL6QQQ9ymH3yxhuc5RAIeFVbTWe9pPfJltI5%2BbZ1AztQpctFmSRic3yVsd%2F6X3Njlf1AfqYednHxEqyx0AV8e5GQWH9TdYKkGUmIczxU%2B9wd2D4Eq%2BsevaJBXNevy%2FxOG9fuTwmVT%2FnEzo5XkF3SPH6Cdet%2BICkQEKHYujDKu5XMBjqkAWoGMdk7NZ1598a9Dfjl2Oo3o%2FomaWv8zD65btpu9eGO1y4NGcCptGk2MyZdB0VHKDVaMKAPZvtrmdtWSLEbTfOmJLs3LjOq4xQM81sq9dUE2m5IJKlyHH0R2N%2FYWiUkKmt47s23rTMvvXBsbif20xIzYR5FAte28nmVGky8Ew%2BrzfHWtcvPrUthQzec4iOtZonjtPy3QpBDEuCibN2I4tJZSAd1&X-Amz-Signature=f0232f91daeee3d8f1fac3a03edab993582da61c6e1ee9a1d7c7db768c3ef6cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRZMEXRH%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQD%2F%2FuBdu2vcaLJeY%2B0IKsQlTizc0n9GMlPWAinLaZD8CgIhAKQxCcQalc2n1Rlt%2BTDSgpolTnFrWS4pmUYekzxjCsJfKv8DCDwQABoMNjM3NDIzMTgzODA1IgwerFSud%2B6m6Dsns1sq3APm05vHlcjQ0rnN42GkSRJkm%2BCFv3aYPnVszKMteD9OjYHGG6cS%2FJ%2F2r3bSLSKOYETXTWhzAD1J6zmgd0sIS7UipVDGtvmnCyfNrf2p7M8aTyhrRTCcCa6otip07%2BJXsJmU2MdZ86I%2FXrFblGIF5kSpZOsdm943wJi%2FqimJZ1hwEWToCyXFzKovFJ%2BYOfDIZ%2F3Sc%2Bt2%2BrSfZhqioMy4hlkcVtCvUdzaWkCGIZnI3WAhKZLZSNGiL5DBNYjLdeMUidMZiPXh%2BqF9uCNBko0q9wnZxxlbmP0xt7utXy1B3m%2FiLQvaDTgSuQY6rcIboIJE4eOF70EIHNpsyMSsFCKYKbYMiluavjgBqakx%2BwQ%2BuwQ0HFgE%2BefkktRd2veSpaF5T5tG4lp%2BbMbQHZ5V%2F2Iy%2F6o%2FBNNtIoz3kGVNItpZ5TGRzokmFDDx0yMlIe2EleAVJfdi59aUE7LWrnVM20yFEDHGYL6QQQ9ymH3yxhuc5RAIeFVbTWe9pPfJltI5%2BbZ1AztQpctFmSRic3yVsd%2F6X3Njlf1AfqYednHxEqyx0AV8e5GQWH9TdYKkGUmIczxU%2B9wd2D4Eq%2BsevaJBXNevy%2FxOG9fuTwmVT%2FnEzo5XkF3SPH6Cdet%2BICkQEKHYujDKu5XMBjqkAWoGMdk7NZ1598a9Dfjl2Oo3o%2FomaWv8zD65btpu9eGO1y4NGcCptGk2MyZdB0VHKDVaMKAPZvtrmdtWSLEbTfOmJLs3LjOq4xQM81sq9dUE2m5IJKlyHH0R2N%2FYWiUkKmt47s23rTMvvXBsbif20xIzYR5FAte28nmVGky8Ew%2BrzfHWtcvPrUthQzec4iOtZonjtPy3QpBDEuCibN2I4tJZSAd1&X-Amz-Signature=c1e3cb2d9d17637689ed8e668eeb30a0d872796a293aa9599926fa299532a763&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



