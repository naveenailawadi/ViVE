from bs4 import BeautifulSoup as bs
from constants import INFILE
from ViVE import ViVECompany, load_file

OUTFILE = 'attendees.csv'

# main function
def main(html_file=INFILE, csv_file=OUTFILE):
	# load the file
	soup = load_file(html_file)

	# get all the companies
	company_blocks = soup.find_all('div', class_="list__Content-cmp__sc-10fr9dg-3 bNggrU")

	# make all the companies
	companies = [ViVECompany(block) for block in company_blocks]

	# generate all the company objects
	objects = [company.info for company in companies]

	# export to excel
	df = pd.DataFrame(objects)
	df.to_csv(csv_file, index=False)
