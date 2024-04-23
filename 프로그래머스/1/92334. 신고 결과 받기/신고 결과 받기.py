def solution(id_list, report, k):
    answer = []
    reported = {id:[] for id in id_list}
    reporters = [0] * len(id_list)
    for r in list(set(report)):
        reporter, reportee = r.split(" ")
        reported[reportee].append(reporter)
    for key,val in reported.items():
        if len(val) >=k:
            for v in val:
                reporters[id_list.index(v)] += 1
    return reporters