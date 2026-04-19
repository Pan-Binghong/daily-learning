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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZATW7T%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIC%2BF8mTB03f8oXhIKUUOB6hM%2F2qQMY3D%2B9oVKwPr%2Bz%2BWAiAHP2QUcQdRw2kcUzitgWNmHNYDhihJ8PaZEFVBbvuVLCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBNekDC0sHjDpy%2FqoKtwDqJCOLxV2Ei2EdVA6O5vbrXtMGLOA41Z3nvSDNE1ireSO4smnYTpYQdP9z%2BnJJX6UY2Mg3ACSNB%2FL0YHXcM1%2BGA1NHDHHFgGscxDuyGJqmF9RxRB6yc0uZbMCc8PEqOAoHn1vuSi2psWHinnVtgfgGUXVB%2F1PcutawzfcpizHku57I%2F1DdFGFzKlgaL2MHb0%2BraLsFfcfSJVPBNCbWhHYVQYjeTU7aBy04KYdbtJDUluj92gqqhWzkGHwb2p5gAdz6LtA8cOVCcp7IhlTqTjkPJRbCep7hZliWNXobaV2yLcQpd4LcfW0Q7JQ9EflzIeIIxIMVEEGncBZWBhqnBzcsuyo5rx%2Fk2MbDb1qw7RVVNUoffOBSY2bcUg3QHgN8zeJmP3t%2FOZj6WLyEQN2GIQT2XoYzqWqrAsPzCXHoVF5j2j97smShbeF0f7YaYk%2F%2FD3uvXZRW1pERZ1O33MyEXzQ%2BGjfXwUs2Hrcpbv0x%2FuToQOvCh4QjZN5PPTJjwlzjXHSVKr2QAkzZaglWQ9iw3ALN0Eu%2BOHAGwEHs4VwT64Rgl2dtP7uNIVWxSq0kv8USk%2BsJmywS0DL%2FEKrpnEoEIYMIGGa9DIBnYrqW1ShXuh5YS4SS3LNhd7YiCI%2Boi0wy9yQzwY6pgH0HeMSvI%2BN1%2B9lU34uHRehAvmTZlLwtq2DuKPDd%2Fjzd5GitIDWOT%2FpinWXX8vxub70Qs14U1dD2QSV2v3WeF%2BSfAN28j73gGhiUSMuj7aaEbZEjJtfFXIxG4OR%2B7YJSYJDgCH1XuPULQCbYvxx%2BQuJbdWLPK%2FPOSw%2F6nWNrxTdthKtnQ14NnWRqZm9I6gZ2tTuc%2Bd4Lf7Er7oLodqSKN9kCsiwCLvm&X-Amz-Signature=e4fd6aadb125d5362c336a7ddb841d32943b23b395ccb81bd406ae5f4d76d863&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZATW7T%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIC%2BF8mTB03f8oXhIKUUOB6hM%2F2qQMY3D%2B9oVKwPr%2Bz%2BWAiAHP2QUcQdRw2kcUzitgWNmHNYDhihJ8PaZEFVBbvuVLCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBNekDC0sHjDpy%2FqoKtwDqJCOLxV2Ei2EdVA6O5vbrXtMGLOA41Z3nvSDNE1ireSO4smnYTpYQdP9z%2BnJJX6UY2Mg3ACSNB%2FL0YHXcM1%2BGA1NHDHHFgGscxDuyGJqmF9RxRB6yc0uZbMCc8PEqOAoHn1vuSi2psWHinnVtgfgGUXVB%2F1PcutawzfcpizHku57I%2F1DdFGFzKlgaL2MHb0%2BraLsFfcfSJVPBNCbWhHYVQYjeTU7aBy04KYdbtJDUluj92gqqhWzkGHwb2p5gAdz6LtA8cOVCcp7IhlTqTjkPJRbCep7hZliWNXobaV2yLcQpd4LcfW0Q7JQ9EflzIeIIxIMVEEGncBZWBhqnBzcsuyo5rx%2Fk2MbDb1qw7RVVNUoffOBSY2bcUg3QHgN8zeJmP3t%2FOZj6WLyEQN2GIQT2XoYzqWqrAsPzCXHoVF5j2j97smShbeF0f7YaYk%2F%2FD3uvXZRW1pERZ1O33MyEXzQ%2BGjfXwUs2Hrcpbv0x%2FuToQOvCh4QjZN5PPTJjwlzjXHSVKr2QAkzZaglWQ9iw3ALN0Eu%2BOHAGwEHs4VwT64Rgl2dtP7uNIVWxSq0kv8USk%2BsJmywS0DL%2FEKrpnEoEIYMIGGa9DIBnYrqW1ShXuh5YS4SS3LNhd7YiCI%2Boi0wy9yQzwY6pgH0HeMSvI%2BN1%2B9lU34uHRehAvmTZlLwtq2DuKPDd%2Fjzd5GitIDWOT%2FpinWXX8vxub70Qs14U1dD2QSV2v3WeF%2BSfAN28j73gGhiUSMuj7aaEbZEjJtfFXIxG4OR%2B7YJSYJDgCH1XuPULQCbYvxx%2BQuJbdWLPK%2FPOSw%2F6nWNrxTdthKtnQ14NnWRqZm9I6gZ2tTuc%2Bd4Lf7Er7oLodqSKN9kCsiwCLvm&X-Amz-Signature=88eaaefd3bd1c20f4aa984aa94fbd8992f3836edbdc9cd351c3d752ccf4539d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZATW7T%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIC%2BF8mTB03f8oXhIKUUOB6hM%2F2qQMY3D%2B9oVKwPr%2Bz%2BWAiAHP2QUcQdRw2kcUzitgWNmHNYDhihJ8PaZEFVBbvuVLCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBNekDC0sHjDpy%2FqoKtwDqJCOLxV2Ei2EdVA6O5vbrXtMGLOA41Z3nvSDNE1ireSO4smnYTpYQdP9z%2BnJJX6UY2Mg3ACSNB%2FL0YHXcM1%2BGA1NHDHHFgGscxDuyGJqmF9RxRB6yc0uZbMCc8PEqOAoHn1vuSi2psWHinnVtgfgGUXVB%2F1PcutawzfcpizHku57I%2F1DdFGFzKlgaL2MHb0%2BraLsFfcfSJVPBNCbWhHYVQYjeTU7aBy04KYdbtJDUluj92gqqhWzkGHwb2p5gAdz6LtA8cOVCcp7IhlTqTjkPJRbCep7hZliWNXobaV2yLcQpd4LcfW0Q7JQ9EflzIeIIxIMVEEGncBZWBhqnBzcsuyo5rx%2Fk2MbDb1qw7RVVNUoffOBSY2bcUg3QHgN8zeJmP3t%2FOZj6WLyEQN2GIQT2XoYzqWqrAsPzCXHoVF5j2j97smShbeF0f7YaYk%2F%2FD3uvXZRW1pERZ1O33MyEXzQ%2BGjfXwUs2Hrcpbv0x%2FuToQOvCh4QjZN5PPTJjwlzjXHSVKr2QAkzZaglWQ9iw3ALN0Eu%2BOHAGwEHs4VwT64Rgl2dtP7uNIVWxSq0kv8USk%2BsJmywS0DL%2FEKrpnEoEIYMIGGa9DIBnYrqW1ShXuh5YS4SS3LNhd7YiCI%2Boi0wy9yQzwY6pgH0HeMSvI%2BN1%2B9lU34uHRehAvmTZlLwtq2DuKPDd%2Fjzd5GitIDWOT%2FpinWXX8vxub70Qs14U1dD2QSV2v3WeF%2BSfAN28j73gGhiUSMuj7aaEbZEjJtfFXIxG4OR%2B7YJSYJDgCH1XuPULQCbYvxx%2BQuJbdWLPK%2FPOSw%2F6nWNrxTdthKtnQ14NnWRqZm9I6gZ2tTuc%2Bd4Lf7Er7oLodqSKN9kCsiwCLvm&X-Amz-Signature=f865a4ef8b1a68c78407b8d20f0dc7f1cc3c7a663d16c50e0a16a8d4abd49abf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFZATW7T%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIC%2BF8mTB03f8oXhIKUUOB6hM%2F2qQMY3D%2B9oVKwPr%2Bz%2BWAiAHP2QUcQdRw2kcUzitgWNmHNYDhihJ8PaZEFVBbvuVLCqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBNekDC0sHjDpy%2FqoKtwDqJCOLxV2Ei2EdVA6O5vbrXtMGLOA41Z3nvSDNE1ireSO4smnYTpYQdP9z%2BnJJX6UY2Mg3ACSNB%2FL0YHXcM1%2BGA1NHDHHFgGscxDuyGJqmF9RxRB6yc0uZbMCc8PEqOAoHn1vuSi2psWHinnVtgfgGUXVB%2F1PcutawzfcpizHku57I%2F1DdFGFzKlgaL2MHb0%2BraLsFfcfSJVPBNCbWhHYVQYjeTU7aBy04KYdbtJDUluj92gqqhWzkGHwb2p5gAdz6LtA8cOVCcp7IhlTqTjkPJRbCep7hZliWNXobaV2yLcQpd4LcfW0Q7JQ9EflzIeIIxIMVEEGncBZWBhqnBzcsuyo5rx%2Fk2MbDb1qw7RVVNUoffOBSY2bcUg3QHgN8zeJmP3t%2FOZj6WLyEQN2GIQT2XoYzqWqrAsPzCXHoVF5j2j97smShbeF0f7YaYk%2F%2FD3uvXZRW1pERZ1O33MyEXzQ%2BGjfXwUs2Hrcpbv0x%2FuToQOvCh4QjZN5PPTJjwlzjXHSVKr2QAkzZaglWQ9iw3ALN0Eu%2BOHAGwEHs4VwT64Rgl2dtP7uNIVWxSq0kv8USk%2BsJmywS0DL%2FEKrpnEoEIYMIGGa9DIBnYrqW1ShXuh5YS4SS3LNhd7YiCI%2Boi0wy9yQzwY6pgH0HeMSvI%2BN1%2B9lU34uHRehAvmTZlLwtq2DuKPDd%2Fjzd5GitIDWOT%2FpinWXX8vxub70Qs14U1dD2QSV2v3WeF%2BSfAN28j73gGhiUSMuj7aaEbZEjJtfFXIxG4OR%2B7YJSYJDgCH1XuPULQCbYvxx%2BQuJbdWLPK%2FPOSw%2F6nWNrxTdthKtnQ14NnWRqZm9I6gZ2tTuc%2Bd4Lf7Er7oLodqSKN9kCsiwCLvm&X-Amz-Signature=2be46fdc97608e4ff85280995383912bf22a562db97559b1706a1cc0329f6c20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



