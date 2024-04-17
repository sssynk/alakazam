import requests
from alakazam.core.threadpool import ThreadPool
from tqdm import tqdm

global count_working
count_working = 0

def test_proxy(proxy):
    global count_working
    proxies = {
        'http': proxy,
        'https': proxy
    }

    try:
        response = requests.get('https://api.join.pokemon.com/', proxies=proxies, timeout=5)
        if 'Missing Authentication Token' in response.text:
            count_working += 1
            return True
        else:
            return False
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
