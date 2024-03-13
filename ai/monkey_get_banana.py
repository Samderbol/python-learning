i=0
def Monkey_go_box(x,y):
    global i
    i=i+1
    print('step:{},monkey从{}走到{}'.format(i,x,y))      #print('step:',i,'monkey从',x,'走到'+y)
def Monkey_move_box(x,y):
    global ia
    i=i+1
    print('step:',i,'monkey把箱子从',x,'移动到'+y)
def Monkey_on_box():
    global i
    i=i+1
    print('step:',i,'monkey爬上箱子')
def Monkey_get_banana():
    global i
    i=i+1
    print('step:',i,'monkey摘到香蕉')
print('请用a，b，c来表示猴子箱子香蕉的位置：')
print('monkey\tbox\tbanana\n')
monkey=input('')
box=input('')
banana=input('')
if monkey!=box:
    Monkey_go_box(monkey,box)
if box!=banana:
    Monkey_move_box(box,banana)
Monkey_on_box()
Monkey_get_banana()
