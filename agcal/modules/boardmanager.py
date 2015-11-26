import json

from agcal.models import Board, User


def get_all_boards_for(username):
    try:
        user = User.objects.get(username=username)
    except Exception:
        response = '{"message": "No such user"}'
        status = 404
    else:
        boards = Board.objects.filter(created_by=user)
        details = []

        for board in boards:
            details.append({
                'name': board.name,
                'description': board.description,
                'id': board.id
            })

        response = json.dumps(details)
        status = 200

    return (response, status)


def get_board_for(username, board_id):
    pass
