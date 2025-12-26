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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYB2TRMQ%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICuLAKZ9Buu7Eu%2FrLRdtOrNnkRFPjUMAdfc50POB%2FHyrAiAfALnpfMcy1Hp8HBMntG%2FsvtSgOzeDSgIJ4ETNfP9L3Sr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMGZNUzUUxa%2FsZWAkvKtwDCtpl9likViiMN6XlZLSttihvbIqpKRR2rc2cww%2F0%2FOb6ZNI8%2BJuAVPR3eZCUjaIdXmouspKNY2c%2BZx2L97vGpY9bhdLPcVlcJFLigZKYrXYDSQnSr2t6tzxlG1uZxvYS9wc%2FafRtUp%2BdKrVoKS1Tw56saTpg9CxxY93KxydTNAyhGHnna0lj3lX57xiZgt5zNT3cLssdrgheKINUwSzdh1c7aLH4td2IAAbiTRJwqTlOhGZwTPMvwQOZhCkS5GnIQX7PfCI4AKxlCRruuVJTNgcVztBiJXI2jSNQDE7Pcto16CknPtTkMxzXHr16%2BMgZpznvfczOo4osDrXgXTK1MuksTcd2pbLMS4s9DAc05SKze2C0SnHY%2FIpDZfOS7tpM1KG1i%2BH9RgNGgDRxYCbUTjcOii%2F%2BeH4gRhnlManVEQzTv9Zm%2F65O5RZvGa0mGc%2FsxA3%2F9GqAk3fFS9gWRnGc2gGQ53uHEG2fX0leL8o3gG3v79xaIXZBfCaSVcRODm02ggY35f7gaqRuVSsjNAp5b8RFX%2FMuE5Q4hUD8rAymlHBICNLMM%2FJKJuu4uPr6O7CvHwKGgpNvy0uecNqbo1pE4gynczCi6XWyzySDrCUOyaowawVU5m8M5ATxIWcwyte3ygY6pgF%2FYT2FaA6XcXoeZli1oPk8fivGoEN5pRTrglNMzW9SNzeQENDlUMAjbzCzrbUMmyxezhLQWQSnyf93QY0EUdoOtgLlREfBg8aXHhXmU3TXYZJzfXFVch8vAwHJFAIM7gL5DNyJNlfHXmTXw18Ga1NKMUGK%2FDoqsvBlDxYTChHyebKy30ziZ7gZIT%2FvvmnfVBarJt45z17uO%2BoxRbxR6t8aEIoAeXIa&X-Amz-Signature=d7dbb5b88c912766caca84551d4b11e32cca98385165e1537010752667f8bdbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYB2TRMQ%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICuLAKZ9Buu7Eu%2FrLRdtOrNnkRFPjUMAdfc50POB%2FHyrAiAfALnpfMcy1Hp8HBMntG%2FsvtSgOzeDSgIJ4ETNfP9L3Sr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMGZNUzUUxa%2FsZWAkvKtwDCtpl9likViiMN6XlZLSttihvbIqpKRR2rc2cww%2F0%2FOb6ZNI8%2BJuAVPR3eZCUjaIdXmouspKNY2c%2BZx2L97vGpY9bhdLPcVlcJFLigZKYrXYDSQnSr2t6tzxlG1uZxvYS9wc%2FafRtUp%2BdKrVoKS1Tw56saTpg9CxxY93KxydTNAyhGHnna0lj3lX57xiZgt5zNT3cLssdrgheKINUwSzdh1c7aLH4td2IAAbiTRJwqTlOhGZwTPMvwQOZhCkS5GnIQX7PfCI4AKxlCRruuVJTNgcVztBiJXI2jSNQDE7Pcto16CknPtTkMxzXHr16%2BMgZpznvfczOo4osDrXgXTK1MuksTcd2pbLMS4s9DAc05SKze2C0SnHY%2FIpDZfOS7tpM1KG1i%2BH9RgNGgDRxYCbUTjcOii%2F%2BeH4gRhnlManVEQzTv9Zm%2F65O5RZvGa0mGc%2FsxA3%2F9GqAk3fFS9gWRnGc2gGQ53uHEG2fX0leL8o3gG3v79xaIXZBfCaSVcRODm02ggY35f7gaqRuVSsjNAp5b8RFX%2FMuE5Q4hUD8rAymlHBICNLMM%2FJKJuu4uPr6O7CvHwKGgpNvy0uecNqbo1pE4gynczCi6XWyzySDrCUOyaowawVU5m8M5ATxIWcwyte3ygY6pgF%2FYT2FaA6XcXoeZli1oPk8fivGoEN5pRTrglNMzW9SNzeQENDlUMAjbzCzrbUMmyxezhLQWQSnyf93QY0EUdoOtgLlREfBg8aXHhXmU3TXYZJzfXFVch8vAwHJFAIM7gL5DNyJNlfHXmTXw18Ga1NKMUGK%2FDoqsvBlDxYTChHyebKy30ziZ7gZIT%2FvvmnfVBarJt45z17uO%2BoxRbxR6t8aEIoAeXIa&X-Amz-Signature=5f07ba769db99a017405a1cfa27577105e8cdf4dccd1e9b3672129233fc88d8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYB2TRMQ%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICuLAKZ9Buu7Eu%2FrLRdtOrNnkRFPjUMAdfc50POB%2FHyrAiAfALnpfMcy1Hp8HBMntG%2FsvtSgOzeDSgIJ4ETNfP9L3Sr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMGZNUzUUxa%2FsZWAkvKtwDCtpl9likViiMN6XlZLSttihvbIqpKRR2rc2cww%2F0%2FOb6ZNI8%2BJuAVPR3eZCUjaIdXmouspKNY2c%2BZx2L97vGpY9bhdLPcVlcJFLigZKYrXYDSQnSr2t6tzxlG1uZxvYS9wc%2FafRtUp%2BdKrVoKS1Tw56saTpg9CxxY93KxydTNAyhGHnna0lj3lX57xiZgt5zNT3cLssdrgheKINUwSzdh1c7aLH4td2IAAbiTRJwqTlOhGZwTPMvwQOZhCkS5GnIQX7PfCI4AKxlCRruuVJTNgcVztBiJXI2jSNQDE7Pcto16CknPtTkMxzXHr16%2BMgZpznvfczOo4osDrXgXTK1MuksTcd2pbLMS4s9DAc05SKze2C0SnHY%2FIpDZfOS7tpM1KG1i%2BH9RgNGgDRxYCbUTjcOii%2F%2BeH4gRhnlManVEQzTv9Zm%2F65O5RZvGa0mGc%2FsxA3%2F9GqAk3fFS9gWRnGc2gGQ53uHEG2fX0leL8o3gG3v79xaIXZBfCaSVcRODm02ggY35f7gaqRuVSsjNAp5b8RFX%2FMuE5Q4hUD8rAymlHBICNLMM%2FJKJuu4uPr6O7CvHwKGgpNvy0uecNqbo1pE4gynczCi6XWyzySDrCUOyaowawVU5m8M5ATxIWcwyte3ygY6pgF%2FYT2FaA6XcXoeZli1oPk8fivGoEN5pRTrglNMzW9SNzeQENDlUMAjbzCzrbUMmyxezhLQWQSnyf93QY0EUdoOtgLlREfBg8aXHhXmU3TXYZJzfXFVch8vAwHJFAIM7gL5DNyJNlfHXmTXw18Ga1NKMUGK%2FDoqsvBlDxYTChHyebKy30ziZ7gZIT%2FvvmnfVBarJt45z17uO%2BoxRbxR6t8aEIoAeXIa&X-Amz-Signature=4dd6deeea02b2717cfdf50b0f9718ac5526cf5dddb6f730811651fefcb523683&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

