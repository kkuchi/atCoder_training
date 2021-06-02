a,b = parse.(Int, split(readline()))

if a * b %2 == 0
    print("Even")
else
    print("Odd")
end