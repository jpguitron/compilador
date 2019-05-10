.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
inp: .asciiz "Entrada: "
a: .word 4
.text
.globl main
main:
li $a0 0
la $a2 a
sw $a0 0($a2)
whilestatement1:
lw $a0 a
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 5
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
lw $a0 a
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $a0 a
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
sw $a0 a
addiu $sp $sp 0
j whilestatement1
endwhile1:
End:
li $v0, 10
syscall
Outbounds:
li $v0 4
la $a0 outbounds
syscall
j End
