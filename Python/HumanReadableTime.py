def make_readable(seconds):
    hr = seconds  // (60 * 3600)
    min = (seconds // 60) - (hr * 60)
    sec = seconds % 60
    pad = lambda n: str(n).zfill(2)
    return "%s:%s:%s" % (pad(hr), pad(min), pad(sec))
