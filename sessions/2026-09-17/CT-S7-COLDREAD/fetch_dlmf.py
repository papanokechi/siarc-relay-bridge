from urllib.request import Request, urlopen
urls = ['https://dlmf.nist.gov/5.11.E12.tex', 'https://dlmf.nist.gov/5.11.E13.tex']
for url in urls:
    print('URL:', url)
    req = Request(url, headers={'User-Agent':'Mozilla/5.0 cold-review CT-S7-COLDREAD'})
    with urlopen(req, timeout=30) as r:
        print(r.read().decode('utf-8').strip())
        print()
