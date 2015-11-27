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
    try:
        board = Board.objects.get(created_by=username, id=board_id)
        response = json.dumps({
            'name': board.name,
            'description': board.description,
            'id': board.id
        })
        status = 200
    except Exception:
        response = '{"message": "No such user/board combo found"}'
        status = 404

    return (response, status)
