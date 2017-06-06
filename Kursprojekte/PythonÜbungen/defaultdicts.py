import collections


if __name__ == '__main__':
    freunde = collections.defaultdict(list)
    print freunde["Susi"].append("Robert")
    print freunde["Susi"].append("Benni")
    print freunde["Benni"].append("Susi")
    print freunde["Robert"].extend(["Benni", "Tobi"])
    for k, v in freunde.iteritems():
        print k, v