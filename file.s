.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
.text
.globl main
perro:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $a0 8($sp)
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
perr:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $t1 8($sp)
lw $t3 0($t1)
li $t0 5
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 100
sw $a0 0($t1)
lw $t1 8($sp)
lw $t3 0($t1)
li $t0 10
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 5
sw $a0 0($t1)
li $a0 10
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1 12($sp)
lw $t3 0($t1)
li $t0 5
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
sw $fp 0($sp)
addiu $sp $sp -4
lw $t1 16($sp)
lw $t3 0($t1)
li $t0 10
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0 0($sp)
addiu $sp $sp -4
jal perro
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
lw $ra 4($sp)
addiu $sp $sp 12
lw $fp 0($sp)
jr $ra
main:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 11
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
sw $fp 0($sp)
addiu $sp $sp -4
move $a0 $sp
addiu $a0 $a0 52
sw $a0 0($sp)
addiu $sp $sp -4
jal perr
sw $a0 60($sp)
lw $a0 60($sp)
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
