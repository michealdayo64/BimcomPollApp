from django.shortcuts import render, redirect
from .models import PollingUnit, AnnouncedPuResults, Lga, Ward, Party
from django.http import JsonResponse
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
# Create your views here.


def index(request):
    pol_unit = PollingUnit.objects.all().order_by('-date_entered')
    paginator = Paginator(pol_unit, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_query = paginator.page(page)
    except PageNotAnInteger:
        paginated_query = paginator.page(1)
    except EmptyPage:
        paginated_query = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'pol_unit': paginated_query, 'page_request_var': page_request_var})

def polling_result(request, id):
    pu_id = PollingUnit.objects.get(id = id)
    pu_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = id)
    #print(pu_result)
    context = {
        'pu_id': pu_id,
        'pu_result': pu_result
    }
    return render(request, 'pu_result.html', context)

def sum_total_result_lga(request):
    local_gov = Lga.objects.all()
    context = {
        'local_gov': local_gov
    }
    return render(request, 'summed_result.html', context)

def get_loc_id(request):
    #data = {}
    ns = json.loads(request.body)
    loc_gov = ns['lga']
    loc_gov_id = Lga.objects.get(id = loc_gov)
    '''wardid = Ward.objects.filter(lga_id = loc_gov_id.id)
    for i in wardid:
        for k in PollingUnit.objects.filter(ward_id = i.ward_id):
            print(k.id)'''
    pollU = AnnouncedPuResults.objects.filter(polling_unit_uniqueid = loc_gov_id.id)
    try:
        pu_id = PollingUnit.objects.filter(id = loc_gov_id.id)
        #print(pu_id)
        total = 0
        for i in pollU:
            #print(f"{i.party_abbreviation} score is {i.party_score} {i.polling_unit_uniqueid} ")
            total += i.party_score

        #print(total)
        poolU = []
        for k in pu_id:
            print(k.polling_unit_name)
            poolU.append(k.polling_unit_name)

        print(len(poolU))
        if len(poolU) == 0:

            data = {
                'polling_unit': f'No Pooling Unit',
                'total_score': f'No Score'
            }
        else:
            data = {
                'polling_unit': f'{poolU[0]}',
                'total_score': f'{total}'
            }
        
    except PollingUnit.DoesNotExist:
        print("Polling not available")
        

    return JsonResponse(data, safe = True)

def store_polling_unit_result(request):
    allWard = Ward.objects.all()
    allLga = Lga.objects.all()
    allParty = Party.objects.all()
    
    if request.method == 'POST':
        polling_unit_id = request.POST.get('polling_unit_id')
        ward_id = request.POST.get('ward_id')
        lga_id = request.POST.get('lga_id')
        uniquewardid = request.POST.get('uniquewardid')
        polling_unit_number = request.POST.get('polling_unit_number')
        polling_unit_name = request.POST.get('polling_unit_name')
        polling_unit_description = request.POST.get('polling_unit_description')
        lat = request.POST.get('lat')
        longi = request.POST.get('longi')
        entered_by_user = request.POST.get('entered_by_user')
        date_entered = request.POST.get('date_entered')
        user_ip_address = request.POST.get('user_ip_address')
        party_name = request.POST.get('party_name')
        party_score = request.POST.get('party_score')


        res = PollingUnit.objects.create(polling_unit_id = polling_unit_id, ward_id = ward_id, lga_id = lga_id, uniquewardid = uniquewardid, polling_unit_number= polling_unit_number, polling_unit_name = polling_unit_name, polling_unit_description = polling_unit_description, lat = lat, longi = longi, entered_by_user = entered_by_user, date_entered = date_entered, user_ip_address = user_ip_address)
        AnnouncedPuResults.objects.create(polling_unit_uniqueid = res.id, party_abbreviation=party_name, party_score = party_score, entered_by_user = entered_by_user,  date_entered = date_entered, user_ip_address = user_ip_address)
        messages.success(request, "Pooling Added Successfully")
        return redirect("index")
    context = {
        'allWard': allWard,
        'allLga': allLga,
        'allParty': allParty
    }
    return render(request, 'store_result.html', context)