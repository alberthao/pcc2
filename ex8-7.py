#Author: Alberthao
#Topic: Function

def make_album(singer_name,album_name,song_no=None):
    singer = {"singer name":singer_name,"album":album_name}
    if song_no:
        singer['song_no']=song_no
    return singer

singer1 = make_album("zhoujielun",'qinghuaci')
print(singer1)

singer2 = make_album("Mao Ning",'Taoshengyijiu',22)
print(singer2)

singer3 = make_album("Qi Qin",'Wolf')
print(singer3)