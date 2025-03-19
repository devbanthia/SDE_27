import json

def read_data_from_json(file_path):

  with open(file_path, 'r') as file:
      deeds_data = json.load(file)

  classes = deeds_data['classes']
  annotations = deeds_data['annotations']

  return classes, annotations


import json
import os

def read_data_from_second_json_file(file_path):

  subfolders = os.listdir(file_path)

  valid_entities = {"BUYER NAME", "SELLER NAME", "BUYER ADDRESS", "BUYER NONINDIVIDUAL NAME", "SELLER NONINDIVIDUAL NAME", "PROPERTY ADDRESS", "ASSESSOR PARCEL NUMBER"}

  labelled_text = []
  for subfolder in subfolders:
    subfolder_path = os.path.join(file_path, subfolder)
    json_files = os.listdir(subfolder_path)
    for json_file in json_files:

      full_file_path = os.path.join(subfolder_path, json_file)
      with open(full_file_path, 'r') as file:
        deeds_data = json.load(file)

      classes = deeds_data['classes']
      annotations = deeds_data['annotations']
      for text, entities in annotations:

        entities_present_in_text = entities["entities"]
        updated_entities = entities_present_in_text[:]

        for i, entity_present_in_text in enumerate(entities_present_in_text):

          if len(entities_present_in_text) > 0:
            if entity_present_in_text[2] == 'SELLER NON INDIVIDUAL NAMES':
              updated_entities[i][2] = 'SELLER NONINDIVIDUAL NAME'

            if entity_present_in_text[2] == 'BUYER ADDDRESS':
              updated_entities[i][2] = 'BUYER ADDRESS'

            filtered_entities = list(filter(lambda x: x[2] in valid_entities, updated_entities))

        labelled_text.append([text, {"entities":filtered_entities}])

  return labelled_text




file_path = '/content/drive/My Drive/WD-(4129)/'

def load_test_data_from_json(file_path , second_file_path):

  json_files = os.listdir(file_path)
  classes = ['ASSESSOR PARCEL NUMBER', 'PROPERTY ADDRESS', 'BUYER ADDRESS', 'BUYER NAME', 'BUYER NONINDIVIDUAL NAME', 'SELLER NAME', 'SELLER NONINDIVIDUAL NAME']
  cleaned_annotations = []
  for json_file in json_files:

    full_file_path = os.path.join(file_path, json_file)

    with open(full_file_path, 'r') as file:
      deeds_data = json.load(file)
      for text, entity in deeds_data["annotations"]:
        cleaned_annotations.append([text, entity])

  if second_file_path != None:

    second_batch = read_data_from_second_json_file(second_file_path)
    cleaned_annotations.extend(second_batch)

  print(len(cleaned_annotations))
  return classes, cleaned_annotations
