from flask import Response, Blueprint, jsonify, json, request
from service.list_se_service import ListSE_service
from util.util_encoder import util_encoder

app_list_se=Blueprint("app_list_se", __name__)

list_se_service = ListSE_service()


@app_list_se.route('/list_se/all')
def get_all_students():
    return Response(status=200, response=json.dumps(list_se_service.get_all_students(), cls=util_encoder),
                    mimetype='aplication/json')

#Agregar el estudiante desde postman

@app_list_se.route('/list_se', methods=['POST'])
def save_students():
    try:
        data= request.json
        list_se_service.add_student(data)
        return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype='aplication/json')

    except Exception as error:
        return Response(status=409, response=json.dumps({"message": str(error)}),
                        mimetype='aplication/json')

#Invertir la lista

@app_list_se.route('/list_se/all/inversed')
def get_reversed_list():
    return Response(status=200, response=json.dumps(list_se_service.reversed_list(), cls=util_encoder),
                    mimetype='aplication/json')

