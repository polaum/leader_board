from flask import Flask, request, jsonify

from leader_board_functions import add_score, get_leaders, _min_score, ScoreNotEligible, is_score_eligible

app = Flask(__name__)


@app.route('/health')
def health():
    return 'ok - leader board API', 200


@app.route('/getScores', methods=['GET'])
def getScores():
    lb = get_leaders()
    response_data = []
    for row in lb:
        response_data.append({"userName": row.user_name, "score": row.score,
                              "itemsShot": row.items_shot, "timePlayed": row.time_played})
    return jsonify(response_data), 200


@app.route('/isScoreEligible', methods=['GET'])
def isScoreEligible():
    score = int(request.args.get('score'))
    if is_score_eligible(score):
        return "score is eligible", 200
    else:
        return "score is not eligible", 400


@app.route('/addScore', methods=['POST'])
def addScore():
    body = request.json
    userName = body['userName']
    score = body['score']
    itemsShot = body['itemsShot']
    timePlayed = body['timePlayed']
    try:
        add_score(userName, score, itemsShot, timePlayed)
        return "score added!", 201
    except ScoreNotEligible:
        return "Score not eligible to enter the leader board!", 400


if __name__ == '__main__':
    app.run('0.0.0.0', 5001)
