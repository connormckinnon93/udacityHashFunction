import hmac

SECRET = "imsosecret"
def has_str(s):
    return hmac.new(SECRET, s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, has_str(s))


def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val


def gae_cookie_hasher():
    visits = 0
    visit_cookie_str = self.request.cookies.get('visits')

    if visit_cookie_str:
        cookie_val = check_secure_val(visit_cookie_str)
        if cookie_val:
            visits = int(cookie_val)

    visits += 1

    new_cookie_val = make_secure_val(str(visits))

    self.response.headers.add_header(
        'Set-Cookie', 'visits=%s' % new_cookie_val)
