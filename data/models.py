
from dataclasses import dataclass
from dataclasses import asdict

import petrovna

@dataclass
class SNILS:
  value: str

  # def __post_init__(self):
  #   if not petrovna.validate_snils(self.value):
  #     raise TypeError('snils is incorrected')

@dataclass
class CoursePositionData:
  course_name: str
  course_url: str
  course_priority: int
  person_position: int
  person_snils: SNILS 
  person_points: int 

  def dict(self) -> dict:
    return {k: str(v) for k, v in asdict(self).items()}

@dataclass
class Competitor:
  snils: SNILS
  priority: int

@dataclass
class PersonCoursePositionsData:
  positions: list[CoursePositionData]
  
  def dict(self) -> dict:
    return {k: str(v) for k, v in asdict(self).items()}
