.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
.text
.globl main
can:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $t1 8($sp)
lw $t3 4($t1)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t1 12($sp)
lw $t3 4($t1)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t1 8($sp)
lw $t3 4($t1)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1 16($sp)
lw $t3 4($t1)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
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
addiu $sp $sp 4
lw $t1 12($sp)
lw $t3 4($t1)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
sw $a0 0($t1)
lw $t1 12($sp)
lw $t3 4($t1)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
perro:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $t1 8($sp)
lw $t3 4($t1)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 69
sw $a0 0($t1)
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
main:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 3
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
lw $t3 16($sp)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 12
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 1000
sw $a0 0($t1)
sw $fp 0($sp)
addiu $sp $sp -4
li $a0 100
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 $a0 20
sw $a0 0($sp)
addiu $sp $sp -4
jal perro
sw $fp 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 $a0 16
sw $a0 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 $a0 20
sw $a0 0($sp)
addiu $sp $sp -4
jal can
lw $t3 16($sp)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 12
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
sw $a0 0($t1)
lw $t3 16($sp)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 12
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 100
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t3 16($sp)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 12
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
