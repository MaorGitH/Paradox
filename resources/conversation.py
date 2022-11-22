from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import conversations

blp = Blueprint("conversations", __name__, description="Operations on conversations")


@blp.route("/conversation/<string:chat_id>")
class Conversation(MethodView):
    @blp.response(200)
    def get(self, chat_id):
        try:
            conversation = conversations[chat_id]
            return conversation
        except KeyError:
            abort(404, message="Chat not found")
