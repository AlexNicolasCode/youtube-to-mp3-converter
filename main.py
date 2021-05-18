import youtube_dl
import os.path

def run():
  # Add url of your musics here
  musics_url = []

  def search():
    for music in musics_url:
      video_info = youtube_dl.YoutubeDL().extract_info(
          url = music,download=False
      )

      filename = f"{video_info['title']}.mp3"
      options={
          'format':'bestaudio/best',
          'keepvideo':False,
          'outtmpl':filename,
      }

      if os.path.isfile(filename):
        print("This file already exist")
        musics_url.remove(music)
        if musics_url == []:
          musics_url.append(input("please enter youtube video url:"))
          search()
        else: search()
      else:
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
        musics_url.remove(music)
        if musics_url == []:
          run()
        else: search()

  if musics_url == []:
    musics_url.append(input("please enter youtube video url:"))
    search()
  else: 
    print("Searching musics...")
    search()

if __name__=='__main__':
  run()