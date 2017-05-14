import hashlib

def has_str(s):
	return hashlib.md5(s).hexdigest()

def make_secure_val(s):
	return "%s,%s" % (s, has_str(s))