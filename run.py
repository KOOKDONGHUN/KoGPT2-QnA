from flask import Flask, request, render_template

app = Flask(__name__)

#----------------------------------------------------
# 페이지 표시
#----------------------------------------------------
@app.route("/")
def show_page():

    #--------------------------------
    # 파라미터 설정
    #--------------------------------
    text = request.args.get("text")
   
    #--------------------------------
    # 대답 구함
    #--------------------------------
    if text != None:
        answer = text
    else:
        answer = None
    
    return render_template('test.html', question = text, answer = answer)



#----------------------------------------------------
# 메인 함수
#----------------------------------------------------
if __name__ == "__main__":

    app.run(host='0.0.0.0', port = 5000, threaded=True)