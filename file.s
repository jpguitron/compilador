.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
inp: .asciiz "Entrada: "
.space 24
arr: .word 0
.text
.globl main
bubbleSort:
move $fp $sp
sw $ra 0($sp)
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
sw $a0 8($sp)
li $a0 0
sw $a0 12($sp)
whilestatement1:
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 28($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
sub $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
slt $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero endwhile1
whilestatement2:
lw $a0 8($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 28($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
sub $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
sub $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
slt $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero endwhile2
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 4($sp)
lw $t1 24($sp)
lw $t3 4($t1)
lw $t0 12($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1 28($sp)
lw $t3 4($t1)
lw $t0 8($sp)
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
sgt $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero elsestatement1
lw $t1 24($sp)
lw $t3 4($t1)
lw $t0 12($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
sw $a0 8($sp)
lw $t1 24($sp)
lw $t3 4($t1)
lw $t0 4($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
lw $t1 24($sp)
lw $t3 4($t1)
lw $t0 12($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
sw $a0 0($t1)
lw $a0 8($sp)
lw $t1 24($sp)
lw $t3 4($t1)
lw $t0 4($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
sw $a0 0($t1)
addiu $sp $sp 0
j endif1
elsestatement1:
endif1:
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 12($sp)
addiu $sp $sp 4
j whilestatement2
endwhile2:
li $a0 0
sw $a0 8($sp)
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 12($sp)
addiu $sp $sp 0
j whilestatement1
endwhile1:
addiu $sp $sp 12
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
main:
la $a0 arr
li $t0, 5
sw $t0 0($a0)
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 5
sw $a0 8($sp)
li $a0 0
sw $a0 4($sp)
whilestatement3:
lw $a0 4($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
slt $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero endwhile3
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
la $t1 arr
lw $t3 0($t1)
addiu $t1 $t1 -4
lw $t0 4($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
sw $a0 0($t1)
lw $a0 4($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 4($sp)
addiu $sp $sp 0
j whilestatement3
endwhile3:
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0 0($sp)
addiu $sp $sp -4
la $a0 arr
addiu $a0 $a0 -4
sw $a0 0($sp)
addiu $sp $sp -4
jal bubbleSort
li $a0 0
sw $a0 4($sp)
whilestatement4:
lw $a0 4($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
slt $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero endwhile4
la $t1 arr
lw $t3 0($t1)
addiu $t1 $t1 -4
lw $t0 4($sp)
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
lw $a0 4($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 4($sp)
addiu $sp $sp 0
j whilestatement4
endwhile4:
End:
li $v0, 10
syscall
Outbounds:
li $v0 4
la $a0 outbounds
syscall
j End
