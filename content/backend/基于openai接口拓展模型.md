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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y76JJHKR%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICrGKMmsgpp4KAi2GSSiQYYl9fp0Awx4ni%2Fk3ySnwHbrAiEA8D6tBegrQhvCKAuFr0Ioh9OFb0ys8hW1NbNMd4FBYAsqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBgGy5M4pj4ILTROzSrcA2SIJug70oUJuUBTMM0%2Bvb58RxOBJetfLIVOAk8%2BzfTSKgsDIp2O89cORSwzE74FuAm6q9WU2xa0%2Fd%2BACWeHVIfoZ0regZL7%2FhS3%2Fz195ShKSSeFBP3EyHtdFRzzIlcaG%2FiPH%2F2NnP1IerkjqsCkAV1tSh8qGhMpkAdNWh%2BGinvOR3SGs1NTKkJrOTJB7jMHOqO4WOA94JAqTcuHj7krCvg%2BV%2B313OWFNqwSnsq25ejymhTR4tckW80TDeWRCYthrnKlklAoUSbv6AKZX5Ji%2FpBKGpA136WGKE2%2FXFDUKaR51vDr7dMMhv04SGWnmbYQSMmhamOemjo737IMRaiftREhPp1F6N%2B7Yiia%2FZWzOUitZ1TgxEarZEklUDD5XPPW1VvvtR1nz%2FmgSqxarb9esDqT3WK8%2FRqHOj6R%2Bmz5lfZV3FF6n%2FCNCQiu8%2BWbypv96iKHHKVew%2F1viK9rcdrRHRQi%2BRpV7ueE2wLdzsaDGO3EU4omXFD6BJUtTwtbgJSCtvQ2xmGERHE8BNwQ3q9yxEBcSg%2BhcJ6BcjKbOg9LZ4ZBF6fWW6dvvgsvTg0cOOKa72vTXF3xdsMirHl3sqXILlDAyq01hM%2FM37I3L1r5xurqT0KwM6ahJTh73RBkMO%2FEgcsGOqUBquaDmqg9ZJXi0mlyYyvqcvdKBuh%2Fq9aGPhx5g9MM3%2FoEYyzfJRWLBjfWNff8OK9Titb1V8s0efELSUdapp8Jl6A9e94eWyFNjIQ%2BOzCxEYkksYNYdp2HLiS3z8IpsN3qt%2FDVKUcX3UGQWQYaJYuAjbgJHkQy8j%2BJUj91HGOkS5VVlX%2B%2BKjYCk8TRzvvtFu3%2B2hX1YDi8OxqLLfUhnnHYt%2BYimLgg&X-Amz-Signature=1d81ccb642d7ce983f8e542423fd766e2aed861ce264d50168d156f0387fc5fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y76JJHKR%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICrGKMmsgpp4KAi2GSSiQYYl9fp0Awx4ni%2Fk3ySnwHbrAiEA8D6tBegrQhvCKAuFr0Ioh9OFb0ys8hW1NbNMd4FBYAsqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBgGy5M4pj4ILTROzSrcA2SIJug70oUJuUBTMM0%2Bvb58RxOBJetfLIVOAk8%2BzfTSKgsDIp2O89cORSwzE74FuAm6q9WU2xa0%2Fd%2BACWeHVIfoZ0regZL7%2FhS3%2Fz195ShKSSeFBP3EyHtdFRzzIlcaG%2FiPH%2F2NnP1IerkjqsCkAV1tSh8qGhMpkAdNWh%2BGinvOR3SGs1NTKkJrOTJB7jMHOqO4WOA94JAqTcuHj7krCvg%2BV%2B313OWFNqwSnsq25ejymhTR4tckW80TDeWRCYthrnKlklAoUSbv6AKZX5Ji%2FpBKGpA136WGKE2%2FXFDUKaR51vDr7dMMhv04SGWnmbYQSMmhamOemjo737IMRaiftREhPp1F6N%2B7Yiia%2FZWzOUitZ1TgxEarZEklUDD5XPPW1VvvtR1nz%2FmgSqxarb9esDqT3WK8%2FRqHOj6R%2Bmz5lfZV3FF6n%2FCNCQiu8%2BWbypv96iKHHKVew%2F1viK9rcdrRHRQi%2BRpV7ueE2wLdzsaDGO3EU4omXFD6BJUtTwtbgJSCtvQ2xmGERHE8BNwQ3q9yxEBcSg%2BhcJ6BcjKbOg9LZ4ZBF6fWW6dvvgsvTg0cOOKa72vTXF3xdsMirHl3sqXILlDAyq01hM%2FM37I3L1r5xurqT0KwM6ahJTh73RBkMO%2FEgcsGOqUBquaDmqg9ZJXi0mlyYyvqcvdKBuh%2Fq9aGPhx5g9MM3%2FoEYyzfJRWLBjfWNff8OK9Titb1V8s0efELSUdapp8Jl6A9e94eWyFNjIQ%2BOzCxEYkksYNYdp2HLiS3z8IpsN3qt%2FDVKUcX3UGQWQYaJYuAjbgJHkQy8j%2BJUj91HGOkS5VVlX%2B%2BKjYCk8TRzvvtFu3%2B2hX1YDi8OxqLLfUhnnHYt%2BYimLgg&X-Amz-Signature=105d65859dd3d2e0fbd3ff3202c803efc7fdc9543b292739abfd547e58a51b96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y76JJHKR%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICrGKMmsgpp4KAi2GSSiQYYl9fp0Awx4ni%2Fk3ySnwHbrAiEA8D6tBegrQhvCKAuFr0Ioh9OFb0ys8hW1NbNMd4FBYAsqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBgGy5M4pj4ILTROzSrcA2SIJug70oUJuUBTMM0%2Bvb58RxOBJetfLIVOAk8%2BzfTSKgsDIp2O89cORSwzE74FuAm6q9WU2xa0%2Fd%2BACWeHVIfoZ0regZL7%2FhS3%2Fz195ShKSSeFBP3EyHtdFRzzIlcaG%2FiPH%2F2NnP1IerkjqsCkAV1tSh8qGhMpkAdNWh%2BGinvOR3SGs1NTKkJrOTJB7jMHOqO4WOA94JAqTcuHj7krCvg%2BV%2B313OWFNqwSnsq25ejymhTR4tckW80TDeWRCYthrnKlklAoUSbv6AKZX5Ji%2FpBKGpA136WGKE2%2FXFDUKaR51vDr7dMMhv04SGWnmbYQSMmhamOemjo737IMRaiftREhPp1F6N%2B7Yiia%2FZWzOUitZ1TgxEarZEklUDD5XPPW1VvvtR1nz%2FmgSqxarb9esDqT3WK8%2FRqHOj6R%2Bmz5lfZV3FF6n%2FCNCQiu8%2BWbypv96iKHHKVew%2F1viK9rcdrRHRQi%2BRpV7ueE2wLdzsaDGO3EU4omXFD6BJUtTwtbgJSCtvQ2xmGERHE8BNwQ3q9yxEBcSg%2BhcJ6BcjKbOg9LZ4ZBF6fWW6dvvgsvTg0cOOKa72vTXF3xdsMirHl3sqXILlDAyq01hM%2FM37I3L1r5xurqT0KwM6ahJTh73RBkMO%2FEgcsGOqUBquaDmqg9ZJXi0mlyYyvqcvdKBuh%2Fq9aGPhx5g9MM3%2FoEYyzfJRWLBjfWNff8OK9Titb1V8s0efELSUdapp8Jl6A9e94eWyFNjIQ%2BOzCxEYkksYNYdp2HLiS3z8IpsN3qt%2FDVKUcX3UGQWQYaJYuAjbgJHkQy8j%2BJUj91HGOkS5VVlX%2B%2BKjYCk8TRzvvtFu3%2B2hX1YDi8OxqLLfUhnnHYt%2BYimLgg&X-Amz-Signature=2a9280002af628b83fe9af962ed511f41d58daf7e770224bee873b9c62324a63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

