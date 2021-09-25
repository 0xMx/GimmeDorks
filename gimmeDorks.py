import requests as rq
from bs4 import BeautifulSoup as bsoup
import re, colorama
rd = colorama.Fore.LIGHTRED_EX
bg = colorama.Fore.LIGHTGREEN_EX
bl = colorama.Fore.LIGHTCYAN_EX
yl = colorama.Fore.LIGHTYELLOW_EX
rst = colorama.Style.RESET_ALL


banner = f"""


{rd}  ░██████╗░██╗███╗░░░███╗███╗░░░███╗███████╗██████╗░░█████╗░██████╗░██╗░░██╗░██████╗{rst}
{yl}  ██╔════╝░██║████╗░████║████╗░████║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝{rst}
{bl}  ██║░░██╗░██║██╔████╔██║██╔████╔██║█████╗░░██║░░██║██║░░██║██████╔╝█████═╝░╚█████╗░{rst}
{rd}  ██║░░╚██╗██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██║░░██║██║░░██║██╔══██╗██╔═██╗░░╚═══██╗{rst}
{yl}  ╚██████╔╝██║██║░╚═╝░██║██║░╚═╝░██║███████╗██████╔╝╚█████╔╝██║░░██║██║░╚██╗██████╔╝{rst}
{bl}  ░╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░{rst}
                                                    
    {bl}|   Meshari Almalki |{rst} 
    {bl}|   Twitter:slv0d   |{rst}
    {bl}|   0xSaudi         |{rst}

"""
print(banner)
def ghdb():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.exploit-db.com/google-hacking-database", "X-Requested-With": "XMLHttpRequest", "Connection": "close"}
    keyword = input(f"{yl}Enter Keyword to search example [SQL] : {rst}")
    numPage = input(f"{yl}Num of page : {rst}")
    for page in range(1,int(numPage)):
        page = (page * 15) - 14
        url = f"https://www.exploit-db.com:443/google-hacking-database?draw=22&columns%5B0%5D%5Bdata%5D=date&columns%5B0%5D%5Bname%5D=date&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=url_title&columns%5B1%5D%5Bname%5D=url_title&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=cat_id&columns%5B2%5D%5Bname%5D=cat_id&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=author_id&columns%5B3%5D%5Bname%5D=author_id&columns%5B3%5D%5Bsearchable%5D=false&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start={page}&length=15&search%5Bvalue%5D={str(keyword)}&search%5Bregex%5D=false&author=&category=&_=1617977705714"
        sender = rq.get(url, headers=headers)
        recordsFiltered = sender.json()['recordsFiltered']
        if  recordsFiltered > page:
            sizeOfSender = len(sender.json()['data'])
            for x in range(sizeOfSender):
                dorks = sender.json()['data'][x]['url_title']
                stripTag = re.sub("<.*?>",' ',dorks)
                print(f"{bg}{stripTag}{rst}")
        else:
            break
ghdb()