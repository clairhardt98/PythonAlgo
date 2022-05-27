def solution(board, moves):
    basket=[0]
    score=0


    for i in range(0,len(moves)):
        for j in range(0,len(board)):
            if board[j][moves[i]-1]!=0:
                basket.append(board[j][moves[i]-1])
                if basket[-1]==basket[-2]:
                    basket.pop()
                    basket.pop()
                    score+=2
                board[j][moves[i]-1]=0
                break
    return score

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]	
solution(board,moves)