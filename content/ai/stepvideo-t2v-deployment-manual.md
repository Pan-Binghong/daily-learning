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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VOBI6F%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTT%2FDinUq8Dn%2FtRtpppVfQTh2mpdJSCKUhL7dN2aoLOwIgeWskE27mc6jqREHWNJnoRsFYaQkx3FsPYM2m%2FrrhiVsq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDN2qKbeEo4CS7XlmeSrcAx2AGOwED0CiD46wGhQyyaUY6IOvnonC0WL%2FNx1Rqnb6%2F2Vt2AEcpFha6FS3R8b8P9OJyZOBQmxaVAxLMWJz3QM2R9BSKiWJERst5yJ5NXC0K%2B%2FFkke1vOJvD0R6EGgovk3x%2BN3w31xMrHF1WB5ZyQ0MJemh6iI59rZFdZBn98Lq2%2FZE5TX4KREpuqIyDG%2B%2BWvXRw%2FTuQDWbyN9T6ujAI2OPLSPqp7fJdX0UYqw44%2B6x3%2FeFIWW1u98IKheljmPwxNKcLpPnxa89VZB3160%2F36UAb%2BCKwAw09DVN7mnaww0iCGZK9Hp8P4G%2B843LFuslfZ%2FAnBRU%2BZ7LZe7Tt9dbB8aJUwDEdinWQyLdqrva%2BIKVe2nojNGM3tdvd0Q88W1Ox%2Fv8s0KDqqrg1UwoPGxKxSN6vo3CQ4NPMFUpL8rHeRE2jvSx%2Ba9ZhBGc%2B4HtJbcMaOE7UdhVYt3DQSHAM%2BfarzMfyXpOGJ9Yuf%2FuV3qlbWKCk4GOrQitC7x10lDx%2FLP9SsGMVDUU8g7RphJy7stsWaHdDrnsS%2FmXrYUrHFsEHpy49bd3mKL0QVpvaQacV9hXJEQusWVA9uhq7ZNwlz3PuL8ZWrF8pu0GazJw4hy74Zo%2BRIRZs7W6oLLf4E3qMOPNqs8GOqUBeBfIar3Qptdd%2BUo8r6n1vjgp%2Bv97RkdQOZEuTBQOaSmgmzdRcjsXVU7dy%2FJ8Dga6UMzcrSl1LgzDdPy5yfJzWpyxERrGPW%2FkJW%2FDb%2BbRti50%2BgHf%2FZMFAuZ8mBBeTbjJ5EuK%2FwXD0PGhnckdzOUuXU4hvrvL5mEzrH9ez4JQ7k96mTQ%2Fr5ICDqkF16fujwHUghK%2BqVdgtoB1sXc35xMY%2BLseym8i&X-Amz-Signature=3edfc3e266d5650d08f31c4fab91ce4850a43362a93371314b5779f634a34886&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VOBI6F%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTT%2FDinUq8Dn%2FtRtpppVfQTh2mpdJSCKUhL7dN2aoLOwIgeWskE27mc6jqREHWNJnoRsFYaQkx3FsPYM2m%2FrrhiVsq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDN2qKbeEo4CS7XlmeSrcAx2AGOwED0CiD46wGhQyyaUY6IOvnonC0WL%2FNx1Rqnb6%2F2Vt2AEcpFha6FS3R8b8P9OJyZOBQmxaVAxLMWJz3QM2R9BSKiWJERst5yJ5NXC0K%2B%2FFkke1vOJvD0R6EGgovk3x%2BN3w31xMrHF1WB5ZyQ0MJemh6iI59rZFdZBn98Lq2%2FZE5TX4KREpuqIyDG%2B%2BWvXRw%2FTuQDWbyN9T6ujAI2OPLSPqp7fJdX0UYqw44%2B6x3%2FeFIWW1u98IKheljmPwxNKcLpPnxa89VZB3160%2F36UAb%2BCKwAw09DVN7mnaww0iCGZK9Hp8P4G%2B843LFuslfZ%2FAnBRU%2BZ7LZe7Tt9dbB8aJUwDEdinWQyLdqrva%2BIKVe2nojNGM3tdvd0Q88W1Ox%2Fv8s0KDqqrg1UwoPGxKxSN6vo3CQ4NPMFUpL8rHeRE2jvSx%2Ba9ZhBGc%2B4HtJbcMaOE7UdhVYt3DQSHAM%2BfarzMfyXpOGJ9Yuf%2FuV3qlbWKCk4GOrQitC7x10lDx%2FLP9SsGMVDUU8g7RphJy7stsWaHdDrnsS%2FmXrYUrHFsEHpy49bd3mKL0QVpvaQacV9hXJEQusWVA9uhq7ZNwlz3PuL8ZWrF8pu0GazJw4hy74Zo%2BRIRZs7W6oLLf4E3qMOPNqs8GOqUBeBfIar3Qptdd%2BUo8r6n1vjgp%2Bv97RkdQOZEuTBQOaSmgmzdRcjsXVU7dy%2FJ8Dga6UMzcrSl1LgzDdPy5yfJzWpyxERrGPW%2FkJW%2FDb%2BbRti50%2BgHf%2FZMFAuZ8mBBeTbjJ5EuK%2FwXD0PGhnckdzOUuXU4hvrvL5mEzrH9ez4JQ7k96mTQ%2Fr5ICDqkF16fujwHUghK%2BqVdgtoB1sXc35xMY%2BLseym8i&X-Amz-Signature=1967069ad85dbbce7a7af98ba65d80553e25e8a985f6d2115e4573ae8386a577&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VOBI6F%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTT%2FDinUq8Dn%2FtRtpppVfQTh2mpdJSCKUhL7dN2aoLOwIgeWskE27mc6jqREHWNJnoRsFYaQkx3FsPYM2m%2FrrhiVsq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDN2qKbeEo4CS7XlmeSrcAx2AGOwED0CiD46wGhQyyaUY6IOvnonC0WL%2FNx1Rqnb6%2F2Vt2AEcpFha6FS3R8b8P9OJyZOBQmxaVAxLMWJz3QM2R9BSKiWJERst5yJ5NXC0K%2B%2FFkke1vOJvD0R6EGgovk3x%2BN3w31xMrHF1WB5ZyQ0MJemh6iI59rZFdZBn98Lq2%2FZE5TX4KREpuqIyDG%2B%2BWvXRw%2FTuQDWbyN9T6ujAI2OPLSPqp7fJdX0UYqw44%2B6x3%2FeFIWW1u98IKheljmPwxNKcLpPnxa89VZB3160%2F36UAb%2BCKwAw09DVN7mnaww0iCGZK9Hp8P4G%2B843LFuslfZ%2FAnBRU%2BZ7LZe7Tt9dbB8aJUwDEdinWQyLdqrva%2BIKVe2nojNGM3tdvd0Q88W1Ox%2Fv8s0KDqqrg1UwoPGxKxSN6vo3CQ4NPMFUpL8rHeRE2jvSx%2Ba9ZhBGc%2B4HtJbcMaOE7UdhVYt3DQSHAM%2BfarzMfyXpOGJ9Yuf%2FuV3qlbWKCk4GOrQitC7x10lDx%2FLP9SsGMVDUU8g7RphJy7stsWaHdDrnsS%2FmXrYUrHFsEHpy49bd3mKL0QVpvaQacV9hXJEQusWVA9uhq7ZNwlz3PuL8ZWrF8pu0GazJw4hy74Zo%2BRIRZs7W6oLLf4E3qMOPNqs8GOqUBeBfIar3Qptdd%2BUo8r6n1vjgp%2Bv97RkdQOZEuTBQOaSmgmzdRcjsXVU7dy%2FJ8Dga6UMzcrSl1LgzDdPy5yfJzWpyxERrGPW%2FkJW%2FDb%2BbRti50%2BgHf%2FZMFAuZ8mBBeTbjJ5EuK%2FwXD0PGhnckdzOUuXU4hvrvL5mEzrH9ez4JQ7k96mTQ%2Fr5ICDqkF16fujwHUghK%2BqVdgtoB1sXc35xMY%2BLseym8i&X-Amz-Signature=7bdae6d1e8b1f649da532b9fb4ef1b09224876bbd5f52a902bfcc24519fe2405&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2VOBI6F%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTT%2FDinUq8Dn%2FtRtpppVfQTh2mpdJSCKUhL7dN2aoLOwIgeWskE27mc6jqREHWNJnoRsFYaQkx3FsPYM2m%2FrrhiVsq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDN2qKbeEo4CS7XlmeSrcAx2AGOwED0CiD46wGhQyyaUY6IOvnonC0WL%2FNx1Rqnb6%2F2Vt2AEcpFha6FS3R8b8P9OJyZOBQmxaVAxLMWJz3QM2R9BSKiWJERst5yJ5NXC0K%2B%2FFkke1vOJvD0R6EGgovk3x%2BN3w31xMrHF1WB5ZyQ0MJemh6iI59rZFdZBn98Lq2%2FZE5TX4KREpuqIyDG%2B%2BWvXRw%2FTuQDWbyN9T6ujAI2OPLSPqp7fJdX0UYqw44%2B6x3%2FeFIWW1u98IKheljmPwxNKcLpPnxa89VZB3160%2F36UAb%2BCKwAw09DVN7mnaww0iCGZK9Hp8P4G%2B843LFuslfZ%2FAnBRU%2BZ7LZe7Tt9dbB8aJUwDEdinWQyLdqrva%2BIKVe2nojNGM3tdvd0Q88W1Ox%2Fv8s0KDqqrg1UwoPGxKxSN6vo3CQ4NPMFUpL8rHeRE2jvSx%2Ba9ZhBGc%2B4HtJbcMaOE7UdhVYt3DQSHAM%2BfarzMfyXpOGJ9Yuf%2FuV3qlbWKCk4GOrQitC7x10lDx%2FLP9SsGMVDUU8g7RphJy7stsWaHdDrnsS%2FmXrYUrHFsEHpy49bd3mKL0QVpvaQacV9hXJEQusWVA9uhq7ZNwlz3PuL8ZWrF8pu0GazJw4hy74Zo%2BRIRZs7W6oLLf4E3qMOPNqs8GOqUBeBfIar3Qptdd%2BUo8r6n1vjgp%2Bv97RkdQOZEuTBQOaSmgmzdRcjsXVU7dy%2FJ8Dga6UMzcrSl1LgzDdPy5yfJzWpyxERrGPW%2FkJW%2FDb%2BbRti50%2BgHf%2FZMFAuZ8mBBeTbjJ5EuK%2FwXD0PGhnckdzOUuXU4hvrvL5mEzrH9ez4JQ7k96mTQ%2Fr5ICDqkF16fujwHUghK%2BqVdgtoB1sXc35xMY%2BLseym8i&X-Amz-Signature=c115c56140c38499368d56bd1e89406395b6f5433ac4c3f0d5c1c01a1796de1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



