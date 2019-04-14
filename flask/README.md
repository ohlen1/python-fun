# flask

## JSON to XML transformer

### Start server
With debug: `python flask-json-to-xml.py debug`  
Without debug: `python flask-json-to-xml.py`

### Use service
Request formatted XML: `curl http://localhost:5000/jsontoxml -H "Content-type: application/json" -X POST -d '{"contactMethod": "sms", "contactAddress": "+46708395267", "subobject": {"subkey": "subvalue"}}'`  
Request formatted XML: `curl http://localhost:5000/jsontoxml?pretty=true -H "Content-type: application/json" -X POST -d '{"contactMethod": "sms", "contactAddress": "+46708395267", "subobject": {"subkey": "subvalue"}}'`
