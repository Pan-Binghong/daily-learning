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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO7ELUFX%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCh6LqPHbKiJy4RsvsjoH6hgUrwgXS70bZEBzFfMb3MgAIhAMEhqP2Dfbj83ynhB1Q4v8%2Fziel1T4vs3ccRrJvn1YemKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9YK4i0faPw%2Fj2fNUq3AMfUM0OAjU%2FMOXHtZQLGNj6Z20bI4umU0B2EgWOWobMe%2BpYGjhIJghMb8yHlefd2632WogfvxB88e2b3sz4ASXPRzcrsp33HdYOmYxF7mno2l1Uh1veoxTEPN1wUZJ8iON8SDm8aQiv0gf5Bl8blfwwBUEeEyKCBa5CJGcuF0gtB9z6cEK91e%2FrFukfb4L6zOeccKzOGT50bvR7EhbRrmQCszS%2B90YUxyWfGS0rxPl0pPEAlMLVj0qn8os9Si2zRDKWBxUHbWhWu6sO2QnNsa7pfCrf42Mj6H84vGusHNp9%2B8oZf3kaBKH%2FnYNDsjsW1QFgWiXl2xnlq1nVKDLvPGsIhhWMtJTDEQ6ij4pSQMLK0l7dI%2FsjK3LCPrJAS56fKigGX7%2BSBHRMfCe561iaOkQwk49QTepkzyQ%2FguzCgmZqvIIArzf0Lx6k9g4ywhUiq7o7InP80rZZvQcNsxr67N4%2BSMnp0AM%2Fj5e5CR3eNJlX2V0iubgLRdcoY9ftzVFudCdXN4cuDdoHszXM9UIUHfYotlaWkaimwSTnSJlPs%2FqbXE4hGs8E%2FI7dO%2Be3kEk2rZtdltotA%2B0x7W0pyBtS27dV%2FjtQUNNpzzy2STjweeEU9jhY4LVYFj1stCYaMTDk1O3JBjqkAciBsc04W%2BzF%2B0OZUkg7nIxgY%2BXYuSKhFr0q5oS2tLcJe3wGwbUdM%2B%2F1akTo3BZN7W%2F9zgGTfMONIW1B998jQa0O54w2QQjjXhTzsWpkILE5RGOtu6qCel8euHz50EA%2BMQDmveYUBI5IcEeYbn5EAVwv5sQDXXKr9VHbEhIII3x%2Be7FrogmcI9KSSRniRI27EoTtv3WMCtHhDemylAlZjUIO%2F7tI&X-Amz-Signature=b4d6bb57c0ef6a17e9bafefd6a4f498850ac4cdadc321273cb590dbefbcb3f9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO7ELUFX%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCh6LqPHbKiJy4RsvsjoH6hgUrwgXS70bZEBzFfMb3MgAIhAMEhqP2Dfbj83ynhB1Q4v8%2Fziel1T4vs3ccRrJvn1YemKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9YK4i0faPw%2Fj2fNUq3AMfUM0OAjU%2FMOXHtZQLGNj6Z20bI4umU0B2EgWOWobMe%2BpYGjhIJghMb8yHlefd2632WogfvxB88e2b3sz4ASXPRzcrsp33HdYOmYxF7mno2l1Uh1veoxTEPN1wUZJ8iON8SDm8aQiv0gf5Bl8blfwwBUEeEyKCBa5CJGcuF0gtB9z6cEK91e%2FrFukfb4L6zOeccKzOGT50bvR7EhbRrmQCszS%2B90YUxyWfGS0rxPl0pPEAlMLVj0qn8os9Si2zRDKWBxUHbWhWu6sO2QnNsa7pfCrf42Mj6H84vGusHNp9%2B8oZf3kaBKH%2FnYNDsjsW1QFgWiXl2xnlq1nVKDLvPGsIhhWMtJTDEQ6ij4pSQMLK0l7dI%2FsjK3LCPrJAS56fKigGX7%2BSBHRMfCe561iaOkQwk49QTepkzyQ%2FguzCgmZqvIIArzf0Lx6k9g4ywhUiq7o7InP80rZZvQcNsxr67N4%2BSMnp0AM%2Fj5e5CR3eNJlX2V0iubgLRdcoY9ftzVFudCdXN4cuDdoHszXM9UIUHfYotlaWkaimwSTnSJlPs%2FqbXE4hGs8E%2FI7dO%2Be3kEk2rZtdltotA%2B0x7W0pyBtS27dV%2FjtQUNNpzzy2STjweeEU9jhY4LVYFj1stCYaMTDk1O3JBjqkAciBsc04W%2BzF%2B0OZUkg7nIxgY%2BXYuSKhFr0q5oS2tLcJe3wGwbUdM%2B%2F1akTo3BZN7W%2F9zgGTfMONIW1B998jQa0O54w2QQjjXhTzsWpkILE5RGOtu6qCel8euHz50EA%2BMQDmveYUBI5IcEeYbn5EAVwv5sQDXXKr9VHbEhIII3x%2Be7FrogmcI9KSSRniRI27EoTtv3WMCtHhDemylAlZjUIO%2F7tI&X-Amz-Signature=3b80e568d69eb5150300131cf06290062271d4f29efeadf1f7a74751f058a1ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO7ELUFX%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCh6LqPHbKiJy4RsvsjoH6hgUrwgXS70bZEBzFfMb3MgAIhAMEhqP2Dfbj83ynhB1Q4v8%2Fziel1T4vs3ccRrJvn1YemKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9YK4i0faPw%2Fj2fNUq3AMfUM0OAjU%2FMOXHtZQLGNj6Z20bI4umU0B2EgWOWobMe%2BpYGjhIJghMb8yHlefd2632WogfvxB88e2b3sz4ASXPRzcrsp33HdYOmYxF7mno2l1Uh1veoxTEPN1wUZJ8iON8SDm8aQiv0gf5Bl8blfwwBUEeEyKCBa5CJGcuF0gtB9z6cEK91e%2FrFukfb4L6zOeccKzOGT50bvR7EhbRrmQCszS%2B90YUxyWfGS0rxPl0pPEAlMLVj0qn8os9Si2zRDKWBxUHbWhWu6sO2QnNsa7pfCrf42Mj6H84vGusHNp9%2B8oZf3kaBKH%2FnYNDsjsW1QFgWiXl2xnlq1nVKDLvPGsIhhWMtJTDEQ6ij4pSQMLK0l7dI%2FsjK3LCPrJAS56fKigGX7%2BSBHRMfCe561iaOkQwk49QTepkzyQ%2FguzCgmZqvIIArzf0Lx6k9g4ywhUiq7o7InP80rZZvQcNsxr67N4%2BSMnp0AM%2Fj5e5CR3eNJlX2V0iubgLRdcoY9ftzVFudCdXN4cuDdoHszXM9UIUHfYotlaWkaimwSTnSJlPs%2FqbXE4hGs8E%2FI7dO%2Be3kEk2rZtdltotA%2B0x7W0pyBtS27dV%2FjtQUNNpzzy2STjweeEU9jhY4LVYFj1stCYaMTDk1O3JBjqkAciBsc04W%2BzF%2B0OZUkg7nIxgY%2BXYuSKhFr0q5oS2tLcJe3wGwbUdM%2B%2F1akTo3BZN7W%2F9zgGTfMONIW1B998jQa0O54w2QQjjXhTzsWpkILE5RGOtu6qCel8euHz50EA%2BMQDmveYUBI5IcEeYbn5EAVwv5sQDXXKr9VHbEhIII3x%2Be7FrogmcI9KSSRniRI27EoTtv3WMCtHhDemylAlZjUIO%2F7tI&X-Amz-Signature=4254a56e4426c146e5e507fce86815d1d37efffb10f08815091cf118899a46a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO7ELUFX%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCh6LqPHbKiJy4RsvsjoH6hgUrwgXS70bZEBzFfMb3MgAIhAMEhqP2Dfbj83ynhB1Q4v8%2Fziel1T4vs3ccRrJvn1YemKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz9YK4i0faPw%2Fj2fNUq3AMfUM0OAjU%2FMOXHtZQLGNj6Z20bI4umU0B2EgWOWobMe%2BpYGjhIJghMb8yHlefd2632WogfvxB88e2b3sz4ASXPRzcrsp33HdYOmYxF7mno2l1Uh1veoxTEPN1wUZJ8iON8SDm8aQiv0gf5Bl8blfwwBUEeEyKCBa5CJGcuF0gtB9z6cEK91e%2FrFukfb4L6zOeccKzOGT50bvR7EhbRrmQCszS%2B90YUxyWfGS0rxPl0pPEAlMLVj0qn8os9Si2zRDKWBxUHbWhWu6sO2QnNsa7pfCrf42Mj6H84vGusHNp9%2B8oZf3kaBKH%2FnYNDsjsW1QFgWiXl2xnlq1nVKDLvPGsIhhWMtJTDEQ6ij4pSQMLK0l7dI%2FsjK3LCPrJAS56fKigGX7%2BSBHRMfCe561iaOkQwk49QTepkzyQ%2FguzCgmZqvIIArzf0Lx6k9g4ywhUiq7o7InP80rZZvQcNsxr67N4%2BSMnp0AM%2Fj5e5CR3eNJlX2V0iubgLRdcoY9ftzVFudCdXN4cuDdoHszXM9UIUHfYotlaWkaimwSTnSJlPs%2FqbXE4hGs8E%2FI7dO%2Be3kEk2rZtdltotA%2B0x7W0pyBtS27dV%2FjtQUNNpzzy2STjweeEU9jhY4LVYFj1stCYaMTDk1O3JBjqkAciBsc04W%2BzF%2B0OZUkg7nIxgY%2BXYuSKhFr0q5oS2tLcJe3wGwbUdM%2B%2F1akTo3BZN7W%2F9zgGTfMONIW1B998jQa0O54w2QQjjXhTzsWpkILE5RGOtu6qCel8euHz50EA%2BMQDmveYUBI5IcEeYbn5EAVwv5sQDXXKr9VHbEhIII3x%2Be7FrogmcI9KSSRniRI27EoTtv3WMCtHhDemylAlZjUIO%2F7tI&X-Amz-Signature=32b4d9fccefaa6b90865cae4195a4230d550a10642a86d70c099e94cef70f1ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



