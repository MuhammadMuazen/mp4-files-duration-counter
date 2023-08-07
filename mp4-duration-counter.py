from tinytag import TinyTag
from datetime import timedelta
import glob
import os

full_duration = 0
folder_path = r'C:\example\example' # Change This
folder_path += r'\**\*.mp4'
video_files = glob.glob(folder_path, recursive=True)

for video_file in video_files:
    video_file_prop = TinyTag.get(video_file)
    video_duration = timedelta(seconds=video_file_prop.duration)
    print(f'{os.path.basename(video_file)} ==> {video_duration}')
    full_duration += video_file_prop.duration
    

print(f'The full Duration is {timedelta(seconds=full_duration)}')

