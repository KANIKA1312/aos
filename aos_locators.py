from faker import Faker

locale_list = ['en-US', 'en_CA']
fake = Faker(locale_list)

# --------------------------- DATA--------------------

app = 'Advantage Online Shopping'
web_url = 'https://advantageonlineshopping.com/#/'
web_title = '\xa0Advantage Shopping'


#Create New User Data

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


# --------------------------- DATA--------------------