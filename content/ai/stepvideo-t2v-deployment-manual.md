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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A7LREEB%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIFN4Jh0lydZgtr0MMzqhaTP4C7iwIEigJHdgG6tuwS%2FIAiBAISTPQDa4lGSuQ%2FQqx09Z9PlrX4oFnOFAPF9UT9H5ySr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMqMCERec41iyhPoEsKtwDNBeF%2FDE6iaebTyAZM%2FQRJL8ZQxms6pflzOMqr1UilIooQ4rnnMCiNuo0DGVe3hZ%2BGXbGphmr3lgM09wqAO0GWwgng%2B4OzVgk6hPJk9Q7f7lEwqKtWlMAePvC%2B5OQuP7MA%2B7e3BpSn6I1PpQYvOxHxtote8Jbak5EkYPzaiMT85BhbkFlhHzkM7giGow87axc2oVk80Cci9lHHxlGh%2F7JUkf%2BVxtpC7d5BVr6orINCLMV4sJ5IRP81is8X9rywE4GK46d2FGuow5nnrBybgB74jAwlBhItIUmiFYDdQgWp%2BUtC6dL8BtVV0yn14fJIpwdbYM7gwuUTGxMfD%2BYpr1uLndZ5MZpUJCQhgcCFztQ4evz6qSCtZKd8PUrv9ZcJXEHKgNSFz8qdGdj%2BQd3F1fut94vP1eTEkzbu9TETZ%2FHpyY11smfKOaH%2Bi2aRCeQn%2F8ORe%2FLEBDEP26nFoZdLXkbZWm2xb2VfmlMF9EIGbtmysXzKrqkLmMO5VohTMHW2hOQ0e2VGJMPnHwJYKYSfyF%2FMDMAfc69W7T7X%2Bzn%2BpVOgqm01cR2C460ydtdGyyswGniEY9rVhLzdu%2FH3irxhRqZVYs0FUSSPtOeHWB5dQL6wTz3VEYe7nq930VOfagw4pPKzAY6pgGO0gOw1P94eQlbY9tsqfkrAMdCQuD3p4dfyAglc6W6rMTMj1AQqNskc2y9knhHsiaHQPAkF56sJWhMkSUYGKfDtmhWwf%2Fjyz6xgzQ0%2BxyMpMYTqh7gWJLKCnYjIO%2FaS8y9Szubcdlbrmq1dENBFAxMnnr99kh%2B%2BrYV%2F0u4wKjZpmfWKNK5u9ae5h7L8mZVKaG9SMLDjCtNTzpj2qGpJ3XAG2XmjsxI&X-Amz-Signature=90c430a72ee884736b0772a799b545b843ad20ab166890f4c5d3579ead5374e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A7LREEB%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIFN4Jh0lydZgtr0MMzqhaTP4C7iwIEigJHdgG6tuwS%2FIAiBAISTPQDa4lGSuQ%2FQqx09Z9PlrX4oFnOFAPF9UT9H5ySr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMqMCERec41iyhPoEsKtwDNBeF%2FDE6iaebTyAZM%2FQRJL8ZQxms6pflzOMqr1UilIooQ4rnnMCiNuo0DGVe3hZ%2BGXbGphmr3lgM09wqAO0GWwgng%2B4OzVgk6hPJk9Q7f7lEwqKtWlMAePvC%2B5OQuP7MA%2B7e3BpSn6I1PpQYvOxHxtote8Jbak5EkYPzaiMT85BhbkFlhHzkM7giGow87axc2oVk80Cci9lHHxlGh%2F7JUkf%2BVxtpC7d5BVr6orINCLMV4sJ5IRP81is8X9rywE4GK46d2FGuow5nnrBybgB74jAwlBhItIUmiFYDdQgWp%2BUtC6dL8BtVV0yn14fJIpwdbYM7gwuUTGxMfD%2BYpr1uLndZ5MZpUJCQhgcCFztQ4evz6qSCtZKd8PUrv9ZcJXEHKgNSFz8qdGdj%2BQd3F1fut94vP1eTEkzbu9TETZ%2FHpyY11smfKOaH%2Bi2aRCeQn%2F8ORe%2FLEBDEP26nFoZdLXkbZWm2xb2VfmlMF9EIGbtmysXzKrqkLmMO5VohTMHW2hOQ0e2VGJMPnHwJYKYSfyF%2FMDMAfc69W7T7X%2Bzn%2BpVOgqm01cR2C460ydtdGyyswGniEY9rVhLzdu%2FH3irxhRqZVYs0FUSSPtOeHWB5dQL6wTz3VEYe7nq930VOfagw4pPKzAY6pgGO0gOw1P94eQlbY9tsqfkrAMdCQuD3p4dfyAglc6W6rMTMj1AQqNskc2y9knhHsiaHQPAkF56sJWhMkSUYGKfDtmhWwf%2Fjyz6xgzQ0%2BxyMpMYTqh7gWJLKCnYjIO%2FaS8y9Szubcdlbrmq1dENBFAxMnnr99kh%2B%2BrYV%2F0u4wKjZpmfWKNK5u9ae5h7L8mZVKaG9SMLDjCtNTzpj2qGpJ3XAG2XmjsxI&X-Amz-Signature=ad24d1ea7756bd8f9a37b220614d362171db14b8fbf8e2133a96f11d3a0f952d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A7LREEB%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIFN4Jh0lydZgtr0MMzqhaTP4C7iwIEigJHdgG6tuwS%2FIAiBAISTPQDa4lGSuQ%2FQqx09Z9PlrX4oFnOFAPF9UT9H5ySr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMqMCERec41iyhPoEsKtwDNBeF%2FDE6iaebTyAZM%2FQRJL8ZQxms6pflzOMqr1UilIooQ4rnnMCiNuo0DGVe3hZ%2BGXbGphmr3lgM09wqAO0GWwgng%2B4OzVgk6hPJk9Q7f7lEwqKtWlMAePvC%2B5OQuP7MA%2B7e3BpSn6I1PpQYvOxHxtote8Jbak5EkYPzaiMT85BhbkFlhHzkM7giGow87axc2oVk80Cci9lHHxlGh%2F7JUkf%2BVxtpC7d5BVr6orINCLMV4sJ5IRP81is8X9rywE4GK46d2FGuow5nnrBybgB74jAwlBhItIUmiFYDdQgWp%2BUtC6dL8BtVV0yn14fJIpwdbYM7gwuUTGxMfD%2BYpr1uLndZ5MZpUJCQhgcCFztQ4evz6qSCtZKd8PUrv9ZcJXEHKgNSFz8qdGdj%2BQd3F1fut94vP1eTEkzbu9TETZ%2FHpyY11smfKOaH%2Bi2aRCeQn%2F8ORe%2FLEBDEP26nFoZdLXkbZWm2xb2VfmlMF9EIGbtmysXzKrqkLmMO5VohTMHW2hOQ0e2VGJMPnHwJYKYSfyF%2FMDMAfc69W7T7X%2Bzn%2BpVOgqm01cR2C460ydtdGyyswGniEY9rVhLzdu%2FH3irxhRqZVYs0FUSSPtOeHWB5dQL6wTz3VEYe7nq930VOfagw4pPKzAY6pgGO0gOw1P94eQlbY9tsqfkrAMdCQuD3p4dfyAglc6W6rMTMj1AQqNskc2y9knhHsiaHQPAkF56sJWhMkSUYGKfDtmhWwf%2Fjyz6xgzQ0%2BxyMpMYTqh7gWJLKCnYjIO%2FaS8y9Szubcdlbrmq1dENBFAxMnnr99kh%2B%2BrYV%2F0u4wKjZpmfWKNK5u9ae5h7L8mZVKaG9SMLDjCtNTzpj2qGpJ3XAG2XmjsxI&X-Amz-Signature=3fff1003312ce0e36bbf7fe50c65f402e7f9de58d088a28773c73c52278ba3c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A7LREEB%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIFN4Jh0lydZgtr0MMzqhaTP4C7iwIEigJHdgG6tuwS%2FIAiBAISTPQDa4lGSuQ%2FQqx09Z9PlrX4oFnOFAPF9UT9H5ySr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMqMCERec41iyhPoEsKtwDNBeF%2FDE6iaebTyAZM%2FQRJL8ZQxms6pflzOMqr1UilIooQ4rnnMCiNuo0DGVe3hZ%2BGXbGphmr3lgM09wqAO0GWwgng%2B4OzVgk6hPJk9Q7f7lEwqKtWlMAePvC%2B5OQuP7MA%2B7e3BpSn6I1PpQYvOxHxtote8Jbak5EkYPzaiMT85BhbkFlhHzkM7giGow87axc2oVk80Cci9lHHxlGh%2F7JUkf%2BVxtpC7d5BVr6orINCLMV4sJ5IRP81is8X9rywE4GK46d2FGuow5nnrBybgB74jAwlBhItIUmiFYDdQgWp%2BUtC6dL8BtVV0yn14fJIpwdbYM7gwuUTGxMfD%2BYpr1uLndZ5MZpUJCQhgcCFztQ4evz6qSCtZKd8PUrv9ZcJXEHKgNSFz8qdGdj%2BQd3F1fut94vP1eTEkzbu9TETZ%2FHpyY11smfKOaH%2Bi2aRCeQn%2F8ORe%2FLEBDEP26nFoZdLXkbZWm2xb2VfmlMF9EIGbtmysXzKrqkLmMO5VohTMHW2hOQ0e2VGJMPnHwJYKYSfyF%2FMDMAfc69W7T7X%2Bzn%2BpVOgqm01cR2C460ydtdGyyswGniEY9rVhLzdu%2FH3irxhRqZVYs0FUSSPtOeHWB5dQL6wTz3VEYe7nq930VOfagw4pPKzAY6pgGO0gOw1P94eQlbY9tsqfkrAMdCQuD3p4dfyAglc6W6rMTMj1AQqNskc2y9knhHsiaHQPAkF56sJWhMkSUYGKfDtmhWwf%2Fjyz6xgzQ0%2BxyMpMYTqh7gWJLKCnYjIO%2FaS8y9Szubcdlbrmq1dENBFAxMnnr99kh%2B%2BrYV%2F0u4wKjZpmfWKNK5u9ae5h7L8mZVKaG9SMLDjCtNTzpj2qGpJ3XAG2XmjsxI&X-Amz-Signature=a2482a23d70c5e3aaebaf1e5b25f1e203388b742e125cc12f2fb1524abe133e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



