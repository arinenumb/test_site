from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    '''Тест нового посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложных дел. Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о
        # списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

        # Ей сразу же прелагается ввести элемент списка

        # Она набирает в текстовом поле "Купить павлинья перья (ее хобби -
        # вязание рыболовных мушек)

        # Когда она нажимает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в каечтсве элемента списка

        # бла-бла-бла

        # Удовлетворенная она снова ложится спать


if __name__ == '__main__':
    unittest.main(warnings='ignore')




