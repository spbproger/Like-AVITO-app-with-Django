import csv
import json

CSV_ADS = "ads.csv"
JSON_ADS = "ads.json"
CSV_CATEG = "categories.csv"
JSON_CATEG = "categories.json"

def transform_file(csv_file, json_file, model_name):
    result = []
    with open(csv_file, encoding="utf-8") as csv_f:
        for str_ in csv.DictReader(csv_f):
            add_to = {"model": model_name, "pk": int(str_['Id'] if "Id" in str_ else str_['id'])}
            if "Id" in str_:
                del str_['Id']
            else:
                del str_['id']
            if "is_published" in str_:
                if str_['is_published'] == "TRUE":
                    str_["is_published"] = True
                else:
                    str_["is_published"] = False
            if "price" in str_:
                str_['price'] = int(str_['price'])
            add_to['fields'] = str_
            result.append(add_to)
    with open(json_file, 'w', encoding="utf-8") as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


transform_file(CSV_ADS, JSON_ADS, "ads.ad")
transform_file(CSV_CATEG, JSON_CATEG, "ads.category")