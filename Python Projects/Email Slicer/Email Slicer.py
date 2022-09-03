"""
    Email Slicer
    Returning username and the domain of the email id after user input.
"""


def email_slicer():
    print('Welcome to email slicer\n')

    email_input = input('Enter your email address: ')

    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)


email_slicer()