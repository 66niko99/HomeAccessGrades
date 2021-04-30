import requests
from bs4 import BeautifulSoup


class grades:
    def __init__(self, username, password, hac_base_link):
        self.username = username
        self.password = password
        self.hac_base_link = hac_base_link
        self.s = requests.session()
        self.logged_in = False

    def fetch_grades(self):
        classes = []

        login_html = self.login()
        login_soup = BeautifulSoup(login_html, 'html.parser')

        table_body = login_soup.find('tbody')

        class_names = table_body.find_all('a', {'id': 'courseName'})
        teacher_names = table_body.find_all('a', {'id': 'staffName'})
        class_grades = table_body.find_all('a', {'id': 'average'})


        for c_name, t_name, c_grade in zip(class_names, teacher_names, class_grades):

            class_data = {'class name': c_name.text, 'grade': c_grade.text, 'teacher': {'name': t_name.text.replace('\r\n', '').strip('  '), 'email': t_name['href']}}
            classes.append(class_data)

        return classes


    def login(self):

        s = self.s
        get_login = s.get(self.hac_base_link + '/HomeAccess/Account/LogOn')

        if self.logged_in:
            return get_login.text

        loginSoup = BeautifulSoup(get_login.content, 'html.parser')

        token = loginSoup.find('input', {'name': '__RequestVerificationToken'})['value']

        login_data = {
            '__RequestVerificationToken': token,
            'SCKTY00328510CustomEnabled': False,
            'SCKTY00436568CustomEnabled': False,
            'Database': '10',
            'VerificationOption': 'UsernamePassword',
            'LogOnDetails.UserName': self.username,
            'tempUN': '',
            'tempPW': '',
            'LogOnDetails.Password': self.password,
        }

        login = s.post(self.hac_base_link + '/HomeAccess/Account/LogOn',
                       data=login_data)

        self.logged_in = True
        return login.text



