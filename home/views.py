from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from heligeo import heliGeoprocessingService
from folium.map import Popup
import pandas as pd
import folium
import dash_html_components as html
from branca.element import Figure
from home.forms import polygonform
from django.views.decorators.csrf import csrf_exempt


def landingpage(request):
    return render(request,'Base.html')


@csrf_exempt
def Home(request):
    form = polygonform()
    apikey = 'jhyterfvdrwesuyt'
    if request.method == "POST":
        fig=Figure(width=550,height=350)
        form = polygonform(request.POST)
        if form.is_valid():
            polygon1 = form.cleaned_data.get('polygon1')
            polygon2 = form.cleaned_data.get('polygon2')
            polygon_list = [polygon1,polygon2]
            union_data = heliGeoprocessingService.Union(apikey,polygon_list)
            x = union_data['features'][0]['geometry']
            y=x['coordinates'][0]
            for i in y:
                m2=folium.Map(location=i)
                fig.add_child(m2)
                folium.Marker(location=i,popup=str(i),tooltip="here").add_to(m2)
                folium.TileLayer('cartodbdark_matter').add_to(m2)
                folium.LayerControl().add_to(m2)
                m2.save("templates/map.html")
        else:
            context = "this is not valid form"
            return JsonResponse({'context':context})
    else:
        context = "Method is not POST"
        return JsonResponse({'context':context})

def show_map(request):
    return render(request, "map.html")