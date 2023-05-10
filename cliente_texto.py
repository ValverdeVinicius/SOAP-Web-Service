# -*- coding: utf-8 -*-
from zeep import Client
client = Client('http://localhost:8080/disciplinasws?wsdl')
result = client.service.getTemas()
print(result)