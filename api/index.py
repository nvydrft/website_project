from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    # 엑셀 파일 경로 설정
    excel_path = os.path.join(os.path.dirname(__file__), '../result4.xlsx')
    # 엑셀 파일 읽기
    df = pd.read_excel(excel_path)
    # HTML 테이블로 변환
    excel_data = df.to_html(index=False, classes='excel-table')
    return render_template('index.html', excel_data=excel_data)

# Vercel 서버리스 함수로 사용하기 위해 app을 export
def handler(event, context):
    return app(event, context)