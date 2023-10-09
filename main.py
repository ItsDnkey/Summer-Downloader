from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

print("""   
   _____ _    _ __  __ __  __ ______ _____  
  / ____| |  | |  \/  |  \/  |  ____|  __ \ 
 | (___ | |  | | \  / | \  / | |__  | |__) |
  \___ \| |  | | |\/| | |\/| |  __| |  _  / 
  ____) | |__| | |  | | |  | | |____| | \ \ 
 |_____/ \____/|_|  |_|_|  |_|______|_|  \_\
 
 By @ItsDnkey on github !                                           
                                            
                                            """)
link = input("Enter the YouTube video URL: ")
Download(link)
