import sys
sys.path.insert(0, './answers')
from answer import frequent_parks_count_df

def test_frequent_parks_count_df():
    a = frequent_parks_count_df("./data/frenepublicinjection2016.csv")

    try:
        out = open("tests/frequent.txt","r").read()
        assert(a == out)
    except:
        out = open("tests/frequent.txt","r", encoding="ISO-8859-1").read()
        assert(a == out)
