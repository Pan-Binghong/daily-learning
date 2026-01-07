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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZASXWAXI%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIESSQBxzAuOUF0t8VBt8CgcrqgyCsqsLTTlT1Pb1i4ExAiABqIPfGXORni8f702u%2FSh6yJW4nLBZ7KcGFXM5naudtyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMBtsgpetO5bscObZmKtwDrHFIiW%2FCzBTzxVPf9eKp6mFdwH5F%2B9tiYtypKjbXc%2FcJGuHvDVqSFRCwCh3lLU4SLE34RFeL6v4rZnYA1zydGImAkZy%2F4bxnROFlqdywNj7ndaVCA%2Bxhda1uAQ2IWnoZi06dEruANv%2FQlxT%2FuWAKZq2kFi3zEDWIvhyoCfghtLOuOQImvVzvsJTDKZLHw5X8%2BngsQiBnWCq%2B2rntERffKb7d167uYJGXMaln3ucKhT%2FFFGKN90zy0FnHe5PUXMIMgPzClWwfPYQp0FsmBwJSDCubmJadGHTwH8KP1cG4QR7VSvZAH4ad%2FQaJa6dH8Iqse3sVhbilSAx7rLkBwSKCE4%2BFLQ9W0KiZYVE0AYUmimRXGi0sLaTaPYZMeTQRn127r2SsPE4HTkAiiap6vBKcMkW8bCKm2T5RMEQi%2FeKDdyEFIb6CpJ9pcKU1HuT1IldfllPHWJwn5znNMF8UmRgrXscCp1jtPqCttvImKp%2FzvkR0E8Z9xCBm%2FOk706lGDoI1ikD74VPt167iphTIpPJJohl172IqSnZNyF1epfYGMg7cOiAgMuWoqGqknZ4235Ty0m%2B3hKOx2l87OuZfOd6cpwctz4PsBy9bOmsX%2F5HfshIXqA0kNkacUFRds88wwo%2F3ygY6pgFHIXob%2FV%2FVPGM%2FY%2FsVAEYsiyBhDlgsi0KVm7wo41d40G%2BE2F6IUVeXdvz205TvhXfV0tZqFWJh99YNeUlQL%2BuWxqzQFV6U3rr4qWYrY7rTntlTaQ3AcEHcRy3Xy97V34aLzs4HjdDl165gs2g42W7CjXQiPKS%2FyZyUiZ6x3wbDyU3OGc5U4FFmKDiHdEuNSspG75t13CQbid264%2BfTTzC8TIVAuIs6&X-Amz-Signature=f88e3153f2b5ef5033f154617d4b624a3eeabfe9acae1d6ba77db5056c5edb75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZASXWAXI%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIESSQBxzAuOUF0t8VBt8CgcrqgyCsqsLTTlT1Pb1i4ExAiABqIPfGXORni8f702u%2FSh6yJW4nLBZ7KcGFXM5naudtyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMBtsgpetO5bscObZmKtwDrHFIiW%2FCzBTzxVPf9eKp6mFdwH5F%2B9tiYtypKjbXc%2FcJGuHvDVqSFRCwCh3lLU4SLE34RFeL6v4rZnYA1zydGImAkZy%2F4bxnROFlqdywNj7ndaVCA%2Bxhda1uAQ2IWnoZi06dEruANv%2FQlxT%2FuWAKZq2kFi3zEDWIvhyoCfghtLOuOQImvVzvsJTDKZLHw5X8%2BngsQiBnWCq%2B2rntERffKb7d167uYJGXMaln3ucKhT%2FFFGKN90zy0FnHe5PUXMIMgPzClWwfPYQp0FsmBwJSDCubmJadGHTwH8KP1cG4QR7VSvZAH4ad%2FQaJa6dH8Iqse3sVhbilSAx7rLkBwSKCE4%2BFLQ9W0KiZYVE0AYUmimRXGi0sLaTaPYZMeTQRn127r2SsPE4HTkAiiap6vBKcMkW8bCKm2T5RMEQi%2FeKDdyEFIb6CpJ9pcKU1HuT1IldfllPHWJwn5znNMF8UmRgrXscCp1jtPqCttvImKp%2FzvkR0E8Z9xCBm%2FOk706lGDoI1ikD74VPt167iphTIpPJJohl172IqSnZNyF1epfYGMg7cOiAgMuWoqGqknZ4235Ty0m%2B3hKOx2l87OuZfOd6cpwctz4PsBy9bOmsX%2F5HfshIXqA0kNkacUFRds88wwo%2F3ygY6pgFHIXob%2FV%2FVPGM%2FY%2FsVAEYsiyBhDlgsi0KVm7wo41d40G%2BE2F6IUVeXdvz205TvhXfV0tZqFWJh99YNeUlQL%2BuWxqzQFV6U3rr4qWYrY7rTntlTaQ3AcEHcRy3Xy97V34aLzs4HjdDl165gs2g42W7CjXQiPKS%2FyZyUiZ6x3wbDyU3OGc5U4FFmKDiHdEuNSspG75t13CQbid264%2BfTTzC8TIVAuIs6&X-Amz-Signature=2fff17d1383cc9eba52f30b20194d32c74b5adc566b2863692e3d04b0783ac83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZASXWAXI%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIESSQBxzAuOUF0t8VBt8CgcrqgyCsqsLTTlT1Pb1i4ExAiABqIPfGXORni8f702u%2FSh6yJW4nLBZ7KcGFXM5naudtyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMBtsgpetO5bscObZmKtwDrHFIiW%2FCzBTzxVPf9eKp6mFdwH5F%2B9tiYtypKjbXc%2FcJGuHvDVqSFRCwCh3lLU4SLE34RFeL6v4rZnYA1zydGImAkZy%2F4bxnROFlqdywNj7ndaVCA%2Bxhda1uAQ2IWnoZi06dEruANv%2FQlxT%2FuWAKZq2kFi3zEDWIvhyoCfghtLOuOQImvVzvsJTDKZLHw5X8%2BngsQiBnWCq%2B2rntERffKb7d167uYJGXMaln3ucKhT%2FFFGKN90zy0FnHe5PUXMIMgPzClWwfPYQp0FsmBwJSDCubmJadGHTwH8KP1cG4QR7VSvZAH4ad%2FQaJa6dH8Iqse3sVhbilSAx7rLkBwSKCE4%2BFLQ9W0KiZYVE0AYUmimRXGi0sLaTaPYZMeTQRn127r2SsPE4HTkAiiap6vBKcMkW8bCKm2T5RMEQi%2FeKDdyEFIb6CpJ9pcKU1HuT1IldfllPHWJwn5znNMF8UmRgrXscCp1jtPqCttvImKp%2FzvkR0E8Z9xCBm%2FOk706lGDoI1ikD74VPt167iphTIpPJJohl172IqSnZNyF1epfYGMg7cOiAgMuWoqGqknZ4235Ty0m%2B3hKOx2l87OuZfOd6cpwctz4PsBy9bOmsX%2F5HfshIXqA0kNkacUFRds88wwo%2F3ygY6pgFHIXob%2FV%2FVPGM%2FY%2FsVAEYsiyBhDlgsi0KVm7wo41d40G%2BE2F6IUVeXdvz205TvhXfV0tZqFWJh99YNeUlQL%2BuWxqzQFV6U3rr4qWYrY7rTntlTaQ3AcEHcRy3Xy97V34aLzs4HjdDl165gs2g42W7CjXQiPKS%2FyZyUiZ6x3wbDyU3OGc5U4FFmKDiHdEuNSspG75t13CQbid264%2BfTTzC8TIVAuIs6&X-Amz-Signature=97773241d804d181894c125f1ee95a6fd2eb0bd4f555a8bec5f72617a4101ba2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZASXWAXI%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIESSQBxzAuOUF0t8VBt8CgcrqgyCsqsLTTlT1Pb1i4ExAiABqIPfGXORni8f702u%2FSh6yJW4nLBZ7KcGFXM5naudtyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMBtsgpetO5bscObZmKtwDrHFIiW%2FCzBTzxVPf9eKp6mFdwH5F%2B9tiYtypKjbXc%2FcJGuHvDVqSFRCwCh3lLU4SLE34RFeL6v4rZnYA1zydGImAkZy%2F4bxnROFlqdywNj7ndaVCA%2Bxhda1uAQ2IWnoZi06dEruANv%2FQlxT%2FuWAKZq2kFi3zEDWIvhyoCfghtLOuOQImvVzvsJTDKZLHw5X8%2BngsQiBnWCq%2B2rntERffKb7d167uYJGXMaln3ucKhT%2FFFGKN90zy0FnHe5PUXMIMgPzClWwfPYQp0FsmBwJSDCubmJadGHTwH8KP1cG4QR7VSvZAH4ad%2FQaJa6dH8Iqse3sVhbilSAx7rLkBwSKCE4%2BFLQ9W0KiZYVE0AYUmimRXGi0sLaTaPYZMeTQRn127r2SsPE4HTkAiiap6vBKcMkW8bCKm2T5RMEQi%2FeKDdyEFIb6CpJ9pcKU1HuT1IldfllPHWJwn5znNMF8UmRgrXscCp1jtPqCttvImKp%2FzvkR0E8Z9xCBm%2FOk706lGDoI1ikD74VPt167iphTIpPJJohl172IqSnZNyF1epfYGMg7cOiAgMuWoqGqknZ4235Ty0m%2B3hKOx2l87OuZfOd6cpwctz4PsBy9bOmsX%2F5HfshIXqA0kNkacUFRds88wwo%2F3ygY6pgFHIXob%2FV%2FVPGM%2FY%2FsVAEYsiyBhDlgsi0KVm7wo41d40G%2BE2F6IUVeXdvz205TvhXfV0tZqFWJh99YNeUlQL%2BuWxqzQFV6U3rr4qWYrY7rTntlTaQ3AcEHcRy3Xy97V34aLzs4HjdDl165gs2g42W7CjXQiPKS%2FyZyUiZ6x3wbDyU3OGc5U4FFmKDiHdEuNSspG75t13CQbid264%2BfTTzC8TIVAuIs6&X-Amz-Signature=9b037c1e22413cb25833b9d687b95633e96a0305745fb91bea17e2c1a5cc343a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



