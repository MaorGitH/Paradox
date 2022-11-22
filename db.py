import requests

# base_path = "http://ec2-54-175-34-191.compute-1.amazonaws.com:8000/conversation_builder"
# answers = requests.get(base_path + "/answer").json()
# chats = requests.get(base_path + "/chat").json()
# questions = requests.get(base_path + "/question").json()

conversations = {
    "1": {
        "first_question": "1",
        "questions": {
            "1": {
                "next_qid": 4,
                "prev_qid": None,
                "type": 1,
                "text": "Why do you want to work at Paradox?",
                "answers": []
            },
            "4": {
                "next_qid": 7,
                "prev_qid": 1,
                "type": 2,
                "text": "How many years of Truck Driving experience do you have?",
                "answers": {
                    "min": 0,
                    "max": 30
                }
            },
            "7": {
                "next_qid": 4,
                "prev_qid": None,
                "type": 3,
                "text": "Would you say you care about the effect of the trucking industry on global warming?",
                "answers": [
                    "Very much",
                    "A bit",
                    "Not so much",
                    "Not at all"
                ]
            }
        }
    }
}
