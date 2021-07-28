import json
#
# def print_file(file_name: str)-> None:
#     with open

#conver json
def demo_json():
    example_data ={
        'name':"Alex",
        'age':28,
        'is_teacher': True,
        'other':None,
        'tags':['Python','C++','Django']
    }

    output_json_string= json.dumps(example_data)
    output_json_string_format = json.dumps(example_data,indent=4)
    print(output_json_string_format)
    print(example_data)
    print(output_json_string)
    print(type(output_json_string))
    parsed_dict_from_string=json.loads(output_json_string)
    print(parsed_dict_from_string)
demo_json()