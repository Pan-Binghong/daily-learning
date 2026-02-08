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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD7IG473%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr%2FxxDGZtwEB9OJF%2FAKdMO2%2BOlBBT%2B9ABfPrFaHH72jAiEA00gbHIAr%2FFS3qOxJqakh7CGUo5baSOMdL8UWKjXuxYcq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKTSUqrYlk8d0dcleSrcA7ypFMqIsYClpyIcFWO7PJYTTe4U6oiuYtua1G3tXGU7G%2B8YtQdBHG8NLMt7ULjJCVY8oqz26Uq0Bsb0tJOOV9Z7oGKDHuSXxCBYJsd59CqbjdmnlmKiazDVvrjCCsQpVwKLZzdj%2FBKUL7lRjFr8eVYpqFmYjkHmSWigK4srrXNQra6N2b5m%2BL1fcVI%2Fgtw43WhvRlhPEWSL7wXUPADG8Aei4qclYyXe0QvV1KJxo3yOBvpe0fou5Z9O1n5eXHZ1Py9fKcZspgwWJO17q7qqT68wDGoaVTGCFWL4fnmDs4IFk8dp%2Bhv6UKkl7gsho4IOrG%2Fu4aCMi7LWWdfCq7gav1P4Sr%2FcwPAfyUFAf29TPbD9iF%2FovWMl9gAz0nOP6giphmGy0Npr0c8Fqq1evZzz6rQ4UAVQjKOJcaxMr92%2BtcdfeUG7T6UHFDRvEiq%2Bzbn9HFhvrfPIQqFefbWM6u6EUsSyw%2FCWl1mVl0Lhbjzefh71ahEJ3dzXgTY04c4M%2FG4K2HLU%2FsNzfr3kzEmw4GEa76CxWoTPWt%2FgcZTNIGUl4raOoe6i5Yu%2BLaJTDkxSuXYaZvH%2B08hEXiDEinBpZAdKVhDBzQ3PfF9URiMuyJK0XDauqoDGf8skborg9MYCML2LoMwGOqUB5AL9wD3YfixJrRvka7VCt6GzRgp46JAKoMnDCnDk8F0kIREIcifaxIFfKXcmx24qrgI%2BECo8j6yelvngx%2Bs3AT6rsJSG6%2Fa1RO67ZAJqg%2B%2FYeW6adiDw11PJ0AxV0xJa1PTiLNxh5%2FxRY7kJVw0k1pYMl4xHNzPIi1S06ge7PRTPAhlg3qUjHrscHPaAhPnHFwjMW8vs%2Fwp0KwCQJP3vyZmDXfja&X-Amz-Signature=17e6eaa9e700944e02d62565dfe2797e8251ae9e1e5ea7838d618ed5f21f67bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD7IG473%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr%2FxxDGZtwEB9OJF%2FAKdMO2%2BOlBBT%2B9ABfPrFaHH72jAiEA00gbHIAr%2FFS3qOxJqakh7CGUo5baSOMdL8UWKjXuxYcq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKTSUqrYlk8d0dcleSrcA7ypFMqIsYClpyIcFWO7PJYTTe4U6oiuYtua1G3tXGU7G%2B8YtQdBHG8NLMt7ULjJCVY8oqz26Uq0Bsb0tJOOV9Z7oGKDHuSXxCBYJsd59CqbjdmnlmKiazDVvrjCCsQpVwKLZzdj%2FBKUL7lRjFr8eVYpqFmYjkHmSWigK4srrXNQra6N2b5m%2BL1fcVI%2Fgtw43WhvRlhPEWSL7wXUPADG8Aei4qclYyXe0QvV1KJxo3yOBvpe0fou5Z9O1n5eXHZ1Py9fKcZspgwWJO17q7qqT68wDGoaVTGCFWL4fnmDs4IFk8dp%2Bhv6UKkl7gsho4IOrG%2Fu4aCMi7LWWdfCq7gav1P4Sr%2FcwPAfyUFAf29TPbD9iF%2FovWMl9gAz0nOP6giphmGy0Npr0c8Fqq1evZzz6rQ4UAVQjKOJcaxMr92%2BtcdfeUG7T6UHFDRvEiq%2Bzbn9HFhvrfPIQqFefbWM6u6EUsSyw%2FCWl1mVl0Lhbjzefh71ahEJ3dzXgTY04c4M%2FG4K2HLU%2FsNzfr3kzEmw4GEa76CxWoTPWt%2FgcZTNIGUl4raOoe6i5Yu%2BLaJTDkxSuXYaZvH%2B08hEXiDEinBpZAdKVhDBzQ3PfF9URiMuyJK0XDauqoDGf8skborg9MYCML2LoMwGOqUB5AL9wD3YfixJrRvka7VCt6GzRgp46JAKoMnDCnDk8F0kIREIcifaxIFfKXcmx24qrgI%2BECo8j6yelvngx%2Bs3AT6rsJSG6%2Fa1RO67ZAJqg%2B%2FYeW6adiDw11PJ0AxV0xJa1PTiLNxh5%2FxRY7kJVw0k1pYMl4xHNzPIi1S06ge7PRTPAhlg3qUjHrscHPaAhPnHFwjMW8vs%2Fwp0KwCQJP3vyZmDXfja&X-Amz-Signature=e6940107a61b2a5c23f5aaad2220dba4674b3061bd954596b6c0b1fa15ee750a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD7IG473%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr%2FxxDGZtwEB9OJF%2FAKdMO2%2BOlBBT%2B9ABfPrFaHH72jAiEA00gbHIAr%2FFS3qOxJqakh7CGUo5baSOMdL8UWKjXuxYcq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKTSUqrYlk8d0dcleSrcA7ypFMqIsYClpyIcFWO7PJYTTe4U6oiuYtua1G3tXGU7G%2B8YtQdBHG8NLMt7ULjJCVY8oqz26Uq0Bsb0tJOOV9Z7oGKDHuSXxCBYJsd59CqbjdmnlmKiazDVvrjCCsQpVwKLZzdj%2FBKUL7lRjFr8eVYpqFmYjkHmSWigK4srrXNQra6N2b5m%2BL1fcVI%2Fgtw43WhvRlhPEWSL7wXUPADG8Aei4qclYyXe0QvV1KJxo3yOBvpe0fou5Z9O1n5eXHZ1Py9fKcZspgwWJO17q7qqT68wDGoaVTGCFWL4fnmDs4IFk8dp%2Bhv6UKkl7gsho4IOrG%2Fu4aCMi7LWWdfCq7gav1P4Sr%2FcwPAfyUFAf29TPbD9iF%2FovWMl9gAz0nOP6giphmGy0Npr0c8Fqq1evZzz6rQ4UAVQjKOJcaxMr92%2BtcdfeUG7T6UHFDRvEiq%2Bzbn9HFhvrfPIQqFefbWM6u6EUsSyw%2FCWl1mVl0Lhbjzefh71ahEJ3dzXgTY04c4M%2FG4K2HLU%2FsNzfr3kzEmw4GEa76CxWoTPWt%2FgcZTNIGUl4raOoe6i5Yu%2BLaJTDkxSuXYaZvH%2B08hEXiDEinBpZAdKVhDBzQ3PfF9URiMuyJK0XDauqoDGf8skborg9MYCML2LoMwGOqUB5AL9wD3YfixJrRvka7VCt6GzRgp46JAKoMnDCnDk8F0kIREIcifaxIFfKXcmx24qrgI%2BECo8j6yelvngx%2Bs3AT6rsJSG6%2Fa1RO67ZAJqg%2B%2FYeW6adiDw11PJ0AxV0xJa1PTiLNxh5%2FxRY7kJVw0k1pYMl4xHNzPIi1S06ge7PRTPAhlg3qUjHrscHPaAhPnHFwjMW8vs%2Fwp0KwCQJP3vyZmDXfja&X-Amz-Signature=16cb57d212d80e5a2c52f62e9a787d004988e68c5273bbfc835cc7ae613771d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD7IG473%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr%2FxxDGZtwEB9OJF%2FAKdMO2%2BOlBBT%2B9ABfPrFaHH72jAiEA00gbHIAr%2FFS3qOxJqakh7CGUo5baSOMdL8UWKjXuxYcq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKTSUqrYlk8d0dcleSrcA7ypFMqIsYClpyIcFWO7PJYTTe4U6oiuYtua1G3tXGU7G%2B8YtQdBHG8NLMt7ULjJCVY8oqz26Uq0Bsb0tJOOV9Z7oGKDHuSXxCBYJsd59CqbjdmnlmKiazDVvrjCCsQpVwKLZzdj%2FBKUL7lRjFr8eVYpqFmYjkHmSWigK4srrXNQra6N2b5m%2BL1fcVI%2Fgtw43WhvRlhPEWSL7wXUPADG8Aei4qclYyXe0QvV1KJxo3yOBvpe0fou5Z9O1n5eXHZ1Py9fKcZspgwWJO17q7qqT68wDGoaVTGCFWL4fnmDs4IFk8dp%2Bhv6UKkl7gsho4IOrG%2Fu4aCMi7LWWdfCq7gav1P4Sr%2FcwPAfyUFAf29TPbD9iF%2FovWMl9gAz0nOP6giphmGy0Npr0c8Fqq1evZzz6rQ4UAVQjKOJcaxMr92%2BtcdfeUG7T6UHFDRvEiq%2Bzbn9HFhvrfPIQqFefbWM6u6EUsSyw%2FCWl1mVl0Lhbjzefh71ahEJ3dzXgTY04c4M%2FG4K2HLU%2FsNzfr3kzEmw4GEa76CxWoTPWt%2FgcZTNIGUl4raOoe6i5Yu%2BLaJTDkxSuXYaZvH%2B08hEXiDEinBpZAdKVhDBzQ3PfF9URiMuyJK0XDauqoDGf8skborg9MYCML2LoMwGOqUB5AL9wD3YfixJrRvka7VCt6GzRgp46JAKoMnDCnDk8F0kIREIcifaxIFfKXcmx24qrgI%2BECo8j6yelvngx%2Bs3AT6rsJSG6%2Fa1RO67ZAJqg%2B%2FYeW6adiDw11PJ0AxV0xJa1PTiLNxh5%2FxRY7kJVw0k1pYMl4xHNzPIi1S06ge7PRTPAhlg3qUjHrscHPaAhPnHFwjMW8vs%2Fwp0KwCQJP3vyZmDXfja&X-Amz-Signature=d7fc9abef52c30bfc4a2e393298b0fd6de76381ebcf2834ce5583cf5c8e77e51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



