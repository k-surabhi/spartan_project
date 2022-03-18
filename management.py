import json
from spartan import Spartan


class SpartanManagement:
    DATA_FILE_NAME = "data.json"
    DATA_FILE_READ_MODE = "r"
    DATA_FILE_WRITE_MODE = "w+"

    Spartan_Trainees_Dict = {}

    def __init__(self):
        try:
            with open(self.DATA_FILE_NAME, self.DATA_FILE_READ_MODE) as data_file:
                self.Spartan_Trainees_Dict = json.load(data_file)
        except:
            pass

    def add_trainee(self, id, f_name, l_name, b_year, b_month, b_day, course, stream):

        try:
            s = Spartan()
            s.spartan_id = id
            s.first_name = f_name
            s.last_name = l_name
            s.birth_year = b_year
            s.birth_month = b_month
            s.birth_day = b_day
            s.course = course
            s.stream = stream

            self.Spartan_Trainees_Dict[id] = s

            self.__update_json()
            return "SUCCESS"

        except Exception as ex:
            print(str(ex))
            return str(ex)

