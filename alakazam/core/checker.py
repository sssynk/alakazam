import requests
from alakazam.core.threadpool import ThreadPool
from tqdm import tqdm

global count_working
count_working = 0

def test_proxy(proxy):
    global count_working
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        response = requests.get('https://join.pokemon.com/', proxies=proxies, timeout=5)
        if 'edet=16' in response.text:
            return False
        else:
            count_working += 1
            return True
    except:
        return False

def _test_proxy_and_save(proxy, outfile):
    if test_proxy(proxy):
        with open(outfile, 'a') as out:
            out.write(proxy + '\n')

def test_proxy_file(file, outfile):
    pool = ThreadPool(300)
    with open(file, 'r') as f:
        proxies = f.readlines()
        for proxy in tqdm(proxies, desc="Testing Proxies"):
            proxy = proxy.strip()
            pool.add_task(_test_proxy_and_save, proxy, outfile)

        pool.wait_completion()
        return count_working, len(proxies), outfile
