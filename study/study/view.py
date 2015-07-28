from django.shortcuts import render_to_response
import datetime
def hello(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html',  locals())