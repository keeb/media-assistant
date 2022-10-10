
from lib.file import get_folder_contents


def test_models_from_folder():
    root_folder = "/storage/01/pussy/alt/sg/4-2020-imageset"
    list_of_models = []
    for folder in get_folder_contents(root_folder):
        model_name = extract_model_name(folder)
        
        model = find_model_by_name(model_name, list_of_models)

        if model is None:
            model = Model(model_name)
            list_of_models.append(model)
            
    print(list_of_models)

"""
tests for Album logic
"""

def test_album():
    h = Model("hairu")
    a = Album(h, "Sugar doll")
    assert(a.model.name == "hairu")
    assert(a.name == "Sugar doll")




"""
tests for Model logic
"""

def test_model():
    h = Model("Hairu")
    assert(h.name == "Hairu")
    