size(200,200)

value = 0.5
m = remap(value, 0, 1, 0, width)
println(m)  # Prints "100.0"

value = 110
m = remap(value, 0, 100, -20, -10)
println(m)  # Prints "-9.0"
