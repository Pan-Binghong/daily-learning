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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676JOSDG7%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8kI%2FwxXF%2F9DvodUdi4uK10IZuz1qjD5s22cKjC6bykAiEAmuo16TQysJ%2B9R2O5GekEYiwHkNUACFoHZ6p456NjH2EqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQP%2FCCaDdcVEfJfCyrcA%2BBQMlKSrRFX6yXal4ZvbPpcrkFPuN0ddtv2oLuBGkE49f7%2FZBrliLruw%2FrxKBX70PqOW59Pod1oFWdP9EEhE46t1WlNcl%2Fvt585Me8gnWD1z%2B%2B5mjTWFoAdWXAC8VjM1Gpm7SQQji6weiA61nI0f4gS4Lrs0m9m4ve5rkLD8H9sdQ8F61w3qMVT%2F8WlRPxqixaB%2F%2FORh8TGoP4xKKFoP77UjKkV8prTRMdwZwIL%2BliZSZhyjCQSN7oCQiDgQ0dUXtKblTK%2FrauLNZTgtp4wzqVJGJwEJrxBO4nQtAxfKuh4y3EH4FZPQGLErd251YbpKpZ0P8HI62qTCh0SpdvRu89zPntaZNTBUiMnyqDJ92ntFdyVD3j8tMKqWupqx06pKSgTM50f2hyZdiW93hyTJKE29gMAfoJf3rK99oMLBSvBaTnw5JsQ6jEkNGay%2FScHiMdR3ksdWxcPt3b%2B%2BAJnshtFS6gCk5IXB0VPWe6YZ8MA3FOl0Rik1%2FL0jJzksyKG1aWFHpdA5znSy7HiADq5gGCiXdV7owPgAq2we53k%2Fxnk1ZNrpZODpDjKg6jpRumedt13tuA5bBbMkEQAjYlZpOoXdwQfcYP8g2sYtSOZNj6q%2Ffmvx8zpUoIOu4VrMOmxzM4GOqUBNlIeelxc0a9eA9BoWt2FfcDu5NTUBhXb7HKF%2BnyPxa0T%2BQHwFCNdfS1d%2B0WyiKkEfsl2r4m%2BfaOeB00nMXXFmCNIuKPvcEA%2FalqpaZcVCWe2nA1oRwcRR51fV%2FRr0YexN7jka0MdSZizje503eN6yWlG4DcacvzUxrz4YC61u4N1BWOVMoJ%2BMrVYxLq9i2CzSotGHjC%2B7WCeR4Ux%2BdhYD5M57ro7&X-Amz-Signature=4adf8f3faf7d382a60bee29bfbb1417508a1f5999b90e8fecf9309fcd595c13f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676JOSDG7%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8kI%2FwxXF%2F9DvodUdi4uK10IZuz1qjD5s22cKjC6bykAiEAmuo16TQysJ%2B9R2O5GekEYiwHkNUACFoHZ6p456NjH2EqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQP%2FCCaDdcVEfJfCyrcA%2BBQMlKSrRFX6yXal4ZvbPpcrkFPuN0ddtv2oLuBGkE49f7%2FZBrliLruw%2FrxKBX70PqOW59Pod1oFWdP9EEhE46t1WlNcl%2Fvt585Me8gnWD1z%2B%2B5mjTWFoAdWXAC8VjM1Gpm7SQQji6weiA61nI0f4gS4Lrs0m9m4ve5rkLD8H9sdQ8F61w3qMVT%2F8WlRPxqixaB%2F%2FORh8TGoP4xKKFoP77UjKkV8prTRMdwZwIL%2BliZSZhyjCQSN7oCQiDgQ0dUXtKblTK%2FrauLNZTgtp4wzqVJGJwEJrxBO4nQtAxfKuh4y3EH4FZPQGLErd251YbpKpZ0P8HI62qTCh0SpdvRu89zPntaZNTBUiMnyqDJ92ntFdyVD3j8tMKqWupqx06pKSgTM50f2hyZdiW93hyTJKE29gMAfoJf3rK99oMLBSvBaTnw5JsQ6jEkNGay%2FScHiMdR3ksdWxcPt3b%2B%2BAJnshtFS6gCk5IXB0VPWe6YZ8MA3FOl0Rik1%2FL0jJzksyKG1aWFHpdA5znSy7HiADq5gGCiXdV7owPgAq2we53k%2Fxnk1ZNrpZODpDjKg6jpRumedt13tuA5bBbMkEQAjYlZpOoXdwQfcYP8g2sYtSOZNj6q%2Ffmvx8zpUoIOu4VrMOmxzM4GOqUBNlIeelxc0a9eA9BoWt2FfcDu5NTUBhXb7HKF%2BnyPxa0T%2BQHwFCNdfS1d%2B0WyiKkEfsl2r4m%2BfaOeB00nMXXFmCNIuKPvcEA%2FalqpaZcVCWe2nA1oRwcRR51fV%2FRr0YexN7jka0MdSZizje503eN6yWlG4DcacvzUxrz4YC61u4N1BWOVMoJ%2BMrVYxLq9i2CzSotGHjC%2B7WCeR4Ux%2BdhYD5M57ro7&X-Amz-Signature=ccbcaa69fb7c551b61dd992ffdeb01038c13960623078cb81899e3a4615b9527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676JOSDG7%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8kI%2FwxXF%2F9DvodUdi4uK10IZuz1qjD5s22cKjC6bykAiEAmuo16TQysJ%2B9R2O5GekEYiwHkNUACFoHZ6p456NjH2EqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQP%2FCCaDdcVEfJfCyrcA%2BBQMlKSrRFX6yXal4ZvbPpcrkFPuN0ddtv2oLuBGkE49f7%2FZBrliLruw%2FrxKBX70PqOW59Pod1oFWdP9EEhE46t1WlNcl%2Fvt585Me8gnWD1z%2B%2B5mjTWFoAdWXAC8VjM1Gpm7SQQji6weiA61nI0f4gS4Lrs0m9m4ve5rkLD8H9sdQ8F61w3qMVT%2F8WlRPxqixaB%2F%2FORh8TGoP4xKKFoP77UjKkV8prTRMdwZwIL%2BliZSZhyjCQSN7oCQiDgQ0dUXtKblTK%2FrauLNZTgtp4wzqVJGJwEJrxBO4nQtAxfKuh4y3EH4FZPQGLErd251YbpKpZ0P8HI62qTCh0SpdvRu89zPntaZNTBUiMnyqDJ92ntFdyVD3j8tMKqWupqx06pKSgTM50f2hyZdiW93hyTJKE29gMAfoJf3rK99oMLBSvBaTnw5JsQ6jEkNGay%2FScHiMdR3ksdWxcPt3b%2B%2BAJnshtFS6gCk5IXB0VPWe6YZ8MA3FOl0Rik1%2FL0jJzksyKG1aWFHpdA5znSy7HiADq5gGCiXdV7owPgAq2we53k%2Fxnk1ZNrpZODpDjKg6jpRumedt13tuA5bBbMkEQAjYlZpOoXdwQfcYP8g2sYtSOZNj6q%2Ffmvx8zpUoIOu4VrMOmxzM4GOqUBNlIeelxc0a9eA9BoWt2FfcDu5NTUBhXb7HKF%2BnyPxa0T%2BQHwFCNdfS1d%2B0WyiKkEfsl2r4m%2BfaOeB00nMXXFmCNIuKPvcEA%2FalqpaZcVCWe2nA1oRwcRR51fV%2FRr0YexN7jka0MdSZizje503eN6yWlG4DcacvzUxrz4YC61u4N1BWOVMoJ%2BMrVYxLq9i2CzSotGHjC%2B7WCeR4Ux%2BdhYD5M57ro7&X-Amz-Signature=254d36b34e6db04ed9c23edd35a0977daaabdd84b1df75a1b36df9a7e802dcdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676JOSDG7%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA8kI%2FwxXF%2F9DvodUdi4uK10IZuz1qjD5s22cKjC6bykAiEAmuo16TQysJ%2B9R2O5GekEYiwHkNUACFoHZ6p456NjH2EqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQP%2FCCaDdcVEfJfCyrcA%2BBQMlKSrRFX6yXal4ZvbPpcrkFPuN0ddtv2oLuBGkE49f7%2FZBrliLruw%2FrxKBX70PqOW59Pod1oFWdP9EEhE46t1WlNcl%2Fvt585Me8gnWD1z%2B%2B5mjTWFoAdWXAC8VjM1Gpm7SQQji6weiA61nI0f4gS4Lrs0m9m4ve5rkLD8H9sdQ8F61w3qMVT%2F8WlRPxqixaB%2F%2FORh8TGoP4xKKFoP77UjKkV8prTRMdwZwIL%2BliZSZhyjCQSN7oCQiDgQ0dUXtKblTK%2FrauLNZTgtp4wzqVJGJwEJrxBO4nQtAxfKuh4y3EH4FZPQGLErd251YbpKpZ0P8HI62qTCh0SpdvRu89zPntaZNTBUiMnyqDJ92ntFdyVD3j8tMKqWupqx06pKSgTM50f2hyZdiW93hyTJKE29gMAfoJf3rK99oMLBSvBaTnw5JsQ6jEkNGay%2FScHiMdR3ksdWxcPt3b%2B%2BAJnshtFS6gCk5IXB0VPWe6YZ8MA3FOl0Rik1%2FL0jJzksyKG1aWFHpdA5znSy7HiADq5gGCiXdV7owPgAq2we53k%2Fxnk1ZNrpZODpDjKg6jpRumedt13tuA5bBbMkEQAjYlZpOoXdwQfcYP8g2sYtSOZNj6q%2Ffmvx8zpUoIOu4VrMOmxzM4GOqUBNlIeelxc0a9eA9BoWt2FfcDu5NTUBhXb7HKF%2BnyPxa0T%2BQHwFCNdfS1d%2B0WyiKkEfsl2r4m%2BfaOeB00nMXXFmCNIuKPvcEA%2FalqpaZcVCWe2nA1oRwcRR51fV%2FRr0YexN7jka0MdSZizje503eN6yWlG4DcacvzUxrz4YC61u4N1BWOVMoJ%2BMrVYxLq9i2CzSotGHjC%2B7WCeR4Ux%2BdhYD5M57ro7&X-Amz-Signature=74313c5f3fbac3a9ea99c4c433d8764164c6c9c8dd70a8e55a52b687d80c0a68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



