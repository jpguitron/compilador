.data
newline: .asciiz "
"
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
li $a0 2
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $a1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 12($sp)
li $a0 9
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 3
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a1, 4($sp)
lw $a0, 8($sp)
div $a0 $a1
mflo $a0
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 4
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a1, 4($sp)
lw $a0, 8($sp)
sub $a0 $a0 $a1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 4
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a1, 4($sp)
lw $a0, 8($sp)
sub $a0 $a0 $a1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a1, 4($sp)
lw $a0, 8($sp)
mul $a0 $a0 $a1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 8($sp)
lw $a0 8($sp)
sw $a0 4($sp)
li $v0 1
lw $a0 12($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
lw $a0 8($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0 1
lw $a0 4($sp)
syscall
li $v0 4
la $a0 newline
syscall
li $v0, 10
syscall
