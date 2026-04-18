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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MIAR63U%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIAVeoGGcV7JZ%2FSjH87ZS3pi%2BDKmftZjHxOxT%2Bsgeh4qeAiEA8IvxRB01lesmTY%2FxeNoxX19NgAHkoPuo2%2BNNnkIJNsUqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH4LryDpqY8WeUm76yrcA2MAeQHkWwBaqExeO%2Fh9VnPEBwvg1104ohMEW2l4ijZ7%2BwMJ97rRkeWNf%2FNrjkDn6Pr6yeKTUT%2FvYgDxnx%2FruMAa%2F9LPhKdeOrjfQh6c62AHxqR7wtAFS19pwiTgAmSC%2FaN8zyR2QY5NwJymH3DsT7k4znzhQi9e1xAg3qnoFjJBAfN1qxbJsKVgMPOa6EUySheWpmsUmW5C1%2FUmnOw2cj8UfogXaYgi9Wp6kBTuQMNZ9GILVjTCCg8MTQ2NbAYYAU1E0TpNrporcsjSBlx8ds3%2FBTiMe4smrQhkaU6oT0ej9M7Zmkic3KI%2BFjKieN6CdgYMAR5Hv4pF725s%2FQEWcEvH%2FbTcor9iKm18AHhSoNVsupSL2emk%2FvqDJz74Lt1YawTDUfKvPTIlbUxVTdqTQUgdrfPyo%2FcPh6NtzZXawLn3Yk5boYebWT6Ex9l8OeleUzXIJms%2Bir67fD%2B79OHHIYBSKVjcYDWEWQBMzsKA6cyp%2FtSa7cNgSFinnvchAyFAb6NgbiX8BV1v4pNt7atwUjP1im4ukze65SEjU1FTdFkQ1auE%2BKUoKHvukHwvclTdm8FuAvUTTmvSSoyoz%2F8UCzXfs176wEaB8AjQrbCBTFNO5%2FZBR%2BrJTrBRRtboMPisi88GOqUBTyQLXurtV2KyBWxenhfGIRONvRslojdovo8ZYcWXYpfIdrWXYTd7FNfZdHgQfJyUYuPPc4EIj%2BLsvkBDzl%2FiAB%2Bo2xQPFH28VQ%2BDOk3XAfzX7M2zLjlPpDOVVnZJ1JWHXv1gKJgee53Y93pJZWOIb6O1L08Pvt1EOdTDSus4EHgZj2oZn0XeG6YKVFNF169F9BkyVdwqDvzBY7nujQntsmrnTBA0&X-Amz-Signature=a53829ce5ca54a2f238ee4f796cb258fc16a8849d10ea8cca551f4701d036ad2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MIAR63U%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIAVeoGGcV7JZ%2FSjH87ZS3pi%2BDKmftZjHxOxT%2Bsgeh4qeAiEA8IvxRB01lesmTY%2FxeNoxX19NgAHkoPuo2%2BNNnkIJNsUqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH4LryDpqY8WeUm76yrcA2MAeQHkWwBaqExeO%2Fh9VnPEBwvg1104ohMEW2l4ijZ7%2BwMJ97rRkeWNf%2FNrjkDn6Pr6yeKTUT%2FvYgDxnx%2FruMAa%2F9LPhKdeOrjfQh6c62AHxqR7wtAFS19pwiTgAmSC%2FaN8zyR2QY5NwJymH3DsT7k4znzhQi9e1xAg3qnoFjJBAfN1qxbJsKVgMPOa6EUySheWpmsUmW5C1%2FUmnOw2cj8UfogXaYgi9Wp6kBTuQMNZ9GILVjTCCg8MTQ2NbAYYAU1E0TpNrporcsjSBlx8ds3%2FBTiMe4smrQhkaU6oT0ej9M7Zmkic3KI%2BFjKieN6CdgYMAR5Hv4pF725s%2FQEWcEvH%2FbTcor9iKm18AHhSoNVsupSL2emk%2FvqDJz74Lt1YawTDUfKvPTIlbUxVTdqTQUgdrfPyo%2FcPh6NtzZXawLn3Yk5boYebWT6Ex9l8OeleUzXIJms%2Bir67fD%2B79OHHIYBSKVjcYDWEWQBMzsKA6cyp%2FtSa7cNgSFinnvchAyFAb6NgbiX8BV1v4pNt7atwUjP1im4ukze65SEjU1FTdFkQ1auE%2BKUoKHvukHwvclTdm8FuAvUTTmvSSoyoz%2F8UCzXfs176wEaB8AjQrbCBTFNO5%2FZBR%2BrJTrBRRtboMPisi88GOqUBTyQLXurtV2KyBWxenhfGIRONvRslojdovo8ZYcWXYpfIdrWXYTd7FNfZdHgQfJyUYuPPc4EIj%2BLsvkBDzl%2FiAB%2Bo2xQPFH28VQ%2BDOk3XAfzX7M2zLjlPpDOVVnZJ1JWHXv1gKJgee53Y93pJZWOIb6O1L08Pvt1EOdTDSus4EHgZj2oZn0XeG6YKVFNF169F9BkyVdwqDvzBY7nujQntsmrnTBA0&X-Amz-Signature=bdf0a0e458d9f2af67a1061f40f300c8dd9b52595ab552aad7b2606bd78dc451&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MIAR63U%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIAVeoGGcV7JZ%2FSjH87ZS3pi%2BDKmftZjHxOxT%2Bsgeh4qeAiEA8IvxRB01lesmTY%2FxeNoxX19NgAHkoPuo2%2BNNnkIJNsUqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH4LryDpqY8WeUm76yrcA2MAeQHkWwBaqExeO%2Fh9VnPEBwvg1104ohMEW2l4ijZ7%2BwMJ97rRkeWNf%2FNrjkDn6Pr6yeKTUT%2FvYgDxnx%2FruMAa%2F9LPhKdeOrjfQh6c62AHxqR7wtAFS19pwiTgAmSC%2FaN8zyR2QY5NwJymH3DsT7k4znzhQi9e1xAg3qnoFjJBAfN1qxbJsKVgMPOa6EUySheWpmsUmW5C1%2FUmnOw2cj8UfogXaYgi9Wp6kBTuQMNZ9GILVjTCCg8MTQ2NbAYYAU1E0TpNrporcsjSBlx8ds3%2FBTiMe4smrQhkaU6oT0ej9M7Zmkic3KI%2BFjKieN6CdgYMAR5Hv4pF725s%2FQEWcEvH%2FbTcor9iKm18AHhSoNVsupSL2emk%2FvqDJz74Lt1YawTDUfKvPTIlbUxVTdqTQUgdrfPyo%2FcPh6NtzZXawLn3Yk5boYebWT6Ex9l8OeleUzXIJms%2Bir67fD%2B79OHHIYBSKVjcYDWEWQBMzsKA6cyp%2FtSa7cNgSFinnvchAyFAb6NgbiX8BV1v4pNt7atwUjP1im4ukze65SEjU1FTdFkQ1auE%2BKUoKHvukHwvclTdm8FuAvUTTmvSSoyoz%2F8UCzXfs176wEaB8AjQrbCBTFNO5%2FZBR%2BrJTrBRRtboMPisi88GOqUBTyQLXurtV2KyBWxenhfGIRONvRslojdovo8ZYcWXYpfIdrWXYTd7FNfZdHgQfJyUYuPPc4EIj%2BLsvkBDzl%2FiAB%2Bo2xQPFH28VQ%2BDOk3XAfzX7M2zLjlPpDOVVnZJ1JWHXv1gKJgee53Y93pJZWOIb6O1L08Pvt1EOdTDSus4EHgZj2oZn0XeG6YKVFNF169F9BkyVdwqDvzBY7nujQntsmrnTBA0&X-Amz-Signature=525e5571620100cec61dea2ffc92da0cf0b27ecb930eaabaa2f6269173ec8f8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

