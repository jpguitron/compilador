.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
inp: .asciiz "Entrada: "
.text
.globl main
gcd:
move $fp $sp
sw $ra 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
seq $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero elsestatement1
lw $a0 8($sp)
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
j endif1
elsestatement1:
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 16($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 24($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
div $a0 $t1
mflo $a0
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 24($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
mul $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
sub $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 20($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal gcd
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
endif1:
addiu $sp $sp 0
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
main:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
sw $a0 8($sp)
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
sw $a0 4($sp)
sw $fp 0($sp)
addiu $sp $sp -4
lw $a0 8($sp)
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 16($sp)
sw $a0 0($sp)
addiu $sp $sp -4
jal gcd
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
