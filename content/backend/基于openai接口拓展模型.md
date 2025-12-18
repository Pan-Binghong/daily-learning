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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/78a35635-95f3-4c36-8041-b8259dfc81b6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSHAC3BR%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdu%2B5MOzb0dyYWz%2BozObXn1lTjnTyoywfdfiwfjzU2OAiBqj2rUWs%2BeSs4eCxBRCZO39i4SebO2zvn7Q1J0uW7UdSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6apY0WiHtO3lhuCIKtwDBJ0UTszsFh1YujsaynAOHEdL%2Bw8oMp%2FocdpcsmJKQzami3m59PGWvrZZK3OWMl3daDbQhCfA9QdqDrGBICbMCdmvijs1QxVW5%2F9tPO3uHOy9I0SOS%2Fhn53fzMw4GiUhcjWTVTeamx%2FdbLASieweEEzVZG45x6Bpze8wXEVK3NRDXr2XpIzPLE0kVt8OLVzkHF%2F%2F6DmhMC0DaoD7apvha%2Ba0l6j8neVvvisEFUkC%2FTRvJbv3%2Bfd2AbAE7ut3ky5Srjcw3OXO%2Bq5HKhAIOhkYvfLfgMyTUvTkZyDbpm7zPGOW5pv2NpQy3GKbaOaoavSlifLAs2ii4R5%2FT2rEKlC3i2KnmdrBTEsfh8sALgVdD0zkt8zWI29vdUyNMOkpwj%2B7GSNxPQA6oJfXDW4JS%2F1DtqTrWfzZF7L2wlOfciL8y74RFDK5yiqYHBjhuOiKvfsVzAETmr969ivx3U34kmTQ89vUisPTNvl4JbGc%2BCraNKCCXP1UDvRun0b2%2F3cMNWODTstPKyEGT%2BH29LBGteC9bHhrqv2LTyVV%2F%2BsLopBG1AAJWcqIp5YQY9gIZPNnIU%2Fi5R3Hl5FOAiU6ObNaID%2BK6Xa2yu42TcnDsEnp4GdQufn6XU8aIUpzCRh6l4l8wt8mNygY6pgGoRUgyG%2Fhn7SH0lGXp2USkQ2KSwK8uFRL6lLHtC%2FJh%2BCedqQyeSnbKFAYy0JHWOSiMlCIp0UDu%2Bl%2FDdg8pC8L4JqAPAGX9iq71utyTtHrE6Su2bllZ0fsUPAVee3S0cRTHPnInZ0pkXl6v9avJ2WlbgrJTrqzHoxwK5Alnz8np3me4bRY%2BujHUVEIY96m1R4DjpBSt%2B7Uq00rukgHQj0T3F75Rp78F&X-Amz-Signature=17de39ab1e53631e6644240cc2132b2597bafc846ef8fe3e40cba412998f63dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Whisper

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/4e675ff3-4c7a-43cf-979c-816d82e91e6e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSHAC3BR%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdu%2B5MOzb0dyYWz%2BozObXn1lTjnTyoywfdfiwfjzU2OAiBqj2rUWs%2BeSs4eCxBRCZO39i4SebO2zvn7Q1J0uW7UdSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6apY0WiHtO3lhuCIKtwDBJ0UTszsFh1YujsaynAOHEdL%2Bw8oMp%2FocdpcsmJKQzami3m59PGWvrZZK3OWMl3daDbQhCfA9QdqDrGBICbMCdmvijs1QxVW5%2F9tPO3uHOy9I0SOS%2Fhn53fzMw4GiUhcjWTVTeamx%2FdbLASieweEEzVZG45x6Bpze8wXEVK3NRDXr2XpIzPLE0kVt8OLVzkHF%2F%2F6DmhMC0DaoD7apvha%2Ba0l6j8neVvvisEFUkC%2FTRvJbv3%2Bfd2AbAE7ut3ky5Srjcw3OXO%2Bq5HKhAIOhkYvfLfgMyTUvTkZyDbpm7zPGOW5pv2NpQy3GKbaOaoavSlifLAs2ii4R5%2FT2rEKlC3i2KnmdrBTEsfh8sALgVdD0zkt8zWI29vdUyNMOkpwj%2B7GSNxPQA6oJfXDW4JS%2F1DtqTrWfzZF7L2wlOfciL8y74RFDK5yiqYHBjhuOiKvfsVzAETmr969ivx3U34kmTQ89vUisPTNvl4JbGc%2BCraNKCCXP1UDvRun0b2%2F3cMNWODTstPKyEGT%2BH29LBGteC9bHhrqv2LTyVV%2F%2BsLopBG1AAJWcqIp5YQY9gIZPNnIU%2Fi5R3Hl5FOAiU6ObNaID%2BK6Xa2yu42TcnDsEnp4GdQufn6XU8aIUpzCRh6l4l8wt8mNygY6pgGoRUgyG%2Fhn7SH0lGXp2USkQ2KSwK8uFRL6lLHtC%2FJh%2BCedqQyeSnbKFAYy0JHWOSiMlCIp0UDu%2Bl%2FDdg8pC8L4JqAPAGX9iq71utyTtHrE6Su2bllZ0fsUPAVee3S0cRTHPnInZ0pkXl6v9avJ2WlbgrJTrqzHoxwK5Alnz8np3me4bRY%2BujHUVEIY96m1R4DjpBSt%2B7Uq00rukgHQj0T3F75Rp78F&X-Amz-Signature=3f6aa3d654b61d0e1e5a31b66db95ea58679bba694074d3e2da4c5d661d68bc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### TTS-1

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0b2043c6-b69a-4903-9ee3-aec03d8c5ef4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSHAC3BR%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFdu%2B5MOzb0dyYWz%2BozObXn1lTjnTyoywfdfiwfjzU2OAiBqj2rUWs%2BeSs4eCxBRCZO39i4SebO2zvn7Q1J0uW7UdSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6apY0WiHtO3lhuCIKtwDBJ0UTszsFh1YujsaynAOHEdL%2Bw8oMp%2FocdpcsmJKQzami3m59PGWvrZZK3OWMl3daDbQhCfA9QdqDrGBICbMCdmvijs1QxVW5%2F9tPO3uHOy9I0SOS%2Fhn53fzMw4GiUhcjWTVTeamx%2FdbLASieweEEzVZG45x6Bpze8wXEVK3NRDXr2XpIzPLE0kVt8OLVzkHF%2F%2F6DmhMC0DaoD7apvha%2Ba0l6j8neVvvisEFUkC%2FTRvJbv3%2Bfd2AbAE7ut3ky5Srjcw3OXO%2Bq5HKhAIOhkYvfLfgMyTUvTkZyDbpm7zPGOW5pv2NpQy3GKbaOaoavSlifLAs2ii4R5%2FT2rEKlC3i2KnmdrBTEsfh8sALgVdD0zkt8zWI29vdUyNMOkpwj%2B7GSNxPQA6oJfXDW4JS%2F1DtqTrWfzZF7L2wlOfciL8y74RFDK5yiqYHBjhuOiKvfsVzAETmr969ivx3U34kmTQ89vUisPTNvl4JbGc%2BCraNKCCXP1UDvRun0b2%2F3cMNWODTstPKyEGT%2BH29LBGteC9bHhrqv2LTyVV%2F%2BsLopBG1AAJWcqIp5YQY9gIZPNnIU%2Fi5R3Hl5FOAiU6ObNaID%2BK6Xa2yu42TcnDsEnp4GdQufn6XU8aIUpzCRh6l4l8wt8mNygY6pgGoRUgyG%2Fhn7SH0lGXp2USkQ2KSwK8uFRL6lLHtC%2FJh%2BCedqQyeSnbKFAYy0JHWOSiMlCIp0UDu%2Bl%2FDdg8pC8L4JqAPAGX9iq71utyTtHrE6Su2bllZ0fsUPAVee3S0cRTHPnInZ0pkXl6v9avJ2WlbgrJTrqzHoxwK5Alnz8np3me4bRY%2BujHUVEIY96m1R4DjpBSt%2B7Uq00rukgHQj0T3F75Rp78F&X-Amz-Signature=1c70b2d648223f9ec693f567be6a3f461238de29c86116877aa932b26a5200fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

