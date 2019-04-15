import json
from flask import Flask, redirect, url_for, request
import sys
app = Flask(__name__)

@app.route('/jsontoxml',methods = ['POST'])
def json_to_xml():
    if not validate_json_to_xml_request():
        return bad_request()
    pretty = request.args.get('pretty')
    request_json = request.get_json(request.data)
    app.logger.debug('json to transform: \n%s',json.dumps(request_json, indent=2))
    xml = transform_json_to_xml(request_json,pretty)
    app.logger.debug('transformed xml:\n%s', xml)
    resp = Flask.make_response(app,xml)
    resp.headers['Content-type'] = 'application/xml'
    return resp

def validate_json_to_xml_request():
    if request.content_type != 'application/json':
        app.logger.warn('Invalid content-type %s', request.content_type)
        return False
    if not request.data:
        app.logger.warn('Missing request payload')
        return False
    return True

def bad_request():
    return 'Bad request', 400

def transform_json_to_xml(my_json,pretty):
    my_xml = '<root>'
    my_xml += transform_dict_to_xml(my_json,1,pretty)
    my_xml += ''.join(('\r\n</root>'))
    return my_xml

def transform_dict_to_xml(my_json,level,pretty):
    my_xml = ''
    for k,v in my_json.iteritems():
        if not isinstance(v,dict):
            if pretty:
                my_xml += '\r\n'
                for x in range(0,level):
                    my_xml += ' '
            my_xml += ''.join(('<',k,'>',v,'</',k,'>'))
        else:
            if pretty:
                my_xml += '\r\n '
            my_xml += ''.join(('<',k,'>'))
            my_xml += transform_dict_to_xml(v,level+1,pretty)
            if pretty:
                my_xml += '\r\n '
            my_xml += ''.join(('<','/',k,'>'))
    return my_xml

if __name__ == '__main__':
   app.run(debug = (len(sys.argv)>1 and sys.argv[1]=='debug'))
