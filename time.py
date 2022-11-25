import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/getTimeStories', methods = ['GET'])
def function():
    url = 'https://time.com/'
    html_text = requests.get(url).text #get html code of whole url in string form
    soup = BeautifulSoup(html_text, 'html.parser') #parsing html text in soup
    
    result = []
    ind = 0

    for i in soup.find_all(class_ = "latest-stories__item-headline"):   #go through all elements whose class contain
                                                                        # this latest-stories__item-headlines
        result.append([i.string])  #text of that element is appended in result
    for j in soup.select(".latest-stories__item > a"):     #iterating over those elements whose class 
                                                            #latest-stories_item-headlines containing "a" tags
        
        result[ind].append('https://time.com/' + j.get('href'))    #to get the link of that element using href 
        ind += 1
    ans = []
    for i in result:
        ans.append({'title':i[0], 'link':i[1]})
    return jsonify(ans)

if __name__ == '__main__':
    app.run(debug=True, port=8000)