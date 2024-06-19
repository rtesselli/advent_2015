main :: IO ()
main = do
  contents <- readFile "../data/day01.txt"
  putStrLn contents