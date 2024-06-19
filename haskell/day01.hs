countParentheses :: String -> Int
countParentheses [] = 0
countParentheses (x:xs) = if x == '(' then 1 + countParentheses xs else -1 + countParentheses xs

main :: IO ()
main = do
  contents <- readFile "../data/day01.txt"
  print(countParentheses contents)
