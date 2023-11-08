# 시간초과
def solution(players, callings):
    for i, j in enumerate(callings):
        target_idx = players.index(j)
        switch_idx = target_idx - 1
        players[target_idx], players[switch_idx] = players[switch_idx], players[target_idx]
    return players

# Dictionary 사용 => 시간초과
def solution(players, callings):
    players_dict = {idx:player for idx, player in enumerate(players)}
    
    for calling in callings:
        rank = players.index(calling)
        players_dict[rank - 1], players_dict[rank] = players_dict[rank], players[rank - 1]
        players = list(players_dict.values())
    return players

# .index 사용하지 않기
def solution(players, callings):
    players_dict = {player:idx for idx, player in enumerate(players)}
    
    for calling in callings:
        current_rank = players_dict[calling]
        pre_current_rank = current_rank - 1
        
        players_dict[calling] = pre_current_rank
        players_dict[players[pre_current_rank]] = current_rank
        
        players[current_rank], players[pre_current_rank] = players[pre_current_rank], players[current_rank]
        
    return players


'''
1. dictionary comprehension 사용 -> dictionary 만들기

2. .index 사용 X
.index 사용 -> 처음부터 하나씩 돌면서 값을 찾기 때문에 느린거 같다
dictionary를 이용해서 index를 먼저 뽑고 그것을 통해 list value를 서로 교환하면 빠르다
'''
