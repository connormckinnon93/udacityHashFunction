import hashlib

def has_str(s):
	return hashlib.md5(s).hexdigest()
