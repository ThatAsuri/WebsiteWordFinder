import requests
from bs4 import BeautifulSoup
import re
counter = dict()
urls = []

main_url = input("Give me URL in this format - https://example.com: ")

mean_words_list = []

try:
    file = open("meanwords.txt")
except:
    print("There was an error with file meanwords.txt, make sure the file exists and is filled with words line by line.")
    quit()
for line in file.readlines():
    mean_words_list.append(line.strip())
file.close()

link = requests.get(main_url)
  
all_links = BeautifulSoup(link.text, "html.parser")

for word in mean_words_list:
    if word in link.text:
        if word in counter:
            counter[word] = counter[word] +1 
        else:
            counter[word] = 1

for httpys in all_links.find_all("a", attrs={"href": re.compile("^http")}):
    print("Detected URL:" + httpys.get("href"))
    urls.append(httpys.get("href"))
    
for url in urls:
    link_2 = requests.get(url)
    link_2_text = link_2.text
    for word in mean_words_list:
        if word in link_2_text:
            if word in counter:
                counter[word] = counter[word] +1 
            else:
                counter[word] = 1
            print("New word found in: " + url + " the word is: " + word)
            print(str(counter) + "\n")    
print("Checking finished !!")







