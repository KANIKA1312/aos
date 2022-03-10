from faker import Faker

locale_list = ['en-US', 'en_CA']
fake = Faker(locale_list)

# --------------------------- DATA--------------------

app = 'Advantage Online Shopping'
web_url = 'https://advantageonlineshopping.com/#/'
web_title = '\xa0Advantage Shopping'

# Create New User Data

password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
username = f'{first_name}13a12'
email = f'{username}@{fake.free_email_domain()}'
phone_number = fake.phone_number()[:15]
country = fake.current_country()
city = fake.city()
address = fake.street_address()
postal_code = fake.postalcode()
contact_sub = 'Hi, When you guyz gonna introduce Boat Headphones?'

# --------------------------- DATA--------------------

# ----------------------------URL'S-------------------
speaker_url = 'https://advantageonlineshopping.com/#/category/Speakers/4'
tablet_url = 'https://advantageonlineshopping.com/#/category/Tablets/3'
laptop_url = 'https://advantageonlineshopping.com/#/category/Laptops/1'
mice_url = 'https://advantageonlineshopping.com/#/category/Mice/5'
headphone_url = 'https://advantageonlineshopping.com/#/category/Headphones/2'
see_offer_url = 'https://advantageonlineshopping.com/#/product/3'
explore_now_url = 'https://advantageonlineshopping.com/#/category/Tablets/3'
product_1 = 'https://advantageonlineshopping.com/#/product/16'
product_2 = 'https://advantageonlineshopping.com/#/product/10'
product_3 = 'https://advantageonlineshopping.com/#/product/21'
chat_url = 'https://advantageonlineshopping.com/chat.html'
fb_link = 'https://www.facebook.com/MicroFocus/'
twitter_link = 'https://twitter.com/MicroFocus'
linkedin_link = 'https://www.linkedin.com/company/micro-focus '
