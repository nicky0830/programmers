def solution(id_pw, db):
    answer = ''
    [id, pw] = id_pw
    for [db_id, db_pw] in db:
        if db_id == id: 
            if db_pw == pw:
                return "login"
            else: 
                return "wrong pw"
    return "fail"