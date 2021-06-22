# plaformproject
此為實作交通部觀光局整理之台灣景點觀光資料庫查詢系統，利用政府的資料開放平台(https://data.gov.tw/dataset/7777)
，找出台灣的景點和觀光資料庫，並抓取其API(https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json)。
抓取後將資料分類和視覺化，能夠更方便的看出景點位於台灣的哪個位置並能夠快速了解景點資訊。

Build process & Introduction:  
-
本project的使用urllib.request來抓取API網址, folium為視覺化的工具(地圖和地圖標示), json來處理API的資料。

此project的運作方式為: 

1.執行後輸入想查詢景點之名稱, 不一定需要完整的名稱, EX:打入"橋", 資料庫中關於"橋"的資料都會輸出。 

2.輸出的資料為: 景點名稱, 景點住址, 景點開放時間, 電話, 路線規劃, 景點介紹。 

3.而在同個目的地會生成html檔, 其中會出現剛剛查詢的資料在台灣的位置, 並用icon標記, 而鼠標移到icon會有景點的名稱。 

4.結束此系統只需輸入"exit"即可退出。

Details of the approach:
-
一開始使用json.load()抓取API上的data，接著找出需要用到的data格放入alist。有所需的data格後處理就相對簡單，先輸入input, 如果input有在data中就排版輸出此data的相關資料。而相關資料中, 用placex_list和placey_list去儲存景點的經度和緯度，接著zip將經緯度合在一起放入placename_list，而為了能夠在地圖的marker中也顯示景點名稱, 順便將名字也存入placename_list中。以上也將地圖所需的資料都準備好，接著將地圖視覺化。

此project的視覺化是使用html的方式呈現，借助folium, 一開始default出整個台灣地圖。接著將剛剛place_list的資料, 在生成的map上做記號。 其中ablocation[0], [1]是景點絕對位置, ablocation[2]為名稱，用folium的add.child將所有資料都標示，最後save map, 輸出標示地圖。

Result:
-
所有景觀的資料, 包括: 景點名稱, 景點住址, 景點開放時間, 電話, 路線規劃, 景點介紹。

map1.html: 景點在台灣地圖的各個位置。


References:
-
1. 政府的資料開放平台: (https://data.gov.tw/dataset/7777)
2. API: (https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json)
3. Folium: https://python-visualization.github.io/folium/index.html
