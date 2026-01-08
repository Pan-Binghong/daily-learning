---
title: 基于Openai接口拓展模型
date: '2024-11-18T07:55:00.000Z'
lastmod: '2024-11-20T03:24:00.000Z'
draft: false
tags:
- Python
- API
categories:
- 后端
---

> 💡 记录一下，基于Openai API进行接口移植的过程，从引用api、测试、最后转接口部署。

---

### GPT-4o接口

```python
client = OpenAI(
    api_key=#这里就放入刚刚购买到的key就可以啦)
from opneai import OpenAI
def gpt_generate_text(prompt, messages_list):
    messages = ''    if messages_list:
        messages = '以下是你和用户的当前会话消息：\n\n' + '\n'.join(messages_list)
    stream = client.chat.completions.create(
        # model="gpt-4-turbo-preview",        model="gpt-4o",
        messages=[
            {"role": "system", "content": messages},
            {"role": "user", "content": prompt},
        ],
        stream=True    )
    text = ''    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            text += chunk.choices[0].delta.content
    return text
```

- 路由函数
---

## Whisper-1接口

- whisper-1模型(进行音频转文本)
```python
def transcribe_audio(audio_file):
    audio=open(audio_file, "rb")
    transcription = client.audio.transcriptions.create(model="whisper-1",file=audio)
    text = transcription.text
    return text
```

- 路由函数
```python
@app.route("/transcribe", methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400    audio_file = request.files['file']
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400    if audio_file:
        # 保存文件到临时位置        temp_file_path = os.path.join("temp", audio_file.filename)
        audio_file.save(temp_file_path)
        # 调用转录函数        transcription_text = transcribe_audio(temp_file_path)
        # 删除临时文件        os.remove(temp_file_path)
        return jsonify({"text": transcription_text})
```

> 首先我们要确定返回的请求中是否包含文件和文件名，如果没有，则返回错误信息和400，其次，我们需要保存文件到临时位置，然后调用我们写好的转录函数进行转录，最后删除临时文件。最后返回转录后的文本给客户端 供使用。

---

## TTS-1接口

- TTS-1(文本转换为语音)
```python
def text_to_speech(text, vocie, model, path):

    response = client.audio.speech.create(
        model=model,
        voice=vocie,
        input=text
    )
    speech_file_path = Path(path)
    with open(speech_file_path, 'wb') as file:
        file.write(response.content)

    print(f'文件已保存到: {speech_file_path}')
    return speech_file_path
```

- 路由函数
```python
app = Flask(__name__)
server_ip = ""  # 替换为你的服务器IP@app.route('/text-to-speech', methods=['POST'])
def text_to_speech_endpoint():
    data = request.json
    text = data.get('text')
    voice = data.get('voice')
    model = data.get('model')
    output_path = './output.mp3'    if not text or not voice or not model:
        return {'error': 'Missing required parameters'}, 400    try:
        # Define the directory where you want to save the files        output_dir = Path('./audio_files')
        output_dir.mkdir(exist_ok=True)
        # Generate a unique filename using UUID        unique_filename = f"{uuid.uuid4()}.mp3"        output_path = output_dir / unique_filename
        # Generate the speech and save the file        speech_file_path = text_to_speech(text, voice, model, output_path)
        # Create the file URL        file_url = f"http://{server_ip}/root/xxx/{speech_file_path}"        # Return the file URL as a response        return jsonify({'file_url': file_url}), 200    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

> 首先我们要在后端代码中写入 我们的服务器ip地址我们要确保我们的json数据存在 四个键 text ， voice ， model ， output_path ，其次我们调用text_to_speech函数，传入text，voice，model，output_path，然后我们生成一个唯一的filename，保存到output_dir目录下最后我们生成一个file_url，然后返回给客户端。

---

## 测试截图

### gpt4o

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO6MFEEO%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENeTRzqAviE6eo%2BZl7NG7RjwMCuoRKIFe9ZjVRXQAy6AiBjphoYuyFJnekKMmxLW8VvCrsmje%2Bbgf7taNtl8gg7RSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4yA0cwmb4adXUrJhKtwD8%2FWS315tT9BgJACzGMwlexa820NLdaOLz4Uapvj0VS56%2B0lzCaCC0BUbewJND5wQz%2BVKH6LYfbKtiPPnNBQIp5Byjm6vUBMeTkveqQM%2B%2Baw2A96fhFsCdxseJaWWGI%2FpUWd2EAw4JpTfw3cnoY%2Fh5PS5bdWoDxbLbkLVrGc4rX0w1hSWShGElFnfrfxH8d9OjZdGLO%2Bn2D3k2%2FhQA5BfNe5bdWwpbBcqBh%2FA%2FIgPPzpd2MA3LKHLj3V1Ts9E9tG5bYhZpIkSf5h0VR1aaXbMExascL4GG5lkqzrDjHqNEtnxsC0V8Il4POqIPD3r4Kb3%2FhoGCa9CeyQxXAGtiC9f2IZf1xGXS5GLZ8XBwBXsdtg04TOe7RuEw6OdORFsRdz96rATtA2djs5T3t%2FP7f785vQVUxJQXzdYfKYRp%2FCo%2F4mZsg2VALw2QDCDrD9K%2BxetYXTGH5cY0vXdshd8aICFAhpRAUnMb4xuagUxhUaHM27Mos%2BM78mMaxtvPUqizD2tAYXX39%2BSUyPM8994O0DpRX5J1BC7MKkag9UzyIBRA%2FhiCvduIxj758G4viGFCfILEs8RD3k%2Fygu4%2Bv3%2BrKAxMh9R%2FEsbuIsC10uaEaGV1MTDvnsLbFVxVrS3YUIwiqn8ygY6pgFFiVJaY%2FOXvVkn34HGFsE5HbHGXi%2B%2F%2FYHE585wZBAHM5w%2B8P0jDILVFCXfmPZGh1%2BRRVOJPLAK0Xo5mzRqIW30X0VfX4FUMdc7RMMxUjVL%2FP20RUCpem2%2FNFVgCe0yg%2Fov6lvmmgVa3%2BhvI1SVq8xPIYktqFvS7ISK2FcDxxFQMvrdjZsQ7KaAb4MGidNidi8lVBLNceLwsjZ609flpSU9QZIy3DCB&X-Amz-Signature=d8c8b18a7503035e88c91828b8cacbe83567931c03ef8759c6c69f7ca08acfdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO6MFEEO%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENeTRzqAviE6eo%2BZl7NG7RjwMCuoRKIFe9ZjVRXQAy6AiBjphoYuyFJnekKMmxLW8VvCrsmje%2Bbgf7taNtl8gg7RSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4yA0cwmb4adXUrJhKtwD8%2FWS315tT9BgJACzGMwlexa820NLdaOLz4Uapvj0VS56%2B0lzCaCC0BUbewJND5wQz%2BVKH6LYfbKtiPPnNBQIp5Byjm6vUBMeTkveqQM%2B%2Baw2A96fhFsCdxseJaWWGI%2FpUWd2EAw4JpTfw3cnoY%2Fh5PS5bdWoDxbLbkLVrGc4rX0w1hSWShGElFnfrfxH8d9OjZdGLO%2Bn2D3k2%2FhQA5BfNe5bdWwpbBcqBh%2FA%2FIgPPzpd2MA3LKHLj3V1Ts9E9tG5bYhZpIkSf5h0VR1aaXbMExascL4GG5lkqzrDjHqNEtnxsC0V8Il4POqIPD3r4Kb3%2FhoGCa9CeyQxXAGtiC9f2IZf1xGXS5GLZ8XBwBXsdtg04TOe7RuEw6OdORFsRdz96rATtA2djs5T3t%2FP7f785vQVUxJQXzdYfKYRp%2FCo%2F4mZsg2VALw2QDCDrD9K%2BxetYXTGH5cY0vXdshd8aICFAhpRAUnMb4xuagUxhUaHM27Mos%2BM78mMaxtvPUqizD2tAYXX39%2BSUyPM8994O0DpRX5J1BC7MKkag9UzyIBRA%2FhiCvduIxj758G4viGFCfILEs8RD3k%2Fygu4%2Bv3%2BrKAxMh9R%2FEsbuIsC10uaEaGV1MTDvnsLbFVxVrS3YUIwiqn8ygY6pgFFiVJaY%2FOXvVkn34HGFsE5HbHGXi%2B%2F%2FYHE585wZBAHM5w%2B8P0jDILVFCXfmPZGh1%2BRRVOJPLAK0Xo5mzRqIW30X0VfX4FUMdc7RMMxUjVL%2FP20RUCpem2%2FNFVgCe0yg%2Fov6lvmmgVa3%2BhvI1SVq8xPIYktqFvS7ISK2FcDxxFQMvrdjZsQ7KaAb4MGidNidi8lVBLNceLwsjZ609flpSU9QZIy3DCB&X-Amz-Signature=d2c2e07b263fb4ad3c01d6741d2dae4f1f11d9ebe259c7686389f7792dd33615&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO6MFEEO%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENeTRzqAviE6eo%2BZl7NG7RjwMCuoRKIFe9ZjVRXQAy6AiBjphoYuyFJnekKMmxLW8VvCrsmje%2Bbgf7taNtl8gg7RSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4yA0cwmb4adXUrJhKtwD8%2FWS315tT9BgJACzGMwlexa820NLdaOLz4Uapvj0VS56%2B0lzCaCC0BUbewJND5wQz%2BVKH6LYfbKtiPPnNBQIp5Byjm6vUBMeTkveqQM%2B%2Baw2A96fhFsCdxseJaWWGI%2FpUWd2EAw4JpTfw3cnoY%2Fh5PS5bdWoDxbLbkLVrGc4rX0w1hSWShGElFnfrfxH8d9OjZdGLO%2Bn2D3k2%2FhQA5BfNe5bdWwpbBcqBh%2FA%2FIgPPzpd2MA3LKHLj3V1Ts9E9tG5bYhZpIkSf5h0VR1aaXbMExascL4GG5lkqzrDjHqNEtnxsC0V8Il4POqIPD3r4Kb3%2FhoGCa9CeyQxXAGtiC9f2IZf1xGXS5GLZ8XBwBXsdtg04TOe7RuEw6OdORFsRdz96rATtA2djs5T3t%2FP7f785vQVUxJQXzdYfKYRp%2FCo%2F4mZsg2VALw2QDCDrD9K%2BxetYXTGH5cY0vXdshd8aICFAhpRAUnMb4xuagUxhUaHM27Mos%2BM78mMaxtvPUqizD2tAYXX39%2BSUyPM8994O0DpRX5J1BC7MKkag9UzyIBRA%2FhiCvduIxj758G4viGFCfILEs8RD3k%2Fygu4%2Bv3%2BrKAxMh9R%2FEsbuIsC10uaEaGV1MTDvnsLbFVxVrS3YUIwiqn8ygY6pgFFiVJaY%2FOXvVkn34HGFsE5HbHGXi%2B%2F%2FYHE585wZBAHM5w%2B8P0jDILVFCXfmPZGh1%2BRRVOJPLAK0Xo5mzRqIW30X0VfX4FUMdc7RMMxUjVL%2FP20RUCpem2%2FNFVgCe0yg%2Fov6lvmmgVa3%2BhvI1SVq8xPIYktqFvS7ISK2FcDxxFQMvrdjZsQ7KaAb4MGidNidi8lVBLNceLwsjZ609flpSU9QZIy3DCB&X-Amz-Signature=3fa169f2c803f96171877f16fd2e8c517233075c570605f1f26ca5ea367737e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

