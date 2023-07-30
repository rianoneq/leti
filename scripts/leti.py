from data.models import SNILS
from data.models import CoursePositionData
from data.models import PersonCoursePositionsData

from requests_ import get_course_json


class LetiParser:
  def __init__(self, snils: SNILS) -> None:
    self.snils: SNILS = snils
    self.coursers_urls: list[str] = []
    self.client_data: PersonCoursePositionsData
    self.BASE_COURSE_URL: str = 'https://abit.etu.ru/ru/postupayushhim/bakalavriat-i-specialitet/spiski-podavshih-zayavlenie/spisok-postupayushhih?list='
    self.TECH_COURSES_DATA: dict[str, str] = {
      'Прикладная математика и информатика': {'id': '1-1-ee0043c0-88ce-4a0e-b3be-d46605fd8fd1',
                                              'amount': 87},
      'Информатика и вычислительная техника (Компьютерное моделирование и проектирование)': {'id': '1-1-c9484eea-449e-42aa-bda4-3111b180b1c0',
                                              'amount': 50},
      'Информатика и вычислительная техника (Искусственный интеллект)': {'id': '1-1-47992162-dc4c-419e-bc00-40d05d58f0ac',
                                              'amount': 100},
      'Информационные системы и технологии': {'id': '1-1-bfcbbd05-a810-4b32-a746-410cd7ba3a64',
                                              'amount': 100},
      'Программная инженерия': {'id': '1-1-a5d6e976-8db5-4c67-8fd7-0bc0059a2910',
                                              'amount': 55},
      'Компьютерная безопасность': {'id': '1-1-536585a4-59a9-4460-9fa1-6e2ca21c534a',
                                              'amount': 70},
      'Радиотехника (Интеллектуальные радиотехнические системы)': {'id': '1-1-301c0a38-64ed-4062-93f5-003a37800e72',
                                              'amount': 58},
      'Радиотехника (Системы компьютерного зрения)': {'id': '1-1-1f27e716-15a1-4153-8b69-d6345d7f05a7',
                                              'amount': 38},
      'Инфокоммуникационные технологии и системы связи': {'id': '1-1-6f0c88a1-afd8-44be-8b22-fa9fe526fac0',
                                              'amount': 69},
      'Конструирование и технология электронных средств': {'id': '1-1-dc2ec766-2c0b-4e20-84e3-4a4c08f07fe3',
                                              'amount': 50},
      'Электроника и наноэлектроника': {'id': '1-1-85edbc68-8acd-46d6-b03e-dd2450077835',
                                              'amount': 235},
      'Радиоэлектронные системы и комплексы': {'id': '1-1-f5a6ea21-107f-4291-bd09-2fcf67860314',
                                              'amount': 25},
      'Приборостроение (Информационно-измерительные системы и геоинформационные технологии)': {'id': '1-1-a0f0b54a-9703-4d14-9f4f-1bac56278aa3',
                                              'amount': 50},
      'Приборостроение (Лазерные, акустические и навигационные системы)': {'id': '1-1-9f65a6d7-5188-460a-9d34-c1ad35109f5d',
                                              'amount': 85},
      'Мехатроника и робототехника': {'id': '1-1-736d5b9e-e5a8-4a5c-9021-1b86b75f117b',
                                              'amount': 15},
      'Техносферная безопасность': {'id': '1-1-2dba0df2-e724-43ed-b067-51fc6c85fa30',
                                              'amount': 40},
      'Биотехнические системы и технологии': {'id': '1-1-56ac57a8-32e8-4986-9617-7dd0947e4c55',
                                              'amount': 60},
      'Управление в технических системах (Автоматика и робототехнические системы)': {'id': '1-1-67735f23-f65a-4b8e-89e1-62490c8988c5',
                                              'amount': 85},
      'Управление в технических системах (Компьютерные интеллектуальные технологии управления в технических системах)': {'id': '1-1-3933eead-073a-49a2-a35e-ac2f718e290a',
                                              'amount': 40},
      'Инноватика': {'id': '1-1-287d9dc0-eb3f-4211-b967-420253e10845',
                                              'amount': 14}
    }

  def _get_courses_urls(self) -> list[str]:

    coursers_urls: list[str] = []
    for course_name, course_data in self.TECH_COURSES_DATA.items():
      course_url: str = f'{self.BASE_COURSE_URL}{course_data["id"]}'
      coursers_urls.append(course_url)

    self.coursers_urls = coursers_urls

  def _get_competitors_snils(self, snils: SNILS) -> list[SNILS]:
    ...

  def _get_person_position_data(self, snils: SNILS, course_url: str) -> CoursePositionData:
    # course_data = get_course_json()
    ...

  def _get_all_person_data(self, snils: SNILS) -> PersonCoursePositionsData:
    ...

  def main(self) -> str:
    courses_urls: list[str] = self._get_courses_urls()



LetiParser('157-856-074 11').main()
