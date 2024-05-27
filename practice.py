if input_name in student["name"]:
    name_index = student["name"].idnex(input_name)
    search = {"name": student["name"][name_index], "age": student["age"][name_index], "score": student["score"][name_index]}