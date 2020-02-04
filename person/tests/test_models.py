from django.test import TestCase
from person.models import Offices, User
# Поместите ваш код тестов здесь


class OfficesTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Offices.objects.create(name='Ленина', short_code='ЛН', phone='654000', start_time='9:00', end_time='23:00', start_out='17:00')
    '''
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass '''

    def test_first_name_label(self):
        office = Offices.objects.get(id=1)
        field_label = office._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Наименование мастерской')

    def test_work_time_out(self):
        office = Offices.objects.get(id=1)
        self.assertEquals(office.clock_work, '9:00 - 23:00')


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(email='wwer@mail.ru', first_name='Иван',middle_name='Иванович', last_name='Иванов', phone='9041922350')
        User.objects.create(email='petrov@mail.ru', first_name='Иван', middle_name='Иванович', last_name='Петров', phone='89650962750')
        User.objects.create(email='sidorov@mail.ru', first_name='Иван', middle_name='Иванович', last_name='Сидоров', phone='123456')

    def test_phone_number(self):
        for n in list(range(1, 4)):
            tst_user = User.objects.get(id=n)
            self.assertEquals(len(tst_user.phone), 12)

    def test_full_name(self):
        tst_user = User.objects.get(id=1)
        self.assertEquals(tst_user.get_full_name(), 'Иванов Иван Иванович')

    def test_short_name(self):
        tst_user = User.objects.get(id=1)