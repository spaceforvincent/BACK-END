from flask import Flask, jsonify 

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.

@app.route('/population') 
def population():  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
	pop_info = {'Seoul' : 9598484, #
	'Busan' : 3372399,
	'Gyeonggi' : 13465837}
	
	return jsonify(pop_info) #json형태로 만듬

if __name__ == "__main__":
    app.run()