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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NLRJC2K%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2ppRcCDW53r5UowlIzduhU%2BHQfGzwAT48q131nqyWmAiEAlYvgqmlt1MeRRnVT%2FoAS2WiIqawMvM3P5zXTYLUc2t8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnEVnHKjWUo2Hu4HircA3qxxABCGaES6jwflfT4Bke59vqwnANXg%2F5tnu7xKLO2hhZG8zGLZZOhtuO3A0vEdStoPF015ytHIpW5xSl%2FQQRjQgbIl2IHNE0FOVmPijMtnvKJlLDcLmNxAKUvTHUZuf9ccgsvaCDy8tCh5M3yiI1RXrv2D0uUq%2BuxPnUpg%2B%2FJ324YwT3VgpsSb0enVwDJVeQRhqKwF2q0iqI4QNmn%2BTuP8SyK0TgmdYLZ27PexQ3CzUJ6jQ%2Fsr4XlF5SQZNLNCLjS4IedxSHJ6goINm9FKsFVluhTPziu5Z7o3JgpHePwcmS95PLes8wBqsolH4gmFclvqlL4ycrd%2F8KsQKfSTlx72VABS2MxqneODSPX7kjAzjTarSaUN7sVGj99dOAjnGJA9oYhKrwaRjw7cJXoX9aAZrn%2FDdtjIveFFqibqUpGmFhrKvrRAGsoolVg0h9fFEtWRq81ibi0IA9sjxVfNEDhdYz%2Fx2qD5aGIDc6CPzGaDARNNrvU5JsJ%2B29ZaPVyCWnxwYTc4Q4ovurthEW97KxKgaS4Wb3OJX%2BdN4C3sV3JdxVrzUKung%2F6Svwh596uaymxbInqvFKOzBD0sij7%2BGAOsY98lIg45z1FNtifyzpkKLjwCuWGeHcioN9DMLKmjc4GOqUBQyy66Sz%2BE4RCmKsiwD%2BOR3ilDELxVMo42K%2FzSD85Kp4FqeBq9Ske2BN5fwylIOPAVwgjlTuMKzG2CWmTe1LxVN39kjzz14MPkF7pagQ9TCuMwSR2wP60RovlIfN0kEJSJKPWEExPsNLGgSFjJv4NT20QG8dA3Czqm4f08igmWy1fbfMzcpTzT2pRVBIpSUfuezZJUUVcWmopJaBTg5qrj5kp4Zmr&X-Amz-Signature=79166819ba2bc964cd1e6d2a17321d8185ef139dd5d9745f1e66d71bcd8dc4b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NLRJC2K%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2ppRcCDW53r5UowlIzduhU%2BHQfGzwAT48q131nqyWmAiEAlYvgqmlt1MeRRnVT%2FoAS2WiIqawMvM3P5zXTYLUc2t8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnEVnHKjWUo2Hu4HircA3qxxABCGaES6jwflfT4Bke59vqwnANXg%2F5tnu7xKLO2hhZG8zGLZZOhtuO3A0vEdStoPF015ytHIpW5xSl%2FQQRjQgbIl2IHNE0FOVmPijMtnvKJlLDcLmNxAKUvTHUZuf9ccgsvaCDy8tCh5M3yiI1RXrv2D0uUq%2BuxPnUpg%2B%2FJ324YwT3VgpsSb0enVwDJVeQRhqKwF2q0iqI4QNmn%2BTuP8SyK0TgmdYLZ27PexQ3CzUJ6jQ%2Fsr4XlF5SQZNLNCLjS4IedxSHJ6goINm9FKsFVluhTPziu5Z7o3JgpHePwcmS95PLes8wBqsolH4gmFclvqlL4ycrd%2F8KsQKfSTlx72VABS2MxqneODSPX7kjAzjTarSaUN7sVGj99dOAjnGJA9oYhKrwaRjw7cJXoX9aAZrn%2FDdtjIveFFqibqUpGmFhrKvrRAGsoolVg0h9fFEtWRq81ibi0IA9sjxVfNEDhdYz%2Fx2qD5aGIDc6CPzGaDARNNrvU5JsJ%2B29ZaPVyCWnxwYTc4Q4ovurthEW97KxKgaS4Wb3OJX%2BdN4C3sV3JdxVrzUKung%2F6Svwh596uaymxbInqvFKOzBD0sij7%2BGAOsY98lIg45z1FNtifyzpkKLjwCuWGeHcioN9DMLKmjc4GOqUBQyy66Sz%2BE4RCmKsiwD%2BOR3ilDELxVMo42K%2FzSD85Kp4FqeBq9Ske2BN5fwylIOPAVwgjlTuMKzG2CWmTe1LxVN39kjzz14MPkF7pagQ9TCuMwSR2wP60RovlIfN0kEJSJKPWEExPsNLGgSFjJv4NT20QG8dA3Czqm4f08igmWy1fbfMzcpTzT2pRVBIpSUfuezZJUUVcWmopJaBTg5qrj5kp4Zmr&X-Amz-Signature=0885d027d880315ff7e09e011a3450cb74b0a362a56e0ac49cd90b890634ac78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NLRJC2K%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2ppRcCDW53r5UowlIzduhU%2BHQfGzwAT48q131nqyWmAiEAlYvgqmlt1MeRRnVT%2FoAS2WiIqawMvM3P5zXTYLUc2t8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnEVnHKjWUo2Hu4HircA3qxxABCGaES6jwflfT4Bke59vqwnANXg%2F5tnu7xKLO2hhZG8zGLZZOhtuO3A0vEdStoPF015ytHIpW5xSl%2FQQRjQgbIl2IHNE0FOVmPijMtnvKJlLDcLmNxAKUvTHUZuf9ccgsvaCDy8tCh5M3yiI1RXrv2D0uUq%2BuxPnUpg%2B%2FJ324YwT3VgpsSb0enVwDJVeQRhqKwF2q0iqI4QNmn%2BTuP8SyK0TgmdYLZ27PexQ3CzUJ6jQ%2Fsr4XlF5SQZNLNCLjS4IedxSHJ6goINm9FKsFVluhTPziu5Z7o3JgpHePwcmS95PLes8wBqsolH4gmFclvqlL4ycrd%2F8KsQKfSTlx72VABS2MxqneODSPX7kjAzjTarSaUN7sVGj99dOAjnGJA9oYhKrwaRjw7cJXoX9aAZrn%2FDdtjIveFFqibqUpGmFhrKvrRAGsoolVg0h9fFEtWRq81ibi0IA9sjxVfNEDhdYz%2Fx2qD5aGIDc6CPzGaDARNNrvU5JsJ%2B29ZaPVyCWnxwYTc4Q4ovurthEW97KxKgaS4Wb3OJX%2BdN4C3sV3JdxVrzUKung%2F6Svwh596uaymxbInqvFKOzBD0sij7%2BGAOsY98lIg45z1FNtifyzpkKLjwCuWGeHcioN9DMLKmjc4GOqUBQyy66Sz%2BE4RCmKsiwD%2BOR3ilDELxVMo42K%2FzSD85Kp4FqeBq9Ske2BN5fwylIOPAVwgjlTuMKzG2CWmTe1LxVN39kjzz14MPkF7pagQ9TCuMwSR2wP60RovlIfN0kEJSJKPWEExPsNLGgSFjJv4NT20QG8dA3Czqm4f08igmWy1fbfMzcpTzT2pRVBIpSUfuezZJUUVcWmopJaBTg5qrj5kp4Zmr&X-Amz-Signature=41289f11b1a2ce4299b50b4e2213a85f8e4dc8e24fe39299b256134f49f5e779&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NLRJC2K%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2ppRcCDW53r5UowlIzduhU%2BHQfGzwAT48q131nqyWmAiEAlYvgqmlt1MeRRnVT%2FoAS2WiIqawMvM3P5zXTYLUc2t8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNnEVnHKjWUo2Hu4HircA3qxxABCGaES6jwflfT4Bke59vqwnANXg%2F5tnu7xKLO2hhZG8zGLZZOhtuO3A0vEdStoPF015ytHIpW5xSl%2FQQRjQgbIl2IHNE0FOVmPijMtnvKJlLDcLmNxAKUvTHUZuf9ccgsvaCDy8tCh5M3yiI1RXrv2D0uUq%2BuxPnUpg%2B%2FJ324YwT3VgpsSb0enVwDJVeQRhqKwF2q0iqI4QNmn%2BTuP8SyK0TgmdYLZ27PexQ3CzUJ6jQ%2Fsr4XlF5SQZNLNCLjS4IedxSHJ6goINm9FKsFVluhTPziu5Z7o3JgpHePwcmS95PLes8wBqsolH4gmFclvqlL4ycrd%2F8KsQKfSTlx72VABS2MxqneODSPX7kjAzjTarSaUN7sVGj99dOAjnGJA9oYhKrwaRjw7cJXoX9aAZrn%2FDdtjIveFFqibqUpGmFhrKvrRAGsoolVg0h9fFEtWRq81ibi0IA9sjxVfNEDhdYz%2Fx2qD5aGIDc6CPzGaDARNNrvU5JsJ%2B29ZaPVyCWnxwYTc4Q4ovurthEW97KxKgaS4Wb3OJX%2BdN4C3sV3JdxVrzUKung%2F6Svwh596uaymxbInqvFKOzBD0sij7%2BGAOsY98lIg45z1FNtifyzpkKLjwCuWGeHcioN9DMLKmjc4GOqUBQyy66Sz%2BE4RCmKsiwD%2BOR3ilDELxVMo42K%2FzSD85Kp4FqeBq9Ske2BN5fwylIOPAVwgjlTuMKzG2CWmTe1LxVN39kjzz14MPkF7pagQ9TCuMwSR2wP60RovlIfN0kEJSJKPWEExPsNLGgSFjJv4NT20QG8dA3Czqm4f08igmWy1fbfMzcpTzT2pRVBIpSUfuezZJUUVcWmopJaBTg5qrj5kp4Zmr&X-Amz-Signature=86228e5e8af807dd299654bf7016cdcac7612de60ece4d83eea244e60bc3e4e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



