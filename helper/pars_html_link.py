from bs4 import BeautifulSoup


def get_html_links(src):
    with open(file=src, mode='r', encoding='utf-8') as file:
        source = file.read()
    
        soup = BeautifulSoup(source, 'lxml')
        
        return [link.get('href') for link in soup.find_all('a')]
