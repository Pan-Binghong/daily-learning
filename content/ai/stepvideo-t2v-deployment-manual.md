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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSH3BALK%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDRQiyB4xiTFvD0WdG2JaVH%2BD%2Fb2Cu2diLw4kYNStzWqAIhAKS7DsJ3bYCPSnjYiiwfuqzALP0MQwCDBY8XfFFeQb1DKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxc8RBIaBkwHPdlWNMq3AMKpSoJhx1upWvcfgmN4Cdb%2BFCLNAjmAoSUJoBX4t80DXTkn5kii40J7nCkGjO6lTrab%2FN%2F02NNrdZZRoeWYbOGevwroL%2BuaVlbqBxsAKNqiOJ%2B8te17Rsfyfbl%2FxDWE8yRUVcfsDmF4eDl%2FJ%2BXdWzJ2P5ozsm4pfuY%2FrVMtnJLpGJkKCvCiOTJKxOMrKhhnEZP3Jn4MSFEfqAA0aZflsWvQIHiqr276kzFfWi9UTRew0TahRmKfQqJ83Lt%2Bv6DftvlJ5xoqhFrHqzbv9hjSjKaK%2FMOXtXpScEP8DlBEjVZBNznl9HuMi7ZhNPQHVDEGl96SpZtM%2FQetnKBqyaLtKo%2Ftsf6bRsZzJVt29PS2tM1rezfOHsTgnyR8KocfFCgKgguvWlzgh3fZpaMxa61WXShQ2yt45RnoiNK23EWGcvaSyg2QgDPUTLjndPtb7sh%2B5cB4orbaAXtUzLRA%2FrOnVtN0XkLgHN%2BFSzWWcBONVf5GF5H7%2BGByQqmDYUoKjRAUXYb0C2FSBj6JiafiIOSAs%2F4QB4gFSwUacmhcZwgnx1t24PYRoe0c0v%2F8MuLwfNTXN4NPseG0yrS91mzSKhhCLaR3ryD5PRNKM0CN%2B1V%2FwbrM3Qr5f8JV1xvT9o6azCZ95DLBjqkAR2ovdQX7XGJWM71HC%2Bs0gyReOsymLnMD7LCNcX5fxeZTeLOtSwiR3q%2FOb8N8RSbj7uQPQ4KKO5NQZFfC3VgrPZ3beWuqo8DXEScLqhPV%2F5f8G0sPqvqWo%2B9GS1bA9g1F79Z53N%2F5tcBx1xVqvQe573YREPq2muNv4mIO%2BxCYx%2Bet47BavRw%2BuJrkPizOJFnR%2FX8jwgUnNkHTo0BN1pX94JFKl68&X-Amz-Signature=80b917458912a993e79c1e1c6de3651fa2b06616da97d95dbfbb4028aa5dd359&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSH3BALK%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDRQiyB4xiTFvD0WdG2JaVH%2BD%2Fb2Cu2diLw4kYNStzWqAIhAKS7DsJ3bYCPSnjYiiwfuqzALP0MQwCDBY8XfFFeQb1DKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxc8RBIaBkwHPdlWNMq3AMKpSoJhx1upWvcfgmN4Cdb%2BFCLNAjmAoSUJoBX4t80DXTkn5kii40J7nCkGjO6lTrab%2FN%2F02NNrdZZRoeWYbOGevwroL%2BuaVlbqBxsAKNqiOJ%2B8te17Rsfyfbl%2FxDWE8yRUVcfsDmF4eDl%2FJ%2BXdWzJ2P5ozsm4pfuY%2FrVMtnJLpGJkKCvCiOTJKxOMrKhhnEZP3Jn4MSFEfqAA0aZflsWvQIHiqr276kzFfWi9UTRew0TahRmKfQqJ83Lt%2Bv6DftvlJ5xoqhFrHqzbv9hjSjKaK%2FMOXtXpScEP8DlBEjVZBNznl9HuMi7ZhNPQHVDEGl96SpZtM%2FQetnKBqyaLtKo%2Ftsf6bRsZzJVt29PS2tM1rezfOHsTgnyR8KocfFCgKgguvWlzgh3fZpaMxa61WXShQ2yt45RnoiNK23EWGcvaSyg2QgDPUTLjndPtb7sh%2B5cB4orbaAXtUzLRA%2FrOnVtN0XkLgHN%2BFSzWWcBONVf5GF5H7%2BGByQqmDYUoKjRAUXYb0C2FSBj6JiafiIOSAs%2F4QB4gFSwUacmhcZwgnx1t24PYRoe0c0v%2F8MuLwfNTXN4NPseG0yrS91mzSKhhCLaR3ryD5PRNKM0CN%2B1V%2FwbrM3Qr5f8JV1xvT9o6azCZ95DLBjqkAR2ovdQX7XGJWM71HC%2Bs0gyReOsymLnMD7LCNcX5fxeZTeLOtSwiR3q%2FOb8N8RSbj7uQPQ4KKO5NQZFfC3VgrPZ3beWuqo8DXEScLqhPV%2F5f8G0sPqvqWo%2B9GS1bA9g1F79Z53N%2F5tcBx1xVqvQe573YREPq2muNv4mIO%2BxCYx%2Bet47BavRw%2BuJrkPizOJFnR%2FX8jwgUnNkHTo0BN1pX94JFKl68&X-Amz-Signature=42b1c388d4b36d21b1333bc0076ecb287ec42f39dd2eda3ec1a0d2554ee3f944&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSH3BALK%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDRQiyB4xiTFvD0WdG2JaVH%2BD%2Fb2Cu2diLw4kYNStzWqAIhAKS7DsJ3bYCPSnjYiiwfuqzALP0MQwCDBY8XfFFeQb1DKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxc8RBIaBkwHPdlWNMq3AMKpSoJhx1upWvcfgmN4Cdb%2BFCLNAjmAoSUJoBX4t80DXTkn5kii40J7nCkGjO6lTrab%2FN%2F02NNrdZZRoeWYbOGevwroL%2BuaVlbqBxsAKNqiOJ%2B8te17Rsfyfbl%2FxDWE8yRUVcfsDmF4eDl%2FJ%2BXdWzJ2P5ozsm4pfuY%2FrVMtnJLpGJkKCvCiOTJKxOMrKhhnEZP3Jn4MSFEfqAA0aZflsWvQIHiqr276kzFfWi9UTRew0TahRmKfQqJ83Lt%2Bv6DftvlJ5xoqhFrHqzbv9hjSjKaK%2FMOXtXpScEP8DlBEjVZBNznl9HuMi7ZhNPQHVDEGl96SpZtM%2FQetnKBqyaLtKo%2Ftsf6bRsZzJVt29PS2tM1rezfOHsTgnyR8KocfFCgKgguvWlzgh3fZpaMxa61WXShQ2yt45RnoiNK23EWGcvaSyg2QgDPUTLjndPtb7sh%2B5cB4orbaAXtUzLRA%2FrOnVtN0XkLgHN%2BFSzWWcBONVf5GF5H7%2BGByQqmDYUoKjRAUXYb0C2FSBj6JiafiIOSAs%2F4QB4gFSwUacmhcZwgnx1t24PYRoe0c0v%2F8MuLwfNTXN4NPseG0yrS91mzSKhhCLaR3ryD5PRNKM0CN%2B1V%2FwbrM3Qr5f8JV1xvT9o6azCZ95DLBjqkAR2ovdQX7XGJWM71HC%2Bs0gyReOsymLnMD7LCNcX5fxeZTeLOtSwiR3q%2FOb8N8RSbj7uQPQ4KKO5NQZFfC3VgrPZ3beWuqo8DXEScLqhPV%2F5f8G0sPqvqWo%2B9GS1bA9g1F79Z53N%2F5tcBx1xVqvQe573YREPq2muNv4mIO%2BxCYx%2Bet47BavRw%2BuJrkPizOJFnR%2FX8jwgUnNkHTo0BN1pX94JFKl68&X-Amz-Signature=63eab30a177bca62725e0d5c058902fa5c2bc90ce8fb3b32e294ad94e370dad8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSH3BALK%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDRQiyB4xiTFvD0WdG2JaVH%2BD%2Fb2Cu2diLw4kYNStzWqAIhAKS7DsJ3bYCPSnjYiiwfuqzALP0MQwCDBY8XfFFeQb1DKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxc8RBIaBkwHPdlWNMq3AMKpSoJhx1upWvcfgmN4Cdb%2BFCLNAjmAoSUJoBX4t80DXTkn5kii40J7nCkGjO6lTrab%2FN%2F02NNrdZZRoeWYbOGevwroL%2BuaVlbqBxsAKNqiOJ%2B8te17Rsfyfbl%2FxDWE8yRUVcfsDmF4eDl%2FJ%2BXdWzJ2P5ozsm4pfuY%2FrVMtnJLpGJkKCvCiOTJKxOMrKhhnEZP3Jn4MSFEfqAA0aZflsWvQIHiqr276kzFfWi9UTRew0TahRmKfQqJ83Lt%2Bv6DftvlJ5xoqhFrHqzbv9hjSjKaK%2FMOXtXpScEP8DlBEjVZBNznl9HuMi7ZhNPQHVDEGl96SpZtM%2FQetnKBqyaLtKo%2Ftsf6bRsZzJVt29PS2tM1rezfOHsTgnyR8KocfFCgKgguvWlzgh3fZpaMxa61WXShQ2yt45RnoiNK23EWGcvaSyg2QgDPUTLjndPtb7sh%2B5cB4orbaAXtUzLRA%2FrOnVtN0XkLgHN%2BFSzWWcBONVf5GF5H7%2BGByQqmDYUoKjRAUXYb0C2FSBj6JiafiIOSAs%2F4QB4gFSwUacmhcZwgnx1t24PYRoe0c0v%2F8MuLwfNTXN4NPseG0yrS91mzSKhhCLaR3ryD5PRNKM0CN%2B1V%2FwbrM3Qr5f8JV1xvT9o6azCZ95DLBjqkAR2ovdQX7XGJWM71HC%2Bs0gyReOsymLnMD7LCNcX5fxeZTeLOtSwiR3q%2FOb8N8RSbj7uQPQ4KKO5NQZFfC3VgrPZ3beWuqo8DXEScLqhPV%2F5f8G0sPqvqWo%2B9GS1bA9g1F79Z53N%2F5tcBx1xVqvQe573YREPq2muNv4mIO%2BxCYx%2Bet47BavRw%2BuJrkPizOJFnR%2FX8jwgUnNkHTo0BN1pX94JFKl68&X-Amz-Signature=f9d48f9a0d792b5ada79eb1a572b9dfacd98339616f15a801d49ceec0ac0fa93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



