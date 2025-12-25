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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGBR2PT%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCX6hVf0e2xIUQwxs5Lv006TaTtKSGAMGT3mpnqmZ8d3wIgLGXAd7%2BDW8odKMrUHnLsHCN8g5FmwL4cXFFVvt8xaVMq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDG7mXY5lO01xNfi7ayrcA0vRdlzqHZ1qRHb3e%2BnbYyzI3ZA6lNvfBXZ5bfXAv%2FqJuLiLDIeuPkl7VGHQYuYu9YRM%2B5ILsJGkvbtDPQdbhuLNY%2F5cEUTB%2FGiTJUJPV0KgKC6VQPuNp3T0DLBlJvCeGAomJKKEmZOWnU%2B82UZCh05z5KFL6VdFv1%2FmTN0BVF6CBlNyr8u94k%2F4z%2B0PI3KOcsCcBndIrh5RVev9JIH5n%2FZu4RLWmESc3gLvO75reRd%2Badwxqo06tX18BNAdnfsl9rd%2FIEU83oxCAL03Frj%2FG9y%2FeFMbDWa0lhIxvqeL%2Bx1otLh3nlJogzoMQEHDjPFepHgVJ7FusTtXB0vJ5C0efLbQZ1srvAXyTYZ%2BUk%2BbJZ9gvGvzhJidG0d6lF%2BBu4vh0WzmpximSxw7Ha6i0SDAY2kWxEvTzTPkgd7jjgUKogjFaABGQlKtxZnKWC2fjO7eA91kDheSETKGzM5un%2FCoPMFdeJoV8jBzzk5AJBMfre1dpT4F390vXTOodhckO84%2BOIieaXejiqxf0xdkPTvK7E8FR5FNGzXWf5wkK1j4VFxAxgkliNY%2FEfaTB5mtgGZMY3w8TGoOi%2B2D5WeGHHJIvWMafiFLaQaI469pFVcPL8WPsHH07PdOK4GZ99HKMNebssoGOqUBMciPyW%2BaA00NF2Ff89xtAmjtBXkCEaa%2BaIsm2pYLYfg6k%2FV5Dv2c4HokgKt2AQo0ylMnU%2BTPW%2BJRYeHHiXWeav3C8aNvJx%2BEZ1d84qf88aGda8%2BIFlHZ0Q4SyniDwfvgPSysInhGcSAg1%2B9kI3yN6vnWWhzh4SJg%2BipJb90oXUEcxG%2F0XqDqejzF2ATVUiOrDkXAxxa23qOcPQRBH9qKyTqsOpgG&X-Amz-Signature=31dafdf43ef9acd6ea6a7f707fbfcdff87d85c2d5d46ca47da84636ed979e70f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGBR2PT%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCX6hVf0e2xIUQwxs5Lv006TaTtKSGAMGT3mpnqmZ8d3wIgLGXAd7%2BDW8odKMrUHnLsHCN8g5FmwL4cXFFVvt8xaVMq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDG7mXY5lO01xNfi7ayrcA0vRdlzqHZ1qRHb3e%2BnbYyzI3ZA6lNvfBXZ5bfXAv%2FqJuLiLDIeuPkl7VGHQYuYu9YRM%2B5ILsJGkvbtDPQdbhuLNY%2F5cEUTB%2FGiTJUJPV0KgKC6VQPuNp3T0DLBlJvCeGAomJKKEmZOWnU%2B82UZCh05z5KFL6VdFv1%2FmTN0BVF6CBlNyr8u94k%2F4z%2B0PI3KOcsCcBndIrh5RVev9JIH5n%2FZu4RLWmESc3gLvO75reRd%2Badwxqo06tX18BNAdnfsl9rd%2FIEU83oxCAL03Frj%2FG9y%2FeFMbDWa0lhIxvqeL%2Bx1otLh3nlJogzoMQEHDjPFepHgVJ7FusTtXB0vJ5C0efLbQZ1srvAXyTYZ%2BUk%2BbJZ9gvGvzhJidG0d6lF%2BBu4vh0WzmpximSxw7Ha6i0SDAY2kWxEvTzTPkgd7jjgUKogjFaABGQlKtxZnKWC2fjO7eA91kDheSETKGzM5un%2FCoPMFdeJoV8jBzzk5AJBMfre1dpT4F390vXTOodhckO84%2BOIieaXejiqxf0xdkPTvK7E8FR5FNGzXWf5wkK1j4VFxAxgkliNY%2FEfaTB5mtgGZMY3w8TGoOi%2B2D5WeGHHJIvWMafiFLaQaI469pFVcPL8WPsHH07PdOK4GZ99HKMNebssoGOqUBMciPyW%2BaA00NF2Ff89xtAmjtBXkCEaa%2BaIsm2pYLYfg6k%2FV5Dv2c4HokgKt2AQo0ylMnU%2BTPW%2BJRYeHHiXWeav3C8aNvJx%2BEZ1d84qf88aGda8%2BIFlHZ0Q4SyniDwfvgPSysInhGcSAg1%2B9kI3yN6vnWWhzh4SJg%2BipJb90oXUEcxG%2F0XqDqejzF2ATVUiOrDkXAxxa23qOcPQRBH9qKyTqsOpgG&X-Amz-Signature=6552bac02ca7a29ba95c50fd6fe93b7c217d7dafbdba373e1c3f23e78994ee72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGBR2PT%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCX6hVf0e2xIUQwxs5Lv006TaTtKSGAMGT3mpnqmZ8d3wIgLGXAd7%2BDW8odKMrUHnLsHCN8g5FmwL4cXFFVvt8xaVMq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDG7mXY5lO01xNfi7ayrcA0vRdlzqHZ1qRHb3e%2BnbYyzI3ZA6lNvfBXZ5bfXAv%2FqJuLiLDIeuPkl7VGHQYuYu9YRM%2B5ILsJGkvbtDPQdbhuLNY%2F5cEUTB%2FGiTJUJPV0KgKC6VQPuNp3T0DLBlJvCeGAomJKKEmZOWnU%2B82UZCh05z5KFL6VdFv1%2FmTN0BVF6CBlNyr8u94k%2F4z%2B0PI3KOcsCcBndIrh5RVev9JIH5n%2FZu4RLWmESc3gLvO75reRd%2Badwxqo06tX18BNAdnfsl9rd%2FIEU83oxCAL03Frj%2FG9y%2FeFMbDWa0lhIxvqeL%2Bx1otLh3nlJogzoMQEHDjPFepHgVJ7FusTtXB0vJ5C0efLbQZ1srvAXyTYZ%2BUk%2BbJZ9gvGvzhJidG0d6lF%2BBu4vh0WzmpximSxw7Ha6i0SDAY2kWxEvTzTPkgd7jjgUKogjFaABGQlKtxZnKWC2fjO7eA91kDheSETKGzM5un%2FCoPMFdeJoV8jBzzk5AJBMfre1dpT4F390vXTOodhckO84%2BOIieaXejiqxf0xdkPTvK7E8FR5FNGzXWf5wkK1j4VFxAxgkliNY%2FEfaTB5mtgGZMY3w8TGoOi%2B2D5WeGHHJIvWMafiFLaQaI469pFVcPL8WPsHH07PdOK4GZ99HKMNebssoGOqUBMciPyW%2BaA00NF2Ff89xtAmjtBXkCEaa%2BaIsm2pYLYfg6k%2FV5Dv2c4HokgKt2AQo0ylMnU%2BTPW%2BJRYeHHiXWeav3C8aNvJx%2BEZ1d84qf88aGda8%2BIFlHZ0Q4SyniDwfvgPSysInhGcSAg1%2B9kI3yN6vnWWhzh4SJg%2BipJb90oXUEcxG%2F0XqDqejzF2ATVUiOrDkXAxxa23qOcPQRBH9qKyTqsOpgG&X-Amz-Signature=7ab2175c4743fb10a1db0e18130d852dee67cff1f0359bcfae9656c7ea249285&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGBR2PT%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCX6hVf0e2xIUQwxs5Lv006TaTtKSGAMGT3mpnqmZ8d3wIgLGXAd7%2BDW8odKMrUHnLsHCN8g5FmwL4cXFFVvt8xaVMq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDG7mXY5lO01xNfi7ayrcA0vRdlzqHZ1qRHb3e%2BnbYyzI3ZA6lNvfBXZ5bfXAv%2FqJuLiLDIeuPkl7VGHQYuYu9YRM%2B5ILsJGkvbtDPQdbhuLNY%2F5cEUTB%2FGiTJUJPV0KgKC6VQPuNp3T0DLBlJvCeGAomJKKEmZOWnU%2B82UZCh05z5KFL6VdFv1%2FmTN0BVF6CBlNyr8u94k%2F4z%2B0PI3KOcsCcBndIrh5RVev9JIH5n%2FZu4RLWmESc3gLvO75reRd%2Badwxqo06tX18BNAdnfsl9rd%2FIEU83oxCAL03Frj%2FG9y%2FeFMbDWa0lhIxvqeL%2Bx1otLh3nlJogzoMQEHDjPFepHgVJ7FusTtXB0vJ5C0efLbQZ1srvAXyTYZ%2BUk%2BbJZ9gvGvzhJidG0d6lF%2BBu4vh0WzmpximSxw7Ha6i0SDAY2kWxEvTzTPkgd7jjgUKogjFaABGQlKtxZnKWC2fjO7eA91kDheSETKGzM5un%2FCoPMFdeJoV8jBzzk5AJBMfre1dpT4F390vXTOodhckO84%2BOIieaXejiqxf0xdkPTvK7E8FR5FNGzXWf5wkK1j4VFxAxgkliNY%2FEfaTB5mtgGZMY3w8TGoOi%2B2D5WeGHHJIvWMafiFLaQaI469pFVcPL8WPsHH07PdOK4GZ99HKMNebssoGOqUBMciPyW%2BaA00NF2Ff89xtAmjtBXkCEaa%2BaIsm2pYLYfg6k%2FV5Dv2c4HokgKt2AQo0ylMnU%2BTPW%2BJRYeHHiXWeav3C8aNvJx%2BEZ1d84qf88aGda8%2BIFlHZ0Q4SyniDwfvgPSysInhGcSAg1%2B9kI3yN6vnWWhzh4SJg%2BipJb90oXUEcxG%2F0XqDqejzF2ATVUiOrDkXAxxa23qOcPQRBH9qKyTqsOpgG&X-Amz-Signature=2b175a847e0c4a59baa21fe189fbfde7f348e7a3f3881dbea0205ec973aa1e1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



