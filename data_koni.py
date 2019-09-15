from bs4 import BeautifulSoup
import re , os , requests

get_url = requests.get("http://siolga.konibali.or.id/biodata/0")
file = open('data.txt','w')
def data_capture(url,page=1):
    global file
    if url != "http://siolga.konibali.or.id/biodata/0":
        link = requests.get("http://siolga.konibali.or.id/biodata/"+ str(page))
    if url == "http://siolga.konibali.or.id/biodata/5000":
        return False
    soup = BeautifulSoup(url.content,'lxml')
    text = soup.get_text()
    predata = re.findall(".*\n:\n.*",text)
    img_all = soup.find_all("img")
    img = img_all[2]["src"]
    if img != "http://siolga.konibali.or.id/img/no-image.jpg":
        file.write(f'Link gambar : {img}\n')
    data_dict= {}
    for i in predata:
        space = i.replace('\n',' ')
        listkan = space.split(":")
        data_dict[listkan[0]] = listkan[1]
    for key,value in data_dict.items():
        if data_dict["NAMA LENGKAP "] == " ":
            break
        file.write(f"{key} : {value}\n")
    
    file.write("="*50+"\n")
    data_capture(link,page=page + 1)
datanya = data_capture(get_url)
