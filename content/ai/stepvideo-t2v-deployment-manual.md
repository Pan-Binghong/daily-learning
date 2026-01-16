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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FNYJSK%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCE8mckucPvrceFPRGWFgdszV%2BtUPd%2FZjZwLmNDyZeg2AIgR3MnKHfXBTCY8eSqTPwubLFX997fG08i%2Bt4b7B4m9Ewq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNjByVavv5F187ZJ8CrcA8Fcc1uHeKunz%2BoZ5TbfVv4mSQmOgiXxxx%2FY%2BbS6GeBdhRtKevt17WC60Z1zlU%2BauTqSNEV0gq1ejEB5agJTxwLaRY0Hs8mWYr0gESP%2F3HayYJhPUSHZNE8WKF3de3VTpbQ4Ie2iZA4qmOtuUBKjO1lbb0gTrxD7iE0cHpIh6L5XsmQVOIFXFbXr%2Bj1x8qjY%2B70Y%2Fig8KTtQkKS4QYv9WA0CspIPleyCCtxq0ofuOzEa%2BPxytr70EVOS1A02HJHFZVW%2FwOUbdDOruo33VjdUy84QuUAZaeoFrtXsk3MPsi%2FUvZ7DA3RSzxhzokFvR1Xlx9XXpRDm8HRueUmfFwL6zI1VL1ZjkOkkO%2FaZ36DnQTtlWJ1uBrewsICe9oyEOngt4wmMASc9rziePJ4uRPa0X6K6eKiy8qnEhuwSc0M9JXtvIxqyvy2sOtegEGMntd0BZ5Alok3uABZZ1VNWsdU9u4PAelWoykfYPtnPZeE2itpCkxm90ftTdCv3p%2FHtWPay2tEDsbqhRfZHJs%2BU2a8GLr6tiCus7L93FDz5yd4TcjfOoOJokhf%2F8zGTo%2FtlzK0kaSNZjI4KG6bnUF7G5CxqUsKirN9%2BaI3F8TvdiwhAsu00d%2B%2BORfEDCk%2F4BI4hMIDApssGOqUBMfQaQBDGw0JcJWkJNl8FItQXInEyK8kjRCPmtaebofsqr74NR%2Bc%2F%2F3%2F75zGOgr0tF3sqFsiwIsUcCcYsXO%2Bur4mbfmAsIUP4lKlko2tto9VeHiqVieevaSzk%2BFT3J7bGoL9RQ1UWnWVi2%2BmFFb05llyPd5cp%2Fqvun2%2FEZLLH7RLK%2BEO0XFdTJHBy1uF2V9wb9kR4POFGGEnjvrwE6D%2B900kL2KR%2F&X-Amz-Signature=adfec1292aee9278dc21ac0dfdcdd75f328c70fa61220d655428fee00052f0cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FNYJSK%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCE8mckucPvrceFPRGWFgdszV%2BtUPd%2FZjZwLmNDyZeg2AIgR3MnKHfXBTCY8eSqTPwubLFX997fG08i%2Bt4b7B4m9Ewq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNjByVavv5F187ZJ8CrcA8Fcc1uHeKunz%2BoZ5TbfVv4mSQmOgiXxxx%2FY%2BbS6GeBdhRtKevt17WC60Z1zlU%2BauTqSNEV0gq1ejEB5agJTxwLaRY0Hs8mWYr0gESP%2F3HayYJhPUSHZNE8WKF3de3VTpbQ4Ie2iZA4qmOtuUBKjO1lbb0gTrxD7iE0cHpIh6L5XsmQVOIFXFbXr%2Bj1x8qjY%2B70Y%2Fig8KTtQkKS4QYv9WA0CspIPleyCCtxq0ofuOzEa%2BPxytr70EVOS1A02HJHFZVW%2FwOUbdDOruo33VjdUy84QuUAZaeoFrtXsk3MPsi%2FUvZ7DA3RSzxhzokFvR1Xlx9XXpRDm8HRueUmfFwL6zI1VL1ZjkOkkO%2FaZ36DnQTtlWJ1uBrewsICe9oyEOngt4wmMASc9rziePJ4uRPa0X6K6eKiy8qnEhuwSc0M9JXtvIxqyvy2sOtegEGMntd0BZ5Alok3uABZZ1VNWsdU9u4PAelWoykfYPtnPZeE2itpCkxm90ftTdCv3p%2FHtWPay2tEDsbqhRfZHJs%2BU2a8GLr6tiCus7L93FDz5yd4TcjfOoOJokhf%2F8zGTo%2FtlzK0kaSNZjI4KG6bnUF7G5CxqUsKirN9%2BaI3F8TvdiwhAsu00d%2B%2BORfEDCk%2F4BI4hMIDApssGOqUBMfQaQBDGw0JcJWkJNl8FItQXInEyK8kjRCPmtaebofsqr74NR%2Bc%2F%2F3%2F75zGOgr0tF3sqFsiwIsUcCcYsXO%2Bur4mbfmAsIUP4lKlko2tto9VeHiqVieevaSzk%2BFT3J7bGoL9RQ1UWnWVi2%2BmFFb05llyPd5cp%2Fqvun2%2FEZLLH7RLK%2BEO0XFdTJHBy1uF2V9wb9kR4POFGGEnjvrwE6D%2B900kL2KR%2F&X-Amz-Signature=903890d195566ea50626c45f39deab51836a633d9bb9bced5ae98fab9b7cf976&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FNYJSK%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCE8mckucPvrceFPRGWFgdszV%2BtUPd%2FZjZwLmNDyZeg2AIgR3MnKHfXBTCY8eSqTPwubLFX997fG08i%2Bt4b7B4m9Ewq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNjByVavv5F187ZJ8CrcA8Fcc1uHeKunz%2BoZ5TbfVv4mSQmOgiXxxx%2FY%2BbS6GeBdhRtKevt17WC60Z1zlU%2BauTqSNEV0gq1ejEB5agJTxwLaRY0Hs8mWYr0gESP%2F3HayYJhPUSHZNE8WKF3de3VTpbQ4Ie2iZA4qmOtuUBKjO1lbb0gTrxD7iE0cHpIh6L5XsmQVOIFXFbXr%2Bj1x8qjY%2B70Y%2Fig8KTtQkKS4QYv9WA0CspIPleyCCtxq0ofuOzEa%2BPxytr70EVOS1A02HJHFZVW%2FwOUbdDOruo33VjdUy84QuUAZaeoFrtXsk3MPsi%2FUvZ7DA3RSzxhzokFvR1Xlx9XXpRDm8HRueUmfFwL6zI1VL1ZjkOkkO%2FaZ36DnQTtlWJ1uBrewsICe9oyEOngt4wmMASc9rziePJ4uRPa0X6K6eKiy8qnEhuwSc0M9JXtvIxqyvy2sOtegEGMntd0BZ5Alok3uABZZ1VNWsdU9u4PAelWoykfYPtnPZeE2itpCkxm90ftTdCv3p%2FHtWPay2tEDsbqhRfZHJs%2BU2a8GLr6tiCus7L93FDz5yd4TcjfOoOJokhf%2F8zGTo%2FtlzK0kaSNZjI4KG6bnUF7G5CxqUsKirN9%2BaI3F8TvdiwhAsu00d%2B%2BORfEDCk%2F4BI4hMIDApssGOqUBMfQaQBDGw0JcJWkJNl8FItQXInEyK8kjRCPmtaebofsqr74NR%2Bc%2F%2F3%2F75zGOgr0tF3sqFsiwIsUcCcYsXO%2Bur4mbfmAsIUP4lKlko2tto9VeHiqVieevaSzk%2BFT3J7bGoL9RQ1UWnWVi2%2BmFFb05llyPd5cp%2Fqvun2%2FEZLLH7RLK%2BEO0XFdTJHBy1uF2V9wb9kR4POFGGEnjvrwE6D%2B900kL2KR%2F&X-Amz-Signature=f72102038260737bf8041f7f2f0b89a5511a8922bdf7d46b5c96138a2f046430&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2FNYJSK%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCE8mckucPvrceFPRGWFgdszV%2BtUPd%2FZjZwLmNDyZeg2AIgR3MnKHfXBTCY8eSqTPwubLFX997fG08i%2Bt4b7B4m9Ewq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNjByVavv5F187ZJ8CrcA8Fcc1uHeKunz%2BoZ5TbfVv4mSQmOgiXxxx%2FY%2BbS6GeBdhRtKevt17WC60Z1zlU%2BauTqSNEV0gq1ejEB5agJTxwLaRY0Hs8mWYr0gESP%2F3HayYJhPUSHZNE8WKF3de3VTpbQ4Ie2iZA4qmOtuUBKjO1lbb0gTrxD7iE0cHpIh6L5XsmQVOIFXFbXr%2Bj1x8qjY%2B70Y%2Fig8KTtQkKS4QYv9WA0CspIPleyCCtxq0ofuOzEa%2BPxytr70EVOS1A02HJHFZVW%2FwOUbdDOruo33VjdUy84QuUAZaeoFrtXsk3MPsi%2FUvZ7DA3RSzxhzokFvR1Xlx9XXpRDm8HRueUmfFwL6zI1VL1ZjkOkkO%2FaZ36DnQTtlWJ1uBrewsICe9oyEOngt4wmMASc9rziePJ4uRPa0X6K6eKiy8qnEhuwSc0M9JXtvIxqyvy2sOtegEGMntd0BZ5Alok3uABZZ1VNWsdU9u4PAelWoykfYPtnPZeE2itpCkxm90ftTdCv3p%2FHtWPay2tEDsbqhRfZHJs%2BU2a8GLr6tiCus7L93FDz5yd4TcjfOoOJokhf%2F8zGTo%2FtlzK0kaSNZjI4KG6bnUF7G5CxqUsKirN9%2BaI3F8TvdiwhAsu00d%2B%2BORfEDCk%2F4BI4hMIDApssGOqUBMfQaQBDGw0JcJWkJNl8FItQXInEyK8kjRCPmtaebofsqr74NR%2Bc%2F%2F3%2F75zGOgr0tF3sqFsiwIsUcCcYsXO%2Bur4mbfmAsIUP4lKlko2tto9VeHiqVieevaSzk%2BFT3J7bGoL9RQ1UWnWVi2%2BmFFb05llyPd5cp%2Fqvun2%2FEZLLH7RLK%2BEO0XFdTJHBy1uF2V9wb9kR4POFGGEnjvrwE6D%2B900kL2KR%2F&X-Amz-Signature=c2b4485ee1e3110c876d6a6f162ca38610cd75d6c3ea2279e1b558844a1ae586&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



