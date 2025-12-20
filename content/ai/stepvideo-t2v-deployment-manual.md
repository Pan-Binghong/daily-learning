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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WH5C3YV%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDtBtz9POdT8VFV2o%2BaIBu3%2BS4M60uB4HsLYBe2iZ52MAiAia6U%2FW8irVxrQLZMylefYrRuRFwyrcOM9C3blZvXobCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME7WGFmXzlYa2BCK%2BKtwDEanXjeLJKL3OvxL3A%2FRIJaAYih0QSF4YLPBj4uBO3rANKznBrtbDO6M56jFT6SqkHuyXepYPakIuN278cAg9DTqR%2FZmBh35iRn4YFQQUWL2Y3C9oj6NjUW%2BOqncOHbv6AE9FSDU8pGH8i9DbKT9EbdsPR9m4IBDKMf2vPUZlmKGBRAqpEJUnpguiD44gbvdwSWVKVVKFGCODRHnjz%2F5JzgfvfTDF7VCgtHIdxBBAxpH8ZLe0tpSyKBoj6ue3N%2Bg5XJOFUZhASGtTFIXgZPeYuJmw4P2aiHWGZNJxK4%2Bijd8ewfr6awwrN9brWXwXRjP4k6o387BDaQObF3wwk%2BWLD0UAk2HjWTQN9n1cBWm0DHF6haJGZam2kglh5KkO%2BdMXtNVYmDireCNhGgXgtl5nXEWzzHwbFgkHPWQsfUoLswPKFuInzzerynu%2Bel%2B46VRRWb20PZZtOqWhrCXTELxL081dek4Z6%2FwJWnEfMqMkM4gCxhEafG%2FZ8NfQ2msCSvhgQwGanKJ41opW0HA5%2BlnDPvma4vE56hklrO%2FnMSsdYDNeA%2B%2Fzr8XiNlzvl%2Bucd7nOSjAw7izvwqXiZFWQVWfdAYlbtFXJWBRkgr8n82m8Bh%2BCk4BaKRiKwsCDZKAw24WYygY6pgHhWt69iCgSx9xhAF5%2Fna%2BirhoV7lxrC4DR619cJZPMjD8R%2BMm1fD9wVuOdubBss%2FHf9TEjZhiUwnaEwOZcrysj3CFfNrlBZU%2BzF%2FbS8Nb7Ff%2FNa3bE2O1AYpnKqpU2pc7U%2BnLFvNcvhgbqT%2FwpIZOvNsnrlFb8%2BbTyhkkPZXSTdUBpUQCDP9yY3DwigmbJCoUbYZYm3%2FdfEwb5Y%2FulSucWeBUGMear&X-Amz-Signature=19a366be139aca2f3f65dbb5200c05d74baaa898320519439f146c39161cde11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WH5C3YV%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDtBtz9POdT8VFV2o%2BaIBu3%2BS4M60uB4HsLYBe2iZ52MAiAia6U%2FW8irVxrQLZMylefYrRuRFwyrcOM9C3blZvXobCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME7WGFmXzlYa2BCK%2BKtwDEanXjeLJKL3OvxL3A%2FRIJaAYih0QSF4YLPBj4uBO3rANKznBrtbDO6M56jFT6SqkHuyXepYPakIuN278cAg9DTqR%2FZmBh35iRn4YFQQUWL2Y3C9oj6NjUW%2BOqncOHbv6AE9FSDU8pGH8i9DbKT9EbdsPR9m4IBDKMf2vPUZlmKGBRAqpEJUnpguiD44gbvdwSWVKVVKFGCODRHnjz%2F5JzgfvfTDF7VCgtHIdxBBAxpH8ZLe0tpSyKBoj6ue3N%2Bg5XJOFUZhASGtTFIXgZPeYuJmw4P2aiHWGZNJxK4%2Bijd8ewfr6awwrN9brWXwXRjP4k6o387BDaQObF3wwk%2BWLD0UAk2HjWTQN9n1cBWm0DHF6haJGZam2kglh5KkO%2BdMXtNVYmDireCNhGgXgtl5nXEWzzHwbFgkHPWQsfUoLswPKFuInzzerynu%2Bel%2B46VRRWb20PZZtOqWhrCXTELxL081dek4Z6%2FwJWnEfMqMkM4gCxhEafG%2FZ8NfQ2msCSvhgQwGanKJ41opW0HA5%2BlnDPvma4vE56hklrO%2FnMSsdYDNeA%2B%2Fzr8XiNlzvl%2Bucd7nOSjAw7izvwqXiZFWQVWfdAYlbtFXJWBRkgr8n82m8Bh%2BCk4BaKRiKwsCDZKAw24WYygY6pgHhWt69iCgSx9xhAF5%2Fna%2BirhoV7lxrC4DR619cJZPMjD8R%2BMm1fD9wVuOdubBss%2FHf9TEjZhiUwnaEwOZcrysj3CFfNrlBZU%2BzF%2FbS8Nb7Ff%2FNa3bE2O1AYpnKqpU2pc7U%2BnLFvNcvhgbqT%2FwpIZOvNsnrlFb8%2BbTyhkkPZXSTdUBpUQCDP9yY3DwigmbJCoUbYZYm3%2FdfEwb5Y%2FulSucWeBUGMear&X-Amz-Signature=837621509cee68f75ac7547fa2a5dc92d85862bb802e8a09c6c9bb233deae13f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WH5C3YV%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDtBtz9POdT8VFV2o%2BaIBu3%2BS4M60uB4HsLYBe2iZ52MAiAia6U%2FW8irVxrQLZMylefYrRuRFwyrcOM9C3blZvXobCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME7WGFmXzlYa2BCK%2BKtwDEanXjeLJKL3OvxL3A%2FRIJaAYih0QSF4YLPBj4uBO3rANKznBrtbDO6M56jFT6SqkHuyXepYPakIuN278cAg9DTqR%2FZmBh35iRn4YFQQUWL2Y3C9oj6NjUW%2BOqncOHbv6AE9FSDU8pGH8i9DbKT9EbdsPR9m4IBDKMf2vPUZlmKGBRAqpEJUnpguiD44gbvdwSWVKVVKFGCODRHnjz%2F5JzgfvfTDF7VCgtHIdxBBAxpH8ZLe0tpSyKBoj6ue3N%2Bg5XJOFUZhASGtTFIXgZPeYuJmw4P2aiHWGZNJxK4%2Bijd8ewfr6awwrN9brWXwXRjP4k6o387BDaQObF3wwk%2BWLD0UAk2HjWTQN9n1cBWm0DHF6haJGZam2kglh5KkO%2BdMXtNVYmDireCNhGgXgtl5nXEWzzHwbFgkHPWQsfUoLswPKFuInzzerynu%2Bel%2B46VRRWb20PZZtOqWhrCXTELxL081dek4Z6%2FwJWnEfMqMkM4gCxhEafG%2FZ8NfQ2msCSvhgQwGanKJ41opW0HA5%2BlnDPvma4vE56hklrO%2FnMSsdYDNeA%2B%2Fzr8XiNlzvl%2Bucd7nOSjAw7izvwqXiZFWQVWfdAYlbtFXJWBRkgr8n82m8Bh%2BCk4BaKRiKwsCDZKAw24WYygY6pgHhWt69iCgSx9xhAF5%2Fna%2BirhoV7lxrC4DR619cJZPMjD8R%2BMm1fD9wVuOdubBss%2FHf9TEjZhiUwnaEwOZcrysj3CFfNrlBZU%2BzF%2FbS8Nb7Ff%2FNa3bE2O1AYpnKqpU2pc7U%2BnLFvNcvhgbqT%2FwpIZOvNsnrlFb8%2BbTyhkkPZXSTdUBpUQCDP9yY3DwigmbJCoUbYZYm3%2FdfEwb5Y%2FulSucWeBUGMear&X-Amz-Signature=484c1ceb2ff8c72cbb13653674f94ce3e618db69a2e32bd45c9e322d57550d3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WH5C3YV%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDtBtz9POdT8VFV2o%2BaIBu3%2BS4M60uB4HsLYBe2iZ52MAiAia6U%2FW8irVxrQLZMylefYrRuRFwyrcOM9C3blZvXobCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME7WGFmXzlYa2BCK%2BKtwDEanXjeLJKL3OvxL3A%2FRIJaAYih0QSF4YLPBj4uBO3rANKznBrtbDO6M56jFT6SqkHuyXepYPakIuN278cAg9DTqR%2FZmBh35iRn4YFQQUWL2Y3C9oj6NjUW%2BOqncOHbv6AE9FSDU8pGH8i9DbKT9EbdsPR9m4IBDKMf2vPUZlmKGBRAqpEJUnpguiD44gbvdwSWVKVVKFGCODRHnjz%2F5JzgfvfTDF7VCgtHIdxBBAxpH8ZLe0tpSyKBoj6ue3N%2Bg5XJOFUZhASGtTFIXgZPeYuJmw4P2aiHWGZNJxK4%2Bijd8ewfr6awwrN9brWXwXRjP4k6o387BDaQObF3wwk%2BWLD0UAk2HjWTQN9n1cBWm0DHF6haJGZam2kglh5KkO%2BdMXtNVYmDireCNhGgXgtl5nXEWzzHwbFgkHPWQsfUoLswPKFuInzzerynu%2Bel%2B46VRRWb20PZZtOqWhrCXTELxL081dek4Z6%2FwJWnEfMqMkM4gCxhEafG%2FZ8NfQ2msCSvhgQwGanKJ41opW0HA5%2BlnDPvma4vE56hklrO%2FnMSsdYDNeA%2B%2Fzr8XiNlzvl%2Bucd7nOSjAw7izvwqXiZFWQVWfdAYlbtFXJWBRkgr8n82m8Bh%2BCk4BaKRiKwsCDZKAw24WYygY6pgHhWt69iCgSx9xhAF5%2Fna%2BirhoV7lxrC4DR619cJZPMjD8R%2BMm1fD9wVuOdubBss%2FHf9TEjZhiUwnaEwOZcrysj3CFfNrlBZU%2BzF%2FbS8Nb7Ff%2FNa3bE2O1AYpnKqpU2pc7U%2BnLFvNcvhgbqT%2FwpIZOvNsnrlFb8%2BbTyhkkPZXSTdUBpUQCDP9yY3DwigmbJCoUbYZYm3%2FdfEwb5Y%2FulSucWeBUGMear&X-Amz-Signature=f75e81c3eb820f47c2387ff9bb2eadec8281648f4925a107b53620bf6defd626&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



