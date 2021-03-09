import urllib.request

url = 'https://vaitechbd.com/index.html'
fhand = urllib.request.urlopen(url)
fh = open('index.html', 'w')

for line in fhand:
    data = line.decode().strip()
    fh.write(data)
fh.close()

print("Cloned the given website successfully!")