<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif)

---

> References



=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTP2ABEE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIETRCuY60SNzAuVakj0JT%2BWuzgrjtjgZJVXNXScmRLcQAiBbDVogtLXppxoCr8c4pCe5Rj%2F3hiE%2FRqqtb%2F4fw7nf1ir%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM%2F1sMGmsGQKU6jxSrKtwDRk6F6rIxRXopOVlw9bnZ4WICp2PfvIS6fZosfgCUj4meewEqOBFd6e6st00rzWdydINozQSbBc6dVvXLTqj%2Biebb4HD0SJBJqswpq4pjaHLZBGJsWNMct%2BOG4sUufnMdGUQBdzsKRdxJLgwpJBQ7b0J%2FNEphOckedU%2BRzXf5y%2BeH6H9OXOIBw0X%2BqURGZt044wYFRBNP5eCotKcsmWw%2F1IPmhbIH9pnxwZ7NP0H59IarklRRlBHeARlhvLemA4kq65iSWQQHA2HLtVyZmAAaYgIdyDA161XKEIoIF6POnUZUAeJTPIHdyqA1lypNZPfsbrifUy%2FlKxezVdH%2FHMmxD9%2FWKphNnWT8osgTDPd7GofCz%2FmLwxBvq8ABYfFnLVHDlrV%2FLxuF62UaJ4Qs2EqajyBzg%2BSBTSoR0L%2FIQeYquXTDsUzeWUucWXLyXhlhAuRHuH1ob1xFVK43VBbLrI1JQkTAINnMxCtL6yf3k2nSl8dcIvcmPa1cH%2BXumDtgvVvDHs3a3mK9%2FKunFGO7U47oMMcgoI55fRpNQYbXesBncrW2kyCG85kgXNdgFeO8K7NPzQaxpQhaYVd%2FKeP7citV9GELapiQ%2B6zAsSnAiAZ0GRwcHPd%2FVYtT4rPAnbgwlJzMzwY6pgGik%2B8dQJucADMT%2B%2BXlRfX6T8GC5Oj%2BTOUyLM7wasEEjScnVNotx%2FuWYEfPILqN08fUNamlg4vEPYzWfjyYxdmR6VLhLmAsogQO6Zr2foC1yoCR%2Bu93JSWdQGKiW2tYIfxQQGBFkpUw5cCZpC4TtP7f1o9EjcyQMUIt%2BJ%2BVN6ViKunJbssoL%2B5%2FU%2FDTRnLY6sk7XAKsTA1YaCpgOo689zAUk3GC47ks&X-Amz-Signature=d670659bec1ef57f996d57c715d5921c12cd08d78035aad59e5127516e6dc93b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTP2ABEE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIETRCuY60SNzAuVakj0JT%2BWuzgrjtjgZJVXNXScmRLcQAiBbDVogtLXppxoCr8c4pCe5Rj%2F3hiE%2FRqqtb%2F4fw7nf1ir%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM%2F1sMGmsGQKU6jxSrKtwDRk6F6rIxRXopOVlw9bnZ4WICp2PfvIS6fZosfgCUj4meewEqOBFd6e6st00rzWdydINozQSbBc6dVvXLTqj%2Biebb4HD0SJBJqswpq4pjaHLZBGJsWNMct%2BOG4sUufnMdGUQBdzsKRdxJLgwpJBQ7b0J%2FNEphOckedU%2BRzXf5y%2BeH6H9OXOIBw0X%2BqURGZt044wYFRBNP5eCotKcsmWw%2F1IPmhbIH9pnxwZ7NP0H59IarklRRlBHeARlhvLemA4kq65iSWQQHA2HLtVyZmAAaYgIdyDA161XKEIoIF6POnUZUAeJTPIHdyqA1lypNZPfsbrifUy%2FlKxezVdH%2FHMmxD9%2FWKphNnWT8osgTDPd7GofCz%2FmLwxBvq8ABYfFnLVHDlrV%2FLxuF62UaJ4Qs2EqajyBzg%2BSBTSoR0L%2FIQeYquXTDsUzeWUucWXLyXhlhAuRHuH1ob1xFVK43VBbLrI1JQkTAINnMxCtL6yf3k2nSl8dcIvcmPa1cH%2BXumDtgvVvDHs3a3mK9%2FKunFGO7U47oMMcgoI55fRpNQYbXesBncrW2kyCG85kgXNdgFeO8K7NPzQaxpQhaYVd%2FKeP7citV9GELapiQ%2B6zAsSnAiAZ0GRwcHPd%2FVYtT4rPAnbgwlJzMzwY6pgGik%2B8dQJucADMT%2B%2BXlRfX6T8GC5Oj%2BTOUyLM7wasEEjScnVNotx%2FuWYEfPILqN08fUNamlg4vEPYzWfjyYxdmR6VLhLmAsogQO6Zr2foC1yoCR%2Bu93JSWdQGKiW2tYIfxQQGBFkpUw5cCZpC4TtP7f1o9EjcyQMUIt%2BJ%2BVN6ViKunJbssoL%2B5%2FU%2FDTRnLY6sk7XAKsTA1YaCpgOo689zAUk3GC47ks&X-Amz-Signature=efd85b1c7915c453b0b8b8c9a7025e2add2c205b6a05204e794d9bd2b3001dcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTP2ABEE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIETRCuY60SNzAuVakj0JT%2BWuzgrjtjgZJVXNXScmRLcQAiBbDVogtLXppxoCr8c4pCe5Rj%2F3hiE%2FRqqtb%2F4fw7nf1ir%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM%2F1sMGmsGQKU6jxSrKtwDRk6F6rIxRXopOVlw9bnZ4WICp2PfvIS6fZosfgCUj4meewEqOBFd6e6st00rzWdydINozQSbBc6dVvXLTqj%2Biebb4HD0SJBJqswpq4pjaHLZBGJsWNMct%2BOG4sUufnMdGUQBdzsKRdxJLgwpJBQ7b0J%2FNEphOckedU%2BRzXf5y%2BeH6H9OXOIBw0X%2BqURGZt044wYFRBNP5eCotKcsmWw%2F1IPmhbIH9pnxwZ7NP0H59IarklRRlBHeARlhvLemA4kq65iSWQQHA2HLtVyZmAAaYgIdyDA161XKEIoIF6POnUZUAeJTPIHdyqA1lypNZPfsbrifUy%2FlKxezVdH%2FHMmxD9%2FWKphNnWT8osgTDPd7GofCz%2FmLwxBvq8ABYfFnLVHDlrV%2FLxuF62UaJ4Qs2EqajyBzg%2BSBTSoR0L%2FIQeYquXTDsUzeWUucWXLyXhlhAuRHuH1ob1xFVK43VBbLrI1JQkTAINnMxCtL6yf3k2nSl8dcIvcmPa1cH%2BXumDtgvVvDHs3a3mK9%2FKunFGO7U47oMMcgoI55fRpNQYbXesBncrW2kyCG85kgXNdgFeO8K7NPzQaxpQhaYVd%2FKeP7citV9GELapiQ%2B6zAsSnAiAZ0GRwcHPd%2FVYtT4rPAnbgwlJzMzwY6pgGik%2B8dQJucADMT%2B%2BXlRfX6T8GC5Oj%2BTOUyLM7wasEEjScnVNotx%2FuWYEfPILqN08fUNamlg4vEPYzWfjyYxdmR6VLhLmAsogQO6Zr2foC1yoCR%2Bu93JSWdQGKiW2tYIfxQQGBFkpUw5cCZpC4TtP7f1o9EjcyQMUIt%2BJ%2BVN6ViKunJbssoL%2B5%2FU%2FDTRnLY6sk7XAKsTA1YaCpgOo689zAUk3GC47ks&X-Amz-Signature=e002559759ed50f01ca95fa1a13f4acadb69376acec651db080eef1a67a00358&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTP2ABEE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIETRCuY60SNzAuVakj0JT%2BWuzgrjtjgZJVXNXScmRLcQAiBbDVogtLXppxoCr8c4pCe5Rj%2F3hiE%2FRqqtb%2F4fw7nf1ir%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM%2F1sMGmsGQKU6jxSrKtwDRk6F6rIxRXopOVlw9bnZ4WICp2PfvIS6fZosfgCUj4meewEqOBFd6e6st00rzWdydINozQSbBc6dVvXLTqj%2Biebb4HD0SJBJqswpq4pjaHLZBGJsWNMct%2BOG4sUufnMdGUQBdzsKRdxJLgwpJBQ7b0J%2FNEphOckedU%2BRzXf5y%2BeH6H9OXOIBw0X%2BqURGZt044wYFRBNP5eCotKcsmWw%2F1IPmhbIH9pnxwZ7NP0H59IarklRRlBHeARlhvLemA4kq65iSWQQHA2HLtVyZmAAaYgIdyDA161XKEIoIF6POnUZUAeJTPIHdyqA1lypNZPfsbrifUy%2FlKxezVdH%2FHMmxD9%2FWKphNnWT8osgTDPd7GofCz%2FmLwxBvq8ABYfFnLVHDlrV%2FLxuF62UaJ4Qs2EqajyBzg%2BSBTSoR0L%2FIQeYquXTDsUzeWUucWXLyXhlhAuRHuH1ob1xFVK43VBbLrI1JQkTAINnMxCtL6yf3k2nSl8dcIvcmPa1cH%2BXumDtgvVvDHs3a3mK9%2FKunFGO7U47oMMcgoI55fRpNQYbXesBncrW2kyCG85kgXNdgFeO8K7NPzQaxpQhaYVd%2FKeP7citV9GELapiQ%2B6zAsSnAiAZ0GRwcHPd%2FVYtT4rPAnbgwlJzMzwY6pgGik%2B8dQJucADMT%2B%2BXlRfX6T8GC5Oj%2BTOUyLM7wasEEjScnVNotx%2FuWYEfPILqN08fUNamlg4vEPYzWfjyYxdmR6VLhLmAsogQO6Zr2foC1yoCR%2Bu93JSWdQGKiW2tYIfxQQGBFkpUw5cCZpC4TtP7f1o9EjcyQMUIt%2BJ%2BVN6ViKunJbssoL%2B5%2FU%2FDTRnLY6sk7XAKsTA1YaCpgOo689zAUk3GC47ks&X-Amz-Signature=071eb100b5385886426f9efca6320ff4a0d121de4522f67d8f6abe09481e70ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
