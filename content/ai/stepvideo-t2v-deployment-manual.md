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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XSTZBVW%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCtPPqUKXTzp%2F0hziDe%2BwxCFQVk60sYPcMa9%2FPSAYxJjQIgcBQC188E0P7Lobt%2BQ0mpNrr7gT6%2B8HKbVvJWn9dLpiYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDA9fbgq0vlIjNn3RBCrcA6XQJKoIHH%2B0X1E6nZjglOzusan6FJ4BX3lRsKhuh3%2FWXi6tvib%2Fw4SfK%2B12iv4XQz0fp%2FDQywxhOX%2Bov1PH8WiLf0UaBGd3YDef5vpVp9Pci9lol%2Bp1f4lxWKTfR5yRu1MtRlixq36OLOZ%2B2lKgKKNE9LD3NaOwmEg5jwJpeRVu6nsm7CoATd1R8ySkBnRXPCAfPM3Slh%2BE%2B49cumqd48p3cVg1Tmd1utjU%2FQGSTMAAHEv92yNaObD2EbNGJ%2Fri9J4ixll3yzjNAmH%2B8yydinQbsp91JwBdwzEGZvtKzXSnudoFTAPKtyr0mjPGuBea9YUGj2MAqTfohlJ00U7XlA6weTIN2LTxWawVxhKW4cEcK5W6B3cOsM0E1Y2GRdqOtqGqgmq4dsZAIshYKozlesXgU0xWe7bNQ87UzxNMVHZbTqKR%2B7AHm4dKzOYI%2Bk7yqVIZXHn8AlZj4rVz8i9pu0PBIN%2FL%2BIDJkQLnyMRmmRkULT2EgQ%2BEn5YX0GYgT809Da65ceNkY5XCCUTsRpyOXv7%2FTJuB23jN1g9cfBXDsoqtvXrEBs0im61vqtpxwjyH6hJdpS8dqcIbqCfN%2BDxv0%2BGq9w2Y3dNqtkPU7DcsyBl%2FfAEermJ6qY7sTrBYMNrTm88GOqUBRnY0SqpzIMR8rlBfovLaHTn286Aj8DiuubZdYu%2FI%2BYd3HTl4uafAI37oQ8dlfZTnw7JxBKLRKfRykBFOCiER70fLHDdQ9cO7IkMZW1RdecLwHL%2FJVtsK7GD4uJPsT67snbwq%2BShOcFuSJKdAjEMI7M0k4hUBQxv7PpYnX%2FQYhI0M4v2c5HukvGvsqvEGyklZWFPRMym9k4cX%2FtEytaj03KA5oHsY&X-Amz-Signature=e4ef201bf0fe3bac8a73a3911f342edd7c57c6522e9dcb78abe287ea5e1cf9bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XSTZBVW%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCtPPqUKXTzp%2F0hziDe%2BwxCFQVk60sYPcMa9%2FPSAYxJjQIgcBQC188E0P7Lobt%2BQ0mpNrr7gT6%2B8HKbVvJWn9dLpiYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDA9fbgq0vlIjNn3RBCrcA6XQJKoIHH%2B0X1E6nZjglOzusan6FJ4BX3lRsKhuh3%2FWXi6tvib%2Fw4SfK%2B12iv4XQz0fp%2FDQywxhOX%2Bov1PH8WiLf0UaBGd3YDef5vpVp9Pci9lol%2Bp1f4lxWKTfR5yRu1MtRlixq36OLOZ%2B2lKgKKNE9LD3NaOwmEg5jwJpeRVu6nsm7CoATd1R8ySkBnRXPCAfPM3Slh%2BE%2B49cumqd48p3cVg1Tmd1utjU%2FQGSTMAAHEv92yNaObD2EbNGJ%2Fri9J4ixll3yzjNAmH%2B8yydinQbsp91JwBdwzEGZvtKzXSnudoFTAPKtyr0mjPGuBea9YUGj2MAqTfohlJ00U7XlA6weTIN2LTxWawVxhKW4cEcK5W6B3cOsM0E1Y2GRdqOtqGqgmq4dsZAIshYKozlesXgU0xWe7bNQ87UzxNMVHZbTqKR%2B7AHm4dKzOYI%2Bk7yqVIZXHn8AlZj4rVz8i9pu0PBIN%2FL%2BIDJkQLnyMRmmRkULT2EgQ%2BEn5YX0GYgT809Da65ceNkY5XCCUTsRpyOXv7%2FTJuB23jN1g9cfBXDsoqtvXrEBs0im61vqtpxwjyH6hJdpS8dqcIbqCfN%2BDxv0%2BGq9w2Y3dNqtkPU7DcsyBl%2FfAEermJ6qY7sTrBYMNrTm88GOqUBRnY0SqpzIMR8rlBfovLaHTn286Aj8DiuubZdYu%2FI%2BYd3HTl4uafAI37oQ8dlfZTnw7JxBKLRKfRykBFOCiER70fLHDdQ9cO7IkMZW1RdecLwHL%2FJVtsK7GD4uJPsT67snbwq%2BShOcFuSJKdAjEMI7M0k4hUBQxv7PpYnX%2FQYhI0M4v2c5HukvGvsqvEGyklZWFPRMym9k4cX%2FtEytaj03KA5oHsY&X-Amz-Signature=ce338dcc2e8705ebff63313885f60435aee6af107d1180e0085f5c1b1633b076&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XSTZBVW%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCtPPqUKXTzp%2F0hziDe%2BwxCFQVk60sYPcMa9%2FPSAYxJjQIgcBQC188E0P7Lobt%2BQ0mpNrr7gT6%2B8HKbVvJWn9dLpiYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDA9fbgq0vlIjNn3RBCrcA6XQJKoIHH%2B0X1E6nZjglOzusan6FJ4BX3lRsKhuh3%2FWXi6tvib%2Fw4SfK%2B12iv4XQz0fp%2FDQywxhOX%2Bov1PH8WiLf0UaBGd3YDef5vpVp9Pci9lol%2Bp1f4lxWKTfR5yRu1MtRlixq36OLOZ%2B2lKgKKNE9LD3NaOwmEg5jwJpeRVu6nsm7CoATd1R8ySkBnRXPCAfPM3Slh%2BE%2B49cumqd48p3cVg1Tmd1utjU%2FQGSTMAAHEv92yNaObD2EbNGJ%2Fri9J4ixll3yzjNAmH%2B8yydinQbsp91JwBdwzEGZvtKzXSnudoFTAPKtyr0mjPGuBea9YUGj2MAqTfohlJ00U7XlA6weTIN2LTxWawVxhKW4cEcK5W6B3cOsM0E1Y2GRdqOtqGqgmq4dsZAIshYKozlesXgU0xWe7bNQ87UzxNMVHZbTqKR%2B7AHm4dKzOYI%2Bk7yqVIZXHn8AlZj4rVz8i9pu0PBIN%2FL%2BIDJkQLnyMRmmRkULT2EgQ%2BEn5YX0GYgT809Da65ceNkY5XCCUTsRpyOXv7%2FTJuB23jN1g9cfBXDsoqtvXrEBs0im61vqtpxwjyH6hJdpS8dqcIbqCfN%2BDxv0%2BGq9w2Y3dNqtkPU7DcsyBl%2FfAEermJ6qY7sTrBYMNrTm88GOqUBRnY0SqpzIMR8rlBfovLaHTn286Aj8DiuubZdYu%2FI%2BYd3HTl4uafAI37oQ8dlfZTnw7JxBKLRKfRykBFOCiER70fLHDdQ9cO7IkMZW1RdecLwHL%2FJVtsK7GD4uJPsT67snbwq%2BShOcFuSJKdAjEMI7M0k4hUBQxv7PpYnX%2FQYhI0M4v2c5HukvGvsqvEGyklZWFPRMym9k4cX%2FtEytaj03KA5oHsY&X-Amz-Signature=9f51b38ffd17f8653a460fb9f5cb6b8535572e6d40e4559829c20db5ea9f3c41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XSTZBVW%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCtPPqUKXTzp%2F0hziDe%2BwxCFQVk60sYPcMa9%2FPSAYxJjQIgcBQC188E0P7Lobt%2BQ0mpNrr7gT6%2B8HKbVvJWn9dLpiYq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDA9fbgq0vlIjNn3RBCrcA6XQJKoIHH%2B0X1E6nZjglOzusan6FJ4BX3lRsKhuh3%2FWXi6tvib%2Fw4SfK%2B12iv4XQz0fp%2FDQywxhOX%2Bov1PH8WiLf0UaBGd3YDef5vpVp9Pci9lol%2Bp1f4lxWKTfR5yRu1MtRlixq36OLOZ%2B2lKgKKNE9LD3NaOwmEg5jwJpeRVu6nsm7CoATd1R8ySkBnRXPCAfPM3Slh%2BE%2B49cumqd48p3cVg1Tmd1utjU%2FQGSTMAAHEv92yNaObD2EbNGJ%2Fri9J4ixll3yzjNAmH%2B8yydinQbsp91JwBdwzEGZvtKzXSnudoFTAPKtyr0mjPGuBea9YUGj2MAqTfohlJ00U7XlA6weTIN2LTxWawVxhKW4cEcK5W6B3cOsM0E1Y2GRdqOtqGqgmq4dsZAIshYKozlesXgU0xWe7bNQ87UzxNMVHZbTqKR%2B7AHm4dKzOYI%2Bk7yqVIZXHn8AlZj4rVz8i9pu0PBIN%2FL%2BIDJkQLnyMRmmRkULT2EgQ%2BEn5YX0GYgT809Da65ceNkY5XCCUTsRpyOXv7%2FTJuB23jN1g9cfBXDsoqtvXrEBs0im61vqtpxwjyH6hJdpS8dqcIbqCfN%2BDxv0%2BGq9w2Y3dNqtkPU7DcsyBl%2FfAEermJ6qY7sTrBYMNrTm88GOqUBRnY0SqpzIMR8rlBfovLaHTn286Aj8DiuubZdYu%2FI%2BYd3HTl4uafAI37oQ8dlfZTnw7JxBKLRKfRykBFOCiER70fLHDdQ9cO7IkMZW1RdecLwHL%2FJVtsK7GD4uJPsT67snbwq%2BShOcFuSJKdAjEMI7M0k4hUBQxv7PpYnX%2FQYhI0M4v2c5HukvGvsqvEGyklZWFPRMym9k4cX%2FtEytaj03KA5oHsY&X-Amz-Signature=58cb7df5926ed5364de433b21088c71c28d5e274bdb33bc6aea779eaf1316659&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



