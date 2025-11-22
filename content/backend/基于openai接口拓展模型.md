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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4JAM7RV%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQC2uYsh7QzjJrg4qisFIK0kYS8FEag0dg8PunfeE8Kr%2BwIgIraJbTDliFeJdEBCDlF85liCRfueWgYo7GpnMII0eT0q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDBtcA%2Bf7hVtTP8pIiCrcA3NI68rcqd4kadnlFNpWYGr38hkaHQeA%2B9roNtdoZlo5z1pFq4lfbWksyABP8ULqatQpL10Bk2D%2Fa2KHSEnRIGPEZ5hQdrCb%2BXsgQxwWkT2wNsD%2BnloeciZ3zKp1fuGTzf2HmSa090vRsNMOOiHlL11b02%2B3W56t2tl18BkMxUNTcwQTm5ATk8kZ%2Fn4A%2BDW0FKgpPtk2T6MP%2FnfnzfO0IzeXrjtpLWFaA1wCe4Fnd%2FOKB0zX07KIbj8wrzijxmRYNJ1brrVeCJUbqJEFFveNM30XmdJfsi3nwJhag1Z7l%2B2HPrOl5SSppre8GSyvI5n0eW4Sjwhd2ciKwdjd%2Bl9gvXsXUsWK0BMfmJD3eJf0LGWCIF9j2G51tj0dD5%2BjbJG8F7YE0qkoe0nBPt21tSVKVylSicckxstw1R3kl3BLDXFKpq%2F9NhB67bZCEgeKRNyeH18UKKzh0Yuow3syOEcZ0Nyqxyp%2Fqvhk6X%2FmFe3h3gygFIPy9Os%2BbZ0hm0bZR%2BQvy75%2FUU3PsiB4A0OqFesbteYZcRXF6Wk0FfOBUUXK97do6j4yJQBrVYC6CggmKjk3IBiI28QJOGWLUf9t9M%2BRl2kphpA9xfAdkusqUXnLuUWpu%2FD910xT6O%2F2p95aMM6ghMkGOqUBITIRIVRnSn2t6iy%2B2SjpIzJC9Ff74TbidxlvkRhLZJClJsmDfMJP12HXGzJdTXUj4NhBgCTa1V4tYz9gyzHJ%2F8AmST6bOa11F9bPeXXg1G9p66bhJVJiSPTrGlN7Hl7kXDKnJhoXi6Dw8MfcgSM5HV0XtwI53xUSoPlP7o3zYAVcmCeab8%2FaOnOjAr5%2Byllj0dXJuucvB0S8z0qzOgfc72phfsHf&X-Amz-Signature=547fb8b605dd515b87243d7b2f43aa7c0a1f435480babb0e2cbec9384b98ef15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4JAM7RV%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQC2uYsh7QzjJrg4qisFIK0kYS8FEag0dg8PunfeE8Kr%2BwIgIraJbTDliFeJdEBCDlF85liCRfueWgYo7GpnMII0eT0q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDBtcA%2Bf7hVtTP8pIiCrcA3NI68rcqd4kadnlFNpWYGr38hkaHQeA%2B9roNtdoZlo5z1pFq4lfbWksyABP8ULqatQpL10Bk2D%2Fa2KHSEnRIGPEZ5hQdrCb%2BXsgQxwWkT2wNsD%2BnloeciZ3zKp1fuGTzf2HmSa090vRsNMOOiHlL11b02%2B3W56t2tl18BkMxUNTcwQTm5ATk8kZ%2Fn4A%2BDW0FKgpPtk2T6MP%2FnfnzfO0IzeXrjtpLWFaA1wCe4Fnd%2FOKB0zX07KIbj8wrzijxmRYNJ1brrVeCJUbqJEFFveNM30XmdJfsi3nwJhag1Z7l%2B2HPrOl5SSppre8GSyvI5n0eW4Sjwhd2ciKwdjd%2Bl9gvXsXUsWK0BMfmJD3eJf0LGWCIF9j2G51tj0dD5%2BjbJG8F7YE0qkoe0nBPt21tSVKVylSicckxstw1R3kl3BLDXFKpq%2F9NhB67bZCEgeKRNyeH18UKKzh0Yuow3syOEcZ0Nyqxyp%2Fqvhk6X%2FmFe3h3gygFIPy9Os%2BbZ0hm0bZR%2BQvy75%2FUU3PsiB4A0OqFesbteYZcRXF6Wk0FfOBUUXK97do6j4yJQBrVYC6CggmKjk3IBiI28QJOGWLUf9t9M%2BRl2kphpA9xfAdkusqUXnLuUWpu%2FD910xT6O%2F2p95aMM6ghMkGOqUBITIRIVRnSn2t6iy%2B2SjpIzJC9Ff74TbidxlvkRhLZJClJsmDfMJP12HXGzJdTXUj4NhBgCTa1V4tYz9gyzHJ%2F8AmST6bOa11F9bPeXXg1G9p66bhJVJiSPTrGlN7Hl7kXDKnJhoXi6Dw8MfcgSM5HV0XtwI53xUSoPlP7o3zYAVcmCeab8%2FaOnOjAr5%2Byllj0dXJuucvB0S8z0qzOgfc72phfsHf&X-Amz-Signature=621ae89678b86672946bcc608ba31ec604472b46f9806d5eca7d99a44c66c862&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4JAM7RV%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQC2uYsh7QzjJrg4qisFIK0kYS8FEag0dg8PunfeE8Kr%2BwIgIraJbTDliFeJdEBCDlF85liCRfueWgYo7GpnMII0eT0q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDBtcA%2Bf7hVtTP8pIiCrcA3NI68rcqd4kadnlFNpWYGr38hkaHQeA%2B9roNtdoZlo5z1pFq4lfbWksyABP8ULqatQpL10Bk2D%2Fa2KHSEnRIGPEZ5hQdrCb%2BXsgQxwWkT2wNsD%2BnloeciZ3zKp1fuGTzf2HmSa090vRsNMOOiHlL11b02%2B3W56t2tl18BkMxUNTcwQTm5ATk8kZ%2Fn4A%2BDW0FKgpPtk2T6MP%2FnfnzfO0IzeXrjtpLWFaA1wCe4Fnd%2FOKB0zX07KIbj8wrzijxmRYNJ1brrVeCJUbqJEFFveNM30XmdJfsi3nwJhag1Z7l%2B2HPrOl5SSppre8GSyvI5n0eW4Sjwhd2ciKwdjd%2Bl9gvXsXUsWK0BMfmJD3eJf0LGWCIF9j2G51tj0dD5%2BjbJG8F7YE0qkoe0nBPt21tSVKVylSicckxstw1R3kl3BLDXFKpq%2F9NhB67bZCEgeKRNyeH18UKKzh0Yuow3syOEcZ0Nyqxyp%2Fqvhk6X%2FmFe3h3gygFIPy9Os%2BbZ0hm0bZR%2BQvy75%2FUU3PsiB4A0OqFesbteYZcRXF6Wk0FfOBUUXK97do6j4yJQBrVYC6CggmKjk3IBiI28QJOGWLUf9t9M%2BRl2kphpA9xfAdkusqUXnLuUWpu%2FD910xT6O%2F2p95aMM6ghMkGOqUBITIRIVRnSn2t6iy%2B2SjpIzJC9Ff74TbidxlvkRhLZJClJsmDfMJP12HXGzJdTXUj4NhBgCTa1V4tYz9gyzHJ%2F8AmST6bOa11F9bPeXXg1G9p66bhJVJiSPTrGlN7Hl7kXDKnJhoXi6Dw8MfcgSM5HV0XtwI53xUSoPlP7o3zYAVcmCeab8%2FaOnOjAr5%2Byllj0dXJuucvB0S8z0qzOgfc72phfsHf&X-Amz-Signature=75489c5d6058d4f3eb355f5a27eeccb1a94c51bf02d1c850f082a497ab0809ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

