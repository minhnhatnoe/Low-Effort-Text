import datetime
def hello() -> 'list[str]':
    return ["Welcome to VNOI Cup! This contest is hosted by VNOI.", "For more information visit https://vnoi.info."]

def sponsor() -> 'list[str]':
    return ["This contest is sponsored by XX YY ZZ"]

def result() -> 'list[str]':
    if datetime.datetime.now() > datetime.datetime(2023, 7, 14, 20, 48):
        return ["Ranking is frozen in the last 1 hour of the contest"]
    return ["1. A: XX | 2. B: XX | 3. C: XX | 4. C: XX | 5. C: XX | 6. C: XX",
            "7. A: XX | 8. B: XX | 9. C: XX | 10. C: XX | 11. C: XX | 12. C: XX"]
