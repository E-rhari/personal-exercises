data Buul = Fake | Truthful

data Point = Point Float Float deriving (Show)

data Shape = Circle Point Float | Rectangle Point Point 
    deriving (Show)


surface :: Shape -> Float
surface (Circle _ r) = pi * r^2
surface (Rectangle (Point x1 y1) (Point x2 y2)) = (abs $ x2 - x1) * (abs $ y2 - y1) 

cocentricCircles :: Point -> [Float] -> [Shape]
cocentricCircles point@(Point x y) (r:rs) = map (Circle point) (r:rs)

nudge :: Shape -> Float -> Float -> Shape
nudge (Circle (Point x y) r) a b = Circle (Point (x+a) (y+b)) r
nudge (Rectangle (Point x1 y1) (Point x2 y2)) a b = Rectangle (Point (x1+a) (y1+b)) (Point (x2+a) (y2+b))


baseCircle :: Float -> Shape
baseCircle r = Circle (Point 0 0) r

baseRect :: Float -> Float -> Shape
baseRect width height = Rectangle (Point 0 0) (Point width height)


data Person = Person { firstName :: String  
                     , lastName :: String  
                     , age :: Int  
                     , height :: Float  
                     , phoneNumber :: String  
                     , flavor :: String  
                     } deriving (Show)  

data Car = Car {company :: String, 
                model :: String, 
                year :: Int} deriving (Show)  

tellCar :: Car -> String
tellCar (Car {company=c, model=m, year=y}) = "This " ++ c ++ " " ++ m ++ " was made in " ++ show y

data Possibly a = Absence | Simply a deriving (Show)


data Vector a = Vector a a a deriving (Show)

vplus :: (Num t) => Vector t -> Vector t -> Vector t
(Vector i j k) `vplus` (Vector l m n) = Vector (i+l) (j+m) (k+n)

vmult :: (Num t) => Vector t -> t -> Vector t
(Vector i j k) `vmult` s = Vector (i*s) (j*s) (k*s)

(°) :: (Num t) => Vector t -> Vector t -> t
(Vector i j k) ° (Vector l m n) = i*l + j*m + k*n



data Person' = Person'  { firstName' :: String
                        , lastName' :: String
                        , age' :: Int
                        } deriving (Eq, Show, Read)


data Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun
    deriving (Eq, Ord, Show, Read, Bounded, Enum)


type PhoneNumber = String
type Name = String
type PhoneBook = [(Name, PhoneNumber)]

inPhoneBook :: Name -> PhoneNumber -> PhoneBook -> Bool
inPhoneBook name pnumber pbook = (name, pnumber) `elem` pbook

type AssocList k v = [(k,v)]


infixr 5 :-:
data List a = Empty | a :-:(List a) deriving (Read, Eq, Ord)


infixr 5 .++
(.++) :: List a -> List a -> List a 
Empty  .++ ys = ys
(x:-:xs) .++ ys = x :-: (xs.++ys) 

data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)



singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree

treeInsert :: (Ord a) => a -> Tree a -> Tree a
treeInsert x EmptyTree = singleton x
treeInsert x (Node a left right)
    | x == a = Node x left right
    | x < a  = Node a (treeInsert x left) right
    | x > a  = Node a left (treeInsert x right) 

treeElem :: (Ord a) => a -> Tree a -> Bool
treeElem x EmptyTree = False
treeElem x (Node a left right) 
    | x == a = True
    | x < a  = treeElem x left
    | x > a  = treeElem x right


class Eq' a where
    (.==) :: a -> a -> Bool
    (./=) :: a -> a -> Bool
    x .== y = not (x ./= y)
    x ./= y = not (x .== y)

data TrafficLight = Red | Yellow | Green

instance Eq TrafficLight where
    Red    == Red       = True
    Green  == Green     = True
    Yellow == Yellow    = True
    _ == _              = False

instance Show TrafficLight where
    show Red = "Red Light"
    show Green = "Green Light"
    show Yellow = "Yellow Light"

instance (Eq m) => Eq (Possibly m) where
    Simply x == Simply y = x == y
    Absence == Absence = True
    _ == _ = False


class YesNo a where
    yesno :: a -> Bool

instance YesNo Int where
    yesno 0 = False
    yesno _ = True
instance YesNo [a] where
    yesno [] = False
    yesno _ = True
instance YesNo Bool where
    yesno = id
instance YesNo (Maybe a) where
    yesno Nothing = False
    yesno (Just _) = True
instance YesNo (Tree a) where
    yesno EmptyTree = False
    yesno _ = True
instance YesNo TrafficLight where
    yesno Red = False
    yesno _ = True

yesnoIf :: (YesNo y) => y -> a -> a -> a
yesnoIf yesnoVal yesResult noResult = if yesno yesnoVal then yesResult else noResult


class Functor' f where
    fmap' :: (a->b) -> f a -> f b

instance Functor' List where
    fmap' _ Empty = Empty
    fmap' f (x:-:xs) = (f x) :-: (fmap' f xs)
instance (Show a) => Show (List a) where
    show Empty = ""
    show (x:-:Empty) = show x ++ "."
    show (x:-:xs) = show x ++ ", " ++ show xs 

instance Functor' Maybe where
    fmap' f (Just x) = Just (f x)
    fmap' f Nothing = Nothing

instance Functor' Tree where
    fmap' f EmptyTree = EmptyTree
    fmap' f (Node x left right) = Node (f x) (fmap' f left) (fmap' f right) 


data Either' a b = Left' a | Right' b 

instance Functor' (Either' a) where
    fmap' f (Right' x) = Right' (f x)
    fmap' f (Left' x) = Left' x