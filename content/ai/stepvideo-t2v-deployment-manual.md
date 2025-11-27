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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B6ZXXIZ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSRA%2BMeWJ58%2Bnwo2pQW7QFmuz4NG30AMh5rXgyCaepiwIgCL9cDR4EBSYVS4x0c33BH0bm1muKw8oTzb5iBI22JmoqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2wJ4t%2FrYAunNFjyyrcA3gXdpxy80%2BF8OuFUhVApF5bYr%2FwdUm8oHvpgTRdQtMXbkEONgElQEQQ2olDAitzwD0BthO5QEqB8G8mKAD7lXO%2FU1W46khyALEFNqqDo8FwShNYZiUUPgFlRS%2Bog2%2FJlR8ebO0JC1L2%2FN3YcMd7oBih5nTV1PHGhED90hWSIcnYOklzMBJc9zlHxBvcJvwpE%2Be1zBZ2ipb8WACGmY6KF22p6C%2BIrjkU9Xi%2Fg%2Fr4oyefDCtPv0YRrmKER2mF9SKaxNkOVDEhOzSUbmL%2FywjSLkrhdhAPKiANz6FeieD%2F4j2GLZXRSctHzQ1hik6U66tHxHhnouliMz2NeuSLU7%2BH5isqITUw6L83xd5Jocdia5NIu9VHDod1a2QnyoO06xQy30UN7gBVG6pYjzL4WSEDBEf4qDg8lQ3vsDAK5HgbFfgQeKOCP4PedH65p0U%2BYxoy1EVLAV9q09KKIE0ll5mKaGPBapuwXNbkMJgsSY9ql92%2FK4Za3VyHGrQT5onEybsY0eNoiffy%2B44%2FxrjtaD4gMBU0MnCQGtNEQrBjX1HWR%2F0na8NAP9zDnnAZ4fG1P9pMx93yHBuDBIF0JerrhnpgKZN0hv8ZAvA79eZyifr3JQFU4LXxOQIyqQmcEsqsMJzNnskGOqUBYNZC50CLM7OlCO7Oakui0v1Y4B%2BlnrzyZc0opeC%2Ft6QC2uPtorjlLc1ZS8pyvLfG67fyiQWiYSa%2FmM1j7YVsuDE94rvhQY9mbY5mwrshlgURu7RT20Jfg8m3hIXdesLnWnUBlSl1RJTtBbwoHOAKBpBZEPh%2F0JyUDI%2BLMA9RKbbdAtMNM2UeQX6V%2BA3YcPhUFl9c8Lr2YB87N9yDdTuUuII%2FaNV5&X-Amz-Signature=9d79351e8b6bc81696daf8f81d33ccd48b42fee39a64a0dc47cecd828ef1301e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B6ZXXIZ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSRA%2BMeWJ58%2Bnwo2pQW7QFmuz4NG30AMh5rXgyCaepiwIgCL9cDR4EBSYVS4x0c33BH0bm1muKw8oTzb5iBI22JmoqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2wJ4t%2FrYAunNFjyyrcA3gXdpxy80%2BF8OuFUhVApF5bYr%2FwdUm8oHvpgTRdQtMXbkEONgElQEQQ2olDAitzwD0BthO5QEqB8G8mKAD7lXO%2FU1W46khyALEFNqqDo8FwShNYZiUUPgFlRS%2Bog2%2FJlR8ebO0JC1L2%2FN3YcMd7oBih5nTV1PHGhED90hWSIcnYOklzMBJc9zlHxBvcJvwpE%2Be1zBZ2ipb8WACGmY6KF22p6C%2BIrjkU9Xi%2Fg%2Fr4oyefDCtPv0YRrmKER2mF9SKaxNkOVDEhOzSUbmL%2FywjSLkrhdhAPKiANz6FeieD%2F4j2GLZXRSctHzQ1hik6U66tHxHhnouliMz2NeuSLU7%2BH5isqITUw6L83xd5Jocdia5NIu9VHDod1a2QnyoO06xQy30UN7gBVG6pYjzL4WSEDBEf4qDg8lQ3vsDAK5HgbFfgQeKOCP4PedH65p0U%2BYxoy1EVLAV9q09KKIE0ll5mKaGPBapuwXNbkMJgsSY9ql92%2FK4Za3VyHGrQT5onEybsY0eNoiffy%2B44%2FxrjtaD4gMBU0MnCQGtNEQrBjX1HWR%2F0na8NAP9zDnnAZ4fG1P9pMx93yHBuDBIF0JerrhnpgKZN0hv8ZAvA79eZyifr3JQFU4LXxOQIyqQmcEsqsMJzNnskGOqUBYNZC50CLM7OlCO7Oakui0v1Y4B%2BlnrzyZc0opeC%2Ft6QC2uPtorjlLc1ZS8pyvLfG67fyiQWiYSa%2FmM1j7YVsuDE94rvhQY9mbY5mwrshlgURu7RT20Jfg8m3hIXdesLnWnUBlSl1RJTtBbwoHOAKBpBZEPh%2F0JyUDI%2BLMA9RKbbdAtMNM2UeQX6V%2BA3YcPhUFl9c8Lr2YB87N9yDdTuUuII%2FaNV5&X-Amz-Signature=9e6e5e1fa50e145707dcb7a4994533026b69b357d90dc9f68727df25c1666fb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B6ZXXIZ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSRA%2BMeWJ58%2Bnwo2pQW7QFmuz4NG30AMh5rXgyCaepiwIgCL9cDR4EBSYVS4x0c33BH0bm1muKw8oTzb5iBI22JmoqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2wJ4t%2FrYAunNFjyyrcA3gXdpxy80%2BF8OuFUhVApF5bYr%2FwdUm8oHvpgTRdQtMXbkEONgElQEQQ2olDAitzwD0BthO5QEqB8G8mKAD7lXO%2FU1W46khyALEFNqqDo8FwShNYZiUUPgFlRS%2Bog2%2FJlR8ebO0JC1L2%2FN3YcMd7oBih5nTV1PHGhED90hWSIcnYOklzMBJc9zlHxBvcJvwpE%2Be1zBZ2ipb8WACGmY6KF22p6C%2BIrjkU9Xi%2Fg%2Fr4oyefDCtPv0YRrmKER2mF9SKaxNkOVDEhOzSUbmL%2FywjSLkrhdhAPKiANz6FeieD%2F4j2GLZXRSctHzQ1hik6U66tHxHhnouliMz2NeuSLU7%2BH5isqITUw6L83xd5Jocdia5NIu9VHDod1a2QnyoO06xQy30UN7gBVG6pYjzL4WSEDBEf4qDg8lQ3vsDAK5HgbFfgQeKOCP4PedH65p0U%2BYxoy1EVLAV9q09KKIE0ll5mKaGPBapuwXNbkMJgsSY9ql92%2FK4Za3VyHGrQT5onEybsY0eNoiffy%2B44%2FxrjtaD4gMBU0MnCQGtNEQrBjX1HWR%2F0na8NAP9zDnnAZ4fG1P9pMx93yHBuDBIF0JerrhnpgKZN0hv8ZAvA79eZyifr3JQFU4LXxOQIyqQmcEsqsMJzNnskGOqUBYNZC50CLM7OlCO7Oakui0v1Y4B%2BlnrzyZc0opeC%2Ft6QC2uPtorjlLc1ZS8pyvLfG67fyiQWiYSa%2FmM1j7YVsuDE94rvhQY9mbY5mwrshlgURu7RT20Jfg8m3hIXdesLnWnUBlSl1RJTtBbwoHOAKBpBZEPh%2F0JyUDI%2BLMA9RKbbdAtMNM2UeQX6V%2BA3YcPhUFl9c8Lr2YB87N9yDdTuUuII%2FaNV5&X-Amz-Signature=d8ba3a5d884a8f5abb777dabb0e9b6f10e0b44022fff76eef8f18bfa92833fd8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B6ZXXIZ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSRA%2BMeWJ58%2Bnwo2pQW7QFmuz4NG30AMh5rXgyCaepiwIgCL9cDR4EBSYVS4x0c33BH0bm1muKw8oTzb5iBI22JmoqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK2wJ4t%2FrYAunNFjyyrcA3gXdpxy80%2BF8OuFUhVApF5bYr%2FwdUm8oHvpgTRdQtMXbkEONgElQEQQ2olDAitzwD0BthO5QEqB8G8mKAD7lXO%2FU1W46khyALEFNqqDo8FwShNYZiUUPgFlRS%2Bog2%2FJlR8ebO0JC1L2%2FN3YcMd7oBih5nTV1PHGhED90hWSIcnYOklzMBJc9zlHxBvcJvwpE%2Be1zBZ2ipb8WACGmY6KF22p6C%2BIrjkU9Xi%2Fg%2Fr4oyefDCtPv0YRrmKER2mF9SKaxNkOVDEhOzSUbmL%2FywjSLkrhdhAPKiANz6FeieD%2F4j2GLZXRSctHzQ1hik6U66tHxHhnouliMz2NeuSLU7%2BH5isqITUw6L83xd5Jocdia5NIu9VHDod1a2QnyoO06xQy30UN7gBVG6pYjzL4WSEDBEf4qDg8lQ3vsDAK5HgbFfgQeKOCP4PedH65p0U%2BYxoy1EVLAV9q09KKIE0ll5mKaGPBapuwXNbkMJgsSY9ql92%2FK4Za3VyHGrQT5onEybsY0eNoiffy%2B44%2FxrjtaD4gMBU0MnCQGtNEQrBjX1HWR%2F0na8NAP9zDnnAZ4fG1P9pMx93yHBuDBIF0JerrhnpgKZN0hv8ZAvA79eZyifr3JQFU4LXxOQIyqQmcEsqsMJzNnskGOqUBYNZC50CLM7OlCO7Oakui0v1Y4B%2BlnrzyZc0opeC%2Ft6QC2uPtorjlLc1ZS8pyvLfG67fyiQWiYSa%2FmM1j7YVsuDE94rvhQY9mbY5mwrshlgURu7RT20Jfg8m3hIXdesLnWnUBlSl1RJTtBbwoHOAKBpBZEPh%2F0JyUDI%2BLMA9RKbbdAtMNM2UeQX6V%2BA3YcPhUFl9c8Lr2YB87N9yDdTuUuII%2FaNV5&X-Amz-Signature=618c9ff7c7da877dabfe8dde4432e9413df9a8b8dfafb32600bec6fcf9a87b16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



