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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJOHHYUB%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFnVQBg4SEY2IrniW9mlqYi9ewZ9hWTbJ5uMvZw92hkWAiAVIXCFOYqJWas%2FnEJHtv99XcL0cU34Pk2vJXgOGySg%2Bir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMRKhV8SDFZylD5QoTKtwD6Sb1Y627Qyebmiw2yzVzpUwRlXG%2BWYehCR%2FerAHkxKET0iC1SzR58f7YyiBr4VgQsGDc9A3ezm8DS%2BFgbFmSR%2FjC6GSirTVkQIsyJ2Yk8UVloaVsaaHmKpW0bKR5Nw96b9R%2F6fxM7DQw8vMQPjK5hYIUqlKaJPNmahNwpJAQ2xwpPab5nKsaXGRBCXqO5oEBvmZUfWwT0Dkrr0j%2FiUhceDLLwhD9gOBm3OTkhiEBS9eCKKTpD0bH5XFSmwrvHZnoKeEe1mLemMF2OJnmybXMctwn8YAxGarTuP%2BTqkt56Bip%2B62lRwgRJIsj%2BmRKJYTYFEBVpb9mm%2FuSmqyQKdoxI4IiO7GDttKvFtCuZPdRas7HJ%2FWR9zZhmZRxhwWRPi%2FCNLjXa9fgDGAeR%2FzKomiWjRrZcj8ptPslHQ24X5ZO%2BVbrNneMY48ow8iPd9xExXeXsKQliPeC8S6eWiBoCKNPz%2Fq7yFjJ%2Bua500dH%2FbqAO7ICxzf9PpMvNcwxahK2IH3ZpxH%2FluvDDdY2YMnYB%2BGLpPZNrxMCd%2Fz2p8sZWOdBYnpwo5G2ipbQIbpGdTDWx93duAIKwp0wlA%2BnWShsJP%2FUmNryAak9lwfSpnzEl3mQzxjUZkpgbljrOt0Fpy8wrYOxywY6pgF8DKdVog7VepPGtfwS82zaM%2F%2BpvkKhlv8IK2VYPSvS0GC9gcxk3SPmntDAahm0n10HZdgcNk1hZY1%2F2TqJbRuZHlOORenadVtcZUZsNSenXmJGnO7FkBoaR5ouUIC%2FfzM%2BuRTRouDC2hVcglRNGWq%2Fq3XzKw9Fd2Eem9D3jI5SkZa%2FpZIKZGt17F3TdtfwecOi8JLj0kNvZXEz10D6BWNtvmBrZ40Z&X-Amz-Signature=98e596d99ab0893cab2cdef41f2faa9bf5db65f4c22ea7b2b691406bebffdf67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJOHHYUB%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFnVQBg4SEY2IrniW9mlqYi9ewZ9hWTbJ5uMvZw92hkWAiAVIXCFOYqJWas%2FnEJHtv99XcL0cU34Pk2vJXgOGySg%2Bir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMRKhV8SDFZylD5QoTKtwD6Sb1Y627Qyebmiw2yzVzpUwRlXG%2BWYehCR%2FerAHkxKET0iC1SzR58f7YyiBr4VgQsGDc9A3ezm8DS%2BFgbFmSR%2FjC6GSirTVkQIsyJ2Yk8UVloaVsaaHmKpW0bKR5Nw96b9R%2F6fxM7DQw8vMQPjK5hYIUqlKaJPNmahNwpJAQ2xwpPab5nKsaXGRBCXqO5oEBvmZUfWwT0Dkrr0j%2FiUhceDLLwhD9gOBm3OTkhiEBS9eCKKTpD0bH5XFSmwrvHZnoKeEe1mLemMF2OJnmybXMctwn8YAxGarTuP%2BTqkt56Bip%2B62lRwgRJIsj%2BmRKJYTYFEBVpb9mm%2FuSmqyQKdoxI4IiO7GDttKvFtCuZPdRas7HJ%2FWR9zZhmZRxhwWRPi%2FCNLjXa9fgDGAeR%2FzKomiWjRrZcj8ptPslHQ24X5ZO%2BVbrNneMY48ow8iPd9xExXeXsKQliPeC8S6eWiBoCKNPz%2Fq7yFjJ%2Bua500dH%2FbqAO7ICxzf9PpMvNcwxahK2IH3ZpxH%2FluvDDdY2YMnYB%2BGLpPZNrxMCd%2Fz2p8sZWOdBYnpwo5G2ipbQIbpGdTDWx93duAIKwp0wlA%2BnWShsJP%2FUmNryAak9lwfSpnzEl3mQzxjUZkpgbljrOt0Fpy8wrYOxywY6pgF8DKdVog7VepPGtfwS82zaM%2F%2BpvkKhlv8IK2VYPSvS0GC9gcxk3SPmntDAahm0n10HZdgcNk1hZY1%2F2TqJbRuZHlOORenadVtcZUZsNSenXmJGnO7FkBoaR5ouUIC%2FfzM%2BuRTRouDC2hVcglRNGWq%2Fq3XzKw9Fd2Eem9D3jI5SkZa%2FpZIKZGt17F3TdtfwecOi8JLj0kNvZXEz10D6BWNtvmBrZ40Z&X-Amz-Signature=fb5a583358b19d51d741cdba66de47108a1f40f54bdca100ac41592fbf2685cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJOHHYUB%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFnVQBg4SEY2IrniW9mlqYi9ewZ9hWTbJ5uMvZw92hkWAiAVIXCFOYqJWas%2FnEJHtv99XcL0cU34Pk2vJXgOGySg%2Bir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMRKhV8SDFZylD5QoTKtwD6Sb1Y627Qyebmiw2yzVzpUwRlXG%2BWYehCR%2FerAHkxKET0iC1SzR58f7YyiBr4VgQsGDc9A3ezm8DS%2BFgbFmSR%2FjC6GSirTVkQIsyJ2Yk8UVloaVsaaHmKpW0bKR5Nw96b9R%2F6fxM7DQw8vMQPjK5hYIUqlKaJPNmahNwpJAQ2xwpPab5nKsaXGRBCXqO5oEBvmZUfWwT0Dkrr0j%2FiUhceDLLwhD9gOBm3OTkhiEBS9eCKKTpD0bH5XFSmwrvHZnoKeEe1mLemMF2OJnmybXMctwn8YAxGarTuP%2BTqkt56Bip%2B62lRwgRJIsj%2BmRKJYTYFEBVpb9mm%2FuSmqyQKdoxI4IiO7GDttKvFtCuZPdRas7HJ%2FWR9zZhmZRxhwWRPi%2FCNLjXa9fgDGAeR%2FzKomiWjRrZcj8ptPslHQ24X5ZO%2BVbrNneMY48ow8iPd9xExXeXsKQliPeC8S6eWiBoCKNPz%2Fq7yFjJ%2Bua500dH%2FbqAO7ICxzf9PpMvNcwxahK2IH3ZpxH%2FluvDDdY2YMnYB%2BGLpPZNrxMCd%2Fz2p8sZWOdBYnpwo5G2ipbQIbpGdTDWx93duAIKwp0wlA%2BnWShsJP%2FUmNryAak9lwfSpnzEl3mQzxjUZkpgbljrOt0Fpy8wrYOxywY6pgF8DKdVog7VepPGtfwS82zaM%2F%2BpvkKhlv8IK2VYPSvS0GC9gcxk3SPmntDAahm0n10HZdgcNk1hZY1%2F2TqJbRuZHlOORenadVtcZUZsNSenXmJGnO7FkBoaR5ouUIC%2FfzM%2BuRTRouDC2hVcglRNGWq%2Fq3XzKw9Fd2Eem9D3jI5SkZa%2FpZIKZGt17F3TdtfwecOi8JLj0kNvZXEz10D6BWNtvmBrZ40Z&X-Amz-Signature=b0adf826d858e40ec86e453f061a0a2772654aa00b7e7234ee083d7e1cc4675a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJOHHYUB%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFnVQBg4SEY2IrniW9mlqYi9ewZ9hWTbJ5uMvZw92hkWAiAVIXCFOYqJWas%2FnEJHtv99XcL0cU34Pk2vJXgOGySg%2Bir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMRKhV8SDFZylD5QoTKtwD6Sb1Y627Qyebmiw2yzVzpUwRlXG%2BWYehCR%2FerAHkxKET0iC1SzR58f7YyiBr4VgQsGDc9A3ezm8DS%2BFgbFmSR%2FjC6GSirTVkQIsyJ2Yk8UVloaVsaaHmKpW0bKR5Nw96b9R%2F6fxM7DQw8vMQPjK5hYIUqlKaJPNmahNwpJAQ2xwpPab5nKsaXGRBCXqO5oEBvmZUfWwT0Dkrr0j%2FiUhceDLLwhD9gOBm3OTkhiEBS9eCKKTpD0bH5XFSmwrvHZnoKeEe1mLemMF2OJnmybXMctwn8YAxGarTuP%2BTqkt56Bip%2B62lRwgRJIsj%2BmRKJYTYFEBVpb9mm%2FuSmqyQKdoxI4IiO7GDttKvFtCuZPdRas7HJ%2FWR9zZhmZRxhwWRPi%2FCNLjXa9fgDGAeR%2FzKomiWjRrZcj8ptPslHQ24X5ZO%2BVbrNneMY48ow8iPd9xExXeXsKQliPeC8S6eWiBoCKNPz%2Fq7yFjJ%2Bua500dH%2FbqAO7ICxzf9PpMvNcwxahK2IH3ZpxH%2FluvDDdY2YMnYB%2BGLpPZNrxMCd%2Fz2p8sZWOdBYnpwo5G2ipbQIbpGdTDWx93duAIKwp0wlA%2BnWShsJP%2FUmNryAak9lwfSpnzEl3mQzxjUZkpgbljrOt0Fpy8wrYOxywY6pgF8DKdVog7VepPGtfwS82zaM%2F%2BpvkKhlv8IK2VYPSvS0GC9gcxk3SPmntDAahm0n10HZdgcNk1hZY1%2F2TqJbRuZHlOORenadVtcZUZsNSenXmJGnO7FkBoaR5ouUIC%2FfzM%2BuRTRouDC2hVcglRNGWq%2Fq3XzKw9Fd2Eem9D3jI5SkZa%2FpZIKZGt17F3TdtfwecOi8JLj0kNvZXEz10D6BWNtvmBrZ40Z&X-Amz-Signature=8732c3c263b49fa1644a8de34764a153fcd45eb2d90cdc5591208af971ee1c6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



