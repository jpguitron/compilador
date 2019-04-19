.text
.globl main
main:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
li $a1 2
sw $a1, 0($sp)
addiu $sp $sp -4
lw $a0, 4($sp)
lw $a1, 8($sp)
add $a0 $a0 $a1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 12($sp)
li $a0 5
sw $a0, 0($sp)
addiu $sp $sp -4
li $a1 5
sw $a1, 0($sp)
addiu $sp $sp -4
lw $a0, 4($sp)
lw $a1, 8($sp)
add $a0 $a0 $a1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 4($sp)
sw $a0 8($sp)
li $a0 5
sw $a0, 0($sp)
addiu $sp $sp -4
li $a1 5
sw $a1, 0($sp)
addiu $sp $sp -4
lw $a0, 4($sp)
lw $a1, 8($sp)
add $a0 $a0 $a1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
li $v0 1
lw $a0 16($sp)
syscall
li $v0 1
lw $a0 12($sp)
syscall
li $v0 1
lw $a0 8($sp)
syscall
li $v0, 10
syscall
