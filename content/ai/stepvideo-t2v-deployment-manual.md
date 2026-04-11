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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U67BWQR5%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQDCJoc%2B69NJeXEDEr0p5mUzvWxePRTwA4%2BpgtieatXgIAIhANYdX0luKOA15kgDJLDw5ZA2AGwp2QlNRr2%2BKTvv%2BBG4Kv8DCDwQABoMNjM3NDIzMTgzODA1Igwi8HPAC1jhsZfrz08q3AMi8Q2fLN2wNuHi%2FAHldMMNkFdt2YvyDQKPuZAPpUTQGzOMGpxtzIhWDWh97U2D%2F9ibHKiUP20DNwXefSD4y59sX0GEZtkXplMeX8JsH7vzTTu3ioJbrUrGVjMIauQLXSZ%2BJ24od4U%2BltXj8gU2R79bkPfIrHjAuixiqnnYsndFNk8WfUmwoI3HibKCpzfOodauGo8bpiEusOu5Toblb4T7Fb7%2BCRhBuoe4bKloeAfs4SYG2zf5pIFLnqZmNd%2BDsLeOYn8MpjmX4aGIoTLmVerGzW4Z2rOiuJSpnwHQhY1lmE%2BIpXSSfQDPvYR5nRUEtvHMlXxEJqEoxXr4k7oW5r2Tb6%2BajI69M1nAxuGYEGm0BJ82zBQ%2BZ2pu5p7h7emny%2B8Jiuk%2FvmuDZJIcac5vIrvNuwlaxzdgDMnCnzmc%2FEHGV3eeCRnoanznO0OYEoOdu0MLLj%2FWuZN4XkF1gMc8Sp4bYoGspw%2Bwmy%2F4aapGNGUmA6NHIs01ZSlV363NkgJpN1K3k94Qs%2FI%2FxHdGr%2Fo2QUka9T%2B%2BfzRAZ2%2B%2FPFydl%2BH6OucpXn%2BN69u8m9SBidw4GtJIvz3gpHVqltzJ0te0OT%2FVV%2FSfxvDN7SrHO%2FIZaKbMWUXNFKuDl5e7EfCCKjDf6ObOBjqkATGRPh8aSazLz%2BYMbXEZFagIgxOvGrjSxvsOyxjdpImOiRRwDeL%2FoJSk7OYxG3bJ9HUS6SK4M9XwRyXQw3neC4nizcdDLTxsKB2BfBWgwmNz6pZBhXiMpgvaG4JO18stsnr6kzndXCpRxxGDflKiOKvUgU8p2I7b%2BxvjQHzNlSIxmgV6sSAIrZanvcXfHomu4JUwLBb1Rn0WVvsFPLy5TYs8R0Q9&X-Amz-Signature=f6ce505615d0fa27a89fa9b378c4e215f13c6707f788f232381f8313e9695311&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U67BWQR5%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQDCJoc%2B69NJeXEDEr0p5mUzvWxePRTwA4%2BpgtieatXgIAIhANYdX0luKOA15kgDJLDw5ZA2AGwp2QlNRr2%2BKTvv%2BBG4Kv8DCDwQABoMNjM3NDIzMTgzODA1Igwi8HPAC1jhsZfrz08q3AMi8Q2fLN2wNuHi%2FAHldMMNkFdt2YvyDQKPuZAPpUTQGzOMGpxtzIhWDWh97U2D%2F9ibHKiUP20DNwXefSD4y59sX0GEZtkXplMeX8JsH7vzTTu3ioJbrUrGVjMIauQLXSZ%2BJ24od4U%2BltXj8gU2R79bkPfIrHjAuixiqnnYsndFNk8WfUmwoI3HibKCpzfOodauGo8bpiEusOu5Toblb4T7Fb7%2BCRhBuoe4bKloeAfs4SYG2zf5pIFLnqZmNd%2BDsLeOYn8MpjmX4aGIoTLmVerGzW4Z2rOiuJSpnwHQhY1lmE%2BIpXSSfQDPvYR5nRUEtvHMlXxEJqEoxXr4k7oW5r2Tb6%2BajI69M1nAxuGYEGm0BJ82zBQ%2BZ2pu5p7h7emny%2B8Jiuk%2FvmuDZJIcac5vIrvNuwlaxzdgDMnCnzmc%2FEHGV3eeCRnoanznO0OYEoOdu0MLLj%2FWuZN4XkF1gMc8Sp4bYoGspw%2Bwmy%2F4aapGNGUmA6NHIs01ZSlV363NkgJpN1K3k94Qs%2FI%2FxHdGr%2Fo2QUka9T%2B%2BfzRAZ2%2B%2FPFydl%2BH6OucpXn%2BN69u8m9SBidw4GtJIvz3gpHVqltzJ0te0OT%2FVV%2FSfxvDN7SrHO%2FIZaKbMWUXNFKuDl5e7EfCCKjDf6ObOBjqkATGRPh8aSazLz%2BYMbXEZFagIgxOvGrjSxvsOyxjdpImOiRRwDeL%2FoJSk7OYxG3bJ9HUS6SK4M9XwRyXQw3neC4nizcdDLTxsKB2BfBWgwmNz6pZBhXiMpgvaG4JO18stsnr6kzndXCpRxxGDflKiOKvUgU8p2I7b%2BxvjQHzNlSIxmgV6sSAIrZanvcXfHomu4JUwLBb1Rn0WVvsFPLy5TYs8R0Q9&X-Amz-Signature=081ecd3652025053fada3bc5678a8dd9ce8ad5cc89c4ae5bfeab18fcf702dc2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U67BWQR5%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQDCJoc%2B69NJeXEDEr0p5mUzvWxePRTwA4%2BpgtieatXgIAIhANYdX0luKOA15kgDJLDw5ZA2AGwp2QlNRr2%2BKTvv%2BBG4Kv8DCDwQABoMNjM3NDIzMTgzODA1Igwi8HPAC1jhsZfrz08q3AMi8Q2fLN2wNuHi%2FAHldMMNkFdt2YvyDQKPuZAPpUTQGzOMGpxtzIhWDWh97U2D%2F9ibHKiUP20DNwXefSD4y59sX0GEZtkXplMeX8JsH7vzTTu3ioJbrUrGVjMIauQLXSZ%2BJ24od4U%2BltXj8gU2R79bkPfIrHjAuixiqnnYsndFNk8WfUmwoI3HibKCpzfOodauGo8bpiEusOu5Toblb4T7Fb7%2BCRhBuoe4bKloeAfs4SYG2zf5pIFLnqZmNd%2BDsLeOYn8MpjmX4aGIoTLmVerGzW4Z2rOiuJSpnwHQhY1lmE%2BIpXSSfQDPvYR5nRUEtvHMlXxEJqEoxXr4k7oW5r2Tb6%2BajI69M1nAxuGYEGm0BJ82zBQ%2BZ2pu5p7h7emny%2B8Jiuk%2FvmuDZJIcac5vIrvNuwlaxzdgDMnCnzmc%2FEHGV3eeCRnoanznO0OYEoOdu0MLLj%2FWuZN4XkF1gMc8Sp4bYoGspw%2Bwmy%2F4aapGNGUmA6NHIs01ZSlV363NkgJpN1K3k94Qs%2FI%2FxHdGr%2Fo2QUka9T%2B%2BfzRAZ2%2B%2FPFydl%2BH6OucpXn%2BN69u8m9SBidw4GtJIvz3gpHVqltzJ0te0OT%2FVV%2FSfxvDN7SrHO%2FIZaKbMWUXNFKuDl5e7EfCCKjDf6ObOBjqkATGRPh8aSazLz%2BYMbXEZFagIgxOvGrjSxvsOyxjdpImOiRRwDeL%2FoJSk7OYxG3bJ9HUS6SK4M9XwRyXQw3neC4nizcdDLTxsKB2BfBWgwmNz6pZBhXiMpgvaG4JO18stsnr6kzndXCpRxxGDflKiOKvUgU8p2I7b%2BxvjQHzNlSIxmgV6sSAIrZanvcXfHomu4JUwLBb1Rn0WVvsFPLy5TYs8R0Q9&X-Amz-Signature=2535b8de5094adf6e74e44193d5238026d2b43997b91f3aabe034845f5c9c16c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U67BWQR5%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQDCJoc%2B69NJeXEDEr0p5mUzvWxePRTwA4%2BpgtieatXgIAIhANYdX0luKOA15kgDJLDw5ZA2AGwp2QlNRr2%2BKTvv%2BBG4Kv8DCDwQABoMNjM3NDIzMTgzODA1Igwi8HPAC1jhsZfrz08q3AMi8Q2fLN2wNuHi%2FAHldMMNkFdt2YvyDQKPuZAPpUTQGzOMGpxtzIhWDWh97U2D%2F9ibHKiUP20DNwXefSD4y59sX0GEZtkXplMeX8JsH7vzTTu3ioJbrUrGVjMIauQLXSZ%2BJ24od4U%2BltXj8gU2R79bkPfIrHjAuixiqnnYsndFNk8WfUmwoI3HibKCpzfOodauGo8bpiEusOu5Toblb4T7Fb7%2BCRhBuoe4bKloeAfs4SYG2zf5pIFLnqZmNd%2BDsLeOYn8MpjmX4aGIoTLmVerGzW4Z2rOiuJSpnwHQhY1lmE%2BIpXSSfQDPvYR5nRUEtvHMlXxEJqEoxXr4k7oW5r2Tb6%2BajI69M1nAxuGYEGm0BJ82zBQ%2BZ2pu5p7h7emny%2B8Jiuk%2FvmuDZJIcac5vIrvNuwlaxzdgDMnCnzmc%2FEHGV3eeCRnoanznO0OYEoOdu0MLLj%2FWuZN4XkF1gMc8Sp4bYoGspw%2Bwmy%2F4aapGNGUmA6NHIs01ZSlV363NkgJpN1K3k94Qs%2FI%2FxHdGr%2Fo2QUka9T%2B%2BfzRAZ2%2B%2FPFydl%2BH6OucpXn%2BN69u8m9SBidw4GtJIvz3gpHVqltzJ0te0OT%2FVV%2FSfxvDN7SrHO%2FIZaKbMWUXNFKuDl5e7EfCCKjDf6ObOBjqkATGRPh8aSazLz%2BYMbXEZFagIgxOvGrjSxvsOyxjdpImOiRRwDeL%2FoJSk7OYxG3bJ9HUS6SK4M9XwRyXQw3neC4nizcdDLTxsKB2BfBWgwmNz6pZBhXiMpgvaG4JO18stsnr6kzndXCpRxxGDflKiOKvUgU8p2I7b%2BxvjQHzNlSIxmgV6sSAIrZanvcXfHomu4JUwLBb1Rn0WVvsFPLy5TYs8R0Q9&X-Amz-Signature=96cda142e4dff71f8111e7ac4ef320ea7ec6834f08f32bb814577b9dd5a75df7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



