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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDBEIZNY%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChxLfYHr2%2FVuy%2BkyI4ylVzkEYGTK2iVV9v5gW0X95D4wIhANc5GjUHyasuRSPf7HN1J7je%2BNmQoN8pbyT1NLG6YVJwKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpHXHbOfWeuHQAVMsq3APgqVQcX%2Bud5KG9T%2BeOtLrDq%2BUnuXBS6xPRkMlkjbJXSH5B0VrPizZHMHht149J0uvzwdzGdjU2MMWIjjOJLp%2B%2Frey33aQatwzHysuAPUtSdGhII1UMywjveuwEaQ1c2gX5r5VC1Sf61GCKEpaArKqXo%2F3HgwIh8nrrp8pHQjl%2FrFToIiOev6Rg5Nzk73eKvGQUG7c8Vm3eNO7a0wl6cDWk8A9ZUyI8c2ETim%2FLhK0SYrVcWb5pl1MVBpQSBRO4e81S%2B5HbN4ZRy3OyxuDyelav2W1w1Vw034I%2Fdolv12C5ejLGEqaZGJ0syheK4IWOG%2FeUvMMtZtlhoGMAOIFxgHS6J8N0FgGiCpyIzn5PHWfBOgNasqoQiEHDjTIHh8TmvJnW%2F0rGhU52MbeEWfG43B1Ew1Fj5rvkxtF%2BYGyADn3qOXXEYZWBfSQUC0syf%2FHMpm%2Bt5sMLHG4qhkB4nny%2BM1c%2FQYDbrQz90IpMJUh4ulWFHDP9nxsxLVQ0z3xZbOyeVDa1B2s5tcbYVSOJrbG1EWhRAYz%2BU%2Bb26981mN64FT8nDW5G3e1zc%2F98vJupBBJJU4RN4u%2FXIIgDF5Yc%2BrXP7gXEvF%2Bkqq5VS4%2Fr4v5IHYzTluOITbRX8jKbluZahjCBuc3NBjqkAU%2FyVXdh42iWI49SrEMVPZUjzRLb9bIM%2F1X4gQ5%2Fm9kuAL5XLyv1ZbwvfBUtZl%2F01pv7RZCZuujadnLISlbJGNG2dz0kAb6sYIL3Hd6HtQC35kLrQ1CQtMSX10lhbjbPTVRkXAB7aBex0slk%2BPKieyYBE6Re6jtKuhPLQMs6dH%2FMTZVXtizdiN%2B6zyNS817TSRzYrSpSAFJQczQVwlUztAraNire&X-Amz-Signature=85740af994313475b9745c4bc849bb1d1e738c71249307f2508ee2a57caf96de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDBEIZNY%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChxLfYHr2%2FVuy%2BkyI4ylVzkEYGTK2iVV9v5gW0X95D4wIhANc5GjUHyasuRSPf7HN1J7je%2BNmQoN8pbyT1NLG6YVJwKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpHXHbOfWeuHQAVMsq3APgqVQcX%2Bud5KG9T%2BeOtLrDq%2BUnuXBS6xPRkMlkjbJXSH5B0VrPizZHMHht149J0uvzwdzGdjU2MMWIjjOJLp%2B%2Frey33aQatwzHysuAPUtSdGhII1UMywjveuwEaQ1c2gX5r5VC1Sf61GCKEpaArKqXo%2F3HgwIh8nrrp8pHQjl%2FrFToIiOev6Rg5Nzk73eKvGQUG7c8Vm3eNO7a0wl6cDWk8A9ZUyI8c2ETim%2FLhK0SYrVcWb5pl1MVBpQSBRO4e81S%2B5HbN4ZRy3OyxuDyelav2W1w1Vw034I%2Fdolv12C5ejLGEqaZGJ0syheK4IWOG%2FeUvMMtZtlhoGMAOIFxgHS6J8N0FgGiCpyIzn5PHWfBOgNasqoQiEHDjTIHh8TmvJnW%2F0rGhU52MbeEWfG43B1Ew1Fj5rvkxtF%2BYGyADn3qOXXEYZWBfSQUC0syf%2FHMpm%2Bt5sMLHG4qhkB4nny%2BM1c%2FQYDbrQz90IpMJUh4ulWFHDP9nxsxLVQ0z3xZbOyeVDa1B2s5tcbYVSOJrbG1EWhRAYz%2BU%2Bb26981mN64FT8nDW5G3e1zc%2F98vJupBBJJU4RN4u%2FXIIgDF5Yc%2BrXP7gXEvF%2Bkqq5VS4%2Fr4v5IHYzTluOITbRX8jKbluZahjCBuc3NBjqkAU%2FyVXdh42iWI49SrEMVPZUjzRLb9bIM%2F1X4gQ5%2Fm9kuAL5XLyv1ZbwvfBUtZl%2F01pv7RZCZuujadnLISlbJGNG2dz0kAb6sYIL3Hd6HtQC35kLrQ1CQtMSX10lhbjbPTVRkXAB7aBex0slk%2BPKieyYBE6Re6jtKuhPLQMs6dH%2FMTZVXtizdiN%2B6zyNS817TSRzYrSpSAFJQczQVwlUztAraNire&X-Amz-Signature=f29c9c8f3ec9d31d3138ed70f861a6abd810aee2edf5021833fe4a83eee78819&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDBEIZNY%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChxLfYHr2%2FVuy%2BkyI4ylVzkEYGTK2iVV9v5gW0X95D4wIhANc5GjUHyasuRSPf7HN1J7je%2BNmQoN8pbyT1NLG6YVJwKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpHXHbOfWeuHQAVMsq3APgqVQcX%2Bud5KG9T%2BeOtLrDq%2BUnuXBS6xPRkMlkjbJXSH5B0VrPizZHMHht149J0uvzwdzGdjU2MMWIjjOJLp%2B%2Frey33aQatwzHysuAPUtSdGhII1UMywjveuwEaQ1c2gX5r5VC1Sf61GCKEpaArKqXo%2F3HgwIh8nrrp8pHQjl%2FrFToIiOev6Rg5Nzk73eKvGQUG7c8Vm3eNO7a0wl6cDWk8A9ZUyI8c2ETim%2FLhK0SYrVcWb5pl1MVBpQSBRO4e81S%2B5HbN4ZRy3OyxuDyelav2W1w1Vw034I%2Fdolv12C5ejLGEqaZGJ0syheK4IWOG%2FeUvMMtZtlhoGMAOIFxgHS6J8N0FgGiCpyIzn5PHWfBOgNasqoQiEHDjTIHh8TmvJnW%2F0rGhU52MbeEWfG43B1Ew1Fj5rvkxtF%2BYGyADn3qOXXEYZWBfSQUC0syf%2FHMpm%2Bt5sMLHG4qhkB4nny%2BM1c%2FQYDbrQz90IpMJUh4ulWFHDP9nxsxLVQ0z3xZbOyeVDa1B2s5tcbYVSOJrbG1EWhRAYz%2BU%2Bb26981mN64FT8nDW5G3e1zc%2F98vJupBBJJU4RN4u%2FXIIgDF5Yc%2BrXP7gXEvF%2Bkqq5VS4%2Fr4v5IHYzTluOITbRX8jKbluZahjCBuc3NBjqkAU%2FyVXdh42iWI49SrEMVPZUjzRLb9bIM%2F1X4gQ5%2Fm9kuAL5XLyv1ZbwvfBUtZl%2F01pv7RZCZuujadnLISlbJGNG2dz0kAb6sYIL3Hd6HtQC35kLrQ1CQtMSX10lhbjbPTVRkXAB7aBex0slk%2BPKieyYBE6Re6jtKuhPLQMs6dH%2FMTZVXtizdiN%2B6zyNS817TSRzYrSpSAFJQczQVwlUztAraNire&X-Amz-Signature=10b9a11dfeb95440c4c98fc4d6dafa2083b3f9f6e9d9d6b2e3e33a6f9686553c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDBEIZNY%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChxLfYHr2%2FVuy%2BkyI4ylVzkEYGTK2iVV9v5gW0X95D4wIhANc5GjUHyasuRSPf7HN1J7je%2BNmQoN8pbyT1NLG6YVJwKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpHXHbOfWeuHQAVMsq3APgqVQcX%2Bud5KG9T%2BeOtLrDq%2BUnuXBS6xPRkMlkjbJXSH5B0VrPizZHMHht149J0uvzwdzGdjU2MMWIjjOJLp%2B%2Frey33aQatwzHysuAPUtSdGhII1UMywjveuwEaQ1c2gX5r5VC1Sf61GCKEpaArKqXo%2F3HgwIh8nrrp8pHQjl%2FrFToIiOev6Rg5Nzk73eKvGQUG7c8Vm3eNO7a0wl6cDWk8A9ZUyI8c2ETim%2FLhK0SYrVcWb5pl1MVBpQSBRO4e81S%2B5HbN4ZRy3OyxuDyelav2W1w1Vw034I%2Fdolv12C5ejLGEqaZGJ0syheK4IWOG%2FeUvMMtZtlhoGMAOIFxgHS6J8N0FgGiCpyIzn5PHWfBOgNasqoQiEHDjTIHh8TmvJnW%2F0rGhU52MbeEWfG43B1Ew1Fj5rvkxtF%2BYGyADn3qOXXEYZWBfSQUC0syf%2FHMpm%2Bt5sMLHG4qhkB4nny%2BM1c%2FQYDbrQz90IpMJUh4ulWFHDP9nxsxLVQ0z3xZbOyeVDa1B2s5tcbYVSOJrbG1EWhRAYz%2BU%2Bb26981mN64FT8nDW5G3e1zc%2F98vJupBBJJU4RN4u%2FXIIgDF5Yc%2BrXP7gXEvF%2Bkqq5VS4%2Fr4v5IHYzTluOITbRX8jKbluZahjCBuc3NBjqkAU%2FyVXdh42iWI49SrEMVPZUjzRLb9bIM%2F1X4gQ5%2Fm9kuAL5XLyv1ZbwvfBUtZl%2F01pv7RZCZuujadnLISlbJGNG2dz0kAb6sYIL3Hd6HtQC35kLrQ1CQtMSX10lhbjbPTVRkXAB7aBex0slk%2BPKieyYBE6Re6jtKuhPLQMs6dH%2FMTZVXtizdiN%2B6zyNS817TSRzYrSpSAFJQczQVwlUztAraNire&X-Amz-Signature=808409d2309e44f3c1b8f801a34774c14d7e3202b5271d837f4cdfc6d5c4dd6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



