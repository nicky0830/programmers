def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    check = ["code", "date", "maximum", "remain"]
    filter_idx = check.index(ext)
    filtered = list(filter(lambda x: x[filter_idx] < val_ext, data))
    sort_idx = check.index(sort_by)
    filtered.sort(key=lambda x: x[sort_idx])
    return filtered
  


