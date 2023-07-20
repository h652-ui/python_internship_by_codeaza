# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    name = scrapy.Field()
    iconPokemon = scrapy.Field()
    typePokemon = scrapy.Field()
    total = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    spAttack = scrapy.Field()
    spDefense = scrapy.Field()
    speed = scrapy.Field()
