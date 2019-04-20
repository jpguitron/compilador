.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
.text
.globl main
main:
li $a0 10
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $t3 48($sp)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 1
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 1
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 2
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 2
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 3
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 3
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 4
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 4
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 5
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 5
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 6
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 6
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 7
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 7
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 8
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t3 52($sp)
li $t0 2
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 48
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t3 52($sp)
li $t0 4
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 48
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t3 56($sp)
li $t0 1
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 52
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
div $a0 $t1
mflo $a0
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
mul $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
lw $t3 48($sp)
li $t0 1
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
sw $a0 0($t1)
lw $t3 48($sp)
li $t0 1
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t3 48($sp)
lw $t3 48($sp)
lw $t3 48($sp)
lw $t3 48($sp)
lw $t3 48($sp)
lw $t0 4($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
move $t0 $a0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
move $t0 $a0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
move $t0 $a0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
move $t0 $a0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 44
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
End:
li $v0, 10
syscall
Outbounds:
li $v0 4
la $a0 outbounds
syscall
j End
