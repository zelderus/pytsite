




def isNotNull(value):
	return value is not None and len(value) > 0


def isNotNullOrEmpty(value):
	return value is not None and len(value) > 0 and value != ""