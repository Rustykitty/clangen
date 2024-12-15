import ujson


class Herb:
    def __init__(
            self,
            herb_name,
            season,
            biome
            ):
        self.name: str = herb_name
        self._herb_dict: dict = HERBS.get(self.name, {})

        self._display_dict = self._herb_dict.get("display", {})
        self.singular_display = self._display_dict.get("singular", self.name)
        self.plural_display = self._display_dict.get("plural", self.name)

        self.expiration: int = self._herb_dict.get("expiration", 1)

    def get_rarity(self, biome, season) -> int:
        """
        returns rarity of the herb within clan's current biome and season
        """
        rarity_dict = self._herb_dict.get("rarity", {})

        return rarity_dict.get(biome.casefold(), {}).get(season.casefold(), 0)


with open("resources/dicts/herbs.json", "r", encoding="utf-8") as read_file:
    HERBS = ujson.loads(read_file.read())