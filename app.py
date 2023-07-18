import webbrowser

def play_youtube_video(video_url):
    try:
        webbrowser.open(video_url)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    youtube_video_url = "https://www.youtube.com/watch?v=8kTOhY2fVkw"
    play_youtube_video(youtube_video_url)
