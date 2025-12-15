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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFJ64PPP%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCzDtAbRfJA5E9yDhnZI%2BhqJJl5L8n5L758yXomAFPFvgIhAMLk5U2xTiwVovl4wm9L64j8o7u%2FBNcFlTCBs%2BIfiL3gKv8DCD8QABoMNjM3NDIzMTgzODA1IgzRHH8yHTgKzOhjZ%2Bwq3ANVB5Nm6nkDkdbpdm2RXUwjepF3kHpwmLWz%2FmkLi4pRSgAVL9D7m53dGv8y0doJP4cxpNBAJwsZu04yGm3%2BBRT97Bk6%2FChE8FV87QUQMrgKDa%2BPTI796H%2B5ed11sVEguDzJt0Hmku%2BLg6xlLvfUNl9M3xB3Zn%2FN6ShEpAHfa5ZaIDa9YCSdfxW9LeGN%2FsnPewvZfTKkfoK7U1%2FFHP85xWMc%2BZXkQuvXPV4Cl14Zwn7VxCuzDV%2BgEqcYpMDDgYeOi0Qo%2FPzSMbg29RXzWgA%2BmM9y1m0GWbRR9VJQI1V7btIEvwVSEgRlNHAlPoUBk10aVqsD0YpA3tgGFzCJ7RhdloNur6PGiZzjbU43Fz6%2BALdTkpQpPP9LOR3qmGNSXE4mW3SSR7VJSPVuuxuJVfn7GRkjj392yvWeBUSMu9HNfxzueCEcF5FX340f8u3k8zSb%2BjgIlOh%2B%2BcVqHhmE0%2FF9eqlYwVh9a0STn1SDa%2FBn0v1IOhBll7af5NhRq5jRErYw6esUgSKU7A0T%2BSQoLiYvSAG1Pp2Wr2s0qXIKX%2FmYAUtInqwViVFvHNc78RHRqwwmm8YztnfHJ5TeL76GCf0u4F3my2fCIRZ2kPy9nbIeQdU6OBcEhNq3trbejEb26zDJ2%2FzJBjqkAfDbSBi0Cl12dwhi6163an9KXqp%2FPbKdGBBZzImbx9J9KN675fMGuxDfSrz8ybP54WzZYf7nB7x%2FX5DJS%2Bf1bXhcGtmwfisuSaRrpTl70gVtK2TTG42t8NR9GUw7qybClhnAbJIC7aGOpSbfefvO8gAXA0cNG7Y8k0%2BwAy98XzIdXWY6RPF0MB6YzzGencZ3AsgiGY5vrn44mcbS9dgYewGeMPXP&X-Amz-Signature=54d3b9c5d73acea9a522ee21cba9bd7062e81bce63dfaaf2a0e20c65739c5dc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFJ64PPP%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCzDtAbRfJA5E9yDhnZI%2BhqJJl5L8n5L758yXomAFPFvgIhAMLk5U2xTiwVovl4wm9L64j8o7u%2FBNcFlTCBs%2BIfiL3gKv8DCD8QABoMNjM3NDIzMTgzODA1IgzRHH8yHTgKzOhjZ%2Bwq3ANVB5Nm6nkDkdbpdm2RXUwjepF3kHpwmLWz%2FmkLi4pRSgAVL9D7m53dGv8y0doJP4cxpNBAJwsZu04yGm3%2BBRT97Bk6%2FChE8FV87QUQMrgKDa%2BPTI796H%2B5ed11sVEguDzJt0Hmku%2BLg6xlLvfUNl9M3xB3Zn%2FN6ShEpAHfa5ZaIDa9YCSdfxW9LeGN%2FsnPewvZfTKkfoK7U1%2FFHP85xWMc%2BZXkQuvXPV4Cl14Zwn7VxCuzDV%2BgEqcYpMDDgYeOi0Qo%2FPzSMbg29RXzWgA%2BmM9y1m0GWbRR9VJQI1V7btIEvwVSEgRlNHAlPoUBk10aVqsD0YpA3tgGFzCJ7RhdloNur6PGiZzjbU43Fz6%2BALdTkpQpPP9LOR3qmGNSXE4mW3SSR7VJSPVuuxuJVfn7GRkjj392yvWeBUSMu9HNfxzueCEcF5FX340f8u3k8zSb%2BjgIlOh%2B%2BcVqHhmE0%2FF9eqlYwVh9a0STn1SDa%2FBn0v1IOhBll7af5NhRq5jRErYw6esUgSKU7A0T%2BSQoLiYvSAG1Pp2Wr2s0qXIKX%2FmYAUtInqwViVFvHNc78RHRqwwmm8YztnfHJ5TeL76GCf0u4F3my2fCIRZ2kPy9nbIeQdU6OBcEhNq3trbejEb26zDJ2%2FzJBjqkAfDbSBi0Cl12dwhi6163an9KXqp%2FPbKdGBBZzImbx9J9KN675fMGuxDfSrz8ybP54WzZYf7nB7x%2FX5DJS%2Bf1bXhcGtmwfisuSaRrpTl70gVtK2TTG42t8NR9GUw7qybClhnAbJIC7aGOpSbfefvO8gAXA0cNG7Y8k0%2BwAy98XzIdXWY6RPF0MB6YzzGencZ3AsgiGY5vrn44mcbS9dgYewGeMPXP&X-Amz-Signature=238c94b086021b8974da72a763d49a9cb621b6816993166cc03e46c8906b1133&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFJ64PPP%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCzDtAbRfJA5E9yDhnZI%2BhqJJl5L8n5L758yXomAFPFvgIhAMLk5U2xTiwVovl4wm9L64j8o7u%2FBNcFlTCBs%2BIfiL3gKv8DCD8QABoMNjM3NDIzMTgzODA1IgzRHH8yHTgKzOhjZ%2Bwq3ANVB5Nm6nkDkdbpdm2RXUwjepF3kHpwmLWz%2FmkLi4pRSgAVL9D7m53dGv8y0doJP4cxpNBAJwsZu04yGm3%2BBRT97Bk6%2FChE8FV87QUQMrgKDa%2BPTI796H%2B5ed11sVEguDzJt0Hmku%2BLg6xlLvfUNl9M3xB3Zn%2FN6ShEpAHfa5ZaIDa9YCSdfxW9LeGN%2FsnPewvZfTKkfoK7U1%2FFHP85xWMc%2BZXkQuvXPV4Cl14Zwn7VxCuzDV%2BgEqcYpMDDgYeOi0Qo%2FPzSMbg29RXzWgA%2BmM9y1m0GWbRR9VJQI1V7btIEvwVSEgRlNHAlPoUBk10aVqsD0YpA3tgGFzCJ7RhdloNur6PGiZzjbU43Fz6%2BALdTkpQpPP9LOR3qmGNSXE4mW3SSR7VJSPVuuxuJVfn7GRkjj392yvWeBUSMu9HNfxzueCEcF5FX340f8u3k8zSb%2BjgIlOh%2B%2BcVqHhmE0%2FF9eqlYwVh9a0STn1SDa%2FBn0v1IOhBll7af5NhRq5jRErYw6esUgSKU7A0T%2BSQoLiYvSAG1Pp2Wr2s0qXIKX%2FmYAUtInqwViVFvHNc78RHRqwwmm8YztnfHJ5TeL76GCf0u4F3my2fCIRZ2kPy9nbIeQdU6OBcEhNq3trbejEb26zDJ2%2FzJBjqkAfDbSBi0Cl12dwhi6163an9KXqp%2FPbKdGBBZzImbx9J9KN675fMGuxDfSrz8ybP54WzZYf7nB7x%2FX5DJS%2Bf1bXhcGtmwfisuSaRrpTl70gVtK2TTG42t8NR9GUw7qybClhnAbJIC7aGOpSbfefvO8gAXA0cNG7Y8k0%2BwAy98XzIdXWY6RPF0MB6YzzGencZ3AsgiGY5vrn44mcbS9dgYewGeMPXP&X-Amz-Signature=b3f0146e1ac9a9df77d4d85158c378191ee56cd5149a3c4cb7d2178419c3ee79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFJ64PPP%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQCzDtAbRfJA5E9yDhnZI%2BhqJJl5L8n5L758yXomAFPFvgIhAMLk5U2xTiwVovl4wm9L64j8o7u%2FBNcFlTCBs%2BIfiL3gKv8DCD8QABoMNjM3NDIzMTgzODA1IgzRHH8yHTgKzOhjZ%2Bwq3ANVB5Nm6nkDkdbpdm2RXUwjepF3kHpwmLWz%2FmkLi4pRSgAVL9D7m53dGv8y0doJP4cxpNBAJwsZu04yGm3%2BBRT97Bk6%2FChE8FV87QUQMrgKDa%2BPTI796H%2B5ed11sVEguDzJt0Hmku%2BLg6xlLvfUNl9M3xB3Zn%2FN6ShEpAHfa5ZaIDa9YCSdfxW9LeGN%2FsnPewvZfTKkfoK7U1%2FFHP85xWMc%2BZXkQuvXPV4Cl14Zwn7VxCuzDV%2BgEqcYpMDDgYeOi0Qo%2FPzSMbg29RXzWgA%2BmM9y1m0GWbRR9VJQI1V7btIEvwVSEgRlNHAlPoUBk10aVqsD0YpA3tgGFzCJ7RhdloNur6PGiZzjbU43Fz6%2BALdTkpQpPP9LOR3qmGNSXE4mW3SSR7VJSPVuuxuJVfn7GRkjj392yvWeBUSMu9HNfxzueCEcF5FX340f8u3k8zSb%2BjgIlOh%2B%2BcVqHhmE0%2FF9eqlYwVh9a0STn1SDa%2FBn0v1IOhBll7af5NhRq5jRErYw6esUgSKU7A0T%2BSQoLiYvSAG1Pp2Wr2s0qXIKX%2FmYAUtInqwViVFvHNc78RHRqwwmm8YztnfHJ5TeL76GCf0u4F3my2fCIRZ2kPy9nbIeQdU6OBcEhNq3trbejEb26zDJ2%2FzJBjqkAfDbSBi0Cl12dwhi6163an9KXqp%2FPbKdGBBZzImbx9J9KN675fMGuxDfSrz8ybP54WzZYf7nB7x%2FX5DJS%2Bf1bXhcGtmwfisuSaRrpTl70gVtK2TTG42t8NR9GUw7qybClhnAbJIC7aGOpSbfefvO8gAXA0cNG7Y8k0%2BwAy98XzIdXWY6RPF0MB6YzzGencZ3AsgiGY5vrn44mcbS9dgYewGeMPXP&X-Amz-Signature=9e735bba1a6a375e829dff94b24aa79df7229ed252f0d8609fb4733463d2fdf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



