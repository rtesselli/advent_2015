countParentheses :: String -> Int
countParentheses [] = 0
countParentheses (x:xs) = if x == '(' then 1 + countParentheses xs else -1 + countParentheses xs

indexBasement :: String -> Int -> Int -> Int
indexBasement [] _ _ = error "Basement never entered"
indexBasement (x:xs) floor position
  | floor == -1 = position
  | x == '(' = indexBasement xs (floor + 1) (position + 1)
  | otherwise = indexBasement xs (floor - 1) (position + 1)


main :: IO ()
main = do
  contents <- readFile "../data/day01.txt"
  print (countParentheses contents)
  print (indexBasement contents 0 0)
