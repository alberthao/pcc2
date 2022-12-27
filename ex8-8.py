#Author: Alberthao
#Topic: Function

def make_album(singer_name,album_name):
    singer= {"singer name":singer_name,"album":album_name}
    return singer

while True:
    print("\nPlease tell me singer name and album name:")
    print("(enter 'q' at any time to quit)")

    singer_name=input("Singer name:")
    if singer_name=='q':
        break
    album_name = input("Album name:")
    if album_name=='q':
        break

    singerx = make_album(singer_name,album_name)
    print(singerx)



