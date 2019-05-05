.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
inp: .asciiz "Entrada: "
.text
.globl main
perro:
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
li $a0 100
sw $a0 8($sp)
whilestatement0:
lw $a0 12($sp)
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
beq $a0 $zero endwhile0
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
lw $a0 8($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 2
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
sle $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero elsestatement1
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
seq $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero elsestatement2
li $a0 79
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
j endif2
elsestatement2:
li $a0 1
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 0
endif2:
li $a0 69
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra
addiu $sp $sp 4
j endif1
elsestatement1:
li $a0 3
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 0
endif1:
lw $a0 16($sp)
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
sw $a0 16($sp)
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
sw $a0 12($sp)
lw $a0 12($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 2
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
sle $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero elsestatement3
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
lw $a0 16($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
li $a0 1
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
seq $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
beq $a0 $zero elsestatement4
li $a0 79
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
j endif4
elsestatement4:
li $a0 1
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 0
endif4:
li $a0 69
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra
addiu $sp $sp 4
j endif3
elsestatement3:
li $a0 3
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 0
endif3:
lw $a0 20($sp)
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
sw $a0 20($sp)
addiu $sp $sp 8
j whilestatement0
endwhile0:
li $a0 1
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra
addiu $sp $sp 12
lw $ra 4($sp)
addiu $sp $sp 8
lw $fp 0($sp)
jr $ra
main:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 34
sw $a0 4($sp)
li $a0 10
sw $a0 8($sp)
lw $a0 8($sp)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
sw $fp 0($sp)
addiu $sp $sp -4
jal perro
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
lw $a0 8($sp)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
li $a0 10002
sw $a0 4($sp)
lw $a0 4($sp)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
addiu $sp $sp 4
lw $a0 4($sp)
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
