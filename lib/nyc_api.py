import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "https://data.cityofchicago.org/resource/ydr8-5enu.json"
        response = requests.get(URL)
        return response.text

    def program_schools(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        print(programs)  # Print the response content for examination
        for program in programs:
            programs_list.append(program["agency"])
        return programs_list

# Instantiate the class
program_instance = GetPrograms()

# Call the method to get program schools
programs_schools = program_instance.program_schools()

# Print out the unique schools
for school in set(programs_schools):
    print(school)
