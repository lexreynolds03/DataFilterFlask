import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    data = read_csv('data.csv')
    if request.method == 'POST':
        name_filter = request.form.get('name', '').strip().lower()
        type_filter = request.form.get('type', '').strip().lower()
        brand_filter = request.form.get('brand', '').strip().lower()

        filtered_data = []
        for row in data:
            name_match = name_filter in row.get('Name', '').lower() if name_filter else True
            type_match = type_filter in row.get('Type', '').lower() if type_filter else True
            brand_match = brand_filter in row.get('Brand', '').lower() if brand_filter else True
            
            if name_match and type_match and brand_match:
                filtered_data.append(row)
        return render_template('index.html', data=filtered_data)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)