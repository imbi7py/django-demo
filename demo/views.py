from django.http import HttpResponse

def hostport(request):
    host = request.get_host()
    port = request.get_port()
    response = "{}:{}".format(host, port)
    return HttpResponse(response)
