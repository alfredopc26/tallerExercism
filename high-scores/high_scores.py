def latest(scores):
    
    return scores.pop()


def personal_best(scores):
    
    return max(scores)


def personal_top_three(scores):
    
    list_ = []
    
    scores.sort(reverse=True)

    for sc in scores:
        list_.append(sc)
        if len(scores) >= 3:
            if len(list_) == 3:
                return list_
        else:
            if len(list_) == len(scores):
                return list_
        
