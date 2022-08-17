import requests


class WaifuImCharacter():
    def __init__(self, image: str, nsfw: bool, tags: list) -> None:
        self.image = image
        self.nsfw = nsfw
        self.name = ""

        # we only need the name of the tags
        cleanedTags = []
        for elements in tags:
            cleanedTags.append(elements['name'])
        self.tags = cleanedTags

        self.tagTable = [
            "uniform",
            "maid",
            "waifu",
            "marin-kitagawa",
            "mori-calliope",
            "raiden-shogun",
            "oppai",
            "selfies",
            # nsfw part
            "ass",
            "hentai",
            "milf",
            "oral",
            "paizuri",
            "ecchi",
            "ero"
        ]

        self.status = None

    def __str__(self) -> str:
        return self.image

    def addStatus(self, newStatus: bool):
        self.status = newStatus

    def getNsfwRating(self) -> bool:
        return self.nsfw

    def formating(self) -> list:
        formated = []
        for i in self.tagTable:
            if i in self.tags:
                formated.append(1)
            else:
                formated.append(0)
        formated.append(self.status)
        return formated


class WaifuImApi():
    def __init__(self) -> None:
        self.url = "https://api.waifu.im/random"

    def getRandomCharacter(self) -> dict:
        return requests.get(self.url).json()

    def returnCharacter(self) -> object:
        character = self.getRandomCharacter()
        character = character['images'][0]

        return WaifuImCharacter(
            character['url'],
            character['is_nsfw'],
            character['tags']
        )


api = WaifuImApi()

anime = api.returnCharacter()
print(anime.formating())
