skin <- read.csv("skin.csv" , header = T)
skin <- skin[-1]
head(skin)
str(skin) 

x <- c("red","blue","blue","red","red") # 빨강공 3개, 파란공 2개 엔트로피 구하기 

#정보엔트로피를 구하는 함수 
info_entropy <- function(x) { 
  
  factor_x <- factor(x) 
  entropy <- 0 
  for(str in levels(factor_x)) {
      pro <- sum(x == str) / length(x) 
      entropy <- entropy - pro * log2(pro) 
  }
  return (entropy)
}

x

info_entropy(x)
#[1] 0.9709506

# 의사결정나무(decision tree)할 때 엔트로피가 감소하는 방향으로 가지치기를 해야 함 

skin
head(skin)

#주어진 데이터셋에 대하여 적용해 본 엔트로피 계산
#맨처음의 '쿠폰반응여부'의 엔트로피



first_entropy <- info_entropy(skin[, "쿠폰반응여부"])
first_entropy
# 0.9709506

for(str in colnames(skin)[1:5]) {     #  고객속성 정보 
    
    #str=조건변수 , factors=조건값집합
    factors <- levels(skin[[str]])
    #print(skin[str])
    #print(skin[[str]])
    #print(factors)
    
    #조건변수를 각각의 가능한 속성값으로 분류하였을때 '쿠폰반응여부'에 대한 엔트로피의 합계
    sum_entropy <- 0 
    for(str2 in factors) { 
      test_x <- skin[skin[[str]] == str2,][6]
      sum_entropy <- sum_entropy + info_entropy(test_x[,1])
      
      #print(str2)
      #print(test_x)
      #print(sum_entropy)
    }
    cat(str , '---->' , sum_entropy,'\n')
    
}

# 결혼여부가 엔트로피가 가장 적음 

#rpart() : 엔트로피에 의해서 가지치기를 해 줌으로써 decision tree를 자동으로 만들어 주는 함수 
library(rpart)  
tree1 <- rpart(쿠폰반응여부 ~ . , data = skin , control=rpart.control(minsplit = 2)) 
plot(tree1 , compress = T , uniform = T , margin=0.1) 
text(tree1 , use.n = T , col = "blue")
tree1

xtabs(~ 결혼여부 + 쿠폰반응여부 , data = skin)

#카이제곱 독립성검정으로 데이터분할하기 
chisq.test(xtabs(~ 결혼여부 + 쿠폰반응여부 , data = skin))


#지니계수를 구하는 함수 
info_gini <- function(x) { 
  
  factor_x <- factor(x) 
  gini_sum <- 0 
  for(str in levels(factor_x)) {
    pro <- sum(x == str) / length(x) 
    gini_sum <- gini_sum + pro^2
  }
  return (1 - gini_sum)
}

#새미의 데이터셋에 대하여 적용해 본 지니계수 계산
#맨처음의 '쿠폰반응여부'의 지니계수
first_gini <- info_gini(skin[,"쿠폰반응여부"])
first_gini
#0.48

for(str in colnames(skin)[1:5]) { 
  
  #str=조건변수 , factors=조건값집합
  factors <- levels(skin[[str]])
  
  #조건변수를 각각의 가능한 속성값으로 분류하였을때 '쿠폰반응여부'에 대한 엔트로피의 합계
  sum_gini <- 0 
  for(str2 in factors) { 
    test_x <- skin[skin[[str]] == str2,][6]
    sum_gini <- sum_gini + info_gini(test_x[,1])
  }
  cat(str , '---->' , sum_gini,'\n')
  
}

