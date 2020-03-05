def main(request, response):
    return 301, [('Location', 'expect-client-hints-headers.html'),('Accept-CH', 'device-memory, DPR')], ''
