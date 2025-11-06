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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466656K24HD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjd5HHOCNWYqvzC8CCgiwdnVlUChFCfBXIoR2icSlUpAiEAtxaifRnPNk%2F%2F%2BZTbjMuSpMKjXypcxJHbd62SS8guN%2BcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNbQFRgV%2FQXCVR04CrcAxMgzKe5YbukmFFiqGmdlW4ypxShjNMT0Co9OLVU04Sq1pplAZyKO4jw5KhBJUECmkC9QVNrmiz64IqGiRqaDEJpRjCpeVY1bqhAEZGGcDlgfA2SF31a2wltKUu6hgQTUmOidLZr0bWrWUtNo6eL45tJMj1J03ycCcsWd%2BJjpoY24tEm0oxkwpF2%2BtbTWYfWauDI0A3fg9%2FjKJqQ%2FAvjfyGVDhXtebWRNXeuO%2FTwHcBmm1CIMOubkckW%2FGoFMZ%2F%2FRBRu1x5T8ur039iEHQraOfNGMLqFuAIs4Z73EU9bSokL8omP7WmKpnfK0TH8qK5fGX6WviVxTTAldusy5Ma%2FFYLP50iwHWyYdinOMa8vHWWeLFkr3r2Y7FIBSW3NKFpS1h7UunNsvKuxLClDy40OKDuSfLWr3sSfvmNYZoNOGFaWgYf9s2jbpEJfsFqOHa5lhZEWErtcaUnT0Goqt4UrxiKzyKZMkQL5IQgHeAhvB09Re5%2Bg1qCQfK4UjggHI%2FkrYXQbZ9XYDY3uLGcTbdVeDvLhkHfF1EadauPYIVq8xng9U7mo0X78CgFOmQBkkNs2dv15GXsiJWFBHdZNO3G87zfJcAf9gnkGkpEkS7n%2F%2F8ahFK0a72%2FuiwnqHxURMLuVsMgGOqUBAU78d3E8d27P6TH3Wrn9Lx8nZ1W1QUTWr0vg4iVJ3GKzCeY6yxO4P52sCI0x%2F6EuUilXFlvGMP2B6hBWut%2FxEJHTuKYqrSm9iQWEwoOYTX55GaeQ%2BOvYDhoLegYpFPozmdNhVVgRnpNSskENpMvzT%2BuyZNEtiICzHp2gi66DoOcDmyPlgXT6KsVpWMK95xiGH8x9xsR%2Fb50sYJdoNCkjYOInkZVg&X-Amz-Signature=ef337db4b6c965253d2a97fe55510a86bc4d7bbf8b8360aeae0b429d60d37f9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466656K24HD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjd5HHOCNWYqvzC8CCgiwdnVlUChFCfBXIoR2icSlUpAiEAtxaifRnPNk%2F%2F%2BZTbjMuSpMKjXypcxJHbd62SS8guN%2BcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNbQFRgV%2FQXCVR04CrcAxMgzKe5YbukmFFiqGmdlW4ypxShjNMT0Co9OLVU04Sq1pplAZyKO4jw5KhBJUECmkC9QVNrmiz64IqGiRqaDEJpRjCpeVY1bqhAEZGGcDlgfA2SF31a2wltKUu6hgQTUmOidLZr0bWrWUtNo6eL45tJMj1J03ycCcsWd%2BJjpoY24tEm0oxkwpF2%2BtbTWYfWauDI0A3fg9%2FjKJqQ%2FAvjfyGVDhXtebWRNXeuO%2FTwHcBmm1CIMOubkckW%2FGoFMZ%2F%2FRBRu1x5T8ur039iEHQraOfNGMLqFuAIs4Z73EU9bSokL8omP7WmKpnfK0TH8qK5fGX6WviVxTTAldusy5Ma%2FFYLP50iwHWyYdinOMa8vHWWeLFkr3r2Y7FIBSW3NKFpS1h7UunNsvKuxLClDy40OKDuSfLWr3sSfvmNYZoNOGFaWgYf9s2jbpEJfsFqOHa5lhZEWErtcaUnT0Goqt4UrxiKzyKZMkQL5IQgHeAhvB09Re5%2Bg1qCQfK4UjggHI%2FkrYXQbZ9XYDY3uLGcTbdVeDvLhkHfF1EadauPYIVq8xng9U7mo0X78CgFOmQBkkNs2dv15GXsiJWFBHdZNO3G87zfJcAf9gnkGkpEkS7n%2F%2F8ahFK0a72%2FuiwnqHxURMLuVsMgGOqUBAU78d3E8d27P6TH3Wrn9Lx8nZ1W1QUTWr0vg4iVJ3GKzCeY6yxO4P52sCI0x%2F6EuUilXFlvGMP2B6hBWut%2FxEJHTuKYqrSm9iQWEwoOYTX55GaeQ%2BOvYDhoLegYpFPozmdNhVVgRnpNSskENpMvzT%2BuyZNEtiICzHp2gi66DoOcDmyPlgXT6KsVpWMK95xiGH8x9xsR%2Fb50sYJdoNCkjYOInkZVg&X-Amz-Signature=d99f990d88fd21fae39947cacc7e855e84cc86826b5c7a000addb92ea0a7158a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466656K24HD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjd5HHOCNWYqvzC8CCgiwdnVlUChFCfBXIoR2icSlUpAiEAtxaifRnPNk%2F%2F%2BZTbjMuSpMKjXypcxJHbd62SS8guN%2BcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNbQFRgV%2FQXCVR04CrcAxMgzKe5YbukmFFiqGmdlW4ypxShjNMT0Co9OLVU04Sq1pplAZyKO4jw5KhBJUECmkC9QVNrmiz64IqGiRqaDEJpRjCpeVY1bqhAEZGGcDlgfA2SF31a2wltKUu6hgQTUmOidLZr0bWrWUtNo6eL45tJMj1J03ycCcsWd%2BJjpoY24tEm0oxkwpF2%2BtbTWYfWauDI0A3fg9%2FjKJqQ%2FAvjfyGVDhXtebWRNXeuO%2FTwHcBmm1CIMOubkckW%2FGoFMZ%2F%2FRBRu1x5T8ur039iEHQraOfNGMLqFuAIs4Z73EU9bSokL8omP7WmKpnfK0TH8qK5fGX6WviVxTTAldusy5Ma%2FFYLP50iwHWyYdinOMa8vHWWeLFkr3r2Y7FIBSW3NKFpS1h7UunNsvKuxLClDy40OKDuSfLWr3sSfvmNYZoNOGFaWgYf9s2jbpEJfsFqOHa5lhZEWErtcaUnT0Goqt4UrxiKzyKZMkQL5IQgHeAhvB09Re5%2Bg1qCQfK4UjggHI%2FkrYXQbZ9XYDY3uLGcTbdVeDvLhkHfF1EadauPYIVq8xng9U7mo0X78CgFOmQBkkNs2dv15GXsiJWFBHdZNO3G87zfJcAf9gnkGkpEkS7n%2F%2F8ahFK0a72%2FuiwnqHxURMLuVsMgGOqUBAU78d3E8d27P6TH3Wrn9Lx8nZ1W1QUTWr0vg4iVJ3GKzCeY6yxO4P52sCI0x%2F6EuUilXFlvGMP2B6hBWut%2FxEJHTuKYqrSm9iQWEwoOYTX55GaeQ%2BOvYDhoLegYpFPozmdNhVVgRnpNSskENpMvzT%2BuyZNEtiICzHp2gi66DoOcDmyPlgXT6KsVpWMK95xiGH8x9xsR%2Fb50sYJdoNCkjYOInkZVg&X-Amz-Signature=2513e166cf627b9515a8832de89f5d0d0065fb2940713dd94b9bf0378c099971&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466656K24HD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjd5HHOCNWYqvzC8CCgiwdnVlUChFCfBXIoR2icSlUpAiEAtxaifRnPNk%2F%2F%2BZTbjMuSpMKjXypcxJHbd62SS8guN%2BcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNbQFRgV%2FQXCVR04CrcAxMgzKe5YbukmFFiqGmdlW4ypxShjNMT0Co9OLVU04Sq1pplAZyKO4jw5KhBJUECmkC9QVNrmiz64IqGiRqaDEJpRjCpeVY1bqhAEZGGcDlgfA2SF31a2wltKUu6hgQTUmOidLZr0bWrWUtNo6eL45tJMj1J03ycCcsWd%2BJjpoY24tEm0oxkwpF2%2BtbTWYfWauDI0A3fg9%2FjKJqQ%2FAvjfyGVDhXtebWRNXeuO%2FTwHcBmm1CIMOubkckW%2FGoFMZ%2F%2FRBRu1x5T8ur039iEHQraOfNGMLqFuAIs4Z73EU9bSokL8omP7WmKpnfK0TH8qK5fGX6WviVxTTAldusy5Ma%2FFYLP50iwHWyYdinOMa8vHWWeLFkr3r2Y7FIBSW3NKFpS1h7UunNsvKuxLClDy40OKDuSfLWr3sSfvmNYZoNOGFaWgYf9s2jbpEJfsFqOHa5lhZEWErtcaUnT0Goqt4UrxiKzyKZMkQL5IQgHeAhvB09Re5%2Bg1qCQfK4UjggHI%2FkrYXQbZ9XYDY3uLGcTbdVeDvLhkHfF1EadauPYIVq8xng9U7mo0X78CgFOmQBkkNs2dv15GXsiJWFBHdZNO3G87zfJcAf9gnkGkpEkS7n%2F%2F8ahFK0a72%2FuiwnqHxURMLuVsMgGOqUBAU78d3E8d27P6TH3Wrn9Lx8nZ1W1QUTWr0vg4iVJ3GKzCeY6yxO4P52sCI0x%2F6EuUilXFlvGMP2B6hBWut%2FxEJHTuKYqrSm9iQWEwoOYTX55GaeQ%2BOvYDhoLegYpFPozmdNhVVgRnpNSskENpMvzT%2BuyZNEtiICzHp2gi66DoOcDmyPlgXT6KsVpWMK95xiGH8x9xsR%2Fb50sYJdoNCkjYOInkZVg&X-Amz-Signature=98b0a2532d956c82031652d6b093424bad2c4a6b317246bc3b269b95bff5318c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



