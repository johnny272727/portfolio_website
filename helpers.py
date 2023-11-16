import csv
from pathlib import Path
from time import gmtime, strftime
def does_file_exists(file_path):
    return Path(file_path).is_file()

def save_data_to_csv(data):
    print(f'data has been saved: {data}')
    file_exists = does_file_exists('./form_submitted_data.csv')
    with open('form_submitted_data.csv', 'a', newline='') as csv_file:
        fieldnames = ['name', 'email','phone','message','datetime']
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
        if not file_exists:
            writer.writerow(fieldnames)    
        writer.writerow([*data.values(), strftime("%Y-%m-%d %H:%M:%S",gmtime())+" UTC"])    

    