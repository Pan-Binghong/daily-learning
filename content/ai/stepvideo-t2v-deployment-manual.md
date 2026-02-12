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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/bb2a4375-94d6-4e64-a40e-f65d22e44ef6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644IPMFBT%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQD7k%2BGH0otfKOTv2WNaW1jGoZD9RZ0sAs22aJMFAFEqpwIhALA%2BH9ixOkUtGVuEfm6JA5ILRgnaRkzbKY1LeBnbhtP9KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHegHHWgvn%2FQhMU08q3AOphjcFTAaIFzAjdyTdJXhb3k1q1sJSzQ0L5xM3Jcu0%2BNwrPrgOe%2FzROeGjMn652VxLVB5ddt7CWW7%2FEiqsvCJp7%2BtOfxa1E2EgfSAhbkRJEi%2B%2BZPUnik8yyU%2FS3Rmowhurq6ymEKqGQhieIH7YXpqgJ0PIEEE%2FaAGLsWAwFh8%2BEXt2VI8juNrILi8Kl7Vw2lBkVAsF3%2Fm1ZsA%2BP%2Fb4Mp00wdui%2FAFyRlpjMO3nUbd3qzYmf32GM7%2B2Btnsodhvq48oU%2FJ3VjPESPH56oNX%2BhfwuOAbt0m5PYns8YoJQx%2BrSDS6pKYxk1U9bUjtwAShIyh46fwfk4kzDoj97yAXu73uzZRNz8leHxSrvCUKZBpSXDHt%2BZDvo41g9nIrW8MyIIXY3TnUFvo9GCfICFIyN7RxWDHrB4K2P7hDUjuDs03d3WhtWk%2FG3BlZWrHLE7dwYIRy4Wm4o0RukxMRm3b2ClBamxOiPq%2BpSe9n9VznYzDOJsE%2BoRLf1L%2Bck55qm1jw0cqG9xqFOmp5pX9aMieJNpkjqEAnZKLeO6hhnleP40PbmwYk%2BX0gdos9%2B4moaMS91bYhq%2FBqUaGV85Jhi874z4TXeV7Z20ueXXObXnXoGyTWNgz2RBvKCE%2B0F45OuzC6krXMBjqkActl4OHuO4IMKgw3mbmFfbQHRcLe6vUbZeEI7BzamSVvKvm3wnY9vRba740TjPGsL6ZRxIPeHBggHq%2BnEB8fzmVMIMiBJofDJPLtpEHG3NLQ8XPISkmwDk3wPZRF6pQMFMHTH3GiNxOF8ivKW%2B5KPw%2F%2FM6WX0iKCIswC6J5PfRGVjh1EbvbSFJs0E4X0ex4%2BGcA63%2BfGY%2F%2BrtInS%2FCPumvIFnnpi&X-Amz-Signature=b48304bb92765bf0a386c541ef2cc01c1836ef32fde2072d6b67c9ec3de5ceb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/33952259-95f6-4b63-bef6-74c8feca00f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644IPMFBT%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQD7k%2BGH0otfKOTv2WNaW1jGoZD9RZ0sAs22aJMFAFEqpwIhALA%2BH9ixOkUtGVuEfm6JA5ILRgnaRkzbKY1LeBnbhtP9KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHegHHWgvn%2FQhMU08q3AOphjcFTAaIFzAjdyTdJXhb3k1q1sJSzQ0L5xM3Jcu0%2BNwrPrgOe%2FzROeGjMn652VxLVB5ddt7CWW7%2FEiqsvCJp7%2BtOfxa1E2EgfSAhbkRJEi%2B%2BZPUnik8yyU%2FS3Rmowhurq6ymEKqGQhieIH7YXpqgJ0PIEEE%2FaAGLsWAwFh8%2BEXt2VI8juNrILi8Kl7Vw2lBkVAsF3%2Fm1ZsA%2BP%2Fb4Mp00wdui%2FAFyRlpjMO3nUbd3qzYmf32GM7%2B2Btnsodhvq48oU%2FJ3VjPESPH56oNX%2BhfwuOAbt0m5PYns8YoJQx%2BrSDS6pKYxk1U9bUjtwAShIyh46fwfk4kzDoj97yAXu73uzZRNz8leHxSrvCUKZBpSXDHt%2BZDvo41g9nIrW8MyIIXY3TnUFvo9GCfICFIyN7RxWDHrB4K2P7hDUjuDs03d3WhtWk%2FG3BlZWrHLE7dwYIRy4Wm4o0RukxMRm3b2ClBamxOiPq%2BpSe9n9VznYzDOJsE%2BoRLf1L%2Bck55qm1jw0cqG9xqFOmp5pX9aMieJNpkjqEAnZKLeO6hhnleP40PbmwYk%2BX0gdos9%2B4moaMS91bYhq%2FBqUaGV85Jhi874z4TXeV7Z20ueXXObXnXoGyTWNgz2RBvKCE%2B0F45OuzC6krXMBjqkActl4OHuO4IMKgw3mbmFfbQHRcLe6vUbZeEI7BzamSVvKvm3wnY9vRba740TjPGsL6ZRxIPeHBggHq%2BnEB8fzmVMIMiBJofDJPLtpEHG3NLQ8XPISkmwDk3wPZRF6pQMFMHTH3GiNxOF8ivKW%2B5KPw%2F%2FM6WX0iKCIswC6J5PfRGVjh1EbvbSFJs0E4X0ex4%2BGcA63%2BfGY%2F%2BrtInS%2FCPumvIFnnpi&X-Amz-Signature=c109f4af7de364cc0a6248c0bda3b4b83d80df40d91f50d57cf21d6732001253&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9608cccd-fd50-4c31-8379-b4d46a60b867/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644IPMFBT%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQD7k%2BGH0otfKOTv2WNaW1jGoZD9RZ0sAs22aJMFAFEqpwIhALA%2BH9ixOkUtGVuEfm6JA5ILRgnaRkzbKY1LeBnbhtP9KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHegHHWgvn%2FQhMU08q3AOphjcFTAaIFzAjdyTdJXhb3k1q1sJSzQ0L5xM3Jcu0%2BNwrPrgOe%2FzROeGjMn652VxLVB5ddt7CWW7%2FEiqsvCJp7%2BtOfxa1E2EgfSAhbkRJEi%2B%2BZPUnik8yyU%2FS3Rmowhurq6ymEKqGQhieIH7YXpqgJ0PIEEE%2FaAGLsWAwFh8%2BEXt2VI8juNrILi8Kl7Vw2lBkVAsF3%2Fm1ZsA%2BP%2Fb4Mp00wdui%2FAFyRlpjMO3nUbd3qzYmf32GM7%2B2Btnsodhvq48oU%2FJ3VjPESPH56oNX%2BhfwuOAbt0m5PYns8YoJQx%2BrSDS6pKYxk1U9bUjtwAShIyh46fwfk4kzDoj97yAXu73uzZRNz8leHxSrvCUKZBpSXDHt%2BZDvo41g9nIrW8MyIIXY3TnUFvo9GCfICFIyN7RxWDHrB4K2P7hDUjuDs03d3WhtWk%2FG3BlZWrHLE7dwYIRy4Wm4o0RukxMRm3b2ClBamxOiPq%2BpSe9n9VznYzDOJsE%2BoRLf1L%2Bck55qm1jw0cqG9xqFOmp5pX9aMieJNpkjqEAnZKLeO6hhnleP40PbmwYk%2BX0gdos9%2B4moaMS91bYhq%2FBqUaGV85Jhi874z4TXeV7Z20ueXXObXnXoGyTWNgz2RBvKCE%2B0F45OuzC6krXMBjqkActl4OHuO4IMKgw3mbmFfbQHRcLe6vUbZeEI7BzamSVvKvm3wnY9vRba740TjPGsL6ZRxIPeHBggHq%2BnEB8fzmVMIMiBJofDJPLtpEHG3NLQ8XPISkmwDk3wPZRF6pQMFMHTH3GiNxOF8ivKW%2B5KPw%2F%2FM6WX0iKCIswC6J5PfRGVjh1EbvbSFJs0E4X0ex4%2BGcA63%2BfGY%2F%2BrtInS%2FCPumvIFnnpi&X-Amz-Signature=79aa2d65a7b5b8b374a61aaba4273013c3adbfc12b8424be0b7d29063ded5fde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 使用步骤

---

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a95ab578-a74b-4758-9842-4f0f51ab65db/PixPin_2025-04-22_11-07-29.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644IPMFBT%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQD7k%2BGH0otfKOTv2WNaW1jGoZD9RZ0sAs22aJMFAFEqpwIhALA%2BH9ixOkUtGVuEfm6JA5ILRgnaRkzbKY1LeBnbhtP9KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzHegHHWgvn%2FQhMU08q3AOphjcFTAaIFzAjdyTdJXhb3k1q1sJSzQ0L5xM3Jcu0%2BNwrPrgOe%2FzROeGjMn652VxLVB5ddt7CWW7%2FEiqsvCJp7%2BtOfxa1E2EgfSAhbkRJEi%2B%2BZPUnik8yyU%2FS3Rmowhurq6ymEKqGQhieIH7YXpqgJ0PIEEE%2FaAGLsWAwFh8%2BEXt2VI8juNrILi8Kl7Vw2lBkVAsF3%2Fm1ZsA%2BP%2Fb4Mp00wdui%2FAFyRlpjMO3nUbd3qzYmf32GM7%2B2Btnsodhvq48oU%2FJ3VjPESPH56oNX%2BhfwuOAbt0m5PYns8YoJQx%2BrSDS6pKYxk1U9bUjtwAShIyh46fwfk4kzDoj97yAXu73uzZRNz8leHxSrvCUKZBpSXDHt%2BZDvo41g9nIrW8MyIIXY3TnUFvo9GCfICFIyN7RxWDHrB4K2P7hDUjuDs03d3WhtWk%2FG3BlZWrHLE7dwYIRy4Wm4o0RukxMRm3b2ClBamxOiPq%2BpSe9n9VznYzDOJsE%2BoRLf1L%2Bck55qm1jw0cqG9xqFOmp5pX9aMieJNpkjqEAnZKLeO6hhnleP40PbmwYk%2BX0gdos9%2B4moaMS91bYhq%2FBqUaGV85Jhi874z4TXeV7Z20ueXXObXnXoGyTWNgz2RBvKCE%2B0F45OuzC6krXMBjqkActl4OHuO4IMKgw3mbmFfbQHRcLe6vUbZeEI7BzamSVvKvm3wnY9vRba740TjPGsL6ZRxIPeHBggHq%2BnEB8fzmVMIMiBJofDJPLtpEHG3NLQ8XPISkmwDk3wPZRF6pQMFMHTH3GiNxOF8ivKW%2B5KPw%2F%2FM6WX0iKCIswC6J5PfRGVjh1EbvbSFJs0E4X0ex4%2BGcA63%2BfGY%2F%2BrtInS%2FCPumvIFnnpi&X-Amz-Signature=5962abf68a4111c3fb15b18c601444d417686babdf07caf9f569df70bbd8a034&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

> References



