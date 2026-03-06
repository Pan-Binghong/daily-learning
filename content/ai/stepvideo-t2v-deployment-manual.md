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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LQF5ZK3%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIHWII%2BWrt6xsEB3yRMBkV2p8DDyGEIKQES6NPLk5VbzxAiEA5S5PQZ8yA7z%2BFyZvDmu1d2cP6Z%2FDiPDoZUD0iYw5%2FkIqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPR3IojEY2tI8uJ1ircA1EonKGC2dgW0gLSQu6CLE9v2BE8fO1fjrC8%2FE6Kvmag7w5S4PIfmd42dZPEFxtMlF7EbE7awOQGHMa8OdMsv2ml7pSb63kkuatP49IB1t%2BTM7fnY9QSDBS7tY9npCv%2BhT7a1O%2F3Eg5kgAXt3M6NS%2B0qz%2Bl4ciGSwOL5okxHnifRAamMPIzLPwwPAG9UX%2Fx9ubSNTDtQWh5ohDW5mJ7ZVUzx0f9ZIYfJtXwaLnCkeOicLl20%2FWythwUYvdDWwINvWT4ytpOfN%2BAoNGm%2BsJQ6nifimSOV4%2FGOk194gnwpYSJDtUayzWPiG3LbZx6VMzHEUQOtC5mV0%2FvLfJ0RoHwcZstwuDa24ETdr2F3BD5aqK5D60MF94f%2BpNbvuCuD4jriU7ssNE8Of1%2F%2FzEKZNgFga8rbDgk4HvGGJiDz6VYjm2T1%2BA8ow69rRlNHQEbqyBAe3HJUNEm5RoVPQiErqdNnKRduph4qSUWuk7QUp6c89oUdFDkuvCfXgKnn44WgJHmyYCpbX77QLjXWnIPsCKLJddO2KMxL2Jg%2FENQFqoNDQ7ZNHYE0zXNcLoA%2BxMIStenfwOJTvYY0CWDPEL%2BApG3%2F2fbhxK8Nqsu4oINDzvrKmWqlSmZ%2B5C1fVgXAVt8tMN3PqM0GOqUBaifwgdJ%2FLsQmafMPtfNLelQSTTpGj44DbdrpCD2qdUrb%2FTPj8EAfXmk4ni%2BDTkVWZXeDB34ceJrP0jbe%2BaKnrnEcvlS6emLl4zZ%2BANvyGtsm4JqWv2l%2FHCd8gGOaXaUAqdsb4I03mgPL0gUEOUSe47%2FHsWVZceG5eLLdSc7RdNhC%2FJTaEx5Hht1LpEHiywyCEYVGZgK7R70m5D0p33NBZhJzPdYJ&X-Amz-Signature=8ad83d2fabf18d2610ec0ef91bf02f01817717f1880d7e6d41c1cbfabf8ec81f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LQF5ZK3%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIHWII%2BWrt6xsEB3yRMBkV2p8DDyGEIKQES6NPLk5VbzxAiEA5S5PQZ8yA7z%2BFyZvDmu1d2cP6Z%2FDiPDoZUD0iYw5%2FkIqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPR3IojEY2tI8uJ1ircA1EonKGC2dgW0gLSQu6CLE9v2BE8fO1fjrC8%2FE6Kvmag7w5S4PIfmd42dZPEFxtMlF7EbE7awOQGHMa8OdMsv2ml7pSb63kkuatP49IB1t%2BTM7fnY9QSDBS7tY9npCv%2BhT7a1O%2F3Eg5kgAXt3M6NS%2B0qz%2Bl4ciGSwOL5okxHnifRAamMPIzLPwwPAG9UX%2Fx9ubSNTDtQWh5ohDW5mJ7ZVUzx0f9ZIYfJtXwaLnCkeOicLl20%2FWythwUYvdDWwINvWT4ytpOfN%2BAoNGm%2BsJQ6nifimSOV4%2FGOk194gnwpYSJDtUayzWPiG3LbZx6VMzHEUQOtC5mV0%2FvLfJ0RoHwcZstwuDa24ETdr2F3BD5aqK5D60MF94f%2BpNbvuCuD4jriU7ssNE8Of1%2F%2FzEKZNgFga8rbDgk4HvGGJiDz6VYjm2T1%2BA8ow69rRlNHQEbqyBAe3HJUNEm5RoVPQiErqdNnKRduph4qSUWuk7QUp6c89oUdFDkuvCfXgKnn44WgJHmyYCpbX77QLjXWnIPsCKLJddO2KMxL2Jg%2FENQFqoNDQ7ZNHYE0zXNcLoA%2BxMIStenfwOJTvYY0CWDPEL%2BApG3%2F2fbhxK8Nqsu4oINDzvrKmWqlSmZ%2B5C1fVgXAVt8tMN3PqM0GOqUBaifwgdJ%2FLsQmafMPtfNLelQSTTpGj44DbdrpCD2qdUrb%2FTPj8EAfXmk4ni%2BDTkVWZXeDB34ceJrP0jbe%2BaKnrnEcvlS6emLl4zZ%2BANvyGtsm4JqWv2l%2FHCd8gGOaXaUAqdsb4I03mgPL0gUEOUSe47%2FHsWVZceG5eLLdSc7RdNhC%2FJTaEx5Hht1LpEHiywyCEYVGZgK7R70m5D0p33NBZhJzPdYJ&X-Amz-Signature=ab28264f0729afd7661f87fa33d798053af960c617f3c945d170cc2f6cca72cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LQF5ZK3%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIHWII%2BWrt6xsEB3yRMBkV2p8DDyGEIKQES6NPLk5VbzxAiEA5S5PQZ8yA7z%2BFyZvDmu1d2cP6Z%2FDiPDoZUD0iYw5%2FkIqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPR3IojEY2tI8uJ1ircA1EonKGC2dgW0gLSQu6CLE9v2BE8fO1fjrC8%2FE6Kvmag7w5S4PIfmd42dZPEFxtMlF7EbE7awOQGHMa8OdMsv2ml7pSb63kkuatP49IB1t%2BTM7fnY9QSDBS7tY9npCv%2BhT7a1O%2F3Eg5kgAXt3M6NS%2B0qz%2Bl4ciGSwOL5okxHnifRAamMPIzLPwwPAG9UX%2Fx9ubSNTDtQWh5ohDW5mJ7ZVUzx0f9ZIYfJtXwaLnCkeOicLl20%2FWythwUYvdDWwINvWT4ytpOfN%2BAoNGm%2BsJQ6nifimSOV4%2FGOk194gnwpYSJDtUayzWPiG3LbZx6VMzHEUQOtC5mV0%2FvLfJ0RoHwcZstwuDa24ETdr2F3BD5aqK5D60MF94f%2BpNbvuCuD4jriU7ssNE8Of1%2F%2FzEKZNgFga8rbDgk4HvGGJiDz6VYjm2T1%2BA8ow69rRlNHQEbqyBAe3HJUNEm5RoVPQiErqdNnKRduph4qSUWuk7QUp6c89oUdFDkuvCfXgKnn44WgJHmyYCpbX77QLjXWnIPsCKLJddO2KMxL2Jg%2FENQFqoNDQ7ZNHYE0zXNcLoA%2BxMIStenfwOJTvYY0CWDPEL%2BApG3%2F2fbhxK8Nqsu4oINDzvrKmWqlSmZ%2B5C1fVgXAVt8tMN3PqM0GOqUBaifwgdJ%2FLsQmafMPtfNLelQSTTpGj44DbdrpCD2qdUrb%2FTPj8EAfXmk4ni%2BDTkVWZXeDB34ceJrP0jbe%2BaKnrnEcvlS6emLl4zZ%2BANvyGtsm4JqWv2l%2FHCd8gGOaXaUAqdsb4I03mgPL0gUEOUSe47%2FHsWVZceG5eLLdSc7RdNhC%2FJTaEx5Hht1LpEHiywyCEYVGZgK7R70m5D0p33NBZhJzPdYJ&X-Amz-Signature=71783a9332ca183cdbb9cb1a2384aa60c46e44beb4756859bd0b25fcd5c5b462&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LQF5ZK3%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIHWII%2BWrt6xsEB3yRMBkV2p8DDyGEIKQES6NPLk5VbzxAiEA5S5PQZ8yA7z%2BFyZvDmu1d2cP6Z%2FDiPDoZUD0iYw5%2FkIqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPR3IojEY2tI8uJ1ircA1EonKGC2dgW0gLSQu6CLE9v2BE8fO1fjrC8%2FE6Kvmag7w5S4PIfmd42dZPEFxtMlF7EbE7awOQGHMa8OdMsv2ml7pSb63kkuatP49IB1t%2BTM7fnY9QSDBS7tY9npCv%2BhT7a1O%2F3Eg5kgAXt3M6NS%2B0qz%2Bl4ciGSwOL5okxHnifRAamMPIzLPwwPAG9UX%2Fx9ubSNTDtQWh5ohDW5mJ7ZVUzx0f9ZIYfJtXwaLnCkeOicLl20%2FWythwUYvdDWwINvWT4ytpOfN%2BAoNGm%2BsJQ6nifimSOV4%2FGOk194gnwpYSJDtUayzWPiG3LbZx6VMzHEUQOtC5mV0%2FvLfJ0RoHwcZstwuDa24ETdr2F3BD5aqK5D60MF94f%2BpNbvuCuD4jriU7ssNE8Of1%2F%2FzEKZNgFga8rbDgk4HvGGJiDz6VYjm2T1%2BA8ow69rRlNHQEbqyBAe3HJUNEm5RoVPQiErqdNnKRduph4qSUWuk7QUp6c89oUdFDkuvCfXgKnn44WgJHmyYCpbX77QLjXWnIPsCKLJddO2KMxL2Jg%2FENQFqoNDQ7ZNHYE0zXNcLoA%2BxMIStenfwOJTvYY0CWDPEL%2BApG3%2F2fbhxK8Nqsu4oINDzvrKmWqlSmZ%2B5C1fVgXAVt8tMN3PqM0GOqUBaifwgdJ%2FLsQmafMPtfNLelQSTTpGj44DbdrpCD2qdUrb%2FTPj8EAfXmk4ni%2BDTkVWZXeDB34ceJrP0jbe%2BaKnrnEcvlS6emLl4zZ%2BANvyGtsm4JqWv2l%2FHCd8gGOaXaUAqdsb4I03mgPL0gUEOUSe47%2FHsWVZceG5eLLdSc7RdNhC%2FJTaEx5Hht1LpEHiywyCEYVGZgK7R70m5D0p33NBZhJzPdYJ&X-Amz-Signature=280e3ddb8db6fd46992032da45eb7b5eab8d3c51fd68c3719c6ec37853fadf62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



