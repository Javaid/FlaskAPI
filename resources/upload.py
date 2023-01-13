from gettext import gettext
import werkzeug
from flask_restful import Resource, reqparse

class Upload(Resource):
    @classmethod
    def post(cls):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        return {"message", gettext(args)}
        # audioFile = args['file']
        # audioFile.save("your_file_name.jpg")