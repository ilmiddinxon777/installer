import requests
import json
def instadownloader(link):

    url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post_v2.php"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "2ac59c3d4amsh4c3e52af68e3696p1e6d36jsn676c78fecbb9",
        "X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    if 'error' in rest:
        return 'Bad'
    else:

        dict = {rest}
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Image':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'






