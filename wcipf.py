import re
import requests
from sys import argv
import typer
import os
import art
from blessed import Terminal
from time import sleep

def main():
    try:
        t = Terminal()
        def cls():
            print(t.clear)
        logo = f"{art.text2art('wcipf')}\nby kotenok_1337\n"

        cls(); print(logo)
        print('Welcome!')
        sleep(2)
        cls()
        print(logo)
        try:
            if not int(argv[1]) > 2358:
                scanv = int(argv[1])
            else:
                print("ERROR: can't find more than 2358 IPs.")
                scanv = 100
        except:
            scanv = 100

        print(f'Finding {scanv} IPs...')
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        all_ips = []
        with typer.progressbar(range(round(scanv / 6))) as progress:
            for _ in progress:
                resp = requests.get(f"http://www.insecam.org/en/bytype/Axis/?page={_}", headers=headers)
                ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', resp.text)
                for __ in ips:
                    if not __ in all_ips:
                        all_ips.append(__)
        ips_str = ''
        for ___ in all_ips[0:scanv]:
            ips_str += ___ + '\n'
        if os.path.lexists('IPs.txt'):
            os.remove('IPs.txt')
        print(f'\nSaving to {os.path.dirname(os.path.abspath(__file__))}\IPs.txt ...')
        file = open('IPs.txt', 'a')
        file.write(ips_str)
        file.close()

        print(f'\n{t.green}Done! Thank you for using my script =){t.white}')
    except:
        cls()
        print(logo)
        print(f'{t.red}ERROR: something went wrong.{t.white}')

main()