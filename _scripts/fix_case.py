from rdflib import Graph

changes = {
    "ANAKIE_PROVINCE": "AnakieProvince",
    "BROKEN_RIVER_PROVINCE": "BrokenRiverProvince",
    "CALLIOPE_PROVINCE": "CalliopeProvince",
    "CENTRALIAN_SUPERBASIN": "CentralianSuperbasin",
    "CHARTERS_TOWERS_PROVINCE": "ChartersTowersProvince",
    "CONNORS_AUBURN_PROVINCE": "ConnorsAuburnProvince",
    "ETHERIDGE_PROVINCE": "EtheridgeProvince",
    "GREAT_AUSTRALIAN_SUPERBASIN": "GreatAustralianSuperbasin",
    "HODGKINSON_PROVINCE": "HodgkinsonProvince",
    "KENNEDY_IGNEOUS_PROVINCE": "KennedyIgneousProvince",
    "MOSSMAN_OROGEN": "MossmanOrogen",
    "NEW_ENGLAND_OROGEN": "NewEnglandOrogen",
    "NORTH_AUSTRALIAN_CRATON": "NorthAustralianCraton",
    "WANDILLA_PROVINCE": "WandillaProvince",
    "WHITSUNDAY_SILICIC_LARGE_IGNEOUS_PROVINCE": "WhitsundaySilicicLargeIgneousProvince",
    "WOOLOMIN_PROVINCE": "WoolominProvince",
    "YARROL_PROVINCE": "YarrolProvince",
}

g = Graph().parse("../qldgeofeatures.gso.ttl")

for o in g.objects(None, None):
    for k in changes.keys():
        if k in str(o):
            g.add(())



g.serialize(destination="../qldgeofeatures.gso.case.ttl")


    