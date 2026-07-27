#Advance Recursion
#Generate Parenthesis

def generate_parentheses(n):
  ind = 0
  total = 0
  brackets = [""]*n*2
  result = []
  def solve(ind, total):
    if ind >= len(brackets):
      if total == 0:
        result.append("".join(brackets))
      return
    if total>len(brackets)//2:
      return
    elif total < 0:
      return
    brackets[ind] = "("
    sum = total+1
    solve(ind+1, sum)
    brackets[ind] = ")"
    sum = total -1
    solve(ind+1, sum)

  solve(ind, total)
  return result

print(generate_parentheses(3))


