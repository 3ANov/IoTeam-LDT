import pymongo
import json

client = pymongo.MongoClient('localhost', 27017)
db = client.hktkru
series_collection = db.hktkru

# a = db.hkt.find({"name" : "г.о. Щербинка - ул. Кирова"}, {"geometry": 1, "_id": 0 })
# a = db.hkt.find({}, {"name": 1, "_id": 0})


geo11 = '{"type": "FeatureCollection", "features": ['
end12 = ']}'
geo21 = '{ "type": "Feature","geometry": '
prp21 = '"properties": '
end22 = '},'


def data_out_v(key):
    a = db.hkt.find({}, {key: 1, "_id": 0})
    with open(key+".json", "a") as f:
        for i in a:
            for k, v in i.items():
                f.write(v + "\n")


def data_out_kv(key):
    a = db.hkt.find({}, {key: 1, "_id": 0})
    with open(key+".json", "a") as f:
        for i in a:
            f.write(json.dumps(i, ensure_ascii=False)+"\n")


def data_prn_geo(key):
    a = db.hkt.find({}, {key: 1, "_id": 0}).limit(20)
    for i in a:
        #        print(geo)
        for k, v in i.items():
            print(json.dumps(v, ensure_ascii=False))


def data_prn(key):
    a = db.hkt.find({}, {key: 1, "_id": 0}).limit(2)
    for i in a:
        for v in i.items():
            print(v)


def data_out1(key):
    a = db.hkt.find({}, {key: 1, "_id": 0}).limit(20)
    with open(key+".json", "a") as f:
        for i in a:
            for k, v in i.items():
                f.write(json.dumps(v, ensure_ascii=False)+"\n")


def data_out(key):
    a = db.hkt.find({}, {key: 1, "calc_attribute": 1, "_id": 0}).limit(6500)

    #a = db.hkt.find({}, {key: 1, "_id": 0})

    with open(key+".json", "w") as f:
        f.write(geo11 + "\n")
        for i in a:
#            f.write(geo21 + "\n")
            for k, v in i.items():
                if k == "geometry":
                    f.write(geo21 + json.dumps(v, ensure_ascii=False) + ',' + "\n")
                elif k == "calc_attribute":
                    f.write(prp21 +json.dumps(v, ensure_ascii=False) + '},' + "\n")
        f.write(end12 + "\n")


data_out("geometry")
#data_prn("calc_attribute")
