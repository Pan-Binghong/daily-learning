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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBC3YZN3%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCID2IXTJINiN6%2Blk0jzqYylHXCc0hv0hojvipxYZnsmJ9AiABRuIV0FW1XBSDD2mB8rAUPIhyc8RO41X%2BuuWBQ6xcyCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMY7FZ%2BxFMpSFCR4zWKtwDAAjVRlfgKh3YyIgrxw9of5RW2MCsXjLk7spiLxLymfXgkxCL%2BMhit5hzfXddSDVj97I8nSKh7Pk%2Bk2Ni%2Fp8LENXORtIispkg%2BvZ1ThavhoirXIzYQYhGMws4Xq1ul95pAyxKq2Hu%2FNrqcdAKO83RKsihBx8%2ByH0q%2BjEEOoLkr6ojhR4h4iqZjCt%2BKHmqqEYFu8Bm4Bcl6xcc2DZBmuhR4GErPWzHbUdrpsIiW4bcOIZXumL7In7LOCt7b1nM4Av%2BK7IOtDo0t%2BJGTSj0X2sY1ORCBrYo1IMKGKGPy8YrB6j%2BjID5XcPX3Zcz4YmFkFFPYAPphTPjKmkttK6gJGYgDC6ayzexCCa6JMMBgNjY8HoMFkcjiYVRkeWiZX7NpevS1lJR6evIVAGnaCHHqJdYXPaOZCanBJCPw%2BsPV2mmeDZkBmxiVAwMohLeHhXxu8LThu4JNbS4PpKoZdrKDi1za82xbR7S1zZgd6vYV6vQrZSY9ODtoAL3Jcg7YBFP7lJTHmDhZi%2FTEhtE6YRzYnjbGfOmjttIAmX9RoDsTl01jeRPvsPO0HSsXahSy2XmOUtLb5OCRZP4IdNBTIzO0n%2FaAThpOmAaqONe%2F5AFfj%2BGvbDsQsp62fW37rNdom8w%2FpKQzAY6pgGg9Hcpc8%2F4htN1rfJ5WybGg67e2bxdrqPd1bvoImlkXg3hotaJ0wBkacrShZzod5Hev6l8WtXndehkdUx7k4zNoK7RDE2s53%2F3HxvZ5qQV6ffEUgRMQK2FYDoARe4KseFuUJ53P61eB2%2BJ5bopuzeCbx1InWW54wiIukD%2FD3ix0CfC%2FeD8ID7Z32TR6uyXvgyOIMMlU%2BzMTLSi2w35%2BFpTGq7D%2FBt%2B&X-Amz-Signature=67c99b51471e5089a7e974bb1ce0543d0c0a332a058c246eff21b2f945d2eae5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBC3YZN3%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCID2IXTJINiN6%2Blk0jzqYylHXCc0hv0hojvipxYZnsmJ9AiABRuIV0FW1XBSDD2mB8rAUPIhyc8RO41X%2BuuWBQ6xcyCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMY7FZ%2BxFMpSFCR4zWKtwDAAjVRlfgKh3YyIgrxw9of5RW2MCsXjLk7spiLxLymfXgkxCL%2BMhit5hzfXddSDVj97I8nSKh7Pk%2Bk2Ni%2Fp8LENXORtIispkg%2BvZ1ThavhoirXIzYQYhGMws4Xq1ul95pAyxKq2Hu%2FNrqcdAKO83RKsihBx8%2ByH0q%2BjEEOoLkr6ojhR4h4iqZjCt%2BKHmqqEYFu8Bm4Bcl6xcc2DZBmuhR4GErPWzHbUdrpsIiW4bcOIZXumL7In7LOCt7b1nM4Av%2BK7IOtDo0t%2BJGTSj0X2sY1ORCBrYo1IMKGKGPy8YrB6j%2BjID5XcPX3Zcz4YmFkFFPYAPphTPjKmkttK6gJGYgDC6ayzexCCa6JMMBgNjY8HoMFkcjiYVRkeWiZX7NpevS1lJR6evIVAGnaCHHqJdYXPaOZCanBJCPw%2BsPV2mmeDZkBmxiVAwMohLeHhXxu8LThu4JNbS4PpKoZdrKDi1za82xbR7S1zZgd6vYV6vQrZSY9ODtoAL3Jcg7YBFP7lJTHmDhZi%2FTEhtE6YRzYnjbGfOmjttIAmX9RoDsTl01jeRPvsPO0HSsXahSy2XmOUtLb5OCRZP4IdNBTIzO0n%2FaAThpOmAaqONe%2F5AFfj%2BGvbDsQsp62fW37rNdom8w%2FpKQzAY6pgGg9Hcpc8%2F4htN1rfJ5WybGg67e2bxdrqPd1bvoImlkXg3hotaJ0wBkacrShZzod5Hev6l8WtXndehkdUx7k4zNoK7RDE2s53%2F3HxvZ5qQV6ffEUgRMQK2FYDoARe4KseFuUJ53P61eB2%2BJ5bopuzeCbx1InWW54wiIukD%2FD3ix0CfC%2FeD8ID7Z32TR6uyXvgyOIMMlU%2BzMTLSi2w35%2BFpTGq7D%2FBt%2B&X-Amz-Signature=4eaa6ee873857438ec25ea4fd75b51b3d77d9d25d85dc9659ed475fa577c6ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBC3YZN3%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCID2IXTJINiN6%2Blk0jzqYylHXCc0hv0hojvipxYZnsmJ9AiABRuIV0FW1XBSDD2mB8rAUPIhyc8RO41X%2BuuWBQ6xcyCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMY7FZ%2BxFMpSFCR4zWKtwDAAjVRlfgKh3YyIgrxw9of5RW2MCsXjLk7spiLxLymfXgkxCL%2BMhit5hzfXddSDVj97I8nSKh7Pk%2Bk2Ni%2Fp8LENXORtIispkg%2BvZ1ThavhoirXIzYQYhGMws4Xq1ul95pAyxKq2Hu%2FNrqcdAKO83RKsihBx8%2ByH0q%2BjEEOoLkr6ojhR4h4iqZjCt%2BKHmqqEYFu8Bm4Bcl6xcc2DZBmuhR4GErPWzHbUdrpsIiW4bcOIZXumL7In7LOCt7b1nM4Av%2BK7IOtDo0t%2BJGTSj0X2sY1ORCBrYo1IMKGKGPy8YrB6j%2BjID5XcPX3Zcz4YmFkFFPYAPphTPjKmkttK6gJGYgDC6ayzexCCa6JMMBgNjY8HoMFkcjiYVRkeWiZX7NpevS1lJR6evIVAGnaCHHqJdYXPaOZCanBJCPw%2BsPV2mmeDZkBmxiVAwMohLeHhXxu8LThu4JNbS4PpKoZdrKDi1za82xbR7S1zZgd6vYV6vQrZSY9ODtoAL3Jcg7YBFP7lJTHmDhZi%2FTEhtE6YRzYnjbGfOmjttIAmX9RoDsTl01jeRPvsPO0HSsXahSy2XmOUtLb5OCRZP4IdNBTIzO0n%2FaAThpOmAaqONe%2F5AFfj%2BGvbDsQsp62fW37rNdom8w%2FpKQzAY6pgGg9Hcpc8%2F4htN1rfJ5WybGg67e2bxdrqPd1bvoImlkXg3hotaJ0wBkacrShZzod5Hev6l8WtXndehkdUx7k4zNoK7RDE2s53%2F3HxvZ5qQV6ffEUgRMQK2FYDoARe4KseFuUJ53P61eB2%2BJ5bopuzeCbx1InWW54wiIukD%2FD3ix0CfC%2FeD8ID7Z32TR6uyXvgyOIMMlU%2BzMTLSi2w35%2BFpTGq7D%2FBt%2B&X-Amz-Signature=39f3310b4a7109fa2916cbdbe121fb9f87936eb45532446cdc8823560d792092&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBC3YZN3%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCID2IXTJINiN6%2Blk0jzqYylHXCc0hv0hojvipxYZnsmJ9AiABRuIV0FW1XBSDD2mB8rAUPIhyc8RO41X%2BuuWBQ6xcyCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMY7FZ%2BxFMpSFCR4zWKtwDAAjVRlfgKh3YyIgrxw9of5RW2MCsXjLk7spiLxLymfXgkxCL%2BMhit5hzfXddSDVj97I8nSKh7Pk%2Bk2Ni%2Fp8LENXORtIispkg%2BvZ1ThavhoirXIzYQYhGMws4Xq1ul95pAyxKq2Hu%2FNrqcdAKO83RKsihBx8%2ByH0q%2BjEEOoLkr6ojhR4h4iqZjCt%2BKHmqqEYFu8Bm4Bcl6xcc2DZBmuhR4GErPWzHbUdrpsIiW4bcOIZXumL7In7LOCt7b1nM4Av%2BK7IOtDo0t%2BJGTSj0X2sY1ORCBrYo1IMKGKGPy8YrB6j%2BjID5XcPX3Zcz4YmFkFFPYAPphTPjKmkttK6gJGYgDC6ayzexCCa6JMMBgNjY8HoMFkcjiYVRkeWiZX7NpevS1lJR6evIVAGnaCHHqJdYXPaOZCanBJCPw%2BsPV2mmeDZkBmxiVAwMohLeHhXxu8LThu4JNbS4PpKoZdrKDi1za82xbR7S1zZgd6vYV6vQrZSY9ODtoAL3Jcg7YBFP7lJTHmDhZi%2FTEhtE6YRzYnjbGfOmjttIAmX9RoDsTl01jeRPvsPO0HSsXahSy2XmOUtLb5OCRZP4IdNBTIzO0n%2FaAThpOmAaqONe%2F5AFfj%2BGvbDsQsp62fW37rNdom8w%2FpKQzAY6pgGg9Hcpc8%2F4htN1rfJ5WybGg67e2bxdrqPd1bvoImlkXg3hotaJ0wBkacrShZzod5Hev6l8WtXndehkdUx7k4zNoK7RDE2s53%2F3HxvZ5qQV6ffEUgRMQK2FYDoARe4KseFuUJ53P61eB2%2BJ5bopuzeCbx1InWW54wiIukD%2FD3ix0CfC%2FeD8ID7Z32TR6uyXvgyOIMMlU%2BzMTLSi2w35%2BFpTGq7D%2FBt%2B&X-Amz-Signature=63f3361b1e49718a3c4e79425fc1c6b5811d20a527a1dc88603c690fd9ad4c15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



