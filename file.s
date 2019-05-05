.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
inp: .asciiz "Entrada: "
.text
.globl main
gdc:
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
beq $a0 $zero elsestatement0
lw $a0 8($sp)
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
j endif0
elsestatement0:
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
jal gdc
move $sp $fp
addiu $sp $sp -4
lw $ra 4($sp)
addiu $sp $sp 16
lw $fp 0($sp)
jr $ra
addiu $sp $sp 0
endif0:
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
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
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
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
sw $a0 48($sp)
lw $t3 44($sp)
li $t0 1
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 40
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
li $a0 1
sw $a0 0($t1)
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
sw $a0 56($sp)
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
sw $a0 52($sp)
li $a0 0
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
addiu $sp $sp 4
beq $a0 $zero elsestatement1
lw $a0 56($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 56($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
mul $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 56($sp)
addiu $sp $sp 0
j endif1
elsestatement1:
lw $a0 56($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 56($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
add $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
sw $a0 56($sp)
addiu $sp $sp 0
endif1:
lw $a0 56($sp)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
li $a0 0
sw $a0 56($sp)
li $a0 5
sw $a0 48($sp)
lw $a0 56($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $a0 52($sp)
sw $a0, 0($sp)
addiu $sp $sp -4
lw $t1, 4($sp)
lw $a0, 8($sp)
slt $a0 $a0 $t1
addiu $sp $sp 8
sw $a0, 0($sp)
addiu $sp $sp -4
addiu $sp $sp 4
whilestatement0:
beq $a0 $zero endwhile0
li $v0 4
la $a0 inp
syscall
addi $v0 , $0 , 5 
syscall
move $a0 , $v0
lw $t3 44($sp)
lw $t0 56($sp)
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 40
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
sw $a0 0($t1)
lw $a0 56($sp)
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
sw $a0 56($sp)
addiu $sp $sp 0
j whilestatement0
endwhile2:
lw $t3 44($sp)
li $t0 0
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 40
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t3 44($sp)
li $t0 1
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 40
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t3 44($sp)
li $t0 2
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 40
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t3 44($sp)
li $t0 3
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 40
li $t2 4
mul $t0 $t0 $t2
sub $t1 $t1 $t0
lw $a0 0($t1)
li $v0 1
syscall
li $v0 4
la $a0 newline
syscall
lw $t3 44($sp)
li $t0 4
blt $t0 $zero Outbounds
bge $t0 $t3 Outbounds
move $t1 $sp
addiu $t1 $t1 40
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
