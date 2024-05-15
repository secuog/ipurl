import requests
import re
from optparse import OptionParser


def main(param):
    # parser = OptionParser("ip查url")
    # parser.add_option('-i',type='string',dest='IP',help='目标ip')
    # options,args = parser.parse_args()
    url = "https://site.ip138.com/"+param  # + options.IP #拼接url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    res = requests.get(url, headers=headers)  # 发送get请求
    pattern1 = r'^<li><span class="date">.*</li>'
    pattern = r'<span class="date">(.*?)</span><a href="(.*?)"'
    matches = re.findall(pattern, res.text, re.MULTILINE)
    for item in matches:
        date = item[0]
        url = item[1]
        print(date, url)
if __name__ == "__main__":
    user_input = input("输入ip")
    main(user_input)
