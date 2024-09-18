import yt_dlp
import os
import pyperclip
# 파일명에 사용할 수 없는 문자들을 '_'로 바꾸는 함수
def format_filename(title):
    return "".join(c if c.isalnum() or c in (' ', '.', '_') else '_' for c in title)

# YouTube 영상을 다운로드하고 WAV로 변환하는 함수
def download_youtube_as_wav(video_url):
    # YouTube 영상의 정보를 추출 (제목 포함)
    ydl_opts = {
        'quiet': True,  # 출력 억제 (필요없는 출력 제거)
        'format': 'bestaudio/best',  # 오디오만 다운로드
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)  # 정보만 추출
        title = info_dict.get('title', 'audio')  # 제목 가져오기, 없으면 'audio'
        formatted_title = format_filename(title)  # 파일 이름으로 사용할 수 있도록 변환
        output_file = f"{formatted_title}.wav"  # 출력 파일명 설정
    
    # WAV로 다운로드 및 변환
    ydl_opts = {
        'format': 'bestaudio/best',  # 최고 품질 오디오 다운로드
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # WAV로 변환
            'preferredquality': '192',  # 품질 설정 (kbps)
        }],
        'outtmpl': output_file  # 출력 파일 템플릿
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    
    print(f"다운로드 및 변환 완료: {output_file}")

# 사용 예시
video_url = pyperclip.paste()
download_youtube_as_wav(video_url)
