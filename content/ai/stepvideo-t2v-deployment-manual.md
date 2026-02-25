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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626UQJPM2%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDJ6Co4CapgNhy5dO5MAfz9H2H8MboYjaAG7QeFYvoNjQIgCgFOkX4HC4b47b1V5Ev19OoAuQjAnRspJNg7HxTivpcq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDK26UdSb0DgIdY58rCrcA6RUFTiizJP%2BiUls7JmzYpVae9oQ225BWElnPcyoXyaWpLmlGRFyZYZAXhB8Dxfnh5P6CMmUanju9RrrsCUAM8DEGJ8AGbdYRoRHjxho3EgTw8b%2Fot%2FXKoDc0l6GGNAZ3ZzYV%2FpCRsrND%2F8AMeCTOywPGC%2Bso9lNRhBD4O64%2BJlFZNqGcinYHt1sBzQzKjg5ogG2XIv9JWUJzmDhUJ4l5TauSAYrky7kq0K1Y2o8Hgnw2IYu6AhrSsGbstM5YPKh8K1RV%2BQFwv0cZnk4UAvrGyxCyPw6zZzHBEBFjvAsi0IJsp0KkFIMd9AQMrxXTr52G80hIblO6AbylZFpmc9tVdifWjqJ25qBRbqNv2XJ%2BCaxSYXFWlBjHm41A4X7U63%2Fn9G8nPm2LEsTdjJqAIdjhp1u6yAxasnEGkw3HxEh3rz8sErHv6Z8yi2sIKMTBRWTqT2lm5w0CW4KLT1wjtacxHcLe4XbBadN8ahsnhZyLD3aID5PNW%2FWOoJOQ6fzRNhnB80%2BattCg7HqOsxMZGk8N4g7alpgaTZdMaxZJPBCbl3uuzeRpQ%2Byhrd8FceiwxKx74oFkwkwFO60HzxuBKyucjcdVuvYHvgF6umOutX1e7edfoIYNfLoxj8rP5E8MOOD%2BcwGOqUBogZpmZV1IEMQaWsbCXdJeHfGxo0x%2BtA%2B%2FAhdyjgNob28F98M02GmvcnKJMnZsmcZsMe63vC9LSuyHk3n1%2F%2BahRlmdEEeLtiew3NRG52ojlbS9ygsqqbw%2B3rnkseP6qHsxL2Himy%2FCCP0j8NEJBGnxnM4zX2eIRCrnGDX2E35fCoV3TnEDCx8Y%2Bu3j%2Bbk3udL7laLHXAbXdmPQTcpEqIOcUP89Iqx&X-Amz-Signature=d37ba41a40b5a3e8af6b8c174a3d548216a9259b914de7323f87b0885f89d4ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626UQJPM2%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDJ6Co4CapgNhy5dO5MAfz9H2H8MboYjaAG7QeFYvoNjQIgCgFOkX4HC4b47b1V5Ev19OoAuQjAnRspJNg7HxTivpcq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDK26UdSb0DgIdY58rCrcA6RUFTiizJP%2BiUls7JmzYpVae9oQ225BWElnPcyoXyaWpLmlGRFyZYZAXhB8Dxfnh5P6CMmUanju9RrrsCUAM8DEGJ8AGbdYRoRHjxho3EgTw8b%2Fot%2FXKoDc0l6GGNAZ3ZzYV%2FpCRsrND%2F8AMeCTOywPGC%2Bso9lNRhBD4O64%2BJlFZNqGcinYHt1sBzQzKjg5ogG2XIv9JWUJzmDhUJ4l5TauSAYrky7kq0K1Y2o8Hgnw2IYu6AhrSsGbstM5YPKh8K1RV%2BQFwv0cZnk4UAvrGyxCyPw6zZzHBEBFjvAsi0IJsp0KkFIMd9AQMrxXTr52G80hIblO6AbylZFpmc9tVdifWjqJ25qBRbqNv2XJ%2BCaxSYXFWlBjHm41A4X7U63%2Fn9G8nPm2LEsTdjJqAIdjhp1u6yAxasnEGkw3HxEh3rz8sErHv6Z8yi2sIKMTBRWTqT2lm5w0CW4KLT1wjtacxHcLe4XbBadN8ahsnhZyLD3aID5PNW%2FWOoJOQ6fzRNhnB80%2BattCg7HqOsxMZGk8N4g7alpgaTZdMaxZJPBCbl3uuzeRpQ%2Byhrd8FceiwxKx74oFkwkwFO60HzxuBKyucjcdVuvYHvgF6umOutX1e7edfoIYNfLoxj8rP5E8MOOD%2BcwGOqUBogZpmZV1IEMQaWsbCXdJeHfGxo0x%2BtA%2B%2FAhdyjgNob28F98M02GmvcnKJMnZsmcZsMe63vC9LSuyHk3n1%2F%2BahRlmdEEeLtiew3NRG52ojlbS9ygsqqbw%2B3rnkseP6qHsxL2Himy%2FCCP0j8NEJBGnxnM4zX2eIRCrnGDX2E35fCoV3TnEDCx8Y%2Bu3j%2Bbk3udL7laLHXAbXdmPQTcpEqIOcUP89Iqx&X-Amz-Signature=c025888c1cbbe510a3dc4b04f5499355baabc9007de5fd8b0f81ba8508a61847&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626UQJPM2%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDJ6Co4CapgNhy5dO5MAfz9H2H8MboYjaAG7QeFYvoNjQIgCgFOkX4HC4b47b1V5Ev19OoAuQjAnRspJNg7HxTivpcq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDK26UdSb0DgIdY58rCrcA6RUFTiizJP%2BiUls7JmzYpVae9oQ225BWElnPcyoXyaWpLmlGRFyZYZAXhB8Dxfnh5P6CMmUanju9RrrsCUAM8DEGJ8AGbdYRoRHjxho3EgTw8b%2Fot%2FXKoDc0l6GGNAZ3ZzYV%2FpCRsrND%2F8AMeCTOywPGC%2Bso9lNRhBD4O64%2BJlFZNqGcinYHt1sBzQzKjg5ogG2XIv9JWUJzmDhUJ4l5TauSAYrky7kq0K1Y2o8Hgnw2IYu6AhrSsGbstM5YPKh8K1RV%2BQFwv0cZnk4UAvrGyxCyPw6zZzHBEBFjvAsi0IJsp0KkFIMd9AQMrxXTr52G80hIblO6AbylZFpmc9tVdifWjqJ25qBRbqNv2XJ%2BCaxSYXFWlBjHm41A4X7U63%2Fn9G8nPm2LEsTdjJqAIdjhp1u6yAxasnEGkw3HxEh3rz8sErHv6Z8yi2sIKMTBRWTqT2lm5w0CW4KLT1wjtacxHcLe4XbBadN8ahsnhZyLD3aID5PNW%2FWOoJOQ6fzRNhnB80%2BattCg7HqOsxMZGk8N4g7alpgaTZdMaxZJPBCbl3uuzeRpQ%2Byhrd8FceiwxKx74oFkwkwFO60HzxuBKyucjcdVuvYHvgF6umOutX1e7edfoIYNfLoxj8rP5E8MOOD%2BcwGOqUBogZpmZV1IEMQaWsbCXdJeHfGxo0x%2BtA%2B%2FAhdyjgNob28F98M02GmvcnKJMnZsmcZsMe63vC9LSuyHk3n1%2F%2BahRlmdEEeLtiew3NRG52ojlbS9ygsqqbw%2B3rnkseP6qHsxL2Himy%2FCCP0j8NEJBGnxnM4zX2eIRCrnGDX2E35fCoV3TnEDCx8Y%2Bu3j%2Bbk3udL7laLHXAbXdmPQTcpEqIOcUP89Iqx&X-Amz-Signature=cb1a13a362a1b3af7004a3c1f61ef182af1d950b3e24fd82e9917ad7c9234272&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626UQJPM2%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDJ6Co4CapgNhy5dO5MAfz9H2H8MboYjaAG7QeFYvoNjQIgCgFOkX4HC4b47b1V5Ev19OoAuQjAnRspJNg7HxTivpcq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDK26UdSb0DgIdY58rCrcA6RUFTiizJP%2BiUls7JmzYpVae9oQ225BWElnPcyoXyaWpLmlGRFyZYZAXhB8Dxfnh5P6CMmUanju9RrrsCUAM8DEGJ8AGbdYRoRHjxho3EgTw8b%2Fot%2FXKoDc0l6GGNAZ3ZzYV%2FpCRsrND%2F8AMeCTOywPGC%2Bso9lNRhBD4O64%2BJlFZNqGcinYHt1sBzQzKjg5ogG2XIv9JWUJzmDhUJ4l5TauSAYrky7kq0K1Y2o8Hgnw2IYu6AhrSsGbstM5YPKh8K1RV%2BQFwv0cZnk4UAvrGyxCyPw6zZzHBEBFjvAsi0IJsp0KkFIMd9AQMrxXTr52G80hIblO6AbylZFpmc9tVdifWjqJ25qBRbqNv2XJ%2BCaxSYXFWlBjHm41A4X7U63%2Fn9G8nPm2LEsTdjJqAIdjhp1u6yAxasnEGkw3HxEh3rz8sErHv6Z8yi2sIKMTBRWTqT2lm5w0CW4KLT1wjtacxHcLe4XbBadN8ahsnhZyLD3aID5PNW%2FWOoJOQ6fzRNhnB80%2BattCg7HqOsxMZGk8N4g7alpgaTZdMaxZJPBCbl3uuzeRpQ%2Byhrd8FceiwxKx74oFkwkwFO60HzxuBKyucjcdVuvYHvgF6umOutX1e7edfoIYNfLoxj8rP5E8MOOD%2BcwGOqUBogZpmZV1IEMQaWsbCXdJeHfGxo0x%2BtA%2B%2FAhdyjgNob28F98M02GmvcnKJMnZsmcZsMe63vC9LSuyHk3n1%2F%2BahRlmdEEeLtiew3NRG52ojlbS9ygsqqbw%2B3rnkseP6qHsxL2Himy%2FCCP0j8NEJBGnxnM4zX2eIRCrnGDX2E35fCoV3TnEDCx8Y%2Bu3j%2Bbk3udL7laLHXAbXdmPQTcpEqIOcUP89Iqx&X-Amz-Signature=8c916200804b54d29b7f8488c5e80be751728146c507f2f61cf825cfbe916d9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



