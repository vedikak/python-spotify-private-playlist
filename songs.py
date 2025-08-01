# from bs4 import BeautifulSoup
# import requests
# SONG_URL = "https://www.billboard.com/charts/hot-100/"


class Songs:
    def __init__(self):
        pass

    def scrap_songs(self):
        user_ip = ["gunshy- Southall, with you i am- cody johnson, forever and ever, amen- randy travis, last goodbye(radiowv session- tanner usrey, she's got it all- kenny chesney, brand new man- brooks & dunn, straight and narrow- sam barber, ghost town- sam barber, sold- john michael montgomery, what was i thinkin- diesels bentley , boondocks- little big town , pretty things- kat hasty , worst way- riley green , missed call- treaty oak revival, fishin in the dark- nitty gritty, parachute- chris stapleton , blue clear sky- george strait, just comes natural- george strait , burn burn burn- zach bryan, something to talk about- koe wetzel , humble and kind- tim mcgraw, heaven- jason aldean, 23- chayce bekham, motorcycle drive by- zach bryan, coal- dylan gossett, , hick town- jason aldean, highways- cory kent, i hope she's drinkin tonight- riley green, charleston girl- tyler childers, hurtin- cody johnson, deadman's curve- tyler childers, all american girl- carrie underwood, chattahoochee- alan jackson, shake the frost- tyler childers, travelin soldier- the chicks, little bitty- alan jackson, stone- whiskey myers, tornado- little big town, better man- little big town, ain't nothin bout you- brooks & dunn , would you go with me- josh turner, this damn song- pecos & the rooftops , loud and heavy- cody jinks, good directions- billy currington, three wooden crosses- randy travis, missing you- flatland calvary"]
        big_string = user_ip[0]
        # Split the string on commas and strip whitespace
        user_ip = [item.split('-')[0].strip() for item in big_string.split(",")]
        singer = [item.split('-')[-1].strip() for item in big_string.split(",")]
        return {'title_text_list':user_ip, 'singer':singer}
    
# response = requests.get(f"{SONG_URL}{user_ip}")        
# title_text_list = []
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_songs = soup.select(selector="li ul li h3")
        # for t in user_ip:
        #     title_text_list.append(t.get_text().strip())        
# user_ip = ["gunshy- Southall, with you i am- cody johnson, forever and ever, amen- randy travis, last goodbye(radiowv session- tanner usrey, she's got it all- kenny chesney, brand new man- brooks & dunn, straight and narrow- sam barber, ghost town- sam barber, sold- john michael montgomery, what was i thinkin- diesels bentley , boondocks- little big town , pretty things- kat hasty , worst way- riley green , missed call- treaty oak revival, fishin in the dark- nitty gritty, parachute- chris stapleton , blue clear sky- george strait, just comes natural- george strait , burn burn burn- zach bryan, something to talk about- koe wetzel , humble and kind- tim mcgraw, heaven- jason aldean, 23- chayce bekham, motorcycle drive by- zach bryan, coal- dylan gossett, , hick town- jason aldean, highways- cory kent, i hope she's drinkin tonight- riley green, charleston girl- tyler childers, hurtin- cody johnson, deadman's curve- tyler childers, all american girl- carrie underwood, chattahoochee- alan jackson, shake the frost- tyler childers, travelin soldier- the chicks, little bitty- alan jackson, stone- whiskey myers, tornado- little big town, better man- little big town, ain't nothin bout you- brooks & dunn , would you go with me- josh turner, this damn song- pecos & the rooftops , loud and heavy- cody jinks, good directions- billy currington, three wooden crosses- randy travis, missing you- flatland calvary"]
# big_string = user_ip[0]
# # Split the string on commas and strip whitespace
# user_ip = [item.split('-')[0].strip() for item in big_string.split(",")]
# singer = [item.split('-')[-1].strip() for item in big_string.split(",")]
# print(user_ip[0])