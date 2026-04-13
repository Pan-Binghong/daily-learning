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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUTUOPYR%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuwaFNnkKq79cVvJFsNQgJ7N11SISW%2FTIiDZtkx6xwCQIgG5uaV6pDJLwH5iQvwmP5tVbI4ncgyuQPc5Xk9FeeHaUq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDA0Z3OcQa1a3WrCwXCrcA%2FbH6cWtt%2BEnZDiImVOMrdrhuwJhYNMEUbGf7ybhCG5CCZotJ%2BoHZJMaeyV%2F9lYtGBTPCj7P7sK0mG5IfaC%2BFeUUTilrPMsOFMM6DjP9GoK6cr90%2BIyCLPIHHQEc9EogjFFvr3VdB1I6ka4W5iz5kaQqgroXcPKb1wuSU0N%2BRC4p4Tzkvz1oGqvtX60PTDFwsdRMcRYN0wuwVdp9eQsAm6yaAy%2BBGSbvgfD8fCYtvT8Co74XtXKaoCP1VRhsa3LFcV7rDmM0fUfOWdUfp4wIVsNosm3lJI5YefFuYsbO2n1ZpX4WXlo7wCwzfLPp3%2BrZkbaRHfrUeC0vMXyryQEoBquCr9Oa%2BdW13XTkKUd7u2YKuda5nGiv8UlpXj%2BRwqd2U5mAsgBv6TPaexkjwm0i4rSLouEvAfF%2BZGeHYAg%2BWZmh%2BVDB7dyDmdDrTcp4hk%2Bz1X5R3f%2BDc02%2BMrWzzwXvvvhcSCmsa2WbXy2Kb8i1yf6Ugs7CsYcooiqAkk8PCf1s2yKJfVfhq%2Bn61cwezJlivNtgjCP9I5%2FU3SWAuWA928rAD9qJD5Yz1bYbMUttT2V34Xj6b40bIn%2F5Xgxzky96AvW1T0DYtSdiGEQJ1dkvBcE9B3Tz0KCTqFXoZ%2FV%2BMIqx8c4GOqUBhBw8tYo1z9BSqkqPZYyrmecEP%2FduUAhnR30F7aKCqulLerRNNizaoU9z5m1Ez5az6r4VckmLPJiFniy54b1uxmcEk2d1FPJeEFm1wwYQdkDurqZPkHTBHEbew1aBY%2Bh6wIjMFrvajQZlVOj010HdNMQePtEoFfgN%2Fj4IpbQM2T8TRT%2B%2B3UYcu%2BNmTzUE1j59tE1Ft5Gmc9ecWY458cXZsvM%2B7C%2Fr&X-Amz-Signature=133162b747b669934d564597c44b1589cf06061f3a39e32cf1d6aa5b6b7b3e4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUTUOPYR%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuwaFNnkKq79cVvJFsNQgJ7N11SISW%2FTIiDZtkx6xwCQIgG5uaV6pDJLwH5iQvwmP5tVbI4ncgyuQPc5Xk9FeeHaUq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDA0Z3OcQa1a3WrCwXCrcA%2FbH6cWtt%2BEnZDiImVOMrdrhuwJhYNMEUbGf7ybhCG5CCZotJ%2BoHZJMaeyV%2F9lYtGBTPCj7P7sK0mG5IfaC%2BFeUUTilrPMsOFMM6DjP9GoK6cr90%2BIyCLPIHHQEc9EogjFFvr3VdB1I6ka4W5iz5kaQqgroXcPKb1wuSU0N%2BRC4p4Tzkvz1oGqvtX60PTDFwsdRMcRYN0wuwVdp9eQsAm6yaAy%2BBGSbvgfD8fCYtvT8Co74XtXKaoCP1VRhsa3LFcV7rDmM0fUfOWdUfp4wIVsNosm3lJI5YefFuYsbO2n1ZpX4WXlo7wCwzfLPp3%2BrZkbaRHfrUeC0vMXyryQEoBquCr9Oa%2BdW13XTkKUd7u2YKuda5nGiv8UlpXj%2BRwqd2U5mAsgBv6TPaexkjwm0i4rSLouEvAfF%2BZGeHYAg%2BWZmh%2BVDB7dyDmdDrTcp4hk%2Bz1X5R3f%2BDc02%2BMrWzzwXvvvhcSCmsa2WbXy2Kb8i1yf6Ugs7CsYcooiqAkk8PCf1s2yKJfVfhq%2Bn61cwezJlivNtgjCP9I5%2FU3SWAuWA928rAD9qJD5Yz1bYbMUttT2V34Xj6b40bIn%2F5Xgxzky96AvW1T0DYtSdiGEQJ1dkvBcE9B3Tz0KCTqFXoZ%2FV%2BMIqx8c4GOqUBhBw8tYo1z9BSqkqPZYyrmecEP%2FduUAhnR30F7aKCqulLerRNNizaoU9z5m1Ez5az6r4VckmLPJiFniy54b1uxmcEk2d1FPJeEFm1wwYQdkDurqZPkHTBHEbew1aBY%2Bh6wIjMFrvajQZlVOj010HdNMQePtEoFfgN%2Fj4IpbQM2T8TRT%2B%2B3UYcu%2BNmTzUE1j59tE1Ft5Gmc9ecWY458cXZsvM%2B7C%2Fr&X-Amz-Signature=904c0edc7902546ac94538bc25a5b86e6d7dcf71ac93241fb8ed49484871ddf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUTUOPYR%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuwaFNnkKq79cVvJFsNQgJ7N11SISW%2FTIiDZtkx6xwCQIgG5uaV6pDJLwH5iQvwmP5tVbI4ncgyuQPc5Xk9FeeHaUq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDA0Z3OcQa1a3WrCwXCrcA%2FbH6cWtt%2BEnZDiImVOMrdrhuwJhYNMEUbGf7ybhCG5CCZotJ%2BoHZJMaeyV%2F9lYtGBTPCj7P7sK0mG5IfaC%2BFeUUTilrPMsOFMM6DjP9GoK6cr90%2BIyCLPIHHQEc9EogjFFvr3VdB1I6ka4W5iz5kaQqgroXcPKb1wuSU0N%2BRC4p4Tzkvz1oGqvtX60PTDFwsdRMcRYN0wuwVdp9eQsAm6yaAy%2BBGSbvgfD8fCYtvT8Co74XtXKaoCP1VRhsa3LFcV7rDmM0fUfOWdUfp4wIVsNosm3lJI5YefFuYsbO2n1ZpX4WXlo7wCwzfLPp3%2BrZkbaRHfrUeC0vMXyryQEoBquCr9Oa%2BdW13XTkKUd7u2YKuda5nGiv8UlpXj%2BRwqd2U5mAsgBv6TPaexkjwm0i4rSLouEvAfF%2BZGeHYAg%2BWZmh%2BVDB7dyDmdDrTcp4hk%2Bz1X5R3f%2BDc02%2BMrWzzwXvvvhcSCmsa2WbXy2Kb8i1yf6Ugs7CsYcooiqAkk8PCf1s2yKJfVfhq%2Bn61cwezJlivNtgjCP9I5%2FU3SWAuWA928rAD9qJD5Yz1bYbMUttT2V34Xj6b40bIn%2F5Xgxzky96AvW1T0DYtSdiGEQJ1dkvBcE9B3Tz0KCTqFXoZ%2FV%2BMIqx8c4GOqUBhBw8tYo1z9BSqkqPZYyrmecEP%2FduUAhnR30F7aKCqulLerRNNizaoU9z5m1Ez5az6r4VckmLPJiFniy54b1uxmcEk2d1FPJeEFm1wwYQdkDurqZPkHTBHEbew1aBY%2Bh6wIjMFrvajQZlVOj010HdNMQePtEoFfgN%2Fj4IpbQM2T8TRT%2B%2B3UYcu%2BNmTzUE1j59tE1Ft5Gmc9ecWY458cXZsvM%2B7C%2Fr&X-Amz-Signature=80e9e0047111b2e2eb5811fb3a97fe059cd517d61e27ea44c603ee0ce5a57609&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUTUOPYR%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCuwaFNnkKq79cVvJFsNQgJ7N11SISW%2FTIiDZtkx6xwCQIgG5uaV6pDJLwH5iQvwmP5tVbI4ncgyuQPc5Xk9FeeHaUq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDA0Z3OcQa1a3WrCwXCrcA%2FbH6cWtt%2BEnZDiImVOMrdrhuwJhYNMEUbGf7ybhCG5CCZotJ%2BoHZJMaeyV%2F9lYtGBTPCj7P7sK0mG5IfaC%2BFeUUTilrPMsOFMM6DjP9GoK6cr90%2BIyCLPIHHQEc9EogjFFvr3VdB1I6ka4W5iz5kaQqgroXcPKb1wuSU0N%2BRC4p4Tzkvz1oGqvtX60PTDFwsdRMcRYN0wuwVdp9eQsAm6yaAy%2BBGSbvgfD8fCYtvT8Co74XtXKaoCP1VRhsa3LFcV7rDmM0fUfOWdUfp4wIVsNosm3lJI5YefFuYsbO2n1ZpX4WXlo7wCwzfLPp3%2BrZkbaRHfrUeC0vMXyryQEoBquCr9Oa%2BdW13XTkKUd7u2YKuda5nGiv8UlpXj%2BRwqd2U5mAsgBv6TPaexkjwm0i4rSLouEvAfF%2BZGeHYAg%2BWZmh%2BVDB7dyDmdDrTcp4hk%2Bz1X5R3f%2BDc02%2BMrWzzwXvvvhcSCmsa2WbXy2Kb8i1yf6Ugs7CsYcooiqAkk8PCf1s2yKJfVfhq%2Bn61cwezJlivNtgjCP9I5%2FU3SWAuWA928rAD9qJD5Yz1bYbMUttT2V34Xj6b40bIn%2F5Xgxzky96AvW1T0DYtSdiGEQJ1dkvBcE9B3Tz0KCTqFXoZ%2FV%2BMIqx8c4GOqUBhBw8tYo1z9BSqkqPZYyrmecEP%2FduUAhnR30F7aKCqulLerRNNizaoU9z5m1Ez5az6r4VckmLPJiFniy54b1uxmcEk2d1FPJeEFm1wwYQdkDurqZPkHTBHEbew1aBY%2Bh6wIjMFrvajQZlVOj010HdNMQePtEoFfgN%2Fj4IpbQM2T8TRT%2B%2B3UYcu%2BNmTzUE1j59tE1Ft5Gmc9ecWY458cXZsvM%2B7C%2Fr&X-Amz-Signature=a113c25b0de092c164442262a9400bfe55761b190ab0db080f88b24dceb3e402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



