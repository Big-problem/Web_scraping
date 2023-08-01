import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    URL = 'http://web.cba.neu.edu/~msolomon/r101.htm'
    page = requests.get(URL)
    print('Done getting')

    soup = BeautifulSoup(page.content, 'html.parser')

    # 可以直接抓tag裡的tag
    results = soup.select('center b tt font')

    task = 101
    index = 103
    file_path = 'R'+str(task)+'.txt'

    with open(file_path, 'w') as f:
        print(task)
        for result in results[2:index]:
            tmp = ';'.join(result.text.split())
            f.write(tmp+'\n')
        print(tmp)

    task += 1
    index += 1
    file_path = 'R'+str(task)+'.txt'
    for i in range(11):
        with open(file_path, 'w') as f:
            print(task)
            for result in results[index:index+101]:
                tmp = ';'.join(result.text.split())
                f.write(tmp+'\n')
            print(tmp)
        task += 1
        index += 102
        file_path = 'R'+str(task)+'.txt'

    print('Done')
