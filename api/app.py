import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, jsonify
from recommendation.recommender import get_recommendations

from flask import Flask, jsonify
from recommendation.recommender import get_recommendations

app = Flask(__name__)

@app.route("/recommend/<int:student_id>")
def recommend(student_id):
    return jsonify({
        "student_id": student_id,
        "recommended_courses": get_recommendations(student_id)
    })

if __name__ == "__main__":
    app.run(debug=True)