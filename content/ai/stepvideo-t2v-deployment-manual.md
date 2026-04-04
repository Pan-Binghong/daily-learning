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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYFQFGSE%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUFmKPITSrlTariE64%2F67nQWcTg3ROlMq9iCdsQ9HxFAiB9Mzf7rjtQoeNtMnpMVXIr%2B%2BfKwlO0pEvnCJ6zDn4UgiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtqWIjum%2BNH9kzFuQKtwDRahFGhaq4F1dGjQ0jwC8AjhUMCu%2F%2FljIR4woEe3VPWgShzJQwNp5%2Bs2U2GfqCV6gBuErF9HrjHtpU0ynuBBQ8r6nry0wcO12D8IcX4W5Dc52ryYMUpbuxfe9PCropBOqEm5EpWQCeAz0ikG%2BymRGCviv4j68SlPUag3HqSiwpVPgVBX9FO3OBr%2F8gihxSAL1p8pocH4DpnpAfn6vNXFp64Vn4kRvNplofB1Kt5YsSlddoE%2BX%2FiQoM42OoysRgy6FW6WZTTHCadMb%2BXdQRXlv5dZE%2F0AJr0B9NdyJQcQrFNaTUCI5xrlsoAm%2BqjEA7o%2FvhYsltKzIFbBsjoyN594Sr13B29lGa%2BY2fuBqOL3SOyL7gPj5%2Fen7GJ5n7gv6IaUyu91YqUDLykiHSpHvzgUix%2BtC0htPlL10Y3fO%2B%2B6CJVYmWMwamqVPNsWqxfjCkSFZ8dtpbpb5fVqJLknSl7OjHG9BR6BjTXyPKy2ceMYhUrBy7qTJgigV59CXZfj%2FWbmh%2Bf2%2F2jdgx%2BqXa0OTg6iyqJCg0gGFaiqClUDHjQpIwp3SOSIPKEoYZrTCGDQk79z%2Brido1vbnTiJpWU4zDLJ4Isd4VBqKe7CzaY0tHzdeKoyHXLre0sDyQ%2BWF2eUw6uXBzgY6pgEnA%2BnEh8hefOkAHjFMY4hNb%2B9u%2BOLt370iTd%2Bh2gSyq0DARLpCJ1rJgynz1wOVt%2FWRbKBm8baLvMC91NBU43de6O0BKJxDevsLFpm7NXGTNPKucVogzP8E3rdR9JULOpI5zmhwKOmw5SqhoQhaJ0wvZOGp0salMfQkaQJyDuEZm7xrydy3Hf%2FmFsgL49sGjEzCG8dNS44%2BY89qlVLAQFzVnq%2BmWGxA&X-Amz-Signature=a864aa19833b3b4ea54b4745ffd3ac56944d5752dc8a9deadd1402f340832979&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYFQFGSE%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUFmKPITSrlTariE64%2F67nQWcTg3ROlMq9iCdsQ9HxFAiB9Mzf7rjtQoeNtMnpMVXIr%2B%2BfKwlO0pEvnCJ6zDn4UgiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtqWIjum%2BNH9kzFuQKtwDRahFGhaq4F1dGjQ0jwC8AjhUMCu%2F%2FljIR4woEe3VPWgShzJQwNp5%2Bs2U2GfqCV6gBuErF9HrjHtpU0ynuBBQ8r6nry0wcO12D8IcX4W5Dc52ryYMUpbuxfe9PCropBOqEm5EpWQCeAz0ikG%2BymRGCviv4j68SlPUag3HqSiwpVPgVBX9FO3OBr%2F8gihxSAL1p8pocH4DpnpAfn6vNXFp64Vn4kRvNplofB1Kt5YsSlddoE%2BX%2FiQoM42OoysRgy6FW6WZTTHCadMb%2BXdQRXlv5dZE%2F0AJr0B9NdyJQcQrFNaTUCI5xrlsoAm%2BqjEA7o%2FvhYsltKzIFbBsjoyN594Sr13B29lGa%2BY2fuBqOL3SOyL7gPj5%2Fen7GJ5n7gv6IaUyu91YqUDLykiHSpHvzgUix%2BtC0htPlL10Y3fO%2B%2B6CJVYmWMwamqVPNsWqxfjCkSFZ8dtpbpb5fVqJLknSl7OjHG9BR6BjTXyPKy2ceMYhUrBy7qTJgigV59CXZfj%2FWbmh%2Bf2%2F2jdgx%2BqXa0OTg6iyqJCg0gGFaiqClUDHjQpIwp3SOSIPKEoYZrTCGDQk79z%2Brido1vbnTiJpWU4zDLJ4Isd4VBqKe7CzaY0tHzdeKoyHXLre0sDyQ%2BWF2eUw6uXBzgY6pgEnA%2BnEh8hefOkAHjFMY4hNb%2B9u%2BOLt370iTd%2Bh2gSyq0DARLpCJ1rJgynz1wOVt%2FWRbKBm8baLvMC91NBU43de6O0BKJxDevsLFpm7NXGTNPKucVogzP8E3rdR9JULOpI5zmhwKOmw5SqhoQhaJ0wvZOGp0salMfQkaQJyDuEZm7xrydy3Hf%2FmFsgL49sGjEzCG8dNS44%2BY89qlVLAQFzVnq%2BmWGxA&X-Amz-Signature=4b40306cb87751c875045affbde6ff3edaca715f8ec3af6834ebcad6c7c63c11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYFQFGSE%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUFmKPITSrlTariE64%2F67nQWcTg3ROlMq9iCdsQ9HxFAiB9Mzf7rjtQoeNtMnpMVXIr%2B%2BfKwlO0pEvnCJ6zDn4UgiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtqWIjum%2BNH9kzFuQKtwDRahFGhaq4F1dGjQ0jwC8AjhUMCu%2F%2FljIR4woEe3VPWgShzJQwNp5%2Bs2U2GfqCV6gBuErF9HrjHtpU0ynuBBQ8r6nry0wcO12D8IcX4W5Dc52ryYMUpbuxfe9PCropBOqEm5EpWQCeAz0ikG%2BymRGCviv4j68SlPUag3HqSiwpVPgVBX9FO3OBr%2F8gihxSAL1p8pocH4DpnpAfn6vNXFp64Vn4kRvNplofB1Kt5YsSlddoE%2BX%2FiQoM42OoysRgy6FW6WZTTHCadMb%2BXdQRXlv5dZE%2F0AJr0B9NdyJQcQrFNaTUCI5xrlsoAm%2BqjEA7o%2FvhYsltKzIFbBsjoyN594Sr13B29lGa%2BY2fuBqOL3SOyL7gPj5%2Fen7GJ5n7gv6IaUyu91YqUDLykiHSpHvzgUix%2BtC0htPlL10Y3fO%2B%2B6CJVYmWMwamqVPNsWqxfjCkSFZ8dtpbpb5fVqJLknSl7OjHG9BR6BjTXyPKy2ceMYhUrBy7qTJgigV59CXZfj%2FWbmh%2Bf2%2F2jdgx%2BqXa0OTg6iyqJCg0gGFaiqClUDHjQpIwp3SOSIPKEoYZrTCGDQk79z%2Brido1vbnTiJpWU4zDLJ4Isd4VBqKe7CzaY0tHzdeKoyHXLre0sDyQ%2BWF2eUw6uXBzgY6pgEnA%2BnEh8hefOkAHjFMY4hNb%2B9u%2BOLt370iTd%2Bh2gSyq0DARLpCJ1rJgynz1wOVt%2FWRbKBm8baLvMC91NBU43de6O0BKJxDevsLFpm7NXGTNPKucVogzP8E3rdR9JULOpI5zmhwKOmw5SqhoQhaJ0wvZOGp0salMfQkaQJyDuEZm7xrydy3Hf%2FmFsgL49sGjEzCG8dNS44%2BY89qlVLAQFzVnq%2BmWGxA&X-Amz-Signature=f6bf3b7413a29f22d7022cd7c4e733df7c438710d931a8f630a320d9a35edd9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYFQFGSE%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUFmKPITSrlTariE64%2F67nQWcTg3ROlMq9iCdsQ9HxFAiB9Mzf7rjtQoeNtMnpMVXIr%2B%2BfKwlO0pEvnCJ6zDn4UgiqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtqWIjum%2BNH9kzFuQKtwDRahFGhaq4F1dGjQ0jwC8AjhUMCu%2F%2FljIR4woEe3VPWgShzJQwNp5%2Bs2U2GfqCV6gBuErF9HrjHtpU0ynuBBQ8r6nry0wcO12D8IcX4W5Dc52ryYMUpbuxfe9PCropBOqEm5EpWQCeAz0ikG%2BymRGCviv4j68SlPUag3HqSiwpVPgVBX9FO3OBr%2F8gihxSAL1p8pocH4DpnpAfn6vNXFp64Vn4kRvNplofB1Kt5YsSlddoE%2BX%2FiQoM42OoysRgy6FW6WZTTHCadMb%2BXdQRXlv5dZE%2F0AJr0B9NdyJQcQrFNaTUCI5xrlsoAm%2BqjEA7o%2FvhYsltKzIFbBsjoyN594Sr13B29lGa%2BY2fuBqOL3SOyL7gPj5%2Fen7GJ5n7gv6IaUyu91YqUDLykiHSpHvzgUix%2BtC0htPlL10Y3fO%2B%2B6CJVYmWMwamqVPNsWqxfjCkSFZ8dtpbpb5fVqJLknSl7OjHG9BR6BjTXyPKy2ceMYhUrBy7qTJgigV59CXZfj%2FWbmh%2Bf2%2F2jdgx%2BqXa0OTg6iyqJCg0gGFaiqClUDHjQpIwp3SOSIPKEoYZrTCGDQk79z%2Brido1vbnTiJpWU4zDLJ4Isd4VBqKe7CzaY0tHzdeKoyHXLre0sDyQ%2BWF2eUw6uXBzgY6pgEnA%2BnEh8hefOkAHjFMY4hNb%2B9u%2BOLt370iTd%2Bh2gSyq0DARLpCJ1rJgynz1wOVt%2FWRbKBm8baLvMC91NBU43de6O0BKJxDevsLFpm7NXGTNPKucVogzP8E3rdR9JULOpI5zmhwKOmw5SqhoQhaJ0wvZOGp0salMfQkaQJyDuEZm7xrydy3Hf%2FmFsgL49sGjEzCG8dNS44%2BY89qlVLAQFzVnq%2BmWGxA&X-Amz-Signature=8c40883ac65757abd8ed3a3305a081f8dc7b49b053b9727f44104b8ca043d031&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



