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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677FKHJL7%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeWofVSz0m%2BYmZzJsPC%2FR%2B9k%2FYJ83UCl5q2k37hkgJvAiALwZrEX4ZGnFnfkA%2Fn83zrFH0BP0gUnKi8A22M6Sk1biqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzdBZOsO77WEGU5OyKtwDpWCpNA08KDjTsKzJ74nzC2Xif6vzeA6tbU%2BCpYBk2woYd8rsjJ%2BEErF6whcpiva76%2Bg%2FP5ovIeIWaC44sORP2wnrSAsj9qutBW7XkmCfJtBEuexZFCDKuEeSzym7sgu1VdmpvWXs6IttM0Y82u9tnW50XzhsOPxYMlhULTZDwPWinHmF9e49xbZFQITDhuYdnlc0wx1R4gSBwODv1ima87kR2NIc1DXZHbA8Ghj9HcyecwdrBoEWjBSWZvUt7YGSCc8fToD1eumWmuaU0DLbeLZkxRIvqu6lqNEAGzkPqCqt8QO170Bztr%2Fm90BNHE%2FgDrFEkCBXH5eMDJkINs66A8G%2BXyels%2BS5O%2F0HjB1bMLQmukf3jpFADqsJmLSBfo9eEuJdNz0sLAybZGq4DWZCTmY%2BlUMDza7gDJTzGMcuZuZiRNnf2lwicyCmswo5ep%2BNWiRGh90%2FJn6RmZmM5xLoBDmjoVta1CGQSXe73%2B%2FUMJDzaYZDVmcmF92IbQ0bd641cfYRuqqpO9a9kS0Bp1qhvAuX95zRbaalCw9bSMqjPRIl3LLnzHhaky5siDpzTwZTlkzbRshVNTN4AaaRbeHwjs43LdWlN2P%2Br50bGX4syf24pMnCsaIbnOGScxUwr5HfzAY6pgFHbsEGgUr%2Fcx%2Fe%2FM206w3ttNw8c8zNPiZCclYYn00L4HZ5cOx90lM3aQDlhn%2BrEjOfyuVQVcBgAGImgfFDYP37UuUYdRtEzzESTfxGL8IUxDp14w%2ByUxzVdNEZseusnJJYVKpM%2FtineQpLzsKHtLTaC10oRgzIlcwT6%2FSuxTqDtws2rwghZh5CsBi6qv4VEwZyBOM7wKyZnB4hXJ2yBH92e4m8B0Di&X-Amz-Signature=9bdfbdc8873cdbd794ad48f730e1078b7968d851038bc55feb3564fb3aa59f64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677FKHJL7%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeWofVSz0m%2BYmZzJsPC%2FR%2B9k%2FYJ83UCl5q2k37hkgJvAiALwZrEX4ZGnFnfkA%2Fn83zrFH0BP0gUnKi8A22M6Sk1biqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzdBZOsO77WEGU5OyKtwDpWCpNA08KDjTsKzJ74nzC2Xif6vzeA6tbU%2BCpYBk2woYd8rsjJ%2BEErF6whcpiva76%2Bg%2FP5ovIeIWaC44sORP2wnrSAsj9qutBW7XkmCfJtBEuexZFCDKuEeSzym7sgu1VdmpvWXs6IttM0Y82u9tnW50XzhsOPxYMlhULTZDwPWinHmF9e49xbZFQITDhuYdnlc0wx1R4gSBwODv1ima87kR2NIc1DXZHbA8Ghj9HcyecwdrBoEWjBSWZvUt7YGSCc8fToD1eumWmuaU0DLbeLZkxRIvqu6lqNEAGzkPqCqt8QO170Bztr%2Fm90BNHE%2FgDrFEkCBXH5eMDJkINs66A8G%2BXyels%2BS5O%2F0HjB1bMLQmukf3jpFADqsJmLSBfo9eEuJdNz0sLAybZGq4DWZCTmY%2BlUMDza7gDJTzGMcuZuZiRNnf2lwicyCmswo5ep%2BNWiRGh90%2FJn6RmZmM5xLoBDmjoVta1CGQSXe73%2B%2FUMJDzaYZDVmcmF92IbQ0bd641cfYRuqqpO9a9kS0Bp1qhvAuX95zRbaalCw9bSMqjPRIl3LLnzHhaky5siDpzTwZTlkzbRshVNTN4AaaRbeHwjs43LdWlN2P%2Br50bGX4syf24pMnCsaIbnOGScxUwr5HfzAY6pgFHbsEGgUr%2Fcx%2Fe%2FM206w3ttNw8c8zNPiZCclYYn00L4HZ5cOx90lM3aQDlhn%2BrEjOfyuVQVcBgAGImgfFDYP37UuUYdRtEzzESTfxGL8IUxDp14w%2ByUxzVdNEZseusnJJYVKpM%2FtineQpLzsKHtLTaC10oRgzIlcwT6%2FSuxTqDtws2rwghZh5CsBi6qv4VEwZyBOM7wKyZnB4hXJ2yBH92e4m8B0Di&X-Amz-Signature=a2e1a60c452ba49b7fad71ae9fb7607fd6deb4d17edba5b963956b62a5b50bd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677FKHJL7%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeWofVSz0m%2BYmZzJsPC%2FR%2B9k%2FYJ83UCl5q2k37hkgJvAiALwZrEX4ZGnFnfkA%2Fn83zrFH0BP0gUnKi8A22M6Sk1biqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzdBZOsO77WEGU5OyKtwDpWCpNA08KDjTsKzJ74nzC2Xif6vzeA6tbU%2BCpYBk2woYd8rsjJ%2BEErF6whcpiva76%2Bg%2FP5ovIeIWaC44sORP2wnrSAsj9qutBW7XkmCfJtBEuexZFCDKuEeSzym7sgu1VdmpvWXs6IttM0Y82u9tnW50XzhsOPxYMlhULTZDwPWinHmF9e49xbZFQITDhuYdnlc0wx1R4gSBwODv1ima87kR2NIc1DXZHbA8Ghj9HcyecwdrBoEWjBSWZvUt7YGSCc8fToD1eumWmuaU0DLbeLZkxRIvqu6lqNEAGzkPqCqt8QO170Bztr%2Fm90BNHE%2FgDrFEkCBXH5eMDJkINs66A8G%2BXyels%2BS5O%2F0HjB1bMLQmukf3jpFADqsJmLSBfo9eEuJdNz0sLAybZGq4DWZCTmY%2BlUMDza7gDJTzGMcuZuZiRNnf2lwicyCmswo5ep%2BNWiRGh90%2FJn6RmZmM5xLoBDmjoVta1CGQSXe73%2B%2FUMJDzaYZDVmcmF92IbQ0bd641cfYRuqqpO9a9kS0Bp1qhvAuX95zRbaalCw9bSMqjPRIl3LLnzHhaky5siDpzTwZTlkzbRshVNTN4AaaRbeHwjs43LdWlN2P%2Br50bGX4syf24pMnCsaIbnOGScxUwr5HfzAY6pgFHbsEGgUr%2Fcx%2Fe%2FM206w3ttNw8c8zNPiZCclYYn00L4HZ5cOx90lM3aQDlhn%2BrEjOfyuVQVcBgAGImgfFDYP37UuUYdRtEzzESTfxGL8IUxDp14w%2ByUxzVdNEZseusnJJYVKpM%2FtineQpLzsKHtLTaC10oRgzIlcwT6%2FSuxTqDtws2rwghZh5CsBi6qv4VEwZyBOM7wKyZnB4hXJ2yBH92e4m8B0Di&X-Amz-Signature=00e4f408ad5968643cde50459e5673e48da5d7bcabd185bb343a9b2b7941cc21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677FKHJL7%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeWofVSz0m%2BYmZzJsPC%2FR%2B9k%2FYJ83UCl5q2k37hkgJvAiALwZrEX4ZGnFnfkA%2Fn83zrFH0BP0gUnKi8A22M6Sk1biqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzdBZOsO77WEGU5OyKtwDpWCpNA08KDjTsKzJ74nzC2Xif6vzeA6tbU%2BCpYBk2woYd8rsjJ%2BEErF6whcpiva76%2Bg%2FP5ovIeIWaC44sORP2wnrSAsj9qutBW7XkmCfJtBEuexZFCDKuEeSzym7sgu1VdmpvWXs6IttM0Y82u9tnW50XzhsOPxYMlhULTZDwPWinHmF9e49xbZFQITDhuYdnlc0wx1R4gSBwODv1ima87kR2NIc1DXZHbA8Ghj9HcyecwdrBoEWjBSWZvUt7YGSCc8fToD1eumWmuaU0DLbeLZkxRIvqu6lqNEAGzkPqCqt8QO170Bztr%2Fm90BNHE%2FgDrFEkCBXH5eMDJkINs66A8G%2BXyels%2BS5O%2F0HjB1bMLQmukf3jpFADqsJmLSBfo9eEuJdNz0sLAybZGq4DWZCTmY%2BlUMDza7gDJTzGMcuZuZiRNnf2lwicyCmswo5ep%2BNWiRGh90%2FJn6RmZmM5xLoBDmjoVta1CGQSXe73%2B%2FUMJDzaYZDVmcmF92IbQ0bd641cfYRuqqpO9a9kS0Bp1qhvAuX95zRbaalCw9bSMqjPRIl3LLnzHhaky5siDpzTwZTlkzbRshVNTN4AaaRbeHwjs43LdWlN2P%2Br50bGX4syf24pMnCsaIbnOGScxUwr5HfzAY6pgFHbsEGgUr%2Fcx%2Fe%2FM206w3ttNw8c8zNPiZCclYYn00L4HZ5cOx90lM3aQDlhn%2BrEjOfyuVQVcBgAGImgfFDYP37UuUYdRtEzzESTfxGL8IUxDp14w%2ByUxzVdNEZseusnJJYVKpM%2FtineQpLzsKHtLTaC10oRgzIlcwT6%2FSuxTqDtws2rwghZh5CsBi6qv4VEwZyBOM7wKyZnB4hXJ2yBH92e4m8B0Di&X-Amz-Signature=dc0adb353e37bf678dede292e14c745ceaff72d20e9ccef93f7caf9a1d3032a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



