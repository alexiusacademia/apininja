# API Created for time_record

def serialize_time_record(data):
	return {"id": data.id}

def serialize_time_records(lst):
	serialized = []
	for item in lst:
		serialized.append(serialize_time_record(item))
	return serialized

def time_record_list_api(lst):
	return serialize_time_records(lst)

def time_record_detail_api(data):
	return serialize_time_record(data)

def time_record_create_api(*args, **kwargs):
	pass

def time_record_update_api(*args, **kwargs):
	pass

def time_record_delete_api(*args):
	pass

