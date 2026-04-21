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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNSX7IMC%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIHS1jMWsfKXTOSoWdnZ1zbFhjYr7rpOTzewwkDtYzY%2BLAiBOOsKSGN1i9DdOA3Qiw4Y%2Fr22qdeoAlppL3loolQB43Sr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMOZHOX7esCrTy2gvxKtwD1MQVESWNwQ1vpI79Omx9O8z%2FCuMAiA5RBZpnd1OkkKNCg1cld4zgJbMS7sdoh1lCBhrLxUF5yAvI7RAXkkpd0MNQfbUUi9ZK6nAjrXIcNyMPYMahCGsHiI2un7c0mDLiX4LOnRLowaG55Vk%2F3WW%2B9g94c8KEoQHwmOXr2c5y0vSD4%2F01Z%2B%2FeiKojHYyiH1JxrA6lL1Y5l6pLfdJtvxcyXK016ShKjGfP5p11MVki%2B850t1AUb0cdpXIZrOXFyfWmZUwo4eP4AR7Zbh5UnZJK5l0K84%2B0TWKr973TtsyVTgrxI7Rrm%2FXAbolPSjuT6W2Y%2B2U1oqaTOTk%2Fb2SCmlLgpRNVGuieMACuHksWSs%2FQedbikkeEQzhzt95z4boE6UK1mLjZhbNKgvJzQNY3wNsfKbDLlNPbuqHdcd8WWIdcaR8atHcVYxGRN5JNlbNVSb8gkOEc9uOF2IFwobO5lBTJS9H08TQ0ixoyXmBpf79eSJ7UAdgy69V%2Bf8iYmowSNgegRdAitgyJJdoGwXUDoaHoHL3HwGBkCXrSh%2B%2Bv8SzWmIsP9Ovl%2Fo0O8FO4aGQcPL06WhT2aIwtFidNLImeDyHHc6ijFik3jllhZXT1qaCzRyHuC35wEMFGRaiZUJ4w1dabzwY6pgHrUgdgI3O1bC8oABv5YVjMqEW%2F7qTGJvei1XCihiCmXLCjM%2B7j5P%2BV%2BUKgUt7vKJmIrKvqOHJ8qPgG%2F%2FxgcF3PclGslsbXkEreBSkBceNB0NiADqkensiAPzYWPsJrFznI6eBsw%2FVX5Jn1FHDCyc4FBz0JsCknXoqIUWueZrx%2BtXd36%2BwCyuFdnn817oB%2FaXWA%2BhU2psda2URyCQ9Ftxi0gQ4xEPxc&X-Amz-Signature=b39e6fadf53276328643ea3ea86f5f8ad771e060762a3e51719f7c4f22ca3c89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNSX7IMC%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIHS1jMWsfKXTOSoWdnZ1zbFhjYr7rpOTzewwkDtYzY%2BLAiBOOsKSGN1i9DdOA3Qiw4Y%2Fr22qdeoAlppL3loolQB43Sr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMOZHOX7esCrTy2gvxKtwD1MQVESWNwQ1vpI79Omx9O8z%2FCuMAiA5RBZpnd1OkkKNCg1cld4zgJbMS7sdoh1lCBhrLxUF5yAvI7RAXkkpd0MNQfbUUi9ZK6nAjrXIcNyMPYMahCGsHiI2un7c0mDLiX4LOnRLowaG55Vk%2F3WW%2B9g94c8KEoQHwmOXr2c5y0vSD4%2F01Z%2B%2FeiKojHYyiH1JxrA6lL1Y5l6pLfdJtvxcyXK016ShKjGfP5p11MVki%2B850t1AUb0cdpXIZrOXFyfWmZUwo4eP4AR7Zbh5UnZJK5l0K84%2B0TWKr973TtsyVTgrxI7Rrm%2FXAbolPSjuT6W2Y%2B2U1oqaTOTk%2Fb2SCmlLgpRNVGuieMACuHksWSs%2FQedbikkeEQzhzt95z4boE6UK1mLjZhbNKgvJzQNY3wNsfKbDLlNPbuqHdcd8WWIdcaR8atHcVYxGRN5JNlbNVSb8gkOEc9uOF2IFwobO5lBTJS9H08TQ0ixoyXmBpf79eSJ7UAdgy69V%2Bf8iYmowSNgegRdAitgyJJdoGwXUDoaHoHL3HwGBkCXrSh%2B%2Bv8SzWmIsP9Ovl%2Fo0O8FO4aGQcPL06WhT2aIwtFidNLImeDyHHc6ijFik3jllhZXT1qaCzRyHuC35wEMFGRaiZUJ4w1dabzwY6pgHrUgdgI3O1bC8oABv5YVjMqEW%2F7qTGJvei1XCihiCmXLCjM%2B7j5P%2BV%2BUKgUt7vKJmIrKvqOHJ8qPgG%2F%2FxgcF3PclGslsbXkEreBSkBceNB0NiADqkensiAPzYWPsJrFznI6eBsw%2FVX5Jn1FHDCyc4FBz0JsCknXoqIUWueZrx%2BtXd36%2BwCyuFdnn817oB%2FaXWA%2BhU2psda2URyCQ9Ftxi0gQ4xEPxc&X-Amz-Signature=c029057662dc2d5375d824d00dd53aa6159ce84e2580072d1c66175a5839efa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNSX7IMC%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIHS1jMWsfKXTOSoWdnZ1zbFhjYr7rpOTzewwkDtYzY%2BLAiBOOsKSGN1i9DdOA3Qiw4Y%2Fr22qdeoAlppL3loolQB43Sr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMOZHOX7esCrTy2gvxKtwD1MQVESWNwQ1vpI79Omx9O8z%2FCuMAiA5RBZpnd1OkkKNCg1cld4zgJbMS7sdoh1lCBhrLxUF5yAvI7RAXkkpd0MNQfbUUi9ZK6nAjrXIcNyMPYMahCGsHiI2un7c0mDLiX4LOnRLowaG55Vk%2F3WW%2B9g94c8KEoQHwmOXr2c5y0vSD4%2F01Z%2B%2FeiKojHYyiH1JxrA6lL1Y5l6pLfdJtvxcyXK016ShKjGfP5p11MVki%2B850t1AUb0cdpXIZrOXFyfWmZUwo4eP4AR7Zbh5UnZJK5l0K84%2B0TWKr973TtsyVTgrxI7Rrm%2FXAbolPSjuT6W2Y%2B2U1oqaTOTk%2Fb2SCmlLgpRNVGuieMACuHksWSs%2FQedbikkeEQzhzt95z4boE6UK1mLjZhbNKgvJzQNY3wNsfKbDLlNPbuqHdcd8WWIdcaR8atHcVYxGRN5JNlbNVSb8gkOEc9uOF2IFwobO5lBTJS9H08TQ0ixoyXmBpf79eSJ7UAdgy69V%2Bf8iYmowSNgegRdAitgyJJdoGwXUDoaHoHL3HwGBkCXrSh%2B%2Bv8SzWmIsP9Ovl%2Fo0O8FO4aGQcPL06WhT2aIwtFidNLImeDyHHc6ijFik3jllhZXT1qaCzRyHuC35wEMFGRaiZUJ4w1dabzwY6pgHrUgdgI3O1bC8oABv5YVjMqEW%2F7qTGJvei1XCihiCmXLCjM%2B7j5P%2BV%2BUKgUt7vKJmIrKvqOHJ8qPgG%2F%2FxgcF3PclGslsbXkEreBSkBceNB0NiADqkensiAPzYWPsJrFznI6eBsw%2FVX5Jn1FHDCyc4FBz0JsCknXoqIUWueZrx%2BtXd36%2BwCyuFdnn817oB%2FaXWA%2BhU2psda2URyCQ9Ftxi0gQ4xEPxc&X-Amz-Signature=39533c0d87a5293d0b76ca499728b4b6548f434089a28e94407115e4171d1b6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

