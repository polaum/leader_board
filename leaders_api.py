from flask import Flask, request, jsonify

from leader_board_functions import add_score, get_leaders, _min_score, ScoreNotEligible

app = Flask(__name__)


@app.route('/health')
def health():
    return 'ok - leader board API', 200


@app.route('/get_scores', methods=['GET'])
def get_scores():
    lb = get_leaders()
    response_data = []
    for row in lb:
        response_data.append({"User name": row.user_name, "score": row.score,
                              "Items shot": row.items_shot, "Time played": row.time_played})
    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run('0.0.0.0', 5001)
