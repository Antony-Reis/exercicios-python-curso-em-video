nums = []

for l in range(0,5):
    num = int(input(f'Insira o {l+1}° número: '))
    nums.append(num)
print(f'O maior número é {max(nums)} e está na {nums.index(max(nums))+1}° posição.\nO menor número é {min(nums)} e está na {nums.index(min(nums))+1}° posição.')