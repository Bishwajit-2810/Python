def movie_recommendation(x,y):
    new_list=[]
    for i in y:
        if i>6:
            new_list.append(x[y.index(i)])
    print(new_list)
movie_list=list(map(str,input().strip().split()))
rating_list=list(map(int,input().strip().split()))
movie_recommendation(movie_list,rating_list)