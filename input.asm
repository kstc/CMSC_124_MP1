begin
read N
pushv N
pushi 2
mod
pushi 0
jeq even
pushi 0
pop ans
jmp stop
even:
pushi 1
pop ans
stop:
disp ans
end