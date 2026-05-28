removeNonUppercase :: String -> String
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z'] ]

lucky :: (Integral a) => a -> String
lucky 7 = "WOW HOW LUCKY!"
lucky x = "Shit number, die"