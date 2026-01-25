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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPIPSWYW%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCGrrwt%2BIAulbmk1qgm%2Bg9BmseAMBOBJnItrLfRGhQ2OwIgPGIwbgdRApbQafA5zOjAl6nvOTN44nRlAxvTUWFy0s4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDEsiYQPCYoAujmYOSrcA1VN80q1BSeQ%2F%2FYtfWsILlnV%2B8zMuqu07wi2Cnri7hx%2BBbEmaWxu5DlXGEd5zJtGeNMaPDgp6G1K9%2F3RJP%2BdI4P0Yv6QsKgRz78xcF%2BaQoqjvDSZnW5kOZmqCyHO%2F6hAy0eemb9eia86sAPJZnW6VYvvqv8Ru3IxzdeIL0FRT7L3sEybnLS91%2FSoF0JUdOr2gDFTI%2FHOCEp8LKoOT5J8XEzbxU%2FVKikbFxIZbSRIGxYxVEN6X6A9onvQ2lMnaCpIADQi2kBUkSXFoq5VjhLpxN51kEJO4WhW%2BXcOCFN0ugY0qvB911Pe6H%2Fp7tG0nHQtxQRt748KqKB8WTw%2FYCA8V2K4MAbZYNYUDIUOsT4Y%2FklJ0WdvEeyEFDIfFNqCTg%2FX5ZMRYgTTpDJadMdO84P42qZDYGELnsaqonR4jH3fLda7MPr6CLnALYMJfm3BCvkiOrwGUCwMuflxMtVvN7p9M24Q57mrDTixx56hVK5xQT%2BtO7zZfHqWJUNtR%2BWjarNvGct6BPCJ1G%2FgzFLwDA3ZZ4%2FNlsh8o1TZZICqeE7EpVQGEVBONogDYRa%2BKjH3rwy2Lw3w%2F6EA2RJZ%2BTJvbeBDY1%2FOy2yeb%2FQphqcFRvRFo0NRzba1BDmfZWaSD7asMPyF1ssGOqUBbzD5eHfPuSQo9wb2zHECV33LGB8DCeaFOuSQDTI5LkQHCgUFg6XEN82LAJr75S7Bl7LeP9Pm6ialuFzhfoT6r8ZQxEToAP9ldHVK5QHi8DHRmHHvrEvPaezTQIHz7O2RETZt7rVqBWQLqB5Bn1u3tmazJZrAnZcClNeCcJ8QBbvjPOAf6kXCC1RJ2m%2B9I4MIAvTlgdATLDzG4DbGfMxYm8522vVw&X-Amz-Signature=39e422367cc434f05579f34cfb022eca9f165fec455266d4a30059269b1d66f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPIPSWYW%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCGrrwt%2BIAulbmk1qgm%2Bg9BmseAMBOBJnItrLfRGhQ2OwIgPGIwbgdRApbQafA5zOjAl6nvOTN44nRlAxvTUWFy0s4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDEsiYQPCYoAujmYOSrcA1VN80q1BSeQ%2F%2FYtfWsILlnV%2B8zMuqu07wi2Cnri7hx%2BBbEmaWxu5DlXGEd5zJtGeNMaPDgp6G1K9%2F3RJP%2BdI4P0Yv6QsKgRz78xcF%2BaQoqjvDSZnW5kOZmqCyHO%2F6hAy0eemb9eia86sAPJZnW6VYvvqv8Ru3IxzdeIL0FRT7L3sEybnLS91%2FSoF0JUdOr2gDFTI%2FHOCEp8LKoOT5J8XEzbxU%2FVKikbFxIZbSRIGxYxVEN6X6A9onvQ2lMnaCpIADQi2kBUkSXFoq5VjhLpxN51kEJO4WhW%2BXcOCFN0ugY0qvB911Pe6H%2Fp7tG0nHQtxQRt748KqKB8WTw%2FYCA8V2K4MAbZYNYUDIUOsT4Y%2FklJ0WdvEeyEFDIfFNqCTg%2FX5ZMRYgTTpDJadMdO84P42qZDYGELnsaqonR4jH3fLda7MPr6CLnALYMJfm3BCvkiOrwGUCwMuflxMtVvN7p9M24Q57mrDTixx56hVK5xQT%2BtO7zZfHqWJUNtR%2BWjarNvGct6BPCJ1G%2FgzFLwDA3ZZ4%2FNlsh8o1TZZICqeE7EpVQGEVBONogDYRa%2BKjH3rwy2Lw3w%2F6EA2RJZ%2BTJvbeBDY1%2FOy2yeb%2FQphqcFRvRFo0NRzba1BDmfZWaSD7asMPyF1ssGOqUBbzD5eHfPuSQo9wb2zHECV33LGB8DCeaFOuSQDTI5LkQHCgUFg6XEN82LAJr75S7Bl7LeP9Pm6ialuFzhfoT6r8ZQxEToAP9ldHVK5QHi8DHRmHHvrEvPaezTQIHz7O2RETZt7rVqBWQLqB5Bn1u3tmazJZrAnZcClNeCcJ8QBbvjPOAf6kXCC1RJ2m%2B9I4MIAvTlgdATLDzG4DbGfMxYm8522vVw&X-Amz-Signature=be87dd55ca4b58f18344d9498fbfd57b4af694ae2dfe314729d9f048d6f6121a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPIPSWYW%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCGrrwt%2BIAulbmk1qgm%2Bg9BmseAMBOBJnItrLfRGhQ2OwIgPGIwbgdRApbQafA5zOjAl6nvOTN44nRlAxvTUWFy0s4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDEsiYQPCYoAujmYOSrcA1VN80q1BSeQ%2F%2FYtfWsILlnV%2B8zMuqu07wi2Cnri7hx%2BBbEmaWxu5DlXGEd5zJtGeNMaPDgp6G1K9%2F3RJP%2BdI4P0Yv6QsKgRz78xcF%2BaQoqjvDSZnW5kOZmqCyHO%2F6hAy0eemb9eia86sAPJZnW6VYvvqv8Ru3IxzdeIL0FRT7L3sEybnLS91%2FSoF0JUdOr2gDFTI%2FHOCEp8LKoOT5J8XEzbxU%2FVKikbFxIZbSRIGxYxVEN6X6A9onvQ2lMnaCpIADQi2kBUkSXFoq5VjhLpxN51kEJO4WhW%2BXcOCFN0ugY0qvB911Pe6H%2Fp7tG0nHQtxQRt748KqKB8WTw%2FYCA8V2K4MAbZYNYUDIUOsT4Y%2FklJ0WdvEeyEFDIfFNqCTg%2FX5ZMRYgTTpDJadMdO84P42qZDYGELnsaqonR4jH3fLda7MPr6CLnALYMJfm3BCvkiOrwGUCwMuflxMtVvN7p9M24Q57mrDTixx56hVK5xQT%2BtO7zZfHqWJUNtR%2BWjarNvGct6BPCJ1G%2FgzFLwDA3ZZ4%2FNlsh8o1TZZICqeE7EpVQGEVBONogDYRa%2BKjH3rwy2Lw3w%2F6EA2RJZ%2BTJvbeBDY1%2FOy2yeb%2FQphqcFRvRFo0NRzba1BDmfZWaSD7asMPyF1ssGOqUBbzD5eHfPuSQo9wb2zHECV33LGB8DCeaFOuSQDTI5LkQHCgUFg6XEN82LAJr75S7Bl7LeP9Pm6ialuFzhfoT6r8ZQxEToAP9ldHVK5QHi8DHRmHHvrEvPaezTQIHz7O2RETZt7rVqBWQLqB5Bn1u3tmazJZrAnZcClNeCcJ8QBbvjPOAf6kXCC1RJ2m%2B9I4MIAvTlgdATLDzG4DbGfMxYm8522vVw&X-Amz-Signature=dd55993d9d886589d487fd3caf77a1677bd43ba05d35f03eec6c61ab1e7d4c4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPIPSWYW%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCGrrwt%2BIAulbmk1qgm%2Bg9BmseAMBOBJnItrLfRGhQ2OwIgPGIwbgdRApbQafA5zOjAl6nvOTN44nRlAxvTUWFy0s4q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDEsiYQPCYoAujmYOSrcA1VN80q1BSeQ%2F%2FYtfWsILlnV%2B8zMuqu07wi2Cnri7hx%2BBbEmaWxu5DlXGEd5zJtGeNMaPDgp6G1K9%2F3RJP%2BdI4P0Yv6QsKgRz78xcF%2BaQoqjvDSZnW5kOZmqCyHO%2F6hAy0eemb9eia86sAPJZnW6VYvvqv8Ru3IxzdeIL0FRT7L3sEybnLS91%2FSoF0JUdOr2gDFTI%2FHOCEp8LKoOT5J8XEzbxU%2FVKikbFxIZbSRIGxYxVEN6X6A9onvQ2lMnaCpIADQi2kBUkSXFoq5VjhLpxN51kEJO4WhW%2BXcOCFN0ugY0qvB911Pe6H%2Fp7tG0nHQtxQRt748KqKB8WTw%2FYCA8V2K4MAbZYNYUDIUOsT4Y%2FklJ0WdvEeyEFDIfFNqCTg%2FX5ZMRYgTTpDJadMdO84P42qZDYGELnsaqonR4jH3fLda7MPr6CLnALYMJfm3BCvkiOrwGUCwMuflxMtVvN7p9M24Q57mrDTixx56hVK5xQT%2BtO7zZfHqWJUNtR%2BWjarNvGct6BPCJ1G%2FgzFLwDA3ZZ4%2FNlsh8o1TZZICqeE7EpVQGEVBONogDYRa%2BKjH3rwy2Lw3w%2F6EA2RJZ%2BTJvbeBDY1%2FOy2yeb%2FQphqcFRvRFo0NRzba1BDmfZWaSD7asMPyF1ssGOqUBbzD5eHfPuSQo9wb2zHECV33LGB8DCeaFOuSQDTI5LkQHCgUFg6XEN82LAJr75S7Bl7LeP9Pm6ialuFzhfoT6r8ZQxEToAP9ldHVK5QHi8DHRmHHvrEvPaezTQIHz7O2RETZt7rVqBWQLqB5Bn1u3tmazJZrAnZcClNeCcJ8QBbvjPOAf6kXCC1RJ2m%2B9I4MIAvTlgdATLDzG4DbGfMxYm8522vVw&X-Amz-Signature=80370be9bd6ef366f1ff7d6f4b38ad171d12decafe7b8b46e1dac93dff4f9386&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



