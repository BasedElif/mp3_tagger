
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os




def get_name(f):

    name = ""
    for lt in f[::-1]:
        if lt != "/": name += lt
        else: break

    return name[::-1]

def get_path(f):

    path = ""
    for cnt , lt in enumerate(f[::-1]):
        if lt == "/":
            return (f[:len(f)-cnt])




def modify(f,fname = "",title = "", artist = "",album = "", nr = -1):

    file = f
    audio = MP3(file,ID3 = EasyID3)

    path = get_path(file)
    current_name = get_name(file)
    full_path = path + current_name


    if title != "":
        audio["TITLE"] = title

    if artist != "":
        audio["ARTIST"] = artist

    if album != "":
        audio["ALBUM"] = album

    if nr != -1:
        audio["TRACKNUMBER"] = str(nr)

    audio.save()

    if fname != "":
        os.rename(full_path,path + fname + ".mp3")
