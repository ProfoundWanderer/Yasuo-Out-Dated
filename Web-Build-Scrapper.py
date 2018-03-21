from bs4 import BeautifulSoup
import requests



def banChamps():
    page = requests.get('http://na.op.gg/champion/statistics')  # gets the link and puts it into page
    # print(page.status_code) #A status_code of 200 means that the page downloaded successfully
    soup = BeautifulSoup(page.content, 'html.parser')  # parses the page and puts it into soup

    print("Champions in order from most to least banned:")
    ban = (soup.select('div.Content span.ChampionName')) # goes to the div called Content then the span called Champion name and selects it then puts it in ban
    for i, ban in enumerate(ban, 1): # enumerates ban starting at one
        print(i, ". ", ban.text, sep='') #prints i then ". " then ban but just the text and takes all the spaces out except the one I made
    print('\n')



def hardMatchUps():
    page = requests.get('http://www.matchup.gg/champion/Yasuo/')  # gets the link and puts it into page
    # print(page.status_code) #A status_code of 200 means that the page downloaded successfully
    soup = BeautifulSoup(page.content, 'html.parser')  # parses the page and puts it into soup

    beware = (soup.find_all('div', {'class': 'champion-lookup-item-info'})) # finds all the class in div then puts it into beware
    print("*Be very careful against these champions!*", end='') # gets rid of all the new lines that are automatically added
    print(beware[0].text[:-20], beware[1].text[:-20], beware[2].text[:-20], beware[3].text[:-19],
          beware[4].text[:-20], beware[5].text[:-19], beware[6].text[:-20], beware[7].text[:-20], beware[8].text[:-20], beware[9].text[:-20]) # finds the indexed item called in beware and prints just the text but deletes the last 20(or 21) letters
    print("\n")



def summary():
    page = requests.get('http://na.op.gg/champion/yasuo/statistics/top')  # gets the link and puts it into page
    # print(page.status_code) #A status_code of 200 means that the page downloaded successfully
    soup = BeautifulSoup(page.content, 'html.parser')  # parses the page and puts it into soup

    table = soup.find('table', {'class': 'ChampionStatsSummaryTable'})  # finds the class 'ChampionStatsSummaryTable' from the table and puts it into table
    tr = table.find_all('tr', {'class': 'Row First'})  # it finds all the tr from table then get the ones with class='Row First' and puts it in tr

    print("-Skill: Max R -> E -> Q -> W")
    print("-Summoner Spells: Up to you but Flash & Teleport/Exhaust are recommended")
    print("-Starting Items: Doran's Blade or Shield(depending on the match up) and a pot\n")

    print("-Core build order based on na.op.gg (can build Frozen Mallet 2nd or 3rd if needed):")
    for img in tr[3].find_all('img', alt=True):  # finds all the images with alt text in tr[3] and puts it in img
        print('', img['alt'])  # prints the alt text of the img after a blank space

    print("\n-Best masteries choice(based on na.op.gg):")
    for img in tr[5].find_all('img', alt=True):
        print('', img['alt'])  # This will just print the Keystone

    a = (soup.find_all('div', {'class': 'Summary'}))
    print(' ', a[0].text[4:-3]) # the [4:-3] is more formating and getting rid of blank space like I did in HardMatchUps()
    print(' ', a[1].text[4:-3])
    print(' ', a[2].text[4:-3])

    print("\n-Best rune choice:")
    label = (soup.find_all('div', {'class': 'Label'}))  # finds all the divs inside of soup with the class label and puts them into label
    value = (soup.find_all('div', {'class': 'Value'}))
    print('', label[2].text, value[2].text)  # after a blank space it prints the text of the 7th label then the text of the 7th value
    print('', label[3].text, value[3].text)
    print('', label[4].text, value[4].text)
    print('', label[5].text, value[5].text)



def main():
    banChamps()
    hardMatchUps()
    summary()

main()



