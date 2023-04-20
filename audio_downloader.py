import os
from pydub import AudioSegment
#Open folder
#Get each line as song
#split link and file name
#download

songs_path = 'download_songs.txt'

if os.path.exists(songs_path):
    with open(songs_path, encoding='utf-8') as txt_file:
        file_stream = txt_file.read() 
        song_list = file_stream.split('\n') 
        print(song_list)

        for song in song_list:
            song_url = song.split(' ', 1)[0]
            song_name = song.split(' ', 1)[1]
            print(song_url)
            
            os.system(f'yt-dlp "{song_url}" -o "{song_name}.m4a" --format "140"')

            AudioSegment.from_file(f"{song_name}.m4a").export(f"{song_name}", format="mp3")