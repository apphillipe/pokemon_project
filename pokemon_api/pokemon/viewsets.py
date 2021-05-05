from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from collections import OrderedDict

import requests

class PokemonViewSet(viewsets.ViewSet):

    def list(self, request):

        if 'name' in request.GET and request.GET['name']:
            response = requests.get('https://pokeapi.co/api/v2/pokemon/' + request.GET['name'])
        
            pokemon_abilities = response.json()['abilities']
            if response.status_code == 200:
                if len(pokemon_abilities) > 0:
                    resp = {}

                    for abilities in pokemon_abilities:
                        ability_name = abilities['ability']['name']
                        ability_url = abilities['ability']['url']

                        resp_ability = requests.get(ability_url)
                        if resp_ability.status_code == 200:

                            ability_detail = resp_ability.json()

                            entry_en = list(filter(lambda x: x['language']['name'] == 'en', ability_detail['effect_entries']))
                            if len(entry_en) > 0:
                                resp[ability_name] = entry_en[0]['effect']

                    resp = OrderedDict(sorted(resp.items(), key=lambda x: x[0]))
                    return Response({
                        'data': resp
                    })

        return Response()
