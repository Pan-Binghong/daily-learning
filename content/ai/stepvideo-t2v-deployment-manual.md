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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEZFIWXS%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAepfEGJFldcNimtFUSCk19O7TbAvH%2BWzxeiACOEhzHZAiB2WpVUw2TtXkVtbrFolJSiiqfYOW6lqnAWaAjBcjKP6yqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4JxEcyW1P4OFQuYlKtwDdrxZwg%2BGfDZM7I38kF4x6lKxKVgkNCsDZLytizDJvw7JjXnAhDiDDKHBs3Xlxi1AsN3ZZiKwF5EG4ufNZ0oUPDXuLYjrhhGDJTfH21qTiCu2u88%2BnwLVt1SM4Ysu0YHIcsvv5ZpfDIt%2BL0TZ%2Fq1HmcIsPK03t3Em%2Fp4WGCooA1XnhG%2B2CLkWpBvbn24eo%2BXXKPLZQXLj248bG5PEbWO1GTuLjOqPt7HkPzTe2cnF4hxn5cN9hIrXasM5ZqzZrlZL0o6OPmhYy%2BsPOAMgnwR2PXsWN3VvtZGYhT8u3IzEsuYAy2cpYNyboS%2FMV%2BBuX8KgJYylIB%2BTt33Wx1PTCY7JKo%2Biee73lSffTGTak0CnDObk7841wA%2FwcxJdAc7GzE5QvHJKs2UlomMjm7THqyhqho5S6Qea5Zo2ifBnVtOpuIu0WSjPXc5tH5lpJDVmDMte%2FD%2BURQHWj6KkMXpMyYDn1lPFYPKhU%2FpZsDy%2B0m9HJVUqdKcknBF8j2ATogFTqdxTbQil0X6LgXuln8%2BTG%2B3lCrd2nXEjR874R2YNczrxAy3wIg%2Ft%2F5BrepZ0QH%2F5EDOmF5aN9lbWErxs80ZTPZE%2FY4XkduendNOiTlPjzqbFszxoZENUpZOIcYIutGIw4JHGzwY6pgHFUMnFIWZry3ofUku7lDuc5qyAsPo2yRp1IpQT1Cz%2B%2B20TFepDGhXeUu5gCWiXkHXVJyzY6nf%2FtQpMI6IJKnjg3aqPl6hYQmTKDFnU0h2fTdC5RDkR5CaLEk6RtyLD7r8qSXKvo4sPqLALGaHcfW%2FiYUVxu9EJ1TMGNPxjqy%2BryxmgS3FzpC7AT71g1q7Z%2BZtbAKvLoBCUKcH878Exi%2FjPwFgFQ7nV&X-Amz-Signature=3b6c19949c940ed57fc6480491dec318aa8675da7a8c550a28498cc1bc692f3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEZFIWXS%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAepfEGJFldcNimtFUSCk19O7TbAvH%2BWzxeiACOEhzHZAiB2WpVUw2TtXkVtbrFolJSiiqfYOW6lqnAWaAjBcjKP6yqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4JxEcyW1P4OFQuYlKtwDdrxZwg%2BGfDZM7I38kF4x6lKxKVgkNCsDZLytizDJvw7JjXnAhDiDDKHBs3Xlxi1AsN3ZZiKwF5EG4ufNZ0oUPDXuLYjrhhGDJTfH21qTiCu2u88%2BnwLVt1SM4Ysu0YHIcsvv5ZpfDIt%2BL0TZ%2Fq1HmcIsPK03t3Em%2Fp4WGCooA1XnhG%2B2CLkWpBvbn24eo%2BXXKPLZQXLj248bG5PEbWO1GTuLjOqPt7HkPzTe2cnF4hxn5cN9hIrXasM5ZqzZrlZL0o6OPmhYy%2BsPOAMgnwR2PXsWN3VvtZGYhT8u3IzEsuYAy2cpYNyboS%2FMV%2BBuX8KgJYylIB%2BTt33Wx1PTCY7JKo%2Biee73lSffTGTak0CnDObk7841wA%2FwcxJdAc7GzE5QvHJKs2UlomMjm7THqyhqho5S6Qea5Zo2ifBnVtOpuIu0WSjPXc5tH5lpJDVmDMte%2FD%2BURQHWj6KkMXpMyYDn1lPFYPKhU%2FpZsDy%2B0m9HJVUqdKcknBF8j2ATogFTqdxTbQil0X6LgXuln8%2BTG%2B3lCrd2nXEjR874R2YNczrxAy3wIg%2Ft%2F5BrepZ0QH%2F5EDOmF5aN9lbWErxs80ZTPZE%2FY4XkduendNOiTlPjzqbFszxoZENUpZOIcYIutGIw4JHGzwY6pgHFUMnFIWZry3ofUku7lDuc5qyAsPo2yRp1IpQT1Cz%2B%2B20TFepDGhXeUu5gCWiXkHXVJyzY6nf%2FtQpMI6IJKnjg3aqPl6hYQmTKDFnU0h2fTdC5RDkR5CaLEk6RtyLD7r8qSXKvo4sPqLALGaHcfW%2FiYUVxu9EJ1TMGNPxjqy%2BryxmgS3FzpC7AT71g1q7Z%2BZtbAKvLoBCUKcH878Exi%2FjPwFgFQ7nV&X-Amz-Signature=d514558ae869e944dea23589c16cf1ef976576e1c7c8c6ea684b1c56a641a151&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEZFIWXS%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAepfEGJFldcNimtFUSCk19O7TbAvH%2BWzxeiACOEhzHZAiB2WpVUw2TtXkVtbrFolJSiiqfYOW6lqnAWaAjBcjKP6yqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4JxEcyW1P4OFQuYlKtwDdrxZwg%2BGfDZM7I38kF4x6lKxKVgkNCsDZLytizDJvw7JjXnAhDiDDKHBs3Xlxi1AsN3ZZiKwF5EG4ufNZ0oUPDXuLYjrhhGDJTfH21qTiCu2u88%2BnwLVt1SM4Ysu0YHIcsvv5ZpfDIt%2BL0TZ%2Fq1HmcIsPK03t3Em%2Fp4WGCooA1XnhG%2B2CLkWpBvbn24eo%2BXXKPLZQXLj248bG5PEbWO1GTuLjOqPt7HkPzTe2cnF4hxn5cN9hIrXasM5ZqzZrlZL0o6OPmhYy%2BsPOAMgnwR2PXsWN3VvtZGYhT8u3IzEsuYAy2cpYNyboS%2FMV%2BBuX8KgJYylIB%2BTt33Wx1PTCY7JKo%2Biee73lSffTGTak0CnDObk7841wA%2FwcxJdAc7GzE5QvHJKs2UlomMjm7THqyhqho5S6Qea5Zo2ifBnVtOpuIu0WSjPXc5tH5lpJDVmDMte%2FD%2BURQHWj6KkMXpMyYDn1lPFYPKhU%2FpZsDy%2B0m9HJVUqdKcknBF8j2ATogFTqdxTbQil0X6LgXuln8%2BTG%2B3lCrd2nXEjR874R2YNczrxAy3wIg%2Ft%2F5BrepZ0QH%2F5EDOmF5aN9lbWErxs80ZTPZE%2FY4XkduendNOiTlPjzqbFszxoZENUpZOIcYIutGIw4JHGzwY6pgHFUMnFIWZry3ofUku7lDuc5qyAsPo2yRp1IpQT1Cz%2B%2B20TFepDGhXeUu5gCWiXkHXVJyzY6nf%2FtQpMI6IJKnjg3aqPl6hYQmTKDFnU0h2fTdC5RDkR5CaLEk6RtyLD7r8qSXKvo4sPqLALGaHcfW%2FiYUVxu9EJ1TMGNPxjqy%2BryxmgS3FzpC7AT71g1q7Z%2BZtbAKvLoBCUKcH878Exi%2FjPwFgFQ7nV&X-Amz-Signature=5304669f369abc25a85eb909f49e22a4e6838bb58e5e4152e5a697a0b7693ec4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEZFIWXS%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIAepfEGJFldcNimtFUSCk19O7TbAvH%2BWzxeiACOEhzHZAiB2WpVUw2TtXkVtbrFolJSiiqfYOW6lqnAWaAjBcjKP6yqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4JxEcyW1P4OFQuYlKtwDdrxZwg%2BGfDZM7I38kF4x6lKxKVgkNCsDZLytizDJvw7JjXnAhDiDDKHBs3Xlxi1AsN3ZZiKwF5EG4ufNZ0oUPDXuLYjrhhGDJTfH21qTiCu2u88%2BnwLVt1SM4Ysu0YHIcsvv5ZpfDIt%2BL0TZ%2Fq1HmcIsPK03t3Em%2Fp4WGCooA1XnhG%2B2CLkWpBvbn24eo%2BXXKPLZQXLj248bG5PEbWO1GTuLjOqPt7HkPzTe2cnF4hxn5cN9hIrXasM5ZqzZrlZL0o6OPmhYy%2BsPOAMgnwR2PXsWN3VvtZGYhT8u3IzEsuYAy2cpYNyboS%2FMV%2BBuX8KgJYylIB%2BTt33Wx1PTCY7JKo%2Biee73lSffTGTak0CnDObk7841wA%2FwcxJdAc7GzE5QvHJKs2UlomMjm7THqyhqho5S6Qea5Zo2ifBnVtOpuIu0WSjPXc5tH5lpJDVmDMte%2FD%2BURQHWj6KkMXpMyYDn1lPFYPKhU%2FpZsDy%2B0m9HJVUqdKcknBF8j2ATogFTqdxTbQil0X6LgXuln8%2BTG%2B3lCrd2nXEjR874R2YNczrxAy3wIg%2Ft%2F5BrepZ0QH%2F5EDOmF5aN9lbWErxs80ZTPZE%2FY4XkduendNOiTlPjzqbFszxoZENUpZOIcYIutGIw4JHGzwY6pgHFUMnFIWZry3ofUku7lDuc5qyAsPo2yRp1IpQT1Cz%2B%2B20TFepDGhXeUu5gCWiXkHXVJyzY6nf%2FtQpMI6IJKnjg3aqPl6hYQmTKDFnU0h2fTdC5RDkR5CaLEk6RtyLD7r8qSXKvo4sPqLALGaHcfW%2FiYUVxu9EJ1TMGNPxjqy%2BryxmgS3FzpC7AT71g1q7Z%2BZtbAKvLoBCUKcH878Exi%2FjPwFgFQ7nV&X-Amz-Signature=509bc2c7d860f54ac7bab4c09160eebf5885ec1bbff89305d29bd8d30f3f4a05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



