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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLYMZH5I%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDhm4M2T%2BT5di6oJ6cpTK7HCvRNrn%2Bss0jJE7iUcNr7wAIhANg1Gx6YAiFlzMIN9T8msk2GZ4ygedlrGGufVA5NgP%2BGKv8DCDQQABoMNjM3NDIzMTgzODA1Igwv795y5gnzDFbysNgq3APpU3rjhUowoWLJx56HA9RokJw397GN4NXMsoXGA6z8fJlIyGyBw%2FWe4d8jZklAaP5X%2B1X8MDPGEFZQDIdvXlxqXBhvDuxCMEmzT3HV%2BHqgESQcF45KaJI%2FaPrpMnBES7TH8Z%2BwwGtoCPjpx3QICIHnWkqgl56NemaUPk1q6h%2BkRiO6CXmAnk0Tq93kfpSgkKzermCyBrLur4TNrKSGT6%2FSbw%2BHz48Q3hty991XSpzYz5JwjoFlG1jfpRU1vHsRbuBkDVEf8Qa5anebabN%2Fz1MB4R31%2BQn0eG3yMGHjqUGkUPrKYpi1lpALFFX3Ek2ecIBV3a0rQP33I9k4ZOItVJOn5RZ9jTS7VG%2BooFbvSBTS2uPKXIaq4INLUztOyovAWgnWU9vq7f%2B7AiTuj3Gv6iUTOE3ZKkN7KGdlRGvfhDISfA9Wrg4%2FQFds8vSCqEUdJLroKxsFkdpSJS17gIkAe9sj%2BCJmZzp7SWHMNGYGAQbMEFZIGhjmLDFXMvvgce3owReL280LYP%2BMWv9v7F8VbZfmCJrcTVahzdkrIPFDNf9mAWVDwtN5bdIQEBgWMEFa8jO%2FmpvCvxBYFaw2EJDpredYii03aviDeR8USDUvGtcw6giFidfIzhtt2iuxmDDE7qzOBjqkAXpfztapRRxp2sNDDZEyytxwhEbJP%2F1Hvph04JPc6tkgrGKtzw9b7pJz6GnBNNp0DjWUVO6Updh1CZV%2FRnAsIhS3JJ48OtkJrL3YvbejNlgyWljR5oukBQG%2Fb9LThCVUNElQrJxOS08FLT54fAZHIYBv%2FsM9VILhAHOCCm3eMKKSal5Hi91I10rTou40RqQUq5rmvFS26S3pVsTj6WaA88AA%2F%2FZt&X-Amz-Signature=3af19931d1ce4ebc0f6ea0d1d1d18ad44b1223ab41ec84314d2f690ab10f104b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLYMZH5I%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDhm4M2T%2BT5di6oJ6cpTK7HCvRNrn%2Bss0jJE7iUcNr7wAIhANg1Gx6YAiFlzMIN9T8msk2GZ4ygedlrGGufVA5NgP%2BGKv8DCDQQABoMNjM3NDIzMTgzODA1Igwv795y5gnzDFbysNgq3APpU3rjhUowoWLJx56HA9RokJw397GN4NXMsoXGA6z8fJlIyGyBw%2FWe4d8jZklAaP5X%2B1X8MDPGEFZQDIdvXlxqXBhvDuxCMEmzT3HV%2BHqgESQcF45KaJI%2FaPrpMnBES7TH8Z%2BwwGtoCPjpx3QICIHnWkqgl56NemaUPk1q6h%2BkRiO6CXmAnk0Tq93kfpSgkKzermCyBrLur4TNrKSGT6%2FSbw%2BHz48Q3hty991XSpzYz5JwjoFlG1jfpRU1vHsRbuBkDVEf8Qa5anebabN%2Fz1MB4R31%2BQn0eG3yMGHjqUGkUPrKYpi1lpALFFX3Ek2ecIBV3a0rQP33I9k4ZOItVJOn5RZ9jTS7VG%2BooFbvSBTS2uPKXIaq4INLUztOyovAWgnWU9vq7f%2B7AiTuj3Gv6iUTOE3ZKkN7KGdlRGvfhDISfA9Wrg4%2FQFds8vSCqEUdJLroKxsFkdpSJS17gIkAe9sj%2BCJmZzp7SWHMNGYGAQbMEFZIGhjmLDFXMvvgce3owReL280LYP%2BMWv9v7F8VbZfmCJrcTVahzdkrIPFDNf9mAWVDwtN5bdIQEBgWMEFa8jO%2FmpvCvxBYFaw2EJDpredYii03aviDeR8USDUvGtcw6giFidfIzhtt2iuxmDDE7qzOBjqkAXpfztapRRxp2sNDDZEyytxwhEbJP%2F1Hvph04JPc6tkgrGKtzw9b7pJz6GnBNNp0DjWUVO6Updh1CZV%2FRnAsIhS3JJ48OtkJrL3YvbejNlgyWljR5oukBQG%2Fb9LThCVUNElQrJxOS08FLT54fAZHIYBv%2FsM9VILhAHOCCm3eMKKSal5Hi91I10rTou40RqQUq5rmvFS26S3pVsTj6WaA88AA%2F%2FZt&X-Amz-Signature=0ad38b8cd25b989b9fdf33f563a626e57af3af6df8571db403d8825f8e891e32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLYMZH5I%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDhm4M2T%2BT5di6oJ6cpTK7HCvRNrn%2Bss0jJE7iUcNr7wAIhANg1Gx6YAiFlzMIN9T8msk2GZ4ygedlrGGufVA5NgP%2BGKv8DCDQQABoMNjM3NDIzMTgzODA1Igwv795y5gnzDFbysNgq3APpU3rjhUowoWLJx56HA9RokJw397GN4NXMsoXGA6z8fJlIyGyBw%2FWe4d8jZklAaP5X%2B1X8MDPGEFZQDIdvXlxqXBhvDuxCMEmzT3HV%2BHqgESQcF45KaJI%2FaPrpMnBES7TH8Z%2BwwGtoCPjpx3QICIHnWkqgl56NemaUPk1q6h%2BkRiO6CXmAnk0Tq93kfpSgkKzermCyBrLur4TNrKSGT6%2FSbw%2BHz48Q3hty991XSpzYz5JwjoFlG1jfpRU1vHsRbuBkDVEf8Qa5anebabN%2Fz1MB4R31%2BQn0eG3yMGHjqUGkUPrKYpi1lpALFFX3Ek2ecIBV3a0rQP33I9k4ZOItVJOn5RZ9jTS7VG%2BooFbvSBTS2uPKXIaq4INLUztOyovAWgnWU9vq7f%2B7AiTuj3Gv6iUTOE3ZKkN7KGdlRGvfhDISfA9Wrg4%2FQFds8vSCqEUdJLroKxsFkdpSJS17gIkAe9sj%2BCJmZzp7SWHMNGYGAQbMEFZIGhjmLDFXMvvgce3owReL280LYP%2BMWv9v7F8VbZfmCJrcTVahzdkrIPFDNf9mAWVDwtN5bdIQEBgWMEFa8jO%2FmpvCvxBYFaw2EJDpredYii03aviDeR8USDUvGtcw6giFidfIzhtt2iuxmDDE7qzOBjqkAXpfztapRRxp2sNDDZEyytxwhEbJP%2F1Hvph04JPc6tkgrGKtzw9b7pJz6GnBNNp0DjWUVO6Updh1CZV%2FRnAsIhS3JJ48OtkJrL3YvbejNlgyWljR5oukBQG%2Fb9LThCVUNElQrJxOS08FLT54fAZHIYBv%2FsM9VILhAHOCCm3eMKKSal5Hi91I10rTou40RqQUq5rmvFS26S3pVsTj6WaA88AA%2F%2FZt&X-Amz-Signature=a49b465586c03d9531626829ed439fc09d5e964e1e91c49763780c1afdf7964a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLYMZH5I%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDhm4M2T%2BT5di6oJ6cpTK7HCvRNrn%2Bss0jJE7iUcNr7wAIhANg1Gx6YAiFlzMIN9T8msk2GZ4ygedlrGGufVA5NgP%2BGKv8DCDQQABoMNjM3NDIzMTgzODA1Igwv795y5gnzDFbysNgq3APpU3rjhUowoWLJx56HA9RokJw397GN4NXMsoXGA6z8fJlIyGyBw%2FWe4d8jZklAaP5X%2B1X8MDPGEFZQDIdvXlxqXBhvDuxCMEmzT3HV%2BHqgESQcF45KaJI%2FaPrpMnBES7TH8Z%2BwwGtoCPjpx3QICIHnWkqgl56NemaUPk1q6h%2BkRiO6CXmAnk0Tq93kfpSgkKzermCyBrLur4TNrKSGT6%2FSbw%2BHz48Q3hty991XSpzYz5JwjoFlG1jfpRU1vHsRbuBkDVEf8Qa5anebabN%2Fz1MB4R31%2BQn0eG3yMGHjqUGkUPrKYpi1lpALFFX3Ek2ecIBV3a0rQP33I9k4ZOItVJOn5RZ9jTS7VG%2BooFbvSBTS2uPKXIaq4INLUztOyovAWgnWU9vq7f%2B7AiTuj3Gv6iUTOE3ZKkN7KGdlRGvfhDISfA9Wrg4%2FQFds8vSCqEUdJLroKxsFkdpSJS17gIkAe9sj%2BCJmZzp7SWHMNGYGAQbMEFZIGhjmLDFXMvvgce3owReL280LYP%2BMWv9v7F8VbZfmCJrcTVahzdkrIPFDNf9mAWVDwtN5bdIQEBgWMEFa8jO%2FmpvCvxBYFaw2EJDpredYii03aviDeR8USDUvGtcw6giFidfIzhtt2iuxmDDE7qzOBjqkAXpfztapRRxp2sNDDZEyytxwhEbJP%2F1Hvph04JPc6tkgrGKtzw9b7pJz6GnBNNp0DjWUVO6Updh1CZV%2FRnAsIhS3JJ48OtkJrL3YvbejNlgyWljR5oukBQG%2Fb9LThCVUNElQrJxOS08FLT54fAZHIYBv%2FsM9VILhAHOCCm3eMKKSal5Hi91I10rTou40RqQUq5rmvFS26S3pVsTj6WaA88AA%2F%2FZt&X-Amz-Signature=a9ccbb6eedad685395d5108b80b8211370155c179c51bbd12147c23063e9e4f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



