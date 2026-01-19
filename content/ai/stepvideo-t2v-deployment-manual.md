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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6MQ5RGW%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFLMJMfpp%2BD%2BLfOyI8yMlvw5osjhl0wsXbBC%2FGY3n1%2FHAiEAm9gA5ePBHu0vFKAcjDK4byGRXmnLiWUqKFpqVgGE%2FkwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2FHKOifuMqNjowvDCrcA5VGT2H%2BUVZwV9awwhC07ijUeQisRWmCDLg%2FDkNdpwkv8JRhC14cgViA%2FA8HXJd13XMTNQrfWLIpFQInZuihts%2BQGdJYwm4xPg4weftCBKzabFddNrtgjrHkBcm4u4waOyQfFyqfGVIqYTTGakITtBXlGCgb4L7LUgAcerpZ4kZ%2BSQI70m5sRK6XO%2FM5S5rNCkFbA2Jrg9fUrIFN%2B6JtNjVFa62eSgorA0AxQuUgr51XmNv3%2FomCLDmbQAhdU%2B2%2F55DEo2FD%2F3aLAMYhuxvKUDPA%2FUC4x%2Fz5FUf8%2BH20uEq7J3fJPYOOzBFHFwfrs7Dtbxht0QaR%2BpPHxJzBUSa6WdRK19bvt04OdhbtqUIC1L%2BSO9%2BrmqktfYrB704HV1kngH6sUad7sT08rzkceojmcDe2OivI%2BZO3wQEk64Gg%2BATLDrGnUenWIgwlvn02c4iMlrHebQBjkQCg2eZanTi8mUYWZnPR0RS7uPIt21hgglGfXEMGrHQT7jtgcg2hxnU4mSMROGe4PWMWVKEqi7ZWII4s8S85ly%2BH2xR5grWakM1m8gyqjnIHta1Lc5SC4PlKb3cqZyXf5N02AwXgBz%2ByvWo5bLWxJ4GV0RXwaMTRZYt4gFqGG35cq%2F97ICTXMITdtcsGOqUBtzkPiISjukEkDMhkUoywx%2BxFl7Dxpm%2BEr9AFb1ZmNHusQCcyaTtjkYoLhOoRKKtzrFW5XHPo%2F8Z0aG49mniRmtv7gmSFEuAdfknqaYUlJSnAmfGh21Yyjn3kapFvrAL2A9cEIA0ZLk8qa8qF7Rbb59AXBWR56IKdqIKpiPaBXJqflOPYVxciUyWUMRwREFyMkezu6oQaMtLuTgdzMS%2FUoW1q%2B2vV&X-Amz-Signature=b16141499c2dd73635a058366682685159d228896d795425cdfb6c6940fd2dd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6MQ5RGW%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFLMJMfpp%2BD%2BLfOyI8yMlvw5osjhl0wsXbBC%2FGY3n1%2FHAiEAm9gA5ePBHu0vFKAcjDK4byGRXmnLiWUqKFpqVgGE%2FkwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2FHKOifuMqNjowvDCrcA5VGT2H%2BUVZwV9awwhC07ijUeQisRWmCDLg%2FDkNdpwkv8JRhC14cgViA%2FA8HXJd13XMTNQrfWLIpFQInZuihts%2BQGdJYwm4xPg4weftCBKzabFddNrtgjrHkBcm4u4waOyQfFyqfGVIqYTTGakITtBXlGCgb4L7LUgAcerpZ4kZ%2BSQI70m5sRK6XO%2FM5S5rNCkFbA2Jrg9fUrIFN%2B6JtNjVFa62eSgorA0AxQuUgr51XmNv3%2FomCLDmbQAhdU%2B2%2F55DEo2FD%2F3aLAMYhuxvKUDPA%2FUC4x%2Fz5FUf8%2BH20uEq7J3fJPYOOzBFHFwfrs7Dtbxht0QaR%2BpPHxJzBUSa6WdRK19bvt04OdhbtqUIC1L%2BSO9%2BrmqktfYrB704HV1kngH6sUad7sT08rzkceojmcDe2OivI%2BZO3wQEk64Gg%2BATLDrGnUenWIgwlvn02c4iMlrHebQBjkQCg2eZanTi8mUYWZnPR0RS7uPIt21hgglGfXEMGrHQT7jtgcg2hxnU4mSMROGe4PWMWVKEqi7ZWII4s8S85ly%2BH2xR5grWakM1m8gyqjnIHta1Lc5SC4PlKb3cqZyXf5N02AwXgBz%2ByvWo5bLWxJ4GV0RXwaMTRZYt4gFqGG35cq%2F97ICTXMITdtcsGOqUBtzkPiISjukEkDMhkUoywx%2BxFl7Dxpm%2BEr9AFb1ZmNHusQCcyaTtjkYoLhOoRKKtzrFW5XHPo%2F8Z0aG49mniRmtv7gmSFEuAdfknqaYUlJSnAmfGh21Yyjn3kapFvrAL2A9cEIA0ZLk8qa8qF7Rbb59AXBWR56IKdqIKpiPaBXJqflOPYVxciUyWUMRwREFyMkezu6oQaMtLuTgdzMS%2FUoW1q%2B2vV&X-Amz-Signature=d7d33b3148f3fd628bc087c26f827dfd90e3a5dcea409524e90b5eb13127e13e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6MQ5RGW%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFLMJMfpp%2BD%2BLfOyI8yMlvw5osjhl0wsXbBC%2FGY3n1%2FHAiEAm9gA5ePBHu0vFKAcjDK4byGRXmnLiWUqKFpqVgGE%2FkwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2FHKOifuMqNjowvDCrcA5VGT2H%2BUVZwV9awwhC07ijUeQisRWmCDLg%2FDkNdpwkv8JRhC14cgViA%2FA8HXJd13XMTNQrfWLIpFQInZuihts%2BQGdJYwm4xPg4weftCBKzabFddNrtgjrHkBcm4u4waOyQfFyqfGVIqYTTGakITtBXlGCgb4L7LUgAcerpZ4kZ%2BSQI70m5sRK6XO%2FM5S5rNCkFbA2Jrg9fUrIFN%2B6JtNjVFa62eSgorA0AxQuUgr51XmNv3%2FomCLDmbQAhdU%2B2%2F55DEo2FD%2F3aLAMYhuxvKUDPA%2FUC4x%2Fz5FUf8%2BH20uEq7J3fJPYOOzBFHFwfrs7Dtbxht0QaR%2BpPHxJzBUSa6WdRK19bvt04OdhbtqUIC1L%2BSO9%2BrmqktfYrB704HV1kngH6sUad7sT08rzkceojmcDe2OivI%2BZO3wQEk64Gg%2BATLDrGnUenWIgwlvn02c4iMlrHebQBjkQCg2eZanTi8mUYWZnPR0RS7uPIt21hgglGfXEMGrHQT7jtgcg2hxnU4mSMROGe4PWMWVKEqi7ZWII4s8S85ly%2BH2xR5grWakM1m8gyqjnIHta1Lc5SC4PlKb3cqZyXf5N02AwXgBz%2ByvWo5bLWxJ4GV0RXwaMTRZYt4gFqGG35cq%2F97ICTXMITdtcsGOqUBtzkPiISjukEkDMhkUoywx%2BxFl7Dxpm%2BEr9AFb1ZmNHusQCcyaTtjkYoLhOoRKKtzrFW5XHPo%2F8Z0aG49mniRmtv7gmSFEuAdfknqaYUlJSnAmfGh21Yyjn3kapFvrAL2A9cEIA0ZLk8qa8qF7Rbb59AXBWR56IKdqIKpiPaBXJqflOPYVxciUyWUMRwREFyMkezu6oQaMtLuTgdzMS%2FUoW1q%2B2vV&X-Amz-Signature=e7f950eb734727d873ce78d0a3ddb0ac16f2a582e6290c6637cb447dfefe968e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6MQ5RGW%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFLMJMfpp%2BD%2BLfOyI8yMlvw5osjhl0wsXbBC%2FGY3n1%2FHAiEAm9gA5ePBHu0vFKAcjDK4byGRXmnLiWUqKFpqVgGE%2FkwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ%2FHKOifuMqNjowvDCrcA5VGT2H%2BUVZwV9awwhC07ijUeQisRWmCDLg%2FDkNdpwkv8JRhC14cgViA%2FA8HXJd13XMTNQrfWLIpFQInZuihts%2BQGdJYwm4xPg4weftCBKzabFddNrtgjrHkBcm4u4waOyQfFyqfGVIqYTTGakITtBXlGCgb4L7LUgAcerpZ4kZ%2BSQI70m5sRK6XO%2FM5S5rNCkFbA2Jrg9fUrIFN%2B6JtNjVFa62eSgorA0AxQuUgr51XmNv3%2FomCLDmbQAhdU%2B2%2F55DEo2FD%2F3aLAMYhuxvKUDPA%2FUC4x%2Fz5FUf8%2BH20uEq7J3fJPYOOzBFHFwfrs7Dtbxht0QaR%2BpPHxJzBUSa6WdRK19bvt04OdhbtqUIC1L%2BSO9%2BrmqktfYrB704HV1kngH6sUad7sT08rzkceojmcDe2OivI%2BZO3wQEk64Gg%2BATLDrGnUenWIgwlvn02c4iMlrHebQBjkQCg2eZanTi8mUYWZnPR0RS7uPIt21hgglGfXEMGrHQT7jtgcg2hxnU4mSMROGe4PWMWVKEqi7ZWII4s8S85ly%2BH2xR5grWakM1m8gyqjnIHta1Lc5SC4PlKb3cqZyXf5N02AwXgBz%2ByvWo5bLWxJ4GV0RXwaMTRZYt4gFqGG35cq%2F97ICTXMITdtcsGOqUBtzkPiISjukEkDMhkUoywx%2BxFl7Dxpm%2BEr9AFb1ZmNHusQCcyaTtjkYoLhOoRKKtzrFW5XHPo%2F8Z0aG49mniRmtv7gmSFEuAdfknqaYUlJSnAmfGh21Yyjn3kapFvrAL2A9cEIA0ZLk8qa8qF7Rbb59AXBWR56IKdqIKpiPaBXJqflOPYVxciUyWUMRwREFyMkezu6oQaMtLuTgdzMS%2FUoW1q%2B2vV&X-Amz-Signature=9f3ee9affde734d21ecfccaef9140c7ee8dc1f7fc1db461b32ebd1e34d4a78b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



