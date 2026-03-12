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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBWUEL2L%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcFhVedH4HVjgkUPL1wF0xFD2ThcJA5UePJOxYsYKL6wIgDanopVjFePq18KRMxEBuXUg46T6yKXEeMyVwo%2Bg6dM8q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDDUozIOD9%2Fp7rpOdJyrcAzRWqXZvd3C4tcMp1mEANUdR%2F2Hd6%2BVGplg6%2BJlww5gyV41deUCcjEIL000dKoeuGT4TEFnJO3Ji%2FFKvsg%2Fe%2F1mekIwaKeX9oSlRo6ju5VjpwkWsb13VFOPXGqv%2Bv53zg404FyOok71tvQzzlZW5yqy2mX7PSZz6oatR9nGQ1PLXZXE8uQ48PzvCHWVjuVFAzg%2F2keNbuibNKHKc5MwimHwD%2B1A1BqIaEhmh8jMUIc%2F6c52tG7K%2F6S9Z4ZN%2F5WTYmAfG4tDIpER3nk6dAtszupV0yd4mgxOJvqhF%2Bs3Gns5WhyHwNXa1zOZz9zrRdMunjRT5DcbvQPVJ4FN0mC8%2BNRRlJJ%2FBVlxE%2FJOP%2BRH3TLQ3X3VBJNupnpyYnYp4UexQAX8TvdfI3SbEVlL7OJpxCB5dntsUmRc%2BGD%2BQ3e4aOyxNyFS3v5qDGY7hrCDL8vrRiV8pgpZxDXfd5%2BuCBSSdLFW%2FKg3fDhNoTotPVfrLwj6BiY2%2BTsiCFxW%2BGmvF4eVI97A2%2FKMxI1IRsr6ARgz1QAK3GgCSFwBKkNzlC2ZdNVrsTKO4c8HQFX29vXGWY13LNJWIsqzZkiVulSyBnUP%2FOejvqKeJ66obx322lmE0tPc%2FiKA4zbYrYAEQyGa3MP2xyM0GOqUBBt%2F5nfgj96vOjz5HDrW15NQrj4W%2B1Cb%2BYptiyhsetJ88ZgtnOGdioDnHJeKqymXXNM3dzVQvrwiCbK9zxarHS96iOM%2BSKDd4IokRAtSy54jUzJ225NUAsduvQ7STKq64OhoahqBnId0Ac9pTEr6kzyIlOEQkTigAxyy7c6zcxA3Albhzt4btEaQO8slNZu7Q0fypXwKks7%2BvKJ6tDEi925H8Eoa7&X-Amz-Signature=46dc97a6ec3edf04be82686ddd5da47cbb82691770b00ceb4abcbc6f22d3d8b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBWUEL2L%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcFhVedH4HVjgkUPL1wF0xFD2ThcJA5UePJOxYsYKL6wIgDanopVjFePq18KRMxEBuXUg46T6yKXEeMyVwo%2Bg6dM8q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDDUozIOD9%2Fp7rpOdJyrcAzRWqXZvd3C4tcMp1mEANUdR%2F2Hd6%2BVGplg6%2BJlww5gyV41deUCcjEIL000dKoeuGT4TEFnJO3Ji%2FFKvsg%2Fe%2F1mekIwaKeX9oSlRo6ju5VjpwkWsb13VFOPXGqv%2Bv53zg404FyOok71tvQzzlZW5yqy2mX7PSZz6oatR9nGQ1PLXZXE8uQ48PzvCHWVjuVFAzg%2F2keNbuibNKHKc5MwimHwD%2B1A1BqIaEhmh8jMUIc%2F6c52tG7K%2F6S9Z4ZN%2F5WTYmAfG4tDIpER3nk6dAtszupV0yd4mgxOJvqhF%2Bs3Gns5WhyHwNXa1zOZz9zrRdMunjRT5DcbvQPVJ4FN0mC8%2BNRRlJJ%2FBVlxE%2FJOP%2BRH3TLQ3X3VBJNupnpyYnYp4UexQAX8TvdfI3SbEVlL7OJpxCB5dntsUmRc%2BGD%2BQ3e4aOyxNyFS3v5qDGY7hrCDL8vrRiV8pgpZxDXfd5%2BuCBSSdLFW%2FKg3fDhNoTotPVfrLwj6BiY2%2BTsiCFxW%2BGmvF4eVI97A2%2FKMxI1IRsr6ARgz1QAK3GgCSFwBKkNzlC2ZdNVrsTKO4c8HQFX29vXGWY13LNJWIsqzZkiVulSyBnUP%2FOejvqKeJ66obx322lmE0tPc%2FiKA4zbYrYAEQyGa3MP2xyM0GOqUBBt%2F5nfgj96vOjz5HDrW15NQrj4W%2B1Cb%2BYptiyhsetJ88ZgtnOGdioDnHJeKqymXXNM3dzVQvrwiCbK9zxarHS96iOM%2BSKDd4IokRAtSy54jUzJ225NUAsduvQ7STKq64OhoahqBnId0Ac9pTEr6kzyIlOEQkTigAxyy7c6zcxA3Albhzt4btEaQO8slNZu7Q0fypXwKks7%2BvKJ6tDEi925H8Eoa7&X-Amz-Signature=34d674d3f3fb96444f53d0eab00aee4341a85cfe8943da1ebeb5610ef3a0db67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBWUEL2L%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcFhVedH4HVjgkUPL1wF0xFD2ThcJA5UePJOxYsYKL6wIgDanopVjFePq18KRMxEBuXUg46T6yKXEeMyVwo%2Bg6dM8q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDDUozIOD9%2Fp7rpOdJyrcAzRWqXZvd3C4tcMp1mEANUdR%2F2Hd6%2BVGplg6%2BJlww5gyV41deUCcjEIL000dKoeuGT4TEFnJO3Ji%2FFKvsg%2Fe%2F1mekIwaKeX9oSlRo6ju5VjpwkWsb13VFOPXGqv%2Bv53zg404FyOok71tvQzzlZW5yqy2mX7PSZz6oatR9nGQ1PLXZXE8uQ48PzvCHWVjuVFAzg%2F2keNbuibNKHKc5MwimHwD%2B1A1BqIaEhmh8jMUIc%2F6c52tG7K%2F6S9Z4ZN%2F5WTYmAfG4tDIpER3nk6dAtszupV0yd4mgxOJvqhF%2Bs3Gns5WhyHwNXa1zOZz9zrRdMunjRT5DcbvQPVJ4FN0mC8%2BNRRlJJ%2FBVlxE%2FJOP%2BRH3TLQ3X3VBJNupnpyYnYp4UexQAX8TvdfI3SbEVlL7OJpxCB5dntsUmRc%2BGD%2BQ3e4aOyxNyFS3v5qDGY7hrCDL8vrRiV8pgpZxDXfd5%2BuCBSSdLFW%2FKg3fDhNoTotPVfrLwj6BiY2%2BTsiCFxW%2BGmvF4eVI97A2%2FKMxI1IRsr6ARgz1QAK3GgCSFwBKkNzlC2ZdNVrsTKO4c8HQFX29vXGWY13LNJWIsqzZkiVulSyBnUP%2FOejvqKeJ66obx322lmE0tPc%2FiKA4zbYrYAEQyGa3MP2xyM0GOqUBBt%2F5nfgj96vOjz5HDrW15NQrj4W%2B1Cb%2BYptiyhsetJ88ZgtnOGdioDnHJeKqymXXNM3dzVQvrwiCbK9zxarHS96iOM%2BSKDd4IokRAtSy54jUzJ225NUAsduvQ7STKq64OhoahqBnId0Ac9pTEr6kzyIlOEQkTigAxyy7c6zcxA3Albhzt4btEaQO8slNZu7Q0fypXwKks7%2BvKJ6tDEi925H8Eoa7&X-Amz-Signature=5978add5f56170b8d6d729d7f8664875bd66d8689acb8ad2359e3307885c092d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBWUEL2L%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcFhVedH4HVjgkUPL1wF0xFD2ThcJA5UePJOxYsYKL6wIgDanopVjFePq18KRMxEBuXUg46T6yKXEeMyVwo%2Bg6dM8q%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDDUozIOD9%2Fp7rpOdJyrcAzRWqXZvd3C4tcMp1mEANUdR%2F2Hd6%2BVGplg6%2BJlww5gyV41deUCcjEIL000dKoeuGT4TEFnJO3Ji%2FFKvsg%2Fe%2F1mekIwaKeX9oSlRo6ju5VjpwkWsb13VFOPXGqv%2Bv53zg404FyOok71tvQzzlZW5yqy2mX7PSZz6oatR9nGQ1PLXZXE8uQ48PzvCHWVjuVFAzg%2F2keNbuibNKHKc5MwimHwD%2B1A1BqIaEhmh8jMUIc%2F6c52tG7K%2F6S9Z4ZN%2F5WTYmAfG4tDIpER3nk6dAtszupV0yd4mgxOJvqhF%2Bs3Gns5WhyHwNXa1zOZz9zrRdMunjRT5DcbvQPVJ4FN0mC8%2BNRRlJJ%2FBVlxE%2FJOP%2BRH3TLQ3X3VBJNupnpyYnYp4UexQAX8TvdfI3SbEVlL7OJpxCB5dntsUmRc%2BGD%2BQ3e4aOyxNyFS3v5qDGY7hrCDL8vrRiV8pgpZxDXfd5%2BuCBSSdLFW%2FKg3fDhNoTotPVfrLwj6BiY2%2BTsiCFxW%2BGmvF4eVI97A2%2FKMxI1IRsr6ARgz1QAK3GgCSFwBKkNzlC2ZdNVrsTKO4c8HQFX29vXGWY13LNJWIsqzZkiVulSyBnUP%2FOejvqKeJ66obx322lmE0tPc%2FiKA4zbYrYAEQyGa3MP2xyM0GOqUBBt%2F5nfgj96vOjz5HDrW15NQrj4W%2B1Cb%2BYptiyhsetJ88ZgtnOGdioDnHJeKqymXXNM3dzVQvrwiCbK9zxarHS96iOM%2BSKDd4IokRAtSy54jUzJ225NUAsduvQ7STKq64OhoahqBnId0Ac9pTEr6kzyIlOEQkTigAxyy7c6zcxA3Albhzt4btEaQO8slNZu7Q0fypXwKks7%2BvKJ6tDEi925H8Eoa7&X-Amz-Signature=ecf1669196ea73379f3f791509dcc0e9f780cba7cbe501e34b3244b4575d9d5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



