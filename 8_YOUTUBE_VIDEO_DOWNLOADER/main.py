from pytube import YouTube
# v = "https://youtu.be/osokoTcr99k?si=DBmuz0OMAqQ0Gk8B"
def get_resolution(yt):
    res = input("Choose the Quality You want to download the video:\n1)High\n2)Low\n: ")
    if res in ['h','H','1']:
        return yt.streams.get_highest_resolution()
    
    elif res in ['l','L','2']:
        return yt.streams.get_lowest_resolution()

    else:
        print("Invalid Input!")
        return get_resolution(yt)

    

def main():
    print("I am a Youtube Video Downloader Bot, Just provide me with the link of video you want to download and i will Do it for you.")
    link = input("Enter the Link of the Video You wnt to download: ")
    yt = YouTube(link)
    print(yt.title)

    video = get_resolution(yt)

    location = input("Enter the Location At which You want to download the video? (By default it is the Downloads.) : ")
    path = location or r'C:\Users\DELL\Downloads'
    print("Your Video is downloading....")
    video.download(output_path=path)
    print("Your Video has been Downloaded")

if __name__ == "__main__":
    main()