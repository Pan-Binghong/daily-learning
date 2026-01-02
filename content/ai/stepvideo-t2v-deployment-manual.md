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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKIEJDRB%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQC0OjxMv%2Fi78TCCyqeEKFxVOHEy0U7SMjzVoWgZbuKwOQIhAJlKMM57GUo0ckUZ7ernb5qQkI%2FwtUKazRTrmeQwKeXNKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxobKAzBURPWo%2B4u7cq3ANoxSoCeEcxR62Gj97wmUnaTjxNyDB3SdWYXM5jxZNr2xu3jiwavuivW1KF%2BBzXgbeyEZk54WJKNF9qAMuPES80vNnWg5xZADbJQ6ceGFdk7Vfe%2FUs1MufErFDzOmYx8CNPYeDYTtWuTxRrEcs1YAAl65N1eW%2BgnEZPM6cc2XvZQBnl9kwQPPCFVkXuivSnypM%2FTB1p%2FOtLUjIT7rfvxBUiuCNEMiDTwEtdZf7BmehzByRmkLtqumvd4fK2SFc6gc0xV8zmd36Piv3qoQpT0MMcsn3OdX0832T5qY1jc83b4fiDGqedRETpFL%2BLrUQXE1T%2Bw%2Bbl7mkIHUvh0XeUbyNss10hHb%2BNgUTGZNlUqg7aWzgzJtMV4d0lYANQZRIzEbE2Qwt%2BLEA9oyYN56tkQpPTUR44bdPelgy2WKxKP%2B%2F4iYGAlApvbMzwT5Ng4qUhUU35bBLTRNPsf%2FCRqFZQtNX79E0iMSAPWVg7afEBynz8HwQAFhP0sHaRuQqSc6TZZu0TM8WZuPxcu0gbKiYDjyZJtvM4FcaoDMeaLWhA58Zm1ePw36zKvhzey0Ef8aKr5hWgQEITPpQhh539dTLI35Mfs2HSCryCnYqi1u6sLeNMvhUc7HeMkMBssw0AUTDVrdzKBjqkAS3ddYo6OragL7q7IC7D1yEXB1TMn4A%2Bkq7RxD231AXL%2FiZhq1EvWb1jUYj7myotwFylh8vqytcm2P7pI0E5g4P0GKxM%2BqpWMhcbo9cJMvP0Gs6g24mHyIHaLXj8Vhrkuz5Ierj8w1zJI%2BfPorWvCsoWiScs9FAN4qU3%2F4NmFTBoPS9gyINCaCHqPEVjZSUF%2BNjZMuQT%2FwvsdP3x9AGdx8uMQuAz&X-Amz-Signature=7a5c70987dfe1debc09b48cde0cafcea2923d6bd68c6a5f55713685f736add65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKIEJDRB%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQC0OjxMv%2Fi78TCCyqeEKFxVOHEy0U7SMjzVoWgZbuKwOQIhAJlKMM57GUo0ckUZ7ernb5qQkI%2FwtUKazRTrmeQwKeXNKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxobKAzBURPWo%2B4u7cq3ANoxSoCeEcxR62Gj97wmUnaTjxNyDB3SdWYXM5jxZNr2xu3jiwavuivW1KF%2BBzXgbeyEZk54WJKNF9qAMuPES80vNnWg5xZADbJQ6ceGFdk7Vfe%2FUs1MufErFDzOmYx8CNPYeDYTtWuTxRrEcs1YAAl65N1eW%2BgnEZPM6cc2XvZQBnl9kwQPPCFVkXuivSnypM%2FTB1p%2FOtLUjIT7rfvxBUiuCNEMiDTwEtdZf7BmehzByRmkLtqumvd4fK2SFc6gc0xV8zmd36Piv3qoQpT0MMcsn3OdX0832T5qY1jc83b4fiDGqedRETpFL%2BLrUQXE1T%2Bw%2Bbl7mkIHUvh0XeUbyNss10hHb%2BNgUTGZNlUqg7aWzgzJtMV4d0lYANQZRIzEbE2Qwt%2BLEA9oyYN56tkQpPTUR44bdPelgy2WKxKP%2B%2F4iYGAlApvbMzwT5Ng4qUhUU35bBLTRNPsf%2FCRqFZQtNX79E0iMSAPWVg7afEBynz8HwQAFhP0sHaRuQqSc6TZZu0TM8WZuPxcu0gbKiYDjyZJtvM4FcaoDMeaLWhA58Zm1ePw36zKvhzey0Ef8aKr5hWgQEITPpQhh539dTLI35Mfs2HSCryCnYqi1u6sLeNMvhUc7HeMkMBssw0AUTDVrdzKBjqkAS3ddYo6OragL7q7IC7D1yEXB1TMn4A%2Bkq7RxD231AXL%2FiZhq1EvWb1jUYj7myotwFylh8vqytcm2P7pI0E5g4P0GKxM%2BqpWMhcbo9cJMvP0Gs6g24mHyIHaLXj8Vhrkuz5Ierj8w1zJI%2BfPorWvCsoWiScs9FAN4qU3%2F4NmFTBoPS9gyINCaCHqPEVjZSUF%2BNjZMuQT%2FwvsdP3x9AGdx8uMQuAz&X-Amz-Signature=2d0428e47801c218ec72fd1ce3e14e12c7b095048fdf6818768d6527fbc22055&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKIEJDRB%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQC0OjxMv%2Fi78TCCyqeEKFxVOHEy0U7SMjzVoWgZbuKwOQIhAJlKMM57GUo0ckUZ7ernb5qQkI%2FwtUKazRTrmeQwKeXNKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxobKAzBURPWo%2B4u7cq3ANoxSoCeEcxR62Gj97wmUnaTjxNyDB3SdWYXM5jxZNr2xu3jiwavuivW1KF%2BBzXgbeyEZk54WJKNF9qAMuPES80vNnWg5xZADbJQ6ceGFdk7Vfe%2FUs1MufErFDzOmYx8CNPYeDYTtWuTxRrEcs1YAAl65N1eW%2BgnEZPM6cc2XvZQBnl9kwQPPCFVkXuivSnypM%2FTB1p%2FOtLUjIT7rfvxBUiuCNEMiDTwEtdZf7BmehzByRmkLtqumvd4fK2SFc6gc0xV8zmd36Piv3qoQpT0MMcsn3OdX0832T5qY1jc83b4fiDGqedRETpFL%2BLrUQXE1T%2Bw%2Bbl7mkIHUvh0XeUbyNss10hHb%2BNgUTGZNlUqg7aWzgzJtMV4d0lYANQZRIzEbE2Qwt%2BLEA9oyYN56tkQpPTUR44bdPelgy2WKxKP%2B%2F4iYGAlApvbMzwT5Ng4qUhUU35bBLTRNPsf%2FCRqFZQtNX79E0iMSAPWVg7afEBynz8HwQAFhP0sHaRuQqSc6TZZu0TM8WZuPxcu0gbKiYDjyZJtvM4FcaoDMeaLWhA58Zm1ePw36zKvhzey0Ef8aKr5hWgQEITPpQhh539dTLI35Mfs2HSCryCnYqi1u6sLeNMvhUc7HeMkMBssw0AUTDVrdzKBjqkAS3ddYo6OragL7q7IC7D1yEXB1TMn4A%2Bkq7RxD231AXL%2FiZhq1EvWb1jUYj7myotwFylh8vqytcm2P7pI0E5g4P0GKxM%2BqpWMhcbo9cJMvP0Gs6g24mHyIHaLXj8Vhrkuz5Ierj8w1zJI%2BfPorWvCsoWiScs9FAN4qU3%2F4NmFTBoPS9gyINCaCHqPEVjZSUF%2BNjZMuQT%2FwvsdP3x9AGdx8uMQuAz&X-Amz-Signature=887de0cbd6e055659afd4665ee3d7215a83b6ddd66af94921f051db7ae6c9b5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKIEJDRB%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQC0OjxMv%2Fi78TCCyqeEKFxVOHEy0U7SMjzVoWgZbuKwOQIhAJlKMM57GUo0ckUZ7ernb5qQkI%2FwtUKazRTrmeQwKeXNKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxobKAzBURPWo%2B4u7cq3ANoxSoCeEcxR62Gj97wmUnaTjxNyDB3SdWYXM5jxZNr2xu3jiwavuivW1KF%2BBzXgbeyEZk54WJKNF9qAMuPES80vNnWg5xZADbJQ6ceGFdk7Vfe%2FUs1MufErFDzOmYx8CNPYeDYTtWuTxRrEcs1YAAl65N1eW%2BgnEZPM6cc2XvZQBnl9kwQPPCFVkXuivSnypM%2FTB1p%2FOtLUjIT7rfvxBUiuCNEMiDTwEtdZf7BmehzByRmkLtqumvd4fK2SFc6gc0xV8zmd36Piv3qoQpT0MMcsn3OdX0832T5qY1jc83b4fiDGqedRETpFL%2BLrUQXE1T%2Bw%2Bbl7mkIHUvh0XeUbyNss10hHb%2BNgUTGZNlUqg7aWzgzJtMV4d0lYANQZRIzEbE2Qwt%2BLEA9oyYN56tkQpPTUR44bdPelgy2WKxKP%2B%2F4iYGAlApvbMzwT5Ng4qUhUU35bBLTRNPsf%2FCRqFZQtNX79E0iMSAPWVg7afEBynz8HwQAFhP0sHaRuQqSc6TZZu0TM8WZuPxcu0gbKiYDjyZJtvM4FcaoDMeaLWhA58Zm1ePw36zKvhzey0Ef8aKr5hWgQEITPpQhh539dTLI35Mfs2HSCryCnYqi1u6sLeNMvhUc7HeMkMBssw0AUTDVrdzKBjqkAS3ddYo6OragL7q7IC7D1yEXB1TMn4A%2Bkq7RxD231AXL%2FiZhq1EvWb1jUYj7myotwFylh8vqytcm2P7pI0E5g4P0GKxM%2BqpWMhcbo9cJMvP0Gs6g24mHyIHaLXj8Vhrkuz5Ierj8w1zJI%2BfPorWvCsoWiScs9FAN4qU3%2F4NmFTBoPS9gyINCaCHqPEVjZSUF%2BNjZMuQT%2FwvsdP3x9AGdx8uMQuAz&X-Amz-Signature=7c9a144e55886bfdd766d9d430f66222acdadb20f534dc7c62be7f3e9cc3d710&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



