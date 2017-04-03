import requests
from bs4 import BeautifulSoup
import urlparse
from app import app
from flask import render_template, request, redirect, url_for, Flask, jsonify

url = "https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/dp/B00X4WHP5E/ref=redir_mobile_desktop?_encoding=UTF8&ref_=ods_gw_ha_d_black"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

# This will look for a meta tag with the og:image property
og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
if og_image and og_image['content']:
    print og_image['content']
    print ''

# This will look for a link tag with a rel attribute set to 'image_src'
thumbnail_spec = soup.find('link', rel='image_src')
if thumbnail_spec and thumbnail_spec['href']:
    print thumbnail_spec['href']
    print ''


@app.route('/images/', methods=['GET', 'POST'])
def image_view():
    imageList = []
    
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
        if "sprite" not in img["src"]:
            results= image % urlparse.urljoin(url, img["src"])
            imageList.append(results)
            if request.headers['Content-Type']=='application/json' or request.method == 'POST':
                return jsonify(imageList)
        return render_template('images.html', imageList=imageList)
