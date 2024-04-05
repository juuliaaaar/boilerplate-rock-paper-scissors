def player(prev_pl, opp_hist=[], pl_ord={}):

    if not prev_pl:
        prev_pl = 'S'

    opp_hist.append(prev_pl)
    pred = 'R'

    if len(opp_hist)>4:
        last = "".join(opp_hist[-5:])
        pl_ord[last] = pl_ord.get(last, 0) + 1
        
        pot_pl = ["".join([*opp_hist[-4:], v]) for v in ['R', 'P', 'S']]

        sub_ord = {k: pl_ord[k] for k in pot_pl if k in pl_ord}

        if sub_ord:
            pred = max(sub_ord, key=sub_ord.get)[-1:]

    ideal_res = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_res[pred]