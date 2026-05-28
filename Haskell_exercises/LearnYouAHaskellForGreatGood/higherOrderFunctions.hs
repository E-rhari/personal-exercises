compareWithHundred :: (Num a, Ord a) => a -> Ordering
compareWithHundred x = compare x 100

divedeByTen :: (Floating a) => a -> a
divedeByTen = (/10)

isUpperCase :: Char -> Bool
isUpperCase = (`elem` ['A'..'Z'])


applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)


zipWith' :: (a->b->c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys


flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f x y = f y x


map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x : map' f xs

map'' :: (a -> b) -> [a] -> [b]
map'' f xs = [f x | x <- xs] 


filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' p (x:xs)
    | p x       = x : filter' p xs
    | otherwise = filter' p xs

filter'' :: (a -> Bool) -> [a] -> [a]
filter'' p xs = [x | x <- xs, p x]


quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
    let smallerSorted = quicksort (filter' (<=x) xs)
        biggerSorted  = quicksort (filter' (>x)  xs)
    in smallerSorted ++ [x] ++ biggerSorted


largestDivisible :: (Integral a) => a -> [a] -> a
largestDivisible n xs = head (filter p xs)
    where p x = x `mod` n == 0

firstWord :: [Char] -> [Char]
firstWord sentence = takeWhile (/=' ') sentence

chain :: (Integral a) => a -> [a]
chain 1 = [1]
chain n
    | even n = n:chain (n `div` 2)
    | odd  n = n:chain (n*3 + 1)


numLongChains :: Int
numLongChains = length (filter (\xs -> length xs > 15) (map chain [1..100]))

sum' :: (Num a) => [a] -> a
sum' xs = foldl (\acc x -> acc + x) 0 xs

sum'' :: (Num a) => [a] -> a
sum'' = foldl (+) 0

product' :: (Num a) => [a] -> a
product' = foldl (*) 1


elem' :: (Eq a) => a -> [a] -> Bool
elem' y xs = foldl (\acc x -> if x == y then True else acc) False xs


map''' :: (a->b) -> [a] -> [b]
map''' f xs = foldr (\x acc -> f x : acc) [] xs

map'''' :: (a->b) -> [a] -> [b]
map'''' f xs = foldl (\acc x -> acc ++ [f x]) [] xs


maximum' :: (Ord a) => [a] -> a
maximum' = foldr1 (\x acc -> if x > acc then x else acc)

reverse' :: [a] -> [a]
reverse' = foldl (\acc x -> x : acc) []

head' :: [a] -> a
head' = foldr1 (\x _ -> x)


foldl' :: (a -> a -> a) -> a -> [a] -> a 
foldl' f acc [] = acc
foldl' f acc (x:xs) = foldl' f (f acc x) xs
-- (f (f (f acc x1) x2) x3) 

foldr' :: (a -> a -> a) -> [a] -> a -> a
foldr' f [] acc = acc
foldr' f (x:xs) acc = foldr' f xs (f x acc) 
-- (f x3 (f x2 (f x1 acc)))

($$) :: (a->b) -> a -> b -- doesn't work the same, for some reason
f $$ x = f x

(°) :: (b->c) -> (a->b) -> a -> c
(f ° g) x = f (g x)