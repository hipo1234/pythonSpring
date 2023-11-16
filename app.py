from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import ex04

app = Flask(__name__)

# 데이터베이스 설정
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:1234@localhost:3306/kcs'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app, engine_options={"connect_args": {"charset": "utf8"}})
#
page_bp = Blueprint('match', __name__, url_prefix='/')

# 파일 업로드
@page_bp.route('/uploads', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            filename = secure_filename(f.filename)
            f.save('static/uploads/' + filename)

            # try:
            #     with db.engine.connect() as conn:
            #         # 파일명과 파일경로를 데이터베이스에 저장함
            #         sql = "INSERT INTO images (image_name, image_dir) VALUES (%s, %s)"
            #         conn.execute(sql, (secure_filename(f.filename), 'uploads/' + filename))
            #     return '파일 업로드가 성공했습니다'
            # except Exception as e:
            #     return 'uploads failed'
        else:
            return 'No file uploaded'

    return 'Invalid request method'
#
# # 메인 페이지
# # @page_bp.route('/')
# # def page():
# #     try:
# #         with db.engine.connect() as conn:
# #             # 이미지 정보를 데이터베이스에서 가져옴
# #             sql = "SELECT image_name, image_dir FROM images"
# #             data = conn.execute(sql).fetchall()
# #
# #         data_list = []
# #
# #         for obj in data:
# #             data_dic = {
# #                 'name': obj[0],
# #                 'dir': obj[1]
# #             }
# #             data_list.append(data_dic)
# #
# #         return render_template('index.html', data_list=data_list)
# #     except Exception as e:
# #         return 'An error occurred while fetching data from the database'
#
#
# # 다른 방법
# # 해당 코드는 파일 업로드 테스트하기 위한 임시 코드임
# # 업로드된 파일을 저장할 경로 설정
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # 업로드된 파일 가져오기
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # 파일 저장 경로 설정
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            # 파일 저장
            uploaded_file.save(file_path)
            return 'File uploaded successfully!'

    productFood = ex04.getProductFood()
    productFoodInfo = ex04.getProductFoodInfo()
    productFoodInfo2 = ex04.getProductFoodInfo2()
    Age = ex04.getAge()
    recommend = process()
    return render_template('index.html', productFood=productFood, productFoodInfo=productFoodInfo, productFoodInfo2=productFoodInfo2, Age=Age, recommend=recommend)

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        data = request.get_json()
        food = data['food']
        food_info = data['foodinfo']
        food_info2 = data['foodinfo2']
        age = data['age']

        if(age == '10대'):
            age = "초등학생 아이 꼬마 아동 여름방학"
        elif(age == '20대'):
            age = "학교 여름방학"
        else:
            age = "가족 집"

        food_info1=[]
        food_info1.append(food_info)
        food_info1.append(food_info2)
        food_info1.append(age)
        # print(food_info1)

        animes = ex04.similar_animes(product_info=food_info1)
        recommend = ex04.recommend_anime(product_index=food, similar_anime_indices=animes)
    else:
        recommend = "No recommendation available"
    return jsonify(recommend)

app.register_blueprint(page_bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")



#
#
#
#
#
#
#
#
#



# 아래 코드는 8월 22일 기준 이미지 파일을 합치는 코드임. 아직까진 미사용임
# from flask import Flask, render_template, request, send_from_directory
# from PIL import Image
# import os
#
# app = Flask(__name__)
#
# UPLOAD_FOLDER = 'uploads'
# COMBINED_FOLDER = 'combined'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
# if not os.path.exists(COMBINED_FOLDER):
#     os.makedirs(COMBINED_FOLDER)

# @app.route('/', methods=['GET', 'POST'])
# def upload_image():
#     if request.method == 'POST':
#         image1 = request.files['file1']
#         image2 = request.files['file2']
#
#         if not image1 or not image2:
#             return 'Please upload both images', 400
#
#         image1_path = os.path.join(UPLOAD_FOLDER, image1.filename)
#         image2_path = os.path.join(UPLOAD_FOLDER, image2.filename)
#         combined_path = os.path.join(COMBINED_FOLDER, 'combined_' + image1.filename)
#
#         image1.save(image1_path)
#         image2.save(image2_path)
#
#         # Combine images
#         with Image.open(image1_path) as img1, Image.open(image2_path) as img2:
#             # Example of combining side by side. Modify as needed.
#             dst = Image.new('RGB', (img1.width + img2.width, img1.height))
#             dst.paste(img1, (0, 0))
#             dst.paste(img2, (img1.width, 0))
#             dst.save(combined_path)
#
#         return send_from_directory(COMBINED_FOLDER, 'combined_' + image1.filename)
#
#     return render_template('upload.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

