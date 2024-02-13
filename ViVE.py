from bs4 import BeautifulSoup as bs


# class for the company
class ViVECompany:
	# company tag
	company_tag = None

	def __init__(self, new_company_tag):
		# store the tag
		self.company_tag = new_company_tag

	# function to get an attribute from a span tag class
	def get_attribute(self, tag_class):
		attribute = self.company_tag.find("span", class_=tag_class)

		if attribute:
			return attribute.contents[0].strip()
		else:
			return 'N/A'

	# get the company name
	@property	
	def company(self):
		return self.get_attribute("clamp__Clamp-ui__sc-1aq2rfp-0 list__Organization-cmp__sc-10fr9dg-10 hAEPUd gFtQuZ")

	# get the attendee
	@property
	def attendee_name(self):
		return self.get_attribute("clamp__Clamp-ui__sc-1aq2rfp-0 list__FullName-cmp__sc-10fr9dg-7 hAEPUd jeYRiH")

	# get the attendee title
	@property
	def attendee_title(self):
		return self.get_attribute("clamp__Clamp-ui__sc-1aq2rfp-0 list__Job-cmp__sc-10fr9dg-9 hAEPUd hgzTsV")

	# get the full information in a dictionary
	@property
	def info(self):
		information_dir = {
			'company': self.company,
			'attendee_name': self.attendee_name,
			'attendee_title': self.attendee_title
		}

		return information_dir


# load file function
def load_file(html_file):
	with open(html_file, 'r', encoding='utf8') as infile:
		# make a soup
		soup = bs(infile.read(), 'html.parser')

	return soup