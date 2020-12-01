from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def hello(request):
	return HttpResponse("Hello World")


@csrf_exempt
def validate_finite_values_entity(request):
	params = json.loads(request.body)
	values = params['values']
	supported_values = params['supported_values']
	key = params['key']
	invalid_trigger = params['invalid_trigger']
	pick_first = params['pick_first']

	valid_list = []
	for item in values:
		if item['value'] in supported_values:
			valid_list.append(item['value'])


	return JsonResponse({
		    "filled": True if len(values)>0 and len(valid_list) == len(values) else False,
		    "partially_filled": True if len(valid_list)!=len(values) or (len(values)>0 and len(valid_list)==0) else False,
		    "trigger": '' if len(values)>0 and len(valid_list) == len(values) else invalid_trigger,
		    "parameters": {key: valid_list[0] if pick_first else valid_list} if len(values)>0 and len(valid_list) == len(values) else {}
		})


@csrf_exempt
def validate_numeric_entity(request):
	params = json.loads(request.body)
	values = params['values']
	key = params['key']
	invalid_trigger = params['invalid_trigger']
	var_name = params['var_name']
	constraint = params['constraint']
	pick_first = params['pick_first']

	valid_list = []
	for item in values:
		value = item['value']
		if eval(constraint.replace(var_name, str(value))):
			valid_list.append(item['value'])


	return JsonResponse({
		    "filled": True if len(values)>0 and len(valid_list) == len(values) else False,
		    "partially_filled": True if len(valid_list)!=len(values) or (len(values)>0 and len(valid_list)==0) else False,
		    "trigger": '' if len(values)>0 and len(valid_list) == len(values) else invalid_trigger,
		    "parameters": {key: valid_list[0] if pick_first else valid_list} if len(valid_list)>0 else {}
		})

