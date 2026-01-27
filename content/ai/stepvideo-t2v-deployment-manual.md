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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637524GIP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKo5xd1Mw5%2FIhF5bkonpQMGMz8s5kqm8OavvsK44dROgIhALX0tHdRVVaWCkxJhlJx1Kdz%2FtDnUMiR%2BCnGLxwGe4MmKv8DCEwQABoMNjM3NDIzMTgzODA1IgyiQixJzsbIcUkyf%2FYq3AO4iOxBCAtRCLs7hAlTMAGdbYkntBDUqoEUKGNRy9DIR%2ByfDUgSyUpLSchf3BNc1PtWx6XGsLYEhSknC2cE0TH0UJHJ9YRCNAIEHJvlSSC1CfiRw5vDIEYL3RPj2c%2BDl4vGdP7wo7ivu6g4yT4Hi53z7axQ7%2BH%2FFe9bsaJGUNTWOB%2FeZ1S2TH4SkaIKMoWPu69b8wx8ANevU6gGd4cTOkarf8zY3T9TiDeyBzyy5vR%2BqEtUkSH5EgM%2Fr9aO7UovYk20XpcYr0WL2XBiZyuIiV2YfNjeXP%2FHHuGEuVbiXfg8bgphAexKZ0eZvUJv0afmGJxC7pjFmsJqO5ik67uahAypT0vwGUoeztJCZFOb8nViAktLalNRVmJlpHFLTc2N%2BN%2Bl3RSf1uG7LgFS3o%2BFxwOX%2BwIHQCBe%2BfPz6G%2BM3e8HdefFW6%2FoYgV%2BhI1DFIi%2B0J3fTR9SncGgYYPE9aaCXG7sbNUPrMs3gmQTUis2K7rppoFMYKxKm5DfugTJbUbwbrmKZ0W8j36WK2tcFqvxZSXGARXBzffWRPgBgDIN%2FvID5SCtVgiIkbU3kvMzjiijzu7HL3OHjcWkb22c8pXCpa1XM46OHyANUd8UyCGtU72r9GunehmgmFgNoTbC1TCv0%2BDLBjqkAYcCc3noH0ij%2FdyqkiV3Dx%2BB5JpB3%2BewWUXFK2nJ%2FZyh0ieaU9PACevcaKSS8JhTyYkcuJzWjxECPJLuycQB480Rq6RtH%2BhCsp9b%2FG5YaJckB6QX07raAmVAoe9kvfqneLCSWxpasaTonHOK7dxFnH9KSZ1HDy2xKE35os12E%2BHsQBAzIIDksXYcVKslXWEmfewciEDREBeo7KQ%2B5qJ4IQcQQyoU&X-Amz-Signature=1b773524ae8dc3f8ee9cf00ca22ca7866995c1e042a7348a98571297621374b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637524GIP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKo5xd1Mw5%2FIhF5bkonpQMGMz8s5kqm8OavvsK44dROgIhALX0tHdRVVaWCkxJhlJx1Kdz%2FtDnUMiR%2BCnGLxwGe4MmKv8DCEwQABoMNjM3NDIzMTgzODA1IgyiQixJzsbIcUkyf%2FYq3AO4iOxBCAtRCLs7hAlTMAGdbYkntBDUqoEUKGNRy9DIR%2ByfDUgSyUpLSchf3BNc1PtWx6XGsLYEhSknC2cE0TH0UJHJ9YRCNAIEHJvlSSC1CfiRw5vDIEYL3RPj2c%2BDl4vGdP7wo7ivu6g4yT4Hi53z7axQ7%2BH%2FFe9bsaJGUNTWOB%2FeZ1S2TH4SkaIKMoWPu69b8wx8ANevU6gGd4cTOkarf8zY3T9TiDeyBzyy5vR%2BqEtUkSH5EgM%2Fr9aO7UovYk20XpcYr0WL2XBiZyuIiV2YfNjeXP%2FHHuGEuVbiXfg8bgphAexKZ0eZvUJv0afmGJxC7pjFmsJqO5ik67uahAypT0vwGUoeztJCZFOb8nViAktLalNRVmJlpHFLTc2N%2BN%2Bl3RSf1uG7LgFS3o%2BFxwOX%2BwIHQCBe%2BfPz6G%2BM3e8HdefFW6%2FoYgV%2BhI1DFIi%2B0J3fTR9SncGgYYPE9aaCXG7sbNUPrMs3gmQTUis2K7rppoFMYKxKm5DfugTJbUbwbrmKZ0W8j36WK2tcFqvxZSXGARXBzffWRPgBgDIN%2FvID5SCtVgiIkbU3kvMzjiijzu7HL3OHjcWkb22c8pXCpa1XM46OHyANUd8UyCGtU72r9GunehmgmFgNoTbC1TCv0%2BDLBjqkAYcCc3noH0ij%2FdyqkiV3Dx%2BB5JpB3%2BewWUXFK2nJ%2FZyh0ieaU9PACevcaKSS8JhTyYkcuJzWjxECPJLuycQB480Rq6RtH%2BhCsp9b%2FG5YaJckB6QX07raAmVAoe9kvfqneLCSWxpasaTonHOK7dxFnH9KSZ1HDy2xKE35os12E%2BHsQBAzIIDksXYcVKslXWEmfewciEDREBeo7KQ%2B5qJ4IQcQQyoU&X-Amz-Signature=0f4968d49a8dcbc41df9c90e2295aefc1e15fcf254ca1da781e689279ebec51f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637524GIP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKo5xd1Mw5%2FIhF5bkonpQMGMz8s5kqm8OavvsK44dROgIhALX0tHdRVVaWCkxJhlJx1Kdz%2FtDnUMiR%2BCnGLxwGe4MmKv8DCEwQABoMNjM3NDIzMTgzODA1IgyiQixJzsbIcUkyf%2FYq3AO4iOxBCAtRCLs7hAlTMAGdbYkntBDUqoEUKGNRy9DIR%2ByfDUgSyUpLSchf3BNc1PtWx6XGsLYEhSknC2cE0TH0UJHJ9YRCNAIEHJvlSSC1CfiRw5vDIEYL3RPj2c%2BDl4vGdP7wo7ivu6g4yT4Hi53z7axQ7%2BH%2FFe9bsaJGUNTWOB%2FeZ1S2TH4SkaIKMoWPu69b8wx8ANevU6gGd4cTOkarf8zY3T9TiDeyBzyy5vR%2BqEtUkSH5EgM%2Fr9aO7UovYk20XpcYr0WL2XBiZyuIiV2YfNjeXP%2FHHuGEuVbiXfg8bgphAexKZ0eZvUJv0afmGJxC7pjFmsJqO5ik67uahAypT0vwGUoeztJCZFOb8nViAktLalNRVmJlpHFLTc2N%2BN%2Bl3RSf1uG7LgFS3o%2BFxwOX%2BwIHQCBe%2BfPz6G%2BM3e8HdefFW6%2FoYgV%2BhI1DFIi%2B0J3fTR9SncGgYYPE9aaCXG7sbNUPrMs3gmQTUis2K7rppoFMYKxKm5DfugTJbUbwbrmKZ0W8j36WK2tcFqvxZSXGARXBzffWRPgBgDIN%2FvID5SCtVgiIkbU3kvMzjiijzu7HL3OHjcWkb22c8pXCpa1XM46OHyANUd8UyCGtU72r9GunehmgmFgNoTbC1TCv0%2BDLBjqkAYcCc3noH0ij%2FdyqkiV3Dx%2BB5JpB3%2BewWUXFK2nJ%2FZyh0ieaU9PACevcaKSS8JhTyYkcuJzWjxECPJLuycQB480Rq6RtH%2BhCsp9b%2FG5YaJckB6QX07raAmVAoe9kvfqneLCSWxpasaTonHOK7dxFnH9KSZ1HDy2xKE35os12E%2BHsQBAzIIDksXYcVKslXWEmfewciEDREBeo7KQ%2B5qJ4IQcQQyoU&X-Amz-Signature=d08044eea92434d4b650e95cb65396b750c71c1f814d3d5105813be18c70e22b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637524GIP%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKo5xd1Mw5%2FIhF5bkonpQMGMz8s5kqm8OavvsK44dROgIhALX0tHdRVVaWCkxJhlJx1Kdz%2FtDnUMiR%2BCnGLxwGe4MmKv8DCEwQABoMNjM3NDIzMTgzODA1IgyiQixJzsbIcUkyf%2FYq3AO4iOxBCAtRCLs7hAlTMAGdbYkntBDUqoEUKGNRy9DIR%2ByfDUgSyUpLSchf3BNc1PtWx6XGsLYEhSknC2cE0TH0UJHJ9YRCNAIEHJvlSSC1CfiRw5vDIEYL3RPj2c%2BDl4vGdP7wo7ivu6g4yT4Hi53z7axQ7%2BH%2FFe9bsaJGUNTWOB%2FeZ1S2TH4SkaIKMoWPu69b8wx8ANevU6gGd4cTOkarf8zY3T9TiDeyBzyy5vR%2BqEtUkSH5EgM%2Fr9aO7UovYk20XpcYr0WL2XBiZyuIiV2YfNjeXP%2FHHuGEuVbiXfg8bgphAexKZ0eZvUJv0afmGJxC7pjFmsJqO5ik67uahAypT0vwGUoeztJCZFOb8nViAktLalNRVmJlpHFLTc2N%2BN%2Bl3RSf1uG7LgFS3o%2BFxwOX%2BwIHQCBe%2BfPz6G%2BM3e8HdefFW6%2FoYgV%2BhI1DFIi%2B0J3fTR9SncGgYYPE9aaCXG7sbNUPrMs3gmQTUis2K7rppoFMYKxKm5DfugTJbUbwbrmKZ0W8j36WK2tcFqvxZSXGARXBzffWRPgBgDIN%2FvID5SCtVgiIkbU3kvMzjiijzu7HL3OHjcWkb22c8pXCpa1XM46OHyANUd8UyCGtU72r9GunehmgmFgNoTbC1TCv0%2BDLBjqkAYcCc3noH0ij%2FdyqkiV3Dx%2BB5JpB3%2BewWUXFK2nJ%2FZyh0ieaU9PACevcaKSS8JhTyYkcuJzWjxECPJLuycQB480Rq6RtH%2BhCsp9b%2FG5YaJckB6QX07raAmVAoe9kvfqneLCSWxpasaTonHOK7dxFnH9KSZ1HDy2xKE35os12E%2BHsQBAzIIDksXYcVKslXWEmfewciEDREBeo7KQ%2B5qJ4IQcQQyoU&X-Amz-Signature=722d4a4b82b74fd6fe13bb27bbd645f0e224986acf30bb17a2fe84b4160626e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



