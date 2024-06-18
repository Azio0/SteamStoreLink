import requests
from bs4 import BeautifulSoup

steamURL = "https://store.steampowered.com/app/"


def get_appid(steam_name=None):
  if steam_name is None:
    return "[SteamStore] No name provided"

  try:
    page = requests.get(
        f"https://store.steampowered.com/search/?term={steam_name}")
    soup = BeautifulSoup(page.content, "html.parser")

    appid_element = soup.select_one('a[data-ds-appid]')
    appid = appid_element.get('data-ds-appid') if appid_element else None

    return appid

  except Exception as error:
    return error


def get_price(steam_link=None):
  if steam_link is None:
    return "[SteamStore] No link provided"

  try:
    link = f"{steamURL}/{steam_link}"
    page = requests.get(link)

    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="appHubAppName_responsive")
    title = title.get_text().replace('\r\n\t\t\t\t\t\t\t$',
                                     '').replace('\t\t\t\t\t\t', '')

    container = soup.find(class_="game_purchase_action")
    price_div = container.find("div", class_="game_purchase_price price")

    price = price_div.get_text().replace('\r\n\t\t\t\t\t\t\t',
                                         '').replace('\t\t\t\t\t\t', '')

    return link, title, price

  except Exception as error:
    return error


# on import
print('[SteamStore] loaded')
