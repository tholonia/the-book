import math

# N=1
# D=math.sqrt(2)
# C=2

N=6
D=2
C=3

print(f"Tri 0:")
CD=C*D
CN=D+(C*N)
ND=(D+N)*C

print(f"\tCD = {CD}")
print(f"\tCN = {CN}")
print(f"\tND = {ND}")


print(f"Tri 1:")
CD=C*(D+N)
CN=D-(C-N)
ND=N*C

print(f"\tCD = {CD}")
print(f"\tCN = {CN}")
print(f"\tND = {ND}")

print(f"Tri 2:")
CD=D+(N*C)
CN=N*D
ND=D+(N-C)

print(f"\tCD = {CD}")
print(f"\tCN = {CN}")
print(f"\tND = {ND}")

print(f"Tri 3:")
CD=C*D
CN=N*C
ND=N*D

print(f"\tCD = {CD}")
print(f"\tCN = {CN}")
print(f"\tND = {ND}")


