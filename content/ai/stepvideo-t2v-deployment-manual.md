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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V62H5BX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRL6QY1NtCVHEgg7jpHUa3hihLfYMLNCJ9yOsIODmKAAiB1HW7mMYA%2FxNj%2Fq6HX%2BoJc4wHaDyfj3Ur6wlRVky1GUCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2BhCZyy31ug8EQk6KtwDaY9DtrMItZivePFT%2B3hUf4cOVcoqOCImCCqUcyqAdgu4JmEoO1M7995L2afxtaFyNLRPBMTzcl0EdZ38nbEIOzyprWsyS2c8uIFGZMyWV9RSLO5lWzhCl0QV8N4PB0dyQEeLTH4i%2F%2BTjYvna3xhp%2FMgyvkyngstfMt6SnWgwAVLxnPrANp0kviMj1PxknNx9ySrqwkOg%2Bc%2BNJvSwVVa5wKxRiUKIHdrJZu5puXi3lnv8e2xmF1%2BtjZrhXT6gXPePlNL2jmotc6IRAaMV9qsLfuRPK%2FXS90Xo3zkkkIEOZBZtO3ztmscJyqtS6THz4dChNOHQvnVv2HmD2zgT6aAvuU04FBHx2r%2FXFJyIwV4huCWWJMJ5hkeSOGEn4rmPOKGUE4LYgZGdy9em9%2F9bDVPFDVupzeaQlQTRpCSTLswdAjB%2Fa61tKlekG6nV6lfUx82sq3yNMfQuDO0xGIwrf0%2BqApOedl63UkEDJKn6Lk7Ml99pKk2jxtiSLFqXSVnSggATFUh7lyPHj1BPEQRyIKxpqOf8K0IJtkVSr6bskLafLsbmbPSbsvnZu20hfcqPT0%2BHTzx9QVmTjncXDgz9t8uCQw%2B0jq36imD9sJVL%2BTv8qE1pN1oviqj4M3%2F%2F7A8wjuKSygY6pgHVpHlJP4blbVY5twObyuXgtnFrK8kkYtTEGgfZg82GK7Gfmdv7w0Q6wUi9rwshq2qH96vWrnyQY20mmlt0PHZ%2Bm2F0MyTPd8CC9ZCjlRc2PfYOe0t8RPJ3wpyCpN%2Fqlqag5H77f9V3HuFGzLLPjVGjTHAQa3NJKQ5NL%2B1HBmU0krkBZK%2FMlppys6Aq%2BkxiHrQ030jAecvgfR2InS4kmzgwCejSSuLB&X-Amz-Signature=036ec54634084f81858c6b4c847146689d2dd998203c458fc46e812afd4b2f77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V62H5BX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRL6QY1NtCVHEgg7jpHUa3hihLfYMLNCJ9yOsIODmKAAiB1HW7mMYA%2FxNj%2Fq6HX%2BoJc4wHaDyfj3Ur6wlRVky1GUCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2BhCZyy31ug8EQk6KtwDaY9DtrMItZivePFT%2B3hUf4cOVcoqOCImCCqUcyqAdgu4JmEoO1M7995L2afxtaFyNLRPBMTzcl0EdZ38nbEIOzyprWsyS2c8uIFGZMyWV9RSLO5lWzhCl0QV8N4PB0dyQEeLTH4i%2F%2BTjYvna3xhp%2FMgyvkyngstfMt6SnWgwAVLxnPrANp0kviMj1PxknNx9ySrqwkOg%2Bc%2BNJvSwVVa5wKxRiUKIHdrJZu5puXi3lnv8e2xmF1%2BtjZrhXT6gXPePlNL2jmotc6IRAaMV9qsLfuRPK%2FXS90Xo3zkkkIEOZBZtO3ztmscJyqtS6THz4dChNOHQvnVv2HmD2zgT6aAvuU04FBHx2r%2FXFJyIwV4huCWWJMJ5hkeSOGEn4rmPOKGUE4LYgZGdy9em9%2F9bDVPFDVupzeaQlQTRpCSTLswdAjB%2Fa61tKlekG6nV6lfUx82sq3yNMfQuDO0xGIwrf0%2BqApOedl63UkEDJKn6Lk7Ml99pKk2jxtiSLFqXSVnSggATFUh7lyPHj1BPEQRyIKxpqOf8K0IJtkVSr6bskLafLsbmbPSbsvnZu20hfcqPT0%2BHTzx9QVmTjncXDgz9t8uCQw%2B0jq36imD9sJVL%2BTv8qE1pN1oviqj4M3%2F%2F7A8wjuKSygY6pgHVpHlJP4blbVY5twObyuXgtnFrK8kkYtTEGgfZg82GK7Gfmdv7w0Q6wUi9rwshq2qH96vWrnyQY20mmlt0PHZ%2Bm2F0MyTPd8CC9ZCjlRc2PfYOe0t8RPJ3wpyCpN%2Fqlqag5H77f9V3HuFGzLLPjVGjTHAQa3NJKQ5NL%2B1HBmU0krkBZK%2FMlppys6Aq%2BkxiHrQ030jAecvgfR2InS4kmzgwCejSSuLB&X-Amz-Signature=2bde74953e2b374d9a5b4adbb12446c563a4d6228884dcf6983a26c6cad1d8eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V62H5BX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRL6QY1NtCVHEgg7jpHUa3hihLfYMLNCJ9yOsIODmKAAiB1HW7mMYA%2FxNj%2Fq6HX%2BoJc4wHaDyfj3Ur6wlRVky1GUCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2BhCZyy31ug8EQk6KtwDaY9DtrMItZivePFT%2B3hUf4cOVcoqOCImCCqUcyqAdgu4JmEoO1M7995L2afxtaFyNLRPBMTzcl0EdZ38nbEIOzyprWsyS2c8uIFGZMyWV9RSLO5lWzhCl0QV8N4PB0dyQEeLTH4i%2F%2BTjYvna3xhp%2FMgyvkyngstfMt6SnWgwAVLxnPrANp0kviMj1PxknNx9ySrqwkOg%2Bc%2BNJvSwVVa5wKxRiUKIHdrJZu5puXi3lnv8e2xmF1%2BtjZrhXT6gXPePlNL2jmotc6IRAaMV9qsLfuRPK%2FXS90Xo3zkkkIEOZBZtO3ztmscJyqtS6THz4dChNOHQvnVv2HmD2zgT6aAvuU04FBHx2r%2FXFJyIwV4huCWWJMJ5hkeSOGEn4rmPOKGUE4LYgZGdy9em9%2F9bDVPFDVupzeaQlQTRpCSTLswdAjB%2Fa61tKlekG6nV6lfUx82sq3yNMfQuDO0xGIwrf0%2BqApOedl63UkEDJKn6Lk7Ml99pKk2jxtiSLFqXSVnSggATFUh7lyPHj1BPEQRyIKxpqOf8K0IJtkVSr6bskLafLsbmbPSbsvnZu20hfcqPT0%2BHTzx9QVmTjncXDgz9t8uCQw%2B0jq36imD9sJVL%2BTv8qE1pN1oviqj4M3%2F%2F7A8wjuKSygY6pgHVpHlJP4blbVY5twObyuXgtnFrK8kkYtTEGgfZg82GK7Gfmdv7w0Q6wUi9rwshq2qH96vWrnyQY20mmlt0PHZ%2Bm2F0MyTPd8CC9ZCjlRc2PfYOe0t8RPJ3wpyCpN%2Fqlqag5H77f9V3HuFGzLLPjVGjTHAQa3NJKQ5NL%2B1HBmU0krkBZK%2FMlppys6Aq%2BkxiHrQ030jAecvgfR2InS4kmzgwCejSSuLB&X-Amz-Signature=97f5a94ca388c98abe7a9ac37f9da5fbaf89aad16f0c5d881e6d9420f8c35251&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V62H5BX%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRL6QY1NtCVHEgg7jpHUa3hihLfYMLNCJ9yOsIODmKAAiB1HW7mMYA%2FxNj%2Fq6HX%2BoJc4wHaDyfj3Ur6wlRVky1GUCqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV%2BhCZyy31ug8EQk6KtwDaY9DtrMItZivePFT%2B3hUf4cOVcoqOCImCCqUcyqAdgu4JmEoO1M7995L2afxtaFyNLRPBMTzcl0EdZ38nbEIOzyprWsyS2c8uIFGZMyWV9RSLO5lWzhCl0QV8N4PB0dyQEeLTH4i%2F%2BTjYvna3xhp%2FMgyvkyngstfMt6SnWgwAVLxnPrANp0kviMj1PxknNx9ySrqwkOg%2Bc%2BNJvSwVVa5wKxRiUKIHdrJZu5puXi3lnv8e2xmF1%2BtjZrhXT6gXPePlNL2jmotc6IRAaMV9qsLfuRPK%2FXS90Xo3zkkkIEOZBZtO3ztmscJyqtS6THz4dChNOHQvnVv2HmD2zgT6aAvuU04FBHx2r%2FXFJyIwV4huCWWJMJ5hkeSOGEn4rmPOKGUE4LYgZGdy9em9%2F9bDVPFDVupzeaQlQTRpCSTLswdAjB%2Fa61tKlekG6nV6lfUx82sq3yNMfQuDO0xGIwrf0%2BqApOedl63UkEDJKn6Lk7Ml99pKk2jxtiSLFqXSVnSggATFUh7lyPHj1BPEQRyIKxpqOf8K0IJtkVSr6bskLafLsbmbPSbsvnZu20hfcqPT0%2BHTzx9QVmTjncXDgz9t8uCQw%2B0jq36imD9sJVL%2BTv8qE1pN1oviqj4M3%2F%2F7A8wjuKSygY6pgHVpHlJP4blbVY5twObyuXgtnFrK8kkYtTEGgfZg82GK7Gfmdv7w0Q6wUi9rwshq2qH96vWrnyQY20mmlt0PHZ%2Bm2F0MyTPd8CC9ZCjlRc2PfYOe0t8RPJ3wpyCpN%2Fqlqag5H77f9V3HuFGzLLPjVGjTHAQa3NJKQ5NL%2B1HBmU0krkBZK%2FMlppys6Aq%2BkxiHrQ030jAecvgfR2InS4kmzgwCejSSuLB&X-Amz-Signature=0024f4feb5d7453ace00985bb9373abce0231a52c878b4477c6e658e624bc874&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



