-- Problem 1
problem_1 = sum [x|x <- [1..999],x `mod` 3 == 0 || x `mod` 5 ==0]

-- Problem 2
problem_2 = sum [x|x <- f [1,1], even x]
    where
      f (x:x1:xs)
        | x >= 4000000 = x:x1:xs
        | otherwise = f (x+x1:x:x1:xs)

-- Problem 4
problem_4 = maximum [z|x<-[100..999],y<-[x..999],let z =x*y, show z == reverse( show z)]

-- Problem 5
problem_5 = foldl1 lcm [1..20]

-- Problem 6
problem_6 = sum[1..100]^2 - sum [x^2|x<-[1..100]]
