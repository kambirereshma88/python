"""
 1.Define Variables?

 Variable is a container to store values.  They are reference to a memory location which is used to store value.
 They are also called Identifiers.


2. difference between snake_case and camelcase.

snake_case: Words are separated by underscores, and all letters are lowercase.
For example: my_variable_name.

camelCase: Words are joined without spaces, and each word except the first begins with a capital letter.
For example: myVariableName.

3.what is meant by Integer division?

Integer division refers to the division operation where both the dividend and the divisor are integers,
and the result is also an integer. Any fractional part of the result is discarded,
so the result is the integer quotient of the division.

"""

#4.Program to exchange the values of two numbers with and without using temporary variables:

#with temporary variable
a=5
b=10

temp = a
a=b
b=temp

print("a=",a)
print("b=",b)

#without temporary variables
a=5
b=10

a=a+b
b=a-b
a=a-b

print("a=",a)
print("b=",b)





#5. Write a program to accept a string value via user input and display the same .

user_input=input("Enter a string:")
print("you entered:", user_input)




#6.Program to find the avag marks for three subjects:

sub1=float(input("marks for sub1:"))
sub2=float(input("marks for sub2:"))
sub3=float(input("marks for sub3:"))


avg_marks = (sub1 + sub2 + sub3) / 3
print("avg_marks:" , avg_marks)


