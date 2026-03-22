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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR3ZNAC4%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkCtc2ziRmBA77g8w%2FldprMsjoU%2FGxu15HLYvDJ92tIAiEAncDt8Gf5qoyXHcbomAp8%2FmlBWFnh88T7ILix6M3f%2Bagq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDHIN93KLbrwHR7OIOircAyllQHWc9aT9H%2B%2BiXqkKkpczXBbIz3MTNJWyoXOvHwLx4%2FKD69UlJifjJUefKn1SBw9MtZR2rHfSyRtZYiFrf4BhO17qj0BNPXnxO4nkBBaxNXJOo3xU3bzHlqDqcQC0poh7N1yJOWRI0ZIMSgrXkSBleAYoWxFUHBXvg1rdcuOwc6%2BnwWnAUjk1UdAJduCIg4cRvzvya7znYLm7q3j1qHmwLsY4U5OSFsS2Zh%2FswMURKwNJXeSjUT%2BcsgoXpQf7j20yVhBBZKrOwVDC3kfYrNGVYGMmNXhdA1giwJpWoLM4T8mIiaf3m5nE3BYBCzP44hGDAbSwJ65XQYkYQuOchpr9KUmfGdXVDr2sRg90EUTzzzSS3pWe7DTzIk2xVfOvfrvgJReYm64TD0OTPyQV9O%2Fvxj%2F84GsagcBGB1l2qOH0mJEwYy2bgrdmqG5sqI4YI1OWoHtrzUf2SFPOOBiAxlDPzDttz9uvgYrzw9%2BzrUxoz8ujuPcuwC0STnzCDgZy487TpP%2BtQw3H5kadtEB0oS1mDeUHPtXvMPrKHK2WA5nQwyGVDbnSw8cXKGxw%2Fs7t4t5epzwV70Ysqj5N43H9cX8HP%2FUeI11%2Fq4%2Fh6QzvijqbjOKtwnkX549kebSgMPWs%2Fc0GOqUBG2fS7b3SbkGVwrZxQCmMfwedcvo9ACvmd69bJe3jydv2k8MkHXqEgPExsgK8LTgpIcCmIN1kqu9c7qnwU8mtyVjQu1LcsKeCJMKlszASdMpK89%2BpI0mYJZEj8LbcMCp%2Ba3LvZOipWCKLtqfXCotgib%2FLfY%2FbPpx8lGgbzxqF31eezznAZDOXQQq9rsiR6L7KvUwiVCfYSbCwev35uUY96PYrYSfN&X-Amz-Signature=49dcd63a493a8dc280d043aee21fe2d83c208f8604fc1c75907316fd0dfb77bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR3ZNAC4%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkCtc2ziRmBA77g8w%2FldprMsjoU%2FGxu15HLYvDJ92tIAiEAncDt8Gf5qoyXHcbomAp8%2FmlBWFnh88T7ILix6M3f%2Bagq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDHIN93KLbrwHR7OIOircAyllQHWc9aT9H%2B%2BiXqkKkpczXBbIz3MTNJWyoXOvHwLx4%2FKD69UlJifjJUefKn1SBw9MtZR2rHfSyRtZYiFrf4BhO17qj0BNPXnxO4nkBBaxNXJOo3xU3bzHlqDqcQC0poh7N1yJOWRI0ZIMSgrXkSBleAYoWxFUHBXvg1rdcuOwc6%2BnwWnAUjk1UdAJduCIg4cRvzvya7znYLm7q3j1qHmwLsY4U5OSFsS2Zh%2FswMURKwNJXeSjUT%2BcsgoXpQf7j20yVhBBZKrOwVDC3kfYrNGVYGMmNXhdA1giwJpWoLM4T8mIiaf3m5nE3BYBCzP44hGDAbSwJ65XQYkYQuOchpr9KUmfGdXVDr2sRg90EUTzzzSS3pWe7DTzIk2xVfOvfrvgJReYm64TD0OTPyQV9O%2Fvxj%2F84GsagcBGB1l2qOH0mJEwYy2bgrdmqG5sqI4YI1OWoHtrzUf2SFPOOBiAxlDPzDttz9uvgYrzw9%2BzrUxoz8ujuPcuwC0STnzCDgZy487TpP%2BtQw3H5kadtEB0oS1mDeUHPtXvMPrKHK2WA5nQwyGVDbnSw8cXKGxw%2Fs7t4t5epzwV70Ysqj5N43H9cX8HP%2FUeI11%2Fq4%2Fh6QzvijqbjOKtwnkX549kebSgMPWs%2Fc0GOqUBG2fS7b3SbkGVwrZxQCmMfwedcvo9ACvmd69bJe3jydv2k8MkHXqEgPExsgK8LTgpIcCmIN1kqu9c7qnwU8mtyVjQu1LcsKeCJMKlszASdMpK89%2BpI0mYJZEj8LbcMCp%2Ba3LvZOipWCKLtqfXCotgib%2FLfY%2FbPpx8lGgbzxqF31eezznAZDOXQQq9rsiR6L7KvUwiVCfYSbCwev35uUY96PYrYSfN&X-Amz-Signature=32bb561d08ceb3fe33b6fc69a23b6a8d16b108d391206e3b295f3c3ecac41b34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR3ZNAC4%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkCtc2ziRmBA77g8w%2FldprMsjoU%2FGxu15HLYvDJ92tIAiEAncDt8Gf5qoyXHcbomAp8%2FmlBWFnh88T7ILix6M3f%2Bagq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDHIN93KLbrwHR7OIOircAyllQHWc9aT9H%2B%2BiXqkKkpczXBbIz3MTNJWyoXOvHwLx4%2FKD69UlJifjJUefKn1SBw9MtZR2rHfSyRtZYiFrf4BhO17qj0BNPXnxO4nkBBaxNXJOo3xU3bzHlqDqcQC0poh7N1yJOWRI0ZIMSgrXkSBleAYoWxFUHBXvg1rdcuOwc6%2BnwWnAUjk1UdAJduCIg4cRvzvya7znYLm7q3j1qHmwLsY4U5OSFsS2Zh%2FswMURKwNJXeSjUT%2BcsgoXpQf7j20yVhBBZKrOwVDC3kfYrNGVYGMmNXhdA1giwJpWoLM4T8mIiaf3m5nE3BYBCzP44hGDAbSwJ65XQYkYQuOchpr9KUmfGdXVDr2sRg90EUTzzzSS3pWe7DTzIk2xVfOvfrvgJReYm64TD0OTPyQV9O%2Fvxj%2F84GsagcBGB1l2qOH0mJEwYy2bgrdmqG5sqI4YI1OWoHtrzUf2SFPOOBiAxlDPzDttz9uvgYrzw9%2BzrUxoz8ujuPcuwC0STnzCDgZy487TpP%2BtQw3H5kadtEB0oS1mDeUHPtXvMPrKHK2WA5nQwyGVDbnSw8cXKGxw%2Fs7t4t5epzwV70Ysqj5N43H9cX8HP%2FUeI11%2Fq4%2Fh6QzvijqbjOKtwnkX549kebSgMPWs%2Fc0GOqUBG2fS7b3SbkGVwrZxQCmMfwedcvo9ACvmd69bJe3jydv2k8MkHXqEgPExsgK8LTgpIcCmIN1kqu9c7qnwU8mtyVjQu1LcsKeCJMKlszASdMpK89%2BpI0mYJZEj8LbcMCp%2Ba3LvZOipWCKLtqfXCotgib%2FLfY%2FbPpx8lGgbzxqF31eezznAZDOXQQq9rsiR6L7KvUwiVCfYSbCwev35uUY96PYrYSfN&X-Amz-Signature=82e80980d7b0e22e6706b5e45fa4b8a0614b974fdf9613066eeee25fb1a20568&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR3ZNAC4%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGkCtc2ziRmBA77g8w%2FldprMsjoU%2FGxu15HLYvDJ92tIAiEAncDt8Gf5qoyXHcbomAp8%2FmlBWFnh88T7ILix6M3f%2Bagq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDHIN93KLbrwHR7OIOircAyllQHWc9aT9H%2B%2BiXqkKkpczXBbIz3MTNJWyoXOvHwLx4%2FKD69UlJifjJUefKn1SBw9MtZR2rHfSyRtZYiFrf4BhO17qj0BNPXnxO4nkBBaxNXJOo3xU3bzHlqDqcQC0poh7N1yJOWRI0ZIMSgrXkSBleAYoWxFUHBXvg1rdcuOwc6%2BnwWnAUjk1UdAJduCIg4cRvzvya7znYLm7q3j1qHmwLsY4U5OSFsS2Zh%2FswMURKwNJXeSjUT%2BcsgoXpQf7j20yVhBBZKrOwVDC3kfYrNGVYGMmNXhdA1giwJpWoLM4T8mIiaf3m5nE3BYBCzP44hGDAbSwJ65XQYkYQuOchpr9KUmfGdXVDr2sRg90EUTzzzSS3pWe7DTzIk2xVfOvfrvgJReYm64TD0OTPyQV9O%2Fvxj%2F84GsagcBGB1l2qOH0mJEwYy2bgrdmqG5sqI4YI1OWoHtrzUf2SFPOOBiAxlDPzDttz9uvgYrzw9%2BzrUxoz8ujuPcuwC0STnzCDgZy487TpP%2BtQw3H5kadtEB0oS1mDeUHPtXvMPrKHK2WA5nQwyGVDbnSw8cXKGxw%2Fs7t4t5epzwV70Ysqj5N43H9cX8HP%2FUeI11%2Fq4%2Fh6QzvijqbjOKtwnkX549kebSgMPWs%2Fc0GOqUBG2fS7b3SbkGVwrZxQCmMfwedcvo9ACvmd69bJe3jydv2k8MkHXqEgPExsgK8LTgpIcCmIN1kqu9c7qnwU8mtyVjQu1LcsKeCJMKlszASdMpK89%2BpI0mYJZEj8LbcMCp%2Ba3LvZOipWCKLtqfXCotgib%2FLfY%2FbPpx8lGgbzxqF31eezznAZDOXQQq9rsiR6L7KvUwiVCfYSbCwev35uUY96PYrYSfN&X-Amz-Signature=d0b3ab5260b1fa1b893fb618597f021a2388b1df22ee325d9888a2d03cc2af02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



