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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSHBPDBV%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVzbO0aD2mgrK4mvH4%2BgBvpUJoIbReNMISgcEWF657%2FQIgHJ80klL1%2FX%2B3YMFzlAbquC9kAYMBlI6Ex9IJhMY%2F4uoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDJfN%2BxzwfaVd52vN%2BCrcA6kMMDcI1W18zyyoKhk5ihA7SIAz6ozZOzPCj7%2FUgst7GfE3rWWHRa15lMMBLG6Erbkw08miEUNZ2goZj1YSfn5kdHKMyyXav4KP3wM9k1h6xcvLK%2F4HIuIVKAcbcZkcVzCwjbRxM6yFVHeU%2BNLUTIY7LmI81ttSXCxC6c1K%2FPZMSPNzbQuMRwgMfE132pETik7bEfZqk9%2F8hlHsZEUOzjNq%2BSNDqD6ti687C7x6LgsUIUPnE0Vu5%2BPFA6Xb5U2Q21KSIkYP%2F2ny9LukBnU55tthReOE67XJVP7lcQhdIoOs4R0G%2BUtH0NL9uqASty2ERSVB76pDbZD8M76wS1EtDOWB7BBYdIWY7rWtp243hYVqivmkc9IRP6yGW83dK%2BaY8KkNsX3Nl12xfC%2Frk6ujtXt1xnKlDhdxOG3Do2PffgleHQYfAUtW0pK%2FE2ghNMTdwwXZnydNI3UBWsK6igYU33S%2FUp%2FnSSMc0tRfiZvqjRqWm6jTYl6d9oCf2W9GhsFGKLGNl3ltSU9eFIYX4Rk0Dc4FoJ2nK0r0hHhD5n3v0DIuOW6Lx2e87fnRkQ2J4zCHsy%2BSGjcOvGOnVwsouPgPm%2BxSpIlq5u0koh4FT6u4on%2BiG85zfFZyDWKFM%2FvXMOvRq8sGOqUBlj70A7fSTmWCukU%2BXTlqbXHfGw7kE3Z70ibbKUfvDeBY5mMZ%2FCYEbs7fd6IdwtYFiTlHnYJ5EdlASy5wgumPNvHkYCXbed9yvHQr2nkCqrtpYuJaKBRERf2aD73AO66GShQpBGYe0fjkjv3wG2AOSLxIqXgMm74a28iUIU9navpcse6iOCWp9yWFpJ9traxd4P%2B2flaXGbsBwbZWjQRivUuAoDBz&X-Amz-Signature=da79d5389c5c92814146487d16b73b3a7498084ab8802fa0cb7c0b9b05b43019&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSHBPDBV%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVzbO0aD2mgrK4mvH4%2BgBvpUJoIbReNMISgcEWF657%2FQIgHJ80klL1%2FX%2B3YMFzlAbquC9kAYMBlI6Ex9IJhMY%2F4uoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDJfN%2BxzwfaVd52vN%2BCrcA6kMMDcI1W18zyyoKhk5ihA7SIAz6ozZOzPCj7%2FUgst7GfE3rWWHRa15lMMBLG6Erbkw08miEUNZ2goZj1YSfn5kdHKMyyXav4KP3wM9k1h6xcvLK%2F4HIuIVKAcbcZkcVzCwjbRxM6yFVHeU%2BNLUTIY7LmI81ttSXCxC6c1K%2FPZMSPNzbQuMRwgMfE132pETik7bEfZqk9%2F8hlHsZEUOzjNq%2BSNDqD6ti687C7x6LgsUIUPnE0Vu5%2BPFA6Xb5U2Q21KSIkYP%2F2ny9LukBnU55tthReOE67XJVP7lcQhdIoOs4R0G%2BUtH0NL9uqASty2ERSVB76pDbZD8M76wS1EtDOWB7BBYdIWY7rWtp243hYVqivmkc9IRP6yGW83dK%2BaY8KkNsX3Nl12xfC%2Frk6ujtXt1xnKlDhdxOG3Do2PffgleHQYfAUtW0pK%2FE2ghNMTdwwXZnydNI3UBWsK6igYU33S%2FUp%2FnSSMc0tRfiZvqjRqWm6jTYl6d9oCf2W9GhsFGKLGNl3ltSU9eFIYX4Rk0Dc4FoJ2nK0r0hHhD5n3v0DIuOW6Lx2e87fnRkQ2J4zCHsy%2BSGjcOvGOnVwsouPgPm%2BxSpIlq5u0koh4FT6u4on%2BiG85zfFZyDWKFM%2FvXMOvRq8sGOqUBlj70A7fSTmWCukU%2BXTlqbXHfGw7kE3Z70ibbKUfvDeBY5mMZ%2FCYEbs7fd6IdwtYFiTlHnYJ5EdlASy5wgumPNvHkYCXbed9yvHQr2nkCqrtpYuJaKBRERf2aD73AO66GShQpBGYe0fjkjv3wG2AOSLxIqXgMm74a28iUIU9navpcse6iOCWp9yWFpJ9traxd4P%2B2flaXGbsBwbZWjQRivUuAoDBz&X-Amz-Signature=0a7e82eee7af9a25f01367179f812dde0701f8c8efeed0cce603d9b2ab3e8995&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSHBPDBV%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVzbO0aD2mgrK4mvH4%2BgBvpUJoIbReNMISgcEWF657%2FQIgHJ80klL1%2FX%2B3YMFzlAbquC9kAYMBlI6Ex9IJhMY%2F4uoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDJfN%2BxzwfaVd52vN%2BCrcA6kMMDcI1W18zyyoKhk5ihA7SIAz6ozZOzPCj7%2FUgst7GfE3rWWHRa15lMMBLG6Erbkw08miEUNZ2goZj1YSfn5kdHKMyyXav4KP3wM9k1h6xcvLK%2F4HIuIVKAcbcZkcVzCwjbRxM6yFVHeU%2BNLUTIY7LmI81ttSXCxC6c1K%2FPZMSPNzbQuMRwgMfE132pETik7bEfZqk9%2F8hlHsZEUOzjNq%2BSNDqD6ti687C7x6LgsUIUPnE0Vu5%2BPFA6Xb5U2Q21KSIkYP%2F2ny9LukBnU55tthReOE67XJVP7lcQhdIoOs4R0G%2BUtH0NL9uqASty2ERSVB76pDbZD8M76wS1EtDOWB7BBYdIWY7rWtp243hYVqivmkc9IRP6yGW83dK%2BaY8KkNsX3Nl12xfC%2Frk6ujtXt1xnKlDhdxOG3Do2PffgleHQYfAUtW0pK%2FE2ghNMTdwwXZnydNI3UBWsK6igYU33S%2FUp%2FnSSMc0tRfiZvqjRqWm6jTYl6d9oCf2W9GhsFGKLGNl3ltSU9eFIYX4Rk0Dc4FoJ2nK0r0hHhD5n3v0DIuOW6Lx2e87fnRkQ2J4zCHsy%2BSGjcOvGOnVwsouPgPm%2BxSpIlq5u0koh4FT6u4on%2BiG85zfFZyDWKFM%2FvXMOvRq8sGOqUBlj70A7fSTmWCukU%2BXTlqbXHfGw7kE3Z70ibbKUfvDeBY5mMZ%2FCYEbs7fd6IdwtYFiTlHnYJ5EdlASy5wgumPNvHkYCXbed9yvHQr2nkCqrtpYuJaKBRERf2aD73AO66GShQpBGYe0fjkjv3wG2AOSLxIqXgMm74a28iUIU9navpcse6iOCWp9yWFpJ9traxd4P%2B2flaXGbsBwbZWjQRivUuAoDBz&X-Amz-Signature=5abed14238f961006b895ff1eea37d6399b919f522a853be355ca85a8b179b18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSHBPDBV%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVzbO0aD2mgrK4mvH4%2BgBvpUJoIbReNMISgcEWF657%2FQIgHJ80klL1%2FX%2B3YMFzlAbquC9kAYMBlI6Ex9IJhMY%2F4uoq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDJfN%2BxzwfaVd52vN%2BCrcA6kMMDcI1W18zyyoKhk5ihA7SIAz6ozZOzPCj7%2FUgst7GfE3rWWHRa15lMMBLG6Erbkw08miEUNZ2goZj1YSfn5kdHKMyyXav4KP3wM9k1h6xcvLK%2F4HIuIVKAcbcZkcVzCwjbRxM6yFVHeU%2BNLUTIY7LmI81ttSXCxC6c1K%2FPZMSPNzbQuMRwgMfE132pETik7bEfZqk9%2F8hlHsZEUOzjNq%2BSNDqD6ti687C7x6LgsUIUPnE0Vu5%2BPFA6Xb5U2Q21KSIkYP%2F2ny9LukBnU55tthReOE67XJVP7lcQhdIoOs4R0G%2BUtH0NL9uqASty2ERSVB76pDbZD8M76wS1EtDOWB7BBYdIWY7rWtp243hYVqivmkc9IRP6yGW83dK%2BaY8KkNsX3Nl12xfC%2Frk6ujtXt1xnKlDhdxOG3Do2PffgleHQYfAUtW0pK%2FE2ghNMTdwwXZnydNI3UBWsK6igYU33S%2FUp%2FnSSMc0tRfiZvqjRqWm6jTYl6d9oCf2W9GhsFGKLGNl3ltSU9eFIYX4Rk0Dc4FoJ2nK0r0hHhD5n3v0DIuOW6Lx2e87fnRkQ2J4zCHsy%2BSGjcOvGOnVwsouPgPm%2BxSpIlq5u0koh4FT6u4on%2BiG85zfFZyDWKFM%2FvXMOvRq8sGOqUBlj70A7fSTmWCukU%2BXTlqbXHfGw7kE3Z70ibbKUfvDeBY5mMZ%2FCYEbs7fd6IdwtYFiTlHnYJ5EdlASy5wgumPNvHkYCXbed9yvHQr2nkCqrtpYuJaKBRERf2aD73AO66GShQpBGYe0fjkjv3wG2AOSLxIqXgMm74a28iUIU9navpcse6iOCWp9yWFpJ9traxd4P%2B2flaXGbsBwbZWjQRivUuAoDBz&X-Amz-Signature=4954eea07ce6f6b9fec2e1a3d939ea724d38799d96e846097f77b19ca19c3e16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



