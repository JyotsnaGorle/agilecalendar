import json

from agcal.models import Board, User


def get_all_boards_for(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
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
    except Board.DoesNotExist:
        response = '{"message": "No such user/board combo found"}'
        status = 404

    return (response, status)


def add_board(creator, description, name):
    try:
        user = User.objects.get(username=creator)
        board = Board(created_by=user, description=description, name=name)
        board.save()
        response = '{"message": "Ok"}'
        status = 200
    except User.DoesNotExist:
        response = '{"message": "No such user found"}'
        status = 404

    return (response, status)


def edit_board(creator, board_id, description, name):
    try:
        board = Board.objects.get(created_by=User.objects.get(username=creator), id=board_id)
        board.description = description
        board.name = name
        board.save()
        response = '{"message": "Ok"}'
        status = 200
    except User.DoesNotExist, Board.DoesNotExist:
        response = '{"message": "No such user/board combo found"}'
        status = 404

    return (response, status)
