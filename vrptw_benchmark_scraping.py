import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

if __name__ == '__main__':
    URL = 'http://web.cba.neu.edu/~msolomon/r101.htm'
    ua = UserAgent()
    user = ua.random

    page = requests.get(URL, headers={'user-agent': user})
    print('Done getting')

    soup = BeautifulSoup(page.content, 'html.parser')

    # 透過tag和css property抓資料
    results = soup.select('font[color="#3366FF"]')

    task = 101
    file_path = 'R'+str(task)+'.txt'  # 設定檔名
    index = 1

    for i in range(12):
        with open(file_path, 'w') as f:
            print(task)
            for result in results[index:index+101]:
                tmp = ';'.join(result.text.split())
                f.write(tmp+'\n')
            print(tmp)
        task += 1
        file_path = 'R'+str(task)+'.txt'
        index += 101
