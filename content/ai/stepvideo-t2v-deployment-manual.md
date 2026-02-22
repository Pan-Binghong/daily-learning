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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U6DQE52%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjc6l%2BrV9sJq7re8D4ZqtesGqWI906n%2BpZQBSvoGBh6QIhAK%2BWk3L1wnv%2F%2Bmbs7Wl9F3lApd25pbxh7kGs8Ytn8X40KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCv0bj1KydejOAjPUq3APHfTK1KaGXVUTJkX3FyHWgjNlz1FnWVrg6Y5aYmO0GJzTsXuYlq4YM5YQK6ccPzf7DBnUGJpmg%2BDtUCI5rl%2F%2FJpjtqD4I2JHauvjahNrCXJh%2F1kx%2BgJUe4EUITBxfWES4KXO1ngBK7wuUohLdd8MHbNKfEWnX%2BQPzq%2BYheu9ezWhxu6dQIa2ICsNE6PDyA6JUBJ0hMQa781KPpGLYhGulwz8orM4rjix3RPefqVu2gkwsy1uoIMDVeQzwD%2BAnV23R%2Bm411BnprLSHm0hELimKLuf10K5Rsf19ZpyvVq4duwx%2BIDm%2F9t5zaO26Pe2IENyo270igGrVJ%2F9OCaUyipA6rBx25ofIq%2BkrmN4TBbegnCrPKiDifHIRFk%2BAzvGq%2Fj20X8ulrUcPX85FdFd1dbOa5ClSFXrBctg3rcAdYB9BknHTgW%2FuVwUlXYX%2FKmnaNdq8uT8OauwVTKPxN7CPrrhFeFLrXiFVbdHdB283GvC5V5MEv%2BtFFMXxg1%2FZjZoMhhlTsOqHHg5zFV95URj0Rz58c%2BZh8Ie6cB58I%2FwRwvYKgmHv9on96cKmFiWbuCMjhW5RWvj%2BdIN1mYtgbgT%2Bovih42PoabJYvzEih4xs%2BM0dopm8Ds%2BYAjI0Mkzz%2FWzDkzOnMBjqkAdlU1F1GCvtJTg2icmqRegfpiXz%2BSbQjxWbiNoZM%2F0YeQ3iCwvsWkDWPEDNgQwfTFpmCZ%2BQngrtbVaH1q2bsdp%2FsVGHq%2BH4SHSk7Lbd1WID7IU8ygLReV70nImt8AUKTy5%2B21EAo9%2BVWs0%2F1umMLh0Xt%2BanHHntvtLdb1%2Bnf1YuTi7bw1sIU6wni1OkcIaLdl%2BzNaGfQpTz7QdW1S6AqiA4JMkh3&X-Amz-Signature=7ab5dd0d950d5b87d94ab5edc3193219f62ba22bd0fc99711fc756036cbb0500&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U6DQE52%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjc6l%2BrV9sJq7re8D4ZqtesGqWI906n%2BpZQBSvoGBh6QIhAK%2BWk3L1wnv%2F%2Bmbs7Wl9F3lApd25pbxh7kGs8Ytn8X40KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCv0bj1KydejOAjPUq3APHfTK1KaGXVUTJkX3FyHWgjNlz1FnWVrg6Y5aYmO0GJzTsXuYlq4YM5YQK6ccPzf7DBnUGJpmg%2BDtUCI5rl%2F%2FJpjtqD4I2JHauvjahNrCXJh%2F1kx%2BgJUe4EUITBxfWES4KXO1ngBK7wuUohLdd8MHbNKfEWnX%2BQPzq%2BYheu9ezWhxu6dQIa2ICsNE6PDyA6JUBJ0hMQa781KPpGLYhGulwz8orM4rjix3RPefqVu2gkwsy1uoIMDVeQzwD%2BAnV23R%2Bm411BnprLSHm0hELimKLuf10K5Rsf19ZpyvVq4duwx%2BIDm%2F9t5zaO26Pe2IENyo270igGrVJ%2F9OCaUyipA6rBx25ofIq%2BkrmN4TBbegnCrPKiDifHIRFk%2BAzvGq%2Fj20X8ulrUcPX85FdFd1dbOa5ClSFXrBctg3rcAdYB9BknHTgW%2FuVwUlXYX%2FKmnaNdq8uT8OauwVTKPxN7CPrrhFeFLrXiFVbdHdB283GvC5V5MEv%2BtFFMXxg1%2FZjZoMhhlTsOqHHg5zFV95URj0Rz58c%2BZh8Ie6cB58I%2FwRwvYKgmHv9on96cKmFiWbuCMjhW5RWvj%2BdIN1mYtgbgT%2Bovih42PoabJYvzEih4xs%2BM0dopm8Ds%2BYAjI0Mkzz%2FWzDkzOnMBjqkAdlU1F1GCvtJTg2icmqRegfpiXz%2BSbQjxWbiNoZM%2F0YeQ3iCwvsWkDWPEDNgQwfTFpmCZ%2BQngrtbVaH1q2bsdp%2FsVGHq%2BH4SHSk7Lbd1WID7IU8ygLReV70nImt8AUKTy5%2B21EAo9%2BVWs0%2F1umMLh0Xt%2BanHHntvtLdb1%2Bnf1YuTi7bw1sIU6wni1OkcIaLdl%2BzNaGfQpTz7QdW1S6AqiA4JMkh3&X-Amz-Signature=dddfd117ef2c939fa8e00f175a34459cdd9c49e5d125baece1353274c769ba16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U6DQE52%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjc6l%2BrV9sJq7re8D4ZqtesGqWI906n%2BpZQBSvoGBh6QIhAK%2BWk3L1wnv%2F%2Bmbs7Wl9F3lApd25pbxh7kGs8Ytn8X40KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCv0bj1KydejOAjPUq3APHfTK1KaGXVUTJkX3FyHWgjNlz1FnWVrg6Y5aYmO0GJzTsXuYlq4YM5YQK6ccPzf7DBnUGJpmg%2BDtUCI5rl%2F%2FJpjtqD4I2JHauvjahNrCXJh%2F1kx%2BgJUe4EUITBxfWES4KXO1ngBK7wuUohLdd8MHbNKfEWnX%2BQPzq%2BYheu9ezWhxu6dQIa2ICsNE6PDyA6JUBJ0hMQa781KPpGLYhGulwz8orM4rjix3RPefqVu2gkwsy1uoIMDVeQzwD%2BAnV23R%2Bm411BnprLSHm0hELimKLuf10K5Rsf19ZpyvVq4duwx%2BIDm%2F9t5zaO26Pe2IENyo270igGrVJ%2F9OCaUyipA6rBx25ofIq%2BkrmN4TBbegnCrPKiDifHIRFk%2BAzvGq%2Fj20X8ulrUcPX85FdFd1dbOa5ClSFXrBctg3rcAdYB9BknHTgW%2FuVwUlXYX%2FKmnaNdq8uT8OauwVTKPxN7CPrrhFeFLrXiFVbdHdB283GvC5V5MEv%2BtFFMXxg1%2FZjZoMhhlTsOqHHg5zFV95URj0Rz58c%2BZh8Ie6cB58I%2FwRwvYKgmHv9on96cKmFiWbuCMjhW5RWvj%2BdIN1mYtgbgT%2Bovih42PoabJYvzEih4xs%2BM0dopm8Ds%2BYAjI0Mkzz%2FWzDkzOnMBjqkAdlU1F1GCvtJTg2icmqRegfpiXz%2BSbQjxWbiNoZM%2F0YeQ3iCwvsWkDWPEDNgQwfTFpmCZ%2BQngrtbVaH1q2bsdp%2FsVGHq%2BH4SHSk7Lbd1WID7IU8ygLReV70nImt8AUKTy5%2B21EAo9%2BVWs0%2F1umMLh0Xt%2BanHHntvtLdb1%2Bnf1YuTi7bw1sIU6wni1OkcIaLdl%2BzNaGfQpTz7QdW1S6AqiA4JMkh3&X-Amz-Signature=9071ee9be56a1d7d827351a43f3d6b02e9ca4df94cabafdafd5df9944db3945c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U6DQE52%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjc6l%2BrV9sJq7re8D4ZqtesGqWI906n%2BpZQBSvoGBh6QIhAK%2BWk3L1wnv%2F%2Bmbs7Wl9F3lApd25pbxh7kGs8Ytn8X40KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCv0bj1KydejOAjPUq3APHfTK1KaGXVUTJkX3FyHWgjNlz1FnWVrg6Y5aYmO0GJzTsXuYlq4YM5YQK6ccPzf7DBnUGJpmg%2BDtUCI5rl%2F%2FJpjtqD4I2JHauvjahNrCXJh%2F1kx%2BgJUe4EUITBxfWES4KXO1ngBK7wuUohLdd8MHbNKfEWnX%2BQPzq%2BYheu9ezWhxu6dQIa2ICsNE6PDyA6JUBJ0hMQa781KPpGLYhGulwz8orM4rjix3RPefqVu2gkwsy1uoIMDVeQzwD%2BAnV23R%2Bm411BnprLSHm0hELimKLuf10K5Rsf19ZpyvVq4duwx%2BIDm%2F9t5zaO26Pe2IENyo270igGrVJ%2F9OCaUyipA6rBx25ofIq%2BkrmN4TBbegnCrPKiDifHIRFk%2BAzvGq%2Fj20X8ulrUcPX85FdFd1dbOa5ClSFXrBctg3rcAdYB9BknHTgW%2FuVwUlXYX%2FKmnaNdq8uT8OauwVTKPxN7CPrrhFeFLrXiFVbdHdB283GvC5V5MEv%2BtFFMXxg1%2FZjZoMhhlTsOqHHg5zFV95URj0Rz58c%2BZh8Ie6cB58I%2FwRwvYKgmHv9on96cKmFiWbuCMjhW5RWvj%2BdIN1mYtgbgT%2Bovih42PoabJYvzEih4xs%2BM0dopm8Ds%2BYAjI0Mkzz%2FWzDkzOnMBjqkAdlU1F1GCvtJTg2icmqRegfpiXz%2BSbQjxWbiNoZM%2F0YeQ3iCwvsWkDWPEDNgQwfTFpmCZ%2BQngrtbVaH1q2bsdp%2FsVGHq%2BH4SHSk7Lbd1WID7IU8ygLReV70nImt8AUKTy5%2B21EAo9%2BVWs0%2F1umMLh0Xt%2BanHHntvtLdb1%2Bnf1YuTi7bw1sIU6wni1OkcIaLdl%2BzNaGfQpTz7QdW1S6AqiA4JMkh3&X-Amz-Signature=8b8e3c46702bf05b40c472c74e5dc39de2ec2a761399839c74e3eb5d013c6efb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



