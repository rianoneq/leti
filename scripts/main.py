from data.models import SNILS
from data.models import CoursePositionData
from data.models import PersonCoursePositionsData

from typing import Union

from .requests_ import get_course_json

class GetCompetitors:
  def __init__(self, search_option: Union[str, int], course_url: str) -> None:
    self.search_option: Union[SNILS, int] = self._serialize_search_option(search_option)

  def _serialize_search_option(self, search_option: Union[str, int]) -> Union[SNILS, int]:
    if isinstance(search_option, str):
      return SNILS(search_option)
    if isinstance(search_option, int):
      return search_option

  def _get_courses_urls(self) -> list[str]:

    coursers_urls: list[str] = []
    for course_name, course_data in self.TECH_COURSES_DATA.items():
      course_url: str = f'{self.BASE_COURSE_URL}{course_data["id"]}'
      coursers_urls.append(course_url)

    return coursers_urls

  def _get_course_by_url(self, course_url: str) -> dict:
    course_id: str = course_url.split('/')[-1]
    for course_name, course_data in self.TECH_COURSES_DATA.items(): 
      if course_data['id'] == course_id:
        return {'name': course_name,
                'id': course_data['id'],
                'amount': course_data['amount']}

  def _get_course_data(self, course_url: str) -> list[dict]:
    course_data: list[dict] = get_course_json(course_url)
    course_data_originals: list[dict] = self._serialize_course_data(course_data)
    return course_data_originals

  def _serialize_course_data(self, course_data: list[dict]) -> list[dict]:
    return [i for i in course_data if i['has_original']]

  def _get_lowest_position(self, search_option: Union[SNILS, int], course_data: list[dict]) -> int:
    
    for person in course_data:
      if isinstance(search_option, SNILS) and person['code'] == search_option.value:
        return course_data.index(person) + 1
      if isinstance(search_option, int) and person['total_points'] < search_option:
        return course_data.index(person) + 1

  def _get_competitors_snilses(self, 
                               course_data: list[dict], 
                               lowest_postion: int) -> list[SNILS]:
    return [SNILS(i['code']) for i in course_data[:lowest_postion - 1]]

  def _get_competitors_data(self, snils: SNILS) -> PersonCoursePositionsData:
    ...

  def main(self) -> str:
    course_data: list[dict] = self._get_course_data(self.coursers_urls[3]) # for example
    lowest_position: Union[None, int] = self._get_lowest_position(self.search_option, course_data=course_data)
    competitors_snilses: list[SNILS] = self._get_competitors_snilses(course_data=course_data,
                                                                     lowest_postion=lowest_position)

    return competitors_snilses

class General:
  def __init__(self, snils) -> None:
    self.client_data: PersonCoursePositionsData
    self.BASE_COURSE_URL: str = 'https://lists.priem.etu.ru/public/list/'
    self.competitors_data = {}
    self.TECH_COURSES_DATA: dict[str, str] = {
      'ee0043c0-88ce-4a0e-b3be-d46605fd8fd1': {'name': 'Прикладная математика и информатика',
                                              'amount': 77},
      'c9484eea-449e-42aa-bda4-3111b180b1c0': {'name': 'Информатика и вычислительная техника (Компьютерное моделирование и проектирование)',
                                              'amount': 43},
      '47992162-dc4c-419e-bc00-40d05d58f0ac': {'name': 'Информатика и вычислительная техника (Искусственный интеллект)',
                                              'amount': 85},
      'bfcbbd05-a810-4b32-a746-410cd7ba3a64': {'name': 'Информационные системы и технологии',
                                              'amount': 76},
      'a5d6e976-8db5-4c67-8fd7-0bc0059a2910': {'name': 'Программная инженерия',
                                              'amount': 45},
      '536585a4-59a9-4460-9fa1-6e2ca21c534a': {'name': 'Компьютерная безопасность',
                                              'amount': 58},
      '301c0a38-64ed-4062-93f5-003a37800e72': {'name': 'Радиотехника (Интеллектуальные радиотехнические системы)',
                                              'amount': 49},
      '1f27e716-15a1-4153-8b69-d6345d7f05a7': {'name': 'Радиотехника (Системы компьютерного зрения)',
                                              'amount': 36},
      '6f0c88a1-afd8-44be-8b22-fa9fe526fac0': {'name': 'Инфокоммуникационные технологии и системы связи',
                                              'amount': 68},
      'dc2ec766-2c0b-4e20-84e3-4a4c08f07fe3': {'name': 'Конструирование и технология электронных средств',
                                              'amount': 42},
      '85edbc68-8acd-46d6-b03e-dd2450077835': {'name': 'Электроника и наноэлектроника',
                                              'amount': 224},
      'f5a6ea21-107f-4291-bd09-2fcf67860314': {'name': 'Радиоэлектронные системы и комплексы',
                                              'amount': 16},
      'a0f0b54a-9703-4d14-9f4f-1bac56278aa3': {'name': 'Приборостроение (Информационно-измерительные системы и геоинформационные технологии)',
                                              'amount': 42},
      '9f65a6d7-5188-460a-9d34-c1ad35109f5d': {'name': 'Приборостроение (Лазерные, акустические и навигационные системы)',
                                              'amount': 76},
      '736d5b9e-e5a8-4a5c-9021-1b86b75f117b': {'name': 'Мехатроника и робототехника',
                                              'amount': 15},
      '2dba0df2-e724-43ed-b067-51fc6c85fa30': {'name': 'Техносферная безопасность',
                                              'amount': 40},
      '56ac57a8-32e8-4986-9617-7dd0947e4c55': {'name': 'Биотехнические системы и технологии',
                                              'amount': 54},
      '67735f23-f65a-4b8e-89e1-62490c8988c5': {'name': 'Управление в технических системах (Автоматика и робототехнические системы)',
                                              'amount': 79},
      '3933eead-073a-49a2-a35e-ac2f718e290a': {'name': 'Управление в технических системах (Компьютерные интеллектуальные технологии управления в технических системах)',
                                              'amount': 38},
      '287d9dc0-eb3f-4211-b967-420253e10845': {'name': 'Инноватика',
                                              'amount': 12},
      '5c53ebd9-f2c0-4698-a74d-7140cfeaf718': {'name': 'Электроэнергетика и электротехника',
                                              'amount': 117},
      'cdb7b189-30f2-4312-bdb7-027a354dce80': {'name': 'Управление качеством',
                                              'amount': 21},
      '65cd1ba5-6d88-4b67-90dd-6946377686ee': {'name': 'Системный анализ и управление',
                                              'amount': 17},
      '52700a93-9eff-4f15-9357-8c6368c52461': {'name': 'Нанотехнологии и микросистемная техника',
                                              'amount': 59},
      '2c47e022-a76b-4ce2-b201-3cc9b66c32c2': {'name': 'Реклама и связи с общественностью',
                                              'amount': 0},
      'de223201-ccc9-4e99-a71f-4f4889e113f6': {'name': 'Лингвистика',
                                              'amount': 0},
    }
    self.coursers_urls: list[str] = self._get_courses_urls()
    self.DATA: list[dict] = []
  
  def _get_course_by_url(self, course_url: str) -> dict:
    course_id: str = course_url.split('/')[-1]
    return {'id': course_id, **self.TECH_COURSES_DATA[course_id]}

  def _serialize_course_data(self, course_data: list[dict], course_base_data) -> list[dict]:
    return [{'code': i['code'], 
             'points': i['total_points'], 
             'priority': i['priority'],
             'course_id': course_base_data['id'],
             'course_amount': course_base_data['amount']} for i in course_data if i['has_original']]

  def _get_courses_urls(self) -> list[str]:

    coursers_urls: list[str] = []
    for course_name, course_data in self.TECH_COURSES_DATA.items():
      course_url: str = f'{self.BASE_COURSE_URL}{course_name}'
      coursers_urls.append(course_url)

    return coursers_urls
  
  def _get_course_data(self, course_url: str) -> list[dict]:
    course_data: list[dict] = get_course_json(course_url)
    course_base_data = self._get_course_by_url(course_url=course_url)
    course_data_originals: list[dict] = self._serialize_course_data(course_data, course_base_data)
    return course_data_originals
  
  def _sort_data(self) -> None:
    self.DATA = sorted(self.DATA, key = lambda x: (x['points'], 
                                                   x['code'],
                                                   -x['priority']
                                                   ), reverse=True)

  def _serialize_data(self) -> None:
    new_data = []
    current_user: list[dict] = [self.DATA[0]]
    for i in range(1, len(self.DATA)):
      if self.DATA[i]['code'] == self.DATA[i-1]['code']:
        current_user.append(self.DATA[i])
      else:
        new_data.append(current_user)
        current_user = [self.DATA[i]]
        print(new_data)
    self.DATA = new_data

  def change_data(self) -> None:
    for i in range(len(self.DATA) - 1):
      if (self.DATA[i]['code'] in self.competitors_data): continue
      last_code = self.DATA[i]['code']
      j = i
      while (j < len(self.DATA)) and (self.DATA[j]['code'] == last_code):
        if (not self.DATA[j]['code'] in self.competitors_data) and self.TECH_COURSES_DATA[self.DATA[j]['course_id']]['amount'] > 0:
          self.TECH_COURSES_DATA[self.DATA[j]['course_id']]['amount'] -= 1
          print(f'{self.DATA[j]["code"]} прошел по приору {self.DATA[j]["priority"]} сюда {self.TECH_COURSES_DATA[self.DATA[j]["course_id"]]["name"]} с баллами {self.DATA[j]["points"]}')
          self.competitors_data[last_code] = {'priority': self.DATA[j]["priority"],
                                              'course_id': self.DATA[j]["course_id"]}
          j+=1
        else:
          break
          

  def main(self):
    urls = self._get_courses_urls()
    for i in urls:
      self.DATA.extend(self._get_course_data(i))
    self._sort_data()
    # self._serialize_data()
    self.change_data()

    print(self.competitors_data)
    return self.TECH_COURSES_DATA