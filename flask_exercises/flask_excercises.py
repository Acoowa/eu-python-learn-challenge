from flask import Flask, request, jsonify


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        DB = {}

        @app.post("/user")
        def creat_user() -> request:
            data = request.json
            if data.get("name", None) is None:
                return jsonify({"errors": {"name": "This field is required"}}), 422

            name = data["name"]
            DB[name] = {}
            return jsonify({"data": f"User {name} is created!"}), 201

        @app.get("/user/<name>")
        def get_user(name: str) -> request:
            if name not in DB:
                return jsonify({"errors": {"name": "There are no user with this name"}}), 404
            return jsonify({"data": f"My name is {name}"}), 200

        @app.patch("/user/<name>")
        def update_user(name: str) -> request:
            if name not in DB:
                return jsonify({"errors": {"name": "There are no user with this name"}}), 404
            data = request.json
            new_name = data["name"]
            DB[new_name] = DB.pop(name)
            return jsonify({"data": f"My name is {new_name}"}), 200

        @app.delete("/user/<name>")
        def delete_user(name):
            if name not in DB:
                return jsonify({"errors": {"name": "There are no user with this name"}}), 404
            DB.pop(name)
            return "", 204
