academy <- read.csv("academy.csv" , stringsAsFactors = F , header = T)
academy <- academy[-1] #학생번호 속성 삭제
head(academy)

# 유클리디언 거리 구하기 
dist_academy <- dist(academy , method = "euclidean")
dist_academy

# 속성정보 : 5개 (5차원) >> 차원 축소 : 2차원 
two_coord <- cmdscale(dist_academy)
plot(two_coord , type = "n") # 번호 : 학생들 
text(two_coord , as.character(1:52))
# cmdscale 함수 이용, 2차원 좌표계로 변환 
# 다차원 척도법 : 여러 속성(다차원)을 저차원으로 변환 

# food 정보 
# 긍정 1, 무응답 0, 부정 -1

food <- read.csv("food.csv" , stringsAsFactors = F , header = T)
food <- food[-1] # 고객정보 속성 삭제 
head(food) 

#잘못된 방법 : 같은 속성일 때도 0, 무응답일 때도 0 이 됨
dist(t(food) , method = "euclidean") # t(): transpose 전치 행렬   

#옳은 방법 : 같은속성 끼리 곱하면 1, 다른 속성끼리 곱하면 -1, 무응답 0 되게 변환 
food.mult <- t(as.matrix(food)) %*% as.matrix(food) # matrix 간의 곱: matrix와 전치행렬 서로 곱하는 것 
food.mult
# 해석
# - 가 붙었다 : 거리가 멀다 
# + 가 많다 : 거리가 가깝다 


dist.food <- dist(food.mult)
dist.food

two_coord2 <- cmdscale(dist.food)
plot(two_coord2 , type = "n")
text(two_coord2 , rownames(food.mult))

