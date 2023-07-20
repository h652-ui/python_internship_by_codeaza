import scrapy
from ..items import PokemonItem

class PokemonSpider(scrapy.Spider):
    name = 'pokemon'
    start_urls = ['https://pokemondb.net/pokedex/all']
    
    def parse(self, response):
        # Create an instance of the PokemonItem class to store scraped data
        items = PokemonItem()
        
        # Select all table rows from the response (excluding the header row)
        trs = response.css('tr')
        trs = trs[1:]
        
        # Extract type icon cells for each row in a separate list
        TPCs = [row.css('td.cell-icon') for row in trs]
        
        # Loop through each row and extract relevant information
        for row in trs:
            # Extract the 'id', 'name', 'iconPokemon', 'typePokemon', 'total', 'hp', 'attack', 'defense', 'spAttack', 'spDefense', 'speed' fields from the row
            id = row.css('span.infocard-cell-data::text').extract()
            name = row.css('a.ent-name::text').extract()
            iconPokemon = row.css('img.icon-pkmn').xpath("@src").extract()
            typePokemon = row.css('td.cell-icon').css('a.type-icon::text').extract()
            total = row.css('td.cell-num::text')[0].extract()
            hp = row.css('td.cell-num::text')[1].extract()
            attack = row.css('td.cell-num::text')[2].extract()
            defense = row.css('td.cell-num::text')[3].extract()
            spAttack = row.css('td.cell-num::text')[4].extract()
            spDefense = row.css('td.cell-num::text')[5].extract()
            speed = row.css('td.cell-num::text')[6].extract()
            
            # Store the extracted information in the PokemonItem instance
            items['id'] = id
            items['name'] = name
            items['iconPokemon'] = iconPokemon
            items['typePokemon'] = typePokemon
            items['total'] = total
            items['hp'] = hp
            items['attack'] = attack
            items['defense'] = defense
            items['spAttack'] = spAttack
            items['spDefense'] = spDefense
            items['speed'] = speed
            
            # Yield the PokemonItem instance to pass it to the output pipeline
            yield items