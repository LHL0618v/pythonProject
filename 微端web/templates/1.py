from flask import Flask
from flask import jsonify
from flask import request

account = 1001
res_ac = request.form.get("account")

print(res_ac, type(res_ac))
