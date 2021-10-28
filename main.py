from youtube_dl import YoutubeDL

def youtube_download_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        mp3_list = ydl.extract_info(playlist_url, download=False)['entries']
        
        for mp3 in mp3_list:
            print('Downloading' + (mp3['title']))
            ydl.download([mp3['webpage_url']])
        
    print("Download complete!")
    
input_url = input("Enter the URL of the playlist: ")
youtube_download_playlist(input_url)
print("Downloading playlist...")