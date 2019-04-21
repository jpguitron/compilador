.data
newline: .asciiz "
"
outbounds: .asciiz "Variable fuera del indice: runtime error 
"
.text
.globl main
main:
li $a0 0
sw $a0 0($sp)
addiu $sp $sp -4
