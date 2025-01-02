from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def retail_sale_home(request):
    districts = District.objects.filter(district_status=True)
    species_categories = Species_Category.objects.filter(species_category_status=True)
    species = Species.objects.filter(species_status=True)

    context = {
        'districts': districts,
        'species_categories': species_categories,
        'species': species,
    }

    return render(request, 'retail_sale_home.html', context)


def depnd_species(req, id_dist):
    district = District.objects.get(id=id_dist)
    species_category = Species_Category.objects.filter(district_name=district, species_category_status=True)
    species_category_list = [{'id': species_category.id, 'name': species_category.species_category_name} for species_category in species_category]

    return JsonResponse({'species_category_list': species_category_list})


def search_data(request):
    if request.method == 'POST':
        dist_id = request.POST.get('dist')
        species_id = request.POST.get('species')

        if species_id:  # If species is selected
            species = Species.objects.get(id=species_id)
            data = {
                'species_name': species.species_name,
                'quantity': species.species_quantity,
                'sub_quantity': species.species_sub_quantity,
                'date': species.species_date,
                'depots': species.species_depots,
                'address_line_1': species.species_address_line_1,
                'address_line_2': species.species_address_line_2,
                'phone': species.species_phone_number,
                'email': species.species_email
            }
            return JsonResponse(data)

        else:  # If only district is selected
            species_list = Species.objects.filter(district_name_id=dist_id, species_status=True)
            data = []
            for species in species_list:
                data.append({
                    'species_name': species.species_name,
                    'quantity': species.species_quantity,
                    'sub_quantity': species.species_sub_quantity,
                    'date': species.species_date,
                    'depots': species.species_depots,
                    'address_line_1': species.species_address_line_1,
                    'address_line_2': species.species_address_line_2,
                    'phone': species.species_phone_number,
                    'email': species.species_email
                })
            return JsonResponse({'species_list': data})

