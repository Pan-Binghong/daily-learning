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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXI2X5T2%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDLI8i9NVbq9Ddxxdbm66vYgUgD4mKPvlFzFTwh81Vx3AIhAO%2F0TnO2eBEQXXJ%2FoQ5LczwCKY%2BdP3Q1DkcCVHX%2B%2BhyDKv8DCB8QABoMNjM3NDIzMTgzODA1Igx52ebaxG2DIDSZeS8q3APfxuUisqS%2BXwDFXHTjhLNxoGzFuGCcjweOeTVelMcuXDR96LHufW7PS86Kz2X%2BX319lF2nWxuRlG0myOr9TGqRBEVmvqIGvw4Pa9WQ58uBXXMYMvW0A%2FaxNO0Ls5v2oLbcYuhxvRvXz99Wa7aFXwZdOmWbVopZ0F0aZQoEXu7Ozm8Z0V2NuWNVTj1idQOimte5P6DWxutYllldqdK%2FvANeRM4rp%2F3kcT2U6MrMyKEWZ6Fz7%2B%2FcsRNw8icG7RA8nfbFI7kuWpXCC8WVPLmc2%2Bjcg88CCGrOuobqH80zf75SOR42%2FG3gOLcKk%2BTCvnvNH9IcLwLqCkRwou%2Frtj5CRl285lBBeGm0WI37tiMKxVertJLPeQ9tcLXONt%2FQMdyhUK4Kg5BMZ8aaPogBCRi%2FnSZW3vIdtmNWSzsVngvcryFlROON9jE5mC4hQYlL3T9%2BTnEt7JztKMZG1t%2BywdVX%2BcBu0Dhzafv0%2BCvSpNFh8BoielaM%2FyuKBn3YpgGNI%2BIn81XjU5bBasSW3v0TF7bUNL9uOnu%2Bxb7W%2FyVuU4rvR0Cm2Dq9NtoUcwmL5WYnVNnmhq%2FCr9ehe5QWWz%2BcUzUskhrsU5Z%2FFyGEZAIPs7JnyMQGFx9hemXufoEjdwnRnDCKpebKBjqkAaAZrqmGAHWe0bK7i%2Fu5bMswdm%2FPCMfvijo%2FLTcmPBPrdUt99VigGq0Hel0270u8Wz3P%2BcX%2BOUot4AzoPPvJL4v%2FZQBN2nhwmI2xEjp7zTBiOefeghtyAGtC7dm2ZAi7goxkgbCaoaRF2ZJ9IWshl%2BbFlD%2FOMK4iOc9PcaN3PemFXxsHVsrBUtv%2Fjpmtg34TSfAgTu6wYGdwijbSWjsWU9%2FzHZ%2Bi&X-Amz-Signature=8df9a2e1b71e2bbd63438bb00f269ad831348080b3d5b9614c79bbfd9e859d31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXI2X5T2%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDLI8i9NVbq9Ddxxdbm66vYgUgD4mKPvlFzFTwh81Vx3AIhAO%2F0TnO2eBEQXXJ%2FoQ5LczwCKY%2BdP3Q1DkcCVHX%2B%2BhyDKv8DCB8QABoMNjM3NDIzMTgzODA1Igx52ebaxG2DIDSZeS8q3APfxuUisqS%2BXwDFXHTjhLNxoGzFuGCcjweOeTVelMcuXDR96LHufW7PS86Kz2X%2BX319lF2nWxuRlG0myOr9TGqRBEVmvqIGvw4Pa9WQ58uBXXMYMvW0A%2FaxNO0Ls5v2oLbcYuhxvRvXz99Wa7aFXwZdOmWbVopZ0F0aZQoEXu7Ozm8Z0V2NuWNVTj1idQOimte5P6DWxutYllldqdK%2FvANeRM4rp%2F3kcT2U6MrMyKEWZ6Fz7%2B%2FcsRNw8icG7RA8nfbFI7kuWpXCC8WVPLmc2%2Bjcg88CCGrOuobqH80zf75SOR42%2FG3gOLcKk%2BTCvnvNH9IcLwLqCkRwou%2Frtj5CRl285lBBeGm0WI37tiMKxVertJLPeQ9tcLXONt%2FQMdyhUK4Kg5BMZ8aaPogBCRi%2FnSZW3vIdtmNWSzsVngvcryFlROON9jE5mC4hQYlL3T9%2BTnEt7JztKMZG1t%2BywdVX%2BcBu0Dhzafv0%2BCvSpNFh8BoielaM%2FyuKBn3YpgGNI%2BIn81XjU5bBasSW3v0TF7bUNL9uOnu%2Bxb7W%2FyVuU4rvR0Cm2Dq9NtoUcwmL5WYnVNnmhq%2FCr9ehe5QWWz%2BcUzUskhrsU5Z%2FFyGEZAIPs7JnyMQGFx9hemXufoEjdwnRnDCKpebKBjqkAaAZrqmGAHWe0bK7i%2Fu5bMswdm%2FPCMfvijo%2FLTcmPBPrdUt99VigGq0Hel0270u8Wz3P%2BcX%2BOUot4AzoPPvJL4v%2FZQBN2nhwmI2xEjp7zTBiOefeghtyAGtC7dm2ZAi7goxkgbCaoaRF2ZJ9IWshl%2BbFlD%2FOMK4iOc9PcaN3PemFXxsHVsrBUtv%2Fjpmtg34TSfAgTu6wYGdwijbSWjsWU9%2FzHZ%2Bi&X-Amz-Signature=d7a264509cb4e69219937f73f4a8c221a4ad5185cd59cddd5fb7385d0a38dfc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXI2X5T2%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDLI8i9NVbq9Ddxxdbm66vYgUgD4mKPvlFzFTwh81Vx3AIhAO%2F0TnO2eBEQXXJ%2FoQ5LczwCKY%2BdP3Q1DkcCVHX%2B%2BhyDKv8DCB8QABoMNjM3NDIzMTgzODA1Igx52ebaxG2DIDSZeS8q3APfxuUisqS%2BXwDFXHTjhLNxoGzFuGCcjweOeTVelMcuXDR96LHufW7PS86Kz2X%2BX319lF2nWxuRlG0myOr9TGqRBEVmvqIGvw4Pa9WQ58uBXXMYMvW0A%2FaxNO0Ls5v2oLbcYuhxvRvXz99Wa7aFXwZdOmWbVopZ0F0aZQoEXu7Ozm8Z0V2NuWNVTj1idQOimte5P6DWxutYllldqdK%2FvANeRM4rp%2F3kcT2U6MrMyKEWZ6Fz7%2B%2FcsRNw8icG7RA8nfbFI7kuWpXCC8WVPLmc2%2Bjcg88CCGrOuobqH80zf75SOR42%2FG3gOLcKk%2BTCvnvNH9IcLwLqCkRwou%2Frtj5CRl285lBBeGm0WI37tiMKxVertJLPeQ9tcLXONt%2FQMdyhUK4Kg5BMZ8aaPogBCRi%2FnSZW3vIdtmNWSzsVngvcryFlROON9jE5mC4hQYlL3T9%2BTnEt7JztKMZG1t%2BywdVX%2BcBu0Dhzafv0%2BCvSpNFh8BoielaM%2FyuKBn3YpgGNI%2BIn81XjU5bBasSW3v0TF7bUNL9uOnu%2Bxb7W%2FyVuU4rvR0Cm2Dq9NtoUcwmL5WYnVNnmhq%2FCr9ehe5QWWz%2BcUzUskhrsU5Z%2FFyGEZAIPs7JnyMQGFx9hemXufoEjdwnRnDCKpebKBjqkAaAZrqmGAHWe0bK7i%2Fu5bMswdm%2FPCMfvijo%2FLTcmPBPrdUt99VigGq0Hel0270u8Wz3P%2BcX%2BOUot4AzoPPvJL4v%2FZQBN2nhwmI2xEjp7zTBiOefeghtyAGtC7dm2ZAi7goxkgbCaoaRF2ZJ9IWshl%2BbFlD%2FOMK4iOc9PcaN3PemFXxsHVsrBUtv%2Fjpmtg34TSfAgTu6wYGdwijbSWjsWU9%2FzHZ%2Bi&X-Amz-Signature=f7e26f595226a8dcf1e05024eee19f886a6a9019d5281ce41ff4a98ea085ffce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXI2X5T2%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDLI8i9NVbq9Ddxxdbm66vYgUgD4mKPvlFzFTwh81Vx3AIhAO%2F0TnO2eBEQXXJ%2FoQ5LczwCKY%2BdP3Q1DkcCVHX%2B%2BhyDKv8DCB8QABoMNjM3NDIzMTgzODA1Igx52ebaxG2DIDSZeS8q3APfxuUisqS%2BXwDFXHTjhLNxoGzFuGCcjweOeTVelMcuXDR96LHufW7PS86Kz2X%2BX319lF2nWxuRlG0myOr9TGqRBEVmvqIGvw4Pa9WQ58uBXXMYMvW0A%2FaxNO0Ls5v2oLbcYuhxvRvXz99Wa7aFXwZdOmWbVopZ0F0aZQoEXu7Ozm8Z0V2NuWNVTj1idQOimte5P6DWxutYllldqdK%2FvANeRM4rp%2F3kcT2U6MrMyKEWZ6Fz7%2B%2FcsRNw8icG7RA8nfbFI7kuWpXCC8WVPLmc2%2Bjcg88CCGrOuobqH80zf75SOR42%2FG3gOLcKk%2BTCvnvNH9IcLwLqCkRwou%2Frtj5CRl285lBBeGm0WI37tiMKxVertJLPeQ9tcLXONt%2FQMdyhUK4Kg5BMZ8aaPogBCRi%2FnSZW3vIdtmNWSzsVngvcryFlROON9jE5mC4hQYlL3T9%2BTnEt7JztKMZG1t%2BywdVX%2BcBu0Dhzafv0%2BCvSpNFh8BoielaM%2FyuKBn3YpgGNI%2BIn81XjU5bBasSW3v0TF7bUNL9uOnu%2Bxb7W%2FyVuU4rvR0Cm2Dq9NtoUcwmL5WYnVNnmhq%2FCr9ehe5QWWz%2BcUzUskhrsU5Z%2FFyGEZAIPs7JnyMQGFx9hemXufoEjdwnRnDCKpebKBjqkAaAZrqmGAHWe0bK7i%2Fu5bMswdm%2FPCMfvijo%2FLTcmPBPrdUt99VigGq0Hel0270u8Wz3P%2BcX%2BOUot4AzoPPvJL4v%2FZQBN2nhwmI2xEjp7zTBiOefeghtyAGtC7dm2ZAi7goxkgbCaoaRF2ZJ9IWshl%2BbFlD%2FOMK4iOc9PcaN3PemFXxsHVsrBUtv%2Fjpmtg34TSfAgTu6wYGdwijbSWjsWU9%2FzHZ%2Bi&X-Amz-Signature=2ebb67414739c5250228eedf5a871ad3c7f4ff8ae9c0437ff790176b17833380&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



