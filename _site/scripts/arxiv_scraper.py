import requests
from bs4 import BeautifulSoup
import yaml
import sys

url = 'https://arxiv.org/search/cond-mat?query=Lal%2C+Siddhartha&searchtype=author&abstracts=hide&order=-submitted_date&size=200'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
output_file = sys.argv[1]
pub_data = []
for result in soup.findAll('li', attrs={'class': 'arxiv-result'}):
    pub_data.append({})
    pub_data[-1]['title'] = result.findChild('p', attrs={'class': 'title is-5 mathjax'}).text.strip()
    pub_data[-1]['authors'] = [tag.text.strip() for tag in result.findChild('p', attrs={'class': 'authors'}).findChildren('a')]
    pub_data[-1]['authors'] = [(author if author not in ['S. Lal', 'Siddharth Lal'] else 'Siddhartha Lal') for author in pub_data[-1]['authors']]
    pub_data[-1]['submit_date'] = result.findChild('span', string='Submitted').next_sibling.strip().replace(';','')
    try:
        pub_data[-1]['journal_ref'] = result.findChild('span', string='Journal ref:').next_sibling.strip()
        if ') and ' in pub_data[-1]['journal_ref']:
            pub_data[-1]['journal_ref'] = pub_data[-1]['journal_ref'].split(' and ')[0]
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref']
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'][:pub_data[-1]['journal_ref_short'].rindex('(')-1] + pub_data[-1]['journal_ref_short'][pub_data[-1]['journal_ref_short'].rindex(')')+1:]
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'].replace('Physical Review ', 'PR')
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'].replace('Phys. Rev. ', 'PR')
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'].replace('J. Phys.: Condens. Matter', 'JPCM.')
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'].replace('Nature Physics', 'Nat. Phys.')
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'].replace('Journal of High Energy Physics', 'JHEP')
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'].replace('Nuclear Physics B', 'Nuc. Phys. B')
        pub_data[-1]['journal_ref_short'] = pub_data[-1]['journal_ref_short'].replace('Europhysics Letters', 'Europhys.Lett.')
        pub_data[-1]['doi'] = result.findChild('span', string='doi').find_next('a')['href']
    except:
         pass
    pub_data[-1]['tags'] = [tag.text for tag in result.findChild('div', attrs={'class': 'tags is-inline-block'}).findChildren('span')]
    pub_data[-1]['arxiv_ref'] = result.find('p', attrs={'class': 'list-title is-inline-block'}).findChild('a').text.strip()
    pub_data[-1]['permalink'] = "/" + pub_data[-1]['arxiv_ref'].replace("arXiv:","") + "/"
    pub_data[-1]['arxiv_doi'] = result.find('p', attrs={'class': 'list-title is-inline-block'}).findChild('a')['href']
yaml.dump(pub_data, open(output_file, 'w'), width=float("inf"))
