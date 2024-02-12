from bs4 import BeautifulSoup as bs
import pandas as pd

# html_file name
INFILE = 'vive_attendees.html'

# csv file name
OUTFILE = 'vive_companies.csv'


def main(html_file=INFILE, csv_file=OUTFILE):
	# open the html_file
	with open(html_file, 'r', encoding='utf8') as infile:
		# make a soup
		soup = bs(infile.read(), 'html.parser')

	# get all company tags
	company_tags = soup.find_all("span", class_="clamp__Clamp-ui__sc-1aq2rfp-0 list__Organization-cmp__sc-10fr9dg-10 hAEPUd gFtQuZ")

	# getting the contents of a company string
	# print(company_tags[0])
	# print(company_tags[0].contents[0].strip())

	# export company text to list
	companies = [tag.contents[0].strip() for tag in company_tags]

	# unique the list
	companies = list(set(companies))

	print(f"Found {len(companies)} companies.")

	# make dataframe
	df = pd.DataFrame({"companies": companies})

	# export list to excel
	df.to_csv(csv_file, index=False)

	return


if __name__ == '__main__':
	main()