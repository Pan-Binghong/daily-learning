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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMVUUVZQ%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYOXzzkuFHV%2B69SVhpiV5Cs7hsC2VuyDq9X%2BM6JSoaMgIhAMmPZK2kiOA0p24X3QrO5A90jHnrV%2FMukHLK3wmG95vtKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1jofXNXYRiO4gElgq3AOR%2BXtYbeMZLmSlsS%2BWdu8kDzJ9AXrUYK%2BvWN%2FTQd7ltrVVJ6ZTw0zSUoUGn2Yeee08stic5Kog3NWOdqcszpevx7n4TaEr1MVP4pFq%2FwEZWUNMByfcP0vMJIRaFfQ39O3qxULh8IUqlfW1PPkeIX9Hp7Csd4Ylc14TJmUaGlvzXWvP9P6rJKNHdZSYtiR3FipjP7%2BYLgHaKs2xAdM%2FaSB6HuO1sJU5ZmbAmLxiUbJ9mhal5WN5AytkXeTUqKQAkpEw6Fazr%2FRKPKBNeZHcw1CsRxXhSLMZ0fIgnNB3uxwP3A9%2FZjCpA8jr%2FO6yzTlVMwl9yMZN1Je04OVj414xG1i%2Bc%2FgnADs7OIJYTFF4xu7Nfmlen4gF%2BpDi2nrPZmgLKddDrzD27GVf%2F8a%2FC5OYaSgj1JuMHq3pibc619ODelBSbqeFLM51ZzlZPn7x6NSi5MNNqlkosznL%2FPD%2FEQhNDNFbIitGNcXhxQA1uARSDPiipUrZWPn2DTystEmf0J3DVnExw5CNMaJcuF1VubqEPX4ksYlsikwTJU75SXHFvnWmoSNd9b1RTPsAASmKc7EcdZCKO%2FIkBn3KAfk3covtLTP%2BHVfZFUv5cE7VgMvkx4EHTgw1P2gayIUGojGuODCqtrXIBjqkAQlIlRDtjIyOyaB5eyN2FKSNyWeXrMqRSRssTz%2BEwArPMztlYF2eLBP48SHJNlXqloI7Ita0DtH%2BBof%2Fn9b%2FsTgvbugEKZQB9USPS1za6mwIwzDA96hVSdYerj0Wg%2FFZi34798%2FV7QIlJXIbI4AH6TXYVjnLXx9mmxNQp0aT9AqclnQOU9Fdsi2zfII9bSWNKROZlukc4WxDj2xhsC8sM6uND2jq&X-Amz-Signature=73b96bf6dfe8111b1aace258d2e23555c0125eea3663527a5b53f36a382e90ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMVUUVZQ%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYOXzzkuFHV%2B69SVhpiV5Cs7hsC2VuyDq9X%2BM6JSoaMgIhAMmPZK2kiOA0p24X3QrO5A90jHnrV%2FMukHLK3wmG95vtKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1jofXNXYRiO4gElgq3AOR%2BXtYbeMZLmSlsS%2BWdu8kDzJ9AXrUYK%2BvWN%2FTQd7ltrVVJ6ZTw0zSUoUGn2Yeee08stic5Kog3NWOdqcszpevx7n4TaEr1MVP4pFq%2FwEZWUNMByfcP0vMJIRaFfQ39O3qxULh8IUqlfW1PPkeIX9Hp7Csd4Ylc14TJmUaGlvzXWvP9P6rJKNHdZSYtiR3FipjP7%2BYLgHaKs2xAdM%2FaSB6HuO1sJU5ZmbAmLxiUbJ9mhal5WN5AytkXeTUqKQAkpEw6Fazr%2FRKPKBNeZHcw1CsRxXhSLMZ0fIgnNB3uxwP3A9%2FZjCpA8jr%2FO6yzTlVMwl9yMZN1Je04OVj414xG1i%2Bc%2FgnADs7OIJYTFF4xu7Nfmlen4gF%2BpDi2nrPZmgLKddDrzD27GVf%2F8a%2FC5OYaSgj1JuMHq3pibc619ODelBSbqeFLM51ZzlZPn7x6NSi5MNNqlkosznL%2FPD%2FEQhNDNFbIitGNcXhxQA1uARSDPiipUrZWPn2DTystEmf0J3DVnExw5CNMaJcuF1VubqEPX4ksYlsikwTJU75SXHFvnWmoSNd9b1RTPsAASmKc7EcdZCKO%2FIkBn3KAfk3covtLTP%2BHVfZFUv5cE7VgMvkx4EHTgw1P2gayIUGojGuODCqtrXIBjqkAQlIlRDtjIyOyaB5eyN2FKSNyWeXrMqRSRssTz%2BEwArPMztlYF2eLBP48SHJNlXqloI7Ita0DtH%2BBof%2Fn9b%2FsTgvbugEKZQB9USPS1za6mwIwzDA96hVSdYerj0Wg%2FFZi34798%2FV7QIlJXIbI4AH6TXYVjnLXx9mmxNQp0aT9AqclnQOU9Fdsi2zfII9bSWNKROZlukc4WxDj2xhsC8sM6uND2jq&X-Amz-Signature=225e36b0effa4ccebc580ae07fd9745bdc921109e8cce2abc6fd99ddd84fb38f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMVUUVZQ%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYOXzzkuFHV%2B69SVhpiV5Cs7hsC2VuyDq9X%2BM6JSoaMgIhAMmPZK2kiOA0p24X3QrO5A90jHnrV%2FMukHLK3wmG95vtKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1jofXNXYRiO4gElgq3AOR%2BXtYbeMZLmSlsS%2BWdu8kDzJ9AXrUYK%2BvWN%2FTQd7ltrVVJ6ZTw0zSUoUGn2Yeee08stic5Kog3NWOdqcszpevx7n4TaEr1MVP4pFq%2FwEZWUNMByfcP0vMJIRaFfQ39O3qxULh8IUqlfW1PPkeIX9Hp7Csd4Ylc14TJmUaGlvzXWvP9P6rJKNHdZSYtiR3FipjP7%2BYLgHaKs2xAdM%2FaSB6HuO1sJU5ZmbAmLxiUbJ9mhal5WN5AytkXeTUqKQAkpEw6Fazr%2FRKPKBNeZHcw1CsRxXhSLMZ0fIgnNB3uxwP3A9%2FZjCpA8jr%2FO6yzTlVMwl9yMZN1Je04OVj414xG1i%2Bc%2FgnADs7OIJYTFF4xu7Nfmlen4gF%2BpDi2nrPZmgLKddDrzD27GVf%2F8a%2FC5OYaSgj1JuMHq3pibc619ODelBSbqeFLM51ZzlZPn7x6NSi5MNNqlkosznL%2FPD%2FEQhNDNFbIitGNcXhxQA1uARSDPiipUrZWPn2DTystEmf0J3DVnExw5CNMaJcuF1VubqEPX4ksYlsikwTJU75SXHFvnWmoSNd9b1RTPsAASmKc7EcdZCKO%2FIkBn3KAfk3covtLTP%2BHVfZFUv5cE7VgMvkx4EHTgw1P2gayIUGojGuODCqtrXIBjqkAQlIlRDtjIyOyaB5eyN2FKSNyWeXrMqRSRssTz%2BEwArPMztlYF2eLBP48SHJNlXqloI7Ita0DtH%2BBof%2Fn9b%2FsTgvbugEKZQB9USPS1za6mwIwzDA96hVSdYerj0Wg%2FFZi34798%2FV7QIlJXIbI4AH6TXYVjnLXx9mmxNQp0aT9AqclnQOU9Fdsi2zfII9bSWNKROZlukc4WxDj2xhsC8sM6uND2jq&X-Amz-Signature=08680ff1f5c14bf3b285933a1e275561a70e699d78fb13e3d131c6590440e0a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMVUUVZQ%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYOXzzkuFHV%2B69SVhpiV5Cs7hsC2VuyDq9X%2BM6JSoaMgIhAMmPZK2kiOA0p24X3QrO5A90jHnrV%2FMukHLK3wmG95vtKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy1jofXNXYRiO4gElgq3AOR%2BXtYbeMZLmSlsS%2BWdu8kDzJ9AXrUYK%2BvWN%2FTQd7ltrVVJ6ZTw0zSUoUGn2Yeee08stic5Kog3NWOdqcszpevx7n4TaEr1MVP4pFq%2FwEZWUNMByfcP0vMJIRaFfQ39O3qxULh8IUqlfW1PPkeIX9Hp7Csd4Ylc14TJmUaGlvzXWvP9P6rJKNHdZSYtiR3FipjP7%2BYLgHaKs2xAdM%2FaSB6HuO1sJU5ZmbAmLxiUbJ9mhal5WN5AytkXeTUqKQAkpEw6Fazr%2FRKPKBNeZHcw1CsRxXhSLMZ0fIgnNB3uxwP3A9%2FZjCpA8jr%2FO6yzTlVMwl9yMZN1Je04OVj414xG1i%2Bc%2FgnADs7OIJYTFF4xu7Nfmlen4gF%2BpDi2nrPZmgLKddDrzD27GVf%2F8a%2FC5OYaSgj1JuMHq3pibc619ODelBSbqeFLM51ZzlZPn7x6NSi5MNNqlkosznL%2FPD%2FEQhNDNFbIitGNcXhxQA1uARSDPiipUrZWPn2DTystEmf0J3DVnExw5CNMaJcuF1VubqEPX4ksYlsikwTJU75SXHFvnWmoSNd9b1RTPsAASmKc7EcdZCKO%2FIkBn3KAfk3covtLTP%2BHVfZFUv5cE7VgMvkx4EHTgw1P2gayIUGojGuODCqtrXIBjqkAQlIlRDtjIyOyaB5eyN2FKSNyWeXrMqRSRssTz%2BEwArPMztlYF2eLBP48SHJNlXqloI7Ita0DtH%2BBof%2Fn9b%2FsTgvbugEKZQB9USPS1za6mwIwzDA96hVSdYerj0Wg%2FFZi34798%2FV7QIlJXIbI4AH6TXYVjnLXx9mmxNQp0aT9AqclnQOU9Fdsi2zfII9bSWNKROZlukc4WxDj2xhsC8sM6uND2jq&X-Amz-Signature=d5162dca93863ce7fc043a7734399f4fd9433a94c576d9a68ae62731d4408b0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



