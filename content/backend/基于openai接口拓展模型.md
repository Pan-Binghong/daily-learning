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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UW43NQW%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIG%2Bj1u1W4B78EUgKEf3%2BOSsUmP8iL4N2DjajOtskz42iAiEArl5Z3Q9GgxwsVMCzEvaQxDLkTDM%2F7%2BRyBAhYAmpITiUqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLgM4sWjxA9HOMBfyrcA3ujkHkF%2FJwSicsSgOcyWUEy4vuBLrXHJM5mIpe3GIbLMHJGHEkN%2FbC%2F2VrkjdpxFbNsc%2BDbupCiEIahzkG1CjaSbwyV5zRrjES6SRtdzftvHnB7lgiuDQ3MuHZJAEDRBjxgqadZigfwANyXsX1SKILIpjmETJH5rgEdABnzMYRU%2FOWZ1hUpBNZg9Ufv9yybu%2F%2FbaIJtPDdZQL2JmF4Msdv6UiirqQS67N8lQlAbwVk%2BF%2FFd0EaiCFy%2BQeigwZt%2Bi1da9CEbwdo%2BqJOffDk%2FyvSsXKxnMepQmk9cHI2SXUqNxSR1Vz6bWi97jq3VghiB7tbn3a4t%2FSBccrSs2t77Un5LEBi8NRvprxtlGF1VLuGONT1YuawOWFmQ2KgXDebIWPfTXNbowXBCMtWH8D2PvXwLbR42mNcDzvZDgCwS1s7IKKDXHZnsJFXJDrtTlBGwejoghEOZgB0nhqBT%2FmHgZwW3JF67Wf7Tr%2ByABQgSKmUIWV0OAP55kGkqKUJXYro1dx9KRFc7IOzl%2FyEedCDhlZCCFj%2BCiVNTQUOZMsVaR1AFlOJ%2BAsiGq3XLOnQBcuMfNXdEKF9K%2BYpJpisbAWc5z%2FBZGxR6PB%2FKc%2BTCQ09UnqWmEQXS6Ig6yhG8v9XIMN7%2Fi8sGOqUBOZEmw8CZ8sdzgMHseEOZhfPdeZgauI6kwRoDai7QCTHYR0BhEqEZjqmH9S%2FlvNnz4iceUzDTUTnhQ0tCS2oMafPARW%2BUPiyHpzBsUKfouIqdnXOmqM3BGVoSahmbTkBYhjTptu3mQ4cfJJB7OH%2FrLSp7VHDWcP%2BVizrfXsK6JysZew5Xd07gmv4J6CY%2F7YCos7Qr8%2FuAzYbwmAV65%2FDqut%2BPx3x2&X-Amz-Signature=147603933308b1fb9f91538c65c9197b51222c4420640dc80ee84aaf19fcc1dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UW43NQW%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIG%2Bj1u1W4B78EUgKEf3%2BOSsUmP8iL4N2DjajOtskz42iAiEArl5Z3Q9GgxwsVMCzEvaQxDLkTDM%2F7%2BRyBAhYAmpITiUqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLgM4sWjxA9HOMBfyrcA3ujkHkF%2FJwSicsSgOcyWUEy4vuBLrXHJM5mIpe3GIbLMHJGHEkN%2FbC%2F2VrkjdpxFbNsc%2BDbupCiEIahzkG1CjaSbwyV5zRrjES6SRtdzftvHnB7lgiuDQ3MuHZJAEDRBjxgqadZigfwANyXsX1SKILIpjmETJH5rgEdABnzMYRU%2FOWZ1hUpBNZg9Ufv9yybu%2F%2FbaIJtPDdZQL2JmF4Msdv6UiirqQS67N8lQlAbwVk%2BF%2FFd0EaiCFy%2BQeigwZt%2Bi1da9CEbwdo%2BqJOffDk%2FyvSsXKxnMepQmk9cHI2SXUqNxSR1Vz6bWi97jq3VghiB7tbn3a4t%2FSBccrSs2t77Un5LEBi8NRvprxtlGF1VLuGONT1YuawOWFmQ2KgXDebIWPfTXNbowXBCMtWH8D2PvXwLbR42mNcDzvZDgCwS1s7IKKDXHZnsJFXJDrtTlBGwejoghEOZgB0nhqBT%2FmHgZwW3JF67Wf7Tr%2ByABQgSKmUIWV0OAP55kGkqKUJXYro1dx9KRFc7IOzl%2FyEedCDhlZCCFj%2BCiVNTQUOZMsVaR1AFlOJ%2BAsiGq3XLOnQBcuMfNXdEKF9K%2BYpJpisbAWc5z%2FBZGxR6PB%2FKc%2BTCQ09UnqWmEQXS6Ig6yhG8v9XIMN7%2Fi8sGOqUBOZEmw8CZ8sdzgMHseEOZhfPdeZgauI6kwRoDai7QCTHYR0BhEqEZjqmH9S%2FlvNnz4iceUzDTUTnhQ0tCS2oMafPARW%2BUPiyHpzBsUKfouIqdnXOmqM3BGVoSahmbTkBYhjTptu3mQ4cfJJB7OH%2FrLSp7VHDWcP%2BVizrfXsK6JysZew5Xd07gmv4J6CY%2F7YCos7Qr8%2FuAzYbwmAV65%2FDqut%2BPx3x2&X-Amz-Signature=2e9c0118d525fcdecf8f167162bc8afdff13cd09a93ce0f7e6c3dfc94e309b9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UW43NQW%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIG%2Bj1u1W4B78EUgKEf3%2BOSsUmP8iL4N2DjajOtskz42iAiEArl5Z3Q9GgxwsVMCzEvaQxDLkTDM%2F7%2BRyBAhYAmpITiUqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLgM4sWjxA9HOMBfyrcA3ujkHkF%2FJwSicsSgOcyWUEy4vuBLrXHJM5mIpe3GIbLMHJGHEkN%2FbC%2F2VrkjdpxFbNsc%2BDbupCiEIahzkG1CjaSbwyV5zRrjES6SRtdzftvHnB7lgiuDQ3MuHZJAEDRBjxgqadZigfwANyXsX1SKILIpjmETJH5rgEdABnzMYRU%2FOWZ1hUpBNZg9Ufv9yybu%2F%2FbaIJtPDdZQL2JmF4Msdv6UiirqQS67N8lQlAbwVk%2BF%2FFd0EaiCFy%2BQeigwZt%2Bi1da9CEbwdo%2BqJOffDk%2FyvSsXKxnMepQmk9cHI2SXUqNxSR1Vz6bWi97jq3VghiB7tbn3a4t%2FSBccrSs2t77Un5LEBi8NRvprxtlGF1VLuGONT1YuawOWFmQ2KgXDebIWPfTXNbowXBCMtWH8D2PvXwLbR42mNcDzvZDgCwS1s7IKKDXHZnsJFXJDrtTlBGwejoghEOZgB0nhqBT%2FmHgZwW3JF67Wf7Tr%2ByABQgSKmUIWV0OAP55kGkqKUJXYro1dx9KRFc7IOzl%2FyEedCDhlZCCFj%2BCiVNTQUOZMsVaR1AFlOJ%2BAsiGq3XLOnQBcuMfNXdEKF9K%2BYpJpisbAWc5z%2FBZGxR6PB%2FKc%2BTCQ09UnqWmEQXS6Ig6yhG8v9XIMN7%2Fi8sGOqUBOZEmw8CZ8sdzgMHseEOZhfPdeZgauI6kwRoDai7QCTHYR0BhEqEZjqmH9S%2FlvNnz4iceUzDTUTnhQ0tCS2oMafPARW%2BUPiyHpzBsUKfouIqdnXOmqM3BGVoSahmbTkBYhjTptu3mQ4cfJJB7OH%2FrLSp7VHDWcP%2BVizrfXsK6JysZew5Xd07gmv4J6CY%2F7YCos7Qr8%2FuAzYbwmAV65%2FDqut%2BPx3x2&X-Amz-Signature=862569bb1e638accbd7535b514c8c81ddbf8e45ff52236b0c32e4333a3b91602&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

