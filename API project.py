import urllib.request as request
from skimage import io
import folium
import json

src = "https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json"
with request.urlopen(src) as response:
    data = json.load(response)
alist = data["XML_Head"]["Infos"]["Info"]

while True:
    name = input("此為交通部觀光局整理之台灣景點觀光資料庫查詢系統, 請輸入查詢景點: ")
    if name == "exit":
        break
    placex_list = []
    placey_list = []
    placename_list = []
    for x in alist:
        if name in x["Name"]:
            placex_list.append(x["Px"])
            placey_list.append(x["Py"])
            placename_list.append(x["Name"])
            print("景點名稱: " + x["Name"] + "\n店家住址: " + x["Add"] + "\n開店時間: " + x["Opentime"] + "\n電話: " + x["Tel"] +
                "\n路線規劃: " + x["Travellinginfo"] + "\n介紹: " + x["Description"])
            print("\n\n")
    place_list = [i for i in zip(placex_list, placey_list, placename_list)]
    fmap = folium.Map(location=[23.5832, 120.5825], zoom_start=7)
    for ablocation in place_list:
        m = folium.Marker(location=[ablocation[1], ablocation[0]] ,tooltip=ablocation[2], icon=folium.Icon(color='red'))
        fmap.add_child(child=m)

    fmap.save('map1.html')
