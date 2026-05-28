factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n-1)

addVectors :: (Num a) => (a,a) -> (a,a) -> (a,a)
addVectors a b = (fst a + fst b, snd a + snd b) -- bad and stinky

addVectors' :: (Num a) => (a,a) -> (a,a) -> (a,a)
addVectors' (x1, y1) (x2, y2) = (x1+x2, y1+y2) -- cool and epic


tripleFirst :: (a,b,c) -> a
tripleFirst (x, _, _) = x

tripleSecond :: (a,b,c) -> b
tripleSecond (_, y, _) = y

tripleThird :: (a,b,c) -> c
tripleThird (_, _, z) = z


sumList :: (Num a) => [a] -> a
sumList []     = 0
sumList (h:t)  = h + sumList t


capital :: String -> String
capital "" = "Damn dude that's empty"
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]
-- capital (x:xs) = "The first letter of " ++ x:xs ++ " is " ++ x


densityTell :: (RealFloat a) => a -> a -> String
densityTell mass volume
    | density <  air   = "Soaring through the sky"
    | density <= water = "Afloat"
    | otherwise        = "Sinkin'"
    where density = mass / volume
          air = 1.2
          water = 1000.0

initials :: String -> String -> String
initials firstName lastName = [f] ++ ". " ++ [l] ++ "."
    where (f:_) = firstName
          (l:_) = lastName


calcDensities :: (RealFloat a) => [(a,a)] -> [a]
calcDensities xs = [density m v | (m,v) <- xs]
    where density mass volume = mass / volume

calcDensities2 :: (RealFloat a) => [(a,a)] -> [a]
calcDensities2 xs = [m/v | (m,v) <- xs]

calcDensities3 :: (RealFloat a) => [(a, a)] -> [a]  
calcDensities3 xs = [density | (m, v) <- xs, let density = m / v, density < 1.2]


cylinder :: (RealFloat a) => a -> a -> a
cylinder r h = 
    let sideArea = 2 * pi * r * h
        topArea  = pi * r^2
    in sideArea + 2*topArea
